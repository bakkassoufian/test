# AI Content Creator Starter Kit

A digital product for Gumroad: **Create 30 days of social media content with AI — without starting from a blank page.**

## What's here

```
ai-content-creator-starter-kit/
├── AI Content Creator Starter Kit/        ← the product (what customers download)
│   ├── 01 — Quick Start Guide.pdf
│   ├── 02 — 100 AI Prompts.pdf
│   ├── 03 — 100 Content Ideas.pdf
│   ├── 04 — 50 Powerful Hooks.pdf
│   ├── 05 — 30-Day Content Calendar.pdf
│   ├── 06 — Social Media Templates.pdf
│   ├── 07 — Publishing Checklist.pdf
│   ├── 08 — BONUS — 50 CTAs.pdf
│   ├── 09 — BONUS — 30 AI Image Prompts.pdf
│   └── 10 — BONUS — Content Repurposing System.pdf
├── AI-Content-Creator-Starter-Kit.zip     ← upload this to Gumroad
├── Seller Kit/                            ← for you, not for customers
│   ├── Gumroad Sales Page Copy.md
│   ├── Gumroad Cover Specification.md
│   ├── Launch Marketing Pack.md
│   └── images/                            ← cover, thumbnail and 5 preview images
└── source/                                ← everything needed to edit and rebuild the PDFs
```

## Editing the content

All text lives in plain Python files, so you can change wording without touching the design:

| File | Content |
|---|---|
| `source/guide.py` | 01 Quick Start Guide |
| `source/content/prompts.py` | 02 100 AI Prompts |
| `source/content/ideas.py` | 03 100 Content Ideas |
| `source/content/hooks.py` | 04 50 Powerful Hooks |
| `source/content/calendar.py` | 05 30-Day Content Calendar |
| `source/content/templates.py` | 06 Social Media Templates |
| `source/bespoke.py` | 07 Publishing Checklist, 10 Content Repurposing System |
| `source/content/ctas.py` | 08 50 CTAs |
| `source/content/image_prompts.py` | 09 30 AI Image Prompts |
| `source/styles.css` | Design system (colors, fonts, layout) |
| `source/marketing.py` | Gumroad cover, thumbnail and preview images |

## Rebuilding

Requires Python 3, Node.js with Playwright, and Chromium.

```bash
cd source
./build.sh
```

`build.sh` runs the quality checks, regenerates every PDF and image, and recreates the zip.

The build **fails** if any of these is not true:

- exactly 100 prompts, 100 ideas, 50 hooks, 30 calendar days, 15 templates, 50 CTAs and 30 image prompts
- no duplicate titles or texts
- every `[PLACEHOLDER]` is explained in its file's glossary
- hook examples contain no leftover placeholders
- every cross-reference (for example “Prompt 022” in the calendar) points to an item that exists. References are written by title and numbered automatically.
- no content overflows a page

Fonts (Inter, Space Grotesk and JetBrains Mono) are licensed under the SIL Open Font License, which allows embedding them in commercial PDFs. The license files are in `source/fonts/`.

## Before you sell

Read through every file once more as a human reviewer, and adjust anything to your own voice. The sales copy contains no invented claims. Keep it that way, and add real testimonials only with the buyer's permission.
