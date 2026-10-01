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
├── arabic/                                ← Arabic edition (right-to-left), same structure
│   ├── حقيبة صانع المحتوى بالذكاء الاصطناعي/   ← the 10 Arabic PDFs
│   ├── AI-Content-Creator-Starter-Kit-Arabic.zip
│   └── Seller Kit/                        ← Arabic sales copy, cover spec, launch pack, images
└── source/                                ← everything needed to edit and rebuild the PDFs
```

## Arabic edition

The Arabic edition is written in Modern Standard Arabic (not machine-translated) and laid out right-to-left with Cairo and IBM Plex Sans Arabic. It has the same structure, counts and numbering as the English edition, so `Prompt 040` and `برومبت 040` are the same prompt.

The 30 image prompts stay in English, with Arabic titles, uses and tips. Image generators, Midjourney especially, follow English prompts much more reliably.

Arabic content lives in `source/ar/`: `content/*.py` holds the data, `guide.py` is File 01, `docs.py` covers Files 02–06, 08 and 09, `bespoke.py` covers Files 07 and 10, and `marketing.py` builds the Gumroad images. The right-to-left styling is in `source/rtl.css`.

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

`build.sh` runs the quality checks, regenerates every PDF and image for both editions, and recreates both zips. The Arabic edition alone builds with `python3 build_ar.py && node render.cjs manifest-ar.json`.

The build **fails** if any of these is not true:

- exactly 100 prompts, 100 ideas, 50 hooks, 30 calendar days, 15 templates, 50 CTAs and 30 image prompts
- no duplicate titles or texts
- every `[PLACEHOLDER]` is explained in its file's glossary
- hook examples contain no leftover placeholders
- every cross-reference (for example “Prompt 022” in the calendar) points to an item that exists. References are written by title and numbered automatically.
- no content overflows a page

Fonts (Inter, Space Grotesk, JetBrains Mono, Cairo and IBM Plex Sans Arabic) are licensed under the SIL Open Font License, which allows embedding them in commercial PDFs. The license files are in `source/fonts/`.

## Before you sell

Read through every file once more as a human reviewer, and adjust anything to your own voice. The sales copy contains no invented claims. Keep it that way, and add real testimonials only with the buyer's permission.
