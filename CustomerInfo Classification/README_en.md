# CustomerInfo Classification Skill

This directory is the `CustomerInfo Classification` workspace. The main OpenClaw skill is located in the `CustomerInfo Classification/` subfolder inside this directory.

## Install

If this folder is already inside your OpenClaw skills workspace, no extra installation is required.

If you want OpenClaw to discover it from the default global skill path, copy the `CustomerInfo Classification/` subfolder that contains `SKILL.md` to:

- Windows: `%USERPROFILE%\\.openclaw\\skills\\CustomerInfo Classification`

## Use

After entering the `CustomerInfo Classification/` subfolder inside this directory, run the analyzer directly:

```bash
cd "CustomerInfo Classification"
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md
```

Generate both JSON and Markdown files:

```bash
cd "CustomerInfo Classification"
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md --format both --output examples/high-opportunity.output.json --markdown-output examples/high-opportunity.output.md
```

## Contents

- `CustomerInfo Classification/SKILL.md`: OpenClaw skill instructions and few-shot guidance
- `CustomerInfo Classification/scripts/analyze_customer_opportunity.py`: CLI analyzer
- `CustomerInfo Classification/config/opportunity_rules.json`: adjustable signal and weighting rules
- `CustomerInfo Classification/references/scoring-rubric.md`: scoring dimension reference
- `CustomerInfo Classification/examples/`: sample inputs and outputs

## Notes

- Default output is JSON.
- Markdown summary is supported through `--format markdown` or `--markdown-output`.
- Input now supports `.md`, `.txt`, `.doc`, `.docx`, and text-based `.pdf` files.
- The script is optimized for Chinese customer dialogue, but it also tolerates mixed English terms like `PoC`, `SSO`, and `API`.
