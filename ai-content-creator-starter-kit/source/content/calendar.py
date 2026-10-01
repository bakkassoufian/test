"""File 05 — 30-Day Content Calendar.

Each day: (content idea, format, pillar, goal, CTA, toolkit references).
Toolkit references name items by title, e.g. ("prompt", "Mistakes Carousel");
build.py resolves them to numbers and fails if a title doesn't exist.
Pillar keys: edu, per, eng, ins, pro, com.
"""

PILLARS = {
    "edu": ("Educational", "p-edu"),
    "per": ("Personal", "p-per"),
    "eng": ("Engagement", "p-eng"),
    "ins": ("Inspirational", "p-ins"),
    "pro": ("Promotional", "p-pro"),
    "com": ("Community", "p-com"),
}

WEEKS = [
    (
        "Week 1 — Introduce yourself",
        "Show people who you are, who you help and what they can expect from your account.",
        [
            ("Introduce yourself: who you help, what you share and why", "Photo post", "per", "Trust", "Say hi and tell me what you’re working on.",
             [("idea", "Why I Started"), ("prompt", "Origin Story")]),
            ("The beginner’s glossary for your niche", "Carousel", "edu", "Saves", "Save this for later.",
             [("idea", "The Beginner’s Glossary"), ("prompt", "7-Slide Educational Carousel"), ("template", "Educational Carousel")]),
            ("This-or-that poll about your topic", "Stories", "eng", "Conversation", "Vote in the poll.",
             [("idea", "This or That"), ("prompt", "Interactive Story Sequence")]),
            ("One common mistake — and the fix", "Reel", "edu", "Reach", "Send this to someone who needs it.",
             [("idea", "Common Mistake, Explained"), ("prompt", "Common Mistake Reel"), ("hook", "Stop doing [X] if you want [RESULT].")]),
            ("Why I started", "Carousel", "per", "Connection", "What made you start?",
             [("idea", "Why I Started"), ("prompt", "Personal Story Carousel"), ("template", "Storytelling")]),
            ("A quick win in under 10 minutes", "Reel", "edu", "Saves", "Try it today and tell me how it went.",
             [("idea", "The 10-Minute Quick Win"), ("prompt", "30-Second Educational Reel"), ("hook", "Here’s how to [RESULT] in [NUMBER] simple steps.")]),
            ("Review the week + share Day 2 in Stories", "Stories", "com", "Review", "Reply with your questions.",
             [("prompt", "Prioritize Your Ideas")]),
        ],
    ),
    (
        "Week 2 — Build trust",
        "Go deeper. Teach complete processes, show your work and start answering real questions.",
        [
            ("Step-by-step tutorial for one key task", "Carousel", "edu", "Saves", "Save this so you can follow along.",
             [("idea", "Step-by-Step Tutorial"), ("prompt", "Step-by-Step Tutorial Carousel"), ("template", "Step-by-Step")]),
            ("Behind the scenes: your workspace and process", "Reel", "per", "Connection", "Show me your workspace.",
             [("idea", "Workspace Tour"), ("prompt", "Day-in-the-Life Reel"), ("template", "Behind the Scenes")]),
            ("Myth vs fact", "Carousel", "edu", "Shares", "Which myth did you believe?",
             [("idea", "Myth vs Reality"), ("prompt", "Myth vs Fact Carousel"), ("template", "Myth vs Fact")]),
            ("Ask me anything — collect questions", "Stories", "eng", "Conversation", "Send me your questions.",
             [("idea", "Ask Me Anything"), ("prompt", "Interactive Story Sequence")]),
            ("Answer one real question from Day 11", "Reel", "edu", "Trust", "Send me your next question.",
             [("idea", "Answer a Real Question"), ("prompt", "Reply-to-Comment Video")]),
            ("Tools I actually use", "Carousel", "edu", "Saves", "Which tool would you add?",
             [("idea", "Tools I Use Every Day"), ("prompt", "Tools and Resources Post")]),
            ("Review the week + one original insight", "Photo post", "ins", "Reach", "Save this if you needed it today.",
             [("prompt", "Original Insight Graphics"), ("template", "Quote")]),
        ],
    ),
    (
        "Week 3 — Show your expertise",
        "Share your methods and your opinions, and introduce your offer for the first time.",
        [
            ("The biggest mistake I made — and what I learned", "Reel", "per", "Trust", "What mistake taught you the most?",
             [("idea", "My Biggest Mistake So Far"), ("prompt", "Failure Story"), ("hook", "I made this [TOPIC] mistake for years. Don’t repeat it.")]),
            ("Your framework, explained", "Carousel", "edu", "Follows", "Follow for more frameworks like this.",
             [("idea", "Your Framework, Explained"), ("prompt", "Framework Post")]),
            ("Agree or disagree? One clear statement", "Photo post", "eng", "Comments", "Agree or disagree? Tell me why.",
             [("idea", "Agree or Disagree?"), ("prompt", "Generate Honest Opinions")]),
            ("Fix one common problem in 3 steps", "Reel", "edu", "Saves", "Save this for when it happens.",
             [("idea", "Fix It in 3 Steps"), ("prompt", "How-To Tutorial Reel"), ("template", "Problem → Solution")]),
            ("Before / after: a real transformation", "Carousel", "ins", "Proof", "Want the steps? Comment below.",
             [("idea", "Progress over Perfection"), ("prompt", "Before/After Carousel"), ("template", "Before / After")]),
            ("How it works: your offer in 3 steps", "Carousel", "pro", "Awareness of offer", "Questions? Send me a message.",
             [("idea", "How It Works"), ("prompt", "Feature-to-Benefit Carousel"), ("template", "Product Promotion")]),
            ("Review the week + Stories recap", "Stories", "com", "Review", "Which post was your favorite?",
             [("prompt", "Weekly Newsletter from Posts")]),
        ],
    ),
    (
        "Week 4 — Convert and connect",
        "Combine your most useful content with proof and a clear, calm invitation to work with you.",
        [
            ("5 tips I’d give a complete beginner", "Carousel", "edu", "Saves", "Send this to a beginner.",
             [("idea", "5 Tips for a Complete Beginner"), ("prompt", "7-Slide Educational Carousel"), ("template", "3 Tips")]),
            ("Customer story or testimonial", "Photo post", "pro", "Proof", "Want results like this? Message me.",
             [("idea", "Customer Review Spotlight"), ("prompt", "Testimonial Post"), ("template", "Testimonial")]),
            ("An honest unpopular opinion", "Reel", "per", "Comments", "Your turn — agree or disagree?",
             [("idea", "Share Your Unpopular Opinion"), ("prompt", "Reaction-Style Reel"), ("hook", "Unpopular opinion: [COMMON ADVICE] is overrated.")]),
            ("A real day in your work", "Reel", "per", "Connection", "Want more behind-the-scenes?",
             [("idea", "A Normal Day"), ("prompt", "Day-in-the-Life Reel")]),
            ("FAQ about your offer", "Carousel", "pro", "Clicks", "Have another question? Ask below.",
             [("idea", "FAQ About the Offer"), ("template", "FAQ")]),
            ("A save-worthy checklist", "Carousel", "edu", "Saves", "Save this checklist.",
             [("idea", "Before-You-Start Checklist"), ("prompt", "Save-Worthy Checklist Post"), ("template", "Checklist")]),
            ("Review the week + a quiz in Stories", "Stories", "eng", "Conversation", "How many did you get right?",
             [("idea", "Test Your Knowledge")]),
        ],
    ),
    (
        "Days 29–30 — Repurpose and reflect",
        "Give your best idea a second life and close the month by sharing what you learned.",
        [
            ("Remake your best post of the month in a new format", "Reel", "edu", "Reach", "Follow for more like this.",
             [("prompt", "Carousel to Reel"), ("prompt", "Refresh an Old Post")]),
            ("30-day recap: what I learned and what’s next", "Carousel", "per", "Follows", "Follow for what’s coming next.",
             [("idea", "This Time Last Year"), ("prompt", "Then vs Now Story")]),
        ],
    ),
]

# Weekday labels starting on a Monday; days 7, 14, 21 and 28 are review days.
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
