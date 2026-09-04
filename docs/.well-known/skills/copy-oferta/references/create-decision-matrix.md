# Create Decision Matrix Task

ACTIVATION-NOTICE: This task file contains complete instructions for workflow selection.

## Metadata

```yaml
task:
  name: Create Decision Matrix
  id: create-decision-matrix
  version: "1.0"
  category: strategy
  primary_agents:
    - eugene-schwartz
    - dan-kennedy
    - todd-brown
  estimated_output: Workflow recommendation with initial configuration
  quality_standard: All 5 questions answered + clear workflow recommendation
```

---

## Purpose

Execute the 5-Question Decision Matrix to determine the optimal workflow for any copywriting project. This is the **MANDATORY FIRST STEP** before starting any workflow in the Copy expansion pack.

---

## When to Use

- **ALWAYS FIRST** - Before selecting any workflow (wf-1 through wf-7)
- When starting a new copy project
- When pivoting an existing project
- When unclear which workflow fits best
- When optimizing existing funnel

---

## The 5-Question Decision Matrix

```
DECISION MATRIX FOR WORKFLOW SELECTION

Before starting ANY workflow, answer these 5 questions:

Q1 → AWARENESS LEVEL → Copy approach
Q2 → MARKET SOPHISTICATION → Mechanism requirements
Q3 → PRICE POINT → Proof & objection handling
Q4 → TRAFFIC TEMPERATURE → Entry point strategy
Q5 → PRIMARY OUTPUT → Workflow selection
```

---

## Inputs

```yaml
required:
  - product_name: What you're selling
  - target_market: Who you're selling to
  - price_point: Approximate price of offer
  - traffic_source: Where prospects come from

optional:
  - competitor_landscape: Who else serves this market
  - existing_assets: What copy/content already exists
  - timeline: When this needs to be ready
  - team_resources: Who will execute
```

---

## Workflow

### Step 1: Answer Q1 - Awareness Level

```
═══════════════════════════════════════════════════════════════════
Q1: AWARENESS LEVEL (Schwartz Framework)
═══════════════════════════════════════════════════════════════════

Where is your prospect on the awareness spectrum?

□ LEVEL 1 - UNAWARE
  "Don't know they have a problem"
  → Need story-based, educational approach
  → Longest copy, most nurturing required
  → Workflows: WF-4 (Organic), WF-5 (Email nurture)

□ LEVEL 2 - PROBLEM-AWARE
  "Know the problem, don't know solutions exist"
  → Lead with problem agitation
  → Medium-long copy, solution introduction
  → Workflows: WF-4 (Organic), WF-1 (Full Launch)

□ LEVEL 3 - SOLUTION-AWARE
  "Know solutions exist, don't know YOUR product"
  → Lead with unique mechanism
  → Differentiation critical
  → Workflows: WF-1 (Full Launch), WF-2 (Paid Traffic)

□ LEVEL 4 - PRODUCT-AWARE
  "Know your product, not convinced yet"
  → Lead with proof and objection removal
  → Medium copy, heavy proof
  → Workflows: WF-6 (Optimization), WF-2 (Paid Traffic)

□ LEVEL 5 - MOST AWARE
  "Ready to buy, just need the offer"
  → Lead with offer and urgency
  → Short copy, direct CTA
  → Workflows: WF-6 (Optimization), WF-1 (Launch re-open)

YOUR ANSWER: Level ___

DIAGNOSTIC HELP:
- Where does your traffic come from?
  • Cold ads → Level 1-2
  • Search → Level 2-3
  • Retargeting → Level 4
  • Email list → Level 4-5
  • Past customers → Level 5
```

### Step 2: Answer Q2 - Market Sophistication

```
═══════════════════════════════════════════════════════════════════
Q2: MARKET SOPHISTICATION (Schwartz Scale)
═══════════════════════════════════════════════════════════════════

How evolved is your market in terms of claims and mechanisms?

□ STAGE 1 - VIRGIN MARKET
  "No one has made this promise before"
  → Simple, direct claims work
  → No mechanism needed
  → First mover advantage

□ STAGE 2 - CLAIMS ENLARGEMENT
  "Claims have been made, must top them"
  → Bigger, faster, easier promises
  → Enlargement competition
  → Still no mechanism required

□ STAGE 3 - MECHANISM REQUIRED
  "Market tired of claims, needs HOW"
  → Unique mechanism mandatory
  → Science/process explanation
  → Todd Brown E5 Method critical

□ STAGE 4 - TIRED OF MECHANISMS
  "Everyone has a 'system' now"
  → Identification over mechanism
  → "For [specific avatar] who..."
  → Deep empathy required

□ STAGE 5 - COMPLETELY SKEPTICAL
  "Heard it all, believe none"
  → Identity/emotion based
  → Community/belonging focus
  → Authenticity paramount

YOUR ANSWER: Stage ___

DIAGNOSTIC HELP:
- Count competitors with "proprietary methods":
  • 0-2 competitors → Stage 1-2
  • 3-10 competitors → Stage 3
  • 10+ competitors → Stage 4-5
- Do prospects roll their eyes at new claims? → Stage 4-5
```

### Step 3: Answer Q3 - Price Point

```
═══════════════════════════════════════════════════════════════════
Q3: PRICE POINT
═══════════════════════════════════════════════════════════════════

What is the price of your primary offer?

□ LOW TICKET: Under $100
  → Impulse purchase possible
  → Less proof required
  → Shorter decision cycle
  → Workflows: WF-2 (Paid Traffic), WF-4 (Organic)

□ MID TICKET: $100 - $1,000
  → Need clear value proposition
  → Moderate proof required
  → Days to decide
  → Workflows: WF-1 (Full Launch), WF-2 (Paid Traffic)

□ HIGH TICKET: $1,000 - $5,000
  → Significant proof required
  → Objection handling critical
  → Weeks to decide
  → Workflows: WF-1 (Full Launch), WF-3 (High-Ticket)

□ PREMIUM: $5,000+
  → Application process recommended
  → Extensive proof stack
  → Sales calls typically required
  → Workflows: WF-3 (High-Ticket) mandatory

YOUR ANSWER: ___________

PRICE POINT → PROOF REQUIREMENTS:
- Low: Testimonials, results screenshots
- Mid: Case studies, specific numbers
- High: Video testimonials, detailed case studies
- Premium: References, live Q&A, guarantees
```

### Step 4: Answer Q4 - Traffic Temperature

```
═══════════════════════════════════════════════════════════════════
Q4: TRAFFIC TEMPERATURE
═══════════════════════════════════════════════════════════════════

How warm is your traffic source?

□ COLD TRAFFIC
  "Never heard of you"
  → Long-form content required
  → Trust building first
  → Multi-touch sequence
  → Workflows: WF-2 (with cold ads focus), WF-4 (Organic)

□ WARM TRAFFIC
  "Heard of you, engaged with content"
  → Medium-form effective
  → Differentiation focus
  → Faster conversion possible
  → Workflows: WF-1 (Full Launch), WF-5 (Email)

□ HOT TRAFFIC
  "Engaged, ready to learn more"
  → Direct offers can work
  → Proof stacking effective
  → Urgency moves them
  → Workflows: WF-1 (Launch), WF-6 (Optimization)

YOUR ANSWER: ___________

TRAFFIC SOURCE → TEMPERATURE MAPPING:
- Facebook/Instagram cold ads → COLD
- Google search ads → WARM
- YouTube subscribers → WARM
- Email list (engaged) → HOT
- Past customers → HOT
- Retargeting → WARM to HOT
```

### Step 5: Answer Q5 - Primary Output Needed

```
═══════════════════════════════════════════════════════════════════
Q5: PRIMARY OUTPUT
═══════════════════════════════════════════════════════════════════

What is the main deliverable you need?

□ VSL (Video Sales Letter)
  → Jon Benson methodology
  → Emotional progression
  → Workflows: WF-1, WF-3

□ SALES LETTER (Long-form written)
  → Gary Halbert methodology
  → Story-driven
  → Workflows: WF-1, WF-3, WF-7

□ EMAIL SEQUENCE
  → Andre Chaperon or Ben Settle
  → SOS or Daily methodology
  → Workflows: WF-5

□ AD CREATIVE
  → Multi-format (video, image, text)
  → Platform specific
  → Workflows: WF-2

□ WEBINAR
  → Education + pitch
  → Benson + Makepeace blend
  → Workflows: WF-3

□ DIRECT MAIL
  → Rutz, Lampropoulos, Deutsch
  → Physical package
  → Workflows: WF-7

□ LANDING PAGE
  → Lead capture or sales
  → Conversion focused
  → Workflows: WF-1, WF-2

□ CONTENT (Organic)
  → Social posts, newsletters
  → Brand building
  → Workflows: WF-4

□ FUNNEL OPTIMIZATION
  → Improve existing assets
  → A/B testing
  → Workflows: WF-6

YOUR ANSWER: ___________
```

---

## Step 6: Workflow Recommendation Matrix

```
WORKFLOW SELECTION MATRIX

Based on your answers, use this matrix:

┌────────────────────────────────────────────────────────────────────────┐
│ WORKFLOW              │ BEST FOR                    │ PRICE POINT      │
├────────────────────────────────────────────────────────────────────────┤
│ WF-1 Full Launch      │ New product launches        │ Mid to High      │
│                       │ Awareness 2-5               │ $100-$5000       │
│                       │ Warm/Hot traffic            │                  │
├────────────────────────────────────────────────────────────────────────┤
│ WF-2 Paid Traffic     │ Paid acquisition            │ Low to Mid       │
│                       │ All awareness levels        │ Under $1000      │
│                       │ Cold to Warm traffic        │                  │
├────────────────────────────────────────────────────────────────────────┤
│ WF-3 High-Ticket      │ Premium offers              │ High to Premium  │
│                       │ Awareness 3-5               │ $1000+           │
│                       │ Any traffic (nurture)       │                  │
├────────────────────────────────────────────────────────────────────────┤
│ WF-4 Organic Content  │ Brand building              │ Any              │
│                       │ Awareness 1-3               │                  │
│                       │ Cold traffic warming        │                  │
├────────────────────────────────────────────────────────────────────────┤
│ WF-5 Email Marketing  │ List monetization           │ Any              │
│                       │ Awareness 2-5               │                  │
│                       │ Warm/Hot traffic            │                  │
├────────────────────────────────────────────────────────────────────────┤
│ WF-6 Funnel Opt       │ Existing funnel improvement │ Any              │
│                       │ Awareness 4-5               │                  │
│                       │ Hot traffic optimization    │                  │
├────────────────────────────────────────────────────────────────────────┤
│ WF-7 Direct Mail      │ Physical mail campaigns     │ High to Premium  │
│                       │ B2B or premium consumer     │ $1000+           │
│                       │ Targeted lists              │                  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Step 7: Generate Recommendation

### Decision Logic

```yaml
decision_tree:

  # Premium Path
  if_premium_price:
    condition: "Price Point = Premium ($5000+)"
    recommendation: "WF-3 High-Ticket"
    reason: "Premium requires sales calls and extensive nurturing"

  # Direct Mail Path
  if_direct_mail_output:
    condition: "Primary Output = Direct Mail"
    recommendation: "WF-7 Direct Mail"
    reason: "Specialized workflow for physical mail"

  # Optimization Path
  if_optimization_output:
    condition: "Primary Output = Funnel Optimization"
    recommendation: "WF-6 Funnel Optimization"
    reason: "Existing funnel improvement focus"

  # Email Path
  if_email_output:
    condition: "Primary Output = Email Sequence"
    recommendation: "WF-5 Email Marketing"
    reason: "Specialized for email systems"

  # Content Path
  if_content_output:
    condition: "Primary Output = Content (Organic)"
    recommendation: "WF-4 Organic Content"
    reason: "Brand building and cold traffic warming"

  # Paid Traffic Path
  if_ad_output_or_cold:
    condition: "Primary Output = Ad Creative OR Traffic = Cold"
    recommendation: "WF-2 Paid Traffic"
    reason: "Optimized for paid acquisition"

  # Default Launch Path
  default:
    condition: "All other cases"
    recommendation: "WF-1 Full Launch"
    reason: "Comprehensive workflow for most scenarios"
```

---

## Output Format

### Recommendation Template

```yaml
decision_matrix_result:

  answers:
    q1_awareness_level: [1-5]
    q2_market_sophistication: [1-5]
    q3_price_point: [Low | Mid | High | Premium]
    q4_traffic_temperature: [Cold | Warm | Hot]
    q5_primary_output: [VSL | Sales Letter | Email | Ad | Webinar | Direct Mail | Landing | Content | Optimization]

  recommendation:
    workflow_id: "wf-X-name"
    workflow_name: "Full Name"
    confidence: [HIGH | MEDIUM | LOW]

  rationale: |
    Based on your answers:
    - [Reason 1 from answers]
    - [Reason 2 from answers]
    - [Reason 3 from answers]

  initial_configuration:
    tier_0_agents:
      - "[Agent 1] for [purpose]"
      - "[Agent 2] for [purpose]"
    tier_1_agents:
      - "[Agent 3] for [purpose]"
    clone_combinations:
      - "[Combination 1] for [purpose]"

  first_steps:
    1: "Run diagnose-awareness-level.md to confirm Level [X]"
    2: "Run diagnose-market-sophistication.md to confirm Stage [X]"
    3: "Execute [Workflow] Phase 1"

  warnings:
    - "[Warning if applicable based on combination]"
```

---

## Clone Combinations by Workflow

```yaml
proven_combinations:

  wf_1_full_launch:
    foundation: "Schwartz (awareness) + Hopkins (testing)"
    strategy: "Kennedy (3Ms) + Todd Brown (mechanism)"
    execution: "Halbert (story) + Makepeace (emotion)"
    email: "Chaperon (SOS) + Sugarman (triggers)"

  wf_2_paid_traffic:
    cold_ads: "Halbert (story hooks) + Schwartz (awareness match)"
    warm_ads: "Carlton (direct benefit) + Bencivenga (fascinations)"
    hot_ads: "Most Aware offers + Sugarman (triggers)"
    landing: "Hopkins (testing) + Bencivenga (bullets)"

  wf_3_high_ticket:
    positioning: "Kennedy (avatar) + Todd Brown (mechanism)"
    webinar: "Benson (VSL) + Makepeace (emotion)"
    email: "Chaperon (long SOS) + Settle (follow-up)"
    call_script: "Kennedy (objections)"

  wf_4_organic:
    short_form: "Collier (entry) + Sugarman (specificity)"
    long_form: "Halbert (storytelling)"
    newsletter: "Halbert (personal letter)"
    pillar: "Ogilvy (research depth)"

  wf_5_email:
    daily: "Settle (infotainment)"
    automation: "Chaperon (SOS)"
    hybrid: "Chaperon (automated) + Settle (broadcast)"

  wf_6_optimization:
    diagnostic: "Hopkins (metrics) + Schwartz (awareness)"
    fixes: "Bencivenga (headlines) + Lampropoulos (bullets)"
    triggers: "Sugarman (30 triggers)"

  wf_7_direct_mail:
    format: "Rutz (magalog innovation)"
    copy: "Lampropoulos (bullets) + Halbert (story)"
    testing: "Hopkins (scientific) + Deutsch (controls)"
```

---

## Common Mistakes to Avoid

```
MISTAKE 1: Skipping the Decision Matrix
- Symptom: Choosing workflow based on preference, not data
- Fix: Always answer all 5 questions before selecting

MISTAKE 2: Misdiagnosing Awareness Level
- Symptom: Copy mismatches where traffic is
- Fix: Cross-reference traffic source with awareness

MISTAKE 3: Ignoring Market Sophistication
- Symptom: Simple claims in sophisticated market
- Fix: Run diagnose-market-sophistication.md

MISTAKE 4: Price-Workflow Mismatch
- Symptom: Using WF-2 for $5k+ offers
- Fix: Premium ALWAYS needs WF-3

MISTAKE 5: Starting Without Foundation
- Symptom: Jumping to execution without strategy
- Fix: Tier 0 agents (Hopkins, Schwartz, Collier) first
```

---

## Integration

- **Prerequisite for**: All workflows (WF-1 through WF-7)
- **Related tasks**: diagnose-awareness-level.md, diagnose-market-sophistication.md
- **Used by**: copy.sh (workflow selection)
- **Agents**: @eugene-schwartz (Tier 0), @dan-kennedy (Tier 2), @todd-brown (Tier 2)

---

## Validation Checklist

- [ ] All 5 questions answered
- [ ] Awareness level cross-referenced with traffic source
- [ ] Market sophistication validated
- [ ] Price point matches workflow
- [ ] Primary output identified
- [ ] Workflow recommendation generated
- [ ] Initial configuration set
- [ ] First steps documented

---

*Task Version: 1.0*
*Created: 2026-01-23*
*Purpose: Workflow selection before any Copy project*
