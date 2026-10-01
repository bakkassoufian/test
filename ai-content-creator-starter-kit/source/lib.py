"""HTML building blocks shared by every document in the kit."""

import html
import re

BRAND = "AI Content Creator Starter Kit"

# Anything in square brackets written in capitals is a fill-in field, e.g. [NICHE].
# Arabic placeholders such as [المجال] are supported for the Arabic edition.
PH_RE = re.compile(r"\[([A-Z0-9\u0600-\u06FF][A-Z0-9 /&'\-\u0600-\u06FF]*)\]")


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def rich(s):
    """Escape text, then apply **bold** and highlight [PLACEHOLDERS]."""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return PH_RE.sub(lambda m: f'<span class="ph">[{m.group(1)}]</span>', s)


def placeholders(s):
    """Unique placeholders in order of first appearance."""
    return list(dict.fromkeys(PH_RE.findall(s)))


def document(title, sections, orientation="portrait", lang="en", brand=BRAND):
    rtl = lang == "ar"
    extra = '<link rel="stylesheet" href="../rtl.css">' if rtl else ""
    return f"""<!doctype html>
<html lang="{lang}" dir="{'rtl' if rtl else 'ltr'}"><head><meta charset="utf-8"><title>{esc(title)}</title>
<link rel="stylesheet" href="../styles.css">{extra}
<style>@page {{ size: A4 {orientation}; margin: 0; }}</style>
</head>
<body class="{orientation}{' rtl' if rtl else ''}" data-doc="{attr(title)}" data-brand="{attr(brand)}">
<div id="source">
{''.join(sections)}
</div>
<div id="book"></div>
<script src="../paginate.js"></script>
</body></html>"""


def full(inner, cls=""):
    return f'<section class="full {cls}">{inner}</section>'


def flow(section_title, blocks, brk=True):
    extra = "" if brk else ' data-break="none"'
    return f'<section class="flow" data-section="{attr(section_title)}"{extra}>{"".join(blocks)}</section>'


COVER_LABELS = dict(brand=BRAND, file="File {num} / 10", kicker="File {num}", tagline="Create. Plan. Publish. Grow.", usage="For personal and client use")


def doc_cover(num, title, subtitle, stats, kicker=None, extra_class="", labels=None):
    """Dark cover used by files 02–10."""
    L = labels or COVER_LABELS
    stats_html = "".join(f'<div class="stat"><div class="v">{esc(v)}</div><div class="l">{esc(l)}</div></div>' for v, l in stats)
    return full(
        f"""
<div class="grid-lines"></div><div class="glow"></div>
<div class="topline" style="position:relative"><span class="b">{esc(L['brand'])}</span><span>{esc(L['file'].format(num=num))}</span></div>
<div class="bignum">{num}</div>
<div class="main">
  <div class="kicker">{esc(kicker or L['kicker'].format(num=num))}</div>
  <h1>{title}</h1>
  <div class="sub">{rich(subtitle)}</div>
  <div class="rule"></div>
  <div class="stats">{stats_html}</div>
</div>
<div class="bottom"><span>{esc(L['tagline'])}</span><span>{esc(L['usage'])}</span></div>
""",
        "cover " + extra_class,
    )


def page_head(eyebrow, title, lead=None):
    out = f'<div class="kwn"><div class="eyebrow">{esc(eyebrow)}</div><h1 class="page-title">{rich(title)}</h1></div>'
    if lead:
        out += f'<p class="lead">{rich(lead)}</p>'
    return out


def section_head(kicker, title, text, count=None):
    c = f'<div class="count">{esc(count)}</div>' if count else ""
    return f'<div class="section-head kwn"><div class="k">{esc(kicker)}</div><h2>{rich(title)}</h2><p>{rich(text)}</p>{c}</div>'


def bullets(items, cls=""):
    return f'<ul class="bullets {cls}">' + "".join(f"<li>{rich(i)}</li>" for i in items) + "</ul>"


def checklist(items, split=False):
    """items: list of (title, detail-or-None)."""
    rows = []
    for t, d in items:
        dd = f'<span class="d">{rich(d)}</span>' if d else ""
        rows.append(f'<li><div class="box"></div><div><strong>{rich(t)}</strong>{dd}</div></li>')
    sp = ' data-split="items"' if split else ""
    return f'<ul class="checklist"{sp}>' + "".join(rows) + "</ul>"


def callout(text, label=None, dark=False):
    lab = f'<span class="label">{esc(label)}</span>' if label else ""
    return f'<div class="callout{" dark" if dark else ""}">{lab}{rich(text)}</div>'


def p(text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f"<p{c}>{rich(text)}</p>"


def h2(text):
    return f'<h2 class="h kwn">{rich(text)}</h2>'


def h3(text):
    return f'<h3 class="h kwn">{rich(text)}</h3>'


def card(title, text, tag=None, cls=""):
    t = f'<span class="tag">{esc(tag)}</span>' if tag else ""
    body = text if text.startswith("<") else f"<p>{rich(text)}</p>"
    return f'<div class="card {cls}">{t}<h4>{rich(title)}</h4>{body}</div>'


def table(headers, rows, cls="t", split=True, widths=None):
    cols = ""
    if widths:
        cols = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    head = "<thead><tr>" + "".join(f"<th>{esc(h)}</th>" for h in headers) + "</tr></thead>"
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    sp = ' data-split="items"' if split else ""
    return f'<table class="{cls}"{sp}>{cols}{head}<tbody>{body}</tbody></table>'


def write_lines(fields):
    """Worksheet fields: list of (question, hint, number_of_lines)."""
    out = []
    for q, hint, n in fields:
        h = f'<div class="hint">{rich(hint)}</div>' if hint else ""
        out.append(f'<div class="field"><div class="q">{rich(q)}</div>{h}' + '<div class="line"></div>' * n + "</div>")
    return "".join(out)


def toc(rows):
    """rows: (number, title, caption)."""
    return "<div>" + "".join(
        f'<div class="toc-row"><span class="n">{esc(n)}</span><span class="t">{rich(t)}</span><span class="c">{esc(c)}</span></div>' for n, t, c in rows
    ) + "</div>"
