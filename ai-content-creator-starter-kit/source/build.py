"""Builds the HTML for every file in the kit, runs quality control, and writes
out/manifest.json for render.cjs.

Usage:  python3 build.py && node render.cjs
"""

import json
import os
import re
import sys

import bespoke
import guide
import marketing
from content import calendar, ctas, hooks, ideas, image_prompts, prompts, templates
from lib import (BRAND, bullets, callout, card, doc_cover, esc, flow, h3, p, page_head, placeholders, rich, section_head, table, toc, write_lines)
from refs import ref

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out")
DIST = os.path.join(KIT, "AI Content Creator Starter Kit")
SELLER_IMG = os.path.join(KIT, "Seller Kit", "images")


def glossary_table(gloss, used):
    rows = [[f'<span class="ph">[{esc(k)}]</span>', esc(gloss[k])] for k in gloss if k in used]
    return table(["Placeholder", "What to put there"], rows, cls="t gloss", widths=["44mm", "auto"])


def ranges(categories):
    out, n = [], 0
    for cat in categories:
        k = len(cat[-1])
        out.append((cat[0], n + 1, n + k))
        n += k
    return out


# ---------------------------------------------------------------- File 02

def prompts_doc():
    used = set()
    for _t, _d, items in prompts.CATEGORIES:
        for _title, text, _tip in items:
            used.update(placeholders(text))
    s = [doc_cover("02", "100 AI Prompts", "Copy-ready prompts for ideas, posts, Reels, TikTok, LinkedIn, captions, storytelling and repurposing.",
                   [("100", "Prompts"), ("8", "Categories"), ("Any", "AI chat tool")], kicker="The prompt library")]
    s.append(flow("How to Use", [
        page_head("Start here", "How to use these prompts",
                  "Every prompt is written to work in any AI chat assistant — ChatGPT, Claude, Gemini, Copilot or similar. No special settings required."),
        '<div class="grid-2">'
        + card("Copy the prompt", "Copy the full text of the prompt into your AI tool.", tag="Step 01")
        + card("Replace the placeholders", "Swap every [PLACEHOLDER] for your own details. The more specific, the better the result.", tag="Step 02")
        + card("Review the output", "Read it critically. Keep what’s useful, delete what’s generic, check every fact.", tag="Step 03")
        + card("Refine with follow-ups", "Ask for changes: “shorter”, “simpler words”, “more specific to beginners”, “5 more options”.", tag="Step 04")
        + "</div>",
        callout("Before your first prompt, tell the AI about yourself once: “I’m a [NICHE] creator. My audience is [TARGET AUDIENCE]. I sell [PRODUCT/SERVICE]. My tone is [TONE].” Most tools remember this for the rest of the conversation.", label="Save time"),
        h3("What’s inside"),
        toc([(f"{a:03d}–{b:03d}", t, f"{b - a + 1} prompts") for t, a, b in ranges(prompts.CATEGORIES)]),
    ]))
    s.append(flow("Placeholder Glossary", [
        page_head("Reference", "Placeholder glossary", "These fill-in fields appear throughout the prompts. Replace the brackets and the words inside them with your own details."),
        glossary_table(prompts.GLOSSARY, used),
    ]))
    n = 0
    for ci, (title, desc, items) in enumerate(prompts.CATEGORIES, 1):
        blocks = [section_head(f"Category {ci:02d} · {len(items)} prompts", title, desc, f"{ci:02d}")]
        for ptitle, text, tip in items:
            n += 1
            fields = placeholders(text)
            cust = ('<div class="cust"><b>Customize</b>' + "".join(f'<span class="ph">[{esc(f)}]</span>' for f in fields) + "</div>") if fields else ""
            tip_html = f'<div class="tip"><b>Tip:</b> {rich(tip)}</div>' if tip else ""
            blocks.append(
                f'<div class="pcard"><div class="top"><span class="n">{n:03d}</span><span class="title">{esc(ptitle)}</span></div>'
                f'<div class="body"><span class="lbl">Prompt</span>{rich(text)}</div>{cust}{tip_html}</div>')
        s.append(flow(f"{ci:02d} · {title}", blocks))
    return s


# ---------------------------------------------------------------- File 03

def ideas_doc():
    s = [doc_cover("03", "100 Content<br>Ideas", "Adaptable ideas for any niche — each with a suggested format and call to action.",
                   [("100", "Ideas"), ("8", "Categories"), ("∞", "Niches")], kicker="The idea bank")]
    s.append(flow("How to Use", [
        page_head("Start here", "How to use these ideas",
                  "These ideas are deliberately flexible. The skill is in making them specific to your niche — that’s where AI helps."),
        h3("Make any idea specific"),
        table(["Generic idea", "Made specific"], [
            ["Common Mistake, Explained", "“The watering mistake that kills most beginner houseplants”"],
            ["The 3-Step Starter Plan", "“How to start freelance copywriting in 3 steps — with no portfolio”"],
            ["Tools I Use Every Day", "“The 4 apps I use to run my bakery’s orders”"],
            ["Myth vs Reality", "“Myth: you need to stretch before every run”"],
        ], split=False, widths=["60mm", "auto"]),
        callout("Paste any idea into your AI tool with this prompt: “Adapt this content idea for [NICHE] and [TARGET AUDIENCE]: [IDEA]. Give me 5 specific versions with a working title and hook for each.”", label="Quick adaptation prompt"),
        h3("What’s inside"),
        toc([(f"{a:03d}–{b:03d}", t, f"{b - a + 1} ideas") for t, a, b in ranges(ideas.CATEGORIES)]),
    ]))
    n = 0
    for ci, (title, desc, items) in enumerate(ideas.CATEGORIES, 1):
        rows = []
        for it, expl, fmt, cta in items:
            n += 1
            rows.append(
                f'<div class="idea"><div class="n">{n:03d}</div><div><h4>{rich(it)}</h4><p>{rich(expl)}</p>'
                f'<div class="meta"><div><b>Format</b><span>{esc(fmt)}</span></div><div><b>Suggested CTA</b><span>{rich(cta)}</span></div></div></div></div>')
        s.append(flow("100 Content Ideas", [section_head(f"Category {ci:02d} · {len(items)} ideas", title, desc, f"{ci:02d}"),
                                            '<div data-split="items">' + "".join(rows) + "</div>"], brk=(ci == 1)))
    return s


# ---------------------------------------------------------------- File 04

def hooks_doc():
    used = set()
    for _t, _d, items in hooks.CATEGORIES:
        for tpl, _ex, _fit in items:
            used.update(placeholders(tpl))
    s = [doc_cover("04", "50 Powerful<br>Hooks", "Fill-in-the-blank opening lines in 8 styles — each with a worked example from a different niche.",
                   [("50", "Hooks"), ("8", "Styles"), ("50", "Examples")], kicker="Opening lines")]
    s.append(flow("How to Use", [
        page_head("Start here", "How to use these hooks",
                  "A hook is the first thing people see: the first line of a caption, the cover of a carousel or the first two seconds of a video. These templates give you a proven starting structure."),
        '<div class="grid-3">'
        + card("Pick a style", "Match the hook style to your content: a mistake post needs a mistake hook.", tag="01")
        + card("Fill the blanks", "Replace the placeholders with specific words your audience uses.", tag="02")
        + card("Keep the promise", "Make sure the content delivers exactly what the hook suggests.", tag="03")
        + "</div>",
        h3("Rules for honest, effective hooks"),
        bullets([
            "**Specific beats clever.** “3 mistakes new runners make” is stronger than “Running secrets revealed”.",
            "**Short beats long.** Aim for under 12 words; cut anything that doesn’t add meaning.",
            "**Honest beats sensational.** Never promise a result your content can’t deliver.",
            "**Test several.** Write three versions and pick the one you’d stop scrolling for.",
        ]),
        h3("What’s inside"),
        toc([(f"{a:02d}–{b:02d}", t, f"{b - a + 1} hooks") for t, a, b in ranges(hooks.CATEGORIES)]),
    ]))
    s.append(flow("Placeholder Glossary", [
        page_head("Reference", "Placeholder glossary", "What to put in each fill-in field."),
        glossary_table(hooks.GLOSSARY, used),
    ]))
    n = 0
    for ci, (title, desc, items) in enumerate(hooks.CATEGORIES, 1):
        rows = []
        for tpl, ex, fit in items:
            n += 1
            rows.append(
                f'<div class="hook"><div class="n">{n:02d}</div><div><div class="line">{rich(tpl)}</div>'
                f'<div class="ex"><b>Example</b>{esc(ex)}</div><div class="fit"><b>Works well for</b>{esc(fit)}</div></div></div>')
        s.append(flow(f"{ci:02d} · {title}", [section_head(f"Style {ci:02d} · {len(items)} hooks", title, desc, f"{ci:02d}"),
                                              '<div data-split="items">' + "".join(rows) + "</div>"]))
    return s


# ---------------------------------------------------------------- File 05

def calendar_doc():
    s = [doc_cover("05", "30-Day Content<br>Calendar", "A complete, balanced month of content — with the exact prompt, idea or template to use each day.",
                   [("30", "Days"), ("6", "Formats & pillars"), ("1", "Person needed")], kicker="Your month, planned")]
    legend = " ".join(f'<span class="pillar {c}">{esc(n)}</span>' for n, c in calendar.PILLARS.values())
    s.append(flow("How to Use", [
        page_head("Start here", "How to use this calendar",
                  "Each day tells you what to post, in which format, which content pillar it serves, the goal, a call to action — and which tools from this kit to use."),
        '<div class="grid-3">'
        + card("Set up your month", "Fill in the worksheet on the next page. It takes 15 minutes and makes every prompt more specific.", tag="Before day 1")
        + card("Follow the toolkit links", "“Prompt 022” means File 02, prompt 022. “Idea”, “Hook” and “Template” point to Files 03, 04 and 06.", tag="Every day")
        + card("Review on lighter days", "Days 7, 14, 21 and 28 are lighter so you can review, reply and plan the next week.", tag="Weekly")
        + "</div>",
        h3("Pillar legend"),
        f"<p>{legend}</p>",
        callout("Posting every day isn’t required. If 3–4 posts a week is realistic for you, follow the calendar in order and simply take longer to complete it. Consistency matters more than speed.", label="Make it yours"),
        p("Swap any day that doesn’t fit your business with an idea from the same pillar in File 03.", "small"),
    ]))
    s.append(flow("Set Up Your Month", [
        page_head("Worksheet", "Set up your month", "Answer these before day 1. Paste your answers into your AI tool at the start of each session."),
        '<div class="grid-2"><div>' + write_lines([
            ("My niche", "Be specific: who and what.", 1),
            ("My target audience", "Who exactly are you creating for?", 1),
            ("Their biggest problem", "In their words, not yours.", 1),
            ("The result they want", None, 1),
        ]) + "</div><div>" + write_lines([
            ("What I sell (or will sell)", "Product, service, newsletter or none yet.", 1),
            ("My main platform", "Start with one.", 1),
            ("My 3–4 content pillars", None, 1),
            ("My tone of voice in 3 words", "e.g. calm, practical, warm", 1),
        ]) + "</div></div>",
        callout("Paste this into your AI tool at the start of each session: “I’m creating content about [NICHE] for [TARGET AUDIENCE]. Their main problem is [PROBLEM]. My tone is [TONE]. Keep this in mind for everything we create today.”", label="Your context prompt"),
    ]))
    day = 0
    for wi, (wtitle, wdesc, days) in enumerate(calendar.WEEKS, 1):
        rows = []
        for idea_t, fmt, pillar, goal, cta, kit in days:
            day += 1
            pname, pcls = calendar.PILLARS[pillar]
            review = day in (7, 14, 21, 28)
            kit_html = " · ".join(ref(k, t) for k, t in kit)
            label = "<small>Review</small>" if review else ""
            rows.append(f'<tr class="{"review" if review else ""}"><td class="day">{day:02d}{label}</td>'
                        f'<td><span class="idea-t">{rich(idea_t)}</span><span class="kit">{esc(kit_html)}</span></td>'
                        f"<td>{esc(fmt)}</td><td><span class=\"pillar {pcls}\">{esc(pname)}</span></td><td>{esc(goal)}</td><td>{rich(cta)}</td>"
                        f'<td><div class="done"></div></td></tr>')
        head = "<thead><tr><th>Day</th><th>Content idea · toolkit</th><th>Format</th><th>Pillar</th><th>Goal</th><th>CTA</th><th>Done</th></tr></thead>"
        cols = '<colgroup><col style="width:15mm"><col style="width:auto"><col style="width:26mm"><col style="width:30mm"><col style="width:28mm"><col style="width:62mm"><col style="width:13mm"></colgroup>'
        tbl = f'<table class="cal" data-split="items">{cols}{head}<tbody>{"".join(rows)}</tbody></table>'
        blocks = [section_head(wtitle.split(" — ")[0], wtitle.split(" — ")[1], wdesc), tbl]
        if wi == len(calendar.WEEKS):
            blocks.append('<div class="spacer-lg"></div>')
            blocks.append('<div class="grid-3">'
                          + card("Run your monthly review", "Use the Monthly Review page at the end of this file to see what worked.", tag="Day 31")
                          + card("Keep your best ideas", "Add your top 5 posts to a list. They’re the first candidates for repurposing next month.", tag="Next month")
                          + card("Plan month two", "Repeat the structure with new ideas from File 03 and new angles on your best topics.", tag="Keep going")
                          + "</div>")
        s.append(flow(wtitle.split(" — ")[0], blocks))
    assert day == 30, f"Calendar has {day} days"

    formats = [d[1] for w in calendar.WEEKS for d in w[2]]
    cells = "".join(f'<div class="cell"><span class="dn">{i:02d}</span><span class="fmt">{esc(f)}</span><span class="box"></span></div>' for i, f in enumerate(formats, 1))
    s.append(flow("30-Day Tracker", [
        page_head("Tracker", "30-day tracker", "Tick each day as you publish. Seeing the streak grow is surprisingly motivating."),
        f'<div class="tracker">{cells}</div>',
    ]))
    s.append(flow("Monthly Review", [
        page_head("After day 30", "Monthly review", "Take 30 minutes to look back before planning your next month."),
        '<div class="grid-2"><div>' + write_lines([
            ("My 3 best posts this month (and why they worked)", None, 3),
            ("Which pillar got the best response?", None, 1),
            ("Which format was easiest to create?", None, 1),
        ]) + "</div><div>" + write_lines([
            ("Questions my audience asked most", None, 3),
            ("What I’ll do more of next month", None, 1),
            ("What I’ll stop or change", None, 1),
        ]) + "</div></div>",
        callout("Start month two by repeating your 5 best-performing days with new angles, then fill the gaps with fresh ideas from File 03.", label="Next month"),
    ]))
    return s


# ---------------------------------------------------------------- File 06

def templates_doc():
    s = [doc_cover("06", "Social Media<br>Templates", "15 slide-by-slide templates with copy, layout and visual direction — easy to rebuild in Canva.",
                   [("15", "Templates"), ("4:5", "Feed-ready"), ("Canva", "Friendly")], kicker="Design blueprints")]
    s.append(flow("How to Use", [
        page_head("Start here", "Building these templates in Canva",
                  "Each template gives you the structure, suggested copy and visual direction. Build it once in Canva, save it as your own template, and reuse it for months."),
        table(["Setting", "Recommendation"], [
            ["<strong>Canvas size</strong>", "Instagram post (portrait) — 1080 × 1350 px. Stories and Reels covers — 1080 × 1920 px."],
            ["<strong>Margins</strong>", "Keep text at least 80 px from every edge. Show margins with File → View settings → Show margins."],
            ["<strong>Fonts</strong>", "One bold headline font (for example Montserrat or Poppins) and one clean body font (for example Inter or Open Sans)."],
            ["<strong>Colors</strong>", "One dark, one light and one accent color. Save them in your Brand Kit or as a palette."],
            ["<strong>Text size</strong>", "Headlines 60–90 pt, body text at least 32 pt so it’s readable on a phone."],
            ["<strong>Consistency</strong>", "Keep headlines, page numbers and your handle in the same position on every slide."],
        ], split=False, widths=["36mm", "auto"]),
        h3("How to read each template"),
        bullets([
            "**Slide structure** — a miniature of each slide and what goes on it.",
            "**Suggested copy** — fill-in text for each slide. Replace the [PLACEHOLDERS] with your details.",
            "**Visual recommendation** — layout and design tips specific to that format.",
            "**CTA** — a natural call to action that matches the template’s purpose.",
        ]),
        callout("Pair each template with a prompt: write the copy with File 02, the hook with File 04, then design here.", label="Fastest workflow"),
    ]))
    s.append(flow("Contents", [
        page_head("Contents", "The 15 templates", "Each template has its own page. Start with the ones that match the content you post most often."),
        toc([(f"{i:02d}", t["name"], t["format"].split(" · ")[0]) for i, t in enumerate(templates.TEMPLATES, 1)]),
        callout("Build your three most-used templates first — usually the Educational Carousel, 3 Tips and Quote. Save them in Canva and duplicate them for every new post.", label="Where to start"),
    ]))
    for i, t in enumerate(templates.TEMPLATES, 1):
        def tone(j, lab):
            if lab == "CTA":
                return "tpl-acc"
            return "tpl-dark" if j == 0 and len(t["slides"]) > 1 else ""
        strip = '<div class="tpl-strip">' + "".join(
            f'<div class="tpl-item"><div class="tpl-slide {tone(j, lab)}"><span class="sn">{j + 1:02d}</span>'
            f'<span class="sl">{esc(lab)}</span><span class="bars"><i style="width:90%"></i><i style="width:65%"></i></span></div>'
            f'<div class="cap">{rich(d)}</div></div>'
            for j, (lab, d) in enumerate(t["slides"])) + "</div>"
        copy = '<div class="copy-block">' + "".join(f'<div class="row"><b>{esc(a)}</b><span>{rich(b)}</span></div>' for a, b in t["copy"]) + "</div>"
        visual = bullets(t["visual"], "tight")
        note = callout(t["note"], label="Note") if t.get("note") else ""
        s.append(flow(f"Template {i:02d}", [
            f'<div class="kwn"><div class="eyebrow">Template {i:02d} · {esc(t["format"])}</div><h1 class="page-title">{esc(t["name"])}</h1></div>',
            f'<p class="lead" style="margin-bottom:4mm">{rich(t["purpose"])}</p>',
            h3("Slide structure"), strip,
            h3("Suggested copy"), copy,
            f'<div class="tpl-meta"><div><h3 class="h" style="margin-top:0">Visual recommendation</h3>{visual}</div>'
            f'<div><h3 class="h" style="margin-top:0">CTA</h3><div class="callout" style="margin-top:0">{rich(t["cta"])}</div></div></div>',
            note,
        ]))
    return s


# ---------------------------------------------------------------- File 08

def ctas_doc():
    used = set()
    for _t, _d, items in ctas.CATEGORIES:
        for line, _w in items:
            used.update(placeholders(line))
    s = [doc_cover("08", "50 CTAs", "Natural calls to action for comments, saves, shares, follows, clicks, leads and community.",
                   [("50", "CTAs"), ("9", "Goals"), ("0", "Spammy lines")], kicker="Bonus 01")]
    s.append(flow("How to Use", [
        page_head("Start here", "Choosing the right CTA",
                  "A good call to action feels like a natural next step, not a demand. Choose one per post, based on what you want that post to achieve."),
        table(["If your post is…", "Ask for…", "Category"], [
            ["A checklist, guide or reference", "A save", "Saves"],
            ["An opinion or a question", "A comment", "Comments"],
            ["Helpful for someone specific", "A share", "Shares"],
            ["Part of a series or ongoing topic", "A follow", "Follows"],
            ["A summary of something longer", "A click", "Website"],
            ["About your offer", "A visit or a message", "Products"],
            ["Offering a free resource", "An email or a message", "Leads"],
            ["About connection and belonging", "An introduction or a win", "Community"],
        ], split=False, widths=["auto", "48mm", "34mm"]),
        h3("Three rules"),
        bullets([
            "**One CTA per post.** Several requests at once dilute every one of them.",
            "**Only promise what you’ll deliver.** If you say “comment and I’ll send it”, reply to every comment.",
            "**Say it your way.** Adjust the wording so it sounds like you.",
        ]),
    ]))
    s.append(flow("Placeholder Glossary", [
        page_head("Reference", "Placeholder glossary", "Some CTAs include fill-in fields. Replace them with your own details."),
        glossary_table(ctas.GLOSSARY, used),
        callout("Rotate your CTAs. Using the same one on every post makes it easy to ignore — keep a short list of favorites for each goal and alternate between them.", label="Tip"),
    ]))
    n = 0
    for ci, (title, desc, items) in enumerate(ctas.CATEGORIES, 1):
        rows = []
        for line, when in items:
            n += 1
            rows.append(f'<div class="cta"><div class="n">{n:02d}</div><div class="line">{rich(line)}</div><div class="when"><b>Use for</b>{esc(when)}</div></div>')
        s.append(flow("50 CTAs", [section_head(f"Goal {ci:02d} · {len(items)} CTAs", title, desc, f"{ci:02d}"), '<div data-split="items">' + "".join(rows) + "</div>"], brk=(ci == 1)))
    return s


# ---------------------------------------------------------------- File 09

def images_doc():
    used = set()
    for _t, items in image_prompts.CATEGORIES:
        for _title, text, _b, _tip in items:
            used.update(placeholders(text))
    s = [doc_cover("09", "30 AI Image<br>Prompts", "Detailed prompts for scroll-stopping, on-brand visuals — for any AI image generator.",
                   [("30", "Prompts"), ("10", "Visual styles"), ("Any", "Image tool")], kicker="Bonus 02")]
    parts = ["Subject", "Setting", "Lighting", "Composition", "Style", "Color", "Format"]
    s.append(flow("How to Use", [
        page_head("Start here", "How to use these image prompts",
                  "These prompts work with most AI image generators, including ChatGPT, Midjourney, Adobe Firefly, Ideogram and Canva’s built-in image tools. Replace the placeholders, generate a few versions and pick the best."),
        h3("The anatomy of a good image prompt"),
        '<div class="formula">' + '<span class="plus">+</span>'.join(f'<span class="term">{x.upper()}</span>' for x in parts) + "</div>",
        table(["Tip", "Why it matters"], [
            ["<strong>Add text afterwards</strong>", "AI image tools often misspell words. Generate the image without text and add your headline in Canva."],
            ["<strong>Ask for empty space</strong>", "“Space on the right for text” gives you room for a headline."],
            ["<strong>Set the aspect ratio</strong>", "Midjourney uses “--ar 4:5”. Other tools usually accept “vertical 4:5 format” in the prompt."],
            ["<strong>Generate, then refine</strong>", "Change one thing at a time: lighting, angle or color, until it’s right."],
            ["<strong>Stay consistent</strong>", "Reuse the same [STYLE] and [COLOR] words so your visuals look like one brand."],
        ], split=False, widths=["46mm", "auto"]),
        callout("Check the terms of the image tool you use, especially for commercial use. Don’t generate real people, logos, trademarks or another artist’s distinctive style, and follow each platform’s rules on labelling AI-generated images.", label="Use responsibly"),
    ]))
    s.append(flow("Placeholder Glossary", [
        page_head("Reference", "Placeholder glossary", "Fill these in to make every image match your brand."),
        glossary_table(image_prompts.GLOSSARY, used),
    ]))
    n = 0
    blocks = []
    for ci, (title, items) in enumerate(image_prompts.CATEGORIES, 1):
        blocks.append(f'<div class="kwn" style="margin:{"0" if ci == 1 else "3mm"} 0 3mm"><div class="eyebrow" style="margin-bottom:1mm">Category {ci:02d}</div><h2 class="h" style="margin:0">{esc(title)}</h2></div>')
        for ptitle, text, best, tip in items:
            n += 1
            tip_html = f"<div><b>Tip</b>{rich(tip)}</div>" if tip else "<div></div>"
            blocks.append(f'<div class="icard"><div class="top"><span class="n">{n:02d}</span><span class="title">{esc(ptitle)}</span></div>'
                          f'<div class="body">{rich(text)}</div><div class="foot"><div><b>Best for</b>{esc(best)}</div>{tip_html}</div></div>')
    s.append(flow("30 AI Image Prompts", blocks))
    return s


# ---------------------------------------------------------------- QC

FORBIDDEN = [r"\bTODO\b", r"\bTBD\b", r"lorem", r"\bXXX\b", r"\{\{", r"game-changer(?![”\"])", r"in today’s fast-paced world(?!…)", r"\bunlock your\b"]


def qc():
    problems = []

    def count(name, cats, expected, per_cat=None):
        got = sum(len(c[-1]) for c in cats)
        if got != expected:
            problems.append(f"{name}: expected {expected}, found {got}")
        if per_cat:
            actual = [len(c[-1]) for c in cats]
            if actual != per_cat:
                problems.append(f"{name}: category sizes {actual} != {per_cat}")

    count("Prompts", prompts.CATEGORIES, 100, [20, 15, 15, 10, 10, 10, 10, 10])
    count("Ideas", ideas.CATEGORIES, 100, [20, 15, 15, 10, 10, 10, 10, 10])
    count("Hooks", hooks.CATEGORIES, 50)
    count("CTAs", ctas.CATEGORIES, 50)
    count("Image prompts", image_prompts.CATEGORIES, 30, [3] * 10)
    if len(templates.TEMPLATES) != 15:
        problems.append(f"Templates: expected 15, found {len(templates.TEMPLATES)}")
    if sum(len(w[2]) for w in calendar.WEEKS) != 30:
        problems.append("Calendar: not 30 days")

    def dupes(name, texts):
        seen = {}
        for t in texts:
            k = re.sub(r"\W+", " ", t.lower()).strip()
            if k in seen:
                problems.append(f"{name}: duplicate “{t}”")
            seen[k] = t

    dupes("Prompt titles", [i[0] for c in prompts.CATEGORIES for i in c[2]])
    dupes("Prompt texts", [i[1] for c in prompts.CATEGORIES for i in c[2]])
    dupes("Idea titles", [i[0] for c in ideas.CATEGORIES for i in c[2]])
    dupes("Hook templates", [i[0] for c in hooks.CATEGORIES for i in c[2]])
    dupes("Hook examples", [i[1] for c in hooks.CATEGORIES for i in c[2]])
    dupes("CTAs", [i[0] for c in ctas.CATEGORIES for i in c[2]])
    dupes("Image prompt titles", [i[0] for c in image_prompts.CATEGORIES for i in c[1]])
    dupes("Image prompts", [i[1] for c in image_prompts.CATEGORIES for i in c[1]])
    dupes("Template names", [t["name"] for t in templates.TEMPLATES])
    dupes("Calendar ideas", [d[0] for w in calendar.WEEKS for d in w[2]])

    # Every placeholder must be explained in the matching glossary.
    def gloss(name, texts, glossary):
        for t in texts:
            for ph in placeholders(t):
                if ph not in glossary:
                    problems.append(f"{name}: placeholder [{ph}] missing from glossary (in: {t[:60]}…)")

    gloss("Prompts", [i[1] for c in prompts.CATEGORIES for i in c[2]], prompts.GLOSSARY)
    gloss("Hooks", [i[0] for c in hooks.CATEGORIES for i in c[2]], hooks.GLOSSARY)
    gloss("CTAs", [i[0] for c in ctas.CATEGORIES for i in c[2]], ctas.GLOSSARY)
    gloss("Image prompts", [i[1] for c in image_prompts.CATEGORIES for i in c[1]], image_prompts.GLOSSARY)

    # Finished examples must not contain placeholders.
    for c in hooks.CATEGORIES:
        for tpl, ex, _ in c[2]:
            if placeholders(ex) or "[" in ex:
                problems.append(f"Hook example contains a placeholder: {ex}")
            if not placeholders(tpl) and "client asked me" not in tpl:
                problems.append(f"Hook template has no placeholder: {tpl}")

    # Calendar references resolve (ref() raises on a broken one).
    for w in calendar.WEEKS:
        for d in w[2]:
            for kind, title in d[5]:
                try:
                    ref(kind, title)
                except KeyError as e:
                    problems.append(str(e))

    # Forbidden filler and leftovers across every text source.
    blob = json.dumps([prompts.CATEGORIES, ideas.CATEGORIES, hooks.CATEGORIES, ctas.CATEGORIES, image_prompts.CATEGORIES,
                       templates.TEMPLATES, calendar.WEEKS], ensure_ascii=False)
    for pat in FORBIDDEN:
        for m in re.finditer(pat, blob, re.I):
            ctx = blob[max(0, m.start() - 50): m.end() + 30]
            if "Avoid clichés" in ctx or "avoid" in ctx.lower():
                continue
            problems.append(f"Forbidden pattern {pat!r}: …{ctx}…")
    return problems


# ---------------------------------------------------------------- main

DOCS = [
    ("01", "01 — Quick Start Guide", guide.build, "portrait", [0, 2, 5, 12]),
    ("02", "02 — 100 AI Prompts", prompts_doc, "portrait", [0, 3, 4]),
    ("03", "03 — 100 Content Ideas", ideas_doc, "portrait", [0, 2]),
    ("04", "04 — 50 Powerful Hooks", hooks_doc, "portrait", [0, 3]),
    ("05", "05 — 30-Day Content Calendar", calendar_doc, "landscape", [0, 3, 4]),
    ("06", "06 — Social Media Templates", templates_doc, "portrait", [0, 3]),
    ("07", "07 — Publishing Checklist", bespoke.checklist_doc, "portrait", [0, 2]),
    ("08", "08 — BONUS — 50 CTAs", ctas_doc, "portrait", [0, 2]),
    ("09", "09 — BONUS — 30 AI Image Prompts", images_doc, "portrait", [0, 3]),
    ("10", "10 — BONUS — Content Repurposing System", bespoke.repurpose_doc, "portrait", [0, 2]),
]


def main():
    problems = qc()
    if problems:
        print("QUALITY CONTROL FAILED:\n  " + "\n  ".join(problems))
        sys.exit(1)
    print("Quality control passed: 100 prompts, 100 ideas, 50 hooks, 30 days, 15 templates, 50 CTAs, 30 image prompts.")

    from lib import document
    os.makedirs(OUT, exist_ok=True)
    manifest = {"documents": [], "images": []}
    for doc_id, title, fn, orient, snaps in DOCS:
        html_name = f"doc-{doc_id}.html"
        with open(os.path.join(OUT, html_name), "w", encoding="utf-8") as f:
            f.write(document(title, fn(), orient))
        manifest["documents"].append({"id": doc_id, "html": html_name, "pdf": os.path.join(DIST, title + ".pdf"), "snapshots": snaps})

    for name, html, w, h in marketing.images():
        html_name = f"img-{name}.html"
        with open(os.path.join(OUT, html_name), "w", encoding="utf-8") as f:
            f.write(html)
        manifest["images"].append({"html": html_name, "png": os.path.join(SELLER_IMG, name + ".png"), "width": w, "height": h})

    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(manifest['documents'])} documents and {len(manifest['images'])} images to {OUT}")


if __name__ == "__main__":
    main()
