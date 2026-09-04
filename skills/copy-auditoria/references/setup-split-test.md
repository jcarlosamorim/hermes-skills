# Setup Split Test - Hopkins Methodology

## Purpose

Create scientifically valid A/B tests using Claude Hopkins' pioneering methodology. Hopkins invented split testing in the early 1900s using coded coupons. This task applies his rigorous principles to modern testing with digital tracking.

## When to Use

- Before scaling any campaign (validate winner first)
- When team disagrees on copy approach (test, don't debate)
- To optimize existing campaigns systematically
- When launching new copy/offer variations
- Before making significant creative changes

## Hopkins on Testing

```
"Almost any question can be answered, cheaply, quickly and finally,
by a test campaign. And that's the way to answer them - not by
arguments around a table. Go to the court of last resort - the
buyers of your product."

"Don't argue around a table. Test in the marketplace."

"The compass of accurate knowledge directs the shortest,
safest, cheapest course."
```

## Inputs

```yaml
required:
  - test_element: What to test (headline | offer | price | cta | copy_length | image | format)
  - control_version: Current/baseline version
  - test_hypothesis: What you believe will perform better and WHY
  - primary_metric: What defines success (CTR | conversion | AOV | revenue)

optional:
  - secondary_metrics: Additional metrics to track
  - test_duration: How long to run (or sample size needed)
  - traffic_source: Where traffic comes from
  - segment: Specific audience segment to test
  - previous_test_results: Learnings from past tests
```

## Hopkins' Testing Principles

### Principle 1: One Variable at a Time

```
ISOLATION RULE:

Hopkins: "Change ONE thing at a time. Otherwise you don't know
what caused the difference."

CORRECT TEST SETUP:
┌─────────────────────────────────────────────────────────┐
│ CONTROL                      │ VARIATION               │
├─────────────────────────────────────────────────────────┤
│ Same ad copy                 │ Same ad copy            │
│ Same offer                   │ Same offer              │
│ Same placement               │ Same placement          │
│ HEADLINE A                   │ HEADLINE B              │ ← ONLY difference
│ Same CTA                     │ Same CTA                │
│ Same image                   │ Same image              │
└─────────────────────────────────────────────────────────┘

INCORRECT TEST SETUP (INVALID):
┌─────────────────────────────────────────────────────────┐
│ CONTROL                      │ VARIATION               │
├─────────────────────────────────────────────────────────┤
│ Headline A                   │ Headline B              │
│ Offer: 20% off               │ Offer: Free shipping    │ ← Multiple changes!
│ Red CTA button               │ Green CTA button        │
│ Product image                │ Lifestyle image         │
└─────────────────────────────────────────────────────────┘
If variation wins, you don't know which change caused it!
```

### Principle 2: Test Hypotheses, Not Random Ideas

```
HYPOTHESIS-DRIVEN TESTING:

Hopkins didn't randomly test. He formed hypotheses based on:
1. Salesmanship principles
2. Consumer psychology understanding
3. Previous test learnings
4. Market observations

WEAK TEST HYPOTHESIS:
"Let's try a different headline"
(No reasoning, no learning regardless of outcome)

STRONG TEST HYPOTHESIS:
"Headlines that call out a specific audience will outperform
generic headlines because Hopkins proved that 'the purpose of
a headline is to pick out people you can interest.'"

HYPOTHESIS TEMPLATE:
"We believe [CHANGE] will [IMPROVE METRIC] because [REASONING
BASED ON PRINCIPLE]. If correct, this teaches us [LEARNING].
If wrong, this teaches us [ALTERNATIVE LEARNING]."
```

### Principle 3: Coded Tracking (Attribution)

```
HOPKINS' INNOVATION: CODED COUPONS

In 1907, Hopkins invented attribution tracking:
- Different department codes for different ads
- "Dept. A" = Headline version A
- "Dept. B" = Headline version B
- "Dept. 1" = New York Tribune
- "Dept. 2" = Chicago Daily

Combined code: "Dept. A-1" = Headline A in NY Tribune

MODERN EQUIVALENTS:

┌─────────────────────────────────────────────────────────┐
│ HOPKINS (1907)         │ MODERN (2024)                 │
├─────────────────────────────────────────────────────────┤
│ Dept. code on coupon   │ UTM parameters                │
│ Different mail address │ Dedicated landing pages       │
│ Phone extension        │ Unique phone numbers          │
│ Coded order form       │ Promo codes                   │
│ Keyed ad (corner mark) │ Pixel tracking                │
└─────────────────────────────────────────────────────────┘

TRACKING CODE STRUCTURE:
utm_source = traffic_source (facebook, google, email)
utm_medium = format (cpc, banner, email)
utm_campaign = test_name (headline_test_jan24)
utm_content = variation (headline_a, headline_b)
```

### Principle 4: Statistical Significance

```
HOPKINS: "Don't stop a test too early. Let the market speak clearly."

SAMPLE SIZE REQUIREMENTS:

For 95% confidence, 80% power, detecting 20% lift:
- 2% baseline conversion: ~2,000 visitors per variation
- 5% baseline conversion: ~800 visitors per variation
- 10% baseline conversion: ~400 visitors per variation

MINIMUM RUNTIME:
- At least 1 full business cycle (7 days minimum)
- Account for day-of-week variations
- Don't call winner on statistical noise

SIGNIFICANCE CHECKLIST:
□ Sample size met for both variations?
□ Runtime covers full week?
□ No external factors during test? (holiday, outage, competitor)
□ Statistical calculator confirms 95%+ confidence?
```

## Workflow

### Step 1: Define the Test

```yaml
test_specification:
  test_name: [descriptive_name]
  test_id: [unique_id_for_tracking]

  element_tested: [headline | offer | cta | price | etc.]

  control:
    description: [Current version]
    tracking_code: [utm_content=control or code_a]

  variation:
    description: [New version to test]
    tracking_code: [utm_content=variation or code_b]

  hypothesis: |
    We believe [CHANGE] will [IMPROVE METRIC] because [REASONING].

  primary_metric: [What defines winner]
  secondary_metrics:
    - [Additional metric 1]
    - [Additional metric 2]

  success_criteria: |
    Variation wins if [X% improvement] with [Y% confidence]
```

### Step 2: Prepare Tracking

```
TRACKING SETUP CHECKLIST:

□ CONTROL VERSION
  UTM String: ?utm_source=___&utm_medium=___&utm_campaign=___&utm_content=control
  Landing URL: _______________
  Coupon Code: _______________
  Phone/Extension: _______________

□ VARIATION VERSION
  UTM String: ?utm_source=___&utm_medium=___&utm_campaign=___&utm_content=variation
  Landing URL: _______________
  Coupon Code: _______________
  Phone/Extension: _______________

□ TRACKING VERIFICATION
  - Analytics receiving data? [Y/N]
  - Conversions tracking properly? [Y/N]
  - No tracking conflicts? [Y/N]
  - Test traffic split working? [Y/N]
```

### Step 3: Calculate Required Sample Size

```
SAMPLE SIZE CALCULATOR:

Current conversion rate: ____%
Minimum detectable effect: ____% (how much lift to detect)
Confidence level: 95% (standard)
Power: 80% (standard)

QUICK REFERENCE:
┌────────────────┬─────────────┬────────────────────────────┐
│ Baseline Conv. │ Detect 20%  │ Required Per Variation     │
├────────────────┼─────────────┼────────────────────────────┤
│ 1%             │ 1.2%        │ ~16,000                    │
│ 2%             │ 2.4%        │ ~8,000                     │
│ 3%             │ 3.6%        │ ~5,300                     │
│ 5%             │ 6.0%        │ ~3,200                     │
│ 10%            │ 12.0%       │ ~1,600                     │
│ 20%            │ 24.0%       │ ~800                       │
└────────────────┴─────────────┴────────────────────────────┘

Required sample per variation: _______
Estimated daily traffic: _______
Estimated test duration: _______ days
```

### Step 4: Document Control and Variation

```
ELEMENT: HEADLINE TEST EXAMPLE

┌─────────────────────────────────────────────────────────────┐
│ CONTROL (A)                                                 │
├─────────────────────────────────────────────────────────────┤
│ "Discover Our Revolutionary New System"                     │
│                                                             │
│ Tracking: utm_content=headline_control                      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ VARIATION (B)                                               │
├─────────────────────────────────────────────────────────────┤
│ "To Parents Whose Children Struggle With Math:              │
│  47 Proven Techniques Used by MIT Tutors"                   │
│                                                             │
│ Tracking: utm_content=headline_specific_audience            │
└─────────────────────────────────────────────────────────────┘

HYPOTHESIS:
Specific audience callout + number specificity will outperform
generic headline because Hopkins proved "the purpose of a headline
is to pick out people you can interest."

WHAT WE'LL LEARN:
If B wins: Audience-specific headlines perform better for this product
If A wins: This audience responds better to curiosity/mystery
```

### Step 5: Launch and Monitor

```
TEST LAUNCH CHECKLIST:

□ PRE-LAUNCH
  - Both versions live and working?
  - Tracking verified on both?
  - Traffic split configured correctly (50/50)?
  - Team notified not to change anything during test?
  - Calendar blocked for test duration?

□ DURING TEST (Daily Check)
  Date: ___________

  Control:
  - Visitors: _____
  - Conversions: _____
  - Conversion Rate: ____%

  Variation:
  - Visitors: _____
  - Conversions: _____
  - Conversion Rate: ____%

  Current Lift: ____%
  Statistical Confidence: ____%
  Sample Size Reached: [Y/N]

  Anomalies/Notes: _________________

□ STOPPING RULES
  STOP EARLY IF:
  - Technical error detected
  - Massive quality issue (>50% conversion drop)
  - External event invalidates test

  DO NOT STOP EARLY IF:
  - One version "looks" like it's winning (wait for significance)
  - Getting impatient
  - Stakeholder pressure
```

### Step 6: Analyze Results

```
FINAL ANALYSIS TEMPLATE:

TEST: [Test Name]
DURATION: [Start Date] to [End Date]
ELEMENT TESTED: [What was tested]

RESULTS:
┌─────────────────────────────────────────────────────────────┐
│ METRIC              │ CONTROL      │ VARIATION    │ LIFT   │
├─────────────────────────────────────────────────────────────┤
│ Visitors            │ _____        │ _____        │        │
│ Conversions         │ _____        │ _____        │        │
│ Conversion Rate     │ _____%       │ _____%       │ ____% │
│ Revenue             │ $_____       │ $_____       │ ____% │
│ AOV                 │ $_____       │ $_____       │ ____% │
└─────────────────────────────────────────────────────────────┘

STATISTICAL VALIDITY:
- Sample size sufficient? [Y/N]
- Confidence level: ____%
- Is result statistically significant? [Y/N]

WINNER: [Control / Variation / Inconclusive]

LEARNING:
What does this tell us about our audience?
_________________________________________________

NEXT TEST:
Based on this result, what should we test next?
_________________________________________________
```

### Step 7: Document and Scale

```
TEST DOCUMENTATION:

Hopkins: "Such agencies become storehouses of advertising experiences,
proved principles and methods."

TEST ARCHIVE ENTRY:

Test ID: [ID]
Date: [Date range]
Element: [What was tested]

HYPOTHESIS:
[What we believed would happen and why]

RESULT:
[What actually happened]

LEARNING:
[What this teaches us for future tests]

IMPLEMENTATION:
□ Winner implemented as new control
□ Results shared with team
□ Learning added to swipe file
□ Next test identified
```

## Testing Priority Framework

```
WHAT TO TEST (Hopkins Priority Order):

1. HEADLINES (HIGHEST IMPACT)
   Hopkins: "Headlines can change results by 500%+"
   Test: Multiple angles, specificity levels, audience callouts

2. OFFERS (HIGH IMPACT)
   Test: Price points, bonuses, guarantees, payment terms

3. LEAD/OPENING (MEDIUM-HIGH IMPACT)
   Test: Story vs direct, problem vs solution lead

4. PROOF ELEMENTS (MEDIUM IMPACT)
   Test: Testimonial placement, type, specificity

5. CTA (MEDIUM IMPACT)
   Test: Copy, color, placement, urgency elements

6. COPY LENGTH (MEDIUM IMPACT)
   Hopkins often found long copy won
   Test: Short vs long for your specific product

7. IMAGES (LOWER IMPACT FOR DIRECT RESPONSE)
   Test: Product vs lifestyle, with vs without
```

## Common Testing Mistakes

```
MISTAKES HOPKINS WOULD CONDEMN:

1. "We tested it, variation lost by 0.1%"
   → 0.1% is statistical noise, not a real result

2. "We ran the test for 2 days"
   → Not enough data, day-of-week effects ignored

3. "We changed the headline AND the offer AND the image"
   → Multiple variables = no valid learning

4. "The new version 'feels' better"
   → Feelings don't matter, data does

5. "We're scaling the winner to all channels"
   → Test may not replicate in different context

6. "The expert/client prefers version A"
   → "Don't argue around a table. Test in the marketplace."
```

## Outputs

### Output Format

```yaml
test_plan:
  test_name: [Name]
  test_id: [ID]
  hypothesis: [What we believe and why]

  setup:
    control:
      description: [Current version]
      tracking: [Codes/UTMs]
    variation:
      description: [Test version]
      tracking: [Codes/UTMs]

  metrics:
    primary: [Main success metric]
    secondary: [List]

  requirements:
    sample_size_per_variation: [Number]
    minimum_runtime: [Days]
    traffic_split: [50/50]

  success_criteria: |
    Winner if [X% lift] at [Y% confidence]

  learnings_expected:
    if_variation_wins: [What we learn]
    if_control_wins: [What we learn]

  next_test_candidates:
    - [What to test next based on result]
```

## Hopkins' Final Word

```
"We cannot go after thousands until we learn how to win one.
So our first ads are sent to sample sections. We test our
undertaking, and test the things we offer. We start on a small
scale, and feel our way."

Test small → Learn → Scale what works

"The man who does twice the testing makes twice the progress."
```

## Integration

- **Precedes**: Scale/rollout decisions
- **Follows**: audit-copy-hopkins.md (validate copy quality first)
- **Related**: hopkins-audit-checklist.md
