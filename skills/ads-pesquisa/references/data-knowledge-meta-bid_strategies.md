# Bid Strategies

## Summary

Meta offers three categories of bid strategies: Spend-based (Lowest Cost, Highest Value), Goal-based (Cost Cap, ROAS Goal, Bid Cap), and Manual (Manual Bid). The right strategy depends on account maturity, conversion volume, and business goals. New accounts should start with Lowest Cost to accumulate data; only migrate to goal-based strategies after achieving 30+ conversions per week.

## Deep Dive

### Bid Strategy Categories

#### 1. Spend-Based Strategies

These strategies focus on spending the full budget while maximizing results.

**Lowest Cost (Default)**
- Meta finds the cheapest conversions available
- No cost ceiling -- will spend the full budget
- Best for: new accounts, data accumulation, maximizing volume
- Risk: CPA can spike during high-competition periods (no cap)

**Highest Value**
- Optimizes for the highest-value conversions (requires value-based optimization)
- Spends full budget while maximizing total conversion value
- Best for: e-commerce with variable order values
- Requires: Purchase event with value parameter, sufficient value data

#### 2. Goal-Based Strategies

These strategies try to hit a specific performance target.

**Cost Cap**
- Sets a maximum average CPA target
- Meta aims to keep average CPA at or below the cap
- May underspend if the cap is too aggressive
- Best for: accounts with 30+ conversions/week and clear CPA targets
- Risk: severely limits delivery if cap is set too low

**ROAS Goal (Minimum ROAS)**
- Sets a minimum return on ad spend target
- Meta optimizes for conversions that meet or exceed the ROAS target
- Requires value-based optimization (purchase events with value)
- Best for: e-commerce with known margin thresholds
- Risk: limits delivery if ROAS target is too aggressive

**Bid Cap**
- Sets a hard maximum bid per auction (not an average)
- Meta will never exceed this bid in any single auction
- Most restrictive strategy -- can severely limit delivery
- Best for: brand campaigns with strict CPM targets, or when you need absolute cost control
- Risk: high risk of underspending if cap is too low

#### 3. Manual Bid

- Direct control over bid amount per auction
- Rarely used in modern Meta campaigns
- Exists primarily for API-level control in specific use cases
- Not recommended for most advertisers

### Decision Tree

```
START
  |
  v
Account has < 30 conversions/week?
  |-- YES --> Use LOWEST COST
  |           (accumulate data, let Meta learn)
  |
  |-- NO --> What is the primary goal?
              |
              |-- Volume at target CPA --> COST CAP
              |   (set cap at current CPA or 10-20% above)
              |
              |-- E-commerce ROAS --> ROAS GOAL
              |   (set target at breakeven ROAS or slightly above)
              |
              |-- Brand with CPM control --> BID CAP
              |   (set maximum you'll pay per impression/action)
              |
              |-- Maximum volume, no cap --> LOWEST COST
              |   (when budget IS the constraint)
              |
              |-- Maximize revenue --> HIGHEST VALUE
                  (requires purchase value data)
```

### Migration Path

The typical maturity path for bid strategy evolution:

```
PHASE 1: New Account (0-29 conversions/week)
  Strategy: Lowest Cost
  Goal: Accumulate conversion data, exit Learning Phase
  Duration: 2-6 weeks

PHASE 2: Data-Rich (30+ conversions/week)
  Strategy: Cost Cap (set at current average CPA)
  Goal: Maintain volume while controlling costs
  Duration: Ongoing, adjust cap quarterly

PHASE 3: Optimization (stable CPA, high volume)
  Strategy: ROAS Goal or Highest Value
  Goal: Maximize return, not just volume
  Duration: Ongoing
```

### Cost Cap Configuration Guidelines

| Scenario | Cost Cap Setting | Rationale |
|----------|-----------------|-----------|
| First time using Cost Cap | Current average CPA + 20% | Give algorithm room to learn |
| Stable performance | Current average CPA | Maintain efficiency |
| Want to scale volume | Current CPA + 10-30% | Accept higher CPA for more volume |
| Want to reduce CPA | Current CPA - 10% | Risk: may reduce delivery significantly |

### Key Behavioral Differences

| Behavior | Lowest Cost | Cost Cap | Bid Cap |
|----------|------------|----------|---------|
| Will spend full budget? | Yes | Not guaranteed | Not guaranteed |
| CPA stability | Low (fluctuates) | Medium (averages to target) | High (hard ceiling) |
| Volume | Maximum for budget | Medium | Lowest |
| Learning Phase exit | Fastest | Medium | Slowest |
| Risk of underspend | None | Medium | High |

## Agent Rules

| Agent | Load Condition |
|-------|----------------|
| @performance-analyst | When evaluating campaign bid strategy effectiveness or recommending strategy changes |
| @campaign-manager | When creating new campaigns (must select appropriate bid strategy based on decision tree) |
| @budget-optimizer | When optimizing spend efficiency or diagnosing underspend/overspend patterns |
| @ad-midas | When user asks about bid strategies, why CPA is fluctuating, or how to control costs |

**Load method:** On-demand via Read tool when bid strategy decisions are needed.

**Key rule:** ALWAYS check account conversion volume before recommending a bid strategy change. The decision tree starts with "does this account have 30+ conversions/week?" -- this is the foundational gate.

## Red Flags

- NEVER recommend Cost Cap or ROAS Goal for accounts with fewer than 30 conversions per week -- insufficient data for the algorithm to optimize against a target
- NEVER set Cost Cap below current average CPA without warning about delivery reduction
- NEVER switch bid strategies during Learning Phase -- this resets learning (see `learning_phase.md`)
- NEVER use Bid Cap as the default strategy -- it's the most restrictive and causes the most underspend issues
- NEVER recommend Highest Value without confirming purchase value data is being passed via pixel/CAPI
- NEVER change bid strategy and budget simultaneously -- isolate variables to understand impact

## Sources

- Meta Business Help Center: "About bid strategies"
- Meta Business Help Center: "Choose the right bid strategy"
- Meta Ads API: Campaign bid_strategy field documentation
- mathiaschu/meta-ads-analyzer: `bid_strategies.md` reference document
- amekala/ads-mcp: Bidding Strategy Decision Tree
