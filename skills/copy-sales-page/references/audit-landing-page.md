# Audit Landing Page Task

## Purpose
Comprehensive landing page audit using Alex Hormozi's conversion checklist. Get a score and specific fixes.

## When to Use
- Landing page converting below 2%
- High traffic but low conversions
- Before scaling ad spend
- After offer changes
- A/B test planning

## Inputs

```yaml
required:
  - landing_page_url: URL of the page to audit
  - product_name: What you're selling
  - price: Price point

optional:
  - current_conversion: Current conversion rate %
  - traffic_source: Where traffic comes from (ads, organic, email)
  - page_type: VSL/Long-form/Short-form/Webinar
  - target_avatar: Ideal customer description
```

## Workflow

### Step 1: Above The Fold Audit
```
CRITICAL FIRST IMPRESSION (5 seconds):

□ HEADLINE MATCH
  - Does headline match the ad that brought them?
  - Is promise crystal clear?
  Score: ___/10

□ CTA VISIBILITY
  - Can they see a CTA without scrolling?
  - Is it obvious what to do next?
  Score: ___/10

□ SOCIAL PROOF VISIBLE
  - Testimonial/logos/badges above fold?
  - Trust indicators present?
  Score: ___/10

□ LOAD SPEED
  - Loads in <2 seconds?
  - No layout shift?
  Score: ___/10

ABOVE FOLD SCORE: ___/40
```

### Step 2: Value Proposition Audit
```
IS THE OFFER CLEAR?

□ DREAM OUTCOME STATED
  - What transformation do they get?
  - Specific and measurable result?
  Score: ___/10

□ TIME TO RESULT
  - When will they see results?
  - Is timeline believable?
  Score: ___/10

□ EFFORT REQUIRED
  - How much work do they do?
  - Is it easier than alternatives?
  Score: ___/10

□ LIKELIHOOD OF SUCCESS
  - Is proof present?
  - Do they believe it works for them?
  Score: ___/10

VALUE PROPOSITION SCORE: ___/40
```

### Step 3: Trust Elements Audit
```
DO THEY BELIEVE YOU?

□ TESTIMONIALS
  - Quantity: How many?
  - Quality: Specific results mentioned?
  - Variety: Different avatars represented?
  - Format: Video/text/screenshot?
  Score: ___/10

□ AUTHORITY MARKERS
  - "As seen in" logos?
  - Certifications/credentials?
  - Media mentions?
  Score: ___/10

□ NUMBERS/PROOF
  - Customers served?
  - Results achieved?
  - Years in business?
  Score: ___/10

□ CASE STUDIES
  - Detailed transformations?
  - Before/after clear?
  - Relatable to avatar?
  Score: ___/10

TRUST SCORE: ___/40
```

### Step 4: Objection Handling Audit
```
ARE OBJECTIONS ADDRESSED?

□ FAQ SECTION
  - Top 5 objections covered?
  - Answers are reassuring, not defensive?
  Score: ___/10

□ GUARANTEE
  - Risk reversal clear?
  - Specific (not generic "satisfaction guaranteed")?
  - Better than competitors?
  Score: ___/10

□ PRICE JUSTIFICATION
  - Value stack shown?
  - ROI math present?
  - Payment options available?
  Score: ___/10

□ "IS THIS FOR ME?"
  - Ideal customer described?
  - "This is for you if..." section?
  Score: ___/10

OBJECTION HANDLING SCORE: ___/40
```

### Step 5: Urgency & Scarcity Audit
```
WHY BUY NOW?

□ DEADLINE PRESENT
  - Clear expiration?
  - Consequence of waiting?
  Score: ___/10

□ SCARCITY REAL
  - Limited quantity?
  - Limited bonuses?
  - Believable, not fake?
  Score: ___/10

□ URGENCY COPY
  - Reason for urgency explained?
  - Loss aversion triggered?
  Score: ___/10

URGENCY SCORE: ___/30
```

### Step 6: CTA Audit
```
IS ACTION OBVIOUS?

□ CTA BUTTON
  - Action verb (Get, Start, Claim)?
  - Contrasting color?
  - Multiple CTAs on page?
  Score: ___/10

□ CTA COPY
  - Benefit-focused?
  - Urgency if appropriate?
  - No generic "Submit" or "Buy Now"?
  Score: ___/10

□ FRICTION REDUCTION
  - Minimal form fields?
  - One-step checkout?
  - Mobile optimized?
  Score: ___/10

CTA SCORE: ___/30
```

### Step 7: Technical Audit
```
DOES IT WORK?

□ MOBILE EXPERIENCE
  - Fully responsive?
  - Buttons thumb-friendly?
  - No horizontal scroll?
  Score: ___/10

□ LOAD SPEED
  - Desktop <2s?
  - Mobile <3s?
  - Images optimized?
  Score: ___/10

□ TRACKING
  - Pixel installed?
  - Events firing correctly?
  - Analytics working?
  Score: ___/10

□ CHECKOUT FLOW
  - No broken links?
  - Payment works?
  - Confirmation email sends?
  Score: ___/10

TECHNICAL SCORE: ___/40
```

### Step 8: Copy Quality Audit
```
IS COPY COMPELLING?

□ HEADLINES
  - Benefit-driven?
  - Specific (numbers/results)?
  - Creates curiosity?
  Score: ___/10

□ BODY COPY
  - Speaks to avatar's pain?
  - Conversational tone?
  - Easy to scan?
  Score: ___/10

□ BULLET POINTS
  - Benefits, not features?
  - Fascination-style bullets?
  - Specific outcomes?
  Score: ___/10

□ EMOTIONAL HOOKS
  - Fear of loss present?
  - Desire amplified?
  - Status/identity addressed?
  Score: ___/10

COPY SCORE: ___/40
```

### Step 9: Generate Final Score
```
LANDING PAGE SCORECARD:

Above The Fold: ___/40
Value Proposition: ___/40
Trust Elements: ___/40
Objection Handling: ___/40
Urgency/Scarcity: ___/30
CTA: ___/30
Technical: ___/40
Copy Quality: ___/40

TOTAL SCORE: ___/300

CONVERSION POTENTIAL:
0-100: 🔴 BROKEN - Complete redesign needed
101-150: 🟠 WEAK - Major fixes required
151-200: 🟡 DECENT - Optimization needed
201-250: 🟢 GOOD - Fine-tuning
251-300: 💎 OPTIMIZED - Test & scale
```

### Step 10: Prioritized Fixes
```
TOP 5 FIXES BY IMPACT:

FIX #1: [Highest impact item]
Current: [What's wrong]
Should Be: [What to change]
Expected Lift: +X% conversion

FIX #2: ...
FIX #3: ...
FIX #4: ...
FIX #5: ...

QUICK WINS (15 min each):
1.
2.
3.

A/B TEST IDEAS:
1. [Element to test]
2. [Element to test]
3. [Element to test]
```

## Output

```yaml
format: markdown
sections:
  - page_summary
  - section_scores (8 sections)
  - total_score_diagnosis
  - prioritized_fixes
  - quick_wins
  - ab_test_recommendations
```

## Conversion Benchmarks

| Page Type | Bad | Average | Good | Great |
|-----------|-----|---------|------|-------|
| Cold Traffic LP | <1% | 1-2% | 2-5% | >5% |
| Warm Traffic LP | <3% | 3-5% | 5-10% | >10% |
| Checkout Page | <30% | 30-50% | 50-70% | >70% |
| VSL Page | <1% | 1-3% | 3-5% | >5% |

## Common LP Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Headline doesn't match ad | -50% conv | Exact headline match |
| No CTA above fold | -30% conv | Add CTA in first screen |
| Generic guarantee | -20% conv | Specific performance guarantee |
| No urgency | -25% conv | Add real deadline |
| Slow load (>3s) | -7% per second | Optimize images, hosting |
| Weak social proof | -40% conv | Add testimonials with results |

---

*Task Version: 1.0*
*Primary Framework: $100M Leads LP Checklist (Alex Hormozi)*
