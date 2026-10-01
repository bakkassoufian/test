"""Arabic builders for files 02, 03, 04, 05, 06, 08 and 09 (mirror build.py)."""

from ar.content import calendar, ctas, hooks, ideas, image_prompts, prompts, templates
from ar.refs import ref
from lib import (bullets, callout, card, doc_cover, esc, flow, h3, p, page_head, placeholders, rich, section_head, table, toc, write_lines)

BRAND = "حقيبة صانع المحتوى بالذكاء الاصطناعي"
LABELS = dict(brand=BRAND, file="الملف {num} / 10", kicker="الملف {num}", tagline="اصنع. خطّط. انشر. تقدّم.", usage="للاستخدام الشخصي ومع العملاء")


def cover(num, title, subtitle, stats, kicker=None):
    return doc_cover(num, title, subtitle, stats, kicker=kicker, labels=LABELS)


def glossary_table(gloss, used):
    rows = [[f'<span class="ph">[{esc(k)}]</span>', esc(gloss[k])] for k in gloss if k in used]
    return table(["الخانة", "ماذا تكتب فيها"], rows, cls="t gloss", widths=["46mm", "auto"])


def ranges(categories):
    out, n = [], 0
    for cat in categories:
        k = len(cat[-1])
        out.append((cat[0], n + 1, n + k))
        n += k
    return out


# ---------------------------------------------------------------- 02

def prompts_doc():
    used = set()
    for _t, _d, items in prompts.CATEGORIES:
        for _title, text, _tip in items:
            used.update(placeholders(text))
    s = [cover("02", "100 برومبت<br>للذكاء الاصطناعي", "برومبتات جاهزة للأفكار والمنشورات والريلز وتيك توك ولينكدإن والكابشن وسرد القصص وإعادة التوظيف.",
               [("100", "برومبت"), ("8", "فئات"), ("أي", "أداة ذكاء اصطناعي")], kicker="مكتبة البرومبتات")]
    s.append(flow("طريقة الاستخدام", [
        page_head("ابدأ هنا", "كيف تستخدم هذه البرومبتات",
                  "كُتب كل برومبت ليعمل في أي مساعد ذكاء اصطناعي — ChatGPT أو Claude أو Gemini أو Copilot أو غيرها. ولا يحتاج أي إعدادات خاصة."),
        '<div class="grid-2">'
        + card("انسخ البرومبت", "انسخ النص الكامل للبرومبت في أداة الذكاء الاصطناعي.", tag="الخطوة 01")
        + card("استبدل الخانات", "استبدل كل [خانة] بتفاصيلك. كلما كنت أدق، كانت النتيجة أفضل.", tag="الخطوة 02")
        + card("راجع النتيجة", "اقرأها بعين ناقدة. احتفظ بالمفيد، واحذف العام، وتحقّق من كل معلومة.", tag="الخطوة 03")
        + card("حسّن بالمتابعة", "اطلب تعديلات: «أقصر»، «كلمات أبسط»، «أكثر تحديدًا للمبتدئين»، «5 خيارات أخرى».", tag="الخطوة 04")
        + "</div>",
        callout("قبل أول برومبت، عرّف الذكاء الاصطناعي بنفسك مرة واحدة: «أنا صانع محتوى في [المجال]. جمهوري [الجمهور المستهدف]. أبيع [المنتج/الخدمة]. نبرتي [النبرة]. اكتب كل الإجابات بالعربية.» ومعظم الأدوات تتذكر ذلك طوال المحادثة.", label="وفّر وقتك"),
        callout("حدّد اللغة التي يتحدث بها جمهورك: فصحى مبسطة تصل إلى كل العالم العربي، أو لهجة محلية (مغربية، مصرية، خليجية، شامية…) لقرب أكبر. أضفها إلى خانة [النبرة].", label="الفصحى أم اللهجة؟"),
    ]))
    s.append(flow("المحتويات", [
        page_head("المحتويات", "ثماني فئات، مئة برومبت", "كل فئة تبدأ بصفحة تعريفية. ابدأ بالفئة التي تناسب ما تنشره هذا الأسبوع."),
        toc([(f"{a:03d}–{b:03d}", t, f"{b - a + 1} برومبت") for t, a, b in ranges(prompts.CATEGORIES)]),
        callout("لا تحاول استخدام البرومبتات بالترتيب. اتبع تقويم الـ 30 يومًا (الملف 05) — فهو يخبرك بالبرومبت المناسب لكل يوم.", label="من أين تبدأ"),
    ]))
    s.append(flow("دليل الخانات", [
        page_head("مرجع", "دليل الخانات", "تظهر هذه الخانات في البرومبتات. استبدل الأقواس وما بداخلها بتفاصيلك."),
        glossary_table(prompts.GLOSSARY, used),
    ]))
    n = 0
    for ci, (title, desc, items) in enumerate(prompts.CATEGORIES, 1):
        blocks = [section_head(f"الفئة {ci:02d} · {len(items)} برومبت", title, desc, f"{ci:02d}")]
        for ptitle, text, tip in items:
            n += 1
            fields = placeholders(text)
            cust = ('<div class="cust"><b>خصّص</b>' + "".join(f'<span class="ph">[{esc(f)}]</span>' for f in fields) + "</div>") if fields else ""
            tip_html = f'<div class="tip"><b>نصيحة:</b> {rich(tip)}</div>' if tip else ""
            blocks.append(
                f'<div class="pcard"><div class="top"><span class="n">{n:03d}</span><span class="title">{esc(ptitle)}</span></div>'
                f'<div class="body"><span class="lbl">البرومبت</span>{rich(text)}</div>{cust}{tip_html}</div>')
        s.append(flow(f"{ci:02d} · {title}", blocks))
    return s


# ---------------------------------------------------------------- 03

def ideas_doc():
    s = [cover("03", "100 فكرة<br>محتوى", "أفكار قابلة للتكييف مع أي مجال — لكل منها صيغة مقترحة ودعوة لاتخاذ إجراء.",
               [("100", "فكرة"), ("8", "فئات"), ("∞", "مجالات")], kicker="بنك الأفكار")]
    s.append(flow("طريقة الاستخدام", [
        page_head("ابدأ هنا", "كيف تستخدم هذه الأفكار",
                  "هذه الأفكار مرنة عن قصد. المهارة الحقيقية هي جعلها محددة لمجالك — وهنا يساعدك الذكاء الاصطناعي."),
        h3("اجعل أي فكرة محددة"),
        table(["الفكرة العامة", "بعد التحديد"], [
            ["خطأ شائع وشرحه", "«خطأ السقي الذي يقتل معظم نباتات المبتدئين المنزلية»"],
            ["خطة البداية في 3 خطوات", "«كيف تبدأ في كتابة المحتوى المستقل في 3 خطوات — دون معرض أعمال»"],
            ["الأدوات التي أستخدمها يوميًا", "«التطبيقات الأربعة التي أدير بها طلبات مخبزي»"],
            ["الاعتقاد مقابل الواقع", "«اعتقاد: يجب أن تتمدد قبل كل جري»"],
        ], split=False, widths=["60mm", "auto"]),
        callout("الصق أي فكرة في أداة الذكاء الاصطناعي مع هذا البرومبت: «كيّف فكرة المحتوى هذه مع [المجال] و[الجمهور المستهدف]: [الفكرة]. أعطني 5 نسخ محددة مع عنوان مبدئي وخطّاف لكل منها.»", label="برومبت تكييف سريع"),
    ]))
    s.append(flow("المحتويات", [
        page_head("المحتويات", "ثماني فئات، مئة فكرة", "اختر الفئة التي تطابق ركيزة المحتوى التي تعمل عليها اليوم."),
        toc([(f"{a:03d}–{b:03d}", t, f"{b - a + 1} فكرة") for t, a, b in ranges(ideas.CATEGORIES)]),
        callout("مزيج متوازن للأسبوع: فكرتان تعليميتان، وفكرة شخصية، وفكرة تفاعلية، وفكرة ترويجية واحدة.", label="نصيحة"),
    ]))
    n = 0
    for ci, (title, desc, items) in enumerate(ideas.CATEGORIES, 1):
        rows = []
        for it, expl, fmt, cta in items:
            n += 1
            rows.append(
                f'<div class="idea"><div class="n">{n:03d}</div><div><h4>{rich(it)}</h4><p>{rich(expl)}</p>'
                f'<div class="meta"><div><b>الصيغة</b><span>{esc(fmt)}</span></div><div><b>الدعوة المقترحة</b><span>{rich(cta)}</span></div></div></div></div>')
        s.append(flow("100 فكرة محتوى", [section_head(f"الفئة {ci:02d} · {len(items)} فكرة", title, desc, f"{ci:02d}"),
                                         '<div data-split="items">' + "".join(rows) + "</div>"], brk=(ci == 1)))
    return s


# ---------------------------------------------------------------- 04

def hooks_doc():
    used = set()
    for _t, _d, items in hooks.CATEGORIES:
        for tpl, _ex, _fit in items:
            used.update(placeholders(tpl))
    s = [cover("04", "50 خطّافًا<br>قويًا", "جمل افتتاحية بفراغات تملؤها في 8 أساليب — لكل منها مثال محلول من مجال مختلف.",
               [("50", "خطّافًا"), ("8", "أساليب"), ("50", "مثالًا")], kicker="جمل افتتاحية")]
    s.append(flow("طريقة الاستخدام", [
        page_head("ابدأ هنا", "كيف تستخدم هذه الخطّافات",
                  "الخطّاف هو أول ما يراه الناس: السطر الأول في الكابشن، أو غلاف الكاروسيل، أو أول ثانيتين في الفيديو. تمنحك هذه القوالب بنية بداية مجرّبة."),
        '<div class="grid-3">'
        + card("اختر الأسلوب", "طابِق أسلوب الخطّاف مع محتواك: منشور الأخطاء يحتاج خطّاف خطأ.", tag="01")
        + card("املأ الفراغات", "استبدل الخانات بكلمات محددة يستخدمها جمهورك.", tag="02")
        + card("أوفِ بالوعد", "تأكد أن المحتوى يقدّم بالضبط ما يوحي به الخطّاف.", tag="03")
        + "</div>",
        h3("قواعد لخطّافات صادقة وفعّالة"),
        bullets([
            "**التحديد يتفوّق على الذكاء.** «3 أخطاء يقع فيها العدّاؤون الجدد» أقوى من «أسرار الجري».",
            "**القِصر يتفوّق على الطول.** استهدف أقل من 12 كلمة، واحذف كل ما لا يضيف معنى.",
            "**الصدق يتفوّق على الإثارة.** لا تعد أبدًا بنتيجة لا يستطيع محتواك تقديمها.",
            "**جرّب أكثر من واحد.** اكتب ثلاث نسخ واختر التي كانت ستوقفك عن التمرير.",
        ]),
        h3("المحتويات"),
        toc([(f"{a:02d}–{b:02d}", t, f"{b - a + 1} خطّافات") for t, a, b in ranges(hooks.CATEGORIES)]),
    ]))
    s.append(flow("دليل الخانات", [
        page_head("مرجع", "دليل الخانات", "ماذا تكتب في كل خانة."),
        glossary_table(hooks.GLOSSARY, used),
    ]))
    n = 0
    for ci, (title, desc, items) in enumerate(hooks.CATEGORIES, 1):
        rows = []
        for tpl, ex, fit in items:
            n += 1
            rows.append(
                f'<div class="hook"><div class="n">{n:02d}</div><div><div class="line">{rich(tpl)}</div>'
                f'<div class="ex"><b>مثال</b>{esc(ex)}</div><div class="fit"><b>يناسب</b>{esc(fit)}</div></div></div>')
        s.append(flow(f"{ci:02d} · {title}", [section_head(f"الأسلوب {ci:02d} · {len(items)} خطّافات", title, desc, f"{ci:02d}"),
                                              '<div data-split="items">' + "".join(rows) + "</div>"]))
    return s


# ---------------------------------------------------------------- 05

def calendar_doc():
    s = [cover("05", "تقويم المحتوى<br>لـ 30 يومًا", "شهر كامل ومتوازن من المحتوى — مع البرومبت أو الفكرة أو القالب الذي تستخدمه كل يوم.",
               [("30", "يومًا"), ("6", "ركائز وصيغ"), ("1", "شخص يكفي")], kicker="شهرك مخطَّط")]
    legend = " ".join(f'<span class="pillar {c}">{esc(n)}</span>' for n, c in calendar.PILLARS.values())
    s.append(flow("طريقة الاستخدام", [
        page_head("ابدأ هنا", "كيف تستخدم هذا التقويم",
                  "كل يوم يخبرك ماذا تنشر، وبأي صيغة، وأي ركيزة يخدم، والهدف، والدعوة لاتخاذ إجراء — وأي أدوات من هذه الحقيبة تستخدم."),
        '<div class="grid-3">'
        + card("جهّز شهرك", "املأ ورقة العمل في الصفحة التالية. تستغرق 15 دقيقة وتجعل كل برومبت أدق.", tag="قبل اليوم 1")
        + card("اتبع إحالات الحقيبة", "«برومبت 022» تعني الملف 02، البرومبت 022. و«فكرة» و«خطّاف» و«قالب» تحيل إلى الملفات 03 و04 و06.", tag="كل يوم")
        + card("راجع في الأيام الأخف", "الأيام 7 و14 و21 و28 أخف لتراجع وترد وتخطط للأسبوع التالي.", tag="أسبوعيًا")
        + "</div>",
        h3("ألوان الركائز"),
        f"<p>{legend}</p>",
        callout("النشر اليومي ليس شرطًا. إذا كان 3–4 منشورات أسبوعيًا هو الواقعي بالنسبة لك، فاتبع التقويم بالترتيب وخذ وقتًا أطول لإكماله. الاستمرارية أهم من السرعة.", label="اجعله لك"),
        p("استبدل أي يوم لا يناسب مشروعك بفكرة من الركيزة نفسها في الملف 03.", "small"),
    ]))
    s.append(flow("جهّز شهرك", [
        page_head("ورقة عمل", "جهّز شهرك", "أجب عن هذه الأسئلة قبل اليوم 1. والصق إجاباتك في أداة الذكاء الاصطناعي في بداية كل جلسة."),
        '<div class="grid-2"><div>' + write_lines([
            ("مجالي", "كن محددًا: من وماذا.", 1),
            ("جمهوري المستهدف", "لمن تصنع المحتوى بالضبط؟", 1),
            ("أكبر مشكلة لديهم", "بكلماتهم هم، لا بكلماتك.", 1),
            ("النتيجة التي يريدونها", None, 1),
        ]) + "</div><div>" + write_lines([
            ("ما أبيعه (أو سأبيعه)", "منتج، خدمة، نشرة بريدية، أو لا شيء بعد.", 1),
            ("منصتي الرئيسية", "ابدأ بواحدة.", 1),
            ("ركائز محتواي (3–4)", None, 1),
            ("نبرتي في 3 كلمات", "مثل: هادئة، عملية، دافئة", 1),
        ]) + "</div></div>",
        callout("الصق هذا في أداة الذكاء الاصطناعي في بداية كل جلسة: «أصنع محتوى عن [المجال] لـ [الجمهور المستهدف]. مشكلتهم الأساسية [المشكلة]. نبرتي [النبرة]. اكتب بالعربية، وتذكّر ذلك في كل ما سنصنعه اليوم.»", label="برومبت السياق"),
    ]))
    day = 0
    for wi, (wtitle, wdesc, days) in enumerate(calendar.WEEKS, 1):
        rows = []
        for idea_t, fmt, pillar, goal, cta, kit in days:
            day += 1
            pname, pcls = calendar.PILLARS[pillar]
            review = day in (7, 14, 21, 28)
            kit_html = " · ".join(ref(k, t) for k, t in kit)
            label = "<small>مراجعة</small>" if review else ""
            rows.append(f'<tr class="{"review" if review else ""}"><td class="day">{day:02d}{label}</td>'
                        f'<td><span class="idea-t">{rich(idea_t)}</span><span class="kit">{esc(kit_html)}</span></td>'
                        f"<td>{esc(fmt)}</td><td><span class=\"pillar {pcls}\">{esc(pname)}</span></td><td>{esc(goal)}</td><td>{rich(cta)}</td>"
                        f'<td><div class="done"></div></td></tr>')
        head = "<thead><tr><th>اليوم</th><th>فكرة المحتوى · الأدوات</th><th>الصيغة</th><th>الركيزة</th><th>الهدف</th><th>الدعوة</th><th>تم</th></tr></thead>"
        cols = '<colgroup><col style="width:15mm"><col style="width:auto"><col style="width:26mm"><col style="width:26mm"><col style="width:28mm"><col style="width:62mm"><col style="width:11mm"></colgroup>'
        tbl = f'<table class="cal" data-split="items">{cols}{head}<tbody>{"".join(rows)}</tbody></table>'
        short, long_ = wtitle.split(" — ")
        blocks = [section_head(short, long_, wdesc), tbl]
        if wi == len(calendar.WEEKS):
            blocks.append('<div class="spacer-lg"></div>')
            blocks.append('<div class="grid-3">'
                          + card("قم بمراجعتك الشهرية", "استخدم صفحة المراجعة الشهرية في نهاية هذا الملف لترى ما نجح.", tag="اليوم 31")
                          + card("احتفظ بأفضل أفكارك", "أضف أفضل 5 منشورات إلى قائمة. فهي أول ما تعيد توظيفه الشهر القادم.", tag="الشهر القادم")
                          + card("خطّط للشهر الثاني", "كرّر البنية نفسها بأفكار جديدة من الملف 03 وزوايا جديدة لأفضل مواضيعك.", tag="استمر")
                          + "</div>")
        s.append(flow(short, blocks))
    assert day == 30

    formats = [d[1] for w in calendar.WEEKS for d in w[2]]
    cells = "".join(f'<div class="cell"><span class="dn">{i:02d}</span><span class="fmt">{esc(f)}</span><span class="box"></span></div>' for i, f in enumerate(formats, 1))
    s.append(flow("متابعة الـ 30 يومًا", [
        page_head("المتابعة", "متابعة الـ 30 يومًا", "ضع علامة على كل يوم تنشر فيه. رؤية السلسلة تكبر محفّزة أكثر مما تتوقع."),
        f'<div class="tracker">{cells}</div>',
    ]))
    s.append(flow("المراجعة الشهرية", [
        page_head("بعد اليوم 30", "المراجعة الشهرية", "خصّص 30 دقيقة للنظر إلى الوراء قبل التخطيط للشهر التالي."),
        '<div class="grid-2"><div>' + write_lines([
            ("أفضل 3 منشورات هذا الشهر (ولماذا نجحت)", None, 3),
            ("أي ركيزة حصلت على أفضل تفاعل؟", None, 1),
            ("أي صيغة كانت الأسهل في الإنتاج؟", None, 1),
        ]) + "</div><div>" + write_lines([
            ("أكثر الأسئلة التي طرحها جمهوري", None, 3),
            ("ما سأفعل منه أكثر الشهر القادم", None, 1),
            ("ما سأتوقف عنه أو أغيّره", None, 1),
        ]) + "</div></div>",
        callout("ابدأ الشهر الثاني بتكرار أفضل 5 أيام أداءً بزوايا جديدة، ثم املأ الفراغات بأفكار جديدة من الملف 03.", label="الشهر القادم"),
    ]))
    return s


# ---------------------------------------------------------------- 06

def templates_doc():
    s = [cover("06", "قوالب مواقع<br>التواصل", "15 قالبًا شريحةً بشريحة مع النصوص والتصميم والتوجيه البصري — سهلة الإعادة في Canva.",
               [("15", "قالبًا"), ("4:5", "جاهزة للنشر"), ("Canva", "متوافقة")], kicker="مخططات التصميم")]
    s.append(flow("طريقة الاستخدام", [
        page_head("ابدأ هنا", "بناء هذه القوالب في Canva",
                  "يعطيك كل قالب البنية والنص المقترح والتوجيه البصري. ابنِه مرة واحدة في Canva، واحفظه كقالب خاص بك، وأعد استخدامه لأشهر."),
        table(["الإعداد", "التوصية"], [
            ["<strong>حجم التصميم</strong>", "منشور إنستغرام عمودي — 1080 × 1350 بكسل. أغلفة الستوري والريلز — 1080 × 1920 بكسل."],
            ["<strong>الهوامش</strong>", "أبقِ النص على بُعد 80 بكسل على الأقل من كل حافة. فعّل الهوامش من: ملف ← إعدادات العرض ← إظهار الهوامش."],
            ["<strong>الخطوط</strong>", "خط عناوين عريض واحد (مثل Cairo أو Tajawal) وخط نص واضح (مثل IBM Plex Sans Arabic أو Noto Sans Arabic)."],
            ["<strong>الألوان</strong>", "لون داكن ولون فاتح ولون مميز واحد. احفظها في Brand Kit أو كلوحة ألوان."],
            ["<strong>حجم النص</strong>", "العناوين 60–90 نقطة، والنص 32 نقطة على الأقل ليُقرأ على الهاتف."],
            ["<strong>الاتساق</strong>", "أبقِ العناوين وأرقام الصفحات واسم حسابك في المكان نفسه في كل شريحة."],
        ], split=False, widths=["36mm", "auto"]),
        h3("كيف تقرأ كل قالب"),
        bullets([
            "**بنية الشرائح** — نموذج مصغّر لكل شريحة وما يوضع فيها.",
            "**النص المقترح** — نص لكل شريحة تملأ فراغاته. استبدل [الخانات] بتفاصيلك.",
            "**التوصية البصرية** — نصائح تصميم وتنسيق خاصة بهذه الصيغة.",
            "**الدعوة لاتخاذ إجراء** — دعوة طبيعية تناسب هدف القالب.",
        ]),
        callout("في التصاميم العربية، ابدأ القراءة من اليمين: ضع العنوان والأرقام في الجهة اليمنى، واجعل اتجاه الأسهم والتقدّم من اليمين إلى اليسار.", label="ملاحظة للتصميم العربي"),
    ]))
    s.append(flow("المحتويات", [
        page_head("المحتويات", "القوالب الخمسة عشر", "لكل قالب صفحته. ابدأ بالقوالب التي تناسب المحتوى الذي تنشره أكثر."),
        toc([(f"{i:02d}", t["name"], t["format"].split(" · ")[0]) for i, t in enumerate(templates.TEMPLATES, 1)]),
        callout("ابنِ أكثر ثلاثة قوالب تستخدمها أولًا — عادةً الكاروسيل التعليمي و3 نصائح والاقتباس. احفظها في Canva وانسخها لكل منشور جديد.", label="من أين تبدأ"),
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
        note = callout(t["note"], label="ملاحظة") if t.get("note") else ""
        s.append(flow(f"القالب {i:02d}", [
            f'<div class="kwn"><div class="eyebrow">القالب {i:02d} · {esc(t["format"])}</div><h1 class="page-title">{esc(t["name"])}</h1></div>',
            f'<p class="lead" style="margin-bottom:4mm">{rich(t["purpose"])}</p>',
            h3("بنية الشرائح"), strip,
            h3("النص المقترح"), copy,
            f'<div class="tpl-meta"><div><h3 class="h" style="margin-top:0">التوصية البصرية</h3>{visual}</div>'
            f'<div><h3 class="h" style="margin-top:0">الدعوة لاتخاذ إجراء</h3><div class="callout" style="margin-top:0">{rich(t["cta"])}</div></div></div>',
            note,
        ]))
    return s


# ---------------------------------------------------------------- 08

def ctas_doc():
    used = set()
    for _t, _d, items in ctas.CATEGORIES:
        for line, _w in items:
            used.update(placeholders(line))
    s = [cover("08", "50 دعوة<br>لاتخاذ إجراء", "دعوات طبيعية للتعليقات والحفظ والمشاركة والمتابعة والنقرات والعملاء والمجتمع.",
               [("50", "دعوة"), ("9", "أهداف"), ("0", "عبارات مزعجة")], kicker="الملحق 01")]
    s.append(flow("طريقة الاستخدام", [
        page_head("ابدأ هنا", "اختيار الدعوة المناسبة",
                  "الدعوة الجيدة لاتخاذ إجراء تبدو خطوة تالية طبيعية لا طلبًا. اختر دعوة واحدة لكل منشور حسب ما تريد أن يحققه."),
        table(["إذا كان منشورك…", "اطلب…", "الفئة"], [
            ["قائمة تحقق أو دليلًا أو مرجعًا", "الحفظ", "الحفظ"],
            ["رأيًا أو سؤالًا", "تعليقًا", "التعليقات"],
            ["مفيدًا لشخص محدد", "مشاركة", "المشاركة"],
            ["جزءًا من سلسلة أو موضوع مستمر", "متابعة", "المتابعة"],
            ["ملخصًا لشيء أطول", "نقرة", "الموقع"],
            ["عن عرضك", "زيارة أو رسالة", "المنتجات"],
            ["يقدّم موردًا مجانيًا", "بريدًا إلكترونيًا أو رسالة", "العملاء المحتملون"],
            ["عن التواصل والانتماء", "تعريفًا بالنفس أو مشاركة إنجاز", "المجتمع"],
        ], split=False, widths=["auto", "52mm", "34mm"]),
        h3("ثلاث قواعد"),
        bullets([
            "**دعوة واحدة لكل منشور.** الطلبات المتعددة تُضعف كل واحد منها.",
            "**لا تعد إلا بما ستفعله.** إذا قلت «اكتب كلمة وسأرسلها لك»، فرد على كل تعليق.",
            "**قلها بطريقتك.** عدّل الصياغة لتشبه صوتك — بالفصحى أو بلهجة جمهورك.",
        ]),
    ]))
    s.append(flow("دليل الخانات", [
        page_head("مرجع", "دليل الخانات", "بعض الدعوات تحتوي خانات تملؤها. استبدلها بتفاصيلك."),
        glossary_table(ctas.GLOSSARY, used),
        callout("نوّع دعواتك. استخدام الدعوة نفسها في كل منشور يجعل تجاهلها سهلًا — احتفظ بقائمة قصيرة من المفضّلة لكل هدف وبدّل بينها.", label="نصيحة"),
    ]))
    n = 0
    for ci, (title, desc, items) in enumerate(ctas.CATEGORIES, 1):
        rows = []
        for line, when in items:
            n += 1
            rows.append(f'<div class="cta"><div class="n">{n:02d}</div><div class="line">{rich(line)}</div><div class="when"><b>استخدمها في</b>{esc(when)}</div></div>')
        s.append(flow("50 دعوة لاتخاذ إجراء", [section_head(f"الهدف {ci:02d} · {len(items)} دعوات", title, desc, f"{ci:02d}"),
                                              '<div data-split="items">' + "".join(rows) + "</div>"], brk=(ci == 1)))
    return s


# ---------------------------------------------------------------- 09

def images_doc():
    used = set()
    for _t, items in image_prompts.CATEGORIES:
        for _title, text, _b, _tip in items:
            used.update(placeholders(text))
    s = [cover("09", "30 برومبت<br>للصور", "برومبتات مفصّلة لصور لافتة ومتسقة مع هويتك — لأي أداة توليد صور بالذكاء الاصطناعي.",
               [("30", "برومبت"), ("10", "أساليب بصرية"), ("أي", "أداة صور")], kicker="الملحق 02")]
    parts = ["العنصر", "المكان", "الإضاءة", "التكوين", "الأسلوب", "اللون", "المقاس"]
    s.append(flow("طريقة الاستخدام", [
        page_head("ابدأ هنا", "كيف تستخدم برومبتات الصور",
                  "تعمل هذه البرومبتات مع معظم أدوات توليد الصور، مثل ChatGPT وMidjourney وAdobe Firefly وIdeogram وأدوات الصور في Canva. استبدل الخانات، وولّد عدة نسخ، واختر الأفضل."),
        callout("أدوات الصور — وخاصة Midjourney — تفهم الإنجليزية أفضل بكثير من العربية، لذلك بقيت البرومبتات بالإنجليزية لتحصل على أفضل نتيجة. العنوان والاستخدام والنصيحة بالعربية، والخانات مشروحة في الصفحة التالية. وإن أردت، اطلب من ChatGPT ترجمة أي برومبت أو تعديله.", label="لماذا البرومبتات بالإنجليزية؟"),
        h3("تشريح برومبت الصورة الجيد"),
        '<div class="formula">' + '<span class="plus">+</span>'.join(f'<span class="term">{x}</span>' for x in parts) + "</div>",
        table(["النصيحة", "لماذا تهم"], [
            ["<strong>أضف النص لاحقًا</strong>", "أدوات الصور كثيرًا ما تشوّه الكلمات — والحروف العربية خصوصًا. ولّد الصورة دون نص وأضف عنوانك في Canva."],
            ["<strong>اطلب مساحة فارغة</strong>", "عبارة «space on the right for text» تمنحك مكانًا لعنوانك. في التصاميم العربية قد تفضّل «space on the left»."],
            ["<strong>حدّد المقاس</strong>", "في Midjourney استخدم ‎«--ar 4:5». والأدوات الأخرى تقبل عادةً «vertical 4:5 format» داخل البرومبت."],
            ["<strong>ولّد ثم حسّن</strong>", "غيّر شيئًا واحدًا في كل مرة: الإضاءة أو الزاوية أو اللون، حتى تصل إلى ما تريد."],
            ["<strong>حافظ على الاتساق</strong>", "أعد استخدام كلمات [STYLE] و[COLOR] نفسها لتبدو صورك كعلامة واحدة."],
        ], split=False, widths=["44mm", "auto"]),
        callout("راجع شروط أداة الصور التي تستخدمها، خاصة للاستخدام التجاري. لا تولّد صورًا لأشخاص حقيقيين أو شعارات أو علامات تجارية أو أسلوب فنان بعينه، واتبع قواعد كل منصة في الإفصاح عن الصور المولّدة بالذكاء الاصطناعي.", label="استخدم بمسؤولية"),
    ]))
    s.append(flow("دليل الخانات", [
        page_head("مرجع", "دليل الخانات", "اكتب ما يناسبك بالإنجليزية في كل خانة لتتطابق كل صورة مع هويتك."),
        glossary_table(image_prompts.GLOSSARY, used),
    ]))
    n = 0
    blocks = []
    for ci, (title, items) in enumerate(image_prompts.CATEGORIES, 1):
        blocks.append(f'<div class="kwn" style="margin:{"0" if ci == 1 else "3mm"} 0 3mm"><div class="eyebrow" style="margin-bottom:1mm">الفئة {ci:02d}</div><h2 class="h" style="margin:0">{esc(title)}</h2></div>')
        for ptitle, text, best, tip in items:
            n += 1
            tip_html = f"<div><b>نصيحة</b>{rich(tip)}</div>" if tip else "<div></div>"
            blocks.append(f'<div class="icard"><div class="top"><span class="n">{n:02d}</span><span class="title">{esc(ptitle)}</span></div>'
                          f'<div class="body en">{rich(text)}</div><div class="foot"><div><b>مناسب لـ</b>{esc(best)}</div>{tip_html}</div></div>')
    s.append(flow("30 برومبت للصور", blocks))
    return s
