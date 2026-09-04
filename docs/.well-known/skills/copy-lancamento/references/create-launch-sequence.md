# Task: Create Launch Sequence

> **Framework**: Product Launch Formula (Jeff Walker)
> **Agent**: @jeff-walker
> **Phase**: Strategy & Planning
> **Output**: Complete launch sequence strategy with timeline, phases, and task routing

---

## Purpose

Design the complete launch sequence strategy using Jeff Walker's Product Launch Formula. This task orchestrates the full launch timeline: Pre-Prelaunch → PLC Sequence → Open Cart → Close. It produces the strategic blueprint that routes to atomic PLF tasks for execution.

---

## Prerequisites

- [ ] Product/offer defined (what is being launched)
- [ ] Avatar research complete (who is buying)
- [ ] Launch dates confirmed (or at least a target window)
- [ ] Campaign brief exists (from copy-chief)

---

## Workflow Steps

### Step 1: Gather Context

**Elicit from user:**
```
1. What are you launching? (course, coaching, software, book, membership)
2. Is this your first launch or a relaunch?
3. What's your list size and relationship quality? (cold, warm, hot)
4. What's your launch window? (specific dates or "in X weeks")
5. Do you have existing proof? (testimonials, case studies, revenue data)
6. What's your comfort level with live events? (recorded only, hybrid, fully live)
7. What's your team capacity? (solo, small team, full team)
```

### Step 2: Select Launch Type

**Decision tree based on Jeff Walker's PLF:**

| Launch Type | Best For | List Size | Complexity | Timeline |
|-------------|----------|-----------|------------|----------|
| Seed Launch | First launch, no list, validation | 0-500 | Low | 1-2 weeks |
| Internal Launch | Existing list, proven offer | 500-50K | Medium | 3-4 weeks |
| JV Launch | Scale with partners | Any | High | 6-8 weeks |
| Evergreen Launch | Automated, ongoing | Any | Medium | 2 weeks setup |
| Live Launch | High engagement, premium | 1K+ | High | 4-6 weeks |

**Reference:**
- `data/plf/timeline-reference-kb.yaml`
- `data/plf/timeline-reference-kb.yaml`

**Routing:**
```
Seed Launch → tasks/plf/create-seed-launch.md
Internal Launch → Continue to Step 3 (this task)
JV Launch → tasks/plf/create-jv-launch.md
Evergreen Launch → tasks/plf/create-evergreen-launch.md
Live Launch → tasks/plf/create-live-launch.md
```

### Step 3: Design Launch Timeline

**Standard Internal Launch (21-28 days):**

| Phase | Days | Focus | Tasks |
|-------|------|-------|-------|
| Pre-Prelaunch | Day 1-7 | Survey, seed curiosity, build anticipation | `create-preprelaunch.md` |
| PLC Sequence | Day 8-18 | Deliver value, build trust, activate triggers | `create-plc-sequence.md` |
| Open Cart | Day 19-23 | Drive sales, handle objections, social proof | `create-open-cart-sequence.md` |
| Cart Close | Day 24-25 | Maximum urgency, final push | (included in open cart) |
| Post-Launch | Day 26-28 | Thank buyers, nurture non-buyers | (included in open cart) |

**Condensed Launch (14 days):**

| Phase | Days | Focus |
|-------|------|-------|
| Pre-Prelaunch | Day 1-3 | Quick survey, teaser |
| PLC Sequence | Day 4-10 | PLCs every 2 days |
| Open Cart | Day 11-14 | Compressed urgency |

### Step 4: Map Mental Triggers Across Phases

**Reference:** `tasks/plf/map-mental-triggers.md`

| Trigger | Pre-Prelaunch | PLC1 | PLC2 | PLC3 | Open Cart | Close |
|---------|--------------|------|------|------|-----------|-------|
| Authority | | X | X | | | |
| Reciprocity | | X | X | X | | |
| Trust | X | X | X | X | X | |
| Anticipation | X | X | X | X | | |
| Likability | X | X | X | | | |
| Events | | | | X | X | X |
| Community | X | X | X | X | X | |
| Social Proof | | | X | | X | X |
| Scarcity | | | | X | X | X |

### Step 5: Define Email Volume

**Email count per phase:**

| Phase | Emails | Frequency |
|-------|--------|-----------|
| Pre-Prelaunch | 3-5 | Every 2-3 days |
| PLC1 | 3 | Announce + 2 reminders |
| PLC2 | 3 | Announce + 2 reminders |
| PLC3 | 3 | Announce + 2 reminders |
| Open Cart | 10-15 | 2-3/day |
| Cart Close (final day) | 3-5 | Escalating urgency |
| Post-Close | 2 | Thank + next steps |

**Total:** 27-37 emails across full launch

### Step 6: Create Launch Calendar

**Output format:**

```yaml
launch_sequence:
  name: "[PRODUCT] Launch"
  type: internal  # seed | internal | jv | evergreen | live
  timeline:
    pre_prelaunch:
      start: "YYYY-MM-DD"
      end: "YYYY-MM-DD"
      task: create-preprelaunch.md
    plc_sequence:
      start: "YYYY-MM-DD"
      end: "YYYY-MM-DD"
      task: create-plc-sequence.md
      plc1_release: "YYYY-MM-DD"
      plc2_release: "YYYY-MM-DD"
      plc3_release: "YYYY-MM-DD"
    open_cart:
      start: "YYYY-MM-DD"
      end: "YYYY-MM-DD"
      task: create-open-cart-sequence.md
    cart_close: "YYYY-MM-DD HH:MM TZ"
  mental_triggers_map: "See Step 4"
  email_count: 30  # estimated total
  launch_stack_task: create-launch-stack.md
  sales_page_task: create-sales-page-plf.md
```

### Step 7: Identify Supporting Assets

**Route to existing tasks:**

| Asset | Task | Required? |
|-------|------|-----------|
| Pre-Prelaunch survey + teasers | `tasks/plf/create-preprelaunch.md` | Yes |
| PLC1, PLC2, PLC3 scripts | `tasks/plf/create-plc-sequence.md` | Yes |
| Launch stack (offer + bonuses) | `tasks/plf/create-launch-stack.md` | Yes |
| Open cart emails | `tasks/plf/create-open-cart-sequence.md` | Yes |
| Sales page | `tasks/plf/create-sales-page-plf.md` | Yes |
| Case studies | `tasks/plf/create-case-study.md` | Recommended |
| Mental trigger mapping | `tasks/plf/map-mental-triggers.md` | Recommended |

### Step 8: Validate Launch Readiness

**Checklist:**
- [ ] Launch type selected and justified
- [ ] Timeline with specific dates
- [ ] Mental triggers mapped across all phases
- [ ] Email volume defined per phase
- [ ] All required tasks identified and routed
- [ ] Supporting assets listed (case studies, proof)
- [ ] Cart open/close dates and times confirmed

**Reference:**
- `checklists/plf/launch-day-execution.md`

---

## Deliverables

1. **Launch Sequence Strategy**
   - Launch type selection with rationale
   - Complete timeline with dates
   - Phase-by-phase breakdown

2. **Launch Calendar**
   - YAML format (see Step 6)
   - All dates, tasks, and routing

3. **Mental Trigger Map**
   - Trigger activation across all phases
   - Gap identification

4. **Task Routing Plan**
   - Which PLF tasks to execute next
   - Execution order and dependencies

---

## Success Criteria

- [ ] Launch type matches audience and assets
- [ ] Timeline is realistic for team capacity
- [ ] All 9 mental triggers activated at least once
- [ ] Scarcity concentrated in final phase (not premature)
- [ ] Every phase has a clear task routing
- [ ] Calendar has specific dates, not "TBD"

---

## Common Mistakes to Avoid

- **Skipping Pre-Prelaunch:** Launching cold without warming the list
- **Compressed PLCs:** Releasing all 3 PLCs in 3 days (minimum 2 days between)
- **Premature scarcity:** Using "limited spots" before cart even opens
- **No post-close plan:** Ignoring non-buyers who may convert next time
- **Too many email gaps:** Going silent for 2+ days during launch

---

## Next Steps

After launch sequence strategy complete:
→ `tasks/plf/create-preprelaunch.md` - Start Pre-Prelaunch phase
→ `tasks/plf/create-plc-sequence.md` - Create PLC content
→ `tasks/plf/create-launch-stack.md` - Build offer stack

---

## References

### Tasks (PLF Suite)
- `tasks/plf/create-preprelaunch.md`
- `tasks/plf/create-plc-sequence.md`
- `tasks/plf/create-open-cart-sequence.md`
- `tasks/plf/create-launch-stack.md`
- `tasks/plf/create-sales-page-plf.md`
- `tasks/plf/create-case-study.md`
- `tasks/plf/map-mental-triggers.md`
- `tasks/plf/create-seed-launch.md`
- `tasks/plf/create-jv-launch.md`
- `tasks/plf/create-evergreen-launch.md`
- `tasks/plf/create-live-launch.md`

### Checklists
- `checklists/plf/launch-day-execution.md`
- `checklists/plf/mental-triggers-activation.md`

### Knowledge Bases
- `data/plf/timeline-reference-kb.yaml`
- `data/plf/timeline-reference-kb.yaml`
- `data/plf/mental-triggers-kb.yaml`
- `data/plf/copy-scripts-extracted.yaml`

---

*Task Version: 1.0*
*Framework: Product Launch Formula - Launch Sequence Strategy*
