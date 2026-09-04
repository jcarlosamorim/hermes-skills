# Create Close Script Task

## Purpose
Generate sales closing scripts using Alex Hormozi's frameworks. Handle objections, close deals.

## When to Use
- Building a sales team
- Training closers
- Low close rate on calls
- Need to handle objections better
- Selling high-ticket offers ($1k+)

## Inputs

```yaml
required:
  - product_name: What you're selling
  - price: Price point
  - offer_summary: What they get
  - main_objections: Top 3 objections you hear

optional:
  - call_type: Setter/Closer/One-call close
  - call_length: Typical call duration
  - guarantee: Guarantee offered
  - payment_options: Payment plans available
  - qualification_criteria: What makes a good lead
```

## Workflow

### Step 1: Call Framework Selection
```
SELECT CALL TYPE:

□ ONE-CALL CLOSE (Simple offer, <$2k)
  Duration: 30-45 min
  Structure: Discover → Pitch → Close

□ SETTER + CLOSER (High-ticket, >$5k)
  Setter: 15-20 min (qualify + book)
  Closer: 45-60 min (full presentation)

□ STRATEGY CALL (Consultative)
  Duration: 60-90 min
  Structure: Audit → Prescription → Close
```

### Step 2: Opening Framework
```
OPENING SCRIPT (First 2 minutes):

"Hey [Name], this is [Your Name] from [Company].
Before we dive in, I just want to set some expectations.

I'm going to ask you some questions to understand your situation.
Then I'll share what we do and how it might help.
And if it makes sense for both of us, we can talk about working together.
If it doesn't make sense, I'll tell you that too.

Sound fair?"

[Wait for confirmation]

"Great. So tell me, what made you book this call today?"
```

### Step 3: Discovery Framework (V.A.C.A.)
```
V - VALIDATE THE PROBLEM

"Tell me about [problem area]..."
"How long has this been going on?"
"What have you tried before?"
"Why didn't that work?"

A - AMPLIFY THE PAIN

"What's this costing you?"
"What happens if nothing changes?"
"How does this affect [other area]?"
"On a scale 1-10, how urgent is solving this?"

C - CONFIRM THE DESIRE

"In a perfect world, what would [outcome] look like?"
"If you had [result], what would that mean for you?"
"What's the deadline for achieving this?"

A - ASSESS READINESS

"Are you the decision maker?"
"If we can solve this, are you ready to move forward today?"
"What would need to happen for you to say yes?"
```

### Step 4: Presentation Framework
```
PITCH STRUCTURE:

1. RECAP THEIR SITUATION
"So just to make sure I understand...
You're dealing with [problem].
You've tried [previous attempts] but they didn't work because [reason].
And what you really want is [dream outcome].
Did I get that right?"

2. INTRODUCE THE SOLUTION
"Based on what you've shared, here's how we can help..."
[Present offer focusing on their specific pain points]

3. VALUE STACK
"Here's everything you get:
- [Core deliverable] - normally worth $X
- [Bonus 1] - worth $Y
- [Bonus 2] - worth $Z
Total value: $[sum]"

4. PRICE DROP
"The investment for all of this is not $[anchor price].
It's just $[actual price]."

5. GUARANTEE
"And to make this a complete no-brainer,
[explain guarantee in detail]."

6. URGENCY
"The only caveat is [scarcity/urgency element]."
```

### Step 5: Objection Handling (V.A.C.A. Framework)
```
FRAMEWORK: VALIDATE → ASK → COUNTER → ASK FOR SALE

OBJECTION: "I need to think about it"

VALIDATE: "I totally understand. This is a big decision."

ASK: "Just so I understand - when you say you need to think about it,
what specifically are you thinking about?"

[Listen for real objection]

COUNTER: [Address the real objection]

ASK FOR SALE: "So if we can [solve that], are you ready to move forward?"

---

OBJECTION: "It's too expensive"

VALIDATE: "I hear you. Price is definitely important."

ASK: "Help me understand - is it that you don't have the money,
or you're not sure it's worth the investment?"

[If not sure it's worth it]:
"What would the result we discussed be worth to you?"
"If you could guarantee [outcome], what would you pay for that?"

[If don't have money]:
"What could you do to make this happen?"
"Do you have access to credit?"
"We do have payment options - would $X/month work?"

---

OBJECTION: "I need to talk to my spouse/partner"

VALIDATE: "Of course. Smart decisions are made together."

ASK: "When you talk to them, what do you think they'll say?"

[If they'll say yes]:
"Great! Why don't we get them on the phone right now?"

[If they'll have concerns]:
"What concerns do you think they'll have?"
[Address those concerns]
"If you can address those concerns, do YOU want to do this?"

---

OBJECTION: "I've been burned before"

VALIDATE: "I'm really sorry to hear that. That's frustrating."

ASK: "What happened?"

[Listen to their story]

COUNTER: "The difference with us is [differentiator].
Plus, we have [guarantee] so you're protected."

ASK FOR SALE: "Does that give you enough confidence to move forward?"
```

### Step 6: Closing Sequences
```
CLOSE #1: ASSUMPTIVE CLOSE
"Great! Let's get you started. Do you prefer to pay in full or use the payment plan?"

CLOSE #2: ALTERNATIVE CLOSE
"Would you like to start with [Option A] or [Option B]?"

CLOSE #3: URGENCY CLOSE
"The [bonus/price/spots] is only available until [deadline].
Should we lock in your spot now?"

CLOSE #4: TAKEAWAY CLOSE
"Based on what you've shared, I'm not actually sure this is right for you.
[Pause]
Why do you feel it would be a good fit?"

CLOSE #5: INVERSION CLOSE
"What would need to happen for you to say yes right now?"
[Give them what they ask for if possible]
"Done. So we're good to go?"

CLOSE #6: PUPPY DOG CLOSE
"Why don't you try it for [trial period] with our guarantee.
If it's not everything I promised, you get every penny back.
What do you have to lose?"
```

### Step 7: Payment Handling
```
PAYMENT SCRIPT:

"Perfect! Let's get you set up.
I'm going to send you a link to complete your order.

[Send link]

Can you confirm you received it?

Great. I'll stay on the line while you complete it.
Let me know when you're on the confirmation page."

[If hesitation]
"Is there something stopping you from completing this right now?"
[Handle final objection]

[On confirmation]
"Congratulations! Welcome to [program/company].
Here's what happens next..."
```

### Step 8: Post-Close Protocol
```
AFTER THE SALE:

1. REINFORCE THE DECISION
"You made a great decision today.
Here's why this is going to work for you..."

2. PREVENT BUYER'S REMORSE
"Over the next 24-48 hours, you might have doubts.
That's totally normal. When that happens, [reassurance]."

3. SET EXPECTATIONS
"Here's exactly what you can expect:
- [Immediate access/delivery]
- [First 24 hours]
- [First week]
- [First 30 days]"

4. NEXT STEPS
"Your immediate next step is [specific action].
Can you do that in the next [time]?"
```

## Output

```yaml
format: markdown
sections:
  - call_framework_overview
  - opening_script
  - discovery_questions
  - presentation_script
  - objection_scripts (per objection)
  - closing_sequences
  - payment_handling
  - post_close_protocol
```

## Call Metrics Targets

| Metric | Target | Red Flag |
|--------|--------|----------|
| Show Rate | >70% | <50% |
| Close Rate (Qualified) | >30% | <15% |
| Average Call Length | 45-60 min | <30 min |
| Cash Collected | >60% in full | <40% |
| Refund Rate | <10% | >15% |

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Pitching too early | -50% close | Complete discovery first |
| Not handling "think about it" | -30% close | Dig for real objection |
| Weak urgency | -25% close | Add real deadline |
| Not asking for sale | -40% close | Always ask directly |
| Giving up after 1 no | -20% close | Average close takes 5 asks |

---

*Task Version: 1.0*
*Primary Framework: $100M Closing Playbook (Alex Hormozi)*
