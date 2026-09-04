# Learning Phase

## Summary

When a campaign or ad set is created or significantly edited, Meta enters a Learning Phase where the delivery system explores the best audience, placements, and times for optimal results. The ad set needs approximately 50 optimization events (conversions) to exit Learning Phase. During this phase, performance is volatile, costs are higher, and any significant edit resets the counter back to zero.

## Deep Dive

### What Is Learning Phase

Meta's delivery system uses machine learning to optimize ad delivery. When an ad set starts fresh or undergoes significant changes, the algorithm lacks data about how this specific combination of targeting + creative + optimization event will perform. Learning Phase is the exploration period where Meta collects enough signal to stabilize delivery.

### Exiting Learning Phase

An ad set exits Learning Phase when it accumulates approximately **50 optimization events within a 7-day window**. The exact threshold can vary, but 50 is the documented benchmark.

- **Optimization event** = whatever you selected as the optimization goal (purchases, leads, link clicks, etc.)
- If the optimization event is rare (e.g., purchases with high AOV), exiting Learning Phase takes longer
- If the ad set cannot reach 50 events in 7 days, it enters **Learning Limited** status

### Learning Limited

Learning Limited means the ad set is unlikely to exit Learning Phase given current settings. Common causes:
- Budget too low relative to the optimization event cost
- Audience too narrow
- Too many ad sets splitting the budget
- Optimization event too rare (e.g., Purchase when most traffic is top-of-funnel)

### Triggers That RESET Learning Phase

These edits restart the learning counter from zero:

| Trigger | Threshold | Impact |
|---------|-----------|--------|
| **Budget change** | >20% increase or decrease | Full reset |
| **Targeting edit** | Any change to audiences, locations, demographics | Full reset |
| **Creative edit** | New creative, changed copy, new image/video | Full reset |
| **Optimization event change** | Switching from Clicks to Conversions, etc. | Full reset |
| **Bid strategy change** | Switching from Lowest Cost to Cost Cap, etc. | Full reset |
| **Adding new ad to ad set** | Adding a new ad creative | Full reset |
| **Pausing for 7+ days** | Extended pause period | Full reset on resume |
| **Placement edit** | Adding or removing placements | Full reset |

### What Does NOT Reset Learning

- Minor budget adjustments (<=20%)
- Changing the ad set name
- Changing the campaign name
- Updating the schedule end date (if not shortening significantly)
- Viewing or downloading reports

### Cost Implications During Learning

During Learning Phase:
- CPA is typically **20-50% higher** than post-learning steady state
- Delivery is inconsistent (spiky spend patterns)
- ROAS is artificially depressed
- These metrics should NOT be used for performance evaluation

### Recommended Budget for Exiting Learning

**Budget >= 50 x Target CPA per week per ad set**

Example: If target CPA is R$50, the ad set needs at least R$2,500/week budget to have a reasonable chance of exiting Learning Phase.

## Agent Rules

| Agent | Load Condition |
|-------|----------------|
| @performance-analyst | **CRITICAL**: MUST load and check learning phase status BEFORE any kill/scale recommendation. If ad set is in Learning Phase --> BLOCK all modification recommendations |
| @campaign-manager | Before executing any campaign edit that could trigger a learning reset. Must warn about reset impact |
| @ad-midas | When user asks about volatile performance on new or recently edited campaigns |
| @budget-optimizer | Before any budget adjustment. Must calculate if change exceeds 20% threshold |

**Load method:** On-demand via Read tool. This is one of the most frequently loaded knowledge docs.

**CRITICAL RULE:** If an ad set is in Learning Phase, the only acceptable agent action is to WAIT. No budget changes, no targeting edits, no creative swaps. The sole exception is pausing a campaign that is clearly violating policy or burning budget with zero results after 2x the expected learning period.

## Red Flags

- NEVER recommend killing or scaling an ad set that is still in Learning Phase
- NEVER make budget changes >20% on an ad set that hasn't exited Learning Phase
- NEVER evaluate CPA/ROAS during Learning Phase as representative of long-term performance
- NEVER stack multiple edits (targeting + creative + budget) simultaneously -- each one resets Learning independently, compounding the damage
- NEVER recommend "just pause and restart" as a performance fix -- this resets Learning Phase entirely
- NEVER ignore Learning Limited status -- it signals a structural problem (budget too low or audience too narrow) that won't resolve by waiting

## Sources

- Meta Business Help Center: "About the learning phase"
- Meta Marketing API: Delivery status fields (LEARNING, LEARNING_LIMITED, ACTIVE)
- mathiaschu/meta-ads-analyzer: `learning_phase.md` reference document
- Meta Ads Best Practices: "How to exit the learning phase faster"
