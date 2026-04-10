# Customer Opportunity Grading Skill

This workspace now contains a reusable skill at `customer-opportunity-grading/`.

## Install

If this folder is already inside your  skills workspace, no extra installation is required.

## Use

Run the analyzer directly:

```bash
cd customer-opportunity-grading
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md
```

Generate both JSON and Markdown files:

```bash
cd customer-opportunity-grading
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md --format both --output examples/high-opportunity.output.json --markdown-output examples/high-opportunity.output.md
```

## Contents

- `customer-opportunity-grading/SKILL.md`: Codex skill instructions and few-shot guidance
- `customer-opportunity-grading/scripts/analyze_customer_opportunity.py`: CLI analyzer
- `customer-opportunity-grading/config/opportunity_rules.json`: adjustable signal and weighting rules
- `customer-opportunity-grading/references/scoring-rubric.md`: scoring dimension reference
- `customer-opportunity-grading/examples/`: sample inputs and outputs

## Notes

- Default output is JSON.
- Markdown summary is supported through `--format markdown` or `--markdown-output`.
- Input now supports `.md`, `.txt`, `.doc`, `.docx`, and text-based `.pdf` files.
- The script is optimized for Chinese customer dialogue, but it also tolerates mixed English terms like `PoC`, `SSO`, and `API`.
