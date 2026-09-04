# Campaign Planning Pack Task

Canonical planning task for the `copy` squad. Use this task whenever a workflow needs persisted campaign artifacts before copy production or `FINAL` promotion.

## Metadata

```yaml
task:
  name: Campaign Planning Pack
  id: campaign-planning-pack
  version: "1.0.0"
  category: strategy
  estimated_time: "30-60 min"
  primary_agents:
    - copy-chief
    - dan-kennedy
    - todd-brown
    - stefan-georgi
  outputs:
    - campaign-brief.yaml
    - message-architecture.yaml
    - creative-brief.yaml
    - assets/asset-brief-*.yaml
```

---

## Purpose

Turn diagnostics, offer truth, and route decisions into the canonical planning bundle used by the `copy` operating model:

1. `Campaign Brief`
2. `Message Architecture`
3. `Creative Brief`
4. `Asset Briefs`

This task is the planning source of truth for campaign-level copy execution. It is not a replacement for specific craft frameworks like RMBC. Those may support production after the planning pack exists.

---

## Required Inputs

```yaml
required:
  - outputs/workspace-context/campaign-context-brief.yaml
  - business_slug
  - product_slug
  - campaign_slug
  - selected_workflow
  - offer_truth
  - audience_truth

recommended:
  - awareness_diagnosis
  - market_sophistication
  - unique_mechanism
  - proof_inventory
  - channel_constraints
  - existing_delivery_artifacts
```

---

## Workflow

### Step 1: Normalize Campaign Scope

Define the execution boundary before planning:

- campaign objective
- commercial moment
- channel mix
- primary conversion event
- delivery route for this workflow

If the campaign is missing a persisted `campaign_slug`, stop `FINAL` promotion and mark the work as draft-only.

### Step 2: Write `campaign-brief.yaml`

Capture:

- business, product, and campaign identifiers
- objective and success metric
- target audience and awareness stage
- offer, price point, and conversion event
- constraints, dependencies, and required proofs
- workflow route and delivery expectations

### Step 3: Write `message-architecture.yaml`

Define the message system for the campaign:

- core promise
- problem framing
- unique mechanism or differentiator
- proof hierarchy
- objection priorities
- tone and language guardrails
- message priority by channel or asset

### Step 4: Write `creative-brief.yaml`

Translate strategy into execution direction:

- creative angle
- headline territories
- emotional posture
- required claims and forbidden shortcuts
- narrative constraints
- review expectations for copy, brand, and compliance

### Step 5: Write Asset Briefs

Create one `assets/asset-brief-*.yaml` per required deliverable in the route.

Minimum route expectations:

- `wf-1-full-launch`
  - `assets/asset-brief-main-asset.yaml`
  - `assets/asset-brief-email.yaml`
- `wf-2-paid-traffic`
  - `assets/asset-brief-ads.yaml`
  - `assets/asset-brief-landing-page.yaml`
- `wf-3-high-ticket`
  - `assets/asset-brief-application.yaml`
  - `assets/asset-brief-webinar.yaml`
  - `assets/asset-brief-email.yaml`
- `wf-5-email-marketing`
  - `assets/asset-brief-email.yaml`
- `wf-6-funnel-optimization`
  - `assets/asset-brief-optimization.yaml`

Each asset brief should define:

- asset objective
- audience slice
- input dependencies
- required sections or beats
- proof and CTA expectations
- delivery path under `outputs/copy/{business}/`

---

## Output Contract

The planning pack is complete only when all required files exist inside:

`{pasta}/copy/{campaign_slug}/`

Expected files:

```yaml
campaign:
  - campaign-brief.yaml
  - message-architecture.yaml
  - creative-brief.yaml
assets:
  - assets/asset-brief-*.yaml
```

---

## Quality Checklist

- [ ] `campaign_slug` is explicit for strategic or `FINAL` work.
- [ ] `campaign-brief.yaml` defines objective, audience, offer, and success metric.
- [ ] `message-architecture.yaml` defines promise, mechanism, proof hierarchy, and objections.
- [ ] `creative-brief.yaml` translates strategy into execution direction.
- [ ] Every asset required by the route has an `asset-brief`.
- [ ] Planning files point to real upstream truth and do not invent missing facts.

---

## Guardrails

1. Do not treat RMBC, Schwartz, Kennedy, or any legacy framework as the planning source of truth by itself.
2. Do not skip asset briefs for multi-asset campaigns.
3. Do not promote to `FINAL` when campaign planning is still implicit.
4. If the offer or proof is unclear, log the blocker instead of guessing.
