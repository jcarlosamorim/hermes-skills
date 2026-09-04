# Build Authority Arsenal - Credibility Elements Extraction Task

## Metadata
```yaml
task_id: build-authority-arsenal
version: 1.0.0
category: agent-creation
difficulty: advanced
elicit: true
dependencies:
  templates:
    - templates/authority-arsenal-tmpl.yaml
  reference:
    - agents/david-ogilvy.md # authority_proof_arsenal section
outputs:
  - Authority arsenal YAML file with:
    - Crucible story (4 acts)
    - Authority statistics
    - Notable products/clients
    - Proof stack templates (4+)
```

## Objective

Build a comprehensive authority proof arsenal that enables the copywriter agent to establish credibility naturally. This includes their origin story, verifiable achievements, notable work, and reusable proof templates.

**Why This Matters:** Authority is the foundation of persuasion. A copywriter agent without credibility elements will produce hollow, unpersuasive copy. This arsenal provides the "social proof layer" that makes every piece of copy more believable.

---

## PREREQUISITES

Before starting, ensure you have:

```
elicit: true
question: "Please confirm the following inputs are available:"
fields:
  - copywriter_name: "Full name of the copywriter"
  - slug: "Snake_case identifier (e.g., dan_koe)"
  - source_directory: "Path to source materials with autobiographical content"
  - psychometric_profile: "Path to psychometric profile JSON (optional but recommended)"
```

### Required Source Materials

| Material Type | Purpose | Minimum |
|--------------|---------|---------|
| Autobiographical content | Extract crucible story | 2+ files |
| Business/career mentions | Extract statistics | 3+ files |
| Product launches/offers | Notable products | 2+ files |
| Client results/testimonials | Notable clients | 1+ file |

### Quality Gate: Prerequisites

- [ ] Source directory exists with autobiographical content
- [ ] At least 2 files contain personal journey/story details
- [ ] At least 3 files contain business metrics or achievements
- [ ] Output directory exists at `outputs/minds/{slug}/analysis/`

---

## PHASE 1: EXTRACT CRUCIBLE STORY

### Objective
Build the copywriter's transformation narrative in 4 acts: Origin → Struggle → Breakthrough → Mastery.

### The 4-Act Structure

The crucible story follows a universal transformation arc:

```
ACT 1: ORIGIN
"Where they started - the humble/relatable beginning"

ACT 2: STRUGGLE
"The challenges, failures, dark night of the soul"

ACT 3: BREAKTHROUGH
"The turning point - what changed everything"

ACT 4: MASTERY
"Current state - where they are now as authority"
```

### Step 1.1: Scan for Autobiographical Content

Read ALL source files looking for:
- Personal history mentions
- "I used to..." or "When I started..." statements
- Failure stories
- Turning point narratives
- Achievement claims
- Timeline markers (years, ages)

Create extraction notes:

| Quote/Paraphrase | Source File | Act | Verified? |
|-----------------|-------------|-----|-----------|
| "[exact quote or close paraphrase]" | [filename] | 1/2/3/4 | ✅/❌ |

### Step 1.2: Build Act 1 - Origin

Extract the starting point of the copywriter's journey.

**Required Fields:**
```yaml
act_1_origin:
  year: "YYYY or YYYY-YYYY range"
  context: "[Starting situation - job, life circumstances]"
  key_event: "[What initiated the journey - inciting incident]"
  mindset: "[How they thought at this stage]"
  challenges:
    - "[Initial challenge 1]"
    - "[Initial challenge 2]"
  sources:
    - "[Source file 1]"
```

**Questions to Answer:**
- What was their life like before the transformation?
- What was their first job/career/situation?
- What made them start down this path?
- What did they believe at this stage?

### Step 1.3: Build Act 2 - Struggle

Extract the challenges, failures, and lessons learned.

**Required Fields:**
```yaml
act_2_struggle:
  period: "YYYY-YYYY or duration"
  challenges:
    - challenge: "[Description]"
      lesson: "[What they learned]"
  failures:
    - failure: "[Specific failure]"
      impact: "[How it affected them]"
  dark_moment: "[The lowest point]"
  pivotal_lesson: "[The key insight from this period]"
  sources:
    - "[Source file 1]"
```

**Questions to Answer:**
- What failures did they experience?
- How many attempts before success?
- What was the darkest moment?
- What did they almost give up on?
- What key lesson emerged from struggle?

### Step 1.4: Build Act 3 - Breakthrough

Extract the turning point that changed everything.

**Required Fields:**
```yaml
act_3_breakthrough:
  year: "YYYY"
  catalyst: "[What triggered the breakthrough]"
  realization: "[The key insight or shift]"
  first_success: "[The first significant win]"
  validation: "[How they knew it was working]"
  sources:
    - "[Source file 1]"
```

**Questions to Answer:**
- What was the specific breakthrough moment?
- What did they figure out that others hadn't?
- What was their first major success?
- How did they validate the approach worked?

### Step 1.5: Build Act 4 - Mastery

Extract their current state and signature achievements.

**Required Fields:**
```yaml
act_4_mastery:
  current_state: "[Where they are now]"
  signature_achievement: "[The defining accomplishment]"
  impact: "[How they've helped others]"
  philosophy: "[Core belief that emerged from journey]"
  sources:
    - "[Source file 1]"
```

**Questions to Answer:**
- Where are they now in their career?
- What is their signature achievement?
- How have they helped others?
- What philosophy emerged from their journey?

### Quality Gate: Crucible Story

- [ ] All 4 acts populated with content
- [ ] Each act has verifiable sources cited
- [ ] Timeline is coherent (years make sense)
- [ ] Story has clear transformation arc
- [ ] Darkest moment and breakthrough are specific, not generic
- [ ] Current state reflects authority position

---

## PHASE 2: COMPILE AUTHORITY STATISTICS

### Objective
Extract verifiable statistics that demonstrate expertise and results.

### Step 2.1: Identify Statistical Categories

Scan source files for numbers related to:

| Category | What to Look For |
|----------|-----------------|
| **Career** | Years of experience, total projects, hours invested |
| **Results** | Revenue generated, clients helped, transformations achieved |
| **Recognition** | Awards, features, endorsements, credentials |
| **Reach** | Followers, subscribers, views, downloads, audience size |

### Step 2.2: Extract and Verify Statistics

For EACH statistic found:

| Statistic | Value | Source | Verifiable? | Date |
|-----------|-------|--------|-------------|------|
| "[metric name]" | [number] | [file] | ✅/❌ | [when stated] |

**Verification Rules:**
- ✅ Verifiable: Number stated directly by copywriter
- ✅ Verifiable: Can be cross-referenced with public data
- ⚠️ Approximate: Use "~" or "over" if rounded
- ❌ Reject: Vague claims like "many" or "countless"

### Step 2.3: Structure Statistics Output

```yaml
authority_statistics:
  career:
    - metric: "[Career metric name]"
      value: "[Specific number/range]"
      context: "[What this means]"
      source: "[Source file]"

  results:
    - metric: "[Results metric name]"
      value: "[Specific number/range]"
      context: "[What this means]"
      source: "[Source file]"

  recognition:
    - metric: "[Recognition metric name]"
      value: "[Specific credential/award]"
      context: "[What this means]"
      source: "[Source file]"

  reach:
    - metric: "[Reach metric name]"
      value: "[Specific number/range]"
      context: "[What this means]"
      source: "[Source file]"
```

### Quality Gate: Statistics

- [ ] Minimum 5 statistics extracted
- [ ] At least 2 different categories covered
- [ ] All statistics have source citations
- [ ] Numbers are specific (not vague)
- [ ] Statistics are impressive enough to establish authority

---

## PHASE 3: LIST NOTABLE PRODUCTS AND CLIENTS

### Objective
Document the copywriter's signature products, services, and notable clients/students.

### Step 3.1: Extract Notable Products

Scan for:
- Courses, programs, memberships
- Books, guides, resources
- Software, tools, templates
- Consulting/coaching offers

```yaml
notable_products:
  - name: "[Product name]"
    type: "course|book|software|service|community"
    description: "[One-line description]"
    result_claim: "[What it helps people achieve]"
    source: "[Source file]"
```

### Step 3.2: Extract Notable Clients/Students

Scan for:
- Client testimonials or mentions
- Student success stories
- Notable people who endorse or follow them
- Collaborations with recognized names

```yaml
notable_clients:
  - name: "[Client/student name or type]"
    result: "[What they achieved]"
    quote: "[Direct quote if available]"
    source: "[Source file]"
```

**Note:** If specific names aren't available, use categories like "Fortune 500 executives" or "6-figure entrepreneurs."

### Quality Gate: Products & Clients

- [ ] At least 3 notable products listed
- [ ] At least 2 notable clients/student types listed
- [ ] Each entry has clear result/benefit
- [ ] Sources are cited

---

## PHASE 4: CREATE PROOF STACK TEMPLATES

### Objective
Create reusable templates for inserting authority proof into copy.

### The 4 Proof Types

Every copywriter agent needs templates for these proof categories:

| Proof Type | Purpose | When to Use |
|------------|---------|-------------|
| **Transformation** | Show personal journey | Opening hooks, about sections |
| **Results** | Demonstrate achievements | Credibility sections, claims |
| **Credibility** | Establish expertise | Introductions, author bios |
| **Social** | Leverage audience/clients | Testimonial sections, validation |

### Step 4.1: Create Transformation Proof Template

Template for using the crucible story:

```yaml
proof_template_transformation:
  name: "Transformation Proof"
  purpose: "Establish relatability through personal journey"
  template: |
    [BEFORE STATE]: {act_1_context}
    [STRUGGLE]: {act_2_dark_moment}
    [TURNING POINT]: {act_3_catalyst}
    [AFTER STATE]: {act_4_current_state}

  usage_guidance:
    - "Use in opening hooks to establish relatability"
    - "Use in about sections to build connection"
    - "Abbreviate for social media bios"

  example_application: |
    "[Copywriter] went from {origin_state} to {mastery_state}
    after discovering {breakthrough_insight}."
```

### Step 4.2: Create Results Proof Template

Template for citing achievements:

```yaml
proof_template_results:
  name: "Results Proof"
  purpose: "Demonstrate capability through numbers"
  template: |
    [METRIC]: {statistic_value}
    [CONTEXT]: {what_it_means}
    [TIMEFRAME]: {when_achieved}

  usage_guidance:
    - "Use after making claims to substantiate"
    - "Use in headlines for specific hooks"
    - "Stack multiple statistics for compound proof"

  example_application: |
    "With {years} years of experience and {revenue_stat} in results,
    [Copywriter] has {achievement_description}."
```

### Step 4.3: Create Credibility Proof Template

Template for establishing expertise:

```yaml
proof_template_credibility:
  name: "Credibility Proof"
  purpose: "Position as authority in the field"
  template: |
    [CREDENTIALS]: {recognition_stats}
    [EXPERIENCE]: {career_stats}
    [NOTABLE WORK]: {products_or_clients}

  usage_guidance:
    - "Use in author bios and introductions"
    - "Use when presenting frameworks or methods"
    - "Use to counter 'who are you?' objection"

  example_application: |
    "[Copywriter], creator of {notable_product}, has helped
    {client_types} achieve {result_description}."
```

### Step 4.4: Create Social Proof Template

Template for leveraging audience and client results:

```yaml
proof_template_social:
  name: "Social Proof"
  purpose: "Leverage others' validation and results"
  template: |
    [AUDIENCE SIZE]: {reach_stats}
    [CLIENT RESULTS]: {client_achievements}
    [ENDORSEMENTS]: {notable_mentions}

  usage_guidance:
    - "Use in testimonial sections"
    - "Use to validate claims with third-party evidence"
    - "Use to show community/following"

  example_application: |
    "Join {audience_size} others who have {transformation_achieved}
    using [Copywriter]'s methods."
```

### Quality Gate: Proof Templates

- [ ] All 4 proof template types created
- [ ] Each template has clear structure
- [ ] Usage guidance provided for each
- [ ] Example applications included
- [ ] Templates reference actual extracted data

---

## PHASE 5: ASSEMBLE FINAL OUTPUT

### Step 5.1: Compile Complete Arsenal

Combine all phases into the final YAML structure:

```yaml
# Authority Arsenal - {Copywriter Name}
# Generated: {date}
# Source files analyzed: {count}

copywriter: "{name}"
slug: "{slug}"
extraction_date: "{YYYY-MM-DD}"
source_files_analyzed: {count}

crucible_story:
  title: "{One-line story title}"
  transformation_arc: "{from X to Y}"

  act_1_origin:
    # ... from Phase 1

  act_2_struggle:
    # ... from Phase 1

  act_3_breakthrough:
    # ... from Phase 1

  act_4_mastery:
    # ... from Phase 1

authority_statistics:
  career:
    # ... from Phase 2
  results:
    # ... from Phase 2
  recognition:
    # ... from Phase 2
  reach:
    # ... from Phase 2

notable_products:
  # ... from Phase 3

notable_clients:
  # ... from Phase 3

proof_stack_templates:
  transformation:
    # ... from Phase 4
  results:
    # ... from Phase 4
  credibility:
    # ... from Phase 4
  social:
    # ... from Phase 4
```

### Step 5.2: Validate YAML Syntax

- [ ] Run YAML linter/validator
- [ ] Check for proper indentation
- [ ] Verify no duplicate keys
- [ ] Ensure all strings are properly quoted if they contain special characters

### Output Location

Save to: `outputs/minds/{slug}/analysis/authority-arsenal.yaml`

---

## FINAL QUALITY CHECKLIST

### Content Completeness

- [ ] **Crucible Story**
  - [ ] Act 1 (Origin) complete with year, context, key event
  - [ ] Act 2 (Struggle) complete with challenges, failures, dark moment
  - [ ] Act 3 (Breakthrough) complete with catalyst, realization, first success
  - [ ] Act 4 (Mastery) complete with current state, signature achievement

- [ ] **Statistics** (minimum 5)
  - [ ] At least 1 career statistic
  - [ ] At least 1 results statistic
  - [ ] At least 1 reach statistic
  - [ ] All statistics have sources

- [ ] **Products & Clients**
  - [ ] At least 3 notable products listed
  - [ ] At least 2 client types or names listed

- [ ] **Proof Templates** (all 4 required)
  - [ ] Transformation proof template
  - [ ] Results proof template
  - [ ] Credibility proof template
  - [ ] Social proof template

### Quality Standards

- [ ] All content derived from source materials (not invented)
- [ ] All sources cited
- [ ] Numbers are specific, not vague
- [ ] Story arc is coherent and compelling
- [ ] Templates are actually usable for copy creation
- [ ] YAML syntax is valid

### Scoring

| Section | Weight | Criteria |
|---------|--------|----------|
| Crucible Story | 30% | All 4 acts complete, compelling arc |
| Statistics | 25% | 5+ stats, specific, verifiable |
| Products/Clients | 15% | 3+ products, 2+ clients |
| Proof Templates | 20% | All 4 types, usable |
| Technical | 10% | Valid YAML, proper sources |

**Target Score: 90%+**

---

## TROUBLESHOOTING

### Common Issues

**Issue:** Not enough autobiographical content
**Solution:** Look for:
- Podcast interviews where they share their story
- Social media posts about their journey
- "About" pages or bio content
- First-person narratives in any content

**Issue:** Statistics seem inflated or unverifiable
**Solution:**
- Use more conservative estimates
- Add qualifiers ("over", "approximately")
- Note the source and date of claim
- Exclude if truly unverifiable

**Issue:** Crucible story feels generic
**Solution:**
- Look for MORE specific details
- Find the unique angle (what makes THEIR struggle different?)
- Include specific failures, not just "challenges"
- Find the exact breakthrough moment

**Issue:** No notable clients named
**Solution:**
- Use client TYPES instead of names
- Look for testimonial content
- Check for any collaboration mentions
- Use audience demographics as proxy

---

## REFERENCE: David Ogilvy Example

For structural reference, see how `authority_proof_arsenal` is formatted in `agents/david-ogilvy.md`:

- Crucible story with 6 acts (we use 4 simplified)
- Statistics with specific numbers and sources
- Notable clients list
- Proof stack templates with setup and usage

---

*CopywriterOS Task v1.0.0*
*Part of the AIOS Expansion Pack System*
