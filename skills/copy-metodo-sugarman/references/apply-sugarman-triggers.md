# Apply Sugarman 30 Psychological Triggers

## Task Anatomy

| Field | Value |
|-------|-------|
| **task_name** | Apply Sugarman 30 Psychological Triggers |
| **status** | `active` |
| **responsible_executor** | @joe-sugarman, @copy-chief |
| **execution_type** | `Agent` |
| **pattern** | EXEC-A-001 |
| **rationale** | Requer interpretação semântica para detectar triggers existentes e gerar enhancements contextuais |

---

## Purpose

Apply Joe Sugarman's 30 Psychological Triggers to existing copy to strengthen persuasion and increase conversion. This is an ENHANCEMENT task - take working copy and inject missing triggers strategically to amplify its effectiveness without creating "trigger overload."

## When to Use

- **After first draft** - Use this to strengthen copy that's already written
- **After Hopkins Audit** - Scientific fundamentals first, then psychological triggers
- **Before publishing** - Final enhancement pass
- **When copy feels weak** - Diagnose which triggers are missing
- **For optimization** - Identify trigger gaps in underperforming copy

## Sugarman's Core Philosophy

```
"If I had to pick the single most powerful force in advertising and selling—
the most important psychological trigger—I would pick honesty. When you're
the first to point out a product's flaws, people trust you about its strengths."
- Joe Sugarman, Triggers

WARNING ON OVERUSE:
- Natural copy has 15-20 triggers organically
- Forcing 25+ triggers feels manipulative
- Overkill = distrust
- Quality over quantity ALWAYS
```

## Inputs

```yaml
required:
  - copy_text: The full copy to enhance (headline, body, CTA, offer)
  - copy_type: sales_page | email | ad | landing_page | vsl_script | webinar
  - product_name: What is being sold
  - target_audience: Who this is written for

optional:
  - current_trigger_count: If known from previous audit
  - priority_triggers: Specific triggers to focus on
  - tone: conversational | professional | urgent | educational
  - word_limit: Maximum words if constrained (e.g., ad copy)
```

## Workflow

### Phase 1: Trigger Audit (Current State)

First, identify which triggers are ALREADY present in the copy.

```
TRIGGER INVENTORY:

Read through the copy and check each trigger present:

TRUST FOUNDATION (1-4):
□ 1. Honesty - Flaws acknowledged openly?
□ 2. Integrity - Promises backed by action?
□ 3. Credibility - All objections resolved?
□ 4. Authority - Expert positioning established?

INVOLVEMENT (5-7):
□ 5. Ownership - Reader imagines using product?
□ 6. Storytelling - Narrative present?
□ 7. Human Relationships - Personal connection built?

VALUE (8-11):
□ 8. Value/Proof - Worth demonstrated?
□ 9. Justify Purchase - Logical reasons given?
□ 10. Greed - Extra value/bonuses included?
□ 11. Satisfaction - Guarantee/confidence shown?

PRODUCT (12-15):
□ 12. Nature of Product - Product personality clear?
□ 13. Prospect Nature - Buyer understanding shown?
□ 14. Linking - New connected to familiar?
□ 15. Specificity - Exact numbers used?

URGENCY (16-19):
□ 16. Sense of Urgency - Time pressure?
□ 17. Instant Gratification - Quick results promised?
□ 18. Current Fads - Trends referenced?
□ 19. Timing - Relevance established?

EXCLUSIVITY (20-22):
□ 20. Exclusivity/Rarity - Limited/special?
□ 21. Desire to Belong - Community aspect?
□ 22. Desire to Collect - Series/sets?

PSYCHOLOGY (23-26):
□ 23. Curiosity - Open loops/intrigue?
□ 24. Hope - Better future painted?
□ 25. Guilt - Obligations reminded? (use sparingly)
□ 26. Familiarity - Known things referenced?

PROCESS (27-30):
□ 27. Simplicity - Easy to understand/buy?
□ 28. Consistency - Small commitment first?
□ 29. Harmonize - Agreement built?
□ 30. Mental Engagement - Reader discovers conclusions?

═══════════════════════════════════════════════════
CURRENT TRIGGER COUNT: ___/30
═══════════════════════════════════════════════════
```

### Phase 2: Gap Analysis (Missing Triggers)

Identify the COMMONLY MISSED triggers that would have the highest impact:

```
HIGH-IMPACT COMMONLY MISSED TRIGGERS:

These 5 triggers are frequently absent but easy to add:

□ #5 Reason Why (Ownership/Involvement)
  Missing: Reader can't visualize using product
  Fix: Add "Imagine..." scenarios with sensory details

□ #7 Honesty
  Missing: Only positive claims made
  Fix: Acknowledge ONE limitation, then explain why it doesn't matter

□ #14 Storytelling
  Missing: No narrative element
  Fix: Add discovery story, customer story, or origin story

□ #16 Specificity
  Missing: Round numbers, vague claims
  Fix: Replace "many customers" with "47,832 customers"

□ #26 Hope
  Missing: No future-pacing
  Fix: Paint the picture of their improved life after purchase

ANALYZE YOUR COPY:

Which of these 5 are missing?
1. ________________________
2. ________________________
3. ________________________

What other gaps exist?
4. ________________________
5. ________________________
```

### Phase 3: Strategic Trigger Injection

For each missing trigger, apply using these templates:

```
═══════════════════════════════════════════════════
TRIGGER 1: HONESTY (Foundation - HIGHEST PRIORITY)
═══════════════════════════════════════════════════

If missing, add near the beginning of copy:

INJECTION TEMPLATE:
"Now, I have to be honest with you about [one real limitation]...
[Acknowledge it openly]
But here's why that doesn't matter: [context that neutralizes the concern]"

EXAMPLE:
"I have to be honest - this course isn't for everyone. If you want
overnight results without doing the work, this won't help you.
But if you're willing to put in 30 minutes a day for 21 days,
you'll see results that last a lifetime."

PLACEMENT: Early in copy (first 20%), before main claims
IMPACT: Makes ALL subsequent claims 10x more believable

═══════════════════════════════════════════════════
TRIGGER 5: INVOLVEMENT/OWNERSHIP
═══════════════════════════════════════════════════

If missing, add in product description section:

INJECTION TEMPLATE:
"Imagine for a moment... You're [specific situation].
[Sensory detail 1 - what they see]
[Sensory detail 2 - what they feel]
[The benefit happening in real-time]"

EXAMPLE:
"Imagine waking up tomorrow morning. You check your phone and
see $847 in sales that came in while you slept. You didn't lift
a finger. That's what automated funnels can do for you."

PLACEMENT: After establishing the problem, before the offer
IMPACT: Creates mental ownership before purchase

═══════════════════════════════════════════════════
TRIGGER 6: STORYTELLING
═══════════════════════════════════════════════════

If missing, add a discovery story:

INJECTION TEMPLATE (Discovery Story):
"Let me tell you how I first discovered this...
[Setting - time and place]
[The problem I was facing]
[The unexpected encounter/discovery]
[The transformation that followed]"

EXAMPLE:
"Three years ago, I was $47,000 in debt and working 60-hour weeks.
I was at a conference, ready to leave early, when I overheard
a conversation that changed everything..."

PLACEMENT: Opening or after the problem section
IMPACT: Creates emotional bond and credibility

═══════════════════════════════════════════════════
TRIGGER 15: SPECIFICITY
═══════════════════════════════════════════════════

Convert vague claims to specific ones:

CONVERSION TABLE:
┌─────────────────────┬──────────────────────────────────────┐
│ VAGUE               │ SPECIFIC (Sugarman Style)            │
├─────────────────────┼──────────────────────────────────────┤
│ Many customers      │ 47,832 customers in 23 countries     │
│ Fast results        │ See results in 4.2 days average      │
│ Save money          │ Save $847 per year (avg customer)    │
│ Popular choice      │ 3,247 sold in last 30 days           │
│ High quality        │ 99.7% pass rate on 47-point QC       │
│ Limited time        │ Ends 11:59pm EST Friday, Jan 24      │
│ Affordable          │ $47/month (less than Netflix)        │
│ Great guarantee     │ 365-day money-back guarantee         │
│ Experienced         │ 127 combined years, 1,847 projects   │
│ Works fast          │ Average 23 minutes to first result   │
└─────────────────────┴──────────────────────────────────────┘

FIND & REPLACE all vague terms in your copy

═══════════════════════════════════════════════════
TRIGGER 21: DESIRE TO BELONG
═══════════════════════════════════════════════════

If missing, add community/belonging element:

INJECTION TEMPLATE:
"Join the [specific number] [type of people] who have already
[achieved specific result].
You'll become part of a community of [identity description]."

EXAMPLE:
"Join the 14,847 entrepreneurs who have already escaped the
9-to-5 trap. You'll become part of a community of location-
independent business owners who value freedom over everything."

PLACEMENT: Near CTA or in benefits section
IMPACT: Leverages tribal psychology

═══════════════════════════════════════════════════
TRIGGER 23: CURIOSITY
═══════════════════════════════════════════════════

If missing, add open loops:

INJECTION TEMPLATES (Seeds of Curiosity):
- "But here's what surprised me most..."
- "What happened next changed everything..."
- "And I haven't even told you the best part..."
- "Now, here's where it gets interesting..."
- "Let me explain why that matters..."

PLACEMENT: End of sections, before transitions
IMPACT: Creates irresistible forward momentum

═══════════════════════════════════════════════════
TRIGGER 24: HOPE
═══════════════════════════════════════════════════

If missing, add future-pacing:

INJECTION TEMPLATE:
"Picture yourself [timeframe] from now...
[Specific positive change 1]
[Specific positive change 2]
[How they'll feel]
This isn't fantasy. It's what happens when you [action]."

EXAMPLE:
"Picture yourself 90 days from now. You've lost 20 pounds.
You're wearing clothes that have been sitting in your closet
for years. You catch your reflection and actually smile.
This isn't fantasy. It's what happens when you follow the system."

PLACEMENT: Before final CTA
IMPACT: Creates emotional pull toward purchase
```

### Phase 4: Integration Check

After injecting triggers, verify they flow naturally:

```
INTEGRATION CHECKLIST:

□ FLOW TEST
  - Read copy aloud - does it sound natural?
  - Are trigger injections seamless or jarring?
  - Does the tone remain consistent?

□ OVERLOAD TEST
  - Total triggers present: ___/30
  - If above 22: Review for redundancy
  - If feels "salesy": Remove weakest 2-3 triggers

□ AUTHENTICITY TEST
  - Is every claim true and verifiable?
  - Does honesty trigger come BEFORE bold claims?
  - Would you be comfortable if customer saw the source?

□ BALANCE TEST
  Categories present:
  □ Trust Foundation (need at least 2/4)
  □ Involvement (need at least 2/3)
  □ Value (need at least 2/4)
  □ Product (need at least 2/4)
  □ Urgency (need at least 1/4)
  □ Exclusivity (need at least 1/3)
  □ Psychology (need at least 2/4)
  □ Process (need at least 2/4)
```

### Phase 5: Final Scoring

```
SUGARMAN TRIGGER ENHANCEMENT - FINAL SCORE

BEFORE ENHANCEMENT:
Trigger Count: ___/30
Missing Critical Triggers: ___________

AFTER ENHANCEMENT:
Trigger Count: ___/30
Triggers Added: ___________

═══════════════════════════════════════════════════
VERDICT:

□ 20-24 triggers: OPTIMAL - Persuasive without overkill
□ 15-19 triggers: GOOD - May add 2-3 more
□ 25+ triggers: CHECK FOR OVERLOAD - May feel manipulative
□ Below 15: NEEDS MORE WORK - Add high-impact triggers

CATEGORY BALANCE:
Trust:      ___/4 (minimum 2)
Involvement: ___/3 (minimum 2)
Value:      ___/4 (minimum 2)
Product:    ___/4 (minimum 2)
Urgency:    ___/4 (minimum 1)
Exclusivity: ___/3 (minimum 1)
Psychology: ___/4 (minimum 2)
Process:    ___/4 (minimum 2)
═══════════════════════════════════════════════════
```

## Outputs

### Output Format

```yaml
enhancement_summary:
  copy_type: [type enhanced]
  before_trigger_count: [X/30]
  after_trigger_count: [X/30]
  triggers_added: [list of added triggers]

gap_analysis:
  missing_critical:
    - trigger: [name]
      impact: HIGH | MEDIUM | LOW
  commonly_missed_present:
    - "#5 Reason Why: [present/added/still missing]"
    - "#7 Honesty: [present/added/still missing]"
    - "#14 Storytelling: [present/added/still missing]"
    - "#16 Specificity: [present/added/still missing]"
    - "#26 Hope: [present/added/still missing]"

injections:
  - trigger: [number and name]
    location: [where in copy]
    text_added: |
      [exact text that was added]
    impact: [expected improvement]

warnings:
  - [any concerns about overload or authenticity]

final_copy: |
  [Complete enhanced copy with triggers injected]

next_steps:
  1: [Recommended action]
  2: [Recommended action]
```

## Quick Reference: High-Impact Trigger Templates

```
HONESTY (Trigger 1):
"I have to be honest with you about [limitation]..."

INVOLVEMENT (Trigger 5):
"Imagine for a moment... You're [scenario]..."

STORYTELLING (Trigger 6):
"Let me tell you how I first discovered this..."

SPECIFICITY (Trigger 15):
[number] [specific unit] in [specific timeframe]

BELONGING (Trigger 21):
"Join the [number] [people] who have already..."

CURIOSITY (Trigger 23):
"But here's what surprised me most..."

HOPE (Trigger 24):
"Picture yourself [timeframe] from now..."
```

## Common Mistakes to Avoid

```
❌ DON'T: Add all 30 triggers
   WHY: Feels manipulative, creates distrust
   DO: Target 18-22 for optimal persuasion

❌ DON'T: Force triggers that don't fit
   WHY: Breaks flow and tone
   DO: Only add triggers that integrate naturally

❌ DON'T: Skip the honesty trigger
   WHY: It's the foundation of all credibility
   DO: Always include honesty, preferably early

❌ DON'T: Use round numbers
   WHY: Look guessed, not measured
   DO: Use specific numbers (47,832 not "about 50,000")

❌ DON'T: Add urgency without justification
   WHY: Fake scarcity destroys trust
   DO: Only use urgency if there's a real reason
```

## Sugarman's Final Words

```
"The more the mind must work to reach a conclusion successfully,
the more positive, enjoyable or stimulating the conclusion."

"Honesty + Integrity = Credibility"

"You sell on emotion, but you justify a purchase with logic."

REMEMBER:
- Triggers are tools, not tricks
- Ethical persuasion serves the buyer
- If you wouldn't want your mother to see it, don't publish it
```

## Integration

- **Precedes**: Final publication, A/B testing
- **Follows**: Hopkins Audit (scientific fundamentals first)
- **Related Checklist**: checklists/sugarman-30-triggers.md
- **Related Agent**: agents/joe-sugarman.md
- **Workflow Integration**: WF-1 Day 5, WF-6 Phase 3

## Dependencies

- Input: Existing copy draft
- Output: Enhanced copy with trigger report
- Agent: joe-sugarman (as tool, not persona)
