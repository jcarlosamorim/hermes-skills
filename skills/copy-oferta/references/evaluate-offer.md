# Evaluate Offer Task

**Task ID:** evaluate-offer
**Version:** 2.0.0
**Category:** Offer Optimization / Audit
**Minimum Output:** Complete scorecard with prioritized fixes
**Primary Methodology:** Hormozi Value Equation + Kennedy Direct Response Principles
**Research Source:** docs/research/offer-evaluation-methodology-research.md

---

## Purpose

Perform a comprehensive audit of any offer using the Value Equation framework and Grand Slam Offer criteria. Generate a numerical score (0-100) and prioritized improvement recommendations.

**The Problem:** Most offers fail not because of bad products, but because of poor offer construction. Symptoms include:
- "Too expensive" objections despite competitive pricing
- "Need to think about it" killing momentum
- Prospects comparing you to cheaper alternatives
- Low conversion rates despite good traffic
- High refund rates after purchase

**The Solution:** A systematic evaluation using proven frameworks that diagnoses EXACTLY what's weak and provides a prioritized fix list.

---

## When to Use

### Primary Triggers
- Conversion rate below 5% (traffic to purchase)
- "Need to think about it" exceeds 50% of prospects
- Price objections dominate sales conversations
- Preparing to invest in paid traffic
- Planning to raise prices
- Launching a new product/service
- Conversion has dropped without explanation

### Secondary Triggers
- Annual offer review
- Competitive pressure increasing
- Refund rate above 5%
- Customer acquisition cost rising
- Market conditions changing

---

## Inputs Required

```yaml
required:
  offer_name: "Nome do produto/serviço"
  offer_description: "Descrição clara do que é oferecido"
  price: "Preço atual"
  target_avatar: "Cliente ideal (quem compra)"
  primary_outcome: "Resultado principal prometido"

recommended:
  current_conversion_rate: "Taxa de conversão atual (visitantes para compradores)"
  average_sales_cycle: "Tempo médio para decisão de compra"
  main_objections: "Top 3 objeções que você ouve"
  guarantee: "Garantia atual (se existir)"
  value_stack: "Lista de tudo que está incluído"
  competitor_prices: "Preços dos principais concorrentes"
  testimonials_available: "Quantos depoimentos com resultados específicos você tem"

optional:
  sales_page_url: "Link para página de vendas"
  cost_to_deliver: "Custo para entregar"
  refund_rate: "Taxa de reembolso atual"
  time_to_result: "Tempo até o cliente ver resultado"
  bonuses: "Bônus incluídos atualmente"
  urgency_element: "Escassez ou urgência atual"
```

---

## Theoretical Foundation

### The Value Equation (Alex Hormozi)

The foundational framework for understanding why people buy:

```
                 Dream Outcome × Perceived Likelihood
Value = ──────────────────────────────────────────────────
              Time Delay × Effort & Sacrifice
```

**Key Insight:** You can increase value by:
1. Making the outcome more desirable (numerator)
2. Making success more likely (numerator)
3. Decreasing time to result (denominator)
4. Decreasing effort required (denominator)

Most offers only try to improve the numerator. **Grand Slam Offers aggressively minimize the denominator.**

### Grand Slam Offer Definition

> "An offer so good that people feel stupid saying no."
> — Alex Hormozi

Five required components:
1. **Starving Crowd** - Market that desperately wants what you sell
2. **Irresistible Offer** - Value stack perceived at 10x+ the price
3. **Unique Mechanism** - Proprietary system that explains why it works
4. **Risk Reversal** - Guarantee that removes all customer risk
5. **Urgency/Scarcity** - Real reason to act now

### Dan Kennedy's Offer Rules

Every strong offer must have:
1. A specific, clear offer (not just product info)
2. A reason to respond NOW
3. Clear instructions on how to respond
4. Tracking and measurement capability
5. Strong sales copy

---

## Workflow: Complete Offer Audit

### Phase 1: Information Gathering

#### Step 1.1: Collect Basic Offer Information

```yaml
gather_basics:
  - Offer name and description
  - Current price point
  - Target customer profile
  - Primary outcome promised
  - Time to achieve result
  - Effort required from customer
  - Current guarantee (if any)
  - Value stack components
  - Urgency/scarcity elements
  - Available social proof
```

#### Step 1.2: Collect Performance Data (If Available)

```yaml
gather_performance:
  - Traffic to page (monthly)
  - Conversion rate (visitors to buyers)
  - Average sales cycle length
  - Refund/chargeback rate
  - Customer lifetime value
  - Top objections heard
  - Win/loss rate on sales calls
  - Competitor comparison frequency
```

#### Step 1.3: Identify Current Positioning

```yaml
positioning_assessment:
  questions:
    - "How do prospects find you?"
    - "What do they compare you to?"
    - "What makes you different?"
    - "Why do people choose you over alternatives?"
    - "Why do people NOT choose you?"
```

---

### Phase 2: Value Equation Scoring

#### Step 2.1: Score Dream Outcome (0-10)

**DREAM OUTCOME** = The ultimate result your customer desires

**Scoring Criteria:**

| Score | Description |
|-------|-------------|
| 1-2 | Vague outcome, hard to visualize |
| 3-4 | Somewhat defined but not compelling |
| 5-6 | Clear outcome, moderate desirability |
| 7-8 | Specific, measurable, highly desirable |
| 9-10 | Crystal clear, life-changing, status-elevating |

**Evaluation Questions:**

```yaml
dream_outcome_audit:
  specificity:
    question: "Can the customer visualize the EXACT result?"
    weak_example: "Improve your marketing"
    strong_example: "Add $50K/month in recurring revenue"

  measurability:
    question: "Can progress be measured objectively?"
    weak_example: "Feel better about your business"
    strong_example: "Reduce customer churn from 8% to 2%"

  desirability:
    question: "Is this a MUST-HAVE or nice-to-have?"
    weak_example: "Learn new skills"
    strong_example: "Finally quit your 9-5 and go full-time"

  status_change:
    question: "Does achieving this change how they're seen?"
    weak_example: "Have a better website"
    strong_example: "Become the go-to expert in your market"

  emotional_pull:
    question: "Does it connect to deep desires/fears?"
    weak_example: "Increase efficiency"
    strong_example: "Never worry about making payroll again"
```

**Red Flags (Score 1-4):**
- Generic benefit claims
- No specific numbers or timeframes
- Outcome sounds like everyone else
- Hard to explain to a friend

**Green Flags (Score 7-10):**
- Specific, measurable result
- Clear timeframe
- Identity/status transformation
- Emotional resonance
- Unique angle or approach

**DREAM OUTCOME SCORE: ___/10**

---

#### Step 2.2: Score Perceived Likelihood of Achievement (0-10)

**PERCEIVED LIKELIHOOD** = Customer's belief they will actually get the result

**Scoring Criteria:**

| Score | Description |
|-------|-------------|
| 1-2 | No proof, skepticism expected |
| 3-4 | Some claims, minimal evidence |
| 5-6 | Decent testimonials, basic guarantee |
| 7-8 | Strong proof, good guarantee, clear method |
| 9-10 | Overwhelming proof, bold guarantee, proven system |

**Evaluation Questions:**

```yaml
likelihood_audit:
  proof_quantity:
    question: "How many success stories exist?"
    weak: "0-5 testimonials"
    adequate: "6-20 testimonials"
    strong: "20+ testimonials with specific results"

  proof_quality:
    question: "How specific are the results in testimonials?"
    weak: "Great product! Loved it."
    adequate: "Helped me improve my business"
    strong: "Went from $3K to $47K/month in 90 days"

  proof_variety:
    question: "Are there different types of proof?"
    checklist:
      - Written testimonials
      - Video testimonials
      - Case studies
      - Before/after documentation
      - Media features
      - Celebrity/expert endorsements
      - Statistics and data

  mechanism_clarity:
    question: "Is there a clear explanation of WHY this works?"
    weak: "Our proven system"
    strong: "The RMBC Method: Research, Mechanism, Brief, Copy"

  guarantee_strength:
    question: "How much risk does the customer take?"
    weak: "No guarantee or satisfaction only"
    adequate: "30-day money-back"
    strong: "90-day results guarantee with additional compensation"
```

**Proof Strength Hierarchy:**
1. Unsubstantiated claims (weakest)
2. Generic testimonials
3. Specific testimonials
4. Video testimonials
5. Case studies with numbers
6. Third-party verification
7. Celebrity/expert endorsements
8. Media features
9. Independent research (strongest)

**PERCEIVED LIKELIHOOD SCORE: ___/10**

---

#### Step 2.3: Score Time Delay (0-10, then INVERT)

**TIME DELAY** = How long until the customer achieves the dream outcome

**Note:** Score the TIME, then invert (10 - score) for final calculation because LOWER time delay = HIGHER value.

**Scoring Criteria (Raw Time Score):**

| Score | Description |
|-------|-------------|
| 1-2 | Results in hours to days |
| 3-4 | Results in 1-2 weeks |
| 5-6 | Results in 1-2 months |
| 7-8 | Results in 3-6 months |
| 9-10 | Results in 6+ months or unclear |

**Evaluation Questions:**

```yaml
time_audit:
  quick_win:
    question: "Is there a result in the first 24-48 hours?"
    weak: "No early wins, just foundational work"
    strong: "First template delivered, first call scheduled"

  total_timeline:
    question: "How long to the PRIMARY promised result?"
    ask: "What's your realistic timeline to [outcome]?"

  progress_visibility:
    question: "Can customers see progress along the way?"
    weak: "Results come at the end"
    strong: "Weekly milestones, dashboards, check-ins"

  speed_vs_competitors:
    question: "Faster or slower than alternatives?"
    weak: "Slower than DIY or competitors"
    strong: "Fastest path to result in the market"
```

**TIME DELAY RAW SCORE: ___/10**
**TIME DELAY INVERTED (10 - raw): ___/10**

---

#### Step 2.4: Score Effort & Sacrifice (0-10, then INVERT)

**EFFORT & SACRIFICE** = What the customer must do/give up to get results

**Note:** Score the EFFORT, then invert (10 - score) for final calculation because LOWER effort = HIGHER value.

**Scoring Criteria (Raw Effort Score):**

| Score | Description |
|-------|-------------|
| 1-2 | Almost nothing required, done for you |
| 3-4 | Minimal effort, clear steps |
| 5-6 | Moderate effort, guided process |
| 7-8 | Significant work required |
| 9-10 | Major lifestyle change, complex process |

**Evaluation Questions:**

```yaml
effort_audit:
  work_required:
    question: "How much does the customer actually DO?"
    done_for_you: "We handle everything, you just review"
    done_with_you: "We guide you, you execute with support"
    do_it_yourself: "Here's the training, go implement"

  sacrifices:
    question: "What must they give up?"
    none: "No lifestyle changes required"
    minimal: "Few hours per week"
    significant: "Major time, money, or comfort trade-offs"

  complexity:
    question: "How easy is it to follow?"
    simple: "Step 1, Step 2, Step 3 - foolproof"
    moderate: "Some decisions, but guided"
    complex: "Multi-variable, requires judgment"

  obstacles_addressed:
    question: "Are common blockers pre-solved?"
    not_addressed: "Customer figures out obstacles"
    partially: "Some solutions provided"
    fully_addressed: "Every common obstacle has a built-in solution"

  tools_provided:
    question: "What tools/templates reduce effort?"
    none: "Start from scratch"
    some: "Basic templates"
    comprehensive: "Done-for-you templates, tools, automation"
```

**EFFORT RAW SCORE: ___/10**
**EFFORT INVERTED (10 - raw): ___/10**

---

#### Step 2.5: Calculate Value Equation Score

```
VALUE EQUATION SCORE CALCULATION:

Dream Outcome:                    ___/10 × 0.30 = ___
Perceived Likelihood:             ___/10 × 0.30 = ___
Time Delay (inverted):            ___/10 × 0.20 = ___
Effort & Sacrifice (inverted):    ___/10 × 0.20 = ___

VALUE EQUATION TOTAL:             ___/10
(Multiply by 4 for 40-point scale: ___/40)
```

---

### Phase 3: Grand Slam Components Audit

#### Step 3.1: Market Quality Assessment (0-5)

```yaml
market_audit:
  pain_urgency:
    question: "How urgent is the problem you solve?"
    score_1: "Nice to have, no urgency"
    score_3: "Important but not critical"
    score_5: "Burning pain, must solve NOW"

  purchasing_power:
    question: "Can your market afford your solution?"
    score_1: "Struggling financially"
    score_3: "Can afford with consideration"
    score_5: "Has budget and authority"

  market_accessibility:
    question: "Can you reach them efficiently?"
    score_1: "Fragmented, hard to find"
    score_3: "Identifiable but scattered"
    score_5: "Concentrated, easy to reach"

  growth_trajectory:
    question: "Is this market growing?"
    score_1: "Shrinking or saturated"
    score_3: "Stable"
    score_5: "Growing rapidly"
```

**MARKET QUALITY SCORE: ___/5**

---

#### Step 3.2: Value Stack Assessment (0-5)

**The 10x Rule:** Perceived value should be at least 10x the price.

```yaml
value_stack_audit:
  itemization:
    question: "Is every component clearly listed with value?"
    score_1: "Just a product/service name"
    score_3: "Some components listed"
    score_5: "Complete itemized stack with dollar values"

  value_multiple:
    question: "What's the perceived value to price ratio?"
    score_1: "Less than 3x"
    score_3: "3-5x"
    score_5: "10x or more"

  standalone_value:
    question: "Do components have value alone?"
    score_1: "Only valuable as bundle"
    score_3: "Some standalone value"
    score_5: "Each item valuable independently"

  variety:
    question: "Are there different types of value?"
    checklist:
      - Core deliverable
      - Templates/tools
      - Training/education
      - Community/support
      - 1-on-1 access
      - Done-for-you elements
```

**VALUE STACK SCORE: ___/5**

---

#### Step 3.3: Unique Mechanism Assessment (0-5)

```yaml
mechanism_audit:
  named_system:
    question: "Does your methodology have a unique name?"
    score_1: "No named approach"
    score_3: "Generic name like 'Our System'"
    score_5: "Proprietary, memorable name (e.g., 'The RMBC Method')"

  differentiation:
    question: "Does it clearly differ from competitors?"
    score_1: "Sounds the same"
    score_3: "Somewhat different"
    score_5: "Clearly unique approach"

  explanation:
    question: "Is there a clear 'why this works' story?"
    score_1: "No explanation"
    score_3: "Basic reasoning"
    score_5: "Compelling, logical explanation"

  curiosity:
    question: "Does it create 'I need to know more' feeling?"
    score_1: "No curiosity"
    score_3: "Some interest"
    score_5: "Strong desire to learn the method"
```

**UNIQUE MECHANISM SCORE: ___/5**

---

#### Step 3.4: Risk Reversal Assessment (0-5)

```yaml
guarantee_audit:
  existence:
    question: "Is there a guarantee?"
    score_0: "No guarantee"
    score_2: "Basic satisfaction guarantee"
    score_5: "Bold performance guarantee"

  strength:
    question: "How much risk does customer take?"
    hierarchy:
      - No guarantee (score 1)
      - Satisfaction guarantee (score 2)
      - Money-back guarantee (score 3)
      - Extended money-back 90+ days (score 4)
      - Performance-based or better-than-money-back (score 5)

  specificity:
    question: "Is it specific or generic?"
    generic: "100% satisfaction guaranteed"
    specific: "If you don't add $10K in 90 days, full refund plus $500"

  competitor_comparison:
    question: "Better than competitors?"
    worse: "Shorter or weaker than alternatives"
    same: "Industry standard"
    better: "Boldest guarantee in the market"
```

**RISK REVERSAL SCORE: ___/5**

---

#### Step 3.5: Urgency/Scarcity Assessment (0-5)

```yaml
urgency_audit:
  existence:
    question: "Is there any urgency element?"
    score_0: "None"
    score_3: "Some deadline or limit"
    score_5: "Strong, real urgency"

  authenticity:
    question: "Is the scarcity REAL?"
    fake: "Always says 'only 3 left' but never runs out"
    real: "Verifiable limit that's enforced"

  consequence:
    question: "Is there a clear cost of waiting?"
    weak: "Price stays the same if you wait"
    strong: "Price goes up, bonus expires, spots fill"

  types_present:
    checklist:
      - Quantity limit (cohort size, inventory)
      - Deadline (doors close date)
      - Price increase (goes up tomorrow)
      - Bonus expiration (only this week)
      - Seasonal/event-based
```

**URGENCY/SCARCITY SCORE: ___/5**

---

#### Step 3.6: Calculate Grand Slam Score

```
GRAND SLAM COMPONENTS CALCULATION:

Market Quality:       ___/5
Value Stack:          ___/5
Unique Mechanism:     ___/5
Risk Reversal:        ___/5
Urgency/Scarcity:     ___/5

GRAND SLAM TOTAL:     ___/25
```

---

### Phase 4: Enhancement Stack Audit (S.U.B.G.N.)

#### Step 4.1: Scarcity Deep Dive (0-5)

```yaml
scarcity_audit:
  presence:
    question: "Is there a quantity limit?"
    examples:
      - "Only 10 spots in this cohort"
      - "Limited edition (100 made)"
      - "First 50 customers only"

  authenticity:
    question: "Would you really turn away a customer at the limit?"
    fake: "No, we'd take more money"
    real: "Yes, capacity is truly limited"

  communication:
    question: "Is it clearly communicated?"
    weak: "Mentioned once in small print"
    strong: "Prominent, repeated, visualized (spots remaining counter)"
```

**SCARCITY SCORE: ___/5**

---

#### Step 4.2: Urgency Deep Dive (0-5)

```yaml
urgency_audit:
  deadline_presence:
    question: "Is there a clear deadline?"
    examples:
      - "Doors close Friday at midnight"
      - "Price increases on [date]"
      - "Enrollment ends in 48 hours"

  deadline_enforcement:
    question: "Is the deadline actually enforced?"
    fake: "Extended or reopened regularly"
    real: "Absolutely enforced, no exceptions"

  consequence_clarity:
    question: "What happens if they miss the deadline?"
    weak: "Same offer available later"
    strong: "Price increases $500 / lose bonus / waitlist"
```

**URGENCY SCORE: ___/5**

---

#### Step 4.3: Bonuses Deep Dive (0-5)

```yaml
bonuses_audit:
  quantity:
    question: "How many bonuses are included?"
    weak: "0-1 bonuses"
    adequate: "2-3 bonuses"
    strong: "4+ valuable bonuses"

  relevance:
    question: "Do bonuses solve real obstacles?"
    weak: "Random add-ons"
    strong: "Each bonus addresses a specific barrier"

  value_communication:
    question: "Are individual values listed?"
    weak: "Plus bonuses!"
    strong: "Bonus 1: [Name] - Value $297"

  exclusivity:
    question: "Are bonuses exclusive or available elsewhere?"
    weak: "Available as separate products"
    strong: "Only available with this offer"
```

**BONUSES SCORE: ___/5**

---

#### Step 4.4: Guarantees Deep Dive (0-5)

(Already covered in Phase 3, but add depth here)

```yaml
guarantee_depth:
  boldness:
    question: "How bold is the guarantee?"
    standard: "30-day money-back"
    bold: "90-day + keep the bonuses"
    extreme: "Double your money back if no result"

  conditions:
    question: "Are there limiting conditions?"
    many_conditions: "Must complete X, Y, Z to qualify"
    no_conditions: "Unconditional refund, no questions"

  length:
    question: "How long is the guarantee period?"
    short: "14-30 days"
    standard: "60 days"
    long: "90+ days or lifetime"
```

**GUARANTEES SCORE: ___/5**

---

#### Step 4.5: Naming Deep Dive (0-5)

```yaml
naming_audit:
  result_in_name:
    question: "Does the name contain the outcome?"
    weak: "Marketing Course"
    strong: "$100K Launch Blueprint"

  timeframe_in_name:
    question: "Does the name suggest speed?"
    weak: "Business Program"
    strong: "90-Day Revenue Accelerator"

  memorability:
    question: "Is it unique and memorable?"
    generic: "Marketing Mastery"
    memorable: "The Midnight Profit Method"

  curiosity_factor:
    question: "Does it create 'what is that?' reaction?"
    weak: "Comprehensive Training"
    strong: "The Invisible Selling Machine"
```

**NAMING SCORE: ___/5**

---

#### Step 4.6: Calculate Enhancement Stack Score

```
ENHANCEMENT STACK (S.U.B.G.N.) CALCULATION:

S - Scarcity:         ___/5
U - Urgency:          ___/5
B - Bonuses:          ___/5
G - Guarantees:       ___/5
N - Naming:           ___/5

ENHANCEMENT TOTAL:    ___/25
```

---

### Phase 5: Red Flags Detection

#### Step 5.1: Identify Active Red Flags

```yaml
red_flags_checklist:
  price_objections:
    flag: "'Too expensive' is frequent objection"
    present: Yes/No
    deduction: -2 if yes
    signal: "Value not communicated effectively"

  think_about_it:
    flag: "'Need to think about it' exceeds 50%"
    present: Yes/No
    deduction: -2 if yes
    signal: "Low perceived value or trust"

  competitor_comparison:
    flag: "Prospects constantly compare to competitors"
    present: Yes/No
    deduction: -2 if yes
    signal: "Commodity positioning"

  ghosting:
    flag: "Prospects ghost after receiving proposal"
    present: Yes/No
    deduction: -2 if yes
    signal: "Trust problem or wrong market"

  discount_requests:
    flag: "Frequently asked for discounts"
    present: Yes/No
    deduction: -2 if yes
    signal: "Price-value disconnect"
```

**RED FLAGS PRESENT: ___/5**
**TOTAL DEDUCTION: ___/10**

---

### Phase 6: Final Score Calculation

```
╔══════════════════════════════════════════════════════════════╗
║                    OFFER SCORECARD                           ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  SECTION A: VALUE EQUATION                        ___/40     ║
║    - Dream Outcome (×0.30×4):           ___                  ║
║    - Perceived Likelihood (×0.30×4):    ___                  ║
║    - Time Delay inverted (×0.20×4):     ___                  ║
║    - Effort inverted (×0.20×4):         ___                  ║
║                                                              ║
║  SECTION B: GRAND SLAM COMPONENTS                 ___/25     ║
║    - Market Quality:                    ___/5                ║
║    - Value Stack:                       ___/5                ║
║    - Unique Mechanism:                  ___/5                ║
║    - Risk Reversal:                     ___/5                ║
║    - Urgency/Scarcity:                  ___/5                ║
║                                                              ║
║  SECTION C: ENHANCEMENT STACK (S.U.B.G.N.)        ___/25     ║
║    - Scarcity:                          ___/5                ║
║    - Urgency:                           ___/5                ║
║    - Bonuses:                           ___/5                ║
║    - Guarantees:                        ___/5                ║
║    - Naming:                            ___/5                ║
║                                                              ║
║  SECTION D: RED FLAGS DEDUCTION                   -___/10    ║
║    - Red flags present:                 ___/5                ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  FINAL SCORE: A + B + C - D =                     ___/100    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

### Phase 7: Diagnosis & Recommendations

#### Step 7.1: Score Interpretation

```yaml
diagnosis_matrix:
  0-30:
    rating: "BROKEN"
    emoji: "🔴"
    meaning: "Offer needs complete rebuild"
    action: "Don't spend on traffic until fixed"
    priority: "Redesign from scratch using Grand Slam framework"

  31-50:
    rating: "WEAK"
    emoji: "🟠"
    meaning: "Major structural problems"
    action: "Significant restructuring required"
    priority: "Fix value equation fundamentals first"

  51-70:
    rating: "DECENT"
    emoji: "🟡"
    meaning: "Working but underperforming"
    action: "Optimization will yield strong returns"
    priority: "Strengthen weakest components"

  71-85:
    rating: "GOOD"
    emoji: "🟢"
    meaning: "Solid offer with fine-tuning opportunities"
    action: "A/B test enhancements"
    priority: "Test pricing, guarantees, bonuses"

  86-100:
    rating: "GRAND SLAM"
    emoji: "💎"
    meaning: "Exceptional offer"
    action: "Scale traffic, protect positioning"
    priority: "Document what works, scale carefully"
```

#### Step 7.2: Generate Prioritized Fix List

**Priority Calculation:** Impact × Ease

```yaml
fix_priority_matrix:
  high_impact_easy:
    priority: 1
    examples:
      - "Add specific numbers to outcome claims"
      - "Name your methodology"
      - "Extend guarantee period"
      - "Add real deadline"
      - "Itemize value stack with dollars"

  high_impact_hard:
    priority: 2
    examples:
      - "Rebuild value stack completely"
      - "Add case studies/testimonials"
      - "Change pricing model"
      - "Reposition to different market"

  low_impact_easy:
    priority: 3
    examples:
      - "Minor copy tweaks"
      - "Add small bonus"
      - "Design improvements"

  low_impact_hard:
    priority: 4
    examples:
      - "Complete rebrand"
      - "New technology platform"
      - "Major operational changes"
```

---

## Output Format

```yaml
deliverables:
  executive_summary:
    - "Offer name and current state"
    - "Overall score and diagnosis"
    - "Top 3 critical issues"
    - "Recommended next steps"

  detailed_scorecard:
    - "Section A: Value Equation breakdown"
    - "Section B: Grand Slam components breakdown"
    - "Section C: Enhancement stack breakdown"
    - "Section D: Red flags identified"
    - "Final score calculation"

  diagnosis:
    - "Score interpretation"
    - "What's working well"
    - "What's holding the offer back"
    - "Market and competitive context"

  prioritized_fixes:
    - "Fix #1: [Highest priority]"
    - "Fix #2: [Second priority]"
    - "Fix #3: [Third priority]"
    - "Quick wins list (implement today)"

  implementation_roadmap:
    - "Week 1 actions"
    - "Week 2-4 actions"
    - "Month 2+ actions"
    - "Testing recommendations"
```

---

## Quality Checklist

### Pre-Audit Validation
```yaml
before_starting:
  - [ ] Have all required inputs
  - [ ] Know current conversion rate (if available)
  - [ ] Understand the target market
  - [ ] Have access to sales data/objections
  - [ ] Know competitor landscape
```

### Post-Audit Validation
```yaml
before_delivering:
  - [ ] All sections scored
  - [ ] Math is correct
  - [ ] Diagnosis matches score
  - [ ] Fixes are prioritized by impact × ease
  - [ ] Recommendations are actionable
  - [ ] Quick wins are truly quick
```

---

## Common Problems & Solutions Quick Reference

| Symptom | Likely Weak Area | Quick Fix |
|---------|-----------------|-----------|
| "Too expensive" | Value Stack | Add itemized value with dollar amounts |
| "Need to think" | Perceived Likelihood | Add case studies, strengthen guarantee |
| "What's included?" | Value Communication | Create explicit value stack |
| "Does it work for me?" | Proof | Add testimonials from similar customers |
| "Takes too long" | Time Delay | Add 24-48 hour quick win |
| "Too complicated" | Effort Required | Add done-for-you elements |
| "Sounds like X competitor" | Unique Mechanism | Name and explain your proprietary method |
| "What if it doesn't work?" | Guarantee | Create bold, specific risk reversal |
| "I'll think about it" | Urgency | Add real deadline with consequence |

---

## Copywriter Recommendations

| Score Range | Recommended Expert | Focus Area |
|-------------|-------------------|------------|
| 0-30 (Broken) | Strategic rebuild first | Don't write copy, fix offer |
| 31-50 (Weak) | @dan-kennedy | Restructure with direct response |
| 51-70 (Decent) | @alex-hormozi | Optimize value equation |
| 71-85 (Good) | @gary-bencivenga | Strengthen proof and credibility |
| 86-100 (Grand Slam) | @david-ogilvy | Polish and scale |

---

## Integration with Other Tasks

### Tasks That Feed This One
- `avatar-research.md` - Understanding customer desires
- `copysearch.md` - Competitive intelligence
- `build-authority-arsenal.md` - Gathering proof

### Tasks This Feeds
- `create-offer.md` - If rebuild is needed
- `create-sales-page.md` - After offer is optimized
- `create-headlines.md` - Using improved value prop

---

## Performance Benchmarks

After implementing fixes, track:

```yaml
improvement_metrics:
  conversion_rate:
    measure: "Visitors to buyers"
    good_improvement: "20% increase"
    great_improvement: "50% increase"
    grand_slam: "100%+ increase"

  sales_cycle:
    measure: "Time from first contact to purchase"
    good_improvement: "20% reduction"
    great_improvement: "50% reduction"

  objection_frequency:
    measure: "% of conversations with price objections"
    good_improvement: "Reduced by half"
    great_improvement: "Rarely occurs"

  refund_rate:
    measure: "% of purchases refunded"
    good: "Below 5%"
    great: "Below 3%"
    grand_slam: "Below 1%"
```

---

## Research Foundation

This task is based on comprehensive research documented in:
`docs/research/offer-evaluation-methodology-research.md`

### Primary Sources
- Alex Hormozi - "$100M Offers" (Value Equation, Grand Slam framework)
- Dan Kennedy - "No B.S. Direct Marketing" (10 Rules, Offer Construction)
- Dan Kennedy - "Magnetic Marketing" methodology
- MECLABS - Value Proposition Assessment Framework

### Theoretical Foundations
- Robert Cialdini - Persuasion psychology (scarcity, social proof)
- Eugene Schwartz - Mechanism and awareness levels
- Kahneman & Tversky - Loss aversion in pricing

---

*Task Version: 2.0.0*
*Last Updated: 2026-01-23*
*Primary Framework: Hormozi Value Equation + Kennedy Direct Response*
*Minimum Output: Complete scorecard with prioritized fixes*
