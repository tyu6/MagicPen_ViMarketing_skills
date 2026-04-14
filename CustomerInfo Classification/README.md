# CustomerInfo Classification Skill

## 概述

该目录是 `CustomerInfo Classification` 的工作目录，核心 OpenClaw Skill 位于当前目录下的 `CustomerInfo Classification/` 子目录，用于根据客户对话内容对商机质量进行分析和分级。

---

## 安装

如果该文件夹已经位于你的 OpenClaw skills 工作区中，则无需额外安装。

如果你希望 OpenClaw 从默认全局 Skill 路径自动发现它，请将当前目录下包含 `SKILL.md` 的 `CustomerInfo Classification/` 子目录放置或复制到：

- Windows：`%USERPROFILE%\\.openclaw\\skills\\CustomerInfo Classification`

---

## 使用方式

进入当前目录下的 `CustomerInfo Classification/` 子目录后，直接运行分析器：

```bash
cd "CustomerInfo Classification"
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md
```

同时生成 JSON 和 Markdown 输出：

```bash
cd "CustomerInfo Classification"
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md --format both --output examples/high-opportunity.output.json --markdown-output examples/high-opportunity.output.md
```

---

## 内容说明

- `CustomerInfo Classification/SKILL.md`：OpenClaw Skill 指令与 few-shot 示例说明
- `CustomerInfo Classification/scripts/analyze_customer_opportunity.py`：命令行分析脚本
- `CustomerInfo Classification/config/opportunity_rules.json`：可调的信号与权重规则
- `CustomerInfo Classification/references/scoring-rubric.md`：评分维度参考
- `CustomerInfo Classification/examples/`：示例输入与输出

---

## 说明

- 默认输出格式为 JSON。
- 可通过 `--format markdown` 或 `--markdown-output` 生成 Markdown 摘要。
- 该脚本针对中文客户对话做了优化，同时也兼容 `PoC`、`SSO`、`API` 等混合英文术语。
