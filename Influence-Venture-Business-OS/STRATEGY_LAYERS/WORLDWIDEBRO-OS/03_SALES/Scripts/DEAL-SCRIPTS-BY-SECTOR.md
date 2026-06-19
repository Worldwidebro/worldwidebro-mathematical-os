# Deal Scripts by Sector

**Purpose:** Exact messaging templates for Echo (E-Commerce), Swift (Technology), and Bella (Beauty & Wellness) agents  
**Status:** Phase 2.2 — Messaging & Objection Handling  
**Created:** May 9, 2026

---

## SECTOR 1: E-COMMERCE (Echo Agent)

### Call Opening (First 30 seconds)

**Script:**
```
"Hi [Name], this is Echo with [Venture Name]. 
I noticed you're managing [Shopify/Amazon/eBay/multi-channel] sales. 
Quick question—how are you handling inventory sync across all those channels right now?"
```

**Tone:** Friendly, curious, peer-to-peer (not salesy)  
**Goal:** Get them talking about their current process (listening phase)  
**Expected response:** Either "manually," "we use a tool," or "it's a nightmare"

### Pain Discovery (2-3 minutes)

**Follow-up questions (pick 1-2):**
- "How often do you oversell on one channel while another is out of stock?"
- "What happens when inventory doesn't sync and you sell something you don't have?"
- "How many hours per week does someone spend managing channels manually?"
- "Have you lost a sale because of inventory confusion across platforms?"

**Listen for:** Cost of problem ($ lost per week), frequency (daily/weekly), impact on business (revenue, credibility, customer satisfaction)

**Quantify the pain:**
- Typical responses: "Maybe 2-3 oversells per week," "costs us $200-300 per incident"
- You calculate: 2.5 oversells × $200 = $500/week = $26K/year in lost revenue
- Say: "So that's roughly $26K a year you could recover by preventing those oversells. Does that math feel right?"

### Pitch (1 minute)

**If they acknowledge pain:**
```
"So here's what we do: We sync your inventory in real-time across Shopify, Amazon, eBay, 
and your website. When you sell one unit, it updates everywhere instantly. 
Most sellers recover $800-$2K per month just from preventing oversells. 
One client went from 2 oversells per week to zero."
```

**Positioning:**
- Not "software"—positioning: "peace of mind on auto-pilot"
- Not "tech tool"—positioning: "your inventory doing the work for you"
- Anchor to ROI: "That $26K/year you're losing? You make that back in the first 3 months."

### Objection Handling

**Objection: "We already use [Inventory tool X]"**
```
Response: "Got it. How well does that sync across [specific channels they mentioned]? 
Most tools are good at one or two channels but struggle with [Shopify + Amazon + manual store] together. 
Worth a quick look at how we handle all three?"
```
**Why it works:** Doesn't attack their tool; shifts to channels they said they use  
**Action:** Ask for demo

---

**Objection: "This sounds expensive"**
```
Response: "I get that—normally we're $500-1,500/month depending on volume. 
But let me ask: how much are those 2-3 oversells per week costing you? 
If it's $26K a year, you're basically getting this free the first quarter and then making money."
```
**Why it works:** Reframes cost as investment with clear ROI; uses their number  
**Action:** Close with demo offer

---

**Objection: "We're not ready to change systems right now"**
```
Response: "I hear that. Most sellers aren't actively looking—they just realize one day 
the manual process is broken and they lose a big sale. 
Would it hurt to see a 15-minute demo now, so you know what's possible when you *are* ready?"
```
**Why it works:** Validates their timeline; frames demo as low-cost education  
**Action:** Calendar demo for next week

---

### Demo Booking Close (30 seconds)

**If they're engaged (pain acknowledged + no hard no):**
```
"Here's what makes sense: let me show you exactly how this works with your channels 
in about 15 minutes. You'll see how real-time sync prevents those oversells. 
Sound good? Are you free [Tuesday afternoon / Thursday morning] this week?"
```

**If they hesitate:**
```
"No pressure—I'll send you a 2-minute video walkthrough. 
If it looks worth 15 minutes, we'll get on a call. Fair?"
```

**Close rate target:** 15-20% of calls

---

## SECTOR 2: TECHNOLOGY (Swift Agent)

### Call Opening (First 30 seconds)

**Script:**
```
"Hi [Name], this is Swift with [Venture Name]. 
I see you're building [product/service]. Quick question—how much time is your team 
spending on deployments vs. actually shipping features right now?"
```

**Tone:** Technical peer, understands dev velocity  
**Goal:** Get them thinking about deploy friction (the bottleneck they haven't quantified)  
**Expected response:** "Too much," "30 minutes usually," "it's a pain"

### Pain Discovery (2-3 minutes)

**Follow-up questions (pick 1-2):**
- "Walk me through a typical deploy. What takes the longest?"
- "How many deploys per day/week can you realistically do?"
- "What if you could ship 5x faster? What would that unlock for your product?"
- "How many good ideas have you delayed shipping because deploys are slow?"

**Listen for:** Time spent, frequency of deploys, impact on shipping velocity, competitive pressure

**Quantify the pain:**
- Typical response: "30 minutes per deploy, 2-5 deploys per week"
- You calculate: 30min × 4 deploys/week × 50 working weeks = 100 hours/year = $50K in engineer time wasted
- Plus: 5 deploys/week → 10 deploys/week = 2x shipping velocity = competitive advantage
- Say: "So you're spending roughly $50K a year on deploy overhead. And if you could ship 10 times a week instead of 5, you'd ship faster than competitors. Does that feel right?"

### Pitch (1 minute)

**If they acknowledge pain:**
```
"Here's what we do: We cut deploy time from 30 minutes down to 3 minutes. 
Fully automated. No infrastructure work. One client went from shipping 2 features per week to 10. 
You get that $50K back in engineer time—plus you move faster than competitors."
```

**Positioning:**
- Not "CI/CD tool"—positioning: "deploy on every commit"
- Not "DevOps"—positioning: "ship code, not infrastructure"
- Anchor to velocity: "Want to ship 5x faster? This is how."

### Objection Handling

**Objection: "We have a custom deploy setup"**
```
Response: "That's actually ideal. Our solution works with custom setups—Kubernetes, Lambda, 
Docker, whatever you're running. Most custom setups are fast for the first 10 minutes, 
then hit a bottleneck. Where's your bottleneck?"
```
**Why it works:** Validates their uniqueness; pivots to the one slow step they can't fix  
**Action:** Ask to understand bottleneck, then show demo

---

**Objection: "We'd have to change too much"**
```
Response: "I get that risk. Usually it's a 3-line config change. 
Here's what I'd do: I'd send you a 10-minute walkthrough showing exactly what changes. 
You can evaluate without committing. Sound fair?"
```
**Why it works:** Lowers activation energy; removes mystery  
**Action:** Async video walkthrough, then demo if interested

---

**Objection: "We're using [CI/CD tool X] and it works fine"**
```
Response: "Cool. So here's the real question: Are you shipping 5x per week, or 5x per day? 
Most teams hit a wall at 5x per day because their current tool wasn't built for that velocity. 
If you're happy at 5x/week, no worries. But if you want to ship faster, there's a reason."
```
**Why it works:** Acknowledges their tool is fine; reframes as a velocity conversation  
**Action:** Demo of 10 deploys/day capability

---

### Demo Booking Close (30 seconds)

**If they're engaged (pain acknowledged + technical curiosity):**
```
"Here's what makes sense: I'll show you a live demo—one of our clients deploying 10 times in an hour. 
You'll see the setup, the time savings, everything. 20 minutes. 
Are you free [Thursday 2pm / Friday 10am] this week?"
```

**If they're skeptical:**
```
"Here's an even better idea: I'll send you a 3-minute video of a deploy in action. 
If it looks like something worth exploring, we can talk next week. Deal?"
```

**Close rate target:** 18-22% of calls

---

## SECTOR 3: BEAUTY & WELLNESS (Bella Agent)

### Call Opening (First 30 seconds)

**Script:**
```
"Hi [Name], this is Bella with [Venture Name]. 
I'm calling salons and spas in your area. Quick question—how much revenue are you 
leaving on the table because of no-shows each month?"
```

**Tone:** Empathetic, practical, business-focused  
**Goal:** Make them think about dollar impact of no-shows (many haven't quantified)  
**Expected response:** "I don't know," "a lot," "maybe $400/week"

### Pain Discovery (2-3 minutes)

**Follow-up questions (pick 1-2):**
- "How many appointments per week are no-shows?"
- "What's your average service price?"
- "How does a no-show impact your day? Do you have another client lined up?"
- "How many staff members are sitting idle because of a no-show?"

**Listen for:** Number of no-shows, revenue per appointment, impact on staff scheduling

**Quantify the pain:**
- Typical response: "Maybe 2 no-shows per day, $120 per appointment"
- You calculate: 2 no-shows × $120 × 5 days/week × 50 weeks = $60K/year in lost revenue
- They're likely surprised: "So that's roughly $60K a year you're losing to no-shows."
- Follow: "What if you could reduce that by 40%? That's $24K back."

### Pitch (1 minute)

**If they acknowledge pain:**
```
"Here's what we do: We send SMS reminders 24 hours before appointments. 
Clients confirm they're coming or reschedule. No-shows drop from 2 per day to 1 per day. 
You recover $24K-$30K per year. Plus your staff isn't sitting idle. 
One salon owner said it was the best ROI decision she made."
```

**Positioning:**
- Not "software"—positioning: "your clients remembering their appointments"
- Not "tech"—positioning: "confirmed appointments = full schedule = less stress"
- Anchor to tangible outcome: "We cut your no-shows in half. That's $30K a year and peace of mind."

### Objection Handling

**Objection: "Don't have a budget for new tools"**
```
Response: "I totally understand. Here's how to think about it: 
You're losing $60K a year to no-shows. Our tool is $200-300/month, so $3K/year. 
You pay for itself in 6 days. Can you find $200/month in the $60K you're losing?"
```
**Why it works:** Reframes cost as recovery, not expense; math is undeniable  
**Action:** Close with demo

---

**Objection: "We already text reminders"**
```
Response: "That's great—you're already thinking about it. Here's the gap: manual texts are good, 
but clients don't always respond. We automate the *confirmation* part. 
They text back 'yes' or 'reschedule,' so you know who's actually coming. 
Worth seeing how that reduces your no-shows even more?"
```
**Why it works:** Validates their effort; shows upgrade path without implying they're wrong  
**Action:** Demo of confirmation workflow

---

**Objection: "Clients won't use it"**
```
Response: "Here's the thing: clients *love* reminders. Nobody wants to forget an appointment. 
The pushback we hear is actually from schedulers worried about extra work. 
But it's actually less work—you know 24 hours ahead who's coming. Zero surprises."
```
**Why it works:** Addresses the real concern (staff friction); shows benefit to them  
**Action:** Demo of staff experience, then client experience

---

### Demo Booking Close (30 seconds)

**If they're engaged (pain acknowledged + seeing value):**
```
"Here's what makes sense: I'll show you exactly how it works with a salon like yours. 
You'll see the reminder flow, how clients respond, how no-shows drop. 15 minutes. 
Are you free [Wednesday 1pm / Friday 10am] this week?"
```

**If they're on the fence:**
```
"I get it—busy schedule. How about this: I'll send you a quick video showing a week 
of how it works. Takes 3 minutes to watch. If it looks good, we schedule a demo. 
Sound fair?"
```

**Close rate target:** 12-18% of calls

---

## Cross-Sector Closing Patterns

### The Warm Close (They're interested, ready to decide)
```
"Perfect. So just to confirm: [recap pain] → [our solution] → [outcome]. 
You want to [see a demo / try a pilot / move forward]?

Great. [Agent name] here will send you a calendar link for [specific day/time]. 
Sound good?"
```

### The Soft Close (They're interested but cautious)
```
"I don't want to push you into anything. But would it hurt to see a demo? 
No obligation—just so you know what's possible if you decide to move forward later.

When works for you? [Next Tuesday? Thursday?]"
```

### The Objection Loop (They keep saying "no")
**Rule:** After 2 objections + 2 responses, ask the final qualifying question:
```
"Look, I don't want to waste your time. Honest question: 
Is this something you'd *want* to solve if the cost and implementation were zero friction?

[Listen to answer]

If yes: 'Then let's find a time to chat.'
If no: 'Totally fair. If that changes, you know where to find me.'"
```

**Why it works:** Resets the conversation; if they still say no, you've qualified them out (don't waste follow-up)

---

## Tone Guidance by Sector

### E-Commerce (Echo)
- **Tone:** Peer, practical, numbers-driven
- **Pace:** Medium (they have a process, you're optimizing it)
- **Trust signal:** Reference other sellers, use their numbers
- **Avoid:** Jargon ("omnichannel," "SKU sync")—say "inventory across all your channels"

### Technology (Swift)
- **Tone:** Technical equal, understands their pain
- **Pace:** Fast (they value velocity)
- **Trust signal:** Reference deploy metrics, mention their tech stack
- **Avoid:** Over-selling ("AI-powered," "revolutionary")—show, don't tell

### Beauty & Wellness (Bella)
- **Tone:** Friendly, empathetic, helpful
- **Pace:** Slower (they're less technical, want to understand impact)
- **Trust signal:** Specific outcomes ("you get your Friday nights back"), ROI math
- **Avoid:** Complexity—keep it simple and tangible

---

## Call Flow Timing

**Ideal call structure:**
- **0-1 min:** Opening + immediate pain question
- **1-3 min:** Discovery (let them talk about their process)
- **3-5 min:** Pain quantification (calculate the cost with them)
- **5-6 min:** Pitch (deliver solution + ROI anchor)
- **6-8 min:** Objection handling (if needed)
- **8-9 min:** Close (ask for demo)

**Total:** 8-10 minutes  
**If over 12 min:** You're in the weeds, pivot to "Let me show you in a demo"

---

## Recording & Refinement

After each sector's first 10 calls:
1. **Review transcripts:** Which opening question got them talking? Which objections came up?
2. **Update messaging:** If "no-shows cost you HOW MUCH?" gets better engagement than asking no-show rate, use it in all future calls
3. **Track metrics:** Demo booking rate per objection type (e.g., "We already use X" has 8% booking vs. cost objections have 22%)
4. **Refine close:** If "Would it hurt to see a demo?" books more than "You need this," keep using it

---

## Expected Outcomes (Week 1)

| Metric | E-Commerce | Technology | Beauty | Target |
|--------|-----------|-----------|---------|--------|
| Calls attempted | 50 | 30 | 40 | 120 |
| Avg call duration | 9 min | 11 min | 8 min | 8-10 min |
| Demos booked | 7 (15%) | 6 (20%) | 5 (13%) | 15-20% |
| **Total demos** | **7** | **6** | **5** | **~18 demos** |

---

## Status: ✅ READY FOR MAY 10

All three sector scripts, messaging templates, objection handling, and close frameworks documented.

**Next:** Deploy agents May 10 and execute Week 1 calling campaign.

