# Customer Dialogue Extraction Skill

This folder contains a practical OpenClaw skill for extracting customer information from conversation transcripts and exporting CRM-friendly outputs.

## Files

- `SKILL.md`: skill instructions and trigger contract
- `scripts/extract_customer_to_excel.py`: CLI extractor and exporter
- `config/field_mapping.json`: output field order and CRM-friendly column mapping
- `references/extraction-rules.md`: rule and heuristic reference
- `examples/`: sample inputs and generated outputs

## Requirements

- Python 3.10+
- `openpyxl` for `.xlsx` export

Install dependency if needed:

```bash
pip install openpyxl
```

## Usage

Single file:

```bash
python scripts/extract_customer_to_excel.py examples/complete-enterprise-dialogue.md
```

Custom output paths:

```bash
python scripts/extract_customer_to_excel.py examples/complete-enterprise-dialogue.md --output-json out.json --output-xlsx out.xlsx --output-md out.md
```

Batch mode:

```bash
python scripts/extract_customer_to_excel.py examples --batch
```

## Output Defaults

For an input file named `demo.md`, default outputs are:

- `customer_export_demo.json`
- `customer_export_demo.xlsx`
- `customer_export_demo.md`

For batch mode, defaults are:

- `customer_export_batch.json`
- `customer_export_batch.xlsx`
- `customer_export_batch.md`

## Notes

- The extractor prefers rule-based evidence for identity and contact fields.
- Semantic fields remain conservative and avoid fabrication.
- When multiple customer identities cannot be cleanly separated, the script keeps at least one row and explains ambiguity in `remarks`.
