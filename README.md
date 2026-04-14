# ViMarketing Skills

这是一个面向营销与客户线索处理场景的 Skill 仓库，当前包含 3 个正式 Skill：

1. `CustomerInfo Extraction/`
   从客户对话中抽取结构化客户资料，并导出 CRM 友好的 `JSON`、`Excel (.xlsx)`、`Markdown`。
2. `CustomerInfo Classification/`
   根据客户对话评估商机等级，输出 `high` / `medium` / `low`，并附带证据、风险和建议动作。
3. `MarketingCopy Writing/`
   面向家具出海场景生成印尼语、英语、中文营销文案，支持文本输入和图片输入。

如果你是第一次使用这个仓库，建议先看本文件，再进入对应子目录查看 `README.md` 和 `SKILL.md`。

## 目录说明

### `CustomerInfo Extraction/`

客户对话信息提取 Skill。

适合场景：

- 从聊天记录中提取姓名、公司、电话、邮箱、微信等字段
- 提取需求、预算、时间线、下一步动作等销售信息
- 批量处理客户对话文件

详细说明见：

- `CustomerInfo Extraction/README.md`
- `CustomerInfo Extraction/SKILL.md`

### `CustomerInfo Classification/`

客户商机分级 Skill。

当前 `CustomerInfo Classification/` 目录本身就是正式 skill 根目录，不再使用旧的嵌套路径。

适合场景：

- 销售跟进前快速判断客户质量
- 从历史沟通记录中筛选高潜力客户
- 对商机打分并输出可解释结论

目录中还包含一些开发或验证用内容，例如 `shared/`、`tmp-customere2e-info/`、`tmp-verification/`。这些目录不是安装或调用正式 skill 的必需内容。

详细说明见：

- `CustomerInfo Classification/README.md`
- `CustomerInfo Classification/SKILL.md`

### `MarketingCopy Writing/`

多语言营销文案生成 Skill。

适合场景：

- 家具产品上架 Shopee、Tokopedia
- 社媒推广与种草内容生成
- 海报、活动页、促销文案制作
- 基于产品图做 image-first 文案生成

详细说明见：

- `MarketingCopy Writing/README.md`
- `MarketingCopy Writing/SKILL.md`

## 推荐使用方式

### 作为 Skill 使用

如果这些目录已经放在 OpenClaw 的 skills 工作区，可以直接按各自的 `SKILL.md` 调用。

### 作为脚本直接运行

部分目录提供了可直接运行的 Python 脚本，适合本地批处理或验证。

示例：

```bash
python "CustomerInfo Extraction/scripts/extract_customer_to_excel.py" "CustomerInfo Extraction/examples/complete-enterprise-dialogue.md"
python "CustomerInfo Classification/scripts/analyze_customer_opportunity.py" "CustomerInfo Classification/examples/high-opportunity.md"
```

## 环境要求

建议环境：

- Python 3.10+

按当前仓库内容，需要注意：

- 导出 `.xlsx` 需要安装 `openpyxl`
- `pdf` 输入仅支持带文本层的 PDF
- `.doc` 解析为 best-effort，稳定性通常不如 `.docx`

如果需要 Excel 导出，可先安装：

```bash
pip install openpyxl
```

## 我该先看哪个目录

如果你的目标是：

- 提取客户资料并导入 CRM：看 `CustomerInfo Extraction/`
- 判断客户是否是高质量商机：看 `CustomerInfo Classification/`
- 生成面向印尼市场的家具营销文案：看 `MarketingCopy Writing/`

## 仓库说明

- `README.md`：中文总览
- `README_en.md`：英文总览
- 各子目录 `README.md` / `README_en.md`：对应 skill 的详细说明
- `LICENSE`：Apache License 2.0
