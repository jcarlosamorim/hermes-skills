# Create Objection Algorithms - Copywriter Response Patterns

## Metadata
```yaml
task_id: create-objection-algorithms
version: 1.0.0
category: agent-creation
difficulty: intermediate
elicit: true
parent_task: create-copywriter-agent.md
phase: 6
dependencies:
  tasks:
    - tasks/extract-frameworks.md
    - tasks/extract-signature-phrases.md
  templates:
    - templates/objection-algorithms-tmpl.yaml
inputs:
  required:
    - source_directory: "Path to source materials"
    - frameworks_file: "Previously extracted frameworks ({pasta}/{slug}/analysis/frameworks.yaml)"
    - signature_phrases_file: "Previously extracted phrases ({pasta}/{slug}/analysis/signature-phrases.yaml)"
  optional:
    - communication_dna_file: "Communication DNA for vocabulary reference"
outputs:
  - Objection algorithms file (YAML)
  - 5 complete objection response algorithms
  - Each algorithm with 5 steps using copywriter's voice
```

## Objective

Create 5 systematic objection-handling algorithms that embody the copywriter's unique voice, frameworks, and philosophy. These algorithms enable the AI agent to respond to common objections authentically, using the copywriter's vocabulary, signature phrases, and proven frameworks.

**Why This Matters:**
- Objection handling reveals a copywriter's true philosophy
- Authentic responses require their actual frameworks and vocabulary
- Systematic algorithms ensure consistent, on-brand responses

---

## PREREQUISITES

### Required Inputs

Before starting this task, ensure you have:

| Input | File Location | Required |
|-------|---------------|----------|
| Frameworks | `{pasta}/{slug}/analysis/frameworks.yaml` | Yes |
| Signature Phrases | `{pasta}/{slug}/analysis/signature-phrases.yaml` | Yes |
| Communication DNA | `{pasta}/{slug}/analysis/communication-dna.yaml` | Recommended |
| Source Materials | `{pasta}/{slug}/sources/` | Yes |

```
elicit: true
question: "Please confirm the following files are available:"
fields:
  - copywriter_name: "Copywriter name (e.g., Dan Koe)"
  - slug: "Mind slug (e.g., dan_koe)"
  - frameworks_path: "Path to frameworks.yaml"
  - phrases_path: "Path to signature-phrases.yaml"
```

### Quality Gate: Prerequisites

- [ ] Frameworks file exists with 10 documented frameworks
- [ ] Signature phrases file exists with 42+ phrases
- [ ] Access to source materials for objection mining
- [ ] Output template available: `templates/objection-algorithms-tmpl.yaml`

---

## PHASE 1: IDENTIFY COMMON OBJECTIONS

### Step 1.1: Mine Objections from Source Materials

Read ALL source files looking for:

1. **Direct objections addressed** — When the copywriter responds to "but what about..."
2. **Anticipated objections** — When they preemptively answer concerns
3. **Audience pain points** — Fears, doubts, and blockers they mention
4. **FAQ content** — Questions they answer repeatedly

**Search patterns:**
- "But..." followed by a response
- "The problem is..."
- "People think... but actually..."
- "Common mistake is thinking..."
- "You might be wondering..."
- "The objection I hear most..."

### Step 1.2: Categorize Objections

Organize discovered objections into 5 universal categories:

| Category | Description | Example Triggers |
|----------|-------------|------------------|
| **Time/Resource Scarcity** | "I don't have time/money" | "I'm too busy", "I can't afford", "I don't have resources" |
| **Competence Doubt** | "I don't know enough" | "I'm not qualified", "I don't know what to write", "I'm not an expert" |
| **Market Saturation** | "The market is too crowded" | "Too many competitors", "Niche is saturated", "It's been done" |
| **Credibility Concern** | "Who am I to do this?" | "I don't have credentials", "No one will listen to me", "I need more experience" |
| **Audience Building** | "I need audience first" | "I don't have followers", "How do I get noticed?", "I need to build a platform first" |

### Step 1.3: Document Specific Triggers

For EACH category, document the specific ways the copywriter's audience expresses the objection:

```yaml
objection_category:
  name: "Time/Resource Scarcity"
  triggers_from_sources:
    - "I don't have time to create content"
    - "I can't write consistently"
    - "I'm too busy with my day job"
  copywriter_response_pattern:
    observed_in: "[Source file name]"
    approach: "[How they typically respond]"
```

### Quality Gate: Objection Mining

- [ ] Read minimum 20 source files for objection content
- [ ] Identified objections in all 5 categories
- [ ] Documented specific trigger phrases from sources
- [ ] Noted how copywriter typically responds

---

## PHASE 2: MAP FRAMEWORKS TO OBJECTIONS

### Step 2.1: Load Extracted Frameworks

Read the frameworks file: `{pasta}/{slug}/analysis/frameworks.yaml`

List all 10 frameworks:
1. [Framework 1 name]
2. [Framework 2 name]
...
10. [Framework 10 name]

### Step 2.2: Map Frameworks to Objection Categories

For each objection category, identify which framework(s) best address it:

| Objection Category | Primary Framework | Secondary Framework |
|--------------------|-------------------|---------------------|
| Time/Resource Scarcity | [Framework name] | [Framework name] |
| Competence Doubt | [Framework name] | [Framework name] |
| Market Saturation | [Framework name] | [Framework name] |
| Credibility Concern | [Framework name] | [Framework name] |
| Audience Building | [Framework name] | [Framework name] |

**Selection Criteria:**
- Framework directly addresses the underlying belief
- Framework provides actionable solution
- Framework is memorable and quotable

### Step 2.3: Extract Framework Principles for Responses

For each mapped framework, extract:
- Core principle (one sentence)
- Key components to reference
- Memorable example from the framework

### Quality Gate: Framework Mapping

- [ ] All 5 objection categories have at least one primary framework
- [ ] Framework selections make logical sense
- [ ] Framework principles extracted for use in algorithms

---

## PHASE 3: MAP SIGNATURE PHRASES TO OBJECTIONS

### Step 3.1: Load Signature Phrases

Read the phrases file: `{pasta}/{slug}/analysis/signature-phrases.yaml`

### Step 3.2: Select Key Phrases for Each Objection

For each objection category, select 3-5 signature phrases that:
- Directly address the objection
- Reframe the limiting belief
- Inspire action or confidence

| Objection Category | Key Phrases |
|--------------------|-------------|
| Time/Resource Scarcity | ["phrase 1", "phrase 2", "phrase 3"] |
| Competence Doubt | ["phrase 1", "phrase 2", "phrase 3"] |
| Market Saturation | ["phrase 1", "phrase 2", "phrase 3"] |
| Credibility Concern | ["phrase 1", "phrase 2", "phrase 3"] |
| Audience Building | ["phrase 1", "phrase 2", "phrase 3"] |

### Step 3.3: Note Phrase Context

For each selected phrase, note:
- Original context from source
- How to adapt it for objection handling
- Natural insertion point in the response

### Quality Gate: Phrase Mapping

- [ ] 3-5 phrases selected for each objection category
- [ ] Phrases are genuinely relevant (not forced)
- [ ] Context documented for natural usage

---

## PHASE 4: CREATE OBJECTION ALGORITHMS

### Algorithm Structure

Each algorithm must follow this 5-step structure:

```yaml
algorithm_name:
  name: "[Descriptive Name]"
  trigger: "When the prospect/reader says something like..."
  trigger_examples:
    - "[Specific phrase 1]"
    - "[Specific phrase 2]"
    - "[Specific phrase 3]"

  algorithm:
    step_1_acknowledge:
      name: "ACKNOWLEDGE"
      purpose: "Validate their concern without agreeing with the limiting belief"
      action: "[Specific acknowledgment in copywriter's voice]"
      scripts:
        - "[Script option 1]"
        - "[Script option 2]"

    step_2_reframe:
      name: "REFRAME"
      purpose: "Shift perspective using copywriter's philosophy"
      action: "[How to reframe the objection]"
      framework_reference: "[Framework name]"
      scripts:
        - "[Script option 1]"
        - "[Script option 2]"

    step_3_evidence:
      name: "EVIDENCE"
      purpose: "Provide proof or example that supports the reframe"
      action: "[What evidence to present]"
      evidence_types:
        - "[Type of evidence 1]"
        - "[Type of evidence 2]"

    step_4_vision:
      name: "VISION"
      purpose: "Paint the positive future if they move past this objection"
      action: "[What future to describe]"
      signature_phrases:
        - "[Phrase 1]"
        - "[Phrase 2]"

    step_5_action:
      name: "ACTION"
      purpose: "Propose specific next step"
      action: "[What action to suggest]"
      call_to_action: "[Specific CTA]"

  resolution: "[Expected outcome when this algorithm is applied]"

  key_phrases:
    - "[Signature phrase 1]"
    - "[Signature phrase 2]"
    - "[Signature phrase 3]"

  framework_reference: "[Primary framework used]"

  full_example: |
    [Complete example response using this algorithm]
```

### Step 4.1: Create Algorithm 1 - Time/Resource Scarcity

**Trigger:** "I don't have time to create content / write consistently / build this"

**Algorithm Focus:**
- Reframe time as investment, not expense
- Show how small, consistent actions compound
- Reference relevant productivity/efficiency framework
- Use signature phrases about consistency/compound effect

**Template to fill:**
```yaml
time_scarcity_algorithm:
  name: "Time Scarcity Resolution"
  trigger: "When prospect says they don't have time"
  trigger_examples:
    - "I don't have time to create content"
    - "I'm too busy with my day job"
    - "I can't write consistently with my schedule"

  algorithm:
    step_1_acknowledge:
      name: "ACKNOWLEDGE"
      action: "[Validate without agreeing]"
      # Fill based on copywriter's typical acknowledgment style

    step_2_reframe:
      name: "REFRAME"
      action: "[Shift from 'no time' to 'priority' or 'efficiency']"
      framework_reference: "[Relevant framework]"

    step_3_evidence:
      name: "EVIDENCE"
      action: "[Example of someone who succeeded despite time constraints]"

    step_4_vision:
      name: "VISION"
      action: "[Describe the future freedom content creates]"

    step_5_action:
      name: "ACTION"
      action: "[Specific small action they can take today]"

  resolution: "Prospect understands that [outcome]"
  key_phrases: [# Select from signature phrases]
  framework_reference: "[Framework name]"
```

### Step 4.2: Create Algorithm 2 - Competence Doubt

**Trigger:** "I don't know what to write / I'm not qualified / I don't have expertise"

**Algorithm Focus:**
- Reframe expertise as experience + curiosity, not credentials
- Show how teaching = learning = content
- Reference relevant content creation framework
- Use signature phrases about learning in public

### Step 4.3: Create Algorithm 3 - Market Saturation

**Trigger:** "The market is too crowded / Too much competition / This has been done"

**Algorithm Focus:**
- Reframe competition as validation
- Show how unique perspective = differentiation
- Reference relevant positioning/differentiation framework
- Use signature phrases about uniqueness

### Step 4.4: Create Algorithm 4 - Credibility Concern

**Trigger:** "I'm not an expert / Who am I to teach this / I don't have credentials"

**Algorithm Focus:**
- Reframe credibility as results + relatability, not credentials
- Show how being a few steps ahead is enough
- Reference relevant authority/proof framework
- Use signature phrases about authenticity

### Step 4.5: Create Algorithm 5 - Audience Building

**Trigger:** "I don't have followers / I need an audience first / How do I get noticed"

**Algorithm Focus:**
- Reframe audience building as content building
- Show how value attracts audience (not the reverse)
- Reference relevant audience/content framework
- Use signature phrases about serving > seeking

### Quality Gate: Algorithm Creation

For EACH algorithm:
- [ ] Trigger clearly defined with 3+ examples
- [ ] All 5 steps complete with scripts
- [ ] Framework reference is valid (from extracted frameworks)
- [ ] Key phrases are actual signature phrases (not made up)
- [ ] Full example demonstrates natural flow
- [ ] Response sounds like the copywriter (not generic)

---

## PHASE 5: VALIDATE VOICE AUTHENTICITY

### Step 5.1: Voice Consistency Check

For each algorithm, verify:

| Check | Algorithm 1 | Algorithm 2 | Algorithm 3 | Algorithm 4 | Algorithm 5 |
|-------|-------------|-------------|-------------|-------------|-------------|
| Uses copywriter's vocabulary? | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| References their frameworks? | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Includes signature phrases? | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Matches their tone? | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Avoids forbidden words? | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |

### Step 5.2: Distinctiveness Test

**Test question:** Could this response come from a generic AI or does it clearly reflect this specific copywriter?

For each algorithm, rate distinctiveness:
- **High:** Clearly sounds like [Copywriter Name]
- **Medium:** Could be identified with context
- **Low:** Too generic, needs revision

**Target:** All algorithms should rate High.

### Step 5.3: Framework Integration Verification

For each algorithm, verify the framework reference:
- [ ] Framework exists in frameworks.yaml
- [ ] Framework is relevant to the objection
- [ ] Framework principles are correctly applied
- [ ] Framework vocabulary is used

### Quality Gate: Voice Validation

- [ ] All 5 algorithms pass voice consistency checks
- [ ] All 5 algorithms rate "High" on distinctiveness
- [ ] All framework references are valid
- [ ] No generic/filler content remains

---

## PHASE 6: OUTPUT AND DOCUMENTATION

### Step 6.1: Compile Final YAML

Using the template: `templates/objection-algorithms-tmpl.yaml`

Create the output file with this structure:

```yaml
# Objection Algorithms - [Copywriter Name]
# Generated by: create-objection-algorithms.md task
# Date: [YYYY-MM-DD]

metadata:
  copywriter: "[Full Name]"
  slug: "[mind_slug]"
  extraction_date: "[YYYY-MM-DD]"
  total_algorithms: 5
  source_files_consulted: [count]
  frameworks_referenced: [list]
  phrases_used: [count]

objection_algorithms:

  - name: "Time Scarcity Resolution"
    # ... [complete algorithm 1]

  - name: "Competence Doubt Resolution"
    # ... [complete algorithm 2]

  - name: "Market Saturation Resolution"
    # ... [complete algorithm 3]

  - name: "Credibility Concern Resolution"
    # ... [complete algorithm 4]

  - name: "Audience Building Resolution"
    # ... [complete algorithm 5]

quality_metrics:
  voice_authenticity: "[high/medium]"
  framework_integration: "[count] frameworks used"
  phrase_integration: "[count] signature phrases used"
  distinctiveness_rating: "[high/medium]"
```

### Step 6.2: Save Output

Save to: `{pasta}/{slug}/analysis/objection-algorithms.yaml`

### Quality Gate: Output

- [ ] File saved to correct location
- [ ] YAML syntax validates (no errors)
- [ ] Metadata section complete
- [ ] All 5 algorithms present and complete
- [ ] Quality metrics documented

---

## FINAL CHECKLIST

### Completion Requirements

- [ ] Phase 1: Objections mined from 20+ source files
- [ ] Phase 2: Frameworks mapped to all 5 objection categories
- [ ] Phase 3: Signature phrases selected for each objection
- [ ] Phase 4: All 5 algorithms created with 5 steps each
- [ ] Phase 5: Voice authenticity validated
- [ ] Phase 6: Output file created and saved

### Quality Standards

- [ ] Exactly 5 algorithms (not more, not less)
- [ ] Each algorithm has exactly 5 steps
- [ ] All key phrases are actual signature phrases
- [ ] All framework references are valid
- [ ] Responses sound like the copywriter
- [ ] YAML syntax is valid
- [ ] No placeholder text remaining

### Integration Verification

- [ ] Algorithms work with existing frameworks.yaml
- [ ] Algorithms work with existing signature-phrases.yaml
- [ ] Output matches template structure
- [ ] Ready for integration into final agent file

---

## TROUBLESHOOTING

### Common Issues

**Issue:** Can't find objection content in sources
**Solution:** Look for FAQ sections, audience Q&A, comment responses, objection handling in sales content

**Issue:** Framework doesn't fit the objection
**Solution:** Choose a different framework or adapt the angle - the framework should naturally address the limiting belief

**Issue:** Signature phrases feel forced
**Solution:** Use fewer phrases, only where they fit naturally - authenticity over quantity

**Issue:** Response sounds generic
**Solution:** Review communication DNA, add more specific vocabulary, include concrete examples from the copywriter's experience

**Issue:** Algorithm too long/verbose
**Solution:** Each step should be 1-3 sentences max, focus on impact not word count

---

## EXAMPLE OUTPUT

For reference, see the objection algorithms in:
- `.aios-core/expansion-packs/copywriter-os/agents/david-ogilvy.md` (objection_algorithms section)
- `.aios-core/expansion-packs/copywriter-os/agents/alex-hormozi.md` (objection_algorithms section)

These demonstrate the expected depth, structure, and voice consistency.

---

*CopywriterOS Task v1.0.0*
*Phase 6 of Create Copywriter Agent Pipeline*
