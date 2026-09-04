# Create Call Script Task

## Task Metadata

```yaml
id: create-call-script
version: 1.0.0
category: sales
tier_recommendation: 2
primary_frameworks:
  - 6-Step No BS Sales Process (Dan Kennedy)
  - 3Ms Triangle (Dan Kennedy)
  - Takeaway Selling (Dan Kennedy)
  - Urgency Engineering (Dan Kennedy)
min_output_lines: 500
primary_agent: dan-kennedy
```

---

## Purpose

Generate comprehensive high-ticket sales call scripts using Dan Kennedy's proven frameworks for $5,000+ offers. This task creates complete 45-60 minute call structures that handle rapport, discovery, presentation, objection handling, and urgency-driven closing.

**Core Principle:** "Stop prospecting. Start positioning. Stop selling. Start closing." (Dan Kennedy)

---

## When to Use This Task

### High-Value Use Cases

- High-ticket offers ($5,000+)
- Coaching and consulting sales
- Mastermind enrollment calls
- Premium program applications
- Strategy/discovery calls
- One-call-close scenarios
- Sales team training

### Ideal Scenarios

| Scenario | Recommended Focus |
|----------|-------------------|
| Coaching program ($5K-$25K) | Full 6-Step process + Takeaway positioning |
| Mastermind enrollment ($10K+) | Heavy qualification + Urgency engineering |
| Consulting engagement ($15K+) | Authority establishment + 3Ms matching |
| Premium course ($3K-$8K) | Condensed framework + Deadline close |
| Done-for-you service ($10K+) | Diagnosis-heavy + Value stack presentation |

---

## Foundational Frameworks

### Framework 1: The 6-Step No BS Sales Process (Dan Kennedy)

The complete Kennedy sales conversation flow:

```
STEP 1: PRE-QUALIFY BEFORE THE CONVERSATION
    "Before we schedule a call, I need to know..."
    "This is specifically for people who..."
    → Only talk to prospects who meet your criteria
    → Time is money - don't waste it on non-buyers

STEP 2: ESTABLISH AUTHORITY IMMEDIATELY
    "Let me be direct - I'm expensive and I'm selective..."
    "I've helped X businesses achieve Y..."
    → Position yourself as the expert from second one
    → Use takeaway positioning from the start

STEP 3: DIAGNOSE BEFORE PRESCRIBING
    "What's the biggest challenge you're facing?"
    "What have you tried before?"
    "What would it mean to solve this?"
    "What happens if you don't fix this?"
    → Ask questions that make THEM sell themselves

STEP 4: PRESENT SOLUTION AS INEVITABLE CONCLUSION
    "Based on what you told me..."
    "The three options are..."
    "Given your situation, option X is clearly..."
    → Make your offer the only logical choice

STEP 5: HANDLE OBJECTIONS WITH QUESTIONS
    Price: "Is it that you don't have the money, or that you're not sure this is the right investment?"
    Think: "What specifically do you need to think about?"
    Spouse: "What do you think their main concern will be?"
    → Never argue - ask questions instead

STEP 6: CLOSE WITH URGENCY
    "I can only hold this price until [deadline]..."
    "We only have X spots remaining..."
    "If you enroll today, you also get [bonus]..."
    → Give them a reason to decide NOW
```

### Framework 2: 3Ms Triangle - Message-Market-Media Match

Kennedy's core targeting framework for maximum relevance:

```
MARKET (Who)
├── Segment by industry/niche
├── Identify problem severity
├── Assess buying stage
└── Know their unique situation

MESSAGE (What)
├── Headline speaks to THEIR specific pain
├── Story features someone LIKE THEM
├── Benefits prioritize THEIR priorities
└── Proof shows results for THEIR situation

MEDIA (Where)
├── Reach them where THEY are
├── Use channels they trust
└── Match communication style
```

**Key Principle:** "Each person believes himself, his business, his situation, his needs to be unique—and is most responsive to someone who acknowledges that."

### Framework 3: Takeaway Selling

Reverse psychology that makes prospects chase you:

```
QUALIFICATION TAKEAWAY:
"This program isn't for everyone. Before we go further,
let me ask a few questions to see if you're even a fit..."

AVAILABILITY TAKEAWAY:
"I'm not even sure I have room in my schedule right now.
Let me check... Actually, I have ONE opening next month."

PRICE TAKEAWAY:
"Let me be upfront - this is a significant investment.
Most people aren't in a position to make this decision.
Is this something you're seriously ready for?"

OUTCOME TAKEAWAY:
"I have to be honest - this system requires work.
Not everyone follows through. Are you committed to
actually implementing what I teach?"
```

**Psychology:** People want what they can't have. The moment you push, they pull away. The moment you pull away, they chase.

### Framework 4: Urgency Engineering

Systematic approach to driving immediate action:

```
DEADLINE-DRIVEN:
├── Hard date cutoff
├── Enrollment window closes
├── Example: "Enrollment closes December 31st"
└── Strength: HIGH if real and enforced

QUANTITY-LIMITED:
├── Limited spots available
├── Capacity constraints
├── Example: "Only 10 spots - 3 remaining"
└── Strength: HIGH if verifiable

BONUS REMOVAL:
├── Bonus removed after deadline
├── Time-limited extras
├── Example: "Bonus expires midnight"
└── Strength: MEDIUM - less urgent than main offer

PRICE INCREASE:
├── Price goes up after deadline
├── Early-bird pricing
├── Example: "Price increases $500 January 1st"
└── Strength: MEDIUM - needs justification

PROGRESSIVE URGENCY:
├── Week out: "Enrollment closing soon..."
├── Day before: "Last day - deadline tomorrow..."
├── Final hours: "2 spots remaining - deadline tonight"
```

**CRITICAL:** Urgency MUST be genuine and verifiable. If you say it closes, IT CLOSES. No extensions. Fake urgency destroys trust permanently.

---

## Required Inputs

```yaml
required:
  product_name: string
    description: What you're selling
    example: "Executive Mastermind Program"

  price: number
    description: Price point of the offer ($5,000+)
    example: 15000

  offer_summary: string
    description: What they get (deliverables)
    example: "12-month mastermind with quarterly retreats, weekly calls, private community"

  target_avatar: object
    description: Ideal client profile
    example:
      industry: "Business coaches"
      revenue_range: "$250K-$1M"
      main_pain: "Stuck at current revenue ceiling"
      desired_outcome: "Scale to $2M+ without burnout"

  main_objections: array[string]
    description: Top 3-5 objections you hear most
    example:
      - "I need to think about it"
      - "It's too expensive"
      - "I need to talk to my spouse"
      - "The timing isn't right"

optional:
  call_duration: number
    description: Call length in minutes
    default: 45

  guarantee: string
    description: Risk reversal offered
    example: "90-day money-back guarantee"

  payment_options: array[string]
    description: Available payment plans
    example: ["Pay in full $15,000", "12 payments of $1,500"]

  urgency_element: string
    description: Legitimate scarcity/deadline
    example: "Only 8 spots per cohort - 3 remaining"

  case_studies: array[object]
    description: Success stories to reference
    example:
      - name: "Sarah"
        before: "$300K revenue, working 60+ hours"
        after: "$1.2M revenue, working 35 hours"
        timeframe: "18 months"

  qualification_criteria: array[string]
    description: What makes a qualified lead
    example:
      - "Revenue $250K+"
      - "Team of 2+"
      - "Decision maker"
      - "Ready to invest"
```

---

## Step-by-Step Workflow

### Phase 1: Pre-Call Preparation

Before writing the script, complete this analysis:

```
MARKET ANALYSIS (3Ms - Market):
□ Who is the ideal prospect? [Industry, revenue, team size]
□ What makes them a "starving crowd"? [Desperate pain]
□ What unique challenges do they face? [Their specific situation]
□ What have they likely tried? [Failed solutions]
□ Why didn't those work? [Gap identification]

MESSAGE ALIGNMENT (3Ms - Message):
□ What specific pain does headline address? [THEIR pain]
□ What story features someone LIKE THEM? [Relatable case]
□ What benefits matter most to THEM? [Priority mapping]
□ What proof exists for THEIR situation? [Relevant evidence]

QUALIFICATION CRITERIA:
□ Minimum revenue: $_____
□ Decision authority: [Yes/Needs approval]
□ Investment capacity: [Can afford/Needs financing]
□ Urgency level: [Ready now/Exploring]
□ Implementation ability: [Can execute/Needs support]
```

### Phase 2: Call Structure Selection

Choose the appropriate 45-60 minute structure:

```
PHASE 1: RAPPORT & AGENDA (5 minutes)
├── Warm greeting
├── Set expectations for the call
├── Gain permission to ask questions
└── Establish takeaway positioning

PHASE 2: DISCOVERY (15-20 minutes)
├── Current situation questions
├── Past attempts and failures
├── Cost of the problem
├── Desired future state
└── Urgency assessment

PHASE 3: PRESENTATION (10-15 minutes)
├── Transition from pain to solution
├── Present unique mechanism
├── Case study that mirrors them
├── Value stack with components
└── Investment and guarantee

PHASE 4: CLOSE (10-15 minutes)
├── Price presentation
├── Payment options
├── Urgency elements
├── Objection handling
└── Decision request
```

### Phase 3: Opening Script (Minutes 0-5)

**Objective:** Build rapport, establish authority, set takeaway frame.

```
KENNEDY-STYLE OPENING:

"[Name], this is [You] from [Company].
Can you hear me okay? Good.

Before we dive in, let me set some expectations.

I'm going to ask you some questions about your business.
Then, if it seems like we might be a fit,
I'll share what we do and see if it makes sense.

I have to be upfront - we're selective about who we work with.
Not everyone qualifies, and that's okay.
If it's not a fit, I'll tell you directly.

Fair enough?

[Wait for yes]

Good. So tell me - what made you apply for this call?"
```

**Authority Establishment Variations:**

```
VARIATION 1: CREDENTIAL LEAD
"Before we start, quick background - I've worked with [X] businesses
in your space and typically see [result]. Just so you know who you're
talking to. Now, what's going on in your business?"

VARIATION 2: TAKEAWAY LEAD
"I'll be honest - my calendar is full and I almost didn't take this call.
But something in your application caught my eye.
Tell me more about [specific detail they mentioned]..."

VARIATION 3: RESULTS LEAD
"I just got off a call with a client who [recent win].
Your situation sounds similar. Walk me through what's happening..."
```

### Phase 4: Discovery Questions (Minutes 5-25)

**Objective:** Diagnose before prescribing. Make them sell themselves.

```
TIER 1: SITUATION (3-5 questions)
Purpose: Understand current state

"Walk me through your business right now..."
"What's your current revenue? Team size?"
"How long have you been at this level?"
"What does a typical week look like for you?"

TIER 2: PROBLEM (3-5 questions)
Purpose: Surface explicit challenges

"What's the biggest challenge holding you back?"
"Where do things break down?"
"What's frustrating you most about [situation]?"
"If I asked your [spouse/team], what would they say the problem is?"

TIER 3: PAST ATTEMPTS (3-5 questions)
Purpose: Understand failed solutions

"What have you tried to solve this?"
"How much have you invested in trying to fix this?"
"Why do you think those didn't work?"
"What was missing from those approaches?"

TIER 4: COST (3-5 questions)
Purpose: Quantify the pain

"What's this costing you - in revenue, time, opportunity?"
"If this continues for another year, what does that look like?"
"What opportunities are you missing because of this?"
"How is this affecting you personally?"

TIER 5: DESIRED OUTCOME (2-3 questions)
Purpose: Paint the picture of success

"In a perfect world, what would [solved] look like?"
"What would that mean for your business? Your life?"
"What would you do differently if this was handled?"
```

**Discovery Flow Example:**

```
YOU: "Walk me through your business right now..."

THEM: "I'm a business coach doing about $300K."

YOU: "How long have you been at that level?"

THEM: "About 2 years. Can't seem to break through."

YOU: "What have you tried to get past it?"

THEM: "Courses, a mastermind, hired a marketing agency..."

YOU: "How much have you invested in those?"

THEM: "Probably $50K over two years."

YOU: "And did any of it work?"

THEM: "Not really. I'm still stuck."

YOU: "What do you think was missing?"

THEM: "I don't know... accountability? A real system?"

YOU: "What's staying stuck costing you?"

THEM: "At least $200K in lost revenue per year. Plus the stress is killing me."

YOU: "If this continues another year, what happens?"

THEM: "I'll probably burn out or quit. I can't keep doing this."

YOU: "On a scale of 1-10, how urgent is solving this?"

THEM: "It's a 10. I need to figure this out now."

[PAIN ESTABLISHED - Ready for transition]
```

### Phase 5: Transition to Presentation (Minutes 25-28)

**Objective:** Bridge from their pain to your solution as the inevitable conclusion.

```
TRANSITION TEMPLATE:

"Based on what you've told me, I think I understand your situation.

Let me make sure I have this right:
- You're stuck at [revenue level] and can't break through
- You've tried [solutions] but they didn't work because [gap]
- This is costing you [quantified cost] per year
- What you really want is [desired outcome]

Did I get that right?

[Wait for confirmation]

Good. Here's what I think is actually happening...
[Diagnose the real problem]

And here's what it would take to fix it...
[Transition to presentation]"
```

**Kennedy-Style Diagnosis:**

```
"Here's what I see...

You don't have a [surface problem] problem.
You have a [root cause] problem.

The reason [past solutions] didn't work is because
they were treating the symptom, not the cause.

What you actually need is [your unique mechanism].

Let me show you what that looks like..."
```

### Phase 6: Presentation (Minutes 28-42)

**Objective:** Present solution as the only logical choice.

```
PRESENTATION STRUCTURE:

SECTION 1: THE MECHANISM (2-3 min)
"Here's WHY you're stuck and what it actually takes to fix it..."
[Explain your unique approach that addresses their specific situation]

SECTION 2: THE SOLUTION (3-4 min)
"Our [program] is designed specifically for [their situation]..."
[Overview connecting to everything they said in discovery]

SECTION 3: CASE STUDY (2-3 min)
"Let me tell you about [Client] - their situation was almost identical to yours..."
[Story that mirrors their situation with specific results]

SECTION 4: THE VALUE STACK (3-4 min)
"Here's everything included:
- [Core component] - This alone is what moves the needle...
- [Component 2] - This handles [specific problem they mentioned]...
- [Component 3] - This ensures [their desired outcome]...
- [Bonus] - For people who start today..."

SECTION 5: THE INVESTMENT (1-2 min)
"The investment for all of this is [price].
We also have [payment option] if that works better."

SECTION 6: THE GUARANTEE (1 min)
"And to make this a complete no-brainer:
[Explain guarantee that addresses their specific fears]"

SECTION 7: THE URGENCY (1 min)
"The only thing is [legitimate scarcity/deadline]..."
```

### Phase 7: Close with Urgency (Minutes 42-55)

**Objective:** Get a decision NOW using Kennedy's closing techniques.

```
CLOSING SEQUENCE:

"So based on everything we discussed:
- You have [pain]
- It's costing you [amount]
- You want [outcome]
- [Program] is designed exactly for your situation
- You're protected by [guarantee]

The investment is [price], or [payment option].

[Urgency element]

Does it make sense to move forward?"
```

**Kennedy Urgency Closes:**

```
THE TAKEAWAY CLOSE:
"Look, I'm not going to convince you. Either you see the value or you don't.
What I will say is - we only have [X] spots remaining,
and based on your application, you're exactly who we designed this for.
But if you're not ready, that's okay. What would you need to see to be ready?"

THE DEADLINE CLOSE:
"I can only hold this price until [date].
After that, I can't make any promises.
If you want in at this level, the time is now."

THE SCARCITY CLOSE:
"We only take [X] clients per cohort.
Right now, [Y] spots are left.
Once they're gone, you'd have to wait [timeframe].
Should I reserve one for you?"

THE BONUS REMOVAL CLOSE:
"The [bonus] I mentioned is only available for people who start today.
Tomorrow, that's gone and won't come back.
Do you want me to include it?"
```

---

## Objection Handling Scripts

### Objection 1: "I need to think about it"

```
KENNEDY RESPONSE:

"Of course. Thinking is good.

[CLARIFY]
What specifically do you need to think about?

Is it:
- Whether this can actually work for you?
- The investment?
- The timing?
- Something else?

[Wait for real objection]

THEM: [Reveals true concern]

YOU: [Address that specific concern, then:]

"If we can handle that, are you ready to move forward?"

---

ALTERNATIVE - THE KENNEDY PUSHBACK:

"I understand. Most people who say that are really saying one of three things:
1. They're not sure it will work
2. They can't afford it
3. They're not ready to commit

Which one is it?

[Wait - let them answer honestly]

[Address the REAL objection]"
```

### Objection 2: "It's too expensive"

```
KENNEDY RESPONSE:

"I appreciate you being direct.

[CLARIFY]
When you say expensive - compared to what?

- Compared to what staying stuck is costing you?
- Compared to what you expected?
- Compared to another option?

---

IF COMPARED TO COST OF INACTION:

"You told me this problem is costing you [amount] per year.
The investment here is [price].

If we solve this, you don't just get [result].
You stop losing [amount] every year.

Which costs more - solving the problem or living with it?"

---

IF THEY CAN'T AFFORD IT:

"I understand. Let me ask you something...

Is it that you literally don't have access to [amount],
or that you're not convinced it's the right investment?

[If not convinced]: "What would you need to see to feel confident?"

[If truly no funds]: "What resources could you access?
Do you have credit? Savings? Could you liquidate anything?
Because if this is really a priority..."

[Payment plan option if available]
```

### Objection 3: "I need to talk to my spouse"

```
KENNEDY RESPONSE:

"Absolutely. Big decisions should be made together.

[CLARIFY]
When you talk to them, what do you think they'll say?"

---

IF SPOUSE WILL BE SUPPORTIVE:

"Great. Since they'll likely support it, let's get them on now.
I can answer their questions directly, and you can decide together.
Can we call them?"

---

IF SPOUSE WILL HAVE CONCERNS:

"What concerns do you think they'll have?"

[Listen]

"Let me address those now so you can explain:
- Concern 1: [Response]
- Concern 2: [Response]
- Concern 3: [Response]

If YOU'RE confident, are you ready to move forward?

[If yes]:
"Talk to them tonight. Share what we discussed.
Let's reconnect tomorrow at [time] for a final decision."

[Schedule specific follow-up - don't leave it open]
```

### Objection 4: "The timing isn't right"

```
KENNEDY RESPONSE:

"I hear you. Timing matters.

Let me ask - is this a 'not right now' or 'never'?"

---

IF NOT RIGHT NOW:

"When would be better? And what changes between now and then?

Here's what I've observed in [X years]:
The 'perfect time' rarely arrives on its own.
People who wait for perfect timing usually wait forever.

What would have to be true for NOW to be the right time?"

---

KENNEDY REFRAME:

"Let me be direct...

You've been dealing with this problem for [time they mentioned].
You've already invested [money they mentioned] trying to fix it.
It's costing you [amount] every year you don't solve it.

How much longer can you afford to wait?

If not now, when? And what will waiting cost you?"
```

---

## Post-Close Protocols

### Reinforcement Script

```
"Congratulations. You made the right decision.

Here's why this is going to work for you:
1. [Connect to their specific pain]
2. [Connect to their specific goal]
3. [Reference similar case study]

Over the next day or two, doubts might creep in.
That's normal. When that happens, remember:
- You have [guarantee], so you're protected
- [X] people in your situation have succeeded
- I wouldn't have accepted you if I didn't think you'd succeed

Here's what happens next:
1. [Immediate step]
2. [First 24 hours]
3. [First week]

Your first action is [specific task].
Can you do that by [deadline]?

Welcome to [program]. Let's get to work."
```

### Follow-Up Sequence (Non-Closes)

```
FOLLOW-UP 1 (24 hours):
Subject: Following up - quick question

[Name],

After our call, I've been thinking about your situation.
Specifically, [specific pain point they mentioned].

Have you made a decision on how to address this?

[Your name]

---

FOLLOW-UP 2 (72 hours):
Subject: [Specific result] - like [case study name]

[Name],

Just spoke with [client] who had the exact same challenge.
[Brief result they achieved].

Still thinking about [their situation]?

[Your name]

---

FOLLOW-UP 3 (7 days):
Subject: Closing your file

[Name],

I want to respect your time, so I'll be direct.

Are you still interested in [solving problem]?

If yes - let's schedule a quick call. [Urgency element].
If no - no hard feelings. I'll close your file.

Either way, let me know?

[Your name]
```

---

## Quality Metrics

### Call Performance Tracking

```
ACTIVITY METRICS:
□ Calls completed: _____
□ Average call duration: _____ minutes
□ Discovery-to-pitch ratio: _____% (Target: 60%+)

CONVERSION METRICS:
□ Show rate: _____% (Target: 80%+)
□ Close rate: _____% (Target: 30-40%)
□ Cash collected: _____% (Target: 70%+)
□ Refund rate: _____% (Target: <5%)

QUALITY INDICATORS:
□ Questions asked per call: _____ (Target: 12-18)
□ Objections surfaced: _____ (Target: 2-4)
□ Close attempts: _____ (Target: 3-5)
□ Takeaway moments: _____ (Target: 2-3)
```

### Benchmark Targets for High-Ticket

| Metric | Poor | Average | Good | Elite |
|--------|------|---------|------|-------|
| Show Rate | <60% | 70% | 80% | 90%+ |
| Close Rate | <20% | 30% | 40% | 50%+ |
| Avg Call Length | <35min | 45min | 55min | 60min |
| Cash Collected | <50% | 65% | 75% | 85%+ |
| Refund Rate | >10% | 7% | 4% | <2% |

---

## Common Mistakes to Avoid

| Mistake | Impact | Kennedy Fix |
|---------|--------|-------------|
| Pitching too early | -40% close rate | Complete discovery FIRST - diagnose before prescribing |
| No takeaway positioning | -25% close rate | Establish you're the prize from the start |
| Weak authority | -30% close rate | Lead with credentials and results |
| Arguing objections | -35% close rate | Ask questions, never argue |
| No urgency | -40% close rate | Every close needs a deadline |
| Fake urgency | -50% trust | Only use genuine, verifiable scarcity |
| Open-ended follow-up | -60% conversion | Always schedule specific next step |

---

## Output Format

```yaml
generated_output:
  format: markdown
  sections:
    - call_framework_summary
    - pre_call_preparation_checklist
    - opening_script (with authority establishment)
    - discovery_questions (customized to their market)
    - transition_script
    - presentation_script (with value stack)
    - closing_sequences (with urgency elements)
    - objection_scripts (for each objection provided)
    - post_close_reinforcement
    - follow_up_sequence
    - performance_tracking_scorecard
```

---

## Integration with Other Tasks

### Before This Task
- `avatar-research.md` - Deep understanding of target market (3Ms - Market)
- `create-offer.md` - Build the high-ticket offer to sell
- `create-unique-mechanism.md` - Develop differentiation for presentation

### After This Task
- `create-email-sequence.md` - Follow-up for non-closes
- `apply-sugarman-triggers.md` - Add psychological triggers to script

### Complementary Tasks
- `create-objection-algorithms.md` - Deep objection handling library
- `build-authority-arsenal.md` - Proof elements for presentation

---

## Workflows Using This Task

| Workflow | Phase | Purpose |
|----------|-------|---------|
| wf-3-high-ticket.yaml | Phase 3 | Sales call script for $5K+ offers |

---

## References

### Primary Sources
- Kennedy, Dan. "No B.S. Sales Success" - 6-Step Sales Process
- Kennedy, Dan. "No B.S. Direct Marketing" - 3Ms Framework
- Kennedy, Dan. "Magnetic Marketing" - Market Selection
- Kennedy, Dan. "Ultimate Sales Letter" - Urgency Engineering

### Related Agent
`squads/copy/agents/dan-kennedy.md`

---

*Task Version: 1.0.0*
*Last Updated: 2026-01-23*
*Primary Frameworks: 6-Step No BS Sales Process, 3Ms Triangle, Takeaway Selling, Urgency Engineering*
*Primary Agent: Dan Kennedy*
*Minimum Output: 500 lines*
