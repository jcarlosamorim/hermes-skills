---
version: "1.0"
date: "2026-03-09"
author:
  agent: "squad-chief"
  squad: "copy"
aios: true
project: "opb-corp"
---

# Task: Review Copy — Cross-Review por Segundo Agente

## Task Anatomy

| Campo | Valor |
|-------|-------|
| task_name | review-copy |
| status | active |
| responsible_executor | segundo agente (selecionado pelo Copy Chief) |
| execution_type | autonomous |
| elicit | false |
| mandatory | false — apenas para high-stakes |

## Objetivo

Um segundo copywriter revisa o draft sob sua perspectiva metodológica. Não reescreve — sugere melhorias baseadas em seus frameworks.

## Quando Usar

- `stakes: high` ou `stakes: critical` no briefing
- Copy Chief identifica que o draft precisa de perspectiva complementar
- Projetos com blending (2-3 writers)

## Input

1. Draft de copy (output de `write-copy.md`)
2. Briefing original
3. Diagnostic Report

## Execution Rules

1. Ativar o agente reviewer via `/copy:agents:{agent-name}`
2. Entregar draft + briefing + diagnostic
3. Instruir: "Revise este draft sob sua perspectiva. Não reescreva — aponte gaps e sugira melhorias usando seus frameworks."

## Reviewer Selection Heuristics

| Situação | Reviewer Sugerido | Razão |
|----------|-------------------|-------|
| Sales page precisa de mais prova | claude-hopkins | Specificity + reason-why |
| Headline fraca | eugene-schwartz | Awareness-level headline strategy |
| Copy sem big idea | gary-bencivenga | Big Idea methodology |
| Urgency insuficiente | dan-kennedy | Urgency/deadline frameworks |
| Mechanism não claro | todd-brown | Unique Mechanism discovery |
| Story fraca | john-carlton | Star/Story/Solution |

## Output

```yaml
review:
  reviewer: "{agent-name}"
  overall_assessment: "{strong | needs_work | weak}"
  strengths:
    - "{strength 1}"
    - "{strength 2}"
  gaps:
    - gap: "{description}"
      framework: "{framework name from reviewer's methodology}"
      suggestion: "{specific improvement}"
  priority_fixes:
    - "{fix 1 — highest impact}"
    - "{fix 2}"
```

## Veto Conditions

- NÃO reescrever o copy inteiro — apenas sugerir melhorias
- NÃO sobrepor a voz do writer original — manter o DNA
- NÃO pular para reviewer se stakes = low

## Handoff

→ Writer original aplica fixes → `qa-gate.md`
