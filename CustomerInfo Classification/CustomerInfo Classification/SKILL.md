---
name: CustomerInfo Classification
description: Analyze sales, business-development, support, or account-management conversation transcripts and grade the customer opportunity as high, medium, or low with structured evidence. Use when OpenClaw receives a path to a dialogue file such as .md, .txt, .doc, .docx, .pdf, .log, .csv, .json, or another readable text file containing Chinese or mixed-language customer conversations, and needs an explainable JSON assessment plus an optional Markdown summary for downstream programs or humans.
---

# Customer Opportunity Grading

Use this skill to turn noisy customer conversation records into a conservative, explainable opportunity assessment.

## Input Contract

- Accept one file path that contains customer-facing dialogue.
- Prefer `.md`, `.txt`, or `.docx`.
- Also accept `.doc`, `.pdf`, `.log`, `.csv`, `.json`, `.yaml`, `.srt`, or extensionless exports.
- `.pdf` only supports PDFs with an embedded text layer; scanned PDFs still need OCR first.
- `.doc` uses best-effort extraction and may be less reliable than `.docx`.
- Treat the file as chat history. It may contain timestamps, speaker labels, system messages, group members, or mixed sales/customer turns.

## Output Contract

Default output is JSON with at least these keys:

- `customer_opportunity_level`: `high` | `medium` | `low`
- `confidence`: integer `0-100`
- `score_breakdown`
- `evidence`
- `reasoning`
- `next_action`
- `risk_flags`

Support an optional Markdown summary that contains:

- 机会等级
- 置信度
- 核心依据
- 关键风险
- 建议跟进动作

## Execution Workflow

1. Confirm the input path exists and is a readable text-like document.
2. Run the bundled analyzer:

```bash
python scripts/analyze_customer_opportunity.py <input_file>
```

3. Return the JSON result directly unless the user asks for Markdown or both formats.
4. To generate Markdown as well, use one of these patterns:

```bash
python scripts/analyze_customer_opportunity.py <input_file> --format markdown
python scripts/analyze_customer_opportunity.py <input_file> --format both --output result.json --markdown-output result.md
```

5. If the file is `.docx`, `.doc`, or `.pdf`, let the script extract text first and then analyze it. If extraction fails, stop and report the specific limitation.

## Scoring Model

The analyzer uses eight dimensions and a 100-point total score. Full dimension details live in [references/scoring-rubric.md](references/scoring-rubric.md).

| Dimension | Max | Interpretation |
| --- | ---: | --- |
| 需求明确度 | 15 | Need, pain point, and scenario clarity |
| 采购意愿 | 20 | Buying, trial, quotation, contract, PoC intent |
| 时间紧迫度 | 10 | Timeline, deadline, rollout urgency |
| 预算/资源信号 | 10 | Budget, price discussion, internal resources |
| 决策信息完整度 | 10 | Buyer, approver, procurement, technical owner |
| 互动积极度 | 10 | Responsiveness and initiative to move forward |
| 落地可行性 | 10 | Deployment, integration, implementation readiness |
| 风险/异议强度 | 15 | Reverse-risk dimension: lower score means stronger blockers |

### Level Mapping

- `high`: total score `>= 70`, and both `采购意愿 >= 10` and `需求明确度 >= 8`, with no severe blocker forcing downgrade
- `medium`: total score `35-69`, or strong interest exists but budget/timeline/decision chain is still incomplete
- `low`: total score `< 35`, or severe blockers appear, such as explicit rejection, no budget, no plan, or obvious stalling

### Strong Signal Rules

- Up-weight these signals: explicit budget, explicit timeline, decision-maker appearance, PoC/trial request, quotation/contract request, implementation owner, or technical docking owner.
- Down-weight or penalize these signals: explicit rejection, no budget, no plan this quarter/year, repeated cooling language, obvious free-consulting behavior, or hard compliance/IT blockers.
- If the evidence is sparse, keep the judgment conservative and reduce confidence.

## Noise Handling

- Strip obvious system noise first: join/leave notices, recall notices, message delivery notices, and empty lines.
- Prefer lines likely spoken by the customer. If speaker identity is ambiguous, still score content-level signals conservatively.
- Do not invent budget, timeline, or decision details that do not appear in the source.
- If the file is noisy, extract the lines that carry need, timeline, budget, decision, risk, or next-step signals and ignore filler chatter.

## Few-Shot Examples

### Example 1: High Opportunity

Input cue:

```text
客户：这周先看方案，如果合适下周安排 PoC。预算大概 15 到 20 万。
客户技术负责人：想确认私有化部署和交付周期，大概多久能上线？
客户：如果价格合适，请今天先发报价和实施计划。
```

Expected shape:

```json
{
  "customer_opportunity_level": "high",
  "confidence": 80,
  "reasoning": "客户已明确 PoC、预算、报价和实施计划，需求和推进路径都比较清晰。"
}
```

### Example 2: Medium Opportunity

Input cue:

```text
客户：我们在看几家方案，想了解下能不能做工单和微信对接。
客户：目前还在调研阶段，预算和时间都没定，先发份资料吧。
```

Expected shape:

```json
{
  "customer_opportunity_level": "medium",
  "confidence": 60,
  "reasoning": "存在明确兴趣和部分场景，但仍处于比较方案阶段，预算和时间未定。"
}
```

### Example 3: Low Opportunity

Input cue:

```text
客户：先随便了解一下。
客户：今年暂时没有预算，项目也没排期。
客户：先不用约演示了，有需要我再联系你。
```

Expected shape:

```json
{
  "customer_opportunity_level": "low",
  "confidence": 88,
  "reasoning": "客户明确表示暂无预算和排期，且拒绝当前推进动作。"
}
```

## Resource Guide

- Use [scripts/analyze_customer_opportunity.py](scripts/analyze_customer_opportunity.py) for the actual scoring and output generation.
- Use [config/opportunity_rules.json](config/opportunity_rules.json) when adjusting keywords, weights, or strong-signal penalties.
- Use [references/scoring-rubric.md](references/scoring-rubric.md) when you need the detailed meaning of each dimension or want to justify a score.
- Use files in [examples](examples) for smoke tests and regression checks.

## Operating Rules

- Default to the script output instead of manually improvising a score when a file path is available.
- Keep the result conservative when evidence conflicts.
- If the content is too short, set low confidence and explicitly say `信息不足`.
- Preserve the original wording in `evidence` wherever possible, but keep the list short and high signal.
