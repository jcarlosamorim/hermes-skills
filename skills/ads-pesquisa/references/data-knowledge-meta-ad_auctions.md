# Ad Auctions

## Summary

Meta uses an auction system to determine which ad is shown to each user. The winning ad is NOT simply the highest bidder -- Meta calculates a Total Value score combining the advertiser's bid, the estimated action rate (how likely the user is to take the desired action), and user value (ad quality and relevance). This means a great creative with a lower bid can beat a poor creative with a higher bid.

## Deep Dive

### The Total Value Formula

Every time an impression opportunity arises, Meta calculates a Total Value score for each eligible ad:

```
Total Value = (Advertiser Bid x Estimated Action Rate) + User Value
```

| Component | What It Measures | Who Controls It |
|-----------|-----------------|-----------------|
| **Advertiser Bid** | How much the advertiser is willing to pay for the desired action | Advertiser (bid strategy + budget) |
| **Estimated Action Rate** | Probability that this specific user will take the desired action (click, convert, etc.) | Meta's ML models (influenced by creative quality and targeting relevance) |
| **User Value** | Ad quality score based on user feedback signals (hides, reports, engagement history) | Creative quality, relevance to audience, landing page experience |

The ad with the highest Total Value wins the auction and gets the impression.

### Why This Matters

The formula has a profound implication: **you cannot simply outbid competitors to win auctions.** An ad with poor creative (low Estimated Action Rate and User Value) would need to bid significantly more to overcome the quality disadvantage.

Conversely, an advertiser with excellent creative can win auctions at lower CPMs because their Estimated Action Rate and User Value components are higher.

### Estimated Action Rate

Meta's ML models predict the Estimated Action Rate using:

1. **User history** -- Has this user engaged with similar ads before? What's their general click/conversion behavior?
2. **Ad history** -- How has this specific ad (or similar ads from this advertiser) performed so far?
3. **Context** -- Time of day, device, placement, connection type
4. **Creative signals** -- Image/video quality, text content, format type

This is why the same ad can have different effective bids for different users -- the Estimated Action Rate varies per user.

### User Value

User Value captures Meta's interest in showing high-quality ads that keep users on the platform:

- **Positive signals:** Likes, comments, shares, saves, long video views
- **Negative signals:** Hide ad, report ad, "not relevant" feedback
- **Quality signals:** Landing page load speed, post-click engagement, bounce rate

Ads with consistently negative user feedback see their User Value decline, effectively making them more expensive to deliver.

### Auction Dynamics

**Second-Price Auction (Modified)**

Meta uses a modified version of the Vickrey-Clarke-Groves (VCG) auction:
- The winner pays slightly more than the minimum needed to beat the second-highest Total Value
- This means you often pay LESS than your maximum bid
- The actual cost depends on the competitive landscape, not just your bid

**Auction Frequency**

Auctions happen billions of times per day, for every impression opportunity. Each auction is independent and considers the current state of all eligible ads.

**Eligibility Filtering**

Before the auction, Meta filters eligible ads based on:
1. Targeting criteria match (does this user fit the audience definition?)
2. Budget availability (does the ad set have remaining budget?)
3. Frequency caps (has this user seen the ad too many times?)
4. Policy compliance (is the ad approved and active?)
5. Pacing considerations (should this ad compete right now given its pacing schedule?)

### Practical Implications for Campaign Management

| Principle | Implication |
|-----------|-------------|
| Creative quality directly affects CPM | Investing in creative reduces cost per impression |
| Estimated Action Rate is per-user | The same ad costs different amounts for different users |
| User Value penalizes bad ads | Poor ads become exponentially more expensive over time |
| Second-price mechanism | You usually pay less than your bid |
| Broad targeting can improve auction | More eligible auctions = more chances to find cheap wins |

### Relationship to Other Knowledge Docs

- **Relevance Diagnostics** (`ad_relevance_diagnostics.md`): The three rankings directly influence Estimated Action Rate and User Value
- **Bid Strategies** (`bid_strategies.md`): The Advertiser Bid component is controlled by your chosen bid strategy
- **Pacing** (`pacing.md`): The pacing multiplier adjusts the effective bid throughout the day
- **Auction Overlap** (`auction_overlap.md`): When your own ads compete in the same auction

## Agent Rules

| Agent | Load Condition |
|-------|----------------|
| @performance-analyst | When analyzing why CPMs are high or why ads are losing auctions. Understanding Total Value helps diagnose the specific weak component |
| @creative-analyst | When justifying creative investment. This doc proves that creative quality directly reduces costs |
| @campaign-manager | When setting up new campaigns. Understanding auction mechanics informs targeting and bidding decisions |
| @ad-midas | When user asks "why are my ads so expensive" or "how does Meta decide which ad to show" |

**Load method:** On-demand via Read tool. Foundational knowledge that supports analysis from other docs.

## Red Flags

- NEVER assume higher bids automatically win auctions -- Total Value includes creative quality and relevance
- NEVER ignore creative quality when trying to reduce CPMs -- it's 2/3 of the Total Value formula
- NEVER treat all users as having the same cost -- Estimated Action Rate varies per user, making some users naturally cheaper to convert
- NEVER optimize only on bid/budget levers while ignoring creative and targeting -- auction mechanics make all three interdependent
- NEVER assume a winning ad today will win tomorrow -- auction dynamics are real-time and competitive landscape shifts constantly

## Sources

- Meta Business Help Center: "About Meta ad auctions"
- Meta Engineering Blog: "Ad auction and delivery system design" (2021)
- Meta Marketing API: Campaign delivery and auction documentation
- mathiaschu/meta-ads-analyzer: `ad_auctions.md` reference document
- VCG Auction Theory: Vickrey-Clarke-Groves mechanism applied to digital advertising
