# ViMarketing Skills

This repository contains three production skills for marketing and customer-lead workflows:

1. `CustomerInfo Extraction/`
   Extract structured customer profile data from conversation transcripts and export CRM-friendly `JSON`, `Excel (.xlsx)`, and `Markdown`.
2. `CustomerInfo Classification/`
   Grade a customer conversation as `high`, `medium`, or `low` opportunity, with evidence, risks, and suggested next actions.
3. `MarketingCopy Writing/`
   Generate Indonesian, English, and Chinese furniture marketing copy from either text prompts or product images.

If you are new to this repository, start here and then open the `README.md` and `SKILL.md` inside the relevant subfolder.

## What Is Included

### `CustomerInfo Extraction/`

Customer dialogue extraction skill.

Typical use cases:

- Extract names, companies, phone numbers, emails, and WeChat IDs from chat logs
- Capture sales fields such as needs, budget, timeline, and next steps
- Batch-process multiple customer dialogue files

See:

- `CustomerInfo Extraction/README.md`
- `CustomerInfo Extraction/SKILL.md`

### `CustomerInfo Classification/`

Customer opportunity grading skill.

The `CustomerInfo Classification/` directory itself is now the installed skill root. The old nested path is no longer used.

Typical use cases:

- Quickly assess lead quality before sales follow-up
- Screen historical conversations for higher-potential customers
- Produce explainable opportunity scoring from dialogue records

This directory also contains development or verification materials such as `shared/`, `tmp-customere2e-info/`, and `tmp-verification/`. Those folders are not required to install or invoke the production skill.

See:

- `CustomerInfo Classification/README.md`
- `CustomerInfo Classification/SKILL.md`

### `MarketingCopy Writing/`

Multilingual marketing copy generation skill for furniture export scenarios.

Typical use cases:

- Listing furniture products on Shopee or Tokopedia
- Creating social media and campaign content
- Producing poster, landing-page, or promotion copy
- Generating image-first copy from a product photo

See:

- `MarketingCopy Writing/README.md`
- `MarketingCopy Writing/SKILL.md`

## Recommended Ways To Use It

### Use as Skills

If these folders are already inside your OpenClaw skills workspace, invoke each skill according to its `SKILL.md`.

### Run the scripts directly

Some directories include Python scripts for local processing or verification.

Examples:

```bash
python "CustomerInfo Extraction/scripts/extract_customer_to_excel.py" "CustomerInfo Extraction/examples/complete-enterprise-dialogue.md"
python "CustomerInfo Classification/scripts/analyze_customer_opportunity.py" "CustomerInfo Classification/examples/high-opportunity.md"
```

## Environment Requirements

Recommended environment:

- Python 3.10+

Keep these points in mind:

- `openpyxl` is required for `.xlsx` export
- `pdf` input only works for PDFs with an embedded text layer
- `.doc` parsing is best-effort and is usually less reliable than `.docx`

If you need Excel export, install:

```bash
pip install openpyxl
```

## Which Folder Should You Start With

If your goal is:

- Extract customer data for CRM import: start with `CustomerInfo Extraction/`
- Judge whether a customer is a strong opportunity: start with `CustomerInfo Classification/`
- Generate furniture marketing copy for the Indonesian market: start with `MarketingCopy Writing/`

## Repository Notes

- `README.md`: Chinese overview
- `README_en.md`: English overview
- Subfolder `README.md` / `README_en.md`: detailed documentation for each skill
- `LICENSE`: Apache License 2.0
