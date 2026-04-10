from __future__ import annotations

import importlib
import re
import zlib
import zipfile
from pathlib import Path
from typing import Iterable, Sequence
from xml.etree import ElementTree

DEFAULT_ENCODINGS = ("utf-8-sig", "utf-8", "gb18030", "gbk", "gb2312", "utf-16", "big5", "latin-1")
TEXT_SUFFIXES = {".md", ".txt", ".log", ".csv", ".json", ".yaml", ".yml", ".srt", ".text", ""}
SUPPORTED_INPUT_SUFFIXES = TEXT_SUFFIXES | {".doc", ".docx", ".pdf"}


class DocumentReadError(RuntimeError):
    pass


def read_document_text(path: Path, encodings: Sequence[str] | None = None) -> tuple[str, str]:
    encodings = tuple(encodings or DEFAULT_ENCODINGS)
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return read_docx_file(path)
    if suffix == ".pdf":
        return read_pdf_file(path)
    if suffix == ".doc":
        return read_doc_file(path, encodings)
    return read_plain_text_file(path, encodings)


def read_plain_text_file(path: Path, encodings: Sequence[str]) -> tuple[str, str]:
    raw = read_bytes(path)
    if raw.count(b"\x00") / max(len(raw), 1) > 0.05:
        raise DocumentReadError(f"文件看起来像二进制，无法按文本处理: {path}")
    for encoding in encodings:
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    raise DocumentReadError(f"无法用常见编码解析文件: {path}")


def read_docx_file(path: Path) -> tuple[str, str]:
    mammoth_text = try_read_docx_with_mammoth(path)
    if mammoth_text:
        return mammoth_text, "docx/mammoth"

    try:
        with zipfile.ZipFile(path) as archive:
            parts = ordered_docx_parts(archive.namelist())
            chunks = [extract_docx_xml_text(archive.read(name)) for name in parts]
    except zipfile.BadZipFile as exc:
        raise DocumentReadError(f"DOCX 文件损坏或不是合法 zip 包: {path}") from exc
    except OSError as exc:
        raise DocumentReadError(f"无法读取 DOCX 文件: {path} ({exc})") from exc

    text = normalize_extracted_text("\n".join(chunks))
    if not text:
        raise DocumentReadError(f"DOCX 中没有提取到可用文本: {path}")
    return text, "docx/xml"


def read_pdf_file(path: Path) -> tuple[str, str]:
    text = try_read_pdf_with_library(path)
    if text:
        return text, "pdf/library"

    raw = read_bytes(path)
    text = extract_pdf_text_fallback(raw)
    if text:
        return text, "pdf/fallback"

    raise DocumentReadError(
        f"PDF 中没有提取到可用文本: {path}。当前仅支持可复制文本的 PDF，不支持扫描件或缺少文本层的 PDF。"
    )


def read_doc_file(path: Path, encodings: Sequence[str]) -> tuple[str, str]:
    raw = read_bytes(path)
    text = extract_doc_text_fallback(raw, encodings)
    if text:
        return text, "doc/fallback"
    raise DocumentReadError(
        f"DOC 中没有提取到可用文本: {path}。当前为 best-effort 提取，复杂旧版 Word 文档建议先另存为 .docx。"
    )


def read_bytes(path: Path) -> bytes:
    try:
        raw = path.read_bytes()
    except FileNotFoundError as exc:
        raise DocumentReadError(f"输入文件不存在: {path}") from exc
    except OSError as exc:
        raise DocumentReadError(f"无法读取输入文件: {path} ({exc})") from exc
    if not raw:
        raise DocumentReadError(f"输入文件为空: {path}")
    return raw


def try_read_docx_with_mammoth(path: Path) -> str:
    try:
        mammoth = importlib.import_module("mammoth")
    except ImportError:
        return ""
    try:
        with path.open("rb") as handle:
            result = mammoth.extract_raw_text(handle)
    except Exception:
        return ""
    return normalize_extracted_text(result.value)


def ordered_docx_parts(names: Iterable[str]) -> list[str]:
    names = set(names)
    ordered: list[str] = []
    preferred = ["word/document.xml", "word/comments.xml", "word/footnotes.xml", "word/endnotes.xml"]
    for name in preferred:
        if name in names:
            ordered.append(name)
    ordered.extend(sorted(name for name in names if re.fullmatch(r"word/header\d+\.xml", name)))
    ordered.extend(sorted(name for name in names if re.fullmatch(r"word/footer\d+\.xml", name)))
    return ordered


def extract_docx_xml_text(payload: bytes) -> str:
    try:
        root = ElementTree.fromstring(payload)
    except ElementTree.ParseError:
        return ""

    paragraphs: list[str] = []
    for node in root.iter():
        if local_name(node.tag) != "p":
            continue
        parts: list[str] = []
        for child in node.iter():
            name = local_name(child.tag)
            if name == "t" and child.text:
                parts.append(child.text)
            elif name == "tab":
                parts.append("\t")
            elif name in {"br", "cr"}:
                parts.append("\n")
        paragraph = normalize_extracted_text("".join(parts))
        if paragraph:
            paragraphs.append(paragraph)
    return "\n".join(paragraphs)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def try_read_pdf_with_library(path: Path) -> str:
    for module_name in ("pypdf", "PyPDF2"):
        try:
            module = importlib.import_module(module_name)
        except ImportError:
            continue
        try:
            reader = module.PdfReader(str(path))
            pages = [page.extract_text() or "" for page in reader.pages]
        except Exception:
            continue
        text = normalize_extracted_text("\n".join(pages))
        if text:
            return text
    return ""


def extract_pdf_text_fallback(raw: bytes) -> str:
    text_blocks: list[str] = []
    for payload in iter_pdf_stream_payloads(raw):
        for candidate in decode_pdf_payloads(payload):
            extracted = extract_pdf_operators_text(candidate)
            if extracted:
                text_blocks.append(extracted)
    if not text_blocks:
        text_blocks.extend(extract_textish_runs(raw.decode("latin-1", errors="ignore"), min_len=12))
    return normalize_extracted_text("\n".join(text_blocks))


def iter_pdf_stream_payloads(raw: bytes) -> Iterable[bytes]:
    for match in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", raw, flags=re.S):
        yield match.group(1).strip(b"\r\n")


def decode_pdf_payloads(payload: bytes) -> list[bytes]:
    candidates = [payload]
    try:
        inflated = zlib.decompress(payload)
    except Exception:
        inflated = b""
    if inflated:
        candidates.append(inflated)
    return candidates


def extract_pdf_operators_text(payload: bytes) -> str:
    content = payload.decode("latin-1", errors="ignore")
    blocks = re.findall(r"BT(.*?)ET", content, flags=re.S) or [content]
    lines: list[str] = []
    for block in blocks:
        for literal in re.findall(r"\((?:\\.|[^\\)])*\)\s*Tj", block):
            lines.append(decode_pdf_literal(literal.rsplit(")", 1)[0][1:]))
        for literal in re.findall(r"<[0-9A-Fa-f\s]+>\s*Tj", block):
            lines.append(decode_pdf_hex_string(literal.split(">", 1)[0][1:]))
        for array_block in re.findall(r"\[(.*?)\]\s*TJ", block, flags=re.S):
            array_parts: list[str] = []
            array_parts.extend(decode_pdf_literal(item[1:-1]) for item in re.findall(r"\((?:\\.|[^\\)])*\)", array_block))
            array_parts.extend(decode_pdf_hex_string(item[1:-1]) for item in re.findall(r"<[0-9A-Fa-f\s]+>", array_block))
            if array_parts:
                lines.append("".join(array_parts))
    return normalize_extracted_text("\n".join(lines))


def decode_pdf_literal(value: str) -> str:
    out: list[str] = []
    index = 0
    escapes = {"n": "\n", "r": "\r", "t": "\t", "b": "\b", "f": "\f", "(": "(", ")": ")", "\\": "\\"}
    while index < len(value):
        char = value[index]
        if char != "\\":
            out.append(char)
            index += 1
            continue
        index += 1
        if index >= len(value):
            break
        escaped = value[index]
        if escaped in escapes:
            out.append(escapes[escaped])
            index += 1
            continue
        if escaped in "\r\n":
            while index < len(value) and value[index] in "\r\n":
                index += 1
            continue
        if escaped in "01234567":
            octal = escaped
            index += 1
            for _ in range(2):
                if index < len(value) and value[index] in "01234567":
                    octal += value[index]
                    index += 1
                else:
                    break
            out.append(chr(int(octal, 8)))
            continue
        out.append(escaped)
        index += 1
    return "".join(out)


def decode_pdf_hex_string(value: str) -> str:
    compact = re.sub(r"\s+", "", value)
    if len(compact) % 2 == 1:
        compact += "0"
    try:
        payload = bytes.fromhex(compact)
    except ValueError:
        return ""
    for encoding in ("utf-16-be", "utf-8", "gb18030", "latin-1"):
        try:
            return payload.decode(encoding)
        except UnicodeDecodeError:
            continue
    return payload.decode("latin-1", errors="ignore")


def extract_doc_text_fallback(raw: bytes, encodings: Sequence[str]) -> str:
    candidates: list[tuple[int, str]] = []
    for encoding in ("utf-16le", "utf-16be", *encodings):
        try:
            decoded = raw.decode(encoding, errors="ignore")
        except LookupError:
            continue
        runs = extract_textish_runs(decoded, min_len=12)
        normalized = normalize_extracted_text("\n".join(runs))
        if normalized:
            candidates.append((len(normalized), normalized))
    if not candidates:
        return ""
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1]


def extract_textish_runs(text: str, min_len: int) -> list[str]:
    pattern = rf"[\u4e00-\u9fffA-Za-z0-9@#&%$+\-_/\\:;,.?!(){{}}\[\]<>，。？！：；、“”‘’《》【】\s]{{{min_len},}}"
    return [collapse_whitespace(match) for match in re.findall(pattern, text) if collapse_whitespace(match)]


def collapse_whitespace(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()


def normalize_extracted_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\ufeff", "").replace("\u3000", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return "\n".join(line.rstrip() for line in text.split("\n")).strip()
