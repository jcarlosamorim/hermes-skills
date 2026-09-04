# Audit Copy - Hopkins Scientific Method

## Purpose

Scientific copy audit based on Claude Hopkins' principles from "Scientific Advertising" (1923). This is the FINAL audit gate before any copy goes live. Hopkins invented the rigorous, measurable approach to advertising that separates profitable copy from expensive guessing.

## When to Use

- **ALWAYS** - As the final checkpoint before publishing ANY copy
- Before A/B testing (validate fundamentals first)
- When copy is converting but you don't know why
- When copy isn't converting and you need diagnosis
- Before scaling ad spend on a winner
- When team disagrees on copy direction (data beats opinions)

## Hopkins' Core Audit Principles

```
"The only purpose of advertising is to make sales.
It is profitable or unprofitable according to its actual sales."
- Claude Hopkins, Scientific Advertising

AUDIT PHILOSOPHY:
1. Every claim must be provable
2. Every element must be testable
3. Every result must be measurable
4. Specificity beats generality ALWAYS
5. Service sells, pitching repels
```

## Inputs

```yaml
required:
  - copy_text: The full copy to audit (headline, body, CTA, offer)
  - copy_type: sales_page | email | ad | landing_page | vsl_script
  - product_name: What is being sold
  - target_audience: Who this is written for

optional:
  - current_metrics: CTR, conversion rate, AOV if available
  - tracking_codes: Existing UTMs or coupon codes
  - test_history: Previous versions tested
  - competitor_copy: What competitors are saying
```

## Workflow

### Phase 1: Salesmanship Test

Hopkins said: "Advertising is salesmanship. Its principles are the principles of salesmanship."

```
SALESMANSHIP AUDIT:

Would a salesperson say this face-to-face?

□ CONVERSATIONAL TONE
  - Reads like one person talking to another?
  - No corporate speak or jargon?
  - Could be spoken aloud naturally?
  Score: ___/10

  FAIL EXAMPLES:
  - "Leveraging synergies to optimize outcomes" (corporate)
  - "We are excited to announce" (no one talks like this)
  - "Solutions for your needs" (vague and generic)

  PASS EXAMPLES:
  - "Here's how to save $847 on your next order"
  - "I want to show you something that took me 3 years to figure out"
  - "You know that feeling when..."

□ SINGLE READER FOCUS
  - Written to ONE specific person?
  - Uses "you" more than "we/our/us"?
  - Addresses THEIR situation specifically?
  Score: ___/10

  Hopkins: "Don't think of people in the mass.
  That gives you a blurred view."

□ SELF-INTEREST ALIGNMENT
  - 100% focused on reader's benefit?
  - No self-congratulation about company?
  - Answers "What's in it for me?"
  Score: ___/10

  Hopkins: "Remember the people you address are selfish,
  as we all are. They care nothing about your interests or profit."

□ SELLING NOT ENTERTAINING
  - Purpose is conversion, not applause?
  - No clever wordplay that obscures message?
  - Entertainment value serves the sale?
  Score: ___/10

  Hopkins: "Ads are not written to entertain.
  Entertainment seekers are rarely the people you want."

SALESMANSHIP SCORE: ___/40
```

### Phase 2: Reason Why Audit

Hopkins said: "If a claim is worth making, make it in the most impressive way - by explaining WHY."

```
REASON WHY AUDIT:

Does every claim have a "Because..."?

□ CLAIM INVENTORY
  List all claims made in copy:

  Claim 1: _______________________
  Reason Why: ____________________
  Proof: ________________________

  Claim 2: _______________________
  Reason Why: ____________________
  Proof: ________________________

  Claim 3: _______________________
  Reason Why: ____________________
  Proof: ________________________

  (Continue for all claims)

□ REASON WHY COMPLETENESS
  - Every claim has explanation of WHY it's true?
  - Process/mechanism is revealed?
  - Reader can verify or understand the logic?
  Score: ___/10

  FAIL: "Our product is the purest"
  PASS: "We filter through 7 stages, including reverse osmosis at 0.0001 microns,
         removing 99.97% of contaminants - here's the lab report"

□ SCHLITZ PRINCIPLE APPLIED
  - Processes everyone does are EXPLAINED as if unique?
  - Common practices made interesting through detail?
  - "Behind the scenes" revealed?
  Score: ___/10

  Hopkins' Schlitz insight: Every brewery purified their beer.
  Hopkins explained HOW Schlitz did it (live steam, 245°).
  Result: 5th place to tied for 1st.

□ DIFFERENTIATION THROUGH EXPLANATION
  - Copy shows WHY this is different (not just claims it)?
  - Reader understands the mechanism?
  - Uniqueness is credible and specific?
  Score: ___/10

REASON WHY SCORE: ___/40
```

### Phase 3: Specificity Audit

Hopkins said: "Platitudes and generalities roll off the human understanding like water from a duck."

```
SPECIFICITY AUDIT:

Are claims precise or vague?

□ GENERALITY DETECTION
  Search for and flag these weak terms:

  [ ] "Best" - Replace with: _________
  [ ] "Leading" - Replace with: _________
  [ ] "Top" - Replace with: _________
  [ ] "Quality" - Replace with: _________
  [ ] "Fast" - Replace with: _________
  [ ] "Effective" - Replace with: _________
  [ ] "Many" - Replace with: _________
  [ ] "Several" - Replace with: _________
  [ ] "Affordable" - Replace with: _________
  [ ] "Premium" - Replace with: _________

  Generality Count: ___
  Target: 0

□ NUMBER SPECIFICITY
  - Uses exact numbers vs rounded? (37.4% not "about 40%")
  - Odd numbers used? (47 not 50, 2,847 not "about 3,000")
  - Source for numbers cited?
  Score: ___/10

  Hopkins: "Numbers build credibility.
  Round numbers look guessed. Exact numbers look measured."

□ TIME SPECIFICITY
  - Exact timeframes given? ("4 days" not "fast")
  - Results timeline specific? ("By Tuesday" not "soon")
  - Deadlines are precise? ("11:59pm EST Jan 15" not "limited time")
  Score: ___/10

□ RESULT SPECIFICITY
  - Outcomes are measurable? ("37% increase" not "better")
  - Examples include specifics? (name, place, amount)
  - Testimonials have concrete details?
  Score: ___/10

SPECIFICITY CONVERSION TABLE:
┌─────────────────────┬──────────────────────────────────────┐
│ VAGUE               │ SPECIFIC (Hopkins Style)             │
├─────────────────────┼──────────────────────────────────────┤
│ Many customers      │ 47,832 customers in 23 countries     │
│ Fast delivery       │ Arrives in 4.2 business days average │
│ High quality        │ 99.7% pass rate on 47-point QC       │
│ Save money          │ Save $847 per year (avg customer)    │
│ Popular choice      │ 3,247 sold in last 30 days           │
│ Experienced team    │ 127 combined years, 1,847 projects   │
│ Guaranteed results  │ 97.3% success rate or full refund    │
│ Limited time        │ Ends 11:59pm EST Friday, Jan 24      │
│ Affordable          │ $47/month (less than Netflix)        │
│ Best in class       │ Ranked #1 by [Source] 3 years in row │
└─────────────────────┴──────────────────────────────────────┘

SPECIFICITY SCORE: ___/40
```

### Phase 4: Service Audit

Hopkins said: "The best ads ask no one to buy. They are based entirely on service."

```
SERVICE AUDIT:

Does copy provide value BEFORE asking for money?

□ VALUE-FIRST TEST
  - Remove the product/CTA - is remaining content useful?
  - Would reader learn something even if they don't buy?
  - Is information genuinely helpful to them?
  Score: ___/10

  FAIL: "Buy now and get our amazing product!"
  PASS: "Here's how to identify the 3 signs of [problem]...
         (genuinely useful content)...
         If you want help fixing it, here's what we built..."

□ EDUCATION RATIO
  - What % is education vs pitch?
  - Minimum 60% educational content for long-form?
  - Reader feels helped, not sold to?
  Score: ___/10

□ CURIOSITY CREATION
  - Opens loops that make reader want more?
  - Uses Zeigarnik effect (incomplete = memorable)?
  - Creates genuine interest in mechanism/process?
  Score: ___/10

  Hopkins: "Curiosity is one of the strongest human incentives."

□ EXPERT POSITIONING
  - Copy demonstrates expertise through teaching?
  - Reader sees you as authority through content quality?
  - Trust built through helpfulness, not claims?
  Score: ___/10

SERVICE SCORE: ___/40
```

### Phase 5: Headline Audit

Hopkins said: "Headlines can change results by 500%."

```
HEADLINE AUDIT:

Does headline select the RIGHT people?

□ AUDIENCE SELECTION
  - Headline calls out specific audience?
  - Wrong people self-deselect?
  - Right people immediately identify?
  Score: ___/10

  Hopkins: "The purpose of a headline is to pick out people you can interest.
  You wish to talk to someone in a crowd."

  FAIL: "Introducing Our New Product Line" (who cares?)
  PASS: "To Parents Whose Children Struggle With Math" (specific callout)

□ BENEFIT PROMISE
  - Clear benefit stated or implied?
  - Reader knows what they'll get?
  - Promise is credible and specific?
  Score: ___/10

□ CURIOSITY GAP
  - Creates desire to read more?
  - Doesn't give everything away?
  - "I need to know more" response?
  Score: ___/10

□ TESTABLE HYPOTHESIS
  - Headline represents a hypothesis about what works?
  - Multiple variations created for testing?
  - Clear metric to measure winner?
  Score: ___/10

  Hopkins ran "Do You Make These Mistakes in English?" for 40 YEARS
  because he tested and found nothing beat it.

HEADLINE PATTERNS TO TEST:
1. Direct Benefit: "How to [achieve X] in [time]"
2. Curiosity: "Do You Make These Mistakes in [area]?"
3. News: "Announcing: [new thing] that [benefit]"
4. Callout: "To [specific audience] who [situation]"
5. Specific: "[Number] Ways to [achieve result]"

HEADLINE SCORE: ___/40
```

### Phase 6: Testability Audit

Hopkins said: "Almost any question can be answered, cheaply, quickly and finally, by a test campaign."

```
TESTABILITY AUDIT:

Can you measure and improve this copy?

□ TRACKING IMPLEMENTATION
  - Unique tracking code/UTM for this copy?
  - Different codes for different channels?
  - Attribution possible to this specific piece?
  Score: ___/10

  TRACKING CODE CHECKLIST:
  □ UTM Source: ____________
  □ UTM Medium: ____________
  □ UTM Campaign: ____________
  □ Coupon Code: ____________
  □ Phone Number: ____________
  □ Landing Page: ____________

□ VARIABLE ISOLATION
  - If testing, only ONE variable changed?
  - Control version documented?
  - Winner criteria defined before test?
  Score: ___/10

□ METRIC CLARITY
  - Primary success metric defined?
  - Secondary metrics identified?
  - ROI calculable from data?
  Score: ___/10

  PRIMARY METRIC: ____________
  SECONDARY: ____________
  ROI FORMULA: ____________

□ TEST VARIATIONS READY
  - At least 3 headline variations?
  - Offer variations considered?
  - CTA variations available?
  Score: ___/10

TESTABILITY SCORE: ___/40
```

### Phase 7: Sample/Trial Strategy Audit

Hopkins said: "The product itself should be its own best salesman."

```
SAMPLE STRATEGY AUDIT:

Does offer let product prove itself?

□ RISK REVERSAL
  - Trial/sample/guarantee offered?
  - Risk on seller, not buyer?
  - Objection "what if it doesn't work" addressed?
  Score: ___/10

  OPTIONS:
  - Free sample
  - Trial period
  - Money-back guarantee
  - Demo/preview
  - Proof before payment

□ SAMPLE QUALITY
  - Sample delivers FULL experience?
  - Not crippled/limited version?
  - Enough to form real impression?
  Score: ___/10

  Hopkins: "Sample must deliver the complete product experience."

□ SAMPLE QUALIFICATION
  - Sample goes to INTERESTED people only?
  - Some barrier to entry (not free for anyone)?
  - Creates respect, not desperation?
  Score: ___/10

  Hopkins: "Give samples to interested people only.
  Create an atmosphere of respect, a desire, an expectation."

□ FOLLOW-UP SYSTEM
  - What happens after sample?
  - Conversion path clear?
  - Timing defined?
  Score: ___/10

SAMPLE STRATEGY SCORE: ___/40
```

## Phase 8: Final Scoring

```
HOPKINS SCIENTIFIC COPY AUDIT - FINAL SCORE

┌────────────────────────┬────────┬────────┐
│ CATEGORY               │ SCORE  │ MAX    │
├────────────────────────┼────────┼────────┤
│ 1. Salesmanship        │ ___    │ /40    │
│ 2. Reason Why          │ ___    │ /40    │
│ 3. Specificity         │ ___    │ /40    │
│ 4. Service             │ ___    │ /40    │
│ 5. Headline            │ ___    │ /40    │
│ 6. Testability         │ ___    │ /40    │
│ 7. Sample Strategy     │ ___    │ /40    │
├────────────────────────┼────────┼────────┤
│ TOTAL                  │ ___    │ /280   │
└────────────────────────┴────────┴────────┘

PERCENTAGE: ____%

GRADE:
- 90%+ (252-280): PUBLISH - Scientific advertising excellence
- 80-89% (224-251): MINOR FIXES - Address noted issues
- 70-79% (196-223): SIGNIFICANT REVISION - Core issues present
- Below 70% (<196): REWRITE - Fundamental problems

VERDICT: ____________
```

## Outputs

### Output Format

```yaml
audit_summary:
  copy_type: [type audited]
  total_score: [X/280]
  percentage: [X%]
  grade: [PUBLISH | MINOR FIXES | REVISION | REWRITE]

strengths:
  - [What Hopkins would approve]
  - [Scientific elements present]

critical_issues:
  - issue: [Description]
    category: [Salesmanship | Reason Why | Specificity | etc.]
    current: [What copy says now]
    hopkins_fix: [How Hopkins would fix it]
    priority: [HIGH | MEDIUM | LOW]

tracking_plan:
  primary_metric: [What to measure]
  tracking_codes:
    - channel: [Name]
      code: [Tracking code]
  test_variations:
    - element: [Headline | Offer | CTA]
      versions: [List of variations to test]

next_steps:
  1: [First action]
  2: [Second action]
  3: [Third action]
```

## Hopkins' Final Words

```
"The compass of accurate knowledge directs
the shortest, safest, cheapest course."

"Guessing is not advertising. Testing is."

Before you publish, ask:
1. Can I measure this?
2. Can I test variations?
3. Can I prove my claims?
4. Would a salesperson say this face-to-face?

If any answer is NO, fix it first.
```

## Integration

- **Follows**: Eugene Schwartz diagnosis (awareness + sophistication levels)
- **Precedes**: Final publication or A/B test launch
- **Related Tasks**: setup-split-test.md, create-headlines.md
- **Related Checklist**: hopkins-audit-checklist.md
