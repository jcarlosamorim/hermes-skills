# Pacing

## Summary

Pacing is how Meta distributes your daily or lifetime budget across the delivery period. Meta uses predictive models to spend budget optimally throughout the day, balancing between finding the cheapest opportunities and ensuring the full budget is spent. Standard delivery (the default) uses even pacing; accelerated delivery front-loads spend into the cheapest early opportunities.

## Deep Dive

### How Meta's Pacing System Works

Meta's pacing algorithm operates in real-time, constantly adjusting how aggressively your ads compete in auctions. The system balances two competing goals:

1. **Efficiency** -- Find the cheapest conversion opportunities
2. **Budget utilization** -- Spend the full daily/lifetime budget

The algorithm uses a pacing multiplier that adjusts the effective bid throughout the day:

```
Effective Bid = Base Bid x Pacing Multiplier

- Multiplier > 1.0: Bidding more aggressively (underspending, need to catch up)
- Multiplier = 1.0: On pace
- Multiplier < 1.0: Bidding less aggressively (overspending, need to slow down)
```

### Standard Delivery (Default)

Standard delivery distributes budget evenly across the day (or delivery period for lifetime budgets). The algorithm:

1. Predicts total available auction opportunities for the day
2. Calculates the ideal spend rate per hour
3. Adjusts the pacing multiplier every few minutes to stay on track
4. Enters more auctions during cheap periods, fewer during expensive periods

**Result:** Consistent delivery throughout the day. Budget is fully spent by end of day. CPA tends to be more stable.

### Accelerated Delivery

Accelerated delivery spends budget as fast as possible, entering every available auction at full bid. The algorithm:

1. Bids at maximum competitiveness from the start
2. Budget may be exhausted before end of day
3. Captures early, often cheaper auction opportunities
4. Stops delivery once budget is depleted

**Result:** Front-loaded spend. Budget may run out by midday. Useful for time-sensitive campaigns (flash sales, event promotions) but generally more expensive.

**Note:** Meta has deprecated accelerated delivery for most campaign types as of 2023. Standard delivery is now the only option for most objectives.

### Lifetime Budget Pacing

For campaigns with a lifetime budget and scheduled end date, Meta distributes budget across the entire flight:

- Spends more on days with better opportunities (lower competition)
- Spends less on days with higher competition
- Accounts for day-of-week patterns (if historical data exists)
- Ensures budget is fully spent by the end date

### Why Underspending Happens

When a campaign consistently underspends its daily budget, common causes include:

| Cause | Explanation | Fix |
|-------|-------------|-----|
| Audience too narrow | Not enough auction opportunities | Expand targeting |
| Bid too low | Losing most auctions | Increase bid or switch to Lowest Cost |
| Ad quality low | Low Total Value score | Improve creative, check relevance diagnostics |
| Budget too high | Budget exceeds available inventory for audience | Reduce budget or expand audience |
| Frequency cap reached | All users in audience have been reached at cap | Expand audience or adjust cap |
| Schedule restriction | Dayparting limits available hours | Expand delivery schedule |

### Why Overspending Happens

Meta may spend up to 25% over the daily budget on any single day, as long as the weekly average stays within the daily budget x 7. This is documented behavior, not a bug.

### Pacing and Learning Phase

During Learning Phase, pacing is less predictable because the algorithm is still learning optimal delivery patterns. Expect:
- Spiky delivery (some hours heavy, some hours near zero)
- Higher variance in daily spend
- Gradual stabilization as learning progresses

## Agent Rules

| Agent | Load Condition |
|-------|----------------|
| @performance-analyst | When investigating delivery issues (underspending, overspending, uneven distribution) |
| @budget-optimizer | When evaluating budget allocation and daily spend patterns |
| @campaign-manager | When setting up delivery schedules or responding to delivery concerns |
| @ad-midas | When user asks "why isn't my budget being spent" or "why did Meta overspend today" |

**Load method:** On-demand via Read tool when delivery/pacing issues are reported.

**Key rule:** Agents should NOT manually adjust delivery schedules unless daily budget is consistently underdelivering (spending <80% of daily budget for 3+ consecutive days). Meta's pacing system is generally better at distribution than manual overrides.

## Red Flags

- NEVER manually adjust delivery schedules as a first response to uneven spend -- investigate root cause first
- NEVER panic over a single day of 25% overspend -- this is documented Meta behavior within their weekly averaging system
- NEVER interpret Learning Phase spiky delivery as a pacing problem -- it's a learning problem
- NEVER recommend accelerated delivery for standard campaigns -- it's deprecated for most objectives and generally less efficient
- NEVER set lifetime budgets without calculating the minimum daily implied spend (lifetime / days) against the 50-conversion learning threshold
- NEVER ignore consistent underspend (<80% daily budget for 3+ days) -- it signals a structural issue with audience, bid, or creative quality

## Sources

- Meta Business Help Center: "About ad delivery pacing"
- Meta Business Help Center: "Why your ad set spent more than your daily budget"
- Meta Engineering Blog: "Pacing for online ad delivery systems" (2019)
- mathiaschu/meta-ads-analyzer: `pacing.md` reference document
