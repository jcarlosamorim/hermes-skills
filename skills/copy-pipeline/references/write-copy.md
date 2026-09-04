---
task-id: write-copy
name: Write Copy
agent: copywriter
version: 1.0.0
purpose: Generate persuasive copy for any platform using proven copywriting frameworks

workflow-mode: interactive
elicit: true
elicitation-type: custom

prerequisites:
  - Product/service information available
  - Target audience defined

inputs:
  - name: copy_type
    type: enum
    description: Type of copy to write
    required: true
    options: ["landing-page", "ad-copy", "email", "social-post", "sales-page", "headline"]
  - name: product
    type: string
    description: Product or service name
    required: true
  - name: audience
    type: string
    description: Target audience description
    required: true
  - name: framework
    type: enum
    description: Copywriting framework to use
    required: false
    options: ["AIDA", "PAS", "BAB", "4Ps", "auto"]
    default: "auto"
  - name: tone
    type: enum
    description: Tone of voice
    required: false
    options: ["professional", "casual", "urgent", "inspirational", "conversational"]
    default: "professional"

outputs:
  - path: "outputs/copywriter-os/{date}-{type}-{product-slug}.md"
    description: Generated copy
    format: "markdown"

validation:
  success-criteria:
    - "Copy follows selected framework structure"
    - "Clear CTA included"
    - "Benefits highlighted over features"
    - "Appropriate tone maintained"
---

# Task: Write Copy

## Purpose

Generate persuasive marketing copy using proven frameworks. Supports landing pages, ads, emails, social posts, sales pages, and headlines.

## Steps

### Step 1: Gather Brief
Elicit from user:
1. Copy type (landing page, ad, email, social, sales page, headline)
2. Product/service details
3. Target audience
4. Key benefits (top 3)
5. Desired action (CTA)
6. Tone of voice
7. Framework preference (or auto-select)

### Step 2: Select Framework
Based on copy type and goals:
- **AIDA:** Attention → Interest → Desire → Action (best for landing pages)
- **PAS:** Problem → Agitate → Solution (best for pain-point driven copy)
- **BAB:** Before → After → Bridge (best for transformation stories)
- **4Ps:** Promise → Picture → Proof → Push (best for sales pages)

### Step 3: Write Copy
Generate copy following the framework:
- **Headline:** Attention-grabbing, benefit-driven
- **Subheadline:** Expand on the promise
- **Body:** Framework-structured argument
- **Social proof:** Testimonials, numbers, authority
- **CTA:** Clear, single, compelling action

### Step 4: Generate Variants
Provide 2-3 variants for:
- Headlines (different angles)
- CTAs (different urgency levels)
- Opening hooks

## Success Criteria
- [ ] Copy follows framework structure
- [ ] CTA is clear and compelling
- [ ] Variants provided for testing
- [ ] Tone matches brief
