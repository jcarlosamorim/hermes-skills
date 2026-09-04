# CPL {{cpl_number}} Evaluation Report

> **Product:** {{product_name}}
> **Creator:** {{creator_name}}
> **Evaluated:** {{evaluation_date}}
> **Workflow:** wf-evaluate-cpl v2.0

---

## Executive Summary

| Metric | Value |
|--------|-------|
| **Overall Score** | {{overall_score}}/10 |
| **Status** | {{status}} |
| **Beat Score** | {{beat_score}}/10 |
| **Rubric Score** | {{rubric_score}}/10 |
| **Trigger Score** | {{trigger_score}}/10 |
| **Mistakes Detected** | {{mistakes_count}}/15 |
| **Veto Conditions** | {{veto_count}} triggered |

### Verdict

{{#if status_pass}}
**PASS** — This CPL meets the minimum quality standards for launch.
{{/if}}
{{#if status_launch_winning}}
**LAUNCH WINNING** — This CPL exceeds expectations. Ready for launch as-is.
{{/if}}
{{#if status_needs_work}}
**NEEDS WORK** — This CPL has significant gaps that should be addressed before launch.
{{/if}}
{{#if status_fail}}
**FAIL** — This CPL requires major revision. Do not launch without rewriting.
{{/if}}

### Critical Issues (Fix First)

{{#each critical_issues}}
- **{{this.type}}:** {{this.description}}
{{/each}}

{{#if no_critical_issues}}
No critical issues detected.
{{/if}}

---

## Beat-by-Beat Analysis

### Expected vs. Actual Structure

| Beat | Expected | Found | Score | Status |
|------|----------|-------|-------|--------|
{{#each beats}}
| {{this.name}} | {{this.expected_duration}} | {{this.actual_duration}} | {{this.score}}/5 | {{this.status_icon}} |
{{/each}}

### Beat Details

{{#each beats}}
#### {{this.order}}. {{this.name}}

**Location:** Lines {{this.start_line}}-{{this.end_line}} ({{this.actual_duration}})

**Score:** {{this.score}}/5 — {{this.score_label}}

**Evidence:**
> "{{this.evidence_quote}}"

**Copy Framework Used:** {{this.copy_framework}}

**Gaps Identified:**
{{#each this.gaps}}
- {{this}}
{{/each}}

{{#if this.gaps_empty}}
No gaps identified.
{{/if}}

---

{{/each}}

## Self-Assessment Rubric Scores

### Dimension Breakdown

| Dimension | Score | Weight | Weighted | Evidence |
|-----------|-------|--------|----------|----------|
{{#each rubric_dimensions}}
| {{this.name}} | {{this.score}}/5 | {{this.weight}} | {{this.weighted_score}} | {{this.evidence_summary}} |
{{/each}}
| **Total** | | | **{{rubric_weighted_total}}** | |

### Dimensions Below Threshold

{{#each low_dimensions}}
#### {{this.name}} (Score: {{this.score}}/5)

**Current State:** {{this.current_description}}

**What "Solid" (3) Looks Like:**
{{this.solid_description}}

**What "Exceptional" (5) Looks Like:**
{{this.exceptional_description}}

**Gap to Close:**
{{this.gap_description}}

**Specific Improvement:**
{{this.improvement_suggestion}}

---

{{/each}}

{{#if no_low_dimensions}}
All dimensions meet minimum threshold (3+).
{{/if}}

---

## Mistake Detection

### Summary

- **Critical Mistakes (#1-5):** {{critical_mistakes_count}} detected
- **Significant Mistakes (#6-10):** {{significant_mistakes_count}} detected
- **Minor Mistakes (#11-15):** {{minor_mistakes_count}} detected
- **Total Damage Score:** {{total_damage_score}}

### Detected Mistakes (Ranked by Damage)

{{#each detected_mistakes}}
#### Mistake #{{this.rank}}: {{this.name}}

**Severity:** {{this.severity}} ({{this.damage_multiplier}}x damage)

**Description:** {{this.description}}

**Evidence:**
> "{{this.evidence_quote}}"
> — Line {{this.evidence_line}}

**Why This Damages the CPL:**
{{this.damage_explanation}}

**How to Fix:**
{{this.fix_suggestion}}

---

{{/each}}

{{#if no_mistakes}}
No mistakes detected.
{{/if}}

### Mistakes Successfully Avoided

{{#each avoided_mistakes}}
- **#{{this.rank}}:** {{this.name}} — {{this.avoidance_evidence}}
{{/each}}

---

## Mental Trigger Analysis

### Trigger Activation Map

| Trigger | Expected In | Activated? | Intensity | Notes |
|---------|-------------|------------|-----------|-------|
{{#each triggers}}
| {{this.name}} | {{this.expected_beats}} | {{this.activated_icon}} | {{this.intensity}}/5 | {{this.notes}} |
{{/each}}

### Primary Triggers (Critical for CPL {{cpl_number}})

{{#each primary_triggers}}
#### {{this.name}}

**Status:** {{this.status}}

**Where Activated:** {{this.location}}

**Intensity:** {{this.intensity}}/5

**Mechanism Used:**
{{this.mechanism}}

**Evidence:**
> "{{this.evidence_quote}}"

{{#if this.missing}}
**Impact of Missing Trigger:**
{{this.missing_impact}}

**How to Activate:**
{{this.activation_suggestion}}
{{/if}}

---

{{/each}}

### Cumulative Emotional State

At the end of this CPL, the viewer should feel:
{{expected_emotional_state}}

**Actual State Based on Trigger Analysis:**
{{actual_emotional_state}}

**Gap:**
{{emotional_state_gap}}

---

## Prioritized Recommendations

### Priority 1: Critical (Must Fix Before Launch)

{{#each priority_1}}
{{this.order}}. **{{this.title}}**
   - Issue: {{this.issue}}
   - Fix: {{this.fix}}
   - Impact: {{this.impact}}
{{/each}}

{{#if priority_1_empty}}
No critical issues requiring immediate attention.
{{/if}}

### Priority 2: Important (Should Fix)

{{#each priority_2}}
{{this.order}}. **{{this.title}}**
   - Issue: {{this.issue}}
   - Fix: {{this.fix}}
   - Impact: {{this.impact}}
{{/each}}

### Priority 3: Nice to Have (Polish)

{{#each priority_3}}
{{this.order}}. **{{this.title}}**
   - Opportunity: {{this.opportunity}}
   - Suggestion: {{this.suggestion}}
{{/each}}

---

## Rewrite Suggestions

### Beats Requiring Rewrite (Score < 3)

{{#each rewrite_beats}}
#### {{this.name}} — Current Score: {{this.score}}/5

**Current Copy:**
```
{{this.current_copy}}
```

**Problem:**
{{this.problem}}

**Suggested Rewrite (Using {{this.framework}} Framework):**
```
{{this.suggested_copy}}
```

**Why This Works Better:**
{{this.improvement_explanation}}

---

{{/each}}

{{#if no_rewrites_needed}}
All beats score 3+. No rewrites required.
{{/if}}

---

## Comparison to PLF Standards

### This CPL vs. Launch-Winning Benchmarks

| Metric | This CPL | PLF Benchmark | Gap |
|--------|----------|---------------|-----|
| Beat Coverage | {{beat_coverage}}% | 100% | {{beat_coverage_gap}}% |
| Rubric Average | {{rubric_average}} | 4.0 | {{rubric_gap}} |
| Trigger Activation | {{trigger_activation}}% | 90%+ | {{trigger_gap}}% |
| Mistakes | {{mistakes_count}} | 0-2 | {{mistakes_gap}} |

### Where This CPL Excels

{{#each strengths}}
- **{{this.area}}:** {{this.description}}
{{/each}}

### Where This CPL Falls Short

{{#each weaknesses}}
- **{{this.area}}:** {{this.description}}
{{/each}}

---

## Next Steps

1. {{next_step_1}}
2. {{next_step_2}}
3. {{next_step_3}}

---

## Appendix: Raw Scores

```yaml
beat_scores:
{{#each beats}}
  {{this.id}}: {{this.score}}
{{/each}}

rubric_scores:
{{#each rubric_dimensions}}
  {{this.id}}: {{this.score}}
{{/each}}

trigger_scores:
{{#each triggers}}
  {{this.id}}: {{this.intensity}}
{{/each}}

mistakes_detected:
{{#each detected_mistakes}}
  - {{this.rank}}
{{/each}}
```

---

*Report generated by wf-evaluate-cpl v2.0*
*Production Aid: {{production_aid_used}}*
*Evaluation depth: {{evaluation_depth}}*
