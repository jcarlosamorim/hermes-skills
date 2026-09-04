---
task-id: optimize-copy
name: Optimize Existing Copy
agent: copywriter
version: 1.0.0
purpose: Analyze and optimize existing copy for better conversion rates

workflow-mode: interactive
elicit: true
elicitation-type: custom

prerequisites:
  - Existing copy to optimize
  - Current performance data (optional but helpful)

inputs:
  - name: current_copy
    type: text
    description: The existing copy to optimize
    required: true
  - name: goal
    type: enum
    description: Optimization goal
    required: true
    options: ["higher-ctr", "more-conversions", "better-engagement", "clearer-message"]
  - name: performance_data
    type: object
    description: Current performance metrics (CTR, conversion rate, etc.)
    required: false

outputs:
  - path: "outputs/copywriter-os/{date}-optimized-{slug}.md"
    description: Optimized copy with analysis
    format: "markdown"

validation:
  success-criteria:
    - "Issues in current copy identified"
    - "Specific optimizations suggested"
    - "Optimized version provided"
    - "A/B test recommendations included"
---

# Task: Optimize Existing Copy

## Purpose

Analyze existing copy, identify weaknesses, and provide an optimized version with specific improvement recommendations.

## Steps

### Step 1: Analyze Current Copy
Review the existing copy for:
- **Structure:** Does it follow a proven framework?
- **Headline:** Is it compelling and benefit-driven?
- **CTA:** Is it clear, single, and actionable?
- **Benefits vs Features:** Are benefits leading?
- **Readability:** Is it scannable and clear?
- **Tone:** Is it consistent and appropriate?

### Step 2: Identify Issues
List specific problems:
- Weak headline (no benefit, no curiosity)
- Buried CTA or multiple CTAs
- Feature-focused instead of benefit-focused
- Too long/short for the format
- Missing social proof
- Unclear value proposition

### Step 3: Optimize
Rewrite the copy with:
- Stronger headline with benefit/curiosity
- Framework-structured body
- Highlighted benefits
- Clear, single CTA
- Added social proof elements

### Step 4: A/B Recommendations
Suggest specific A/B tests:
- Headline variants to test
- CTA wording alternatives
- Layout/structure changes

## Success Criteria
- [ ] Current copy issues identified
- [ ] Optimized version provided
- [ ] Specific changes explained
- [ ] A/B test plan included
