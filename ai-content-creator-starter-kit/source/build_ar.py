"""Builds the Arabic edition: quality control, HTML for every file, and
out/manifest-ar.json for render.cjs.

Usage:  python3 build_ar.py && node render.cjs manifest-ar.json
"""

import json
import os
import sys

import build
from ar import bespoke, docs, guide, marketing
from ar.content import calendar, ctas, hooks, ideas, image_prompts, prompts, templates
from ar.refs import ref
from lib import document

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(os.path.dirname(HERE), "arabic")
OUT = os.path.join(HERE, "out")
DIST = os.path.join(KIT, "حقيبة صانع المحتوى بالذكاء الاصطناعي")
SELLER_IMG = os.path.join(KIT, "Seller Kit", "images")
BRAND = docs.BRAND

DOCS = [
    ("ar-01", "01 — دليل البدء السريع", guide.build, "portrait", [0, 2, 5, 12]),
    ("ar-02", "02 — 100 برومبت للذكاء الاصطناعي", docs.prompts_doc, "portrait", [0, 4, 5]),
    ("ar-03", "03 — 100 فكرة محتوى", docs.ideas_doc, "portrait", [0, 3]),
    ("ar-04", "04 — 50 خطّافًا قويًا", docs.hooks_doc, "portrait", [0, 3]),
    ("ar-05", "05 — تقويم المحتوى لـ 30 يومًا", docs.calendar_doc, "landscape", [0, 3, 4]),
    ("ar-06", "06 — قوالب مواقع التواصل", docs.templates_doc, "portrait", [0, 3]),
    ("ar-07", "07 — قائمة تحقق النشر", bespoke.checklist_doc, "portrait", [0, 2]),
    ("ar-08", "08 — ملحق — 50 دعوة لاتخاذ إجراء", docs.ctas_doc, "portrait", [0, 2]),
    ("ar-09", "09 — ملحق — 30 برومبت للصور", docs.images_doc, "portrait", [0, 3]),
    ("ar-10", "10 — ملحق — نظام إعادة توظيف المحتوى", bespoke.repurpose_doc, "portrait", [0, 2]),
]


def main():
    problems = build.qc(prompts, ideas, hooks, ctas, image_prompts, templates, calendar, ref, ("سألني أحد العملاء",))
    if problems:
        print("QUALITY CONTROL FAILED:\n  " + "\n  ".join(problems))
        sys.exit(1)
    print("Arabic quality control passed: 100 prompts, 100 ideas, 50 hooks, 30 days, 15 templates, 50 CTAs, 30 image prompts.")

    os.makedirs(OUT, exist_ok=True)
    manifest = {"documents": [], "images": []}
    for doc_id, title, fn, orient, snaps in DOCS:
        html_name = f"{doc_id}.html"
        with open(os.path.join(OUT, html_name), "w", encoding="utf-8") as f:
            f.write(document(title, fn(), orient, lang="ar", brand=BRAND))
        manifest["documents"].append({"id": doc_id, "html": html_name, "pdf": os.path.join(DIST, title + ".pdf"), "snapshots": snaps})

    for name, html, w, h in marketing.images():
        html_name = f"ar-img-{name}.html"
        with open(os.path.join(OUT, html_name), "w", encoding="utf-8") as f:
            f.write(html)
        manifest["images"].append({"html": html_name, "png": os.path.join(SELLER_IMG, name + ".png"), "width": w, "height": h})

    with open(os.path.join(OUT, "manifest-ar.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(manifest['documents'])} documents and {len(manifest['images'])} images to {OUT}")


if __name__ == "__main__":
    main()
