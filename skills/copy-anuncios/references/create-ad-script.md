# Create Ad Script Task

## Metadata

```yaml
task_id: create-ad-script
version: 2.0
framework: copy-framework-v2
category: video_advertising
complexity: advanced
estimated_time: 60-120min
requires_research: true

dependencies:
  research: docs/research/ad-script-methodology-research.md
  templates: templates/ad-script-templates/

theoretical_foundation:
  - Eugene Schwartz - Breakthrough Advertising (5 Awareness Levels)
  - Alex Hormozi - $100M GOATed Ads Playbook
  - UGC Best Practices 2025-2026
```

---

## Purpose

Create high-converting video ad scripts using the Hormozi GOATed Ads methodology: 50 hooks × 3-5 meats × 1-3 CTAs = 150-750 ad combinations for systematic testing at scale.

**Core Principle:**
> "Your job is not to create one perfect ad. Your job is to create a testing machine. Let the data tell you what works."

**Critical Insight:**
- 80% of ad performance is determined by the first 1-3 seconds
- Spend 80% of creative effort on the hook
- The rest is optimization

---

## Phase 1: Information Gathering

### 1.1 Required Inputs

```yaml
product_context:
  product_name:
    required: true
    description: "What you're advertising"

  product_type:
    required: true
    options:
      - physical_product
      - digital_product
      - saas_software
      - service
      - course_coaching
      - info_product
      - event
      - lead_magnet

  offer:
    required: true
    description: "The specific offer (price, bonuses, guarantee)"

  unique_mechanism:
    required: true
    description: "What makes this different from alternatives?"

audience_context:
  target_avatar:
    required: true
    description: "Who is the ideal customer? Be specific."

  main_transformation:
    required: true
    format: "Before state → After state"
    example: "Struggling freelancer → Booked 3 months out"

  primary_pain:
    required: true
    description: "The #1 problem this solves"

  primary_desire:
    required: true
    description: "What they really want"

campaign_context:
  platform:
    required: true
    options:
      - tiktok
      - youtube_instream
      - youtube_shorts
      - meta_feed
      - meta_reels
      - instagram_stories
      - linkedin

  ad_format:
    required: true
    options:
      - video_ugc
      - video_produced
      - talking_head
      - demo_product
      - testimonial
      - animation
      - static_to_video

  funnel_stage:
    required: true
    options:
      - cold_traffic
      - warm_retargeting
      - hot_retargeting
```

### 1.2 Optional Inputs

```yaml
performance_context:
  current_winning_ads:
    description: "Links to current best performers"

  winning_hooks:
    description: "Hooks that have worked before"

  budget_daily:
    description: "Daily ad spend"

proof_elements:
  testimonials:
    description: "Customer results available"

  case_studies:
    description: "Documented transformations"

  statistics:
    description: "Numbers, data, percentages"

  credentials:
    description: "Authority markers"

competitor_context:
  competitor_ads:
    description: "Links to competitor ads for inspiration"
```

---

## Phase 2: Awareness Level Assessment

### 2.1 Eugene Schwartz's 5 Levels

**Select the target awareness level for this campaign:**

```yaml
level_1_unaware:
  definition: "Don't know they have a problem"
  audience_size: "Largest"
  temperature: "Coldest"

  identification:
    - "Going about their day normally"
    - "Haven't identified the pain yet"
    - "May not admit the problem to themselves"

  approach:
    - Spark curiosity
    - Tell stories
    - Highlight what feels "off"
    - Don't sell directly

  hook_types:
    - Curiosity-driven
    - Story openings
    - Phenomena-based
    - Shocking statistics

  example_hooks:
    - "The hidden [thing] that's costing you [pain]"
    - "Why [counterintuitive statement]"
    - "[Number]% of [avatar] don't know this about [topic]"
    - "Something weird is happening with [topic]..."

level_2_problem_aware:
  definition: "Know the problem, not the solution"
  audience_size: "Large"
  temperature: "Cool"

  identification:
    - "They know they're struggling"
    - "Haven't figured out how to fix it"
    - "May be blaming themselves"

  approach:
    - Help them name the problem
    - Agitate the pain
    - Show you understand
    - Validate their frustration

  hook_types:
    - Pain-driven
    - Agitation
    - "You're not alone"

  example_hooks:
    - "Tired of [specific problem]?"
    - "If you're still [old way], you're [losing X]"
    - "Stop [wrong approach]. Here's why..."
    - "The real reason [problem] keeps happening"

level_3_solution_aware:
  definition: "Know solutions exist, not your product"
  audience_size: "Medium"
  temperature: "Warm"

  identification:
    - "They've tried things before"
    - "Maybe failed with alternatives"
    - "Looking for something different"

  approach:
    - Differentiate your solution
    - Show unique mechanism
    - Promise specific results
    - Address why other solutions fail

  hook_types:
    - Promise-driven
    - Differentiation
    - Unique mechanism reveal

  example_hooks:
    - "How to [achieve result] in [timeframe]"
    - "The fastest way to [desire] without [sacrifice]"
    - "[Result] in [time] - introducing [product]"
    - "Why [common solution] doesn't work and what to do instead"

level_4_product_aware:
  definition: "Know your product, not convinced"
  audience_size: "Smaller"
  temperature: "Hot"

  identification:
    - "They've seen your ads/content"
    - "Visited your site"
    - "Need more proof to convert"

  approach:
    - Stack proof elements
    - Show testimonials
    - Address specific objections
    - Build certainty

  hook_types:
    - Proof-driven
    - Testimonial-led
    - Objection handling

  example_hooks:
    - "Why [number] people chose [product] to [result]"
    - "See how [avatar] got [specific result]"
    - "[Customer name] went from [before] to [after]"
    - "Still on the fence about [product]? Watch this."

level_5_most_aware:
  definition: "Know you, just need the deal"
  audience_size: "Smallest"
  temperature: "Hottest"

  identification:
    - "Ready to buy"
    - "Waiting for the right moment"
    - "Previous customers or engaged leads"

  approach:
    - Lead with offer
    - Add urgency/scarcity
    - Remove friction
    - Make it easy

  hook_types:
    - Offer-driven
    - Urgency/scarcity
    - Deal announcements

  example_hooks:
    - "[Discount]% off [product] - [deadline]"
    - "Last chance: [bonus] expires [when]"
    - "New: [feature] now included with [product]"
    - "You asked for it—[offer] is finally here"
```

### 2.2 Awareness Selection Matrix

```yaml
campaign_type_to_awareness:
  cold_prospecting:
    primary: "Level 1-2 (Unaware, Problem-Aware)"
    why: "Building initial interest"

  lead_generation:
    primary: "Level 2-3 (Problem-Aware, Solution-Aware)"
    why: "Capturing interested prospects"

  retargeting_engaged:
    primary: "Level 3-4 (Solution-Aware, Product-Aware)"
    why: "They know you exist"

  retargeting_cart:
    primary: "Level 4-5 (Product-Aware, Most Aware)"
    why: "Close to purchase"

  customer_reactivation:
    primary: "Level 5 (Most Aware)"
    why: "They already trust you"
```

---

## Phase 3: Platform-Specific Script Structures

### 3.1 TikTok Ad Scripts

```yaml
platform_context:
  attention_span: "1.3-2 seconds"
  style: "Native, authentic, not 'ad-like'"
  aesthetic: "DIY > polished"
  sound: "Essential (audio-on platform)"
  optimal_length: "15-60 seconds (21-34s sweet spot)"

script_structure:
  0-3s:
    name: "HOOK"
    purpose: "Pattern interrupt, stop scroll"
    critical: true
    must_have:
      - Text overlay
      - Immediate attention grab
      - Native feel
      - Value signal

  3-15s:
    name: "PROBLEM/STORY"
    purpose: "Connect with pain or journey"
    approaches:
      - "I had this problem..."
      - "Everyone does this wrong..."
      - "Here's what nobody tells you..."
      - Relatable situation setup

  15-25s:
    name: "SOLUTION"
    purpose: "Reveal product/method"
    approaches:
      - Product demo
      - Before/after
      - Mechanism explanation
      - "Then I discovered..."

  25-30s:
    name: "CTA"
    purpose: "Drive action"
    native_ctas:
      - "Link in bio"
      - "Comment [word] for link"
      - "Follow for part 2"
      - "Save this for later"

tiktok_rules:
  - DON'T look like an ad
  - Use trending sounds when relevant
  - Feature real people (creators, employees, customers)
  - Lean into trends, memes, challenges
  - Use creator-style language ("no cap", "lowkey", "literally")
  - Authentic > Polished always
```

### 3.2 YouTube In-Stream Ad Scripts

```yaml
platform_context:
  skip_after: "5 seconds"
  critical_window: "0-5 seconds = everything"
  ideal_length: "30-60 seconds"
  viewer_intent: "Watching content, ad is interruption"
  effort_allocation: "Spend 80% of creative time on first 5 seconds"

script_structure:
  0-5s:
    name: "HOOK (Pre-Skip Window)"
    purpose: "MUST keep them watching"
    critical: true
    techniques:
      - Lead with end result
      - Make bold claim
      - Pattern interrupt
      - Direct address avatar
    warning: "If you lose here, nothing else matters"

  5-15s:
    name: "PROBLEM"
    purpose: "Connect with their pain"
    techniques:
      - Agitate the problem
      - Show you understand
      - Create emotional connection
      - "You've probably tried..."

  15-35s:
    name: "SOLUTION"
    purpose: "Present your offer/product"
    techniques:
      - Present unique mechanism
      - Explain how it's different
      - Stack benefits
      - "What if there was..."

  35-50s:
    name: "PROOF"
    purpose: "Build credibility"
    techniques:
      - Show real results
      - Use specific numbers
      - Include testimonials
      - Authority markers

  50-60s:
    name: "CTA"
    purpose: "Drive action"
    techniques:
      - Tell exactly what to do
      - Give reason to act NOW
      - Remove friction
      - Show what happens next

youtube_5_second_hook_patterns:
  bold_claim:
    template: "I'm going to show you how to [result] in [timeframe]."
    example: "I'm going to show you how to get 100 leads per day in 60 seconds."

  question:
    template: "What if you could [desired outcome] without [obstacle]?"
    example: "What if you could lose 20 pounds without giving up your favorite foods?"

  pattern_interrupt:
    description: "Start mid-action, unusual visual, unexpected statement"
    example: "*Person mid-sentence* ...and that's exactly why most ads fail."

  social_proof:
    template: "Over [X] people have already [result] with this..."
    example: "Over 50,000 entrepreneurs have tripled their income with this method."

  direct_address:
    template: "Hey [avatar], if you're struggling with [problem], watch this."
    example: "Hey business owner, if you can't find good employees, the next 60 seconds will change everything."
```

### 3.3 Meta (Facebook/Instagram) Video Scripts

```yaml
platform_context:
  autoplay: "Yes (often muted)"
  text_overlay: "Critical for silent viewing"
  attention_span: "Slightly longer than TikTok"
  sound: "Design for sound-off first"

feed_videos:
  optimal_length: "15-30 seconds"

  script_structure:
    0-3s:
      name: "HOOK"
      purpose: "Stop scroll"
      must_have:
        - Strong text overlay
        - Visual pattern interrupt
        - Works without sound

    3-15s:
      name: "VALUE"
      purpose: "Problem/solution"
      approaches:
        - Agitate problem
        - Present solution
        - Show transformation

    15-25s:
      name: "PROOF"
      purpose: "Build belief"
      elements:
        - Results
        - Testimonials
        - Data

    25-30s:
      name: "CTA"
      purpose: "Clear action"
      must_have:
        - Specific instruction
        - Visual CTA reinforcement

stories_reels:
  optimal_length: "15 seconds"
  format: "Vertical 9:16"

  script_structure:
    0-3s: "HOOK - Text + visual grab"
    3-12s: "CORE MESSAGE - Main value"
    12-15s: "CTA - Swipe up/action"

meta_specific_rules:
  - Design for sound-off first (captions essential)
  - Use text overlays on every key point
  - Front-load the message
  - Mobile-first framing (faces centered)
  - Test square (1:1) vs vertical (4:5) vs stories (9:16)
```

### 3.4 VSL (Video Sales Letter) Scripts

```yaml
context:
  length: "5-45+ minutes"
  purpose: "Full sales presentation in video format"
  conversion_lift: "Up to 3x vs text sales pages"
  best_for: "High-ticket, complex offers, webinar replays"

vsl_structure:
  attention:
    duration: "First 30-60 seconds"
    purpose: "Hook and big promise"
    elements:
      - Pattern interrupt
      - Big bold promise
      - Credibility hint
      - "Stay till the end" hook

  problem:
    duration: "2-5 minutes"
    purpose: "Agitate the pain deeply"
    elements:
      - Identify the problem specifically
      - Make it vivid and emotional
      - Show consequences of not solving
      - "You're not alone" validation

  solution:
    duration: "3-7 minutes"
    purpose: "Present unique mechanism"
    elements:
      - Introduce your concept/method
      - Explain why it's different
      - Build belief in the approach
      - Name the system/framework

  credibility:
    duration: "2-5 minutes"
    purpose: "Build trust"
    elements:
      - Your story (relatable)
      - Credentials and experience
      - Results you've achieved
      - Why you created this

  offer:
    duration: "3-5 minutes"
    purpose: "Present what they get"
    elements:
      - Core product/service
      - Bonuses (stack the value)
      - Price anchoring
      - Total value summary

  proof:
    duration: "3-7 minutes"
    purpose: "Overcome skepticism"
    elements:
      - Multiple testimonials
      - Case studies with specifics
      - Data and statistics
      - Before/after stories

  close:
    duration: "2-5 minutes"
    purpose: "Drive action NOW"
    elements:
      - Price reveal (with justification)
      - Guarantee (reverse risk)
      - Urgency/scarcity
      - Clear CTA instructions
      - Future pacing (life after purchase)
      - Final push
```

---

## Phase 4: Hook Writing Session (50 Hooks)

### 4.1 Hook Sources

```yaml
source_1_your_winners:
  what: "Previous winning ad hooks"
  action: "Analyze what worked, create 10 variations"
  questions:
    - "Which hook got highest CTR?"
    - "Which hook got best retention?"
    - "What pattern can you replicate?"

source_2_organic_content:
  what: "Your best-performing organic posts/videos"
  action: "Repurpose viral content openings into ad hooks"
  questions:
    - "Which post got most engagement?"
    - "What made people stop scrolling?"
    - "Can this opening work as an ad?"

source_3_competitor_ads:
  what: "Hooks from top competitors"
  action: "Swipe and adapt (don't copy word-for-word)"
  tools:
    - Meta Ad Library
    - TikTok Creative Center
    - Foreplay.co
    - AdSpy

source_4_cross_industry:
  what: "Hooks from different industries"
  action: "Apply successful patterns to your niche"
  why: "Best hooks often come from outside your category"
```

### 4.2 Hook Formula Templates by Awareness Level

```yaml
curiosity_hooks_level_1_2:
  template_1: "The hidden [thing] that's costing you [pain]"
  template_2: "Why [counterintuitive statement]"
  template_3: "[Number]% of [avatar] don't know this about [topic]"
  template_4: "Nobody's talking about this [topic] secret"
  template_5: "I discovered something weird about [topic]"
  template_6: "The [topic] mistake everyone makes"
  template_7: "What [successful group] knows that you don't"
  template_8: "Why [common practice] is actually hurting you"

pain_hooks_level_2:
  template_1: "Tired of [specific problem]?"
  template_2: "If you're still [old way], you're [losing X]"
  template_3: "Stop [wrong approach]. Here's why..."
  template_4: "The real reason [problem] keeps happening"
  template_5: "Are you [negative state] because of [problem]?"
  template_6: "[Problem] ruining your [area of life]?"
  template_7: "Struggling with [problem]? You're not alone"
  template_8: "Why [problem] won't go away (and what to do)"

promise_hooks_level_3:
  template_1: "How to [achieve result] in [timeframe]"
  template_2: "The fastest way to [desire] without [sacrifice]"
  template_3: "[Result] in [time] - here's how"
  template_4: "From [before] to [after] in [timeframe]"
  template_5: "The [number]-step system for [result]"
  template_6: "What if you could [result] starting today?"
  template_7: "The method that got me [specific result]"
  template_8: "Finally: a way to [result] that actually works"

proof_hooks_level_4:
  template_1: "Why [number] people chose [product]"
  template_2: "See how [avatar] got [specific result]"
  template_3: "[Customer] went from [before] to [after]"
  template_4: "[Number] [avatar]s can't be wrong"
  template_5: "The results speak for themselves..."
  template_6: "After [timeframe], [customer] achieved [result]"
  template_7: "Here's what happened when [customer] tried [product]"
  template_8: "Real results from real [avatar]s"

offer_hooks_level_5:
  template_1: "[Discount]% off [product] - [deadline]"
  template_2: "Last chance: [bonus] expires [when]"
  template_3: "New: [feature] now included"
  template_4: "Finally back in stock"
  template_5: "Limited time: [special offer]"
  template_6: "You asked, we listened: [offer]"
  template_7: "For the next [time], get [bonus]"
  template_8: "[Product] just got even better"
```

### 4.3 Hook Generation Worksheet

```yaml
generate_50_hooks:
  instructions: |
    Using the templates above and your inputs, generate:
    - 10 Curiosity Hooks (Levels 1-2)
    - 10 Pain Hooks (Level 2)
    - 12 Promise Hooks (Level 3)
    - 10 Proof Hooks (Level 4)
    - 8 Offer Hooks (Level 5)

  output_format:
    |
    ## CURIOSITY HOOKS (Level 1-2)
    1. [Hook]
    2. [Hook]
    ...

    ## PAIN HOOKS (Level 2)
    1. [Hook]
    2. [Hook]
    ...

    ## PROMISE HOOKS (Level 3)
    1. [Hook]
    2. [Hook]
    ...

    ## PROOF HOOKS (Level 4)
    1. [Hook]
    2. [Hook]
    ...

    ## OFFER HOOKS (Level 5)
    1. [Hook]
    2. [Hook]
    ...
```

---

## Phase 5: Ad Meat Selection (3-5 Formats)

### 5.1 Meat Format Options

```yaml
format_1_demonstration:
  description: "Show the product/service in action"
  types:
    - Product demo/unboxing
    - Before/after comparison
    - Live use or reaction
    - Screen recording (software)
    - High production hero ad

  best_for:
    - Physical products
    - Software/SaaS
    - Tangible results

  production_needs: "Medium-High"

format_2_testimonial:
  description: "Real customers sharing experiences"
  types:
    - Direct to camera testimonial
    - Podcast-style clip
    - Walk-n-talk rant
    - Parade of proof (multiple testimonials)
    - Raw iPhone style
    - Interview format

  best_for:
    - Services
    - Coaching/courses
    - B2B offerings

  production_needs: "Low-Medium"

format_3_education:
  description: "Teach something valuable"
  types:
    - Whiteboard explainer
    - How-to/tutorial
    - Listicle ("3 ways to...")
    - Myth-busting
    - Expert breakdown

  best_for:
    - Complex products
    - B2B
    - Premium offers
    - Thought leadership

  production_needs: "Medium"

format_4_story:
  description: "Narrative-driven content"
  types:
    - Origin story/founder journey
    - Customer transformation story
    - Problem-solution narrative
    - Documentary style
    - Day-in-the-life

  best_for:
    - Brand building
    - Emotional connection
    - Premium positioning

  production_needs: "Medium-High"

format_5_faceless:
  description: "No person on camera"
  types:
    - Screenshot compilations (comments/texts)
    - Text-only with music
    - Slideshow with voiceover
    - Animation/cartoon
    - Stock footage + VO

  best_for:
    - Privacy concerns
    - Quick production
    - Scale content creation
    - Testing volume

  production_needs: "Low"
```

### 5.2 Meat Selection by Product Type

```yaml
physical_products:
  primary: "Demonstration"
  secondary: "Testimonial"
  tertiary: "Faceless (screenshots/reviews)"

services_consulting:
  primary: "Testimonial"
  secondary: "Education"
  tertiary: "Story"

saas_software:
  primary: "Demonstration (screen recording)"
  secondary: "Education"
  tertiary: "Testimonial"

courses_coaching:
  primary: "Education"
  secondary: "Testimonial"
  tertiary: "Story (transformation)"

info_products:
  primary: "Education"
  secondary: "Story"
  tertiary: "Testimonial"

ecommerce_general:
  primary: "Demonstration"
  secondary: "Faceless"
  tertiary: "Testimonial (UGC)"
```

---

## Phase 6: CTA Variations (1-3 CTAs)

### 6.1 CTA Formula

```
What to do + How to do it + When + What they get + What happens next
```

### 6.2 CTA Types

```yaml
cta_1_direct:
  template: "Click the button below to get [offer]"
  when: "Clear path to conversion"
  tone: "Straightforward"
  example: "Click the link below to start your free trial"

cta_2_urgency:
  template: "Tap now before [deadline/scarcity]"
  when: "Limited time/quantity offers"
  tone: "Time-sensitive"
  example: "Grab yours before the 50% off sale ends tonight"

cta_3_benefit_focused:
  template: "Start your [transformation] today - link below"
  when: "Softer sell, value-focused"
  tone: "Aspirational"
  example: "Start building your dream body today - link in bio"

cta_4_curiosity:
  template: "See what happens next →"
  when: "Multi-step funnels, lead gen"
  tone: "Intriguing"
  example: "Find out if you qualify - take the quiz"

cta_5_social_native:
  template: "Comment [word] and I'll send you the link"
  when: "TikTok/Instagram engagement"
  tone: "Interactive"
  example: "Comment 'READY' and I'll DM you the free guide"
```

### 6.3 Show & Tell CTA Enhancement

```yaml
visual_cta_elements:
  - Demonstrate clicking the button on screen
  - Show what the landing page looks like
  - Walk through the sign-up process
  - Display the checkout page
  - Show the product arriving/in use

why: "Reduces friction by showing exactly what happens next"
```

---

## Phase 7: Ad Assembly Matrix

### 7.1 Combinatorial Math

```yaml
formula: "50 hooks × 3-5 meats × 1-3 CTAs = 150-750 ad combinations"

example_calculation:
  hooks: 50
  meats: 4
  ctas: 3
  total_combinations: "50 × 4 × 3 = 600 unique ads"

reality_check: |
  You don't test all 600 at once.
  Start with top 10-20 combinations based on hypothesis.
  Let data guide expansion.
```

### 7.2 Assembly Strategy

```yaml
testing_priority:
  wave_1:
    focus: "Hooks (80% of impact)"
    test: "5-10 hook variations with 1 meat and 1 CTA"
    budget: "20% of test budget"

  wave_2:
    focus: "Meats with winning hooks"
    test: "Top 3 hooks × 3-4 meat formats"
    budget: "40% of test budget"

  wave_3:
    focus: "CTAs with winning combinations"
    test: "Top 2-3 hook+meat combos × 2-3 CTAs"
    budget: "40% of test budget"

  scale:
    focus: "Scale proven winners"
    action: "Increase budget on winners, create variations"
```

### 7.3 Assembly Matrix Template

```yaml
matrix_example:
  |
  | Hook Type  | Demo | Testimonial | Education | Story | CTA Options |
  |------------|------|-------------|-----------|-------|-------------|
  | Curiosity  | ✓    | -           | ✓         | ✓     | All 3       |
  | Pain       | -    | ✓           | ✓         | -     | 1, 3        |
  | Promise    | ✓    | -           | ✓         | ✓     | All 3       |
  | Proof      | -    | ✓           | -         | -     | 1, 2        |
  | Offer      | ✓    | -           | -         | -     | 2           |

top_10_combinations_to_test:
  1: "[Curiosity Hook #1] + [Demo] + [Direct CTA]"
  2: "[Pain Hook #1] + [Testimonial] + [Benefit CTA]"
  3: "[Promise Hook #1] + [Education] + [Direct CTA]"
  4: "[Curiosity Hook #2] + [Story] + [Curiosity CTA]"
  5: "[Pain Hook #2] + [Education] + [Direct CTA]"
  # ... continue for 10
```

---

## Phase 8: Full Script Templates

### 8.1 E-commerce Product Script

```
[0-3s] HOOK
"Stop scrolling if you [problem/desire]"

[3-10s] PROBLEM
"I used to [struggle with X]... tried everything..."

[10-20s] SOLUTION + DEMO
"Then I found [product]. Watch this—"
*Show product solving the problem*
"It [unique mechanism] so you get [benefit]"

[20-25s] PROOF
"After [timeframe], [specific result]"
*Show before/after or product in use*

[25-30s] CTA
"Link in bio to grab yours before they sell out"
```

### 8.2 Course/Coaching Script

```
[0-3s] HOOK
"How I went from [before] to [after] in [time]"

[3-12s] STORY
"[X time] ago, I was [struggling]..."
"I tried [thing 1], [thing 2]—nothing worked"
"Then I discovered [insight]..."

[12-22s] METHOD
"The key was [framework/system name]"
"It works because [mechanism]"
"No [sacrifice] required"

[22-27s] PROOF
"Now I [result] and I've helped [number] others do the same"
*Show testimonial clip or results*

[27-30s] CTA
"Want to learn how? Link in bio for the free training"
```

### 8.3 SaaS/Software Script

```
[0-3s] HOOK
"What if [pain point] only took [small time/effort]?"

[3-15s] DEMO
*Screen recording showing product*
"Watch this—[demonstrate key feature]"
"Instead of [old way], you just [new way]"

[15-22s] BENEFITS
"That means you get:
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]"

[22-27s] SOCIAL PROOF
"[Number] teams already use [product] to [result]"
*Show logos or testimonial*

[27-30s] CTA
"Try it free for 14 days—link below"
```

### 8.4 Service Business Script

```
[0-3s] HOOK
"[Avatar], still dealing with [problem]?"

[3-10s] AGITATE
"You've tried [solution 1], [solution 2]... nothing works"
"Meanwhile, [consequence getting worse]"

[10-18s] DIFFERENTIATE
"Here's why: [insight about why solutions fail]"
"We do it differently by [mechanism]"

[18-25s] PROOF
"[Client name] was stuck at [before].
After working with us, [after]"
*Show testimonial or results*

[25-30s] CTA
"Book a free call—link in bio"
```

### 8.5 UGC-Style Native Script

```
[0-3s] HOOK (native feel)
"Okay so nobody's talking about this but..."
OR "I have to tell you about this [product]"

[3-12s] STORY
"I was struggling with [problem]"
"I tried like everything—nothing worked"
"Then my [friend/influencer/ad] told me about [product]"

[12-22s] EXPERIENCE
"So I tried it and honestly?"
"[Specific result] in [timeframe]"
*Show product/results naturally*

[22-27s] RECOMMENDATION
"If you're dealing with [problem], you NEED to try this"
"Seriously, game changer"

[27-30s] SOFT CTA
"I'll link it below if you want to check it out"
```

---

## Phase 9: Output Deliverables

### 9.1 Output Format per Ad

```yaml
ad_deliverable:
  ad_name: "[Descriptive name]"
  platform: "[Platform]"
  duration: "[X seconds]"
  awareness_level: "[Level 1-5]"

  hook:
    text: "[Full hook text]"
    category: "[Curiosity/Pain/Promise/Proof/Offer]"
    text_overlay: "[If applicable]"

  meat:
    format: "[Demo/Testimonial/Education/Story/Faceless]"
    script: |
      [Full body script with timestamps]

  cta:
    type: "[Direct/Urgency/Benefit/Curiosity]"
    text: "[Full CTA text]"
    visual: "[Description of visual CTA]"

  full_script: |
    [0-Xs] HOOK
    "[Hook text]"

    [Xs-Xs] BODY
    "[Body text with timestamps]"

    [Xs-Xs] CTA
    "[CTA text]"

  production_notes:
    - "[Note 1]"
    - "[Note 2]"

  testing_priority: "[1-10]"
```

### 9.2 Complete Deliverable Package

```yaml
package_contents:
  summary:
    product: "[Product name]"
    platform: "[Platform]"
    awareness_target: "[Level]"
    hooks_generated: 50
    meats_selected: "[3-5]"
    ctas_created: "[1-3]"
    total_combinations: "[Number]"

  hook_library:
    curiosity: "[10 hooks]"
    pain: "[10 hooks]"
    promise: "[12 hooks]"
    proof: "[10 hooks]"
    offer: "[8 hooks]"

  meat_scripts:
    format_1: "[Full script]"
    format_2: "[Full script]"
    format_3: "[Full script]"

  cta_variations:
    cta_1: "[Script]"
    cta_2: "[Script]"
    cta_3: "[Script]"

  full_ads:
    ad_1: "[Complete ad deliverable]"
    ad_2: "[Complete ad deliverable]"
    ad_3: "[Complete ad deliverable]"
    # ... up to 5-10 priority ads

  assembly_matrix: "[Matrix showing all combinations]"

  testing_roadmap:
    week_1: "Test hooks (5-10 variations)"
    week_2: "Test meats with top 3 hooks"
    week_3: "Test CTAs with top combos"
    week_4: "Scale winners"
```

---

## Phase 10: Ad Metrics & Quality Gates

### 10.1 Performance Targets

```yaml
early_indicators_day_1_3:
  hook_hold_rate:
    good: ">50% watching past 3 seconds"
    red_flag: "<30%"

  thumb_stop_rate:
    good: ">30%"
    red_flag: "<15%"

  video_3s_views:
    good: ">30%"
    red_flag: "<15%"

engagement_metrics:
  ctr:
    good: ">1%"
    excellent: ">2%"
    red_flag: "<0.5%"

  link_ctr:
    good: ">0.8%"
    red_flag: "<0.5%"

cost_metrics:
  cpm:
    benchmark: "<$30"
    red_flag: ">$50"
    note: "Industry dependent"
```

### 10.2 Scaling Rules

```yaml
scale_when:
  - "ROAS >3x for 7 days straight"
  - "CPA stable for 500+ conversions"
  - "Frequency <3 after 14 days"
  - "CTR maintains >1%"

how_to_scale:
  gradual: "20% budget increase every 48h"
  horizontal: "New ad sets with same creative, different audience"
  creative_refresh: "New hooks with winning meat/CTA"

dont_scale_when:
  - "ROAS declining 3+ days"
  - "CPA increasing week over week"
  - "Frequency >3"
  - "CTR dropping below 0.8%"
```

### 10.3 Quality Checklist

```yaml
pre_launch:
  hook:
    - [ ] Stops scroll in <3 seconds
    - [ ] Matches awareness level
    - [ ] Platform-native feel
    - [ ] Clear value signal

  body:
    - [ ] Addresses pain/desire
    - [ ] Shows unique mechanism
    - [ ] Includes proof element
    - [ ] Maintains attention

  cta:
    - [ ] Clear action instruction
    - [ ] Reason to act now
    - [ ] Friction removed
    - [ ] Platform-appropriate

  production:
    - [ ] Audio quality acceptable
    - [ ] Text overlays readable
    - [ ] Platform specs met
    - [ ] Mobile-optimized
```

---

## Appendix: Quick Reference

### A.1 Awareness Level Quick Match

```yaml
cold_traffic: "Level 1-2 (Curiosity/Pain hooks)"
warm_traffic: "Level 2-3 (Pain/Promise hooks)"
hot_traffic: "Level 3-4 (Promise/Proof hooks)"
retargeting: "Level 4-5 (Proof/Offer hooks)"
```

### A.2 Platform Length Guide

```yaml
tiktok: "15-60s (21-34s optimal)"
youtube_instream: "30-60s"
youtube_shorts: "15-60s"
meta_feed: "15-30s"
meta_reels: "15-30s"
stories: "15s"
vsl: "5-45+ minutes"
```

### A.3 Hook Priority by Platform

```yaml
tiktok: "1-3 seconds to hook"
youtube: "5 seconds (pre-skip)"
meta: "3 seconds (silent hook)"
linkedin: "3-5 seconds"
```

---

## Version History

```yaml
version: 2.0
date: 2026-01-23
author: Ralph Autonomous Agent
project: Copy Framework v2.0 Upgrade
story: US-034

changes:
  - Complete rewrite following Framework v2.0 standards
  - Added comprehensive Schwartz awareness framework
  - Expanded Hook-Body-CTA structure
  - Added platform-specific script templates
  - Added Hormozi combinatorial testing methodology
  - Added full script templates for all use cases
  - Added quality gates and metrics targets
  - Research foundation: 670+ lines

line_count: 1100+
quality_gates:
  - [x] 600+ lines ✓
  - [x] Research foundation referenced ✓
  - [x] Platform-specific guidance ✓
  - [x] Multiple frameworks included ✓
  - [x] Quality checklist included ✓
  - [x] Actionable output format ✓
```

---

*Task Version: 2.0*
*Copy Framework v2.0 Upgrade*
*Research: docs/research/ad-script-methodology-research.md*
