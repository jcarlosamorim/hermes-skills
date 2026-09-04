# Task: Create PLF Sales Page

> **Framework**: Product Launch Formula (Jeff Walker)
> **Agent**: @jeff-walker
> **Phase**: Sales Page Creation
> **Output**: Complete sales page following PLF principles

---

## Purpose

Create a sales page that naturally follows from the PLC sequence. Unlike traditional long-form sales letters, PLF sales pages assume the prospect has already consumed prelaunch content and is primed to buy.

---

## PLF Sales Page Philosophy

> "Your sales page is NOT where you make the sale.
> The sale happens during the prelaunch.
> The sales page is where they complete the transaction." - Jeff Walker

**Key difference from traditional sales pages:**
- Shorter (prospect is already educated)
- Focused on offer details and logistics
- Heavy on social proof
- Clear next steps

---

## Prerequisites

- [ ] PLC sequence complete
- [ ] Launch stack finalized
- [ ] Testimonials ready
- [ ] Checkout integrated
- [ ] Template ready: `templates/plf/sales-page-blueprint-tmpl.md`
- [ ] Reference: `checklists/plf/sales-page-plf.md`

---

## Inputs Required

```yaml
product_name: ""
headline_promise: ""
core_transformation: ""
price: ""
payment_plan: ""
guarantee: ""
cart_close_date: ""
testimonials: []
modules: []
bonuses: []
urgency_elements: []
```

---

## Workflow

### Phase 1: Page Architecture

#### Step 1.1: PLF Sales Page Structure

Unlike traditional 10,000+ word sales letters:

```
1. Hero Section (Above the Fold)
   - Headline (transformation-focused)
   - Subheadline (who it's for)
   - CTA button
   - Social proof element

2. Video/Recap Section
   - Brief PLC recap video OR
   - Text summary of journey
   - "You're ready" positioning

3. Who This Is For
   - Ideal customer description
   - "This is for you if..."
   - "This is NOT for you if..."

4. The Offer Stack
   - Core product details
   - Module breakdown
   - Bonuses
   - Total value
   - Price

5. Testimonials/Proof
   - Video testimonials (if available)
   - Written testimonials
   - Case study summaries
   - Numbers/stats

6. Guarantee Section
   - Clear guarantee terms
   - How it works
   - Confidence statement

7. FAQ Section
   - Top questions
   - Objection handling

8. Final CTA
   - Urgency reminder
   - CTA button
   - Scarcity element

9. Footer
   - Support contact
   - Legal links
```

---

### Phase 2: Hero Section

#### Step 2.1: Headline Formula

**PLF Headline Approaches:**

**Transformation Focus:**
```
"Finally [ACHIEVE RESULT] Without [COMMON OBSTACLE]"

"The Complete System for [TRANSFORMATION] in [TIMEFRAME]"

"How to [RESULT] Even If [OBJECTION]"
```

**Ownership Focus:**
```
"Your Journey to [RESULT] Starts Here"

"Everything You Need to [ACHIEVE GOAL]"

"Welcome to [PRODUCT NAME]"
```

**Social Proof Focus:**
```
"Join [NUMBER] People Who Have [RESULT]"

"The Proven Method [NUMBER] People Trust"
```

#### Step 2.2: Subheadline

```
"For [AVATAR] who want to [RESULT]
without [PAIN/OBSTACLE]"

"The step-by-step system for going from
[CURRENT STATE] to [DESIRED STATE]"
```

#### Step 2.3: Hero CTA

```
Button: "Join [PRODUCT] Now"
Below: "Cart closes [DATE] at [TIME]"
```

---

### Phase 3: Offer Stack Section

#### Step 3.1: Stack Presentation

```markdown
## Everything You Get Inside [PRODUCT]

### The Core Program (Value: R$X,XXX)

✓ **Module 1: [NAME]**
  [One-line benefit]

✓ **Module 2: [NAME]**
  [One-line benefit]

✓ **Module 3: [NAME]**
  [One-line benefit]

✓ **Module 4: [NAME]**
  [One-line benefit]

---

### BONUS #1: [NAME] (Value: R$XXX)
[Brief description and benefit]

### BONUS #2: [NAME] (Value: R$XXX)
[Brief description and benefit]

### BONUS #3: [NAME] (Value: R$XXX)
[Brief description and benefit]

---

**Total Value: R$X,XXX**

**Your Investment Today: R$XXX**

[CTA BUTTON]

*Or X payments of R$XX*
```

---

### Phase 4: Social Proof Section

#### Step 4.1: Testimonial Display

**Video Testimonials (Best):**
- 3-5 video testimonials
- 60-120 seconds each
- Specific results mentioned
- Diverse perspectives

**Written Testimonials:**
```
"[SPECIFIC RESULT QUOTE]"

[Full Name], [Title/Location]
[Before context → After result]
```

#### Step 4.2: Testimonial Selection Criteria

- [ ] Specific, measurable results
- [ ] Relatable to target avatar
- [ ] Addresses common objections
- [ ] Includes name and photo
- [ ] Permission obtained

#### Step 4.3: Results Statistics

```
"[PRODUCT] by the Numbers"

✓ X students enrolled
✓ X% average [METRIC] improvement
✓ X countries represented
✓ X combined [RESULT]
```

---

### Phase 5: FAQ Section

#### Step 5.1: Essential FAQs

**Logistics:**
- How long do I have access?
- How is it delivered?
- When do I get access?
- What if I need help?

**Objections:**
- What if it doesn't work for me?
- I've tried other things before...
- I don't have time...
- Is this right for my situation?

**Purchase:**
- Is there a payment plan?
- What's your refund policy?
- Can I pay by [method]?
- Is it secure?

#### Step 5.2: FAQ Format

```
**Q: [Question]?**

[Answer in 2-4 sentences. Be helpful and honest.
Address the real concern behind the question.]
```

---

### Phase 6: Urgency & Scarcity Section

#### Step 6.1: Deadline Display

```
⚠️ IMPORTANT: Cart Closes [DATE] at [TIME] [TIMEZONE]

After that, [PRODUCT] will not be available.

[COUNTDOWN TIMER]

[CTA BUTTON]
```

#### Step 6.2: What They'll Miss

```
"When the cart closes, you'll lose access to:
✗ [CORE PRODUCT]
✗ [BONUS 1]
✗ [BONUS 2]
✗ [BONUS 3]
✗ The [SPECIAL OFFER] pricing"
```

---

### Phase 7: Technical Implementation

#### Step 7.1: Page Elements

**Required:**
- [ ] Responsive design
- [ ] Fast loading (<3 seconds)
- [ ] Working CTAs
- [ ] Checkout integration
- [ ] Analytics tracking

**Recommended:**
- [ ] Exit intent (optional)
- [ ] Live chat (optional)
- [ ] Countdown timer
- [ ] Trust badges
- [ ] Testimonial slider

#### Step 7.2: Mobile Optimization

- [ ] Readable on mobile
- [ ] Buttons tap-friendly
- [ ] Videos play correctly
- [ ] No horizontal scroll
- [ ] Forms work on mobile

#### Step 7.3: Checkout Integration

- [ ] CTA → Checkout seamless
- [ ] Payment options clear
- [ ] Guarantee visible
- [ ] Support contact available

---

### Phase 8: Validation

#### Step 8.1: Quality Checklist

Apply: `checklists/plf/sales-page-plf.md`

**Key checks:**
- [ ] Headline is transformation-focused
- [ ] Stack complete and valued
- [ ] Social proof sufficient
- [ ] FAQs address objections
- [ ] Guarantee clear
- [ ] Technical working
- [ ] Copy quality high

#### Step 8.2: Pre-Launch Testing

- [ ] All links work
- [ ] Checkout completes
- [ ] Mobile tested
- [ ] Multiple browsers
- [ ] Timer accurate
- [ ] Videos play

---

## Outputs

### Primary Output
```
outputs/launches/{product}/sales-page/
├── copy/
│   ├── headline-variations.md
│   ├── full-page-copy.md
│   ├── stack-section.md
│   ├── testimonials.md
│   └── faq-section.md
├── design/
│   ├── wireframe.md
│   └── visual-specs.md
├── technical/
│   ├── page-requirements.md
│   └── tracking-setup.md
└── validation-report.md
```

---

## PLF vs Traditional Sales Page

| Element | Traditional | PLF |
|---------|-------------|-----|
| Length | 10,000+ words | 2,000-4,000 words |
| Education | Heavy | Light (done in PLCs) |
| Proof | Extensive | Featured |
| Story | Long | Brief recap |
| Urgency | Created | Natural (cart close) |
| Purpose | Sell | Close |

---

## Jeff's Wisdom

> "By the time they get to your sales page, they should
> already be sold. The page is just the final details."

> "Make it easy. Clear headline, clear offer, clear CTA.
> Don't make them think."

> "Testimonials do the heavy lifting on your sales page.
> Let your customers sell for you."

---

## Common Mistakes

1. **Too long** - PLF sales pages are shorter
2. **Repeating PLC content** - They've already seen it
3. **Weak stack presentation** - Make value crystal clear
4. **Hidden guarantee** - Make it prominent
5. **Confusing CTAs** - One clear action
6. **Slow page** - Speed kills conversions

---

## Handoff

After sales page complete:
→ `tasks/plf/create-open-cart-sequence.md` (link in emails)
→ `checklists/plf/launch-day-execution.md` (final checks)

---

*Task Version: 1.0*
*Framework: Product Launch Formula - Sales Page*
