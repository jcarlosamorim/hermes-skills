# Task: Plan Paid Traffic Strategy

> **Framework**: Product Launch Formula (Jeff Walker)
> **Agent**: @jeff-walker
> **Phase**: Traffic & List Building
> **Output**: Complete paid traffic strategy for PLF launch

---

## Purpose

Create a paid traffic strategy that supports your Product Launch Formula launch. Paid traffic accelerates list building and amplifies your launch when done strategically.

---

## Paid Traffic in PLF Context

> "Paid traffic is gasoline on your fire. But you need a fire first. Don't spend money driving traffic until you have a proven conversion process." - Jeff Walker

**When to use paid traffic:**
- After at least one successful organic launch
- With proven opt-in and conversion rates
- When you can afford to test and learn
- To scale a working system

**When NOT to use paid traffic:**
- First launch (do organic first)
- Untested offer
- No tracking in place
- Cash-strapped

---

## Prerequisites

- [ ] At least one internal launch completed
- [ ] Conversion data from previous launch
- [ ] Budget allocated for ads
- [ ] Tracking pixels installed
- [ ] Landing pages ready

---

## Workflow Steps

### Step 1: Gather Context

**Elicit from user:**
```
1. Have you done a launch before? Conversion rate?
2. What's your total ad budget?
3. What platforms are you considering? (Facebook, Google, etc.)
4. What's your cost per lead target?
5. Do you have existing pixel data?
6. What's your product price?
7. What lead magnet will you use?
```

### Step 2: Calculate Traffic Economics

**Key metrics to know:**

```yaml
# From previous launch
list_size: ""
conversion_rate: ""
average_order_value: ""
earnings_per_subscriber: ""

# Traffic targets
target_new_subscribers: ""
cost_per_lead_target: ""
total_traffic_budget: ""

# Calculations
max_cpl_for_profit: "" # (conversion_rate × aov) / 3
```

**Example calculation:**
```
Previous conversion: 2%
Average order: R$997
Revenue per 100 subs: R$1,994
Max CPL for 3x ROI: R$6.65

If budget is R$5,000:
Expected leads: 750 (at R$6.65 CPL)
Expected revenue: R$14,955
ROI: 3x
```

### Step 3: Select Traffic Platforms

**Platform comparison:**

| Platform | Best For | Typical CPL | Learning Curve |
|----------|----------|-------------|----------------|
| Facebook/Meta | B2C, broad audiences | R$3-15 | Medium |
| Google Search | High-intent | R$10-30 | Medium-High |
| YouTube | Educational content | R$5-20 | High |
| LinkedIn | B2B, professional | R$20-50 | Medium |
| TikTok | Younger audiences | R$2-10 | Medium |

**Selection criteria:**
- Where is your avatar?
- What's your budget?
- What content do you have?
- What's your experience level?

**Reference:**
- `data/plf/platform-comparison-kb.yaml`

### Step 4: Define Campaign Structure

**PLF traffic funnel:**

```
COLD TRAFFIC
    ↓
Opt-in Page (Lead Magnet or PLC Access)
    ↓
Thank You Page + PLC1
    ↓
Email Sequence → PLCs → Sales Page
    ↓
PURCHASE
```

**Campaign types needed:**

1. **List Building Campaign (Primary)**
   - Objective: Conversions (leads)
   - Landing: Opt-in page
   - Budget: 70% of total

2. **Retargeting Campaign**
   - Objective: Conversions
   - Audience: Page visitors, email list
   - Budget: 20% of total

3. **Lookalike Campaign**
   - Objective: Conversions (leads)
   - Audience: Lookalike of buyers/engagers
   - Budget: 10% of total

### Step 5: Create Audience Strategy

**Audience layers:**

| Layer | Audience | Temperature | Use For |
|-------|----------|-------------|---------|
| 1 | Lookalike buyers | Warmest | List building |
| 2 | Lookalike subscribers | Warm | List building |
| 3 | Interest targeting | Cold | Testing |
| 4 | Page visitors | Hot | Retargeting |
| 5 | Email list | Hot | Retargeting |

**Custom audiences to create:**
- [ ] Email list upload (customers)
- [ ] Email list upload (subscribers)
- [ ] Website visitors (all pages)
- [ ] Sales page visitors
- [ ] PLC viewers (if trackable)
- [ ] Video viewers (if applicable)

**Lookalike audiences:**
- [ ] 1% lookalike of buyers
- [ ] 1% lookalike of subscribers
- [ ] 1-2% lookalike of engagers

### Step 6: Plan Creative Strategy

**Ad types for PLF:**

1. **Lead Gen Ads**
   - Focus on lead magnet value
   - Clear transformation promise
   - Strong CTA to opt-in

2. **Content Ads**
   - Promote PLC content
   - Educational angle
   - Build authority

3. **Retargeting Ads**
   - Remind to watch PLCs
   - Cart open reminders
   - Urgency-focused

**Creative variations to test:**
- [ ] Image vs video
- [ ] Long copy vs short copy
- [ ] Direct response vs content
- [ ] Different hooks/angles
- [ ] Various formats (carousel, single, etc.)

**Example ad angles:**
```
Angle 1: Problem-focused
"Struggling with [PROBLEM]? Here's why..."

Angle 2: Curiosity
"The [X] method that [RESULT] (most people miss this)"

Angle 3: Social proof
"How [X] people [ACHIEVED RESULT] with [METHOD]"

Angle 4: Direct
"Free training: [SPECIFIC RESULT]"
```

### Step 7: Set Budget Allocation

**Budget phasing:**

| Phase | Duration | Budget % | Focus |
|-------|----------|----------|-------|
| Testing | 2-4 weeks | 20% | Find winners |
| Pre-Launch | 2 weeks | 30% | Build list |
| Launch Week | 1 week | 40% | Maximum push |
| Retargeting | Ongoing | 10% | Cart recovery |

**Daily budget calculation:**
```
Total budget: R$10,000
Testing (20%): R$2,000 ÷ 14 days = R$143/day
Pre-Launch (30%): R$3,000 ÷ 14 days = R$214/day
Launch (40%): R$4,000 ÷ 7 days = R$571/day
Retargeting (10%): R$1,000 ÷ ongoing
```

### Step 8: Plan Launch Week Traffic

**Cart open strategy:**

| Day | Campaigns Active | Budget Allocation |
|-----|------------------|-------------------|
| Open Day | List building + Retargeting | 25% of launch budget |
| Day 2-3 | Retargeting heavy | 30% |
| Day 4 | Retargeting + urgency | 20% |
| Final Day | All urgency messaging | 25% |

**Retargeting sequences:**
1. PLC viewers who didn't opt-in → Push opt-in
2. Opted in, didn't watch PLCs → Push PLC
3. Watched PLCs, didn't buy → Push sales page
4. Visited sales page, didn't buy → Cart recovery
5. Started checkout, didn't complete → Abandonment

### Step 9: Set Up Tracking

**Required tracking:**
- [ ] Facebook pixel installed
- [ ] Google Analytics connected
- [ ] UTM parameters on all links
- [ ] Conversion tracking verified
- [ ] Email platform integrated

**Key events to track:**
```
- Page view (all pages)
- Lead (opt-in complete)
- ViewContent (PLC views)
- InitiateCheckout (checkout start)
- Purchase (sale complete)
```

**Attribution setup:**
- Use UTM parameters
- Track by campaign/adset/ad
- Connect to email platform
- Build revenue attribution

### Step 10: Create Testing Plan

**Test hierarchy:**

```
1. Audience testing (first)
   - Which audiences perform best?
   - 3-5 audiences, same creative
   - Pick winners at R$50-100 spend each

2. Creative testing (second)
   - Which creatives win?
   - 3-5 creatives, winning audience
   - Pick winners at R$50-100 spend each

3. Optimization (ongoing)
   - Scale winners
   - Kill losers
   - Test new variations
```

**Kill criteria:**
- CPL > 2x target after R$100 spent
- CTR < 0.5% after 5,000 impressions
- No conversions after R$50 spent

### Step 11: Plan Contingencies

**If CPL too high:**
- Pause and reassess
- Test new audiences
- Test new creatives
- Improve landing page

**If not spending budget:**
- Expand audiences
- Raise bid
- Add placements
- Create new ads

**Reference:**
- `data/plf/contingency-framework-kb.yaml`

### Step 12: Validate Strategy

**Pre-launch checklist:**
- [ ] Pixel firing correctly
- [ ] Audiences created
- [ ] Creatives approved
- [ ] Budget confirmed
- [ ] Team aligned
- [ ] Landing pages tested

---

## Deliverables

1. **Traffic Strategy Document**
   - Platform selection
   - Budget allocation
   - Timeline

2. **Audience Plan**
   - Custom audiences to create
   - Lookalike strategy
   - Interest targeting backup

3. **Creative Brief**
   - Ad angles to test
   - Copy variations
   - Visual requirements

4. **Budget Breakdown**
   - Phase allocations
   - Daily budgets
   - Contingency reserves

5. **Tracking Setup**
   - Pixel implementation
   - Conversion events
   - Attribution plan

---

## Success Criteria

- [ ] CPL at or below target
- [ ] Sufficient lead volume
- [ ] Positive ROAS on launch
- [ ] Clear data for optimization
- [ ] Scalable system identified

---

## Budget Guidelines

| Launch Revenue Goal | Min Ad Budget | Typical Ad Budget |
|---------------------|---------------|-------------------|
| R$10,000 | R$500 | R$1,000-2,000 |
| R$50,000 | R$2,500 | R$5,000-10,000 |
| R$100,000 | R$5,000 | R$10,000-20,000 |
| R$500,000+ | R$25,000+ | R$50,000+ |

**Rule of thumb:** 10-20% of revenue goal in ad spend

---

## Common Mistakes

1. **Too early** - Running ads before proven organic launch
2. **No testing** - Going big without testing phase
3. **No tracking** - Can't optimize what you don't measure
4. **Wrong audience** - Wasting money on non-buyers
5. **Bad landing page** - Traffic without conversion
6. **Giving up too early** - Need data to optimize

---

## References

### Knowledge Bases
- `data/plf/platform-comparison-kb.yaml`
- `data/plf/launch-budget-kb.yaml`
- `data/plf/contingency-framework-kb.yaml`

### Checklists
- `checklists/plf/preprelaunch-readiness.md`

---

*Task Version: 1.0*
*Framework: Product Launch Formula - Paid Traffic*
