"""File 01 — Quick Start Guide. One flow section per printed page."""

from refs import pref, ref
from lib import (BRAND, bullets, callout, card, checklist, full, flow, h2, h3, p, page_head, rich, table, esc)


def cover():
    return full(
        """
<div class="grid-lines"></div><div class="glow"></div>
<div class="topline" style="position:relative"><span class="b">Quick Start Guide</span><span>File 01 / 10</span></div>
<div class="bignum">01</div>
<div class="main">
  <div class="kicker">The complete toolkit</div>
  <h1>AI CONTENT CREATOR<br><span class="soft">STARTER KIT</span></h1>
  <div class="tagline">Create<span>.</span> Plan<span>.</span> Publish<span>.</span> Grow<span>.</span></div>
  <div class="sub">30 days of practical AI-powered content creation.</div>
  <div class="rule"></div>
  <div class="stats">
    <div class="stat"><div class="v">100</div><div class="l">AI prompts</div></div>
    <div class="stat"><div class="v">100</div><div class="l">Content ideas</div></div>
    <div class="stat"><div class="v">50</div><div class="l">Hooks</div></div>
    <div class="stat"><div class="v">30</div><div class="l">Day calendar</div></div>
  </div>
</div>
<div class="bottom"><span>10 files · Beginner friendly</span><span>Start in under an hour</span></div>
""",
        "cover hero",
    )


def welcome():
    return flow("Welcome", [
        page_head("Welcome", "You don’t need more ideas. You need a system.",
                  "This kit gives you a simple, repeatable way to plan, create and publish social media content with AI — so you can stop staring at a blank screen and start showing up consistently."),
        p("Most people don’t struggle with content because they lack talent. They struggle because every post starts from zero: what should I say, how should I say it, and where does it fit? AI can help with all three — but only when you give it clear direction."),
        p("That’s what this toolkit is for. It combines **ready-to-use prompts**, **proven content structures** and a **30-day plan**, so AI does the heavy lifting and you add what only you can: your experience, your opinions and your voice."),
        h2("What this kit will help you do"),
        bullets([
            "Understand where AI fits into content creation — and where it doesn’t.",
            "Generate specific content ideas for your niche in minutes.",
            "Write posts, captions, hooks and short-video scripts faster.",
            "Follow a realistic 30-day plan without needing a strategy degree.",
            "Turn one idea into several pieces of content for different platforms.",
            "Publish consistently, review what works and keep improving.",
        ]),
        callout("Read this guide once (about 30 minutes). Then keep the prompts, hooks and calendar open while you work. You don’t need to use everything — pick what fits and come back for the rest.", label="How to use this guide"),
        '<div class="big-quote">AI gives you a first draft.<br>You make it worth reading.</div>',
    ])


def what_you_get():
    items = [
        ("01", "Quick Start Guide", "The system behind everything: workflow, prompting, pillars, hooks and your action plan."),
        ("02", "100 AI Prompts", "Copy-ready prompts for ideas, posts, Reels, TikTok, LinkedIn, captions, stories and repurposing."),
        ("03", "100 Content Ideas", "Adaptable ideas across 8 categories, each with a format and a suggested CTA."),
        ("04", "50 Powerful Hooks", "Fill-in-the-blank opening lines in 8 styles, each with a worked example."),
        ("05", "30-Day Content Calendar", "A balanced month of content, with links to the exact prompt, idea or template to use."),
        ("06", "Social Media Templates", "15 slide-by-slide templates you can recreate in Canva in minutes."),
        ("07", "Publishing Checklist", "Before- and after-publishing checks, plus a weekly review routine."),
        ("08", "Bonus · 50 CTAs", "Natural calls to action for comments, saves, shares, follows, leads and sales."),
        ("09", "Bonus · 30 AI Image Prompts", "Detailed prompts for on-brand visuals across 10 visual categories."),
        ("10", "Bonus · Content Repurposing System", "Turn one core idea into 16 pieces of content, step by step."),
    ]
    cards = "".join(card(t, d, tag="File " + n) for n, t, d in items)
    return flow("What You Will Get", [
        page_head("Inside the kit", "What you will get",
                  "Ten files that work together. The guide explains the system; the other files give you the tools to run it every day."),
        f'<div class="grid-2">{cards}</div>',
        callout("**Start with:** this guide → the 30-day calendar (File 05) → the prompts it links to (File 02). Everything else is there when you need it."),
    ])


def ai_workflow():
    steps = [
        ("IDEA", "Decide what this piece of content is about and who it’s for. One idea, one audience, one point. Use File 03 when you’re stuck.", False),
        ("PROMPT", "Turn the idea into clear instructions for AI: role, context, audience, goal, format and tone. File 02 gives you 100 ready-made prompts.", True),
        ("AI GENERATION", "Let AI produce options — several hooks, an outline, a script or a draft caption. Ask for more than you need and pick the best.", True),
        ("EDIT", "Make it yours. Check facts, add your experience, cut generic lines and adjust the tone until it sounds like you.", False),
        ("DESIGN", "Create the visual: carousel slides, a Reel, a photo or a graphic. File 06 and File 09 help here.", False),
        ("PUBLISH", "Post at a time that fits your routine, with a clear caption and one call to action. Use File 07 before you hit publish.", False),
        ("ANALYZE", "After a few days, look at what people saved, shared and commented on. Do more of what works.", False),
    ]
    html = '<div class="flow-steps">' + "".join(
        f'<div class="flow-step{" hl" if hl else ""}"><div class="dot">{i:02d}</div><div><h4>{t}</h4><p>{rich(d)}</p></div></div>'
        for i, (t, d, hl) in enumerate(steps, 1)) + "</div>"
    return flow("How AI Fits In", [
        page_head("The workflow", "How AI fits into content creation",
                  "AI is a powerful assistant in the middle of the process. You still own the beginning (the idea) and the end (the edit, the publishing and the learning)."),
        html,
        callout("The highlighted steps are where AI helps most. The rest is where your judgment makes the difference between content that’s generic and content that’s worth following.", label="Notice"),
    ])


def five_step_system():
    rows = [
        ("Step 1", "Define your audience", "Be specific about who you’re talking to and what they’re struggling with.",
         "Not “people who want to get fit” but “busy parents who want 20-minute home workouts”."),
        ("Step 2", "Choose your content pillar", "Pick which kind of value this post delivers: education, inspiration, personal story, engagement or promotion.",
         "This week: two educational posts, one personal story, one engagement post, one soft promotion."),
        ("Step 3", "Generate ideas", "Use AI to brainstorm many ideas, then keep the most specific and useful ones.",
         f"{pref('Generate Content Ideas')} gives you 20 ideas in one go. Keep the 5 you’d genuinely want to read."),
        ("Step 4", "Create the content", "Write with AI, edit with your voice and design with a template.",
         f"{pref('7-Slide Educational Carousel')} drafts a 7-slide carousel; {ref('template', 'Educational Carousel')} in File 06 shows how to lay it out."),
        ("Step 5", "Publish and improve", "Post consistently, review what worked each week and adjust.",
         "Your myth-busting carousel got twice the saves? Plan another one next week."),
    ]
    blocks = [page_head("The system", "The 5-step content system",
                        "Every piece of content in this kit follows the same five steps. Once they become a habit, creating content stops feeling like a guessing game.")]
    for n, t, d, ex in rows:
        blocks.append(
            f'<div class="plan-step"><div class="when">{n}</div><div><h4>{esc(t)}</h4><p>{rich(d)}</p>'
            f'<p class="small" style="margin-top:1.4mm"><strong class="accent">Example:</strong> {rich(ex)}</p></div></div>')
    return flow("The 5-Step Content System", blocks)


def better_prompts():
    elements = [
        ("Context", "What’s the situation? Your business, your niche, what you’ve already tried."),
        ("Role", "Who should AI act as? A strategist, a copywriter, a teacher, an editor."),
        ("Audience", "Who will read or watch this? Age, situation, level of knowledge."),
        ("Objective", "What should the content achieve? Saves, comments, clicks, trust."),
        ("Format", "What exactly do you want back? 7 slides, a 30-second script, 3 caption options."),
        ("Tone", "How should it sound? Friendly, direct, calm, playful, expert."),
        ("Constraints", "Limits that keep it useful: word counts, things to avoid, required elements."),
    ]
    grid = '<div class="grid-2">' + "".join(
        f'<div class="card soft"><span class="tag">{i:02d}</span><h4>{t}</h4><p>{rich(d)}</p></div>' for i, (t, d) in enumerate(elements, 1)) + (
        '<div class="card dark"><span class="tag">Rule of thumb</span><h4>Not every time</h4><p>You won’t need all seven for every prompt. '
        'Role, audience and format alone already make a big difference.</p></div>') + "</div>"
    compare = (
        '<div class="compare">'
        '<div class="side bad"><div class="label">✕ Bad prompt</div>“Give me an Instagram post.”'
        '<div class="why">No audience, no goal, no format. AI has to guess — so you get something generic.</div></div>'
        '<div class="side good"><div class="label">✓ Better prompt</div>“You are a social media strategist. Create an Instagram carousel for a small coffee shop targeting students aged 18–25. The goal is to increase engagement. Use a friendly and energetic tone. Give me a 7-slide structure with a strong hook and a clear CTA.”'
        '<div class="why">Role, audience, goal, tone and format are all defined. The result is usable on the first try.</div></div>'
        "</div>"
    )
    return flow("Better AI Prompts", [
        page_head("Prompting", "How to write better AI prompts",
                  "AI isn’t a mind reader. The quality of what you get back depends almost entirely on the quality of what you put in. Seven elements make the difference."),
        grid, compare,
    ])


def prompt_formula():
    terms = ["ROLE", "CONTEXT", "AUDIENCE", "GOAL", "FORMAT", "TONE", "CONSTRAINTS"]
    bar = '<div class="formula">' + '<span class="plus">+</span>'.join(f'<span class="term">{t}</span>' for t in terms) + "</div>"
    rows = [
        ["<strong>Role</strong>", "Who AI should be", "“You are a content strategist for wellness brands.”"],
        ["<strong>Context</strong>", "Background AI needs", "“I run a small yoga studio and post on Instagram three times a week.”"],
        ["<strong>Audience</strong>", "Who it’s for", "“Office workers aged 25–40 with back pain.”"],
        ["<strong>Goal</strong>", "What success looks like", "“I want people to save the post and visit my profile.”"],
        ["<strong>Format</strong>", "The exact output", "“A 6-slide carousel with a headline and up to 20 words per slide.”"],
        ["<strong>Tone</strong>", "How it should sound", "“Calm, encouraging and practical.”"],
        ["<strong>Constraints</strong>", "Rules and limits", "“No medical claims. No jargon. End with a question.”"],
    ]
    template = ("You are a [ROLE]. [CONTEXT]. Create [FORMAT] for [AUDIENCE]. "
                "The goal is to [GOAL]. Use a [TONE] tone. [CONSTRAINTS].")
    return flow("The Prompt Formula", [
        page_head("Prompting", "The prompt formula",
                  "Use this formula whenever you write your own prompt. You don’t need every element every time — but the more you include, the less you’ll need to edit."),
        bar,
        table(["Element", "Purpose", "Example"], rows, split=False, widths=["26mm", "40mm", "auto"]),
        h3("Reusable template"),
        f'<div class="pcard"><div class="body"><span class="lbl">Copy and fill in</span>{rich(template)}</div></div>',
        callout("**Follow-up prompts matter too.** If the first answer isn’t right, don’t start over. Reply with “Make it shorter”, “Make the hook more specific”, “Use simpler words” or “Give me 5 more options”.", label="Pro tip"),
    ])


def pillars():
    data = [
        ("Educational", "Teach something useful.", "How-to carousels, tutorials, tips, myth-busting, explainers."),
        ("Entertaining", "Make people smile or relate.", "Relatable situations, light humor, POV videos, trends adapted to your niche."),
        ("Inspirational", "Encourage and motivate — with substance.", "Progress stories, transformations, lessons from setbacks."),
        ("Personal", "Let people know the person behind the account.", "Your story, your workspace, your opinions, your bad days."),
        ("Promotional", "Present your offer clearly.", "Product introductions, testimonials, FAQs, launch announcements."),
        ("Community / Engagement", "Start conversations and involve your audience.", "Polls, questions, “this or that”, community spotlights."),
    ]
    cards = "".join(card(t, f'<p><strong>{esc(a)}</strong></p><p>{esc(b)}</p>', tag=f"Pillar {i:02d}") for i, (t, a, b) in enumerate(data, 1))
    return flow("Content Pillars", [
        page_head("Strategy", "Content pillars",
                  "Content pillars are the 3–6 recurring types of content your account is built on. They keep your feed balanced and make planning much easier."),
        f'<div class="grid-2">{cards}</div>',
        callout("**A healthy starting mix:** mostly educational and personal content, a regular dose of engagement, and promotion in roughly one post out of every five. Adjust once you see what your audience responds to.", label="Suggested balance"),
    ])


def platforms():
    rows = [
        ["<strong>Instagram</strong>", "Carousels, Reels, Stories, photo posts", "Visual brands, educators, creators, local businesses", "Carousels for saves; Stories for daily connection."],
        ["<strong>TikTok</strong>", "Short vertical video, replies, series", "Personal brands, entertainers, educators with personality", "Casual, native-feeling video works better than polished ads."],
        ["<strong>LinkedIn</strong>", "Text posts, document carousels, short video", "B2B, freelancers, consultants, professionals", "Lessons, opinions and case studies from your work."],
        ["<strong>Facebook</strong>", "Posts, groups, events, short video", "Local businesses, communities, older audiences", "Groups and events are useful for community building."],
        ["<strong>YouTube</strong>", "Long-form video, Shorts", "Teachers, reviewers, in-depth creators", "Searchable content that keeps being found for longer."],
    ]
    return flow("Choosing Your Platform", [
        page_head("Strategy", "Choosing your platform",
                  "You don’t need to be everywhere. Start with one main platform where your audience already spends time, and add a second one once posting feels routine."),
        table(["Platform", "Formats that feel natural", "Often a good fit for", "What tends to work"], rows, split=False, widths=["25mm", "40mm", "47mm", "auto"]),
        h3("How to choose"),
        bullets([
            "**Where is your audience already?** Ask a few customers or look at where people in your niche are active.",
            "**What can you create comfortably?** If you hate being on camera, start with carousels or text posts.",
            "**How much time do you have?** One platform done well beats three done badly.",
        ]),
        callout("Platforms change their features and recommendations often. Rather than chasing rules about “the algorithm”, focus on what you can control: useful content, clear hooks, consistency and genuine conversations.", label="A note on algorithms"),
    ])


def hooks():
    structures = [
        ("Curiosity", "Nobody tells you this about [TOPIC]…"),
        ("Problem", "Struggling to [GOAL]? Start here."),
        ("Mistake", "Stop doing [X] if you want [RESULT]."),
        ("Story", "I wish I knew this when I started [ACTIVITY]."),
        ("List", "[NUMBER] mistakes beginners make when [ACTIVITY]."),
        ("Contrarian", "Unpopular opinion: [COMMON ADVICE] is overrated."),
    ]
    rows = [[f"<strong>{t}</strong>", rich(h)] for t, h in structures]
    return flow("Hooks", [
        page_head("Writing", "Hooks: why the first sentence matters",
                  "Your hook is the first line of a caption, the first slide of a carousel or the first two seconds of a video. If it doesn’t give people a reason to stay, the rest of the content never gets seen."),
        h3("A strong hook is…"),
        bullets([
            "**Specific** — “3 pricing mistakes freelancers make” beats “Some business tips”.",
            "**Relevant** — your audience instantly knows it’s for them.",
            "**Honest** — it promises something the content actually delivers.",
            "**Short** — usually under 12 words, readable in a glance.",
        ]),
        h3("Six hook structures to start with"),
        table(["Type", "Template"], rows, split=False, widths=["32mm", "auto"]),
        callout(f"Write 5–10 hooks for every important post and choose the best one. {pref('10 Hook Variations')} does this for you, and File 04 gives you 50 templates with examples.", label="Habit to build"),
    ])


def ctas():
    rows = [
        ["Comments", "Start a conversation", "“What would you add to this list?”"],
        ["Saves", "Useful reference content", "“Save this for your next planning session.”"],
        ["Shares", "Content that helps others", "“Send this to someone who’s just starting.”"],
        ["Follows", "Series and ongoing value", "“This is part 1 — follow for part 2.”"],
        ["Clicks", "Products, guides, sign-ups", "“The full checklist is free — link in bio.”"],
    ]
    return flow("Calls to Action", [
        page_head("Writing", "Calls to action",
                  "A call to action (CTA) tells people what to do next. Without one, even great content leaves readers with nowhere to go."),
        h3("When to use which CTA"),
        table(["Goal", "Best for", "Example"], [[f"<strong>{a}</strong>", b, c] for a, b, c in rows], split=False, widths=["26mm", "50mm", "auto"]),
        h3("Three rules for natural CTAs"),
        bullets([
            "**One CTA per post.** Asking people to like, comment, share, save and click all at once means they’ll do none of them.",
            "**Match the CTA to the content.** A checklist asks for a save; an opinion asks for a comment; a tutorial invites people to try it.",
            "**Make it easy.** “What’s your biggest challenge with pricing?” is easier to answer than “Thoughts?”.",
        ]),
        callout("File 08 contains 50 ready-to-use CTAs, organized by goal.", label="More CTAs"),
    ])


def human_editing():
    items = [
        ("Fact-check", "AI can state wrong information confidently. Verify numbers, claims, dates and anything health-, money- or law-related."),
        ("Tone", "Read it out loud. Would you actually say this? Replace stiff phrases with the words you naturally use."),
        ("Originality", "Remove clichés and filler (“In today’s fast-paced world…”). If a line could appear on anyone’s account, rewrite it."),
        ("Personal experience", "Add one real example, story, mistake or result. This is what AI can’t provide — and what people remember."),
        ("Brand voice", "Keep your words, emoji use, sentence length and formatting consistent across posts."),
        ("Grammar", "Check spelling, punctuation and readability. Short sentences and line breaks make posts easier to read on a phone."),
    ]
    grid = '<div class="grid-2">' + "".join(card(t, d, tag=f"Check {i:02d}") for i, (t, d) in enumerate(items, 1)) + "</div>"
    return flow("AI + Human Editing", [
        page_head("Quality", "AI + human editing",
                  "AI-generated content is a starting point, not a finished product. A few minutes of editing turns a generic draft into something that sounds like you and earns trust."),
        grid,
        '<div class="compare"><div class="side bad"><div class="label">✕ Raw AI draft</div>“Consistency is key to success on social media. By posting regularly, you can unlock your full potential and grow your audience.”</div>'
        '<div class="side good"><div class="label">✓ Edited by a human</div>“I posted 3 times a week for 2 months before anything changed. What finally worked wasn’t posting more — it was posting the same type of carousel every Tuesday.”</div></div>',
        p("Be open about using AI where it matters to your audience, and follow each platform’s rules on AI-generated or altered media.", "small"),
    ])


def faster():
    chain = ('<div class="chain"><span class="node hl">One idea</span><span class="arrow">→</span><span class="node">Reel</span><span class="arrow">→</span>'
             '<span class="node">Carousel</span><span class="arrow">→</span><span class="node">Story</span><span class="arrow">→</span><span class="node">LinkedIn post</span>'
             '<span class="arrow">→</span><span class="node">Short video</span><span class="arrow">→</span><span class="node">Newsletter</span></div>')
    rows = [
        ["Reel", "Talk through the 3 mistakes in 30 seconds, one per cut.", pref("Common Mistake Reel")],
        ["Carousel", "One mistake per slide, each with its fix.", pref("Mistakes Carousel")],
        ["Story", "Poll: “Which mistake have you made?” Reveal the fixes the next day.", pref("Interactive Story Sequence")],
        ["LinkedIn post", "The story of when you made mistake #2 and what it cost.", pref("Lesson-Learned Post")],
        ["Short video", "Reply to a comment asking about mistake #3.", pref("Reply-to-Comment Video")],
        ["Newsletter", "All three mistakes, with a deeper fix and a resource.", pref("Weekly Newsletter from Posts")],
    ]
    return flow("Creating Content Faster", [
        page_head("Efficiency", "Creating content faster",
                  "The fastest creators don’t come up with more ideas. They get more out of each idea. One well-researched topic can fill a week of content across formats."),
        chain,
        h3("Example: “3 pricing mistakes new freelancers make”"),
        table(["Format", "How the idea is adapted", "Use"], rows, split=False, widths=["32mm", "auto", "26mm"]),
        callout(f"**Adapt, don’t copy-paste.** Each format has its own rhythm: a Reel is spoken, a carousel is visual, a LinkedIn post is reflective. AI is excellent at this kind of rewriting — see the repurposing prompts ({pref('Article to Carousel')[7:]}–{pref('Content Atomizer')[7:]}) and File 10.", label="The rule"),
    ])


def thirty_day():
    return flow("The 30-Day System", [
        page_head("Your plan", "The 30-day system",
                  "File 05 gives you a complete month of content. Each day tells you what to post, in which format, why, and which prompt or template to use."),
        h3("How the month is structured"),
        table(["Week", "Focus", "What you’ll post"], [
            ["<strong>Week 1</strong>", "Introduce yourself", "Who you are, beginner-friendly education, your first Stories poll."],
            ["<strong>Week 2</strong>", "Build trust", "Tutorials, behind the scenes, answering real questions."],
            ["<strong>Week 3</strong>", "Show your expertise", "Frameworks, opinions, a transformation and your first soft promotion."],
            ["<strong>Week 4</strong>", "Convert and connect", "Proof, an FAQ about your offer, a checklist and a quiz."],
            ["<strong>Days 29–30</strong>", "Repurpose and reflect", "Remake your best post and share what you learned."],
        ], split=False, widths=["28mm", "40mm", "auto"]),
        h3("How to use it"),
        bullets([
            "**Fill in the “Set up your month” page first.** Your niche, audience and offer make every prompt sharper.",
            "**Batch your work.** Create 3–4 posts in one session instead of starting from scratch every day.",
            "**Swap freely.** If a day doesn’t fit your business, replace it with an idea from the same pillar in File 03.",
            "**Missed a day?** Don’t try to catch up. Skip it and continue with the next one.",
            "**Days 7, 14, 21 and 28 are lighter on purpose.** Use them to review, reply and rest.",
        ]),
        callout("You don’t need to post every single day to benefit from this calendar. Posting 3–4 times a week and following the order still gives you a balanced, intentional month.", label="Realistic expectations"),
    ])


def weekly_workflow():
    days = [
        ("Monday", "Create", "Batch-create the posts for Tuesday to Thursday. Generate drafts with AI, edit them and design the visuals."),
        ("Tuesday", "Publish", "Finalize and schedule or post. Reply to comments in the first hours after posting."),
        ("Wednesday", "Engage", "Spend 20–30 minutes commenting thoughtfully on accounts in your niche and answering messages."),
        ("Thursday", "Create", "Batch-create the posts for Friday to Monday. Use the prompts linked in your calendar."),
        ("Friday", "Publish", "Publish, reply and save any questions you receive — they’re next week’s ideas."),
        ("Weekend", "Analyze / Repurpose", "Run the weekly review in File 07. Pick your best post and plan how to repurpose it."),
    ]
    html = "<div>" + "".join(f'<div class="week"><div class="d">{d}</div><div class="a"><strong>{a}</strong><p>{rich(t)}</p></div></div>' for d, a, t in days) + "</div>"
    return flow("Weekly Workflow", [
        page_head("Your routine", "A simple weekly workflow",
                  "Consistency comes from routine, not motivation. This rhythm separates creating, publishing and engaging, so each task gets your full attention."),
        html,
        callout("Your posts can still go out every day — you create them in two batches and schedule them. Most platforms and many free tools let you schedule posts in advance.", label="How daily posting fits"),
        p("Time budget: around 2 hours per creation session, 15 minutes on publishing days and 20–30 minutes for engagement. Adjust to your life — a routine you can keep beats an ambitious one you abandon.", "small"),
    ])


def quality_checklist():
    return flow("Content Quality Checklist", [
        page_head("Quality", "Content quality checklist",
                  "Run through these questions before you design or publish anything. If you can answer “yes” to all of them, the post is ready."),
        checklist([
            ("Is it for one specific audience?", "You could name the person this post is written for."),
            ("Does it make one clear point?", "If you can’t summarize it in one sentence, split it into two posts."),
            ("Does the hook earn attention honestly?", "Specific, relevant and delivered on by the content."),
            ("Is it useful, relatable or interesting?", "Your audience gets something: a lesson, a laugh, a feeling or a decision."),
            ("Have you added something only you could add?", "A personal example, opinion, result or story."),
            ("Are the facts correct?", "Every number, claim and recommendation checked."),
            ("Does it sound like you?", "Read it out loud. Remove anything you wouldn’t say."),
            ("Is it easy to read on a phone?", "Short sentences, line breaks, large text on visuals."),
            ("Is there one clear call to action?", "Matched to the goal of the post."),
            ("Does it fit your pillars and your brand?", "Consistent colors, fonts, tone and topics."),
        ]),
    ])


def mistakes():
    data = [
        ("Writing for everyone", "Content aimed at everyone resonates with no one. Pick one audience and speak directly to them."),
        ("No clear audience", "If you don’t know who you’re helping, AI won’t either. Define your audience before you prompt."),
        ("Weak hooks", "A great post with a vague first line rarely gets seen. Write several hooks and choose the strongest."),
        ("Too much promotion", "If every post is an advert, people stop paying attention. Lead with value; promote occasionally."),
        ("No call to action", "People rarely take action unless invited. End every post with one clear next step."),
        ("Copying AI output without editing", "Unedited AI text sounds generic and can contain errors. Always fact-check and personalize."),
        ("Posting without a strategy", "Random posts are hard to build on. Use pillars and the calendar so each post has a purpose."),
        ("Giving up too early", "Most accounts grow slowly at first. Judge your progress over months, not days."),
    ]
    html = "<div>" + "".join(f'<div class="mistake"><div class="x">✕</div><div><strong>{esc(t)}</strong><p>{esc(d)}</p></div></div>' for t, d in data) + "</div>"
    return flow("Mistakes to Avoid", [
        page_head("Avoid these", "Mistakes to avoid",
                  "Almost every beginner makes some of these. Knowing them in advance saves you weeks of frustration."),
        html,
    ])


def action_plan():
    steps = [
        ("Today", "Choose your niche", "Write one sentence: “I help [TARGET AUDIENCE] with [RESULT].” Complete the “Set up your month” page in File 05."),
        ("Tomorrow", "Create your first 3 ideas", f"Run {pref('Generate Content Ideas')} with your niche and audience. Choose the three ideas you’d most like to read yourself."),
        ("Day 3", "Create your first post", "Pick one idea, use the matching template from File 06, write the hook with File 04, edit, and publish."),
        ("Day 4+", "Follow the 30-day calendar", "One day at a time. Review every weekend with the checklist in File 07."),
    ]
    html = "<div>" + "".join(f'<div class="plan-step"><div class="when">{w}</div><div><h4>{esc(t)}</h4><p>{rich(d)}</p></div></div>' for w, t, d in steps) + "</div>"
    return flow("Final Action Plan", [
        page_head("Start now", "Your final action plan",
                  "Reading about content doesn’t create content. Here’s exactly what to do over the next few days."),
        html,
        '<div class="spacer"></div>',
        callout("Your first posts won’t be perfect, and they don’t need to be. Every post you publish teaches you something the next one can use. Start small, stay consistent and let the system do the heavy lifting.", label="One last thing", dark=True),
        p(f"Thank you for choosing the {BRAND}. Now go create something.", "small"),
    ])


def build():
    return [
        cover(), welcome(), what_you_get(), ai_workflow(), five_step_system(), better_prompts(), prompt_formula(),
        pillars(), platforms(), hooks(), ctas(), human_editing(), faster(), thirty_day(), weekly_workflow(),
        quality_checklist(), mistakes(), action_plan(),
    ]
