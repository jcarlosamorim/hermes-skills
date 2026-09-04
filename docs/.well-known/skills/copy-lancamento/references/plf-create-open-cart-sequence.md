# Task: Create Open Cart Sequence

> **Framework**: Product Launch Formula (Jeff Walker)
> **Agent**: @jeff-walker
> **Phase**: Open Cart
> **Output**: Complete open cart email sequence and daily strategy

---

## Purpose

Create the complete Open Cart sequence of emails that drive sales during the launch window. This phase is where all the prelaunch work converts into revenue through strategic urgency and social proof.

---

## Prerequisites

- [ ] PLC sequence completed
- [ ] Launch stack finalized
- [ ] Sales page live (or ready)
- [ ] Checkout working and tested
- [ ] Cart dates confirmed
- [ ] Testimonials/social proof ready

---

## Workflow Steps

### Step 1: Gather Context

**Elicit from user:**
```
1. How many days is your cart open? (3-7 typical)
2. Cart open date/time: ___
3. Cart close date/time: ___
4. Do you have a fast action bonus? What's the deadline?
5. How many emails per day do you want? (2-4)
6. Do you have buyer testimonials from previous launches?
7. Will you do live events during cart? (webinar, Q&A)
```

### Step 2: Design Cart Sequence Architecture

**Standard 5-day sequence:**

| Day | Focus | Emails | Primary Trigger |
|-----|-------|--------|-----------------|
| Day 1 | LAUNCH | 2-3 | Events, Social Proof |
| Day 2 | Social Proof | 2 | Social Proof, Trust |
| Day 3 | Objections | 2 | Trust, Authority |
| Day 4 | Stories | 2 | Community, Likability |
| Day 5 | CLOSE | 3-4 | Scarcity, Urgency |

**Reference:**
- `data/plf/timeline-reference-kb.yaml`
- `checklists/plf/open-cart-sequence.md`

### Step 3: Create Day 1 Emails (Cart Open)

**Use template:**
- `templates/plf/open-cart-day1-tmpl.md`

**Email 1: "Doors Are Open" (morning)**
- Announce cart is open
- Recap transformation
- Link to sales page
- Fast action bonus (if applicable)

**Email 2: "Inside Look" (midday)**
- Behind the scenes
- What they get
- First buyer stories (if available)

**Email 3: "Day 1 Recap" (evening)**
- Excitement building
- Social proof numbers
- FAQ answered
- Tomorrow teaser

### Step 4: Create Middle Days (Days 2-4)

**Day 2: Social Proof Focus**
- Email 1: Case study spotlight
- Email 2: "X people joined" update

**Day 3: Objection Handling**
- Email 1: "The #1 question I'm getting"
- Email 2: Risk reversal (guarantee focus)

**Day 4: Stories & Connection**
- Email 1: Your "why" story
- Email 2: Student transformation story

**Reference:**
- `data/plf/copy-swipes-kb.yaml`
- `templates/plf/case-study-tmpl.md`

### Step 5: Create Final Day Emails (Cart Close)

**Use template:**
- `templates/plf/open-cart-final-tmpl.md`

**Email 1: "Last Day" (morning)**
- Clear deadline reminder
- What they'll miss
- Final recap of offer

**Email 2: "Hours Left" (afternoon)**
- Countdown intensifies
- Last chance positioning
- Direct appeal

**Email 3: "Final Call" (2 hours before close)**
- Maximum urgency
- Clear deadline
- Simple CTA

**Email 4: "Closing Now" (30 min before)**
- Last chance
- Final push
- Countdown

**Email 5: "Closed" (after close)**
- Thank buyers
- Acknowledge fence-sitters
- "Next time" positioning

### Step 6: Create Subject Line Variations

**For each email, create 2-3 options:**

| Email | Option A | Option B | Option C |
|-------|----------|----------|----------|
| Open | "It's time" | "[NAME], doors open" | "🚀 We're live" |
| Social Proof | "X joined" | "This just happened" | "Wow..." |
| Objection | "Your question" | "I need to address..." | "Quick answer" |
| Close | "[X] hours left" | "Closing tonight" | "Last chance" |

**Reference:**
- `templates/plf/email-subject-lines-tmpl.md`
- `data/plf/email-benchmarks-kb.yaml`

### Step 7: Map Daily Tasks

**Launch Commander schedule:**

| Day | Morning | Midday | Afternoon | Evening |
|-----|---------|--------|-----------|---------|
| 1 | Send Open | Send Inside | - | Send Recap |
| 2 | Send Proof | - | Send Update | - |
| 3 | Send Objection | - | Send Guarantee | - |
| 4 | Send Story | - | Send Student | - |
| 5 | Send Last | Send Hours | Send Final | Send Close |

**Reference:**
- `checklists/plf/launch-day-execution.md`

### Step 8: Create Social Proof Updates

**Real-time proof templates:**
```
"X people have joined [PRODUCT] in the last X hours!"

"Just got this message from [NAME]: '[QUOTE]'"

"The momentum is incredible - X new members today alone."
```

### Step 9: Plan Live Events (Optional)

**If doing live events during cart:**
- Day 1: Launch celebration/walkthrough
- Day 3: Live Q&A
- Day 5: Final Q&A before close

### Step 10: Validate Sequence

**Run checklist:**
- `checklists/plf/open-cart-sequence.md`

**Quality checks:**
- [ ] Every email has single clear CTA
- [ ] Urgency builds progressively
- [ ] Social proof integrated
- [ ] Objections addressed
- [ ] Final day has 3+ emails
- [ ] Post-close email ready

---

## Deliverables

1. **Complete Email Sequence**
   - All emails for each day
   - Subject line variations
   - Sending times

2. **Subject Line Matrix**
   - 2-3 options per email
   - A/B test recommendations

3. **Social Proof Templates**
   - Real-time update copy
   - Testimonial integration

4. **Launch Day Schedule**
   - Hour-by-hour plan
   - Task assignments
   - Contingency notes

5. **Cart Close Sequence**
   - Final day emails
   - Post-close communication

---

## Success Criteria

- [ ] Email open rates: 25-35%
- [ ] Click rates: 3-8%
- [ ] Conversion: 2-10% of engaged list
- [ ] Final day: 30-50% of total sales
- [ ] No complaints about spam
- [ ] Cart closes on time (no extension)

---

## Email Timing Best Practices

**Day 1 (Launch):**
- 8-9 AM: Doors open
- 12-1 PM: Inside look
- 7-8 PM: Day recap

**Middle Days:**
- 8-10 AM: Main email
- 4-6 PM: Follow-up

**Final Day:**
- 8 AM: Last day
- 12 PM: Hours left
- 6 PM: Final call
- 9 PM: Closing (if close at 11:59)
- 11:30 PM: Last chance
- 12:05 AM: Closed

---

## Next Steps

After open cart sequence complete:
→ `tasks/plf/create-sales-page-plf.md` - Ensure page ready
→ `checklists/plf/launch-day-execution.md` - Day-of checklist
→ `tasks/plf/diagnose-failed-launch.md` - If needed post-launch

---

## References

### Templates
- `templates/plf/open-cart-day1-tmpl.md`
- `templates/plf/open-cart-final-tmpl.md`
- `templates/plf/email-subject-lines-tmpl.md`

### Checklists
- `checklists/plf/open-cart-sequence.md`
- `checklists/plf/launch-day-execution.md`

### Knowledge Bases
- `data/plf/copy-swipes-kb.yaml`
- `data/plf/email-benchmarks-kb.yaml`
- `data/plf/timeline-reference-kb.yaml`

---

*Task Version: 1.0*
*Framework: Product Launch Formula - Open Cart Sequence*
