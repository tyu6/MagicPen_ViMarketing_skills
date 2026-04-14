# ViMarketing Skills

这是一个面向营销与客户线索处理的 OpenClaw Skill 集合仓库。

仓库中的内容主要分成两类：

- 客户对话处理：从聊天记录中提取客户信息、判断商机质量。
- 营销文案生成：为家具出海场景生成适合印尼和欧美市场的多语言营销文案。

如果你第一次打开这个仓库，建议先看本文件了解整体结构，再进入对应子目录查看更详细的 `README.md` 和 `SKILL.md`。

## 仓库包含什么

### 1. `CustomerInfo Extraction/`

客户对话信息提取 Skill。

它的作用是把销售、客服或商务沟通记录整理成适合 CRM 导入的结构化结果，支持导出：

- `JSON`
- `Excel (.xlsx)`
- `Markdown`

适合场景：

- 从客户聊天记录中提取姓名、公司、电话、邮箱、微信等字段
- 提取需求、预算、时间线、下一步动作等销售信息
- 批量处理客户对话文件

更详细的使用说明见：

- `CustomerInfo Extraction/README.md`
- `CustomerInfo Extraction/SKILL.md`

### 2. `CustomerInfo Classification/`

客户询盘分析相关目录。

这个目录当前主要包含一个核心子技能：

- `CustomerInfo Classification/CustomerInfo Classification/`：根据客户对话判断商机等级，输出 `high` / `medium` / `low`，并附带证据、风险和建议动作。

同时还包含一些辅助内容：

- `shared/`：文档读取公共代码，支持读取 `md`、`txt`、`doc`、`docx`、带文本层的 `pdf` 等输入
- `tmp-customere2e-info/`：临时复制的客户信息提取相关文件
- `tmp-verification/`：用于验证文档解析效果的样例文件和输出结果

适合场景：

- 销售跟进前快速判断客户质量
- 从历史沟通记录中筛选高潜力客户
- 对商机打分并输出可解释结论

更详细的使用说明见：

- `CustomerInfo Classification/README.md`
- `CustomerInfo Classification/CustomerInfo Classification/SKILL.md`

### 3. `MarketingCopy Writing/`

多语言营销文案生成 Skill。

这个技能主要为中国家具企业出海印尼市场设计，支持根据产品信息或产品图片生成：

- 印尼语文案
- 英语文案
- 中文文案

输出内容包括：

- 电商标题
- 产品卖点
- 详情页文案
- Instagram / Facebook 文案
- 小红书风格文案
- 海报短句
- 促销话术

适合场景：

- 家具产品上架 Shopee、Tokopedia
- 社媒推广与种草内容生成
- 海报、活动页、促销文案制作

更详细的使用说明见：

- `MarketingCopy Writing/README.md`
- `MarketingCopy Writing/SKILL.md`

## 推荐使用方式

### 作为 OpenClaw Skill 使用

如果这些目录已经放在 OpenClaw 的技能工作区中，可以直接按各自的 `SKILL.md` 触发对应技能。

### 作为脚本直接运行

部分目录提供了可直接执行的 Python 脚本，适合本地批处理或验证。

常见示例：

```bash
python "CustomerInfo Extraction/scripts/extract_customer_to_excel.py" "CustomerInfo Extraction/examples/complete-enterprise-dialogue.md"
python "CustomerInfo Classification/CustomerInfo Classification/scripts/analyze_customer_opportunity.py" "CustomerInfo Classification/CustomerInfo Classification/examples/high-opportunity.md"
```

## 环境要求

建议环境：

- Python 3.10+

按当前仓库内容，额外需要注意：

- 导出 `.xlsx` 时需要安装 `openpyxl`
- `pdf` 输入只支持带文本层的 PDF，不支持纯扫描件
- `.doc` 的解析是尽力处理，稳定性通常不如 `.docx`

如果需要导出 Excel，可先安装：

```bash
pip install openpyxl
```

## 该先看哪个目录

如果你的目标是：

- 提取客户资料并导入 CRM：看 `CustomerInfo Extraction/`
- 判断客户是不是高质量商机：看 `CustomerInfo Classification/`
- 生成多语言市场的家具营销文案：看 `MarketingCopy Writing/`

## 仓库说明

- 根目录 `README.md`：中文总览说明
- 根目录 `README_en.md`：英文总览说明
- 各子目录 `README.md` / `README_en.md`：对应技能的详细说明
- `LICENSE`：Apache License 2.0
