# Create Copywriter Agent - Master Orchestration Task

## Metadata

```yaml
task_id: create-copywriter-agent
version: 2.0.0
category: agent-creation
difficulty: advanced
elicit: true
minimum_output_lines: 600

methodology_source: "docs/research/copywriter-agent-creation-methodology-research.md"
theoretical_foundation:
  - "DeepPersona Research Framework - Taxonomy-guided persona creation"
  - "CharacterGPT - Persona reconstruction methodology"
  - "Nature: Psychometric Framework for LLM Personality"
  - "DPRF - Dynamic Persona Refinement Framework"
  - "Linguistic Fingerprinting - Voice capture methodology"

dependencies:
  tasks:
    - tasks/extract-frameworks.md
    - tasks/extract-communication-dna.md
    - tasks/extract-signature-phrases.md
    - tasks/build-authority-arsenal.md
    - tasks/create-objection-algorithms.md
  templates:
    - templates/copywriter-agent-tmpl.yaml
    - templates/frameworks-extraction-tmpl.yaml
    - templates/communication-dna-tmpl.yaml
    - templates/signature-phrases-tmpl.yaml
    - templates/authority-arsenal-tmpl.yaml
    - templates/objection-algorithms-tmpl.yaml
  checklists:
    - checklists/copywriter-agent-creation-checklist.md
  reference:
    - agents/dan-kennedy.md
    - agents/david-ogilvy.md

outputs:
  primary: "squads/copy/agents/{slug}.md"
  analysis_files:
    - "{pasta}/{slug}/analysis/frameworks.yaml"
    - "{pasta}/{slug}/analysis/communication-dna.yaml"
    - "{pasta}/{slug}/analysis/signature-phrases.yaml"
    - "{pasta}/{slug}/analysis/authority-arsenal.yaml"
    - "{pasta}/{slug}/analysis/objection-algorithms.yaml"
    - "{pasta}/{slug}/analysis/{slug}-rules.yaml"
    - "{pasta}/{slug}/analysis/validation-report.md"
```

---

## Executive Summary

**What This Task Does:**
Create a comprehensive AI copywriter agent that authentically replicates a master copywriter's thinking, communication, and methodology.

**Why This Matters:**
Generic AI produces generic copy. An authentic copywriter agent channels decades of expertise, distinctive voice, and proven frameworks - enabling anyone to access elite copywriting capability.

**The Persona Equation:**
```
Authentic Agent = Operational Frameworks + Communication DNA + Signature Phrases + Authority Arsenal + Objection Algorithms + Psychometric Integration
```

**Quality Standard:**
The resulting agent must be DISTINCTIVE (sounds like no one else), COMPLETE (can handle any relevant topic), CONSISTENT (responds reliably), and AUTHENTIC (true to source material).

---

## Theoretical Foundation

### The DeepPersona Research Framework

From academic research on synthetic personas:

> "Most synthetic personas are shallow and simplistic, capturing minimal attributes and failing to reflect the rich complexity and diversity of real human identities."

**Solution:** Taxonomy-guided, multi-layer extraction that captures not just WHAT someone says, but HOW they think and WHY they believe certain things.

### Persona Attribute Hierarchy

```
LAYER 4: MOTIVATIONAL (Hardest to extract)
├── Core values
├── Driving fears
└── Aspirations

LAYER 3: COGNITIVE
├── Mental models
├── Problem-solving approaches
└── Belief systems

LAYER 2: BEHAVIORAL
├── Communication style
├── Decision patterns
└── Response tendencies

LAYER 1: SURFACE (Easiest to extract)
├── Name, background
├── Profession, achievements
└── Public credentials
```

**Rule:** Extract from Layer 1 up. Surface attributes inform behavioral inference; behavioral patterns reveal cognitive approaches; cognitive understanding unlocks motivational drivers.

### Linguistic Fingerprint Components

A linguistic fingerprint is the unique combination of language patterns that make a person's communication identifiable:

| Component | Description | Extraction Method |
|-----------|-------------|-------------------|
| **Lexical** | Word choice patterns | Frequency analysis |
| **Syntactic** | Sentence structure | Length/complexity analysis |
| **Rhetorical** | Persuasion patterns | Device cataloging |
| **Pragmatic** | Communication intent | Directness/hedging analysis |

---

## PREREQUISITES

### Required Inputs

```yaml
elicit: true
question: "Please provide the following information about the copywriter:"
fields:
  - copywriter_name: "Full name of the copywriter (e.g., Dan Kennedy)"
  - slug: "Snake_case identifier (e.g., dan_kennedy)"
  - source_directory: "Path to source materials directory"
  - psychometric_profile: "Path to psychometric profile (optional)"
  - reference_agent: "Existing agent to use as structure reference"
```

### Source Material Requirements

| Material Type | Minimum | Ideal | Quality Indicators |
|--------------|---------|-------|-------------------|
| **Writing/Content advice** | 5 files | 10+ | Contains "how to," frameworks |
| **Business/Strategy** | 4 files | 8+ | Contains methodology, systems |
| **Personal journey** | 3 files | 6+ | Contains origin story, struggles |
| **Philosophy/Mindset** | 2 files | 4+ | Contains beliefs, principles |
| **Interviews/Podcasts** | 2 files | 4+ | Contains unscripted responses |
| **TOTAL** | 20 files | 40+ | 500+ words per file |

### Source Supplementation

When source material is insufficient:

```yaml
supplementation_sources:
  youtube_transcripts:
    value: "Natural speech patterns, unfiltered thought"
    process: "Download transcript, clean formatting, save as markdown"

  podcast_transcripts:
    value: "Long-form thinking, framework explanations"
    process: "Transcribe audio, clean, format as markdown"

  social_media:
    value: "Condensed, punchy signature phrases"
    process: "Collect threads/posts, organize by theme"

  book_excerpts:
    value: "Polished, edited framework explanations"
    process: "Extract key passages with proper citation"
```

### Quality Gate: Prerequisites

```
MANDATORY CHECKS:
- [ ] Source directory exists with 20+ files
- [ ] All source files are readable (markdown/text)
- [ ] Files span 4+ content type categories
- [ ] Reference agent file(s) identified
- [ ] Output directory exists: {pasta}/{slug}/analysis/
- [ ] Each file contains 500+ words of substantive content

QUALITY CHECKS:
- [ ] At least 3 files contain origin story / journey content
- [ ] At least 4 files contain explicit methodology / frameworks
- [ ] At least 2 files are interview/podcast format (natural speech)
- [ ] Content spans at least 3 years (shows evolution)
```

---

## PHASE 1: SETUP AND RECONNAISSANCE

### Step 1.1: Create Output Directory Structure

```bash
mkdir -p {pasta}/{slug}/analysis
mkdir -p {pasta}/{slug}/docs
```

### Step 1.2: Inventory Source Materials

Read ALL source files and create categorized inventory:

**Inventory Template:**

| File | Type | Topics | Quality | Lines | Extraction Value |
|------|------|--------|---------|-------|------------------|
| [filename] | Article | [topics] | High/Med/Low | [#] | Frameworks/DNA/Story |

**Type Categories:**
- `writing` - Copywriting advice and techniques
- `business` - Business strategy and methodology
- `marketing` - Marketing systems and approaches
- `personal` - Journey, struggles, origin story
- `philosophy` - Beliefs, principles, mindset
- `interview` - Unscripted conversations

**Extraction Value Tags:**
- `Frameworks` - Contains teachable methodologies
- `DNA` - Rich with distinctive vocabulary/style
- `Story` - Contains autobiographical content
- `Phrases` - Contains quotable statements
- `Stats` - Contains verifiable metrics

### Step 1.3: Read Reference Agents

Read reference agent files to understand target structure:

**Primary Reference:** `squads/copy/agents/dan-kennedy.md`
**Secondary Reference:** `squads/copy/agents/david-ogilvy.md`

**Analyze:**
1. Overall structure and sections
2. Depth of operational frameworks (10 required)
3. Communication DNA format and completeness
4. Signature phrases organization (7 tiers)
5. Authority arsenal components
6. Objection algorithm structure

### Step 1.4: Initial Extraction Pass

Before executing sub-tasks, do a quick pass through all sources to identify:

```yaml
initial_extraction_notes:

  framework_candidates:
    description: "Potential frameworks spotted"
    markers: "Step-by-step processes, named systems"
    count_target: "15+ candidates (will select 10)"

  vocabulary_patterns:
    description: "Distinctive words and phrases"
    markers: "Repeated unusual terms"
    count_target: "30+ potential mandatory words"

  story_elements:
    description: "Autobiographical content"
    markers: "Origin, struggles, breakthrough"
    completeness: "4 acts identifiable?"

  quotable_phrases:
    description: "Memorable statements"
    markers: "Standalone, original, powerful"
    count_target: "60+ candidates (will select 42+)"

  statistics:
    description: "Verifiable metrics"
    markers: "Numbers, achievements, results"
    count_target: "10+ potential statistics"
```

### Quality Gate: Setup Complete

```
- [ ] Output directory structure created
- [ ] All source files inventoried with categories
- [ ] Reference agent(s) thoroughly analyzed
- [ ] Initial extraction pass completed
- [ ] Framework candidates identified (15+)
- [ ] Vocabulary patterns noted (30+)
- [ ] Story elements mapped (4 acts)
- [ ] Quotable phrases marked (60+)
```

---

## PHASE 2: EXTRACT OPERATIONAL FRAMEWORKS

**Execute Sub-Task:** `tasks/extract-frameworks.md`

### Objective

Identify and document 10 operational frameworks the copywriter uses repeatedly. These are their intellectual property - the "how" behind their work.

### Framework Criteria

All 10 frameworks must meet these criteria:

```yaml
framework_criteria:

  repeatability:
    requirement: "Used across multiple contexts"
    evidence: "Appears in 3+ source files"

  teachability:
    requirement: "Can be explained to others"
    evidence: "Has clear steps or components"

  structure:
    requirement: "Identifiable process"
    evidence: "Steps, phases, or components"

  originality:
    requirement: "Their distinctive version"
    evidence: "Not generic advice"
```

### Framework Identification Markers

Scan sources for these language patterns:

| Pattern Type | Examples |
|--------------|----------|
| **Process language** | "The first thing I do is...", "My approach to..." |
| **Naming language** | "I call this the...", "My [X] method..." |
| **Teaching language** | "If you want to...", "The key is to..." |
| **Structural language** | "There are three types of...", "The components are..." |

### Framework Documentation Structure

```yaml
framework_template:
  name: "[Framework name]"
  category: "[copywriting|offer_creation|marketing|sales|content|audience|product|mindset]"
  origin: "[Source file or concept origin]"

  definition:
    one_sentence: "[Single sentence summary]"
    principle: "[Underlying belief or insight]"

  components:
    - component_1: "[First element]"
    - component_2: "[Second element]"
    - component_3: "[Third element - if applicable]"

  process:
    step_1:
      action: "[What to do]"
      output: "[Expected result]"
    step_2:
      action: "[What to do]"
      output: "[Expected result]"

  application:
    when_to_use: "[Trigger conditions]"
    when_not_to_use: "[Counter-indications]"

  common_mistakes:
    - mistake_1: "[What people do wrong]"
    - mistake_2: "[Another common error]"

  examples:
    - source: "[Source file]"
      quote: "[Relevant passage demonstrating framework]"

  related_frameworks:
    - "[Other framework this pairs with]"
```

### Category Distribution

Aim for diversity across categories:

| Category | Minimum | Description |
|----------|---------|-------------|
| copywriting | 2 | How they write persuasive copy |
| offer_creation | 1 | How they design offers |
| marketing_strategy | 1 | How they approach marketing |
| sales | 1 | How they close deals |
| content | 1 | How they create content |
| audience | 1 | How they understand audiences |
| mindset | 1 | How they think about success |
| (any) | 2 | Additional from any category |

### Output

- **File:** `{pasta}/{slug}/analysis/frameworks.yaml`
- **Template:** `templates/frameworks-extraction-tmpl.yaml`

### Quality Gate: Frameworks

```
MANDATORY CHECKS:
- [ ] Exactly 10 frameworks documented
- [ ] All categories represented (minimum 3 different)
- [ ] Each framework has all required fields
- [ ] Each framework has at least 1 source example
- [ ] YAML syntax validated

QUALITY CHECKS:
- [ ] Frameworks are distinctive (not generic advice)
- [ ] Frameworks are actionable (clear steps)
- [ ] Frameworks are complete (no gaps in process)
- [ ] Category distribution is balanced
```

---

## PHASE 3: EXTRACT COMMUNICATION DNA

**Execute Sub-Task:** `tasks/extract-communication-dna.md`

### Objective

Capture the copywriter's linguistic fingerprint: vocabulary, rhetoric, and formulas that make their communication distinctive.

### DNA Components

#### A. Vocabulary Extraction

**Mandatory Words (15+ required)**

Terms the copywriter uses constantly, often multiple times per piece.

```yaml
mandatory_word_extraction:

  process:
    1: "Analyze all source files for word frequency"
    2: "Identify words appearing in 80%+ of files"
    3: "Remove common words (the, is, and, etc.)"
    4: "Categorize by type"

  categories:
    action_verbs: "What actions they describe"
    value_words: "What they consider important"
    identity_words: "How they describe people"
    process_words: "How they describe activities"

  documentation:
    word: "[word]"
    frequency: "[times per 1000 words]"
    context: "[typical usage]"
    example: "[quote from source]"
```

**Forbidden Words (10+ required)**

Terms the copywriter never uses or actively avoids.

```yaml
forbidden_word_identification:

  detection_methods:
    absence_analysis: "Words common in field but absent in their work"
    explicit_rejection: "Words they criticize or mock"
    replacement_patterns: "What they use instead"

  documentation:
    word: "[forbidden word]"
    reason: "[why they avoid it]"
    replacement: "[what they use instead]"
```

**Signature Vocabulary (10+ required)**

Unique terms with specific meanings in their lexicon.

```yaml
signature_vocabulary:

  documentation:
    term: "[unique word or phrase]"
    their_definition: "[their specific meaning]"
    standard_definition: "[normal meaning if different]"
    usage: "[when/how they use this]"
    source: "[where first encountered]"
```

#### B. Trigram Analysis (20+ required)

Three-word combinations that appear frequently.

```yaml
trigram_extraction:

  quality_criteria:
    minimum_frequency: "Appears 3+ times"
    distinctiveness: "Not common in general writing"
    recognizability: "Would identify the writer"

  documentation:
    trigram: "[three-word phrase]"
    frequency: "[count]"
    context: "[when they use it]"
    example: "[quote showing usage]"
```

#### C. Rhetorical Devices (5+ required)

Persuasion patterns they favor.

```yaml
rhetorical_devices:

  common_types:
    - reframing: "Presenting concept from new angle"
    - juxtaposition: "Contrasting ideas for emphasis"
    - rule_of_three: "Concepts in groups of three"
    - anecdote: "Personal story to illustrate"
    - socratic_questioning: "Leading via questions"
    - pattern_interrupt: "Breaking flow for attention"
    - call_out: "Directly addressing audience"

  documentation:
    device: "[device name]"
    description: "[how they use it]"
    markers: "[words/phrases that signal it]"
    example: "[quote demonstrating]"
    frequency: "[how often used]"
```

#### D. Quick Formulas (5+ required)

Templates for common copy elements.

```yaml
quick_formulas:

  categories:
    hook: "Opening attention grabber"
    headline: "Main promise structure"
    cta: "Call to action pattern"
    transition: "Moving between sections"
    close: "Ending pattern"

  documentation:
    name: "[Formula name]"
    structure: "[Pattern with placeholders]"
    example: "[Filled-in example]"
    when_to_use: "[Appropriate contexts]"
```

#### E. Psychometric Influence (if profile available)

```yaml
psychometric_integration:

  disc_profile:
    dominant: "[D/I/S/C]"
    communication_impact:
      - "[How it affects their style]"

  mbti_type:
    type: "[4-letter type]"
    communication_impact:
      - "[How it affects their approach]"

  enneagram:
    type: "[1-9]"
    wing: "[wing number]"
    communication_impact:
      - "[How it affects their voice]"
```

### Output

- **File:** `{pasta}/{slug}/analysis/communication-dna.yaml`
- **Template:** `templates/communication-dna-tmpl.yaml`

### Quality Gate: Communication DNA

```
MANDATORY CHECKS:
- [ ] 15+ mandatory words with context
- [ ] 10+ forbidden words with reasoning
- [ ] 10+ signature vocabulary with definitions
- [ ] 20+ trigrams extracted
- [ ] 5+ rhetorical devices documented
- [ ] 5+ quick formulas created
- [ ] YAML syntax validated

QUALITY CHECKS:
- [ ] Vocabulary is distinctive (not generic)
- [ ] Trigrams are recognizable
- [ ] Formulas are actionable
- [ ] Psychometric integration complete (if profile exists)
```

---

## PHASE 4: EXTRACT SIGNATURE PHRASES

**Execute Sub-Task:** `tasks/extract-signature-phrases.md`

### Objective

Curate 42+ memorable, quotable phrases organized in 7 tiers by usage frequency.

### Phrase Selection Criteria

Each phrase must be:

```yaml
phrase_criteria:

  standalone:
    requirement: "Makes sense without context"
    test: "Would this work on a t-shirt?"

  memorable:
    requirement: "Sticks in the mind"
    test: "Would someone quote this?"

  original:
    requirement: "Distinctively theirs"
    test: "Could anyone else have said this?"

  attributable:
    requirement: "Clearly from this person"
    test: "Would readers recognize the source?"
```

### The 7-Tier System

| Tier | Name | Usage Frequency | Count | Purpose |
|------|------|-----------------|-------|---------|
| 1 | Core Mantras | Every piece (1-2x daily) | 3-5 | Signature identity phrases |
| 2 | Methodology Pillars | Weekly | 5-7 | Framework summary phrases |
| 3 | Theme: [Primary Topic] | Per topic | 6-8 | Main expertise area |
| 4 | Theme: [Secondary Topic] | Per topic | 6-8 | Second expertise area |
| 5 | Theme: [Tertiary Topic] | Per topic | 6-8 | Third expertise area |
| 6 | Philosophy & Mindset | Monthly | 5-7 | Worldview statements |
| 7 | Tactical & Situational | As needed | 5-7 | Specific context phrases |

### Phrase Documentation Structure

```yaml
signature_phrase_entry:
  phrase: "[Original phrase in English]"
  tier: "[1-7]"
  context: "[When/how to use this phrase]"
  source: "[Source file or content piece]"
  related_framework: "[If connects to a framework]"
  emotional_tone: "[inspiring|challenging|reassuring|etc.]"
```

### Extraction Process

```
1. READ all source files marking quotable statements
2. FILTER for phrases meeting all 4 criteria
3. CATEGORIZE by tier based on importance/frequency
4. BALANCE distribution across all 7 tiers
5. VERIFY each phrase has source citation
6. DEDUPLICATE similar phrases
7. SELECT final 42+ best phrases
```

### Output

- **File:** `{pasta}/{slug}/analysis/signature-phrases.yaml`
- **Template:** `templates/signature-phrases-tmpl.yaml`

### Quality Gate: Signature Phrases

```
MANDATORY CHECKS:
- [ ] Minimum 42 phrases extracted
- [ ] All 7 tiers populated
- [ ] Each phrase has context and source
- [ ] No duplicate phrases
- [ ] YAML syntax validated

QUALITY CHECKS:
- [ ] Phrases are genuinely quotable (not generic)
- [ ] Tier 1 phrases are truly distinctive
- [ ] Theme tiers match their actual expertise areas
- [ ] Distribution across tiers is balanced
```

---

## PHASE 5: BUILD AUTHORITY ARSENAL

**Execute Sub-Task:** `tasks/build-authority-arsenal.md`

### Objective

Compile credibility elements: crucible story (4 acts), statistics, products, clients, and proof templates.

### A. Crucible Story (4 Acts)

```yaml
crucible_story_structure:

  act_1_origin:
    purpose: "Establish relatability"
    required_fields:
      year: "YYYY or range"
      location: "Where this happened"
      context: "Starting situation"
      key_event: "Inciting incident"
      initial_belief: "What they thought then"
      emotional_state: "How they felt"
    sources_to_check:
      - "About pages"
      - "Origin story articles"
      - "Book introductions"
      - "Early podcast interviews"

  act_2_struggle:
    purpose: "Build credibility through adversity"
    required_fields:
      period: "Timeframe of struggles"
      primary_challenge: "Main obstacle"
      failures:
        - failure: "Specific failure"
          impact: "How it affected them"
          lesson: "What they learned"
      dark_moment:
        description: "Lowest point - be specific"
        year: "When this occurred"
        what_almost_happened: "What they nearly did"
    sources_to_check:
      - "Vulnerable posts"
      - "Failure stories"
      - "Lesson learned content"

  act_3_breakthrough:
    purpose: "Establish unique value"
    required_fields:
      year: "When breakthrough occurred"
      catalyst: "What triggered the change"
      realization:
        insight: "Key realization"
        how_discovered: "How they found this"
      first_success:
        description: "First major win"
        metric: "Specific result"
    sources_to_check:
      - "Success stories"
      - "Methodology origin"
      - "Turning point narratives"

  act_4_mastery:
    purpose: "Demonstrate current authority"
    required_fields:
      current_state:
        position: "Current title/role"
        reach: "Audience size"
        recognition: "How industry sees them"
      signature_achievement: "Defining accomplishment"
      impact_on_others:
        students_helped: "Number transformed"
        methodology_spread: "How approach has spread"
      core_philosophy: "Central belief"
    sources_to_check:
      - "Current bio"
      - "Results pages"
      - "Recent interviews"
```

### B. Authority Statistics

```yaml
authority_statistics_categories:

  career:
    examples:
      - "Years of experience"
      - "Number of clients"
      - "Projects completed"
    minimum: 2 statistics

  results:
    examples:
      - "Revenue generated"
      - "ROI delivered"
      - "Growth achieved"
    minimum: 2 statistics

  recognition:
    examples:
      - "Awards received"
      - "Media features"
      - "Books published"
    minimum: 1 statistic

  reach:
    examples:
      - "Email subscribers"
      - "Social followers"
      - "Course students"
    minimum: 1 statistic

  verification_level:
    A: "Third-party verified"
    B: "Publicly documented"
    C: "Self-reported with evidence"
    D: "Self-reported claim"
```

### C. Notable Products/Clients

```yaml
notable_work:

  products:
    documentation:
      name: "[Product name]"
      type: "[course|book|software|service|community|system]"
      description: "[One-line description]"
      result_claim: "[What it helps achieve]"
      social_proof: "[Sales/users if available]"
    minimum: 3 products

  clients:
    documentation:
      name: "[Client name or type]"
      type: "[individual|company|organization]"
      recognition_level: "[celebrity|industry_leader|notable|general]"
      result: "[What they achieved]"
    minimum: 2 clients/types
```

### D. Proof Stack Templates (4 required)

```yaml
proof_templates:

  transformation_proof:
    structure: "From [before] to [after] in [timeframe]"
    purpose: "Relatability + possibility"

  results_proof:
    structure: "[Number] achieved [in timeframe] for [audience]"
    purpose: "Capability demonstration"

  credibility_proof:
    structure: "[Title] + [years] + [achievement]"
    purpose: "Expert positioning"

  social_proof:
    structure: "[Number] of [audience] have [result]"
    purpose: "Community validation"
```

### Output

- **File:** `{pasta}/{slug}/analysis/authority-arsenal.yaml`
- **Template:** `templates/authority-arsenal-tmpl.yaml`

### Quality Gate: Authority Arsenal

```
MANDATORY CHECKS:
- [ ] 4-act crucible story complete
- [ ] Each act has source citations
- [ ] 5+ verifiable statistics documented
- [ ] 3+ notable products listed
- [ ] 2+ client types listed
- [ ] 4 proof stack templates created
- [ ] YAML syntax validated

QUALITY CHECKS:
- [ ] Story has clear transformation arc
- [ ] Dark moment is specific (not generic)
- [ ] Statistics are impressive (establish authority)
- [ ] Proof templates use actual extracted data
```

---

## PHASE 6: CREATE OBJECTION ALGORITHMS

**Execute Sub-Task:** `tasks/create-objection-algorithms.md`

### Objective

Create 5 response algorithms for common objections using the copywriter's voice, frameworks, and vocabulary.

### Algorithm Structure

```yaml
objection_algorithm_template:

  metadata:
    name: "[Algorithm name]"
    trigger: "When user says something like '[objection]'"
    category: "[time|competence|market|credibility|prerequisite]"

  response_pattern:
    step_1_acknowledge:
      purpose: "Validate the objection"
      pattern: "I get it. [Rephrase their concern]."
      key_phrase: "[Signature phrase to use]"

    step_2_reframe:
      purpose: "Shift perspective"
      pattern: "But here's what most people miss..."
      framework_reference: "[Related framework]"

    step_3_evidence:
      purpose: "Provide proof"
      pattern: "[Story/stat that addresses objection]"
      source: "[From authority arsenal]"

    step_4_vision:
      purpose: "Paint the future"
      pattern: "Imagine if instead of [objection], you..."
      emotional_tone: "[inspiring|challenging|etc.]"

    step_5_action:
      purpose: "Propose next step"
      pattern: "Here's what I'd do if I were you..."
      call_to_action: "[Specific action]"

  resolution:
    expected_outcome: "[What should happen]"
    fallback: "[If objection persists]"

  integration:
    key_phrases: ["[phrase 1]", "[phrase 2]"]
    framework_used: "[framework name]"
    vocabulary_used: ["[mandatory words]"]
```

### Required Objection Categories

| # | Category | Trigger Examples |
|---|----------|------------------|
| 1 | Time/Resource Scarcity | "I don't have time", "I can't afford it" |
| 2 | Competence Doubt | "I don't know enough", "I'm not an expert" |
| 3 | Market Saturation | "It's too competitive", "I'm too late" |
| 4 | Credibility Concern | "Who would listen to me?", "I have no credentials" |
| 5 | Prerequisite Myth | "I need more followers first", "I need to validate first" |

### Output

- **File:** `{pasta}/{slug}/analysis/objection-algorithms.yaml`
- **Template:** `templates/objection-algorithms-tmpl.yaml`

### Quality Gate: Objection Algorithms

```
MANDATORY CHECKS:
- [ ] Exactly 5 algorithms created
- [ ] Each algorithm has 5 steps
- [ ] Key phrases are from signature phrases
- [ ] Framework references exist in extracted frameworks
- [ ] YAML syntax validated

QUALITY CHECKS:
- [ ] Responses sound like the copywriter
- [ ] Reframes use their mental models
- [ ] Evidence uses their actual stories/stats
- [ ] Actions align with their methodology
```

---

## PHASE 7: EXTRACT COPYWRITER-SPECIFIC RULES

### Objective

Extract explicit rules and advice the copywriter gives, organized by category.

### Rule Structure

```yaml
copywriter_rules:

  writing:
    minimum: 8 rules
    extraction_markers:
      - "Always..."
      - "Never..."
      - "The key is..."
      - "What most people get wrong..."
    format:
      rule: "[Actionable imperative]"
      source: "[Source file]"
      context: "[When this applies]"

  content_strategy:
    minimum: 6 rules
    extraction_markers:
      - "When creating content..."
      - "The best content..."
      - "I recommend..."

  business:
    minimum: 6 rules
    extraction_markers:
      - "In business..."
      - "The most successful..."
      - "If you want to grow..."

  mindset:
    minimum: 6 rules
    extraction_markers:
      - "The truth is..."
      - "Most people believe..."
      - "Success requires..."
```

### Output

- **File:** `{pasta}/{slug}/analysis/{slug}-rules.yaml`

### Quality Gate: Rules

```
MANDATORY CHECKS:
- [ ] 8+ writing rules
- [ ] 6+ content strategy rules
- [ ] 6+ business rules
- [ ] 6+ mindset rules (26+ total)
- [ ] All rules have source citations
- [ ] YAML syntax validated

QUALITY CHECKS:
- [ ] Rules are actionable (imperative voice)
- [ ] Rules are specific (not generic advice)
- [ ] Rules are verifiable from sources
```

---

## PHASE 8: ASSEMBLE FINAL AGENT FILE

### Objective

Combine all extracted components into the final agent markdown file.

### Agent File Structure

```markdown
# {Copywriter Name} - CopywriterOS Agent

## YAML Front Matter
```yaml
IDE-FILE-RESOLUTION:
  - Dependencies map to squads/copy/{type}/{name}

REQUEST-RESOLUTION: "[How to handle requests]"

activation-instructions:
  - STEP 1: Read THIS ENTIRE FILE
  - STEP 2: Adopt the persona of {Copywriter Name}
  - STEP 3: Greet user with: "[Greeting in their voice]"
  - STAY IN CHARACTER!

agent:
  name: "{Copywriter Name}"
  id: "{slug}"
  title: "{Title/description}"
  icon: "{emoji}"
  era: "{Classic|Transition|Modern}"
  whenToUse: "{When to activate this agent}"
  customization: |
    [Key behavioral notes]

persona:
  role: "{Professional role}"
  style: "{Communication style}"
  identity: "{One-sentence identity}"
  focus: "{What they focus on}"
  background: |
    [Brief background from crucible story]

core_principles:
  - "[Principle 1 - from frameworks/rules]"
  - "[Principle 2]"
  - "[Principle 3]"

commands:
  - "*help - View available commands"
  - "*{command1} - [Description]"
  - "*{command2} - [Description]"
  [Continue with all commands]

operational_frameworks:
  [All 10 frameworks from Phase 2]

communication_dna:
  [Complete DNA from Phase 3]

signature_phrases:
  [All 7 tiers from Phase 4]

authority_proof_arsenal:
  [Complete arsenal from Phase 5]

objection_algorithms:
  [All 5 algorithms from Phase 6]

{copywriter}_rules:
  [All rules from Phase 7]

security:
  [Boundaries and limitations]

dependencies:
  [Required files and resources]

knowledge_areas:
  [Topics the agent is expert in]

capabilities:
  [What the agent can do]
```
---
**MMOS Integration Note:**
[If mind exists in database, link to it]
```

### Output

- **File:** `squads/copy/agents/{slug}.md`

### Quality Gate: Assembly

```
MANDATORY CHECKS:
- [ ] All sections populated
- [ ] Structure matches reference agents
- [ ] No placeholder text remaining
- [ ] YAML blocks are valid
- [ ] Markdown renders correctly

QUALITY CHECKS:
- [ ] Greeting sounds like them
- [ ] Commands are relevant to their expertise
- [ ] Integration references are accurate
```

---

## PHASE 9: VALIDATION

**Execute Checklist:** `checklists/copywriter-agent-creation-checklist.md`

### Validation Process

```yaml
validation_process:

  structural_validation:
    - "All required sections present"
    - "YAML syntax valid"
    - "Markdown renders correctly"
    - "No placeholder text"

  content_validation:
    - "10 frameworks documented"
    - "42+ signature phrases"
    - "5 objection algorithms"
    - "Complete communication DNA"
    - "Full authority arsenal"
    - "26+ rules"

  authenticity_validation:
    - "Voice is distinctive (not generic)"
    - "Frameworks are their methodology"
    - "Phrases are from actual sources"
    - "Statistics are verifiable"

  functionality_testing:
    test_prompts:
      - "Ask for advice on [their expertise]"
      - "Ask about their methodology"
      - "Raise common objection"
      - "Request specific framework"
    pass_criteria:
      - "Response sounds like them"
      - "Uses signature vocabulary"
      - "References their frameworks"
      - "Includes appropriate phrases"
```

### Scoring Targets

| Section | Target | Weight |
|---------|--------|--------|
| Required Sections | 100% | 15% |
| Operational Frameworks | 90%+ | 20% |
| Communication DNA | 90%+ | 20% |
| Signature Phrases | 90%+ | 15% |
| Authority Arsenal | 90%+ | 15% |
| Objection Algorithms | 90%+ | 10% |
| Final Validation | 90%+ | 5% |

**Overall Target: 90%+**

### Output

- **File:** `{pasta}/{slug}/analysis/validation-report.md`

### Quality Gate: Validation

```
- [ ] Overall score 90%+
- [ ] All critical issues resolved
- [ ] YAML syntax validated
- [ ] Agent tested with sample prompts
- [ ] Distinctiveness confirmed
```

---

## FINAL OUTPUT SUMMARY

Upon successful completion:

### Analysis Files

| File | Location |
|------|----------|
| frameworks.yaml | `{pasta}/{slug}/analysis/` |
| communication-dna.yaml | `{pasta}/{slug}/analysis/` |
| signature-phrases.yaml | `{pasta}/{slug}/analysis/` |
| authority-arsenal.yaml | `{pasta}/{slug}/analysis/` |
| objection-algorithms.yaml | `{pasta}/{slug}/analysis/` |
| {slug}-rules.yaml | `{pasta}/{slug}/analysis/` |
| validation-report.md | `{pasta}/{slug}/analysis/` |

### Agent File

| File | Location |
|------|----------|
| {slug}.md | `squads/copy/agents/` |

---

## TROUBLESHOOTING

### Common Issues

**Issue:** Not enough source material

**Solutions:**
- Supplement with YouTube/podcast transcripts
- Search for interviews and appearances
- Check social media for threads/posts
- Look for book excerpts and reviews

---

**Issue:** Framework overlap

**Solutions:**
- Merge similar frameworks
- Keep the 10 most distinctive
- Look for unique applications
- Focus on process differences

---

**Issue:** Generic-sounding phrases

**Solutions:**
- Dig deeper into sources
- Look for unusual word combinations
- Find their distinctive expressions
- Verify uniqueness against common phrases

---

**Issue:** Incomplete authority arsenal

**Solutions:**
- Search harder for origin stories
- Use available metrics only
- Focus on qualitative proof
- Check all interview content

---

**Issue:** Validation score below 90%

**Solutions:**
- Review failed sections
- Supplement missing components
- Improve weak areas
- Re-test after improvements

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2024-01 | Initial task creation |
| 2.0.0 | 2026-01-23 | Complete rewrite with research-first methodology, added theoretical foundation, expanded all phases, detailed quality gates |

---

*CopywriterOS Task v2.0.0*
*Part of the AIOS Squad System*
*Based on: docs/research/copywriter-agent-creation-methodology-research.md*
