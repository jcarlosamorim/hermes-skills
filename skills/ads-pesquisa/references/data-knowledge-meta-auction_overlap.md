# Auction Overlap

## Summary

Auction overlap occurs when your own ad sets compete against each other in the same Meta auction. This happens when multiple ad sets target overlapping audiences, effectively bidding against yourself. It wastes budget, inflates CPMs, and fragments data that the algorithm needs to optimize. Meta provides an Audience Overlap tool to detect this, and agents should recommend consolidation or mutual exclusions when overlap exceeds 30%.

## Deep Dive

### How Auction Overlap Works

Meta runs billions of auctions per day. Each time an impression opportunity arises for a user, all eligible ads compete. When two of YOUR ad sets target the same user, they enter the same auction. Meta then:

1. Selects the highest-performing ad set (by Total Value score) to compete
2. Suppresses the other ad set from that specific auction
3. The suppressed ad set loses an opportunity it could have won if it were the only one targeting that user

This suppression mechanism (called "auction deduplication") means you're NOT literally bidding against yourself in price -- but you ARE fragmenting your delivery and reducing the effective reach of each ad set.

### Why It's Harmful

1. **Fragmented Learning** -- Instead of one ad set getting 100 conversions to exit Learning Phase, two overlapping ad sets each get 50, potentially keeping both in Learning Limited status.

2. **Budget Inefficiency** -- Budget allocated to the suppressed ad set sits idle during overlapping auctions. Delivery becomes uneven.

3. **Inconsistent Optimization** -- The algorithm cannot learn efficiently when the same user pool is being targeted by competing ad sets with different optimization signals.

4. **Higher CPMs** -- In some cases, internal competition can inflate the effective cost per impression.

### Common Causes of Overlap

| Scenario | Example |
|----------|---------|
| Broad + narrow targeting | One ad set targets "all women 25-54", another targets "women 25-34 interested in yoga" |
| Retargeting + prospecting | Retargeting ad set captures users also in the prospecting audience |
| Lookalike audiences | 1% lookalike and 3% lookalike share significant overlap |
| Interest stacking | Multiple ad sets each targeting related interests with natural overlap |
| Duplicate campaigns | Legacy campaigns left running alongside new ones |

### How to Detect Overlap

**Meta Audience Overlap Tool:**
1. Go to Audiences in Ads Manager
2. Select 2-5 saved audiences
3. Click "Show Audience Overlap"
4. Review the percentage overlap between each pair

**Via API (MCP tools):**
- Use audience size estimates to calculate theoretical overlap
- Compare audience definitions programmatically
- Track delivery metrics: if two ad sets show similar frequency patterns, suspect overlap

### Overlap Severity Scale

| Overlap % | Severity | Action |
|-----------|----------|--------|
| 0-15% | Low | Monitor, no action needed |
| 15-30% | Moderate | Watch for Learning Phase issues, consider future consolidation |
| 30-50% | High | Recommend consolidation or mutual audience exclusions |
| 50%+ | Critical | Immediate consolidation required. Merge ad sets or implement hard exclusions |

### Remediation Strategies

1. **Consolidation** -- Merge overlapping ad sets into a single ad set with broader targeting. Let Meta's algorithm handle the sub-segmentation.

2. **Mutual Exclusions** -- Exclude Custom Audiences from each ad set to create non-overlapping pools. Example: exclude retargeting audience from prospecting ad sets.

3. **Campaign Budget Optimization (CBO)** -- Move overlapping ad sets into a single CBO campaign. Meta will allocate budget dynamically, reducing the impact of overlap.

4. **Advantage+ Audience** -- Consider using Advantage+ targeting which lets Meta expand beyond your defined audiences, reducing the impact of manual overlap.

## Agent Rules

| Agent | Load Condition |
|-------|----------------|
| @performance-analyst | During periodic campaign health checks (weekly minimum). Check overlap when multiple ad sets exist with similar targeting |
| @campaign-manager | Before creating new ad sets. Must evaluate overlap with existing ad sets before launch |
| @ad-midas | When user reports "my campaigns seem to be competing with each other" or asks about audience strategy |

**Load method:** On-demand via Read tool during campaign structure reviews.

**Periodic check:** @performance-analyst should flag overlap check as part of the weekly digest if the account has 3+ active ad sets.

## Red Flags

- NEVER launch a new ad set without checking overlap against existing active ad sets
- NEVER ignore overlap >30% -- it directly impacts budget efficiency and Learning Phase exit
- NEVER create multiple ad sets targeting the same Lookalike audience at different percentages without exclusions
- NEVER assume CBO alone solves overlap -- it helps but doesn't eliminate the underlying audience fragmentation
- NEVER split audiences into micro-segments "for testing" without understanding the overlap implications on Learning Phase

## Sources

- Meta Business Help Center: "About audience overlap"
- Meta Ads Manager: Audience Overlap tool documentation
- mathiaschu/meta-ads-analyzer: `auction_overlap.md` reference document
- Meta Best Practices: "How to structure campaigns to avoid auction overlap"
