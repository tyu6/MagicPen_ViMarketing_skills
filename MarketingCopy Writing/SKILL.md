---
name: MarketingCopy Writing
description: Generate professional multi-language marketing copy for furniture e-commerce from text prompts or product images, supporting Indonesian, English, and Chinese. Outputs include e-commerce titles, selling points, product details, social media posts, poster copy, and promotional scripts tailored for Indonesian market.
version: 1.1.0
user-invocable: true
argument-hint: "[product-name] [material] [style] [selling-points]"
metadata:
  author: OpenClaw
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

This Skill generates professional, ready-to-use marketing copy for furniture products in multiple languages (Indonesian, English, Chinese). It supports both text-first prompting and image-first generation, with Indonesian market localization that keeps the copy natural and native-level.

## Target Users

- Furniture e-commerce operators
- Marketing teams
- International trade sales
- Small and medium merchants

## Applicable Scenarios

- E-commerce product listing (Shopee, Tokopedia)
- Social media marketing (Instagram, Facebook, Xiaohongshu)
- Promotional campaigns and flash sales
- Print/ digital poster creation
- Cross-border furniture sales

---

## Required Inputs

### Text Mode

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| input_mode | No | `text` by default | `"text"` |
| product_name | Yes | Product name/identifier | "Solid Teak Dining Table" |
| material | Yes | Primary material | "100% solid teak wood" |
| style | Yes | Design style (Natural/Nanyang/Minimalist/Modern) | "Nanyang style" |
| core_selling_points | Yes | 1-2 key selling points | "Handcrafted, durable, natural wood grain" |
| usage | No | Usage scenario | "Dining room, family gatherings" |
| promotion_info | No | Current promotions | "Free shipping, 20% off this week" |
| target_tone | No | Output tone (Premium/Cozy-Concise/Promotional) | "Cozy-natural" |
| target_platform | No | Target platform (Shopee/Tokopedia/IG/FB/Xiaohongshu) | "Shopee" |
| output_versions | No | Number of versions to generate (default: 2) | 2 |

### Image Mode

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| input_mode | Yes | Must be `image` for image-first generation | `"image"` |
| reference_image | Yes | Attached image, local image path, or image URL | `"./assets/teak-dining-table.jpg"` |
| image_focus | No | Which visual elements to emphasize | `"tabletop texture and premium dining atmosphere"` |
| visual_notes | No | User-provided context when the image is incomplete | `"Seats 6-8 people, target market is Indonesia"` |
| promotion_info | No | Current promotions | `"Free shipping this week"` |
| target_tone | No | Output tone | `"Premium"` |
| target_platform | No | Target platform | `"Instagram"` |
| output_versions | No | Number of versions to generate (default: 2) | 2 |

### Input Rules

1. Keep the current text mode unchanged when `input_mode` is omitted or set to `text`.
2. When `input_mode` is `image`, infer product attributes from the image first, then generate copy.
3. If both text and image are provided, treat the text as the source of truth and use the image to enrich visual detail.

---

## Workflow

### Step 1: Input Validation & Enhancement

1. Detect `input_mode` (`text` by default, `image` when an image is supplied as the primary source)
2. Validate the required fields for the selected mode
3. If optional fields are missing, use intelligent defaults based on product type
4. Infer additional selling points from material and style combinations

### Step 2: Visual Analysis for Image Mode

1. Identify the product category from the image
2. Extract visible attributes only: shape, color tone, finish, construction cues, room setting, and styling mood
3. Infer likely style keywords from the visual composition
4. Mark uncertain observations clearly and avoid converting guesses into hard claims
5. Build a structured attribute summary that can feed the same copy-generation pipeline used by text mode

### Step 3: Style Analysis

1. Parse the style field and match to corresponding style vocabulary
2. Load appropriate tone modifiers and imagery keywords
3. Select relevant phrases from the 2026 Indonesian Furniture Phrase Bank

### Step 4: Multi-Language Copy Generation

For each target language, generate:

#### E-commerce Copy
- **Title**: 2-3 candidates per language, platform-optimized (Shopee: 70 chars max, Tokopedia: 60 chars)
- **5 Selling Points**: Bullet format, each 20-40 words
- **Product Details**: 150-300 words, conversion-focused

#### Social Media Copy
- **Instagram/Facebook**: 2 versions (Engagement-focused vs. Conversion-focused)
- **Xiaohongshu**: Native platform style with emojis and hashtags

#### Marketing Assets
- **Poster Short Copy**: 1-2 impactful sentences
- **Promotional Scripts**: 2-3 urgency-driven phrases

### Step 5: Quality Review

1. Check Indonesian copy for natural expression (avoid direct translation patterns)
2. Verify platform-specific character limits
3. Ensure style consistency across all copy variations
4. In image mode, verify that all material, size, and construction claims are either user-confirmed or visibly supported
5. Prefer cautious phrasing such as "looks like", "natural wood tone", or "appears handcrafted" when certainty is limited

### Step 6: Output Formatting

1. Organize by language → by usage type
2. Include "ready-to-copy" formatting markers
3. Append optimization suggestions
4. When image mode is used, prepend a short visual analysis summary before the copy sections

---

## Output Format

```
================================================================================
                    MarketingCopy Writing
================================================================================

PRODUCT: [Product Name]
INPUT MODE: [text | image]
STYLE: [Style]
TARGET PLATFORM: [Platform(s)]
GENERATED: [Timestamp]

VISUAL ANALYSIS SUMMARY: [Only when image mode is used]
- Product type: [What is visible]
- Visible materials/finish: [Only visually supported claims]
- Scene/mood: [Lifestyle cues from the image]
- Confidence notes: [Uncertain elements or missing details]

================================================================================
                           【 INDONESIAN / BAHASA INDONESIA 】
================================================================================

▸ E-COMMERCE LISTING
─────────────────────────────────────────────────────────────────────────────

【 JUDUL PRODUK 】
Option 1: [Title]
Option 2: [Title]
Option 3: [Title]

【 5 KEUNGGULAN PRODUK 】
1. [Selling point 1]
2. [Selling point 2]
3. [Selling point 3]
4. [Selling point 4]
5. [Selling point 5]

【 DETAIL PRODUK 】
[Product description paragraph]

▸ SOCIAL MEDIA
─────────────────────────────────────────────────────────────────────────────

【 INSTAGRAM / FACEBOOK 】
Version A (Engagement Style):
[Caption with hashtags]

Version B (Conversion Style):
[Caption with call-to-action]

【 XIAOHONGSHU STYLE 】
[Chinese copy with emojis and hashtags]

▸ MARKETING ASSETS
─────────────────────────────────────────────────────────────────────────────

【 POSTER COPY 】
• [Short impactful line 1]
• [Short impactful line 2]

【 PROMOTIONAL SCRIPTS 】
• " [Promo phrase 1]"
• " [Promo phrase 2]"
• " [Promo phrase 3]"

================================================================================
                           【 ENGLISH 】
================================================================================
[Same structure as Indonesian section]

================================================================================
                           【 CHINESE / 中文 】
================================================================================
[Same structure as Indonesian section]

================================================================================
                           【 OPTIMIZATION TIPS 】
================================================================================
• [Tip 1]
• [Tip 2]
• [Tip 3]

================================================================================
                           【 REWRITE INSTRUCTIONS 】
================================================================================
You can request revisions using these commands:
• "更口语一点" → Make it more conversational
• "更高级一点" → Make it more premium
• "更适合印尼市场" → Better adapted for Indonesian market
• "缩短到海报可用" → Shorten for poster use
• "改成促销语气" → Change to promotional tone
```

---

## Style Rules

### Style Mapping

| Style | Tone Keywords | Imagery | Indonesian Keywords |
|-------|---------------|---------|---------------------|
| Natural (自然风) | Warm, organic, earthy | Sunlight, wood grain, nature | natural, hangat, organik, kayu asli |
| Nanyang (南洋风) | Classic, heritage, tropical | Rattan, vintage, tropical vibes | klasik, vintage, tropis, rotan |
| Minimalist (简约风) | Clean, modern, functional | Clean lines, neutral, sleek | minimalis, modern, simpel, elegan |
| Modern (现代风) | Bold, contemporary, stylish | Geometric, trendy, statement | kontemporer, stylish, trend |

### Tone Modifiers

| Tone | Characteristics | Indonesian Indicators |
|------|-----------------|----------------------|
| Premium (高级感) | Sophisticated, exclusive vocabulary | eksklusif, premium, mewah, berkualitas tinggi |
| Cozy-natural (温馨自然) | Warm, family-oriented, relatable | nyaman, hangat, keluarga, rumah idaman |
| Concise (简洁利落) | Direct, feature-focused, efficient | praktis, efisien, langsung to the point |
| Promotional (促销感强) | Urgent, value-focused, action-oriented | diskon, promo, terbatas, murah, hemat |

---

## Platform-Specific Rules

### Shopee (Indonesia)
- Title max: 70 characters
- Include keywords: termurah, terlaris, ready stock
- Use emoji sparingly (max 3 in title)
- Selling points: focus on value and authenticity

### Tokopedia (Indonesia)
- Title max: 60 characters
- Emphasize: original, bergaransi, rating tinggi
- More formal tone preferred
- Detailed specifications valued

### Instagram
- Caption: 150-300 words optimal
- Include 5-15 hashtags
- Strong opening hook (first line visible)
- Call-to-action in bio reference

### Facebook
- Longer captions work (up to 500 words)
- Community tone, conversational
- Include links and calls-to-action
- Less hashtag-heavy than IG

### Xiaohongshu (小红书)
- Title: 15-20 characters with emoji
- Content: Review/atmosphere style
- Must include emojis (8-12 throughout)
- Hashtags: 5-10 relevant tags
- Focus: 避坑, 种草, 氛围感

---

## Indonesian Localization Guidelines

### Critical Rules for Natural Indonesian Copy

1. **Avoid Direct Translation Patterns**
   - ❌ "Meja makan ini memiliki kualitas yang sangat baik"
   - ✅ "Meja makan berkualitas, awet bertahun-tahun!"

2. **Use Local Marketing Vocabulary**
   - Prefer "ga pake lama" over "segera" for urgency
   - Use "kece badai" for trendy/stylish products
   - "Bikin betah di rumah" for comfort-focused items

3. **Conversational Tone is Preferred**
   - Indonesian e-commerce buyers respond to friendly, chatty tone
   - Use "Kalian" or address customer directly
   - Exclamation points and emphasis words (banget, lho, dong)

4. **Platform-Specific Indonesian Expressions**

   | Platform | Common Phrases |
   |----------|----------------|
   | Shopee | Ready stock, COD, gratis ongkir, flash sale |
   | Tokopedia | Original 100%, bisa_cod, pengiriman cepat |
   | IG | Yuk dicek, swipe up, link di bio, DM for order |
   | FB | Hubungi kami, stok terbatas, buruan sebelum habis |

5. **Furniture-Specific Indonesian Terms**
   - Use "meja" not "table" for table
   - "Kursi" for chair, "sofa" for sofa
   - "Kayu jati" for teak wood (high value indicator)
   - "Full kayu" instead of "100% wood"

---

## Guardrails

### Content Safety

1. **Do NOT generate:**
   - False claims about materials or certifications
   - Prices that contradict user's actual pricing
   - Competitor comparisons or misleading claims
   - Cultural insensitive references

2. **Material Claims**
   - Only state materials user has confirmed
   - Use "natural wood finish" if material type unclear
   - Avoid "authentic antique" unless user specifies

3. **Cultural Sensitivity**
   - Respect Indonesian cultural values
   - Avoid references to gambling, alcohol, or sensitive topics
   - Consider Muslim-majority market (no alcohol imagery references)

4. **Image-Based Claims**
   - Do not invent dimensions, certifications, hidden features, or exact materials from the image alone
   - Do not claim "solid teak", "waterproof", "export grade", or similar unless the user confirms it or the evidence is explicit
   - If the image contains multiple products, focus on the most prominent item unless the user specifies otherwise

### Quality Standards

1. All copy must be:
   - Grammatically correct in target language
   - Free of machine translation artifacts
   - Appropriate tone for platform
   - Within character limits

2. At least 2 version options required for:
   - Product titles
   - Social media captions

3. For image mode specifically:
   - Separate observable facts from inferred style language
   - State uncertainty briefly when needed instead of fabricating certainty
   - Keep promotional language grounded in what the image actually supports

---

## Rewrite Command Handling

When user requests revisions, apply these transformations:

| Command | Action |
|---------|--------|
| 更口语一点 / Make it more conversational | Use casual Indonesian expressions, add "lho", "dong", "banget" |
| 更高级一点 / Make it more premium | Use sophisticated vocabulary, emphasize exclusivity |
| 更适合印尼市场 / Better for Indonesian market | Apply localization rules, use local expressions |
| 缩短到海报可用 / Shorten for poster | Reduce to 1-2 impactful sentences |
| 改成促销语气 / Change to promotional tone | Add urgency words, time-limited phrases, value emphasis |

---

## Reference Files

This Skill references the following knowledge base:

- `references/indonesian-marketing-phrases.md` - 2026 Indonesian Furniture Marketing Phrase Bank
- `references/style-vocabulary.md` - Style-specific vocabulary and imagery
- `references/platform-guidelines.md` - Platform-specific copy requirements
- `references/furniture-terminology.md` - Furniture industry terminology
- `references/translation-avoid-list.md` - Common translation errors to avoid

---

## Example Usage

```
User Input:
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

[See examples/example-output.md for complete output demonstration]
```

### Image-First Example

```
User Input:
{
  "input_mode": "image",
  "reference_image": "./assets/teak-dining-room.jpg",
  "image_focus": "highlight the warm wood texture and family dining atmosphere",
  "visual_notes": "target Indonesia, tone should feel premium but approachable",
  "promotion_info": "Free shipping in Jakarta this week",
  "target_tone": "Cozy-natural",
  "target_platform": "Instagram"
}

Expected behavior:
1. Analyze the image and identify the most likely furniture product
2. Infer style and atmosphere from visible cues
3. Generate the same multi-language output pack without requiring a full text-only prompt

[See examples/example-image-output.md for image-based output demonstration]
```
