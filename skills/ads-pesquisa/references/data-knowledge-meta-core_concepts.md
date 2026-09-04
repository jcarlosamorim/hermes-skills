# Core Concepts

## Summary

This document covers the fundamental Meta advertising concepts that all agents must understand: the campaign structure hierarchy (Campaign > Ad Set > Ad), auction mechanics, the delivery system, optimization events, attribution windows, and the Advantage+ suite. These are the building blocks upon which all other knowledge documents and agent behaviors are built.

## Deep Dive

### Campaign Structure Hierarchy

Meta uses a three-level hierarchy for organizing ads:

```
CAMPAIGN (top level)
  |-- Objective (what you want to achieve)
  |-- Budget (optional: Campaign Budget Optimization)
  |-- Bid Strategy
  |
  |-- AD SET (middle level)
  |     |-- Targeting (audiences, locations, demographics)
  |     |-- Budget (if not using CBO)
  |     |-- Schedule (start/end dates, dayparting)
  |     |-- Placements (Feed, Stories, Reels, etc.)
  |     |-- Optimization Event (what to optimize for)
  |     |
  |     |-- AD (bottom level)
  |           |-- Creative (image, video, carousel, etc.)
  |           |-- Copy (headline, primary text, description)
  |           |-- CTA button
  |           |-- Destination URL
  |
  |-- AD SET 2
        |-- (different targeting, same or different creatives)
        |-- AD 3
        |-- AD 4
```

**Key rules:**
- Each campaign has exactly ONE objective
- Ad sets within a campaign share the same objective
- Ads within an ad set share the same targeting and budget
- Creative variation happens at the Ad level
- Targeting variation happens at the Ad Set level
- Strategic decisions happen at the Campaign level

### Campaign Objectives (ODAX)

Meta uses the Outcome-Driven Ad Experiences (ODAX) framework with 6 simplified objectives:

| Objective | Use Case | Optimization Events |
|-----------|----------|---------------------|
| **Awareness** | Brand reach, video views | Reach, Impressions, ThruPlay |
| **Traffic** | Drive website/app visits | Link Clicks, Landing Page Views |
| **Engagement** | Post engagement, page likes, event responses | Post Engagement, Page Likes |
| **Leads** | Form fills, Messenger conversations | Leads, Conversations |
| **App Promotion** | App installs, app events | App Installs, App Events |
| **Sales** | Purchases, add to cart, value optimization | Purchase, Add to Cart, Initiated Checkout |

### Optimization Events

The optimization event tells Meta's algorithm what success looks like. The algorithm then optimizes delivery toward users most likely to take that action.

**Event hierarchy (higher = harder to optimize for, requires more data):**

```
Impressions (easiest, most data)
  v
Link Clicks
  v
Landing Page Views
  v
Add to Cart
  v
Initiate Checkout
  v
Purchase (hardest, requires most data)
  v
Purchase with Value (requires conversion value)
```

**Rule of thumb:** Optimize for the lowest-funnel event that your ad set can generate 50+ of per week. If you can't get 50 purchases per week, optimize for Add to Cart instead.

### Attribution Windows

Attribution windows define the time period in which a conversion is attributed to an ad view or click.

**Default attribution window (as of 2024):**
- **7-day click** -- Conversion counted if user clicked the ad within the last 7 days
- **1-day view** -- Conversion counted if user viewed (but didn't click) the ad within the last 1 day

**Available configurations:**
| Window | Type | When to Use |
|--------|------|-------------|
| 1-day click | Click | Short purchase cycles (impulse buys, low-cost items) |
| 7-day click | Click | Standard e-commerce, lead gen (DEFAULT) |
| 1-day view | View | Brand awareness, high-frequency products |
| 7-day click + 1-day view | Combined | Standard full-funnel (DEFAULT) |
| 28-day click | Click | Long purchase cycles (B2B, high-value items) -- limited availability |

**Important:** Changing the attribution window does NOT change actual campaign performance -- it changes how conversions are COUNTED and REPORTED. A shorter window will show fewer conversions; a longer window will show more.

### The Delivery System

Meta's delivery system is the engine that decides which ad to show to which user at which time. It operates through:

1. **Targeting** -- Defines the eligible user pool
2. **Auction** -- Selects the winning ad for each impression (see `ad_auctions.md`)
3. **Pacing** -- Distributes budget across time (see `pacing.md`)
4. **Learning** -- Optimizes delivery based on accumulated data (see `learning_phase.md`)

The delivery system is NOT a simple matchmaker -- it actively predicts user behavior and optimizes in real-time.

### Campaign Budget Optimization (CBO)

CBO moves budget control from the Ad Set level to the Campaign level:

**Without CBO (Ad Set Budget):**
- Each ad set has its own budget
- You control exactly how much each ad set spends
- Requires manual reallocation between ad sets

**With CBO (Campaign Budget):**
- Single budget at campaign level
- Meta automatically allocates across ad sets
- Ad sets with better performance get more budget
- Minimum/maximum spend limits can be set per ad set

**When to use CBO:**
- Multiple ad sets with similar audiences (Meta optimizes allocation)
- When you trust the algorithm to find the best performers
- When managing 3+ ad sets per campaign

**When to use Ad Set Budget:**
- Specific budget requirements per audience
- Testing scenarios requiring equal spend per ad set
- When you need precise control over segment-level investment

### Advantage+ Suite

Advantage+ is Meta's automation layer that progressively removes manual controls in favor of algorithmic optimization.

| Feature | What It Does | Manual Equivalent |
|---------|-------------|-------------------|
| **Advantage+ Placements** | Meta chooses where to show ads (Feed, Stories, Reels, etc.) | Manual placement selection |
| **Advantage+ Audience** | Meta expands targeting beyond defined audiences when beneficial | Strict audience targeting |
| **Advantage+ Creative** | Meta auto-generates creative variations (format, text, enhancements) | Manual creative variants |
| **Advantage+ Shopping Campaigns** | Fully automated e-commerce campaigns (minimal input) | Manual campaign structure |
| **Advantage+ App Campaigns** | Fully automated app install campaigns | Manual app campaign structure |

**Key consideration:** Advantage+ features reduce manual control but often improve performance for accounts with sufficient data. They are NOT recommended for new accounts with no conversion history.

### Pixel and Conversions API (CAPI)

Meta tracks user actions through two complementary systems:

**Meta Pixel (Browser-side):**
- JavaScript code on your website
- Fires events when users take actions (page view, add to cart, purchase)
- Subject to browser restrictions (ITP, ad blockers, cookie deprecation)

**Conversions API (Server-side):**
- Server-to-server event transmission
- Not affected by browser restrictions
- Requires server-side implementation
- Recommended alongside Pixel for maximum data coverage

**Best practice:** Use BOTH Pixel and CAPI with deduplication enabled. Meta deduplicates events using event_id and event_name.

## Agent Rules

| Agent | Load Condition |
|-------|----------------|
| @ad-midas | Foundational context for any user interaction. Load when user is new or asks basic questions about campaign structure |
| @campaign-manager | When creating campaigns. This doc defines the structural rules that campaigns must follow |
| @performance-analyst | Reference for understanding how optimization events and attribution windows affect reported metrics |
| @creative-analyst | Understanding how the creative layer fits within the campaign hierarchy |

**Load method:** On-demand via Read tool. This is the foundational reference document -- other docs build upon these concepts.

## Red Flags

- NEVER create a campaign without a clear objective that maps to a business goal
- NEVER optimize for Purchase events if the ad set cannot generate 50+ per week -- use a higher-funnel event
- NEVER compare metrics across campaigns with different attribution windows without normalizing
- NEVER ignore the Pixel + CAPI dual setup -- browser-only tracking loses significant conversion data
- NEVER use Advantage+ Shopping Campaigns on accounts with zero conversion history -- the algorithm needs data to optimize
- NEVER set multiple optimization events within a single ad set -- each ad set has ONE optimization event

## Sources

- Meta Business Help Center: "Campaign structure"
- Meta Business Help Center: "About attribution settings"
- Meta Business Help Center: "About Advantage+ features"
- Meta Marketing API Documentation: Campaign, Ad Set, and Ad object schemas
- mathiaschu/meta-ads-analyzer: `core_concepts.md` reference document
- Meta Conversions API Documentation
