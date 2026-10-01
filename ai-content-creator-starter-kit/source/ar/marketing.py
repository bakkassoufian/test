"""Arabic Gumroad cover, thumbnail and five previews (mirrored, right-to-left).

Mockups are real snapshots of the Arabic PDFs (out/snapshots/ar-XX-<page>.png).
"""

from lib import esc
from marketing import BASE_CSS

RTL_CSS = """
<link rel="stylesheet" href="../rtl.css">
<style>
  body { direction: rtl; }
  .brand::before { order: 0; }
  h1 { line-height: 1.3; }
</style>
"""

COVER = dict(title="حقيبة صانع المحتوى", second="بالذكاء الاصطناعي", subtitle="30 يومًا من صناعة المحتوى بالذكاء الاصطناعي",
             badge="100 برومبت + 100 فكرة + تقويم 30 يومًا")


def page(html, w, h):
    return (f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">{BASE_CSS}{RTL_CSS}</head>'
            f'<body class="rtl"><div class="canvas" style="width:{w}px;height:{h}px">{html}</div></body></html>')


def snap(n, page_no):
    return f"snapshots/ar-{n}-{page_no}.png"


def cover():
    w, h = 1280, 720
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:900px;height:900px;left:-260px;bottom:-420px"></div>
<img class="shot" src="{snap('05', 4)}" style="width:430px;left:-40px;top:300px;transform:rotate(4deg)">
<img class="shot" src="{snap('02', 5)}" style="width:300px;left:250px;top:150px;transform:rotate(8deg)">
<img class="shot" src="{snap('01', 1)}" style="width:310px;left:40px;top:60px;transform:rotate(-5deg)">
<div style="position:absolute;right:72px;top:60px" class="brand">حقيبة رقمية · 10 ملفات PDF</div>
<div style="position:absolute;right:72px;top:170px;width:650px">
  <div class="badge" style="font-size:17px;padding:10px 22px;margin-bottom:30px">{esc(COVER['badge'])}</div>
  <h1 style="font-size:70px">{esc(COVER['title'])}<br><span class="soft">{esc(COVER['second'])}</span></h1>
  <div class="rule" style="margin:30px 0 22px"></div>
  <div class="sub" style="font-size:27px;font-weight:500">{esc(COVER['subtitle'])}</div>
</div>
"""
    return page(html, w, h), w, h


def thumbnail():
    w, h = 600, 600
    html = f"""
<div class="grid" style="background-size:40px 40px"></div>
<div class="glow" style="width:620px;height:620px;left:-260px;bottom:-280px"></div>
<img class="shot" src="{snap('01', 1)}" style="width:250px;left:-36px;bottom:-110px;transform:rotate(7deg)">
<div style="position:absolute;right:46px;top:46px;width:520px">
  <div class="brand" style="font-size:14px;margin-bottom:40px">حقيبة البداية</div>
  <h1 style="font-size:54px">حقيبة صانع<br>المحتوى<br><span class="soft">بالذكاء الاصطناعي</span></h1>
  <div class="rule" style="margin:24px 0 18px"></div>
  <div class="sub" style="font-size:21px;font-weight:500;width:330px;line-height:1.5">100 برومبت، 100 فكرة<br>وخطة لـ 30 يومًا</div>
</div>
"""
    return page(html, w, h), w, h


def preview_inside():
    w, h = 1280, 720
    files = ["دليل البدء السريع", "100 برومبت للذكاء الاصطناعي", "100 فكرة محتوى", "50 خطّافًا قويًا", "تقويم المحتوى لـ 30 يومًا",
             "قوالب مواقع التواصل", "قائمة تحقق النشر", "ملحق · 50 دعوة لاتخاذ إجراء", "ملحق · 30 برومبت للصور", "ملحق · نظام إعادة توظيف المحتوى"]
    rows = "".join(
        f'<div style="display:flex;gap:18px;align-items:baseline;padding:5px 0;border-bottom:1px solid rgba(255,255,255,.08)">'
        f'<span style="font-size:15px;color:#a99fff;font-weight:600">{i:02d}</span><span style="font-size:19px;color:#fff;font-weight:500">{esc(f)}</span></div>'
        for i, f in enumerate(files, 1))
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:800px;height:800px;left:-300px;top:-300px"></div>
<img class="shot" src="{snap('01', 3)}" style="width:330px;left:70px;top:110px;transform:rotate(-4deg)">
<img class="shot" src="{snap('03', 4)}" style="width:300px;left:330px;top:200px;transform:rotate(5deg)">
<div style="position:absolute;right:72px;top:44px;width:540px">
  <div class="brand" style="margin-bottom:14px">ماذا بداخل الحقيبة</div>
  <h1 style="font-size:40px;margin-bottom:12px">10 ملفات. نظام محتوى <span class="soft">متكامل.</span></h1>
  {rows}
</div>
"""
    return page(html, w, h), w, h


def preview_prompts():
    w, h = 1280, 720
    cats = ["أفكار المحتوى", "منشورات إنستغرام", "ريلز", "تيك توك", "لينكدإن", "الكابشن", "سرد القصص", "إعادة التوظيف"]
    chips = "".join(f'<span class="chip" style="font-size:15px">{c}</span>' for c in cats)
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:820px;height:820px;left:-280px;bottom:-380px"></div>
<img class="shot" src="{snap('02', 6)}" style="width:400px;left:60px;top:70px;transform:rotate(-3deg)">
<img class="shot" src="{snap('02', 5)}" style="width:360px;left:360px;top:190px;transform:rotate(5deg)">
<div style="position:absolute;right:72px;top:64px;width:470px">
  <div class="brand" style="margin-bottom:24px">الملف 02</div>
  <h1 style="font-size:62px;margin-bottom:20px">100<br><span class="soft">برومبت جاهز</span></h1>
  <div class="sub" style="font-size:22px;line-height:1.6;margin-bottom:26px">انسخ، املأ الفراغات، والصق في أي أداة ذكاء اصطناعي. كل برومبت جاهز للاستخدام بالعربية.</div>
  <div>{chips}</div>
</div>
"""
    return page(html, w, h), w, h


def preview_calendar():
    w, h = 1280, 720
    stat = lambda v, l: f'<div><div style="font-family:var(--display);font-size:44px;color:#fff;font-weight:700;line-height:1.2">{v}</div><div style="font-size:15px;color:#8d8f99">{l}</div></div>'
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:820px;height:820px;right:-300px;bottom:-420px"></div>
<img class="shot" src="{snap('05', 4)}" style="width:700px;left:-40px;top:250px;transform:rotate(3deg)">
<div style="position:absolute;right:72px;top:60px;width:1100px">
  <div class="brand" style="margin-bottom:20px">الملف 05</div>
  <h1 style="font-size:58px;margin-bottom:14px">أيامك الثلاثون القادمة، <span class="soft">مخطّطة.</span></h1>
  <div class="sub" style="font-size:22px;line-height:1.6;width:480px">كل يوم: ماذا تنشر، والصيغة، والهدف، والدعوة لاتخاذ إجراء — والبرومبت أو الخطّاف أو القالب الذي تستخدمه.</div>
</div>
<div style="position:absolute;right:72px;bottom:64px;display:flex;gap:44px">
  {stat("30", "يومًا")}{stat("4", "محاور أسبوعية")}{stat("6", "ركائز")}
</div>
"""
    return page(html, w, h), w, h


def preview_hooks():
    import re
    w, h = 1280, 720
    samples = ["لا أحد يخبرك بهذا عن [الموضوع]…", "توقّف عن [س] إذا كنت تريد [النتيجة].", "تمنيت لو عرفت هذا عندما بدأت [النشاط]."]

    def fmt(s):
        return re.sub(r"\[([^\]]+)\]", r'<span style="color:#a99fff">[\1]</span>', esc(s))
    lines = "".join(f'<div style="font-family:var(--display);font-size:27px;color:#fff;font-weight:600;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.1)">{fmt(s)}</div>' for s in samples)
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:820px;height:820px;left:-320px;top:-320px"></div>
<img class="shot" src="{snap('04', 4)}" style="width:400px;left:70px;top:110px;transform:rotate(-4deg)">
<div style="position:absolute;right:72px;top:64px;width:640px">
  <div class="brand" style="margin-bottom:22px">الملف 04</div>
  <h1 style="font-size:58px;margin-bottom:14px">50 خطّافًا <span class="soft">لجمل أولى أقوى</span></h1>
  <div class="sub" style="font-size:21px;margin-bottom:16px">8 أساليب · املأ الفراغات · مثال محلول لكل خطّاف</div>
  {lines}
</div>
"""
    return page(html, w, h), w, h


def preview_bonus():
    w, h = 1280, 720
    items = [("08", "50 دعوة لاتخاذ إجراء", "دعوات طبيعية لكل هدف"), ("09", "30 برومبت للصور", "صور متسقة مع هويتك في 10 أساليب"),
             ("10", "نظام إعادة توظيف المحتوى", "فكرة واحدة ← 16 قطعة محتوى")]
    cards = "".join(
        f'<div style="width:350px"><div style="height:330px;overflow:hidden;border-radius:6px;box-shadow:0 24px 50px rgba(0,0,0,.5)"><img src="{snap(n, 1)}" style="width:350px;display:block;margin-top:-165px"></div>'
        f'<div style="font-size:15px;color:#a99fff;margin-top:18px;font-weight:600">ملف الملحق {n}</div>'
        f'<div style="font-family:var(--display);font-size:26px;color:#fff;font-weight:700;margin-top:2px">{esc(t)}</div>'
        f'<div style="font-size:18px;color:#a7a9b2;margin-top:2px">{esc(d)}</div></div>'
        for n, t, d in items)
    html = f"""
<div class="grid"></div>
<div class="glow" style="width:900px;height:900px;right:190px;top:-560px"></div>
<div style="position:absolute;right:72px;top:46px;left:72px;display:flex;justify-content:space-between;align-items:flex-end">
  <h1 style="font-size:54px">ومعها <span class="soft">3 ملفات إضافية</span></h1>
  <div class="brand">مضمّنة دون تكلفة إضافية</div>
</div>
<div style="position:absolute;right:72px;left:72px;top:170px;display:flex;justify-content:space-between;height:530px;overflow:hidden">{cards}</div>
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
