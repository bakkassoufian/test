"""Gumroad cover, square thumbnail and five preview images.

Each image is an HTML page rendered to PNG by render.cjs. The page mockups are
real snapshots of the rendered PDFs (out/snapshots/<file>-<page>.png).
"""

from lib import esc

BASE_CSS = """
<link rel="stylesheet" href="../styles.css">
<style>
  html, body { margin: 0; background: #0f1013; }
  body { font-family: var(--sans); color: #c9cad2; }
  .canvas { position: relative; overflow: hidden; background: var(--ink); }
  .grid { position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,.035) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px); background-size: 48px 48px; }
  .glow { position: absolute; border-radius: 50%; background: radial-gradient(circle, rgba(91,76,255,.5), rgba(91,76,255,0) 65%); }
  .mono { font-family: var(--mono); letter-spacing: .18em; text-transform: uppercase; }
  .brand { font-family: var(--mono); font-size: 13px; letter-spacing: .2em; text-transform: uppercase; color: #8d8f99; display: flex; align-items: center; gap: 10px; }
  .brand::before { content: ""; width: 10px; height: 10px; background: var(--accent); border-radius: 2px; }
  h1 { font-family: var(--display); color: #fff; font-weight: 700; letter-spacing: -.025em; line-height: .98; margin: 0; }
  h1 .soft { color: #a99fff; }
  .badge { display: inline-flex; align-items: center; gap: 10px; font-family: var(--mono); font-weight: 500; letter-spacing: .12em; text-transform: uppercase; color: #fff; background: var(--accent); border-radius: 999px; }
  .sub { color: #d9dae0; }
  .shot { position: absolute; border-radius: 6px; box-shadow: 0 30px 60px rgba(0,0,0,.55), 0 0 0 1px rgba(255,255,255,.06); background: #fff; }
  .rule { width: 64px; height: 4px; background: var(--accent); border-radius: 2px; }
  .chip { background: transparent; font-family: var(--mono); font-size: 12px; letter-spacing: .1em; text-transform: uppercase; color: #d9dae0; border: 1px solid rgba(255,255,255,.16); border-radius: 999px; padding: 7px 14px; display: inline-block; margin: 0 8px 10px 0; }
</style>
"""

# Text used on each image — mirrored in "Seller Kit/Gumroad Cover Specification.md".
COVER = dict(title="AI CONTENT CREATOR", second="STARTER KIT", subtitle="30 Days of AI-Powered Content Creation",
             badge="100 PROMPTS + 100 IDEAS + 30-DAY CALENDAR")


def page(html, w, h):
    return f'<!doctype html><html><head><meta charset="utf-8">{BASE_CSS}</head><body><div class="canvas" style="width:{w}px;height:{h}px">{html}</div></body></html>'


def snap(doc, n):
    return f"snapshots/{doc}-{n}.png"


def cover():
    w, h = 1280, 720
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:900px;height:900px;right:-260px;bottom:-420px"></div>
<img class="shot" src="{snap('05', 4)}" style="width:430px;right:-40px;top:300px;transform:rotate(-4deg)">
<img class="shot" src="{snap('02', 4)}" style="width:300px;right:250px;top:150px;transform:rotate(-8deg)">
<img class="shot" src="{snap('01', 1)}" style="width:310px;right:40px;top:60px;transform:rotate(5deg)">
<div style="position:absolute;left:72px;top:64px" class="brand">Digital toolkit · 10 PDF files</div>
<div style="position:absolute;left:72px;top:190px;width:640px">
  <div class="badge" style="font-size:14px;padding:11px 20px;margin-bottom:34px">{esc(COVER['badge'])}</div>
  <h1 style="font-size:78px">{esc(COVER['title'])}<br><span class="soft">{esc(COVER['second'])}</span></h1>
  <div class="rule" style="margin:34px 0 26px"></div>
  <div class="sub" style="font-size:27px;font-weight:500">{esc(COVER['subtitle'])}</div>
</div>
"""
    return page(html, w, h), w, h


def thumbnail():
    w, h = 600, 600
    html = f"""
<div class="grid" style="background-size:40px 40px"></div>
<div class="glow" style="width:620px;height:620px;right:-260px;bottom:-280px"></div>
<img class="shot" src="{snap('01', 1)}" style="width:250px;right:-36px;bottom:-110px;transform:rotate(-7deg)">
<div style="position:absolute;left:46px;top:50px;width:520px">
  <div class="brand" style="font-size:11px;margin-bottom:58px">Starter kit</div>
  <h1 style="font-size:54px">AI CONTENT<br>CREATOR<br><span class="soft">STARTER KIT</span></h1>
  <div class="rule" style="margin:28px 0 22px"></div>
  <div class="sub" style="font-size:19px;font-weight:500;width:260px;line-height:1.35">100 prompts, 100 ideas &amp; a 30-day plan</div>
</div>
"""
    return page(html, w, h), w, h


def preview_inside():
    w, h = 1280, 720
    files = ["Quick Start Guide", "100 AI Prompts", "100 Content Ideas", "50 Powerful Hooks", "30-Day Content Calendar",
             "Social Media Templates", "Publishing Checklist", "BONUS · 50 CTAs", "BONUS · 30 AI Image Prompts", "BONUS · Content Repurposing System"]
    rows = "".join(
        f'<div style="display:flex;gap:18px;align-items:baseline;padding:8px 0;border-bottom:1px solid rgba(255,255,255,.08)">'
        f'<span class="mono" style="font-size:13px;color:#a99fff">{i:02d}</span><span style="font-size:18px;color:#fff;font-weight:500">{esc(f)}</span></div>'
        for i, f in enumerate(files, 1))
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:800px;height:800px;right:-300px;top:-300px"></div>
<img class="shot" src="{snap('01', 3)}" style="width:330px;right:70px;top:110px;transform:rotate(4deg)">
<img class="shot" src="{snap('03', 3)}" style="width:300px;right:330px;top:200px;transform:rotate(-5deg)">
<div style="position:absolute;left:72px;top:52px;width:520px">
  <div class="brand" style="margin-bottom:22px">What’s inside</div>
  <h1 style="font-size:42px;margin-bottom:16px">10 files. One complete<br><span class="soft">content system.</span></h1>
  {rows}
</div>
"""
    return page(html, w, h), w, h


def preview_prompts():
    w, h = 1280, 720
    cats = ["Content ideas", "Instagram posts", "Reels", "TikTok", "LinkedIn", "Captions", "Storytelling", "Repurposing"]
    chips = "".join(f'<span class="chip">{c}</span>' for c in cats)
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:820px;height:820px;right:-280px;bottom:-380px"></div>
<img class="shot" src="{snap('02', 5)}" style="width:400px;right:60px;top:70px;transform:rotate(3deg)">
<img class="shot" src="{snap('02', 4)}" style="width:360px;right:360px;top:190px;transform:rotate(-5deg)">
<div style="position:absolute;left:72px;top:72px;width:470px">
  <div class="brand" style="margin-bottom:30px">File 02</div>
  <h1 style="font-size:64px;margin-bottom:24px">100<br><span class="soft">AI prompts</span></h1>
  <div class="sub" style="font-size:22px;line-height:1.4;margin-bottom:30px">Copy, fill in the blanks, paste into any AI chat tool. Every prompt is ready to use.</div>
  <div>{chips}</div>
</div>
"""
    return page(html, w, h), w, h


def preview_calendar():
    w, h = 1280, 720
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:820px;height:820px;left:-300px;bottom:-420px"></div>
<img class="shot" src="{snap('05', 4)}" style="width:700px;right:-40px;top:250px;transform:rotate(-3deg)">
<div style="position:absolute;left:72px;top:68px;width:1100px">
  <div class="brand" style="margin-bottom:26px">File 05</div>
  <h1 style="font-size:60px;margin-bottom:20px">Your next 30 days, <span class="soft">planned.</span></h1>
  <div class="sub" style="font-size:22px;line-height:1.4;width:470px">Every day: what to post, the format, the goal, the CTA — and the exact prompt, hook or template to use.</div>
</div>
<div style="position:absolute;left:72px;bottom:70px;display:flex;gap:44px">
  <div><div style="font-family:var(--display);font-size:44px;color:#fff;font-weight:700">30</div><div class="mono" style="font-size:12px;color:#8d8f99">Days</div></div>
  <div><div style="font-family:var(--display);font-size:44px;color:#fff;font-weight:700">4</div><div class="mono" style="font-size:12px;color:#8d8f99">Weekly themes</div></div>
  <div><div style="font-family:var(--display);font-size:44px;color:#fff;font-weight:700">6</div><div class="mono" style="font-size:12px;color:#8d8f99">Pillars</div></div>
</div>
"""
    return page(html, w, h), w, h


def preview_hooks():
    w, h = 1280, 720
    samples = ["Nobody tells you this about [TOPIC]…", "Stop doing [X] if you want [RESULT].", "I wish I knew this when I started [ACTIVITY]."]
    def fmt(s):
        import re
        return re.sub(r"\[([A-Z ]+)\]", r'<span style="color:#a99fff">[\1]</span>', esc(s))
    lines = "".join(f'<div style="font-family:var(--display);font-size:27px;color:#fff;font-weight:600;padding:15px 0;border-bottom:1px solid rgba(255,255,255,.1)">{fmt(s)}</div>' for s in samples)
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:820px;height:820px;right:-320px;top:-320px"></div>
<img class="shot" src="{snap('04', 4)}" style="width:400px;right:70px;top:110px;transform:rotate(4deg)">
<div style="position:absolute;left:72px;top:72px;width:640px">
  <div class="brand" style="margin-bottom:28px">File 04</div>
  <h1 style="font-size:62px;margin-bottom:20px">50 hooks for <span class="soft">stronger<br>first lines</span></h1>
  <div class="sub" style="font-size:21px;margin-bottom:22px">8 styles · fill-in-the-blank · a worked example for every hook</div>
  {lines}
</div>
"""
    return page(html, w, h), w, h


def preview_bonus():
    w, h = 1280, 720
    items = [("08", "50 CTAs", "Natural calls to action for every goal"), ("09", "30 AI Image Prompts", "On-brand visuals in 10 styles"),
             ("10", "Content Repurposing System", "One idea → 16 pieces of content")]
    cards = "".join(
        f'<div style="width:350px"><div style="height:330px;overflow:hidden;border-radius:6px;box-shadow:0 24px 50px rgba(0,0,0,.5)"><img src="{snap(n, 1)}" style="width:350px;display:block;margin-top:-165px"></div>'
        f'<div class="mono" style="font-size:12px;color:#a99fff;margin-top:22px">Bonus file {n}</div>'
        f'<div style="font-family:var(--display);font-size:26px;color:#fff;font-weight:700;margin-top:6px">{esc(t)}</div>'
        f'<div style="font-size:17px;color:#a7a9b2;margin-top:4px">{esc(d)}</div></div>'
        for n, t, d in items)
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:900px;height:900px;left:190px;top:-560px"></div>
<div style="position:absolute;left:72px;top:58px;right:72px;display:flex;justify-content:space-between;align-items:flex-end">
  <h1 style="font-size:54px">Plus <span class="soft">3 bonus files</span></h1>
  <div class="brand">Included at no extra cost</div>
</div>
<div style="position:absolute;left:72px;right:72px;top:170px;display:flex;justify-content:space-between;height:520px;overflow:hidden">{cards}</div>
"""
    return page(html, w, h), w, h


def images():
    out = []
    for name, fn in [("gumroad-cover", cover), ("gumroad-thumbnail", thumbnail), ("preview-1-whats-inside", preview_inside),
                     ("preview-2-100-ai-prompts", preview_prompts), ("preview-3-30-day-calendar", preview_calendar),
                     ("preview-4-50-hooks", preview_hooks), ("preview-5-bonus-content", preview_bonus)]:
        html, w, h = fn()
        out.append((name, html, w, h))
    return out
