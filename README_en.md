# ViMarketing Skills

This repository is a collection of OpenClaw skills for marketing workflows and customer-lead processing.

The contents mainly fall into two groups:

- Customer dialogue processing: extract customer data from conversations and evaluate opportunity quality.
- Marketing copy generation: create multilingual marketing copy for furniture export scenarios, especially for the Indonesian market.

If you are new to this repository, read this file first for the overall structure, then open the `README.md` and `SKILL.md` inside the relevant subfolder.

## What Is Included

### 1. `CustomerInfo Extraction/`

Customer dialogue extraction skill.

It converts sales, support, or business conversation records into CRM-friendly structured outputs, including:

- `JSON`
- `Excel (.xlsx)`
- `Markdown`

Typical use cases:

- Extract names, companies, phone numbers, emails, and WeChat IDs from chat logs
- Capture sales fields such as needs, budget, timeline, and next steps
- Batch-process multiple customer dialogue files

See the detailed documentation in:

- `CustomerInfo Extraction/README.md`
- `CustomerInfo Extraction/SKILL.md`

### 2. `CustomerInfo Classification/`

Customer inquiry analysis workspace.

This directory currently centers around one main sub-skill:

- `CustomerInfo Classification/CustomerInfo Classification/`: grades a customer conversation as `high`, `medium`, or `low` opportunity, with supporting evidence, risks, and suggested next actions.

It also includes supporting materials:

- `shared/`: shared document-reading code for `md`, `txt`, `doc`, `docx`, and text-based `pdf` inputs
- `tmp-customere2e-info/`: a temporary copy of customer extraction-related files
- `tmp-verification/`: sample files and generated outputs used for document parsing verification

Typical use cases:

- Quickly assess lead quality before sales follow-up
- Screen historical conversations for higher-potential customers
- Produce explainable opportunity scoring from dialogue records

See the detailed documentation in:

- `CustomerInfo Classification/README.md`
- `CustomerInfo Classification/CustomerInfo Classification/SKILL.md`

### 3. `MarketingCopy Writing/`

Multilingual marketing copy generation skill.

This skill is mainly designed for Chinese furniture companies expanding into the Indonesian market. It can generate:

- Indonesian copy
- English copy
- Chinese copy

Supported outputs include:

- E-commerce titles
- Product selling points
- Product detail copy
- Instagram / Facebook copy
- Xiaohongshu-style copy
- Poster short lines
- Promotional scripts

Typical use cases:

- Listing furniture products on Shopee or Tokopedia
- Creating social media and campaign content
- Producing poster, landing-page, or promotion copy

See the detailed documentation in:

- `MarketingCopy Writing/README.md`
- `MarketingCopy Writing/SKILL.md`

## Recommended Ways To Use It

### Use as OpenClaw skills

If these folders are already inside your OpenClaw skills workspace, you can invoke the corresponding skill according to each folder's `SKILL.md`.

### Run the scripts directly

Some directories include Python scripts that can be executed directly for local processing or verification.

Common examples:

```bash
python "CustomerInfo Extraction/scripts/extract_customer_to_excel.py" "CustomerInfo Extraction/examples/complete-enterprise-dialogue.md"
python "CustomerInfo Classification/CustomerInfo Classification/scripts/analyze_customer_opportunity.py" "CustomerInfo Classification/CustomerInfo Classification/examples/high-opportunity.md"
```

## Environment Requirements

Recommended environment:

- Python 3.10+

Based on the current repository contents, keep these points in mind:

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
