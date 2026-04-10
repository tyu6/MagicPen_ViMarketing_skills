# Multi-Language Marketing Copy Skill

## 多语言营销文案自动生成 Skill

---

## 概述 Overview

本 Skill 专为中国家具企业出海印尼市场设计,能够自动生成多语言营销文案,支持印尼语、英语、中文三种语言,覆盖电商详情页、社媒种草、海报素材等多种营销场景。

This Skill is designed for Chinese furniture companies expanding to the Indonesian market. It automatically generates multi-language marketing copy in Indonesian, English, and Chinese, covering e-commerce listings, social media content, poster copy, and more. It now supports both text-based prompting and image-based generation.

---

## 目录结构 Directory Structure

```
Multi-language marketing copy Skill/
│
├── SKILL.md                                    # Skill 主定义文件
│                                               # Main Skill definition file
│
├── README.md                                   # 使用说明 (本文件)
│                                               # Usage guide (this file)
│
├── references/                                 # 参考知识库
│   ├── indonesian-marketing-phrases.md        # 印尼语营销话术库
│   ├── style-vocabulary.md                    # 风格词库与意象指导
│   ├── platform-guidelines.md                 # 平台文案规范
│   ├── furniture-terminology.md               # 家具术语对照表
│   └── translation-avoid-list.md              # 翻译避坑指南
│
├── templates/                                  # 输出模板
│   └── output-template.md                     # 标准输出模板
│
└── examples/                                   # 示例输出
    └── example-output.md                      # 完整示例演示
```

---

## 快速开始 Quick Start

### 1. 基本输入 Basic Inputs

| 字段 | 必填 | 说明 | 示例 |
|------|------|------|------|
| product_name | ✅ | 产品名称 | "Scandinavian Teak Dining Table" |
| material | ✅ | 主材质 | "100% solid teak wood" |
| style | ✅ | 设计风格 | "Natural" / "Nanyang" / "Minimalist" |
| core_selling_points | ✅ | 核心卖点(1-2句) | "Handcrafted, natural wood grain" |
| usage | ⬜ | 使用场景 | "Dining room, family gatherings" |
| promotion_info | ⬜ | 促销信息 | "Free shipping, 15% off" |
| target_tone | ⬜ | 输出语气 | "Premium" / "Cozy-natural" / "Promotional" |
| target_platform | ⬜ | 目标平台 | "Shopee" / "Instagram" / "Xiaohongshu" |

### 2. 输出内容 Output Contents

- ✅ 多语言电商标题 (每语言2-3个备选)
- ✅ 5点产品卖点
- ✅ 产品详情描述
- ✅ Instagram/Facebook 文案 (种草型 + 转化型)
- ✅ 小红书风格文案
- ✅ 海报短句
- ✅ 促销话术
- ✅ 优化建议

---

## 核心特性 Key Features

### 🇮🇩 印尼语本地化优化

- 避免中式直译,输出符合印尼本地表达习惯
- 融入当地电商常用词汇 (Ready stock, COD, gratis ongkir)
- 支持"bun"、"lho"、"banget"等地道口语表达

### 🎨 风格适配

- **自然风 Natural**: 温暖、有机、大地色系
- **南洋风 Nanyang**: 复古、热带、藤编元素
- **简约风 Minimalist**: 干净、现代、功能至上

### 📱 平台适配

| 平台 | 标题限制 | 文案特点 |
|------|----------|----------|
| Shopee | 70字符 | 口语化、强调性价比和现货 |
| Tokopedia | 60字符 | 正式、强调信任和品质 |
| Instagram | 无限制 | 美感导向、互动性强 |
| Facebook | 无限制 | 社区感、长文案友好 |
| 小红书 | 20字符 | 个人测评、emojis丰富 |

### 🔄 改写支持

支持用户后续改写请求:
- `更口语一点` → 更亲切自然的表达
- `更高级一点` → 提升高端感
- `更适合印尼市场` → 强化本地化
- `缩短到海报可用` → 精简为短句
- `改成促销语气` → 增加紧迫感

---

## 参考知识库说明 Reference Library

### indonesian-marketing-phrases.md
印尼语营销话术库,包含:
- 开场钩子 (Opening hooks)
- 品质表达 (Quality expressions)
- 风格词汇 (Style vocabulary)
- 紧迫感话术 (Urgency phrases)
- 社媒互动语 (Social media engagement)
- 常见买家问答 (Common Q&A)

### style-vocabulary.md
风格词库与意象指导,详细定义:
- 每种风格的语调特点
- 印尼/中/英文关键词对照
- 意象联想表格
- 示例文案片段

### platform-guidelines.md
平台文案规范,包含:
- 各平台字符限制
- 标题格式建议
- Hashtag 策略
- 不同平台内容适配规则

### furniture-terminology.md
家具术语对照表,提供:
- 家具类型印尼/中/英文对照
- 材质术语
- 尺寸表达规范
- 功能特性词汇

### translation-avoid-list.md
翻译避坑指南,列出:
- 常见直译错误及修正
- 过于正式的表达 → 替换为口语化表达
- 文化敏感性注意事项

---

## 使用场景示例 Use Cases

### 场景1: 新品上架 Shopee

```
输入:
- 产品: 柚木餐椅
- 材质: 100%印尼柚木
- 风格: 简约风
- 卖点: 榫卯结构，无甲醛漆面
- 平台: Shopee

输出:
- 3个Shopee优化标题(70字符内)
- 5点卖点(口语化，带emoji)
- 产品详情(300字)
- 促销话术
```

### 场景2: Instagram 种草推广

```
输入:
- 产品: 南洋风藤编沙发
- 材质: 天然藤+实木框架
- 风格: 南洋风
- 卖点: 纯手工编织，复古设计
- 平台: Instagram
- 语气: 温馨自然

输出:
- IG文案A(种草型，互动性强)
- IG文案B(转化型，促销导向)
- 精选hashtag
- 海报短句
```

### 场景3: 小红书爆款笔记

```
输入:
- 产品: 北欧风实木书桌
- 材质: 橡木
- 风格: 自然风
- 卖点: 大桌板，适合居家办公
- 平台: 小红书

输出:
- 小红书标题(带emoji)
- 测评风格正文
- 话题标签
- 朋友圈分享版
```

---

## 实现建议与注意事项

### 1. 印尼语生成质量

**风险点**: AI模型可能产出过于书面化的印尼语

**建议方案**:
- 在 prompt 中明确要求使用 conversational tone
- 参考 translation-avoid-list.md 中的替换规则
- 后处理阶段检查并替换过于正式的表达

### 2. 风格一致性

**风险点**: 不同输出项之间风格可能不一致

**建议方案**:
- 先确定 style 和 tone，所有输出项共享同一风格参数
- 在 SKILL.md 的 Workflow 中明确风格传递规则

### 3. 平台限制

**风险点**: 生成的标题可能超出平台字符限制

**建议方案**:
- 在输出后自动检测字符数
- 超限版本标记为"备选"，推荐合规版本

### 4. 话术库更新

**建议**: 建立季度更新机制
- 分析 Shopee/Tokopedia 热销商品文案
- 追踪 Instagram 家具类 trending hashtag
- 收集用户反馈，优化表达

### 5. 多版本输出

**实现建议**:
- 每种语言至少输出 2-3 个标题备选
- 社媒文案提供"种草型"和"转化型"两个版本
- 保持版本多样性，便于用户 A/B 测试

---

## Image Mode

Use image-first generation when you already have a product photo and do not want to write a full product brief.

Recommended input:

```json
{
  "input_mode": "image",
  "reference_image": "./assets/sofa.jpg",
  "image_focus": "rattan texture and cozy tropical atmosphere",
  "visual_notes": "target Indonesia, premium but warm tone",
  "target_platform": "Instagram"
}
```

Image mode adds:

- Visual analysis before copywriting
- Inferred style and mood from the image
- Multi-language copy generation without changing the existing text mode
- Safer claim handling when materials or dimensions are not fully visible

## 版本历史 Version History

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.1.0 | 2026-04-09 | Added image-based marketing copy generation |
| 1.0.0 | 2026-04-05 | 初始版本发布 |

---

## 联系方式 Contact

如有问题或建议，请联系 Skill 维护团队。

---

*本 Skill 专为家具行业印尼市场出海场景设计，持续优化中。*
