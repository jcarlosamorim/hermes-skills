---
task_id: run-research-protocol
version: 1.0
category: ads_research
squad: hybrid-ads
agent: ad-midas
elicit: false
templates:
  - research-brief.md
  - strategy.md
references:
  - templates/business-profile.yaml
  - templates/product-card.yaml
  - templates/icp-profile.yaml
  - data/industry-templates/
  - data/knowledge/meta/
---

# Run Research Protocol — 5-Phase Autonomous Research

> **Type:** Autonomous task (elicit: false)
> **Version:** 1.0.0
> **Agent:** @ad-midas (concierge, executes autonomously)
> **Output:** `research-brief-{campaign_slug}.md` saved to campaign folder

---

## Overview

This task implements the 5-Phase Research Protocol. After receiving business context (slug), @ad-midas runs all phases autonomously without user interaction. The output is a populated research brief that informs campaign strategy.

**Prerequisites:**
- `{pasta}/ads/business-profile.yaml` must exist (run `setup-business-profile` first)
- At least one product card in `{pasta}/ads/products/`
- At least one ICP profile in `{pasta}/ads/icps/`

---

## Input

The task requires a single input: the business slug.

```
Usage: run-research-protocol {business_slug}
Example: run-research-protocol bilhon
```

The agent derives all context from the workspace files.

---

## Process

### Phase 1 — Load Context

**Goal:** Assemble all business data into working memory.

**Steps:**

1. Read `{pasta}/ads/business-profile.yaml`
   - Extract: company, identity, market, ad_history, assets
   - HALT if file not found: "Business profile missing. Run setup-business-profile first."

2. Read `{pasta}/ads/STRATEGY.md` (if exists)
   - Extract: active directives (PREFER/AVOID/CONSTRAINT), campaign priorities
   - If not found: note as "first campaign -- no prior strategy"

3. Read first product card from `{pasta}/ads/products/`
   - Extract: product, benefits, common_objections, social_proof
   - HALT if no product cards: "No product cards found. Run setup-business-profile first."

4. Read first ICP profile from `{pasta}/ads/icps/`
   - Extract: demographics, psychographics, primary_pain, desired_outcome
   - HALT if no ICP profiles: "No ICP profiles found. Run setup-business-profile first."

5. Load industry template from `references/industry-templates/{segment}.yaml`
   - Match business-profile.company.segment to template filename
   - If no exact match: load `generic.yaml` as fallback
   - Extract: benchmarks, recommended funnels, creative patterns

**Phase 1 Output:** Business context fully loaded in working memory.

---

### Phase 2 — Brand Website Crawl

**Goal:** Analyze the brand website to understand live positioning, products, and trust signals.

**Tool:** WebFetch

**Steps:**

1. Fetch `business-profile.company.site` (main website)
   - Extract: page title, meta description, H1s, main CTA, product listings, pricing
   - Note: trust signals (SSL, testimonials, social proof, guarantees)
   - Note: gaps (missing elements that could hurt ad performance)

2. If `product.sales_url` differs from main site: fetch that too
   - Analyze: checkout flow, urgency elements, objection handling on page
   - Note: friction points that could hurt conversion after ad click

3. Check for Facebook Pixel presence in page source
   - Look for: `fbq(`, `connect.facebook.net`, pixel ID
   - If found: note as "Pixel detected on site"
   - If not found: note as gap "No Facebook Pixel detected on landing page"

**Phase 2 Output:** Populate Section 1 (Brand Analysis) of research-brief.

---

### Phase 3 — Competitor Research

**Goal:** Analyze 3-5 competitors to understand market positioning, pricing, and ad strategies.

**Tools:** WebSearch, WebFetch

**Steps:**

1. Build competitor list from `business-profile.market.direct_competitors`
   - Use the names and sites provided during onboarding
   - If fewer than 3 competitors listed: use WebSearch to find additional competitors
     - Query: "{segment} {sub_segment} competitors Brasil" or equivalent

2. For each competitor (3-5 max):
   a. WebFetch their website
      - Extract: pricing, value proposition, main CTA, trust signals
   b. WebSearch for their Meta Ad Library presence
      - Query: "site:facebook.com/ads/library {competitor_name}"
      - Note: active ad count, dominant formats, creative angles, duration running
   c. WebSearch for reviews/reputation
      - Query: "{competitor_name} reclame aqui" or "{competitor_name} reviews"
      - Note: rating, common complaints, strengths mentioned

3. Synthesize competitor insights:
   - Most common creative format across competitors
   - Dominant messaging pattern (pain-focused / result-focused / authority-focused)
   - Pricing range across market
   - Gaps: what NO competitor is doing or communicating

**Phase 3 Output:** Populate Section 2 (Competitive Landscape) of research-brief.

---

### Phase 4 — Differentiation Mapping

**Goal:** Identify unique angles and underserved opportunities based on Phase 1-3 data.

**Tool:** Analysis (no external tools -- pure reasoning from collected data)

**Steps:**

1. Compare business strengths (from business-profile + product-card) against competitor weaknesses (from Phase 3)
   - What does THIS business offer that competitors DON'T?
   - What does THIS business communicate that competitors IGNORE?

2. Identify underserved audience segments
   - Cross-reference ICP with competitor targeting patterns
   - Find segments that competitors serve poorly or not at all

3. Map unexplored creative angles
   - Angles present in the business data but absent from competitor ads
   - Format gaps (e.g., competitors all use static images, video is unexplored)
   - Messaging gaps (e.g., competitors focus on features, nobody addresses emotional pain)

4. Rank opportunities by potential impact
   - High: unique + underserved + clear proof available
   - Medium: partially unique + some proof
   - Low: common but better executed

**Phase 4 Output:** Populate Section 3 (Differentiation Map) of research-brief.

---

### Phase 5 — Ad Intelligence

**Goal:** Pull existing performance data OR establish industry benchmarks.

**Conditional logic based on `business-profile.ad_history.has_advertised`:**

#### Path A: Business HAS ad history (has_advertised = true)

**Tool:** MCP (get_insights via Pipeboard, if platform-status.yaml shows OK)

1. If `platform-status.yaml` exists and meta.status = OK:
   - Call `get_insights` for account-level data (last 90 days)
   - Extract: total spend, avg CPA, ROAS, CTR, CPM, top campaigns
   - Identify: best performing campaign (lowest CPA or highest ROAS)
   - Identify: worst performing campaign (highest CPA or lowest ROAS)
   - Extract: winning creative patterns (what worked)
   - Extract: failed creative patterns (what didn't)

2. If MCP not available or no data returned:
   - Fall back to Path B (industry benchmarks)
   - Note: "Historical data requested but MCP unavailable -- using industry benchmarks as fallback"

#### Path B: Business has NO ad history (has_advertised = false)

**Tool:** Industry template from Phase 1

1. Load benchmarks from the matched industry template
   - Extract: CPA range, ROAS range, CTR range, CPM range, conversion rate
   - Note source as "Industry benchmark -- {template_name}"

2. If `generic.yaml` was used: add note "Cross-industry averages -- refine after first campaign data"

**Phase 5 Output:** Populate Section 4 (Ad Intelligence) of research-brief.

---

## Post-Processing

After all 5 phases complete:

1. **Populate Section 5** (Research Summary and Recommendations)
   - Top 3 opportunities (from Phase 4 ranking)
   - Top 3 risks (from all phases -- gaps, competitor strengths, tracking issues)
   - Recommended first campaign (objective, funnel, primary angle, budget based on benchmarks + margin)

2. **Validate completeness**
   - Every section of research-brief must have at least 1 data point
   - If any section is empty: mark as "Insufficient data -- {reason}" (do NOT leave blank)

3. **Save output**
   - File: `research-brief-{campaign_slug}.md` (use product slug as campaign slug for first campaign)
   - Path: `{pasta}/ads/research/`
   - Create directory if it doesn't exist

4. **Initialize STRATEGY.md** (if it doesn't exist)
   - Copy template from `references/strategy.md`
   - Populate header fields (business, date)
   - Add CONSTRAINT entries from `config/safety-rules.yaml` defaults
   - Add first PREFER directives based on research findings
   - Save to `{pasta}/ads/STRATEGY.md`

---

## Output

| File | Path | Condition |
|------|------|-----------|
| Research Brief | `{pasta}/ads/research/research-brief-{campaign_slug}.md` | Always created |
| STRATEGY.md | `{pasta}/ads/STRATEGY.md` | Created only if it doesn't exist |

---

## Error Handling

| Error | Action |
|-------|--------|
| Business profile not found | HALT -- "Run setup-business-profile first" |
| No product cards found | HALT -- "Run setup-business-profile first (Phase 2)" |
| No ICP profiles found | HALT -- "Run setup-business-profile first (Phase 3)" |
| WebFetch fails on brand site | Log warning, skip Phase 2 site analysis, continue with profile data |
| WebSearch returns no results | Log warning, reduce competitor count, continue |
| WebFetch fails on competitor site | Skip that competitor, continue with others (min 2 competitors for valid analysis) |
| MCP not available for Phase 5 | Fall back to industry benchmarks (Path B) |
| Industry template not found | Use generic.yaml -- always available as fallback |
| Fewer than 2 competitors analyzed | Log warning in research brief, reduce confidence of competitive analysis |

---

## Timing Expectations

| Phase | Estimated Duration | Notes |
|-------|-------------------|-------|
| Phase 1 (Load) | < 5 seconds | Local file reads only |
| Phase 2 (Crawl) | 15-30 seconds | 1-2 WebFetch calls |
| Phase 3 (Research) | 60-120 seconds | Multiple WebSearch + WebFetch |
| Phase 4 (Mapping) | < 10 seconds | Pure analysis, no external calls |
| Phase 5 (Intel) | 10-30 seconds | 1 MCP call or template read |
| **Total** | **~2-4 minutes** | |

---

_Task: run-research-protocol v1.0 | @ad-midas_
