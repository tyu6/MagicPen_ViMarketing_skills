# MarketingCopy Writing Skill

## 概述

这个 Skill 面向中国家具企业出海印尼市场的营销场景，可自动生成印尼语、英语、中文三种语言的营销文案，覆盖电商详情页、社媒文案、海报短句等常见使用场景。

它同时支持：

- 文本输入模式
- 图片优先模式

## 目录结构

```text
MarketingCopy Writing/
├── SKILL.md
├── README.md
├── README_en.md
├── references/
│   ├── indonesian-marketing-phrases.md
│   ├── style-vocabulary.md
│   ├── platform-guidelines.md
│   ├── furniture-terminology.md
│   └── translation-avoid-list.md
├── templates/
│   └── output-template.md
└── examples/
    ├── example-output.md
    └── example-image-output.md
```

## 快速开始

### 基本文本输入

| 字段 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- |
| `product_name` | 是 | 产品名称 | `"Scandinavian Teak Dining Table"` |
| `material` | 是 | 主要材质 | `"100% solid teak wood"` |
| `style` | 是 | 风格 | `"Natural"` / `"Nanyang"` / `"Minimalist"` |
| `core_selling_points` | 是 | 核心卖点 | `"Handcrafted, natural wood grain"` |
| `usage` | 否 | 使用场景 | `"Dining room, family gatherings"` |
| `promotion_info` | 否 | 促销信息 | `"Free shipping, 15% off"` |
| `target_tone` | 否 | 目标语气 | `"Premium"` / `"Cozy-natural"` / `"Promotional"` |
| `target_platform` | 否 | 目标平台 | `"Shopee"` / `"Instagram"` / `"Xiaohongshu"` |

### 输出内容

- 多语言电商标题，每种语言 2 到 3 个备选
- 5 条产品卖点
- 产品详情文案
- Instagram / Facebook 文案
- 小红书风格文案
- 海报短句
- 促销话术
- 优化建议

## 核心特性

### 印尼语本地化

- 避免中式直译
- 优先使用更自然的印尼本地电商表达
- 结合印尼家具营销常见口吻和平台用语

### 风格适配

- `Natural`：温暖、自然、有机
- `Nanyang`：复古、热带、藤编气质
- `Minimalist`：干净、现代、功能导向
- `Modern`：时尚、当代、强调设计感

### 平台适配

| 平台 | 标题限制 | 文案特点 |
| --- | --- | --- |
| Shopee | 70 字符 | 口语化，强调性价比和现货 |
| Tokopedia | 60 字符 | 更正式，强调信任和品质 |
| Instagram | 无严格限制 | 视觉导向、互动感强 |
| Facebook | 无严格限制 | 适合更长文案 |
| Xiaohongshu | 约 15 到 20 字标题 | 强调氛围感与种草感 |

## 图片模式

当你已经有产品图，但不想手写完整产品 brief 时，可以使用图片优先模式。

推荐输入：

```json
{
  "input_mode": "image",
  "reference_image": "D:/path/to/product.jpg",
  "image_focus": "rattan texture and cozy tropical atmosphere",
  "visual_notes": "target Indonesia, premium but warm tone",
  "target_platform": "Instagram"
}
```

说明：

- 仓库中不附带固定演示图片，`reference_image` 请传你自己的本地路径、附件或图片 URL
- 图片模式会先做视觉属性总结，再生成文案
- 对材质、尺寸、认证等不可见信息会保持保守表达

## 参考知识库

- `references/indonesian-marketing-phrases.md`
- `references/style-vocabulary.md`
- `references/platform-guidelines.md`
- `references/furniture-terminology.md`
- `references/translation-avoid-list.md`

## 示例场景

### 场景 1：Shopee 新品上架

- 产品：柚木餐桌
- 材质：100% 实木柚木
- 风格：Natural
- 卖点：手工制作、木纹自然、适合 6 至 8 人
- 平台：Shopee

### 场景 2：Instagram 种草

- 产品：南洋风藤编沙发
- 材质：天然藤 + 实木框架
- 风格：Nanyang
- 平台：Instagram
- 语气：温暖自然

### 场景 3：图片优先生成

- 已有产品图
- 希望先从视觉元素推断风格与氛围
- 输出印尼市场导向的多语言营销文案

## 版本历史

| 版本 | 日期 | 更新内容 |
| --- | --- | --- |
| 1.1.0 | 2026-04-09 | 增加图片优先模式 |
| 1.0.0 | 2026-04-05 | 初始版本 |
