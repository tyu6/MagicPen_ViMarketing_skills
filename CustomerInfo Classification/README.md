# CustomerInfo Classification Skill

当前目录本身就是 `CustomerInfo Classification` 的正式 skill 根目录。

## 安装

将当前目录直接复制到 OpenClaw 的 skills 目录即可，例如：

- Windows：`%USERPROFILE%\\.openclaw\\skills\\CustomerInfo Classification`

这个 skill 已经自包含，不依赖同级 `shared/` 目录才能运行。

## 使用

在 skill 根目录执行：

```bash
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md
```

同时生成 JSON 和 Markdown：

```bash
python scripts/analyze_customer_opportunity.py examples/high-opportunity.md --format both --output examples/high-opportunity.output.json --markdown-output examples/high-opportunity.output.md
```

## 目录结构

- `SKILL.md`：Skill 指令与 few-shot 说明
- `agents/openai.yaml`：Skill 展示元数据
- `scripts/analyze_customer_opportunity.py`：命令行分析脚本
- `scripts/document_input.py`：内置文档读取模块
- `config/opportunity_rules.json`：可调的信号与权重规则
- `references/scoring-rubric.md`：评分维度参考
- `examples/`：示例输入与输出

## 说明

- 默认输出格式为 `JSON`
- 可通过 `--format markdown` 或 `--markdown-output` 生成 Markdown 摘要
- 输入支持 `.md`、`.txt`、`.doc`、`.docx` 与带文本层的 `.pdf`
- 分析器主要针对中文客户对话优化，同时兼容 `PoC`、`SSO`、`API` 等混合术语
- 当前工作区中的 `shared/`、`tmp-customere2e-info/`、`tmp-verification/` 主要用于开发或验证，不是安装这个正式 skill 的必需内容
