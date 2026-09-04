# STRATEGY.md — Campaign Strategy Directives

> **INSTRUCTIONS FOR AGENTS:** Read this file FIRST before any campaign action.
> This is the single source of truth for strategic direction.
> Updated by @ad-midas. Consulted by ALL agents before decisions.

---

## Template Info

| Campo | Valor |
|-------|-------|
| **Business** | {empresa_slug} |
| **Created** | {date} |
| **Last Updated** | {date} |
| **Updated By** | @ad-midas |

**Path:** `{pasta}/ads/STRATEGY.md`

**Story:** SAIOX-ADS-V5-2.4 (AC5)

---

## Active Directives

### PREFER

Directives that agents SHOULD follow when making decisions. Use these as defaults unless data contradicts.

| # | Directive | Rationale | Added |
|---|-----------|-----------|-------|
| 1 | {Example: PREFER video over static for cold traffic} | {Higher engagement in this niche} | {date} |

### AVOID

Patterns, strategies, or actions that have been tested and failed, or carry unacceptable risk.

| # | Directive | Rationale | Added |
|---|-----------|-----------|-------|
| 1 | {Example: AVOID broad targeting on accounts < 90 days} | {Triggers Meta moderation AI} | {date} |

### CONSTRAINT

Hard limits that agents MUST NOT violate. Override PREFER if conflict exists.

| # | Constraint | Source | Added |
|---|------------|--------|-------|
| 1 | Max budget increase: +20%/day | safety-rules.yaml | {date} |
| 2 | All campaigns created PAUSED | safety-rules.yaml | {date} |
| 3 | WAL entry required before any API write | safety-rules.yaml | {date} |

---

## Decision Log

Chronological record of strategic decisions. Append-only -- never delete entries.

| Date | Decision | Agent | Rationale |
|------|----------|-------|-----------|
| {date} | {Example: Switch from ABO to CBO} | @ad-midas | {Example: Account matured past 90 days, 5+ adsets performing well} |

---

## Campaign Priorities

Current priority order for active campaigns. Updated weekly by @ad-midas.

| Priority | Campaign | Objective | Status |
|----------|----------|-----------|--------|
| P1 | {campaign_slug} | {objetivo} | {active/paused/learning} |

---

## Notes

> Additional strategic context that doesn't fit the structured sections above.
> Keep concise. If it grows past 10 lines, create a dedicated doc.

---

_Template: STRATEGY.md (ads-mcp pattern) | @ad-midas_
