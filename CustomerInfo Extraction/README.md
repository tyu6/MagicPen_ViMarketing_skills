# 客户对话信息提取 Skill

## 概述

该目录包含一个实用的 OpenClaw Skill，用于从客户对话记录中提取关键信息，并导出为适合 CRM 使用的结构化结果。

---

## 文件说明

- `SKILL.md`：Skill 指令与触发契约
- `scripts/extract_customer_to_excel.py`：命令行提取与导出脚本
- `config/field_mapping.json`：输出字段顺序与 CRM 友好的列映射
- `references/extraction-rules.md`：提取规则与启发式参考
- `examples/`：示例输入与生成结果

---

## 环境要求

- Python 3.10+
- 导出 `.xlsx` 需要安装 `openpyxl`

如有需要，可先安装依赖：

```bash
pip install openpyxl
```

---

## 使用方式

单文件处理：

```bash
python scripts/extract_customer_to_excel.py examples/complete-enterprise-dialogue.md
```

自定义输出路径：

```bash
python scripts/extract_customer_to_excel.py examples/complete-enterprise-dialogue.md --output-json out.json --output-xlsx out.xlsx --output-md out.md
```

批量模式：

```bash
python scripts/extract_customer_to_excel.py examples --batch
```

---

## 默认输出

对于名为 `demo.md` 的输入文件，默认输出为：

- `customer_export_demo.json`
- `customer_export_demo.xlsx`
- `customer_export_demo.md`

在批量模式下，默认输出为：

- `customer_export_batch.json`
- `customer_export_batch.xlsx`
- `customer_export_batch.md`

---

## 说明

- 提取器在身份与联系方式字段上优先使用基于规则的证据。
- 语义类字段保持保守，不会臆造信息。
- 当多个客户身份无法被清晰拆分时，脚本仍会至少保留一行结果，并在 `remarks` 中说明歧义情况。
