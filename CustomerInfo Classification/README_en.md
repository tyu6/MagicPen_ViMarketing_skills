# CustomerInfo Classification Skill

This directory is now the skill root for `CustomerInfo Classification`.

## Install

Copy this directory directly into your OpenClaw skills path:

- Windows: `%USERPROFILE%\\.openclaw\\skills\\CustomerInfo Classification`

The skill is self-contained and does not require a sibling `shared/` directory.

## Use

Run the analyzer from the skill root:

```bash
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md
```

Generate both JSON and Markdown outputs:

```bash
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md --format both --output examples/high-opportunity.output.json --markdown-output examples/high-opportunity.output.md
```

## Structure

- `SKILL.md`: OpenClaw skill instructions and few-shot guidance
- `agents/openai.yaml`: skill display metadata
- `scripts/analyze_customer_opportunity.py`: CLI analyzer
- `scripts/document_input.py`: bundled document-reading helpers
- `config/opportunity_rules.json`: adjustable signal and weighting rules
- `references/scoring-rubric.md`: scoring dimension reference
- `examples/`: sample inputs and outputs

## Notes

- Default output is JSON.
- Markdown summary is supported through `--format markdown` or `--markdown-output`.
- Input supports `.md`, `.txt`, `.doc`, `.docx`, and text-based `.pdf` files.
- The analyzer is optimized for Chinese customer dialogue and tolerates mixed terms like `PoC`, `SSO`, and `API`.
- `shared/` and `tmp-*` directories in this workspace are not required for installing this skill.
