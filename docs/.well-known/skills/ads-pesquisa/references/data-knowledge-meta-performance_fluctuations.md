# Performance Fluctuations

## Summary

Not every metric change is an anomaly. Meta ads exhibit normal day-to-day fluctuations of up to +-15% in CPA, with seasonal patterns and day-of-week effects. Agents must distinguish between normal variation and genuine anomalies (>30% CPA increase sustained 3+ days, CTR drops >50% from 7-day average, or spend dropping to $0). Reacting to normal fluctuations causes unnecessary Learning Phase resets and wasted optimization cycles.

## Deep Dive

### Normal Fluctuations (Do NOT React)

Daily performance variation is inherent in digital advertising. These patterns are expected and should not trigger agent intervention:

| Pattern | Expected Range | Cause |
|---------|---------------|-------|
| **Daily CPA variation** | +-15% from 7-day average | Auction competition shifts, user behavior changes, time-of-day effects |
| **Weekend vs. weekday** | 10-25% CPA difference | Different user intent and competition levels |
| **Day-of-week effects** | Consistent patterns per weekday | Industry-specific (e.g., B2B lower on weekends, e-commerce higher on Fridays) |
| **Seasonal patterns** | Gradual shifts over weeks | Holiday seasons, industry cycles, weather |
| **CTR micro-fluctuations** | +-10% daily | Normal audience rotation, frequency effects |
| **CPM variation** | +-20% daily | Auction competition is highly dynamic |
| **Impression volume variation** | +-25% daily | Pacing algorithm adjustments (see `pacing.md`) |
| **Monthly billing cycle effects** | Higher spend at month start | Many advertisers reset budgets monthly, increasing competition |

### How to Identify Normal Fluctuations

Use the **7-day rolling average** as the baseline. A single day outside the normal range is NOT an anomaly -- it takes 3+ consecutive days of deviation to signal a real trend.

```
NORMAL: Day 1 CPA = R$48, Day 2 = R$55, Day 3 = R$45
        (7-day avg = R$50, all within +-15%)

ABNORMAL: Day 1 CPA = R$65, Day 2 = R$68, Day 3 = R$72
          (7-day avg = R$50, sustained >30% increase for 3 days)
```

### Anomalies (MUST React)

These patterns indicate genuine problems that require investigation:

| Anomaly | Detection Criteria | Severity | Likely Cause |
|---------|-------------------|----------|-------------|
| **CPA spike (sustained)** | >30% increase from 7-day average for 3+ consecutive days | HIGH | Creative fatigue, audience saturation, competitor entry, targeting drift |
| **CTR crash** | >50% drop from 7-day average | HIGH | Creative fatigue, audience mismatch, ad disapproval, placement issue |
| **Spend drops to $0** | Zero delivery for 4+ hours during active schedule | CRITICAL | Account issue (billing, policy), ad disapproval, budget depleted, audience size zero |
| **Frequency spike** | Frequency >3.0 in 7 days (prospecting) or >8.0 (retargeting) | MEDIUM | Audience too narrow, budget too high for audience size |
| **ROAS collapse** | >40% drop from 7-day average for 3+ days | HIGH | Conversion tracking issue, landing page problem, offer fatigue |
| **CPM explosion** | >50% increase sustained 3+ days | MEDIUM | Increased competition (holiday, political season), audience quality shift |
| **Conversion rate drop** | >40% drop from 7-day average for 3+ days | HIGH | Landing page issue, pixel/CAPI problem, offer-audience mismatch |

### Root Cause Analysis Framework

When an anomaly is detected, investigate in this order:

```
STEP 1: Check Technical Issues First
  - Is the pixel/CAPI firing correctly?
  - Is the landing page working (load time, 404 errors)?
  - Is the ad approved and active?
  - Is the payment method valid?
  - Is the account in good standing?

STEP 2: Check External Factors
  - Is there a major holiday or event?
  - Did a competitor launch an aggressive campaign?
  - Is there a seasonal shift in the industry?
  - Did the audience platform change (iOS update, algorithm shift)?

STEP 3: Check Campaign Factors
  - Is the ad in Learning Phase? (see learning_phase.md)
  - Has frequency reached fatigue levels?
  - Has the creative been running too long without refresh?
  - Were any manual changes made recently?

STEP 4: Check Data Quality
  - Did the attribution window change?
  - Is there a reporting delay?
  - Are events being deduplicated correctly?
```

### Reaction Timing Guidelines

| Timeframe | Action | Rationale |
|-----------|--------|-----------|
| **Day 1 of anomaly** | Monitor. Log the observation. Do NOT change anything | Could be normal fluctuation |
| **Day 2 of anomaly** | Investigate root cause (technical, external, campaign, data) | Two days starts to suggest a trend |
| **Day 3 of anomaly** | Act if root cause is identified. If no root cause found, escalate | Three days of sustained anomaly is statistically significant |
| **Day 5+ of anomaly** | Mandatory action. Cannot ignore further | Extended anomaly causes cumulative budget waste |

### Seasonal Calendar (Brazil Market)

Key periods with expected performance shifts for Brazilian campaigns:

| Period | Expected Impact | Notes |
|--------|----------------|-------|
| Carnaval (Feb-Mar) | CPM +20-40%, CTR -10-20% | Reduced commercial intent, higher competition for remaining attention |
| Dia das Maes (May) | CPM +30-50% (e-commerce) | Heavy competition, plan budgets 2 weeks before |
| Dia dos Namorados (Jun 12) | CPM +20-30% | Gifts/e-commerce spike |
| Black Friday (Nov) | CPM +50-100%, CPA +30-60% | Most competitive period. Budget 3x for similar volume |
| Natal (Dec) | CPM +40-80% | Extended high-competition period |
| Janeiro | CPM -20-30% | Low competition, good for testing |

### False Positive Prevention

Agents must avoid these common false positive triggers:

1. **Single bad day followed by recovery** -- NOT an anomaly
2. **Weekend drop for B2B** -- Expected, not a problem
3. **Post-holiday normalization** -- Return to baseline after a peak is normal
4. **New creative launch with initial high CPA** -- Learning Phase effect (see `learning_phase.md`)
5. **Slight CPM increase during peak hours** -- Pacing effect (see `pacing.md`)

## Agent Rules

| Agent | Load Condition |
|-------|----------------|
| @performance-analyst | Primary consumer. Load during every performance review. Use the anomaly detection criteria as the decision framework for when to flag issues vs. when to observe |
| @budget-optimizer | When evaluating spend anomalies (underspend, overspend patterns) |
| @ad-midas | When user panics about "my CPA went up today" -- use this doc to determine if intervention is warranted |
| @campaign-manager | When deciding whether to make campaign changes in response to performance shifts |

**Load method:** On-demand via Read tool during performance analysis.

**CRITICAL RULE:** Agents should NOT react to single-day fluctuations within the normal range. The default response to a single off day is "monitor" -- not "change."

## Red Flags

- NEVER react to a single day of performance fluctuation within +-15% of the 7-day average
- NEVER make campaign changes (budget, targeting, creative) in response to normal day-to-day variation -- this resets Learning Phase unnecessarily
- NEVER ignore sustained anomalies (3+ days of >30% deviation) -- waiting beyond 5 days causes cumulative budget waste
- NEVER diagnose anomalies without checking technical factors first (pixel, landing page, account status)
- NEVER assume all CPM increases are problems -- seasonal competition increases are expected and should be budgeted for
- NEVER compare raw daily numbers without using a rolling average baseline -- absolute numbers without context are meaningless

## Sources

- Meta Business Help Center: "Understanding ad performance fluctuations"
- Meta Marketing Science: "Statistical significance in campaign reporting"
- mathiaschu/meta-ads-analyzer: `performance_fluctuations.md` reference document
- Industry benchmarks: Brazilian digital advertising seasonal patterns (IAB Brasil, 2025)
