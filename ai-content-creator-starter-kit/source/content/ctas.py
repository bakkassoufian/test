"""File 08 — BONUS: 50 CTAs.

Each category: (title, guidance, [(cta, when to use it)]).
"""

GLOSSARY = {
    "TOPIC": "The subject you post about.",
    "ACTIVITY": "Something your audience does.",
    "SITUATION": "A moment when your post becomes useful again.",
    "STAGE": "A point in your audience’s journey — “ready to launch”, “planning your first trip”.",
    "FREQUENCY": "How often you post or send — “Tuesday”, “week”, “month”.",
    "PROJECT": "Something you’re building in public.",
    "LINK": "A web address. Remember: most platforms only allow clickable links in specific places.",
    "PRODUCT": "The name of your product.",
    "SERVICE": "The name of your service.",
    "DATE": "A real deadline.",
    "KEYWORD": "A single word people comment to receive something.",
    "RESOURCE": "A free guide, checklist, template or mini-course.",
    "COMMUNITY": "Your group, server, membership or forum.",
    "GOAL": "What your audience is working toward.",
}

CATEGORIES = [
    (
        "Engagement",
        "Low-effort ways to interact. Use these when you want quick reactions and a sense of who’s reading.",
        [
            ("Which one are you — A or B? Tell me below.", "Comparison posts, this-or-that content"),
            ("If this sounds familiar, you’re not alone. Let me know you’ve been there.", "Relatable posts about common struggles"),
            ("Vote in today’s Story — I’ll share the results tomorrow.", "When you want to move feed viewers to Stories"),
            ("Rate your [TOPIC] confidence from 1 to 10. No judgment.", "Educational posts, audience research"),
            ("Which tip are you trying first?", "List and tips posts"),
            ("Tag the friend you’d do this with.", "Fun, shareable or activity-based posts"),
        ],
    ),
    (
        "Comments",
        "Ask questions that are easy to answer. A specific question gets more replies than “Thoughts?”.",
        [
            ("What would you add to this list?", "Lists, resource roundups, tips"),
            ("Agree or disagree? I’d genuinely like to hear the other side.", "Opinion and contrarian posts"),
            ("Drop your biggest question about [TOPIC] — I’ll answer as many as I can.", "Educational posts; collects ideas for future content"),
            ("What’s one thing you’d do differently?", "Storytelling and lesson-learned posts"),
            ("What’s the hardest part of [ACTIVITY] for you right now?", "Problem-focused posts, audience research"),
            ("Have you tried this? How did it go?", "Tutorials and how-to content"),
        ],
    ),
    (
        "Saves",
        "Saves suit content people will need again later. Remind them when it will be useful.",
        [
            ("Save this for the next time you [SITUATION].", "Checklists, troubleshooting guides"),
            ("Bookmark this before your next [ACTIVITY].", "Preparation posts and checklists"),
            ("Save this — you’ll want it when you’re [STAGE].", "Content for people who aren’t ready yet"),
            ("Keep this checklist somewhere you’ll see it.", "Checklist carousels"),
            ("Save it now, try it this weekend.", "Practical tutorials and projects"),
            ("Save this so you don’t have to search for it later.", "Reference content, glossaries, resource lists"),
        ],
    ),
    (
        "Shares",
        "People share content that makes them look helpful or says something they agree with.",
        [
            ("Send this to someone who’s just getting started.", "Beginner-friendly educational posts"),
            ("Share this with the friend who always asks you about [TOPIC].", "Explainers and FAQs"),
            ("Know someone who needs to hear this today? Pass it on.", "Encouraging or inspirational posts"),
            ("Share this to your Stories if you agree.", "Opinion posts and strong statements"),
            ("Forward this to your team before your next planning meeting.", "Professional and LinkedIn content"),
            ("If this helped you, share it with one person it could help too.", "Any genuinely useful post"),
        ],
    ),
    (
        "Follows",
        "Give a reason to follow: what people will keep getting, how often, or what’s coming next.",
        [
            ("Follow for practical [TOPIC] tips you can use the same day.", "Educational content"),
            ("I post about [TOPIC] every [FREQUENCY]. Follow along if that’s useful to you.", "When you have a consistent schedule"),
            ("This is part 1. Follow so you don’t miss part 2.", "Series and multi-part stories"),
            ("Follow if you want the no-fluff version of [TOPIC].", "Direct, practical creators"),
            ("I’m building [PROJECT] in public — follow to see how it goes.", "Behind-the-scenes and journey content"),
            ("New here? Start with the pinned posts, then follow for more.", "Posts likely to reach new viewers"),
        ],
    ),
    (
        "Website",
        "Send people somewhere with more depth. Be clear about what they’ll find when they click.",
        [
            ("The full guide is on my website — link in bio.", "When the post summarizes a longer article"),
            ("I wrote a longer breakdown on the blog. Link in bio.", "Educational posts with more detail available"),
            ("The templates are free on my site — link in bio.", "Posts that mention a free download"),
            ("Read the full case study at [LINK].", "LinkedIn, newsletters, platforms with clickable links"),
            ("Everything I mentioned in this video is listed on my website.", "Tool and resource videos"),
        ],
    ),
    (
        "Products",
        "Be direct and calm. Say what it is, who it’s for and where to find it — then stop.",
        [
            ("If you want the full system, it’s in [PRODUCT] — link in bio.", "After an educational post on the same subject"),
            ("[PRODUCT] is open until [DATE]. Details in bio.", "Launches and real deadlines only"),
            ("Not sure if [PRODUCT] is right for you? Send me a message and ask.", "Higher-priced offers; builds trust"),
            ("Here’s what’s inside [PRODUCT]. Link in bio if it’s a fit.", "Product walkthroughs"),
            ("Want help with this? That’s exactly what [SERVICE] is for — book a call through the link in bio.", "Service providers, consultants, freelancers"),
        ],
    ),
    (
        "Leads",
        "Offer something useful in exchange for an email or a message. Only use keyword CTAs if you will actually reply.",
        [
            ("Comment “[KEYWORD]” and I’ll send you the free checklist.", "When you can reply personally or use an approved automation"),
            ("Get the free [RESOURCE] — link in bio.", "Lead magnets and free downloads"),
            ("Join the newsletter for one practical tip every [FREQUENCY].", "Building an email list"),
            ("Message me “[KEYWORD]” and I’ll send you the template.", "Direct messages, warm leads"),
            ("Grab the free [RESOURCE] before [DATE].", "Time-limited free resources"),
        ],
    ),
    (
        "Community",
        "Invite people to connect with you and with each other. These work best when you show up in the replies.",
        [
            ("Introduce yourself in the comments — let’s connect.", "Welcome posts, milestone posts"),
            ("Join our free [COMMUNITY] — link in bio.", "Groups, servers and free memberships"),
            ("Share your progress in the comments each week. We’ll cheer you on.", "Challenges and recurring series"),
            ("Got a win this week? Post it below — big or small.", "End-of-week posts"),
            ("Who else is working on [GOAL] this month? Say hi and find your people.", "Goal-based communities"),
        ],
    ),
]
