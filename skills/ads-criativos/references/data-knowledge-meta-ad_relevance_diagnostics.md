# Ad Relevance Diagnostics

## Summary

Meta provides three quality rankings for every ad: Quality Ranking, Engagement Rate Ranking, and Conversion Rate Ranking. Each is rated as Above Average, Average, or Below Average relative to ads competing for the same audience. These diagnostics reveal WHY an ad is underperforming and guide targeted fixes rather than blind creative iteration.

## Deep Dive

### The Three Rankings

| Ranking | Measures | Based On |
|---------|----------|----------|
| **Quality Ranking** | Perceived quality of the ad compared to competitors | User feedback signals: hide, report, low-quality indicators. Higher quality = fewer negative signals |
| **Engagement Rate Ranking** | Expected engagement rate (clicks, reactions, comments, shares) compared to competitors | Historical engagement data for ads targeting the same audience |
| **Conversion Rate Ranking** | Expected conversion rate compared to competitors targeting the same optimization goal | Historical conversion data for ads with the same optimization event |

### How Rankings Affect Delivery

These rankings feed directly into Meta's auction system. The Total Value formula includes:

```
Total Value = (Advertiser Bid x Estimated Action Rate) + User Value
```

- **Engagement Rate Ranking** influences the Estimated Action Rate
- **Quality Ranking** influences User Value (Meta penalizes low-quality ads to protect user experience)
- **Conversion Rate Ranking** influences Estimated Action Rate for conversion-optimized campaigns

A high-quality ad with a lower bid can beat a low-quality ad with a higher bid. This makes diagnostics directly actionable for cost reduction.

### Diagnostic Interpretation Matrix

| Quality | Engagement | Conversion | Diagnosis | Action |
|---------|------------|------------|-----------|--------|
| Above | Above | Above | Excellent. Ad is performing well across all dimensions | Scale budget, test new audiences |
| Below | Above | Above | Creative looks spammy or clickbaity but users who click do convert | Improve visual quality, reduce sensationalist copy, maintain the value proposition |
| Above | Below | Above | Ad is high quality but not engaging. Users who do engage, convert well | Test more attention-grabbing hooks, stronger CTAs, dynamic formats (video, carousel) |
| Above | Above | Below | Ad attracts attention but doesn't convert. Targeting mismatch or landing page issue | Review landing page, check audience-offer alignment, verify pixel/CAPI setup |
| Below | Below | Above | Poor creative drives away most users, but the rare engager converts. Niche appeal | Complete creative overhaul while preserving the core value proposition |
| Below | Below | Below | Fundamental problem. Ad, offer, targeting, or landing page is fundamentally broken | Full diagnostic: review offer-market fit, targeting, creative, landing page. Consider pausing |
| Above | Below | Below | High quality creative that nobody clicks or converts. Wrong audience or weak offer | Targeting is likely the issue. Test different audiences, review offer strength |
| Below | Above | Below | Low quality creative that generates curiosity clicks but no conversions. Clickbait pattern | Align creative promise with actual offer. Improve landing page experience |

### Minimum Data Requirements

Rankings only appear after an ad has accumulated sufficient impressions (typically 500+ impressions). Below that threshold, rankings show as "--" or "Not enough data."

### Ranking Refresh Frequency

Rankings are recalculated continuously but visible updates in Ads Manager typically lag by 24-48 hours. Do not make rapid creative changes based on rankings that may not yet reflect recent delivery patterns.

### Relationship to Ad Fatigue

As an ad ages and frequency increases:
- Engagement Rate Ranking tends to decline first (users stop clicking familiar ads)
- Quality Ranking may decline as users start hiding the ad
- Conversion Rate Ranking is often the last to decline (committed audiences still convert)

This pattern is a leading indicator of creative fatigue.

## Agent Rules

| Agent | Load Condition |
|-------|----------------|
| @performance-analyst | When diagnosing underperforming ads. Use the diagnostic matrix to guide root cause analysis |
| @creative-analyst | When evaluating creative quality and recommending iterations. Rankings indicate WHAT to fix |
| @ad-midas | When user asks "why isn't my ad working" or "how do I improve my ad quality" |

**Load method:** On-demand via Read tool during ad-level performance analysis.

**Key rule:** Always present the three rankings TOGETHER with the diagnostic interpretation. A single ranking in isolation is misleading.

## Red Flags

- NEVER evaluate ad quality based on a single ranking in isolation -- always consider all three together
- NEVER make creative changes based on rankings with insufficient data (<500 impressions)
- NEVER ignore the Below/Below/Below pattern -- it indicates fundamental issues that creative iteration alone won't fix
- NEVER confuse Quality Ranking with Relevance Score (deprecated in 2019). They are different systems
- NEVER assume "Above Average" on all three means the ad cannot be improved -- it means it's competitive, not optimal
- NEVER react to ranking changes within 24 hours of a creative edit -- allow recalculation time

## Sources

- Meta Business Help Center: "About ad relevance diagnostics"
- Meta Ads API: Ad-level fields for quality_ranking, engagement_rate_ranking, conversion_rate_ranking
- mathiaschu/meta-ads-analyzer: `ad_relevance_diagnostics.md` reference document
- Meta Marketing Science: "Understanding Ad Quality Signals" (2024)
