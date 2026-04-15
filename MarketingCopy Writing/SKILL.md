---
name: MarketingCopy Writing
description: Generate professional multi-language marketing copy for furniture e-commerce from text prompts or product images, supporting Indonesian, English, and Chinese. Outputs include e-commerce titles, selling points, product details, social media posts, poster copy, and promotional scripts tailored for the Indonesian market.
version: 1.1.0
user-invocable: true
argument-hint: "[product-name] [material] [style] [selling-points]"
metadata:
  author: ViMarketing
  category: marketing
  tags:
    - furniture
    - e-commerce
    - social-media
    - multi-language
    - indonesian-market
  supported_platforms:
    - Shopee
    - Tokopedia
    - Instagram
    - Facebook
    - Xiaohongshu
  supported_languages:
    - Indonesian
    - English
    - Chinese
---

# MarketingCopy Writing Skill

## Purpose

Generate ready-to-use marketing copy for furniture products in Indonesian, English, and Chinese. The skill supports both text-first prompting and image-first generation, with Indonesian market localization as a core requirement.

## Target Users

- Furniture e-commerce operators
- Marketing teams
- International trade sales
- Small and medium merchants

## Applicable Scenarios

- E-commerce product listings on Shopee or Tokopedia
- Social media content for Instagram, Facebook, and Xiaohongshu
- Promotional campaigns, flash sales, and poster copy
- Cross-border furniture sales for the Indonesian market

## Required Inputs

### Text Mode

| Field | Required | Description | Example |
| --- | --- | --- | --- |
| `input_mode` | No | Defaults to `text` | `"text"` |
| `product_name` | Yes | Product name or identifier | `"Solid Teak Dining Table"` |
| `material` | Yes | Primary material | `"100% solid teak wood"` |
| `style` | Yes | Design style | `"Natural"` |
| `core_selling_points` | Yes | One or two key selling points | `"Handcrafted, durable, natural wood grain"` |
| `usage` | No | Usage scenario | `"Dining room, family gatherings"` |
| `promotion_info` | No | Promotion details | `"Free shipping, 20% off this week"` |
| `target_tone` | No | Desired tone | `"Cozy-natural"` |
| `target_platform` | No | Target platform | `"Shopee"` |
| `output_versions` | No | Number of versions to generate | `2` |

### Image Mode

| Field | Required | Description | Example |
| --- | --- | --- | --- |
| `input_mode` | Yes | Must be `image` | `"image"` |
| `reference_image` | Yes | Attached image, local image path, or image URL | `"D:/path/to/product.jpg"` |
| `image_focus` | No | Which visual elements to emphasize | `"tabletop texture and premium dining atmosphere"` |
| `visual_notes` | No | User-provided context for missing details | `"Seats 6-8 people, target market is Indonesia"` |
| `promotion_info` | No | Promotion details | `"Free shipping this week"` |
| `target_tone` | No | Desired tone | `"Premium"` |
| `target_platform` | No | Target platform | `"Instagram"` |
| `output_versions` | No | Number of versions to generate | `2` |

### Input Rules

1. Keep text mode as the default when `input_mode` is omitted
2. When `input_mode` is `image`, infer product attributes from the image first, then generate copy
3. If both text and image are provided, treat the text as the source of truth and use the image only to enrich visual detail
4. Do not assume the repository ships with bundled sample images; `reference_image` should be a user-provided attachment, local path, or URL

## Workflow

### Step 1: Input Validation and Enrichment

1. Detect `input_mode`
2. Validate required fields for the selected mode
3. Apply sensible defaults for missing optional fields
4. Infer additional selling points from material and style combinations

### Step 2: Visual Analysis for Image Mode

1. Identify the most likely product category from the image
2. Extract visible attributes only: shape, color tone, finish, construction cues, room setting, and mood
3. Infer likely style keywords from the visual composition
4. Mark uncertain observations clearly and avoid converting guesses into hard claims

### Step 3: Style Analysis

1. Parse the style field and match it to the relevant style vocabulary
2. Load appropriate tone modifiers and imagery keywords
3. Select useful phrases from the Indonesian furniture marketing references

### Step 4: Multi-Language Copy Generation

Generate output for Indonesian, English, and Chinese.

Include:

- E-commerce titles: 2 to 3 candidates per language
- Five selling points
- Product details
- Instagram and Facebook captions
- Xiaohongshu-style copy when relevant
- Poster short copy
- Promotional scripts

### Step 5: Quality Review

1. Check Indonesian copy for natural expression and avoid direct translation artifacts
2. Verify platform-specific character limits
3. Ensure style consistency across variations
4. In image mode, verify that material, size, and construction claims are either user-confirmed or visually supported

### Step 6: Output Formatting

1. Organize by language, then by usage type
2. Keep the output ready to copy
3. Append optimization suggestions
4. In image mode, prepend a short visual analysis summary

## Output Format

Expected sections:

- Product summary
- Visual analysis summary when `input_mode = image`
- Indonesian copy pack
- English copy pack
- Chinese copy pack
- Optimization tips
- Rewrite instructions

You may adapt the exact formatting, but keep the structure easy to scan and easy to reuse.

## Style Rules

### Style Mapping

| Style | Tone Keywords | Imagery | Indonesian Keywords |
| --- | --- | --- | --- |
| Natural | Warm, organic, earthy | Sunlight, wood grain, nature | `natural`, `hangat`, `organik`, `kayu asli` |
| Nanyang | Classic, heritage, tropical | Rattan, vintage, tropical vibes | `klasik`, `vintage`, `tropis`, `rotan` |
| Minimalist | Clean, modern, functional | Clean lines, neutral tones, sleek details | `minimalis`, `modern`, `simpel`, `elegan` |
| Modern | Bold, contemporary, stylish | Geometric, trendy, statement pieces | `kontemporer`, `stylish`, `trend` |

### Tone Modifiers

| Tone | Characteristics | Indonesian Indicators |
| --- | --- | --- |
| Premium | Sophisticated, exclusive | `eksklusif`, `premium`, `mewah` |
| Cozy-natural | Warm, family-oriented | `nyaman`, `hangat`, `rumah idaman` |
| Concise | Direct, feature-focused | `praktis`, `efisien` |
| Promotional | Urgent, value-focused | `diskon`, `promo`, `terbatas`, `hemat` |

## Platform-Specific Rules

### Shopee

- Title max: 70 characters
- Highlight value, availability, and authenticity
- Use emoji sparingly

### Tokopedia

- Title max: 60 characters
- More formal tone preferred
- Detailed specifications are valued

### Instagram

- Caption target: 150 to 300 words
- Strong first line
- 5 to 15 hashtags

### Facebook

- Longer captions are acceptable
- Conversational tone works well

### Xiaohongshu

- Short, catchy title
- Review or atmosphere style
- Emoji and hashtags are expected

## Indonesian Localization Guidelines

1. Avoid direct translation patterns
2. Prefer local e-commerce vocabulary where appropriate
3. Conversational tone is usually better than stiff formal copy
4. Keep platform-specific Indonesian phrasing natural and credible
5. Use furniture terms consistently, such as `meja`, `kursi`, `sofa`, and `kayu jati`

## Guardrails

### Do Not Generate

- False claims about materials, certifications, or dimensions
- Prices that contradict the user's real pricing
- Misleading competitor comparisons
- Culturally insensitive references

### Image-Based Claims

- Do not invent hidden features, exact materials, certifications, or exact dimensions from the image alone
- If evidence is incomplete, use cautious phrasing
- If the image contains multiple products, focus on the most prominent one unless the user specifies otherwise

## Rewrite Command Handling

When the user asks for revisions, support transformations such as:

- `Make it more conversational`
- `Make it more premium`
- `Better for Indonesian market`
- `Shorten for poster`
- `Change to promotional tone`

## Reference Files

- `references/indonesian-marketing-phrases.md`
- `references/style-vocabulary.md`
- `references/platform-guidelines.md`
- `references/furniture-terminology.md`
- `references/translation-avoid-list.md`

## Example Usage

### Text-First Example

```json
{
  "product_name": "Scandinavian Teak Dining Table",
  "material": "100% solid teak wood",
  "style": "Natural",
  "core_selling_points": "Handcrafted by artisans, natural wood grain patterns, seats 6-8 people",
  "usage": "Dining room, family gatherings, dinner parties",
  "promotion_info": "Free shipping to Jabodetabek, 15% off for first 50 orders",
  "target_tone": "Cozy-natural",
  "target_platform": "Shopee"
}
```

See `examples/example-output.md` for a full sample.

### Image-First Example

```json
{
  "input_mode": "image",
  "reference_image": "D:/path/to/product.jpg",
  "image_focus": "highlight the warm wood texture and family dining atmosphere",
  "visual_notes": "target Indonesia, tone should feel premium but approachable",
  "promotion_info": "Free shipping in Jakarta this week",
  "target_tone": "Cozy-natural",
  "target_platform": "Instagram"
}
```

Expected behavior:

1. Analyze the image and identify the most likely furniture product
2. Infer style and atmosphere from visible cues
3. Generate the same multi-language output pack without requiring a full text-only brief

See `examples/example-image-output.md` for an image-based output example.
