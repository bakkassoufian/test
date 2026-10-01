"""Files 07 (Publishing Checklist) and 10 (Content Repurposing System)."""

from lib import (callout, card, checklist, doc_cover, flow, h2, h3, p, page_head, rich, table, bullets, esc, write_lines)
from refs import pref, ref


# ---------------------------------------------------------------- File 07

def checklist_doc():
    s = [doc_cover("07", "Publishing<br>Checklist", "Check every post before it goes out — and learn from every post after it does.",
                   [("3", "Checklists"), ("1", "Weekly review"), ("5 min", "Per post")], kicker="Quality control")]

    s.append(flow("How to Use", [
        page_head("Start here", "How to use this checklist",
                  "Good content is often let down by small things: a typo in the first line, a missing call to action, a cropped graphic. Two minutes with this checklist catches them."),
        h3("Three checklists, three moments"),
        '<div class="grid-3">'
        + card("Before publishing", "A final quality check on every post. Takes 2–3 minutes once it becomes a habit.", tag="Every post")
        + card("After publishing", "What to do in the hours and days after a post goes live.", tag="Every post")
        + card("Weekly review", "A 20-minute routine to learn what’s working and plan what’s next.", tag="Once a week")
        + "</div>",
        h3("Ways to use it"),
        bullets([
            "**Print it** and keep it next to your desk.",
            "**Copy the checklists** into your notes app or project tool as a reusable template.",
            "**Pin the “Before publishing” list** next to your scheduling tool so you see it every time.",
        ]),
        callout("You don’t need to be perfect. If a post passes the “Before publishing” checklist, it’s ready — publish it and move on.", label="Remember"),
    ]))

    s.append(flow("Before Publishing", [
        page_head("Every post", "Before publishing", "Work from top to bottom. If you can’t tick an item, fix it before you post."),
        h3("Message"),
        checklist([
            ("Strong hook", "The first line, slide or two seconds gives a clear reason to keep reading or watching."),
            ("Clear message", "The post makes one main point that you could summarize in one sentence."),
            ("Target audience identified", "You know exactly who this is for, and the wording speaks to them."),
        ]),
        h3("Visual & caption"),
        checklist([
            ("Visual reviewed", "Text is readable on a phone, nothing important is cropped and the design is consistent."),
            ("Caption reviewed", "It adds context, sounds like you and uses line breaks for easy reading."),
            ("CTA included", "One clear next step that matches the goal of the post."),
        ]),
        h3("Accuracy & brand"),
        checklist([
            ("Spelling checked", "Read it once more, slowly — or out loud. Check names and handles especially."),
            ("Facts checked", "Every number, claim and recommendation verified, particularly anything AI generated."),
            ("Brand consistency checked", "Your colors, fonts, tone of voice and topics match the rest of your content."),
        ]),
    ]))

    s.append(flow("Before Publishing", [
        page_head("Every post", "Final technical checks", "Quick checks that prevent the most common avoidable problems."),
        checklist([
            ("Correct size and format", "Portrait 4:5 for feed posts, 9:16 for Stories, Reels and TikTok. See the reference table below."),
            ("Text inside the safe area", "On vertical video, keep important text away from the top and bottom edges, where buttons and captions appear."),
            ("Alt text added where available", "A short description of the image helps people using screen readers."),
            ("Links tested", "Any link in your bio, Story or caption opens the right page."),
            ("Tags and mentions correct", "You have permission to feature anyone you tag, show or quote."),
            ("Keywords and hashtags relevant", "A few specific, relevant terms — not a long list of unrelated ones."),
            ("Posting time decided", "Scheduled or posted at a time when you can reply to early comments."),
        ]),
        h3("Common format reference"),
        table(["Platform / format", "Recommended size", "Ratio"], [
            ["Instagram feed post (portrait)", "1080 × 1350 px", "4:5"],
            ["Instagram square post", "1080 × 1080 px", "1:1"],
            ["Instagram Stories & Reels", "1080 × 1920 px", "9:16"],
            ["TikTok & YouTube Shorts", "1080 × 1920 px", "9:16"],
            ["LinkedIn image post", "1080 × 1080 or 1080 × 1350 px", "1:1 or 4:5"],
            ["YouTube thumbnail", "1280 × 720 px", "16:9"],
        ], split=False, widths=["auto", "60mm", "26mm"]),
        p("Platforms update their specifications from time to time. If something looks cropped after uploading, check the platform’s current guidance.", "small"),
    ]))

    s.append(flow("After Publishing", [
        page_head("Every post", "After publishing", "Publishing is the middle of the process, not the end. What you do next helps you build relationships and better content."),
        checklist([
            ("Reply to comments", "Answer thoughtfully, especially in the first few hours. Ask a follow-up question where it feels natural."),
            ("Save useful feedback", "Copy questions, objections and kind words into a note. They’re future content ideas and testimonials."),
            ("Review engagement", "After 2–3 days, note saves, shares, comments and profile visits — not just likes."),
            ("Identify what worked", "Was it the topic, the hook, the format or the timing? Write one sentence about why."),
            ("Repurpose strong content", "Add your best posts to a “repurpose” list and give them a second life in a new format."),
        ]),
        h3("Signals worth paying attention to"),
        table(["Signal", "What it usually tells you"], [
            ["<strong>Saves</strong>", "The content is useful enough to come back to."],
            ["<strong>Shares and sends</strong>", "People think it will help or speak to someone they know."],
            ["<strong>Comments</strong>", "The topic started a conversation or touched a nerve."],
            ["<strong>Profile visits & follows</strong>", "The post made people curious about you."],
            ["<strong>Link clicks & messages</strong>", "Interest in going further — your offer, your guide, your services."],
        ], split=False, widths=["50mm", "auto"]),
        callout("Compare your posts with each other, not with other accounts. Your own trends over a few weeks are far more useful than any single number.", label="Keep perspective"),
    ]))

    s.append(flow("Weekly Review", [
        page_head("Once a week", "Weekly review checklist", "Set aside 20 minutes at the end of each week. This is where the real improvement happens."),
        checklist([
            ("List everything you published this week", "Use the worksheet on the next page."),
            ("Find your top post", "The one with the most saves, shares or meaningful comments."),
            ("Find your weakest post", "Look for a reason, not a judgment: topic, hook, format or timing?"),
            ("Note recurring questions", "What did people ask more than once? That’s next week’s content."),
            ("Check your pillar balance", "Mostly value, some personal, occasional promotion?"),
            ("Pick one post to repurpose", "Plan its new format using File 10."),
            ("Plan next week’s posts", "Check your calendar and swap any ideas that no longer fit."),
            ("Batch-create your first posts", "Draft at least two posts now, while ideas are fresh."),
        ]),
    ]))

    rows = [["", "", "", "", "", "", ""] for _ in range(8)]
    s.append(flow("Weekly Review", [
        page_head("Worksheet", "Weekly review worksheet", "Print a copy each week, or recreate it in a spreadsheet."),
        p("**Week of:** ______________________"),
        table(["Day", "Post / topic", "Format", "Pillar", "Saves", "Shares", "Comments"], rows, cls="t review-grid", split=False, widths=["14mm", "auto", "22mm", "24mm", "15mm", "15mm", "20mm"]),
        write_lines([
            ("What worked best this week, and why?", None, 2),
            ("What will I do differently next week?", None, 2),
            ("Which post will I repurpose, and into what format?", None, 1),
            ("Questions from my audience to answer next week:", None, 2),
        ]),
    ]))
    return s


# ---------------------------------------------------------------- File 10

STAGES = [
    ("Core idea", "1 content brief",
     "Choose one topic your audience genuinely cares about and develop it into a brief: the main message, supporting points, examples and hooks.",
     "Turns a vague topic into a structured plan, and suggests angles you might not have thought of.",
     "Pick an idea from real audience questions or your best-performing post. Add your own opinion to the brief.",
     ("R1", "Develop the Core Idea",
      "You are a content strategist. My niche is [NICHE] and my audience is [TARGET AUDIENCE]. My core idea is: [TOPIC]. Develop it into a content brief with: the main message in one sentence, 5 key points that support it, 3 realistic examples or scenarios, the most common objection or question, and 10 possible hooks. I will use this brief to create content for several platforms.")),
    ("Long-form article", "1 article (or video outline)",
     "Expand the brief into one in-depth piece: a blog post, a long caption series, a YouTube outline or a newsletter essay. This is the source everything else is cut from.",
     "Drafts a well-structured article from the brief in minutes.",
     "Add your personal story, real examples and opinions. Check every fact.",
     ("R2", "Write the Long-Form Piece",
      "Using this content brief: [PASTE CONTENT], write a 900–1,200 word article for [TARGET AUDIENCE]. Include a clear headline, a short introduction that names the problem, one section per key point with practical advice, and a conclusion with one next step. Where a personal example would help, leave a line that says “ADD MY STORY HERE”. Tone: [TONE].")),
    ("Short videos", "3 Reels, TikToks or Shorts",
     "Pull three key points from the article and turn each one into a short, standalone video.",
     "Finds the most “video-friendly” moments and writes hooks, scripts and on-screen text.",
     "Rewrite the script in your own spoken words before filming. Film all three in one session.",
     ("R3", "Extract 3 Short Videos",
      "Here is my article: [PASTE CONTENT]. Create 3 short video scripts of 30–45 seconds, each based on a different key point. For each script, give a hook under 10 words, the spoken script, on-screen text, and a closing call to action. Each video must make sense on its own.")),
    ("Instagram posts", "5 feed posts",
     "Create five feed posts in different formats so the same idea feels fresh: carousels, a quote, a checklist and a question.",
     "Turns the article into slide text and captions for each format.",
     "Design with the templates in File 06. Space the posts out over one to two weeks.",
     ("R4", "Create 5 Instagram Posts",
      "From this article: [PASTE CONTENT], create 5 Instagram posts in different formats: an educational carousel (7 slides), a mistakes or myth carousel, a quote graphic, a checklist post, and an engagement question post. For each, write the slide or graphic text and a caption under 150 words with one call to action.")),
    ("Stories", "5 Story frames",
     "Use Stories to start a conversation around the topic, test your audience’s knowledge and point them to your posts.",
     "Writes interactive frames with poll, quiz and question-sticker ideas.",
     "Film at least one frame of yourself talking — Stories are where people get to know you.",
     ("R5", "Plan 5 Story Frames",
      "Create 5 Instagram Story frames based on this idea: [TOPIC]. Frame 1: a question or poll that introduces the topic. Frames 2–3: two quick tips. Frame 4: a quiz or slider to test understanding. Frame 5: an invitation to see the full post. Give on-screen text under 15 words per frame and the sticker type to use.")),
    ("LinkedIn post", "1 professional post",
     "Reframe the idea for a professional audience: what you learned, what it means for their work, or a story from a client project.",
     "Shifts the tone and structure to suit LinkedIn while keeping your message.",
     "Lead with a real experience. LinkedIn readers respond to specific, first-hand insight.",
     ("R6", "Adapt for LinkedIn",
      "Turn this article into a LinkedIn post for [TARGET AUDIENCE]: [PASTE CONTENT]. Lead with a personal or professional insight rather than a summary, keep paragraphs to 1–2 sentences, include one concrete example, and end with a question. Maximum 220 words, no hashtags in the body.")),
    ("Email", "1 newsletter",
     "Send the most useful takeaway to your email list, with a personal note and one call to action.",
     "Drafts subject lines and a short, personal email from the article.",
     "Write the opening yourself. Email is the most personal channel you have.",
     ("R7", "Write the Newsletter",
      "Write a short email newsletter based on this article: [PASTE CONTENT]. Give me 5 subject line options, a friendly opening of 2–3 sentences, the single most useful takeaway explained in about 150 words, and one call to action to [GOAL]. Write it like a message to one person, not a broadcast.")),
]

REVIEW_PROMPT = ("R8", "Review and Plan the Next Round",
                 "Here are the results from the content I created around one idea: [PASTE CONTENT]. Identify which formats and angles performed best and suggest why. Then recommend which piece I should repurpose again next month, in what new format, and with what new angle.")


def rcard(code, title, text):
    return (f'<div class="pcard"><div class="top"><span class="n">{code}</span><span class="title">{esc(title)}</span><span class="use">Copy-ready prompt</span></div>'
            f'<div class="body">{rich(text)}</div></div>')


def repurpose_doc():
    s = [doc_cover("10", "Content<br>Repurposing System", "Turn one core idea into 16 pieces of content — with AI doing the heavy lifting at every stage.",
                   [("1", "Core idea"), ("16", "Pieces of content"), ("8", "Copy-ready prompts")], kicker="Bonus 03")]

    s.append(flow("Why Repurpose", [
        page_head("The principle", "Create less. Publish more.",
                  "Most of your audience won’t see every post you publish. Repurposing lets one strong idea reach more people, in the formats they prefer — without starting from scratch each time."),
        h3("Four rules for repurposing well"),
        '<div class="grid-2">'
        + card("Adapt, don’t duplicate", "Change the format, the length and the angle for each platform. The message stays; the packaging changes.", tag="Rule 01")
        + card("Start with depth", "A long-form piece gives you enough material to cut into many short ones. Short content rarely expands well.", tag="Rule 02")
        + card("Space it out", "Spread pieces of the same idea over one to two weeks. Repetition helps people remember you.", tag="Rule 03")
        + card("Keep a library", "Save your best ideas and their results. Good ideas can be repurposed again months later.", tag="Rule 04")
        + "</div>",
        callout("Repurposing isn’t lazy. It’s how you make sure your best thinking actually reaches the people it’s meant for.", label="Mindset"),
    ]))

    levels = [
        ("ONE CORE IDEA", "The topic, message and angle", "core"),
        ("1 long-form article", "Blog post, video outline or newsletter essay", "acc"),
        ("3 short videos", "Reels, TikToks or YouTube Shorts", ""),
        ("5 Instagram posts", "Carousels, quote, checklist, question", ""),
        ("5 Stories", "Poll, tips, quiz, link", ""),
        ("1 LinkedIn post", "A professional angle on the same idea", ""),
        ("1 email", "The most useful takeaway, sent personally", ""),
    ]
    cascade = '<div class="cascade">' + '<div class="ar">↓</div>'.join(
        f'<div class="lvl {c}">{esc(t)}<small>{esc(d)}</small></div>' for t, d, c in levels) + "</div>"
    s.append(flow("The System", [
        page_head("Overview", "The repurposing cascade", "One idea flows down into 16 pieces of content. Each stage uses the stage above it as its source material."),
        cascade,
        p("**1 brief + 1 article + 3 videos + 5 posts + 5 Stories + 1 LinkedIn post + 1 email = 16 pieces of content from a single idea.**", "small"),
    ]))

    stage_blocks = [page_head("Step by step", "The seven stages", "For each stage: what you create, how AI helps, the prompt to use and the human touch that makes it yours.")]
    for i, (name, output, what, ai, human, (code, ptitle, prompt)) in enumerate(STAGES, 1):
        stage_blocks.append(
            f'<div class="kwn" style="display:grid;grid-template-columns:18mm 1fr;gap:4mm;margin-top:3mm;margin-bottom:2mm">'
            f'<div class="stage-num">{i:02d}</div><div><div class="eyebrow" style="margin-bottom:1mm">{esc(output)}</div>'
            f'<h2 class="h" style="margin:0 0 1.6mm">{esc(name)}</h2><p style="margin:0">{rich(what)}</p></div></div>')
        stage_blocks.append(
            f'<div class="grid-2" style="margin-bottom:2.6mm"><div class="card soft"><span class="tag">How AI helps</span><p>{rich(ai)}</p></div>'
            f'<div class="card accent"><span class="tag">Human touch</span><p>{rich(human)}</p></div></div>')
        stage_blocks.append(rcard(code, ptitle, prompt))
    stage_blocks.append(h2("After the week: review"))
    stage_blocks.append(rcard(*REVIEW_PROMPT))
    stage_blocks.append(h3("A realistic schedule for one person"))
    stage_blocks.append(table(["When", "Task", "Time"], [
            ["Monday", "Run R1 and R2: brief and article. Edit and add your story.", "90 min"],
            ["Tuesday", "Run R3. Film all three short videos in one session.", "60 min"],
            ["Wednesday", "Run R4. Design the five posts in Canva using File 06.", "90 min"],
            ["Thursday", "Run R5–R7. Schedule the Stories, LinkedIn post and email.", "45 min"],
            ["Over the next 1–2 weeks", "Publish the pieces gradually, reply to comments.", "15 min/day"],
            ["End of the cycle", "Run R8 with your results. Choose the next core idea.", "20 min"],
        ], split=False, widths=["40mm", "auto", "24mm"]))
    s.append(flow("The Seven Stages", stage_blocks))

    example_rows = [
        ["Core idea", "How to price your first freelance project"],
        ["Article", "How to Price Your First Freelance Project (Without Undercharging)"],
        ["Video 1", "“Stop charging by the hour for your first project.”"],
        ["Video 2", "“The three numbers you need before you send a quote.”"],
        ["Video 3", "“What to say when a client says your price is too high.”"],
        ["Post 1", "Carousel: Pricing your first project in 5 steps"],
        ["Post 2", "Carousel: 4 pricing myths new freelancers believe"],
        ["Post 3", "Quote graphic: “Your price is a decision, not a guess.”"],
        ["Post 4", "Checklist: 7 things to check before you send a quote"],
        ["Post 5", "Question: “What was the first price you ever charged?”"],
        ["Stories", "Poll (hourly or per project?) → tip → tip → quiz → link to the carousel"],
        ["LinkedIn", "“The first quote I ever sent was far too low. Here’s what I’d do differently.”"],
        ["Email", "Subject: The pricing mistake I made on my first project"],
    ]
    s.append(flow("Worked Example", [
        page_head("Worked example", "One idea, 16 pieces of content",
                  "Here’s the full system applied to a single idea for an audience of new freelancers. Use it as a model for your own niche."),
        table(["Stage", "Output"], [[f"<strong>{a}</strong>", rich(b)] for a, b in example_rows], split=False, widths=["28mm", "auto"]),
        callout("Notice that every piece makes the same core point, but each one enters from a different door: a how-to, a myth, a quote, a checklist, a question, a story. Someone who sees three of them won’t feel they’re seeing the same post.", label="Why it works"),
    ]))

    tracker_rows = [[s_, "", "", "", ""] for s_ in ["Brief", "Article", "Video 1", "Video 2", "Video 3", "Post 1", "Post 2", "Post 3", "Post 4", "Post 5", "Stories", "LinkedIn", "Email"]]
    s.append(flow("Repurposing Tracker", [
        page_head("Worksheet", "Repurposing tracker", "Print this page for each core idea and tick off each piece as you go."),
        p("**Core idea:** ________________________________________________   **Dates:** ____________________"),
        table(["Piece", "Working title", "Platform", "Publish date", "Result / notes"], tracker_rows, cls="t review-grid", split=False, widths=["24mm", "auto", "28mm", "28mm", "45mm"]),
        callout(f"Looking for more repurposing prompts? See {pref('Article to Carousel')} to {pref('Content Atomizer')} in File 02.", label="More prompts"),
    ]))
    return s
