# 客户对话信息提取 Skill

这个目录包含一个用于客户信息抽取的 OpenClaw Skill，可把销售、客服或商务沟通记录整理为适合 CRM 导入的结构化结果。

## 文件说明

- `SKILL.md`：Skill 指令、触发条件和输出约束
- `scripts/extract_customer_to_excel.py`：命令行抽取与导出脚本
- `config/field_mapping.json`：字段顺序与 CRM 友好列映射
- `references/extraction-rules.md`：抽取规则与启发式说明
- `examples/`：示例输入与输出

## 环境要求

- Python 3.10+
- 导出 `.xlsx` 需要安装 `openpyxl`

如有需要，可先安装依赖：

```bash
pip install openpyxl
```

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

## 默认输出

脚本默认会同时导出 `JSON`、`Excel`、`Markdown` 三个文件。

对于名为 `demo.md` 的输入文件，默认输出为：

- `customer_export_demo.json`
- `customer_export_demo.xlsx`
- `customer_export_demo.md`

在批量模式下，默认输出为：

- `customer_export_batch.json`
- `customer_export_batch.xlsx`
- `customer_export_batch.md`

## 说明

- 抽取器在身份字段和联系方式字段上优先依赖规则证据。
- 语义类字段保持保守，不会凭空补全不存在的信息。
- 当多个客户身份无法可靠拆分时，脚本会至少保留一条记录，并在 `remarks` 中说明歧义。
