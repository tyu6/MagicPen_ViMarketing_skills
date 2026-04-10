#!/usr/bin/env python3
"""Analyze customer conversation files and grade sales opportunity."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from shared.document_input import DEFAULT_ENCODINGS, DocumentReadError, read_document_text


ENCODINGS = list(DEFAULT_ENCODINGS)


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def load_rules() -> dict:
    config_path = Path(__file__).resolve().parent.parent / "config" / "opportunity_rules.json"
    try:
        with config_path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise SystemExit(f"规则文件不存在: {config_path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"规则文件不是合法 JSON: {config_path} ({exc})") from exc


def read_text_file(path: Path) -> Tuple[str, str]:
    try:
        raw = path.read_bytes()
    except FileNotFoundError as exc:
        raise SystemExit(f"输入文件不存在: {path}") from exc
    except OSError as exc:
        raise SystemExit(f"无法读取输入文件: {path} ({exc})") from exc

    if not raw:
        raise SystemExit(f"输入文件为空: {path}")

    if raw.count(b"\x00") / max(len(raw), 1) > 0.02:
        raise SystemExit(f"文件看起来像二进制，无法按文本分析: {path}")

    for encoding in ENCODINGS:
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue

    raise SystemExit(f"无法用常见编码解码文本: {path}")


def read_text_file(path: Path) -> Tuple[str, str]:
    try:
        return read_document_text(path, ENCODINGS)
    except DocumentReadError as exc:
        raise SystemExit(str(exc)) from exc


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u3000", " ").replace("\ufeff", "")
    return text


def compile_patterns(patterns: List[str]) -> List[re.Pattern]:
    return [re.compile(pattern, re.IGNORECASE) for pattern in patterns]


def guess_speaker(label: str, rules: dict) -> str:
    lowered = label.lower()
    for marker in rules["speaker_markers"]["customer"]:
        if marker.lower() in lowered:
            return "customer"
    for marker in rules["speaker_markers"]["seller"]:
        if marker.lower() in lowered:
            return "seller"
    return "unknown"


def preprocess_lines(text: str, rules: dict) -> List[dict]:
    system_patterns = compile_patterns(rules["system_message_patterns"])
    parsed: List[dict] = []

    for line_number, raw_line in enumerate(text.split("\n"), start=1):
        original = raw_line.strip()
        if not original:
            continue
        if any(pattern.search(original) for pattern in system_patterns):
            continue

        line = original
        line = re.sub(r"^\[[^\]]+\]\s*", "", line)
        line = re.sub(r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}\s+\d{1,2}:\d{2}(?::\d{2})?\s*", "", line)
        line = re.sub(r"^\d{1,2}:\d{2}(?::\d{2})?\s*", "", line)

        speaker = "unknown"
        content = line
        speaker_match = re.match(r"^(?P<label>[^:：]{1,24})[:：]\s*(?P<content>.+)$", line)
        if speaker_match:
            label = speaker_match.group("label").strip()
            content = speaker_match.group("content").strip()
            speaker = guess_speaker(label, rules)

        if len(content) < 2:
            continue

        parsed.append(
            {
                "line_number": line_number,
                "speaker": speaker,
                "raw": original,
                "content": content,
            }
        )

    return parsed


def speaker_weight(speaker: str) -> float:
    if speaker == "customer":
        return 1.0
    if speaker == "unknown":
        return 0.7
    return 0.35


def speaker_allowed(expected: str, actual: str) -> bool:
    if expected == "any":
        return True
    if expected == "customer_only":
        return actual == "customer"
    if expected == "customer_or_unknown":
        return actual in {"customer", "unknown"}
    return True


def format_evidence(line: dict) -> str:
    return f"L{line['line_number']}: {line['raw']}"


def evaluate_signals(lines: List[dict], rules: dict) -> Tuple[dict, Dict[str, List[dict]]]:
    matched_by_signal: Dict[str, List[dict]] = {}
    signal_definitions = rules["signals"]

    for signal in signal_definitions:
        compiled = compile_patterns(signal["patterns"])
        hits: List[dict] = []
        for line in lines:
            if not speaker_allowed(signal.get("speaker", "any"), line["speaker"]):
                continue
            haystack = f"{line['raw']} {line['content']}"
            if any(pattern.search(haystack) for pattern in compiled):
                score = round(signal["points"] * speaker_weight(line["speaker"]))
                if score <= 0:
                    continue
                hits.append(
                    {
                        "line_number": line["line_number"],
                        "speaker": line["speaker"],
                        "raw": line["raw"],
                        "content": line["content"],
                        "weighted_points": score,
                        "label": signal["label"],
                        "direction": signal["direction"],
                        "dimension": signal["dimension"],
                    }
                )
            if len(hits) >= signal.get("max_hits", 1):
                break
        if hits:
            matched_by_signal[signal["id"]] = hits

    dimension_defs = rules["dimensions"]
    breakdown = {}
    for key, definition in dimension_defs.items():
        score = definition.get("base_score", 0)
        positive_hits = []
        negative_hits = []
        for signal in signal_definitions:
            if signal["dimension"] != key or signal["id"] not in matched_by_signal:
                continue
            hits = matched_by_signal[signal["id"]]
            signal_points = sum(hit["weighted_points"] for hit in hits)
            evidence = [format_evidence(hit) for hit in hits]
            entry = {
                "signal_id": signal["id"],
                "label": signal["label"],
                "points": signal_points,
                "evidence": evidence,
            }
            if signal["direction"] == "positive":
                score += signal_points
                positive_hits.append(entry)
            else:
                score -= signal_points
                negative_hits.append(entry)
        breakdown[key] = {
            "label": definition["label"],
            "score": int(clamp(score, 0, definition["max_score"])),
            "max_score": int(definition["max_score"]),
            "meaning": definition["meaning"],
            "positive_hits": positive_hits,
            "negative_hits": negative_hits,
        }

    return breakdown, matched_by_signal


def compute_bonus_and_penalty(matched: Dict[str, List[dict]]) -> Tuple[List[dict], List[dict], bool]:
    bonuses: List[dict] = []
    penalties: List[dict] = []
    severe_blocker = False

    def first_evidence(signal_id: str) -> str:
        return format_evidence(matched[signal_id][0]) if signal_id in matched else ""

    if "purchase_explicit" in matched and "timeline_present" in matched:
        bonuses.append(
            {
                "label": "明确推进窗口",
                "points": 5,
                "evidence": [first_evidence("purchase_explicit"), first_evidence("timeline_present")],
            }
        )
    if "purchase_explicit" in matched and "budget_explicit" in matched:
        bonuses.append(
            {
                "label": "采购意愿与预算同时出现",
                "points": 5,
                "evidence": [first_evidence("purchase_explicit"), first_evidence("budget_explicit")],
            }
        )
    if "decision_maker_present" in matched and "implementation_owner" in matched:
        bonuses.append(
            {
                "label": "决策链和落地角色同时出现",
                "points": 3,
                "evidence": [first_evidence("decision_maker_present"), first_evidence("implementation_owner")],
            }
        )

    if "purchase_rejected" in matched:
        penalties.append(
            {
                "label": "客户明确拒绝当前推进",
                "points": 15,
                "evidence": [first_evidence("purchase_rejected")],
            }
        )
        severe_blocker = True
    if "risk_no_plan" in matched and "risk_budget_blocker" in matched:
        penalties.append(
            {
                "label": "无计划且预算受阻",
                "points": 10,
                "evidence": [first_evidence("risk_no_plan"), first_evidence("risk_budget_blocker")],
            }
        )
        severe_blocker = True
    if "free_consulting_risk" in matched:
        penalties.append(
            {
                "label": "偏向收集信息而非真实推进",
                "points": 8,
                "evidence": [first_evidence("free_consulting_risk")],
            }
        )
    if "implementation_blocker" in matched:
        penalties.append(
            {
                "label": "存在技术或合规阻塞",
                "points": 8,
                "evidence": [first_evidence("implementation_blocker")],
            }
        )

    return bonuses, penalties, severe_blocker


def pick_evidence(breakdown: dict, bonuses: List[dict], penalties: List[dict]) -> List[str]:
    scored_lines: Dict[str, int] = {}

    for dimension in breakdown.values():
        for bucket in ("positive_hits", "negative_hits"):
            for hit in dimension[bucket]:
                for evidence in hit["evidence"]:
                    scored_lines[evidence] = max(scored_lines.get(evidence, 0), hit["points"])

    for item in bonuses + penalties:
        for evidence in item["evidence"]:
            if evidence:
                scored_lines[evidence] = max(scored_lines.get(evidence, 0), item["points"])

    return [text for text, _ in sorted(scored_lines.items(), key=lambda item: (-item[1], item[0]))[:8]]


def compute_total_score(breakdown: dict, bonuses: List[dict], penalties: List[dict]) -> int:
    base = sum(item["score"] for item in breakdown.values())
    bonus = sum(item["points"] for item in bonuses)
    penalty = sum(item["points"] for item in penalties)
    return int(clamp(base + bonus - penalty, 0, 100))


def information_insufficient(lines: List[dict], evidence: List[str], matched: Dict[str, List[dict]]) -> bool:
    informative_chars = sum(len(line["content"]) for line in lines)
    return informative_chars < 80 or len(lines) < 3 or len(evidence) < 2 or len(matched) < 2


def build_risk_flags(breakdown: dict, matched: Dict[str, List[dict]], insufficient: bool) -> List[str]:
    flags: List[str] = []
    explicit_map = {
        "risk_no_plan": "客户明确表示暂无计划或排期",
        "risk_budget_blocker": "预算不足或预算审批受阻",
        "purchase_rejected": "客户明确拒绝当前推进动作",
        "implementation_blocker": "存在技术或合规阻塞",
        "free_consulting_risk": "存在只收集信息或白拿方案的倾向",
        "engagement_cooling": "互动积极度下降，存在明显降温信号",
    }
    for signal_id, label in explicit_map.items():
        if signal_id in matched:
            flags.append(label)

    if breakdown["budget_resources"]["score"] <= 3:
        flags.append("预算/资源未明确")
    if breakdown["decision_info"]["score"] <= 3:
        flags.append("决策链条不清晰")
    if breakdown["time_urgency"]["score"] <= 3:
        flags.append("时间计划不明确")
    if insufficient:
        flags.append("信息不足")

    deduped = []
    for flag in flags:
        if flag not in deduped:
            deduped.append(flag)
    return deduped


def compute_confidence(
    lines: List[dict],
    matched: Dict[str, List[dict]],
    evidence: List[str],
    severe_blocker: bool,
    insufficient: bool,
) -> int:
    customer_lines = sum(1 for line in lines if line["speaker"] == "customer")
    unknown_lines = sum(1 for line in lines if line["speaker"] == "unknown")
    positive_signals = 0
    negative_signals = 0
    for hits in matched.values():
        if hits and hits[0]["direction"] == "positive":
            positive_signals += 1
        elif hits:
            negative_signals += 1

    confidence = 35
    confidence += min(20, len(matched) * 3)
    confidence += min(15, len(lines) * 2)
    confidence += min(10, len(evidence) * 2)
    confidence += 8 if customer_lines >= 2 else 0
    confidence += 4 if severe_blocker else 0
    confidence -= 15 if insufficient else 0
    confidence -= 8 if unknown_lines > customer_lines and customer_lines == 0 else 0
    confidence -= min(10, min(positive_signals, negative_signals) * 2)
    return int(clamp(confidence, 18, 96))


def determine_level(total_score: int, breakdown: dict, severe_blocker: bool, insufficient: bool) -> str:
    if severe_blocker:
        return "low"
    if (
        total_score >= 70
        and breakdown["purchase_intent"]["score"] >= 10
        and breakdown["need_clarity"]["score"] >= 8
        and breakdown["risk_objection_strength"]["score"] >= 6
        and not insufficient
    ):
        return "high"
    if total_score >= 35:
        return "medium"
    return "low"


def build_reasoning(level: str, breakdown: dict, risk_flags: List[str], insufficient: bool) -> str:
    pieces = []
    if breakdown["purchase_intent"]["score"] >= 10:
        pieces.append("客户已出现明确推进或采购信号")
    if breakdown["need_clarity"]["score"] >= 8:
        pieces.append("需求和使用场景较清晰")
    if breakdown["time_urgency"]["score"] >= 5:
        pieces.append("时间计划较明确")
    if breakdown["decision_info"]["score"] >= 5:
        pieces.append("决策或采购角色已有信息")
    if breakdown["budget_resources"]["score"] >= 5:
        pieces.append("预算或资源信号较明确")
    if insufficient:
        pieces.append("信息不足，判断需保守")
    if risk_flags and level != "high":
        pieces.append(f"主要风险包括：{'；'.join(risk_flags[:2])}")

    if not pieces:
        pieces.append("缺少足够的高质量推进信号，机会判断偏保守")

    return "；".join(pieces) + "。"


def build_next_action(level: str, breakdown: dict, risk_flags: List[str], insufficient: bool) -> str:
    if insufficient:
        return "先补充客户原话或更多轮次对话，再确认预算、时间和决策链。"
    if level == "high":
        return "尽快安排需求澄清或演示会议，锁定报价、PoC 范围、负责人和上线时间。"
    if level == "medium":
        missing = []
        if breakdown["budget_resources"]["score"] <= 3:
            missing.append("预算")
        if breakdown["time_urgency"]["score"] <= 3:
            missing.append("时间表")
        if breakdown["decision_info"]["score"] <= 3:
            missing.append("决策链")
        if missing:
            return f"继续资格确认，优先补齐{'、'.join(missing)}，并争取一次短会换取明确下一步。"
        return "推动一次短会或定向演示，把兴趣转成明确的试用、报价或技术对接动作。"
    if any("预算" in flag or "暂无计划" in flag for flag in risk_flags):
        return "降低优先级，转为 nurture 跟进，约定未来窗口再联系，避免继续投入重方案成本。"
    return "维持轻量跟进，只发送简版资料；若客户没有新信号，不要继续重投入推进。"


def render_markdown(result: dict) -> str:
    lines = [
        "# 客户机会分级摘要",
        "",
        f"- 机会等级：{result['level_zh']} (`{result['customer_opportunity_level']}`)",
        f"- 置信度：{result['confidence']}",
        f"- 总分：{result['score_breakdown']['total_score']}/100",
        "",
        "## 核心依据",
    ]
    evidence = result.get("evidence") or ["无足够证据"]
    for item in evidence:
        lines.append(f"- {item}")
    lines.extend(["", "## 关键风险"])
    risk_flags = result.get("risk_flags") or ["暂无明显高风险信号"]
    for item in risk_flags:
        lines.append(f"- {item}")
    lines.extend(["", "## 建议跟进动作", f"- {result['next_action']}", "", "## 判断说明", f"- {result['reasoning']}"])
    return "\n".join(lines)


def build_result(path: Path, encoding: str, lines: List[dict], breakdown: dict, matched: Dict[str, List[dict]]) -> dict:
    bonuses, penalties, severe_blocker = compute_bonus_and_penalty(matched)
    evidence = pick_evidence(breakdown, bonuses, penalties)
    insufficient = information_insufficient(lines, evidence, matched)
    if insufficient:
        penalties = penalties + [{"label": "信息不足", "points": 8, "evidence": []}]
    total_score = compute_total_score(breakdown, bonuses, penalties)
    risk_flags = build_risk_flags(breakdown, matched, insufficient)
    level = determine_level(total_score, breakdown, severe_blocker, insufficient)
    confidence = compute_confidence(lines, matched, evidence, severe_blocker, insufficient)
    level_zh = {"high": "高机会客户", "medium": "中机会客户", "low": "低机会客户"}[level]

    return {
        "input_file": str(path),
        "detected_encoding": encoding,
        "customer_opportunity_level": level,
        "level_zh": level_zh,
        "confidence": confidence,
        "score_breakdown": {
            "total_score": total_score,
            "level_mapping": {
                "high": ">= 70 且采购意愿/需求明确度达到高机会门槛，且无严重阻塞",
                "medium": "35-69 或存在兴趣但预算/时间/决策链未补齐",
                "low": "< 35，或出现明确拒绝、无预算、无计划等严重阻塞"
            },
            "dimensions": breakdown,
            "bonuses": bonuses,
            "penalties": penalties
        },
        "evidence": evidence,
        "reasoning": build_reasoning(level, breakdown, risk_flags, insufficient),
        "next_action": build_next_action(level, breakdown, risk_flags, insufficient),
        "risk_flags": risk_flags,
        "analysis_meta": {
            "line_count": len(lines),
            "customer_line_count": sum(1 for line in lines if line["speaker"] == "customer"),
            "unknown_speaker_line_count": sum(1 for line in lines if line["speaker"] == "unknown"),
            "matched_signal_count": len(matched),
            "information_insufficient": insufficient
        }
    }


def write_output(content: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze customer conversation and grade opportunity level.")
    parser.add_argument("input_file", help="Path to a text-like conversation file")
    parser.add_argument(
        "--format",
        choices=["json", "markdown", "both"],
        default="json",
        help="Primary output format. Default: json"
    )
    parser.add_argument("--output", help="Path to write the primary output")
    parser.add_argument("--markdown-output", help="Path to write the markdown summary")
    args = parser.parse_args()

    input_path = Path(args.input_file).expanduser().resolve()
    rules = load_rules()
    text, encoding = read_text_file(input_path)
    normalized = normalize_text(text)
    lines = preprocess_lines(normalized, rules)
    breakdown, matched = evaluate_signals(lines, rules)
    result = build_result(input_path, encoding, lines, breakdown, matched)
    json_text = json.dumps(result, ensure_ascii=False, indent=2)
    markdown_text = render_markdown(result)

    if args.format == "json":
        if args.output:
            write_output(json_text + "\n", Path(args.output))
        else:
            print(json_text)
        if args.markdown_output:
            write_output(markdown_text + "\n", Path(args.markdown_output))
    elif args.format == "markdown":
        if args.output:
            write_output(markdown_text + "\n", Path(args.output))
        else:
            print(markdown_text)
    else:
        output_path = Path(args.output) if args.output else input_path.with_suffix(".opportunity.json")
        markdown_path = Path(args.markdown_output) if args.markdown_output else input_path.with_suffix(".opportunity.md")
        write_output(json_text + "\n", output_path)
        write_output(markdown_text + "\n", markdown_path)
        print(json.dumps({"json_output": str(output_path), "markdown_output": str(markdown_path)}, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    sys.exit(main())
