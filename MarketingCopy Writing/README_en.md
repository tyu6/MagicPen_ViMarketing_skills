# MarketingCopy Writing Skill

## Overview

This Skill is designed for Chinese furniture companies expanding into the Indonesian market. It automatically generates multilingual marketing copy in Indonesian, English, and Chinese for a range of use cases, including e-commerce product pages, social media posts, poster copy, and other marketing materials.

It supports both text-based prompting and image-based generation.

---

## Directory Structure

```text
MarketingCopy Writing Skill/
|
+-- SKILL.md                           # Main Skill definition file
+-- README.md                          # Chinese / bilingual usage guide
+-- README_en.md                       # English usage guide
+-- references/                        # Reference knowledge base
|   +-- indonesian-marketing-phrases.md
|   +-- style-vocabulary.md
|   +-- platform-guidelines.md
|   +-- furniture-terminology.md
|   `-- translation-avoid-list.md
+-- templates/                         # Output templates
|   `-- output-template.md
`-- examples/                          # Example outputs
    +-- example-output.md
    `-- example-image-output.md
```

---

## Quick Start

### 1. Basic Inputs

| Field | Required | Description | Example |
|------|------|------|------|
| `product_name` | Yes | Product name | `"Scandinavian Teak Dining Table"` |
| `material` | Yes | Main material | `"100% solid teak wood"` |
| `style` | Yes | Design style | `"Natural"` / `"Nanyang"` / `"Minimalist"` |
| `core_selling_points` | Yes | Core selling points, 1 to 2 sentences | `"Handcrafted, natural wood grain"` |
| `usage` | No | Usage scenario | `"Dining room, family gatherings"` |
| `promotion_info` | No | Promotion details | `"Free shipping, 15% off"` |
| `target_tone` | No | Desired tone of voice | `"Premium"` / `"Cozy-natural"` / `"Promotional"` |
| `target_platform` | No | Target platform | `"Shopee"` / `"Instagram"` / `"Xiaohongshu"` |

### 2. Output Contents

- Multilingual e-commerce titles, with 2 to 3 options per language
- Five product selling points
- Product description copy
- Instagram and Facebook copy, including awareness and conversion versions
- Xiaohongshu-style copy
- Short poster lines
- Promotional messaging
- Optimization suggestions

---

## Key Features

### Indonesian Localization

- Avoids literal Chinese-style translation and produces copy that matches natural Indonesian usage
- Incorporates common Indonesian e-commerce terms such as `Ready stock`, `COD`, and `gratis ongkir`
- Supports local conversational expressions such as `bun`, `lho`, and `banget`

### Style Adaptation

- **Natural**: warm, organic, earth-tone oriented
- **Nanyang**: vintage, tropical, with rattan-inspired elements
- **Minimalist**: clean, modern, function-first

### Platform Adaptation

| Platform | Title Limit | Copy Characteristics |
|------|------|------|
| Shopee | 70 characters | Conversational, highlights value for money and ready stock |
| Tokopedia | 60 characters | More formal, emphasizes trust and quality |
| Instagram | No strict limit | Visual-first, interactive, lifestyle-oriented |
| Facebook | No strict limit | Community-friendly, suitable for longer copy |
| Xiaohongshu | 20 characters | Personal-review style, emoji-friendly |

### Rewrite Support

The Skill also supports follow-up rewriting requests such as:

- `Make it more conversational`
- `Make it feel more premium`
- `Make it more suitable for the Indonesian market`
- `Shorten it for poster use`
- `Turn it into a promotional tone`

---

## Reference Library

### `indonesian-marketing-phrases.md`

An Indonesian marketing phrase library that includes:

- Opening hooks
- Quality expressions
- Style vocabulary
- Urgency phrases
- Social media engagement phrases
- Common buyer Q&A

### `style-vocabulary.md`

A style vocabulary and imagery guide that defines:

- Tone characteristics for each style
- Indonesian, Chinese, and English keyword mappings
- Imagery association tables
- Example copy snippets

### `platform-guidelines.md`

Platform-specific copy guidelines, including:

- Character limits by platform
- Title formatting recommendations
- Hashtag strategies
- Content adaptation rules for different platforms

### `furniture-terminology.md`

A furniture terminology reference that provides:

- Furniture type mappings in Indonesian, Chinese, and English
- Material terminology
- Size expression standards
- Functional feature vocabulary

### `translation-avoid-list.md`

A translation pitfalls guide that lists:

- Common literal translation mistakes and fixes
- Overly formal expressions and their more natural alternatives
- Cultural sensitivity notes

---

## Example Use Cases

### Use Case 1: New Product Listing on Shopee

```text
Input:
- Product: Teak dining chair
- Material: 100% Indonesian teak
- Style: Minimalist
- Selling points: Mortise-and-tenon structure, formaldehyde-free finish
- Platform: Shopee

Output:
- 3 Shopee-optimized titles within 70 characters
- 5 selling points in a conversational tone with emojis
- Product description around 300 words
- Promotional messaging
```

### Use Case 2: Instagram Awareness Campaign

```text
Input:
- Product: Nanyang-style rattan sofa
- Material: Natural rattan + solid wood frame
- Style: Nanyang
- Selling points: Handwoven, vintage-inspired design
- Platform: Instagram
- Tone: Warm and natural

Output:
- IG Copy A for awareness and engagement
- IG Copy B for conversion and promotion
- Selected hashtags
- Short poster lines
```

### Use Case 3: Xiaohongshu Viral Note

```text
Input:
- Product: Nordic solid wood desk
- Material: Oak
- Style: Natural
- Selling points: Large tabletop, ideal for home office use
- Platform: Xiaohongshu

Output:
- Xiaohongshu title with emojis
- Review-style body copy
- Topic tags
- A version suitable for sharing in Moments
```

---

## Implementation Suggestions and Notes

### 1. Indonesian Output Quality

**Risk**: The model may generate Indonesian that sounds too formal or bookish.

**Suggested approach**:

- Explicitly request a conversational tone in the prompt
- Refer to the replacement rules in `translation-avoid-list.md`
- Add post-processing checks to replace overly formal expressions

### 2. Style Consistency

**Risk**: Different output sections may drift in tone or style.

**Suggested approach**:

- Decide on `style` and `tone` first, then share them across all output items
- Define style propagation rules clearly in the `Workflow` section of `SKILL.md`

### 3. Platform Limits

**Risk**: Generated titles may exceed platform character limits.

**Suggested approach**:

- Automatically check character count after generation
- Mark over-limit versions as alternatives and recommend compliant ones

### 4. Phrase Library Maintenance

**Suggestion**: Maintain a quarterly update process.

- Analyze best-selling copy on Shopee and Tokopedia
- Track trending furniture hashtags on Instagram
- Collect user feedback and refine phrasing accordingly

### 5. Multi-Version Output

**Suggested implementation**:

- Generate at least 2 to 3 title options per language
- Provide both awareness and conversion versions for social media copy
- Keep outputs diverse enough for A/B testing

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

- Visual analysis before copy generation
- Inferred style and mood from the image
- Multilingual copy generation without changing the existing text mode
- Safer claim handling when materials or dimensions are not fully visible

---

## Version History

| Version | Date | Update |
|------|------|------|
| 1.1.0 | 2026-04-09 | Added image-based marketing copy generation |
| 1.0.0 | 2026-04-05 | Initial release |

---

## Contact

If you have questions or suggestions, please contact the Skill maintenance team.

---

*This Skill is built specifically for furniture brands entering the Indonesian market and is under continuous improvement.*
