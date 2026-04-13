# Extraction Rules

## Hard Extraction First

Use rule-based extraction for:

- Mobile numbers and landline phones
- Email addresses
- WeChat IDs when preceded by `微信`, `微信号`, `vx`, or `wx`
- Company names with common suffixes such as `公司`, `有限公司`, `集团`, `科技`, `信息`, `网络`, `医院`, `银行`
- Titles such as `经理`, `总监`, `负责人`, `采购`, `老板`, `主任`, `CEO`
- Province and city names that appear explicitly in the text
- Timestamps in message prefixes

## Semantic Aggregation

Use conservative sentence selection for:

- `product_interest`
- `use_case`
- `pain_points`
- `budget_info`
- `timeline_info`
- `current_status`
- `next_step`
- `communication_summary`
- `risk_flags`

## Multi-Customer Splitting

Split into multiple records only when one of these conditions is met:

- Distinct customer names appear with separate contact details
- Distinct companies appear with enough surrounding customer-side context
- Distinct mobile/email/wechat identifiers clearly map to different contacts

If the evidence is not strong enough, keep one record and note the ambiguity in `remarks`.

## Confidence Guidance

Increase confidence when:

- Identity fields and contact fields are directly extracted from customer lines
- Company, title, demand, and status all have direct support
- There are multiple consistent signals without conflicts

Decrease confidence when:

- Only nicknames appear
- Key fields are missing
- Field candidates conflict
- The file is short or noisy
- The role labels are unclear
