---
name: CustomerInfo Extraction
description: Extract structured customer profile data from sales, customer-service, account-management, or business-development conversation transcripts and export CRM-friendly JSON, Excel, and Markdown. Use when the input is a readable dialogue file or directory and the user wants conservative field extraction rather than a free-form summary.
version: 1.1.0
user-invocable: true
argument-hint: "<input-file-or-dir> [--batch]"
metadata:
  author: ViMarketing
  category: customer-ops
  tags:
    - crm
    - extraction
    - dialogue
    - json
    - excel
---

# CustomerInfo Extraction

Use this skill to convert customer conversation records into structured customer records for CRM import.

## Trigger Conditions

Use this skill when all of the following are true:

- The input is a file path or directory containing customer dialogue text
- The goal is to extract customer information, not just summarize the conversation
- The user wants machine-readable output for downstream systems or review

Do not use this skill for:

- Audio, image, or scanned PDF inputs that require OCR or speech-to-text first
- Pure invoice, contract, or form extraction without conversation context
- Cases where the user only wants a free-form sales summary

## Accepted Inputs

- Single file: `.md`, `.txt`, `.log`, `.csv`, `.json`, `.yaml`, `.yml`, `.srt`, or another readable text-like document
- Directory batch mode: pass a folder with `--batch`
- The script attempts UTF-8, GBK, GB2312, GB18030, UTF-16, Big5, and Latin-1 decoding

## Processing Steps

1. Confirm the path exists and is readable text
2. Clean obvious noise such as system notices, join/leave messages, empty media placeholders, and duplicated quote markers
3. Parse timestamps, speaker labels, and likely customer-side utterances
4. Extract hard fields with rules first: phone, mobile, email, wechat, time, company, region, common titles
5. Use conservative aggregation for soft fields: product interest, use case, pain points, current status, next step, risk flags, and opportunity level
6. Split into multiple records only when there is enough evidence of multiple customer identities; otherwise keep one row and explain uncertainty in `remarks`
7. Export the result set

## Command Usage

```bash
python scripts/extract_customer_to_excel.py <input_file>
python scripts/extract_customer_to_excel.py <input_file> --output-json result.json --output-xlsx result.xlsx --output-md result.md
python scripts/extract_customer_to_excel.py <input_dir> --batch
```

## Output Contract

The current script always writes three artifacts by default:

- `JSON`
- `Excel (.xlsx)`
- `Markdown`

Each record includes at least these fields in fixed order:

- `customer_name`
- `gender_guess`
- `phone`
- `mobile`
- `email`
- `wechat`
- `company_name`
- `company_short_name`
- `department`
- `job_title`
- `city`
- `province`
- `industry`
- `customer_type`
- `source_channel`
- `product_interest`
- `use_case`
- `pain_points`
- `budget_info`
- `timeline_info`
- `decision_maker`
- `current_status`
- `next_step`
- `opportunity_level`
- `confidence`
- `last_contact_time`
- `communication_summary`
- `key_quotes`
- `risk_flags`
- `remarks`
- `source_file`
- `extraction_time`
- `raw_text_length`
- `missing_fields`

## Field Rules

- Prefer direct evidence from customer lines
- Leave unknown fields empty instead of guessing
- Use the latest, clearest, and most complete value if the same field appears multiple times
- If multiple conflicting values remain plausible, choose one conservatively and write the conflict into `remarks`
- Lower `confidence` when key fields are missing, conflicting, or only weakly supported
- Mark suspicious data in `risk_flags` or `remarks`

## Boundary Handling

- No clear name, company, or contact information: keep fields empty and lower confidence
- Only a nickname exists: use it only when it looks like a stable identity; otherwise keep `customer_name` empty and mention it in `remarks`
- Multiple customers in one file: split only when distinct names, phones, emails, or companies appear
- Mixed roles and unclear labels: rely on content plus rule evidence, but stay conservative
- Very short text: still export results, but include `信息不足` in `risk_flags` and reduce confidence

## Few-Shot Examples

### Example 1

Input cue:

```text
客户：我是上海智联制造的采购经理李晨，手机号 13800138000，邮箱 lichen@zhilian.com。
客户：我们想了解你们的客服质检产品，这个月要做方案评估，下周想看报价。
```

Expected shape:

```json
{
  "records": [
    {
      "customer_name": "李晨",
      "company_name": "上海智联制造",
      "mobile": "13800138000",
      "email": "lichen@zhilian.com",
      "current_status": "方案评估",
      "opportunity_level": "high"
    }
  ]
}
```

### Example 2

Input cue:

```text
客户：我这边先了解一下，微信是 wx_ops_2024。
客户：我们在比较几家工单系统，预算还没定，后面拉技术同事一起看。
```

Expected shape:

```json
{
  "records": [
    {
      "wechat": "wx_ops_2024",
      "product_interest": "工单系统",
      "budget_info": "预算还没定",
      "current_status": "需求沟通",
      "opportunity_level": "medium"
    }
  ]
}
```

### Example 3

Input cue:

```text
客户：先发资料吧。
客户：有需要我再联系你。
```

Expected shape:

```json
{
  "records": [
    {
      "confidence": 20,
      "risk_flags": ["信息不足"],
      "missing_fields": ["customer_name", "company_name", "mobile"]
    }
  ]
}
```

## Review Checklist

Before returning results:

- Confirm JSON fields are fixed and complete
- Confirm Excel column order matches the JSON field order
- Confirm missing fields are listed
- Confirm `remarks` records conflicts or split uncertainty
- Confirm no fabricated values were introduced
