# 客户商机分级 Skill

## 概述

该目录包含一个可复用的  Skill，用于根据客户对话内容对商机质量进行分析和分级。

---

## 安装

如果该文件夹已经位于你的  skills 工作区中，则无需额外安装。

如果你希望 Codex 从默认全局 Skill 路径自动发现它，请将该文件夹放置或复制到：

- Windows：`%USERPROFILE%\\.codex\\skills\\customer-inquiry`

---

## 使用方式

直接运行分析器：

```bash
cd customer-inquiry
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md
```

同时生成 JSON 和 Markdown 输出：

```bash
cd customer-inquiry
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md --format both --output examples/high-opportunity.output.json --markdown-output examples/high-opportunity.output.md
```

---

## 内容说明

- `SKILL.md`：Codex Skill 指令与 few-shot 示例说明
- `scripts/analyze_customer_opportunity.py`：命令行分析脚本
- `config/opportunity_rules.json`：可调的信号与权重规则
- `references/scoring-rubric.md`：评分维度参考
- `examples/`：示例输入与输出

---

## 说明

- 默认输出格式为 JSON。
- 可通过 `--format markdown` 或 `--markdown-output` 生成 Markdown 摘要。
- 该脚本针对中文客户对话做了优化，同时也兼容 `PoC`、`SSO`、`API` 等混合英文术语。
