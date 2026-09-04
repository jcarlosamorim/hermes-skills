# Breakdown Effect

## Summary

Meta's breakdown metrics (by age, gender, placement, device, etc.) do NOT sum to the campaign/ad set total. This is because Meta's delivery system allocates impressions differently when segmenting, and overlap between breakdown dimensions means the same conversion can appear in multiple segments. Breakdowns are diagnostic tools, not decision-making anchors.

## Deep Dive

### Why Breakdowns Don't Sum to Total

When you request a breakdown by age or gender, Meta's reporting system retroactively attributes each impression, click, or conversion to a segment. However, several factors cause discrepancies:

1. **Delivery Optimization vs. Reporting Segmentation** -- Meta's algorithm optimizes delivery holistically across all audiences. It does NOT run separate mini-campaigns per segment. When you break down by age group, you're slicing the results of a unified delivery system, not viewing independent experiments.

2. **Cross-Device Attribution** -- A user might see an ad on mobile (attributed to "Mobile" placement) and convert on desktop (attributed to "Desktop" placement). The total counts one conversion, but placement breakdowns might attribute fragments differently depending on the attribution model.

3. **Overlap Between Dimensions** -- A single impression belongs to one age group AND one gender AND one placement simultaneously. When breakdowns are requested across multiple dimensions, the interaction effects create apparent discrepancies.

4. **Statistical Sampling** -- For large accounts, Meta uses sampling for breakdown-level reporting. The sampled breakdown estimates may not perfectly reconstruct the exact total.

5. **Time Zone and Reporting Lag** -- Breakdown data may be computed at slightly different times than aggregate data, causing minor mismatches during active delivery periods.

### Practical Example

A campaign shows 100 conversions total. Breaking down by age:
- 18-24: 22 conversions
- 25-34: 35 conversions
- 35-44: 28 conversions
- 45-54: 12 conversions
- 55-64: 5 conversions
- 65+: 2 conversions
- Sum: 104 conversions

The 4-conversion discrepancy is normal. It does NOT indicate a bug or data quality issue.

### When Breakdowns ARE Useful

- Identifying which demographics respond best (directional signal)
- Spotting placement-level creative fatigue (e.g., Stories CTR declining while Feed holds)
- Understanding device distribution for creative optimization
- Informing future targeting decisions with directional data

### When Breakdowns Are DANGEROUS

- Making kill/scale decisions based on a single breakdown dimension
- Concluding "age 55+ doesn't work" from a small sample within a breakdown
- Reallocating budget based on breakdown-level CPA without considering delivery dynamics

## Agent Rules

| Agent | Load Condition |
|-------|----------------|
| @performance-analyst | When analyzing campaign performance by segments, before any segment-level recommendation |
| @ad-midas | When user asks "why don't my breakdown numbers add up" or requests segment analysis |
| @creative-analyst | When evaluating placement-level creative performance |

**Load method:** On-demand via Read tool when breakdown analysis is requested.

## Red Flags

- NEVER make kill/scale decisions based solely on breakdown data
- NEVER conclude a demographic "doesn't work" from breakdown-level metrics alone
- NEVER reallocate budget between segments based purely on breakdown CPA differences
- NEVER present breakdown totals as if they should match aggregate totals -- explain the discrepancy proactively
- NEVER combine multiple breakdown dimensions (age x gender x placement) and treat the resulting micro-segments as statistically significant

## Sources

- Meta Business Help Center: "About breakdowns in Ads reporting"
- Meta Marketing API Documentation: Insights endpoint breakdown parameters
- mathiaschu/meta-ads-analyzer: `breakdown_effect.md` reference document
- Meta Ads Auction and Delivery System whitepaper (2024)
