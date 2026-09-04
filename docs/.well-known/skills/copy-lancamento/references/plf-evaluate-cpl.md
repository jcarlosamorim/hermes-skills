# Task: Evaluate CPL (Pre-Launch Content)

> **Framework**: Product Launch Formula (Jeff Walker)
> **Agent**: @jeff-walker
> **Phase**: Quality Assurance
> **Output**: Complete CPL evaluation with scores and improvement recommendations

---

## CRITICAL: Load Infrastructure First

**ANTES DE AVALIAR, CARREGAR:**

```yaml
# 1. Execution Checklist (MANDATORY)
execution_checklist: "squads/copy/checklists/plf/cpl-evaluation-execution-checklist.md"

# 2. Production Aid for this CPL (MANDATORY)
production_aids:
  1: "squads/copy/checklists/plf/plc1-complete-production-aid.md"  # ~590 lines
  2: "squads/copy/checklists/plf/plc2-complete-production-aid.md"  # ~827 lines
  3: "squads/copy/checklists/plf/plc3-complete-production-aid.md"  # ~943 lines
  4: "squads/copy/checklists/plf/sales-video-complete-production-aid.md"  # ~1126 lines

# 3. Templates for output
templates:
  report: "squads/copy/templates/plf/cpl-evaluation-report-tmpl.md"
  rubric: "squads/copy/templates/plf/rubric-scores-tmpl.yaml"
  beats: "squads/copy/templates/plf/beat-analysis-tmpl.yaml"

# 4. Workflow reference
workflow: "squads/copy/workflows/wf-evaluate-cpl.yaml"

# 5. Extracted PLF source layers (MANDATORY SUPPORT)
source_layers:
  scripts: "squads/copy/data/plf/copy-scripts-extracted.yaml"
  criteria: "squads/copy/data/plf/plc-criteria-extracted.yaml"
```

**WHY THIS MATTERS:**
- Production Aid tem 10 seções com critérios completos
- Rubric tem 10 dimensões com pesos específicos
- Top 15 Mistakes tem ranking de dano (3x, 2x, 1x)
- Template tem 350 linhas de estrutura
- Extracted source layers preserve Jeff Walker phrasing, PLC sequencing, and criteria language that the aids alone do not fully expose

**Sem carregar = avaliação improvisada = resultado inconsistente.**

---

## Purpose

Avaliar um CPL (Conteúdo de Pré-Lançamento) de forma completa usando os Production Aids do PLF para identificar pontos fortes, gaps e oportunidades de melhoria.

---

## Prerequisites

- [ ] **Production Aid carregado COMPLETO** (ver seção acima)
- [ ] **Execution Checklist carregado**
- [ ] Arquivo de transcrição do CPL disponível
- [ ] Conhecimento de qual número é o CPL (1, 2, 3 ou 4)
- [ ] Contexto do lançamento (produto, criador, avatar)

---

## Inputs Required

```yaml
cpl_file: "" # Caminho completo do arquivo
cpl_number: "" # 1, 2, 3 ou 4
product_name: "" # Nome do produto sendo lançado
creator_name: "" # Nome do expert/criador
avatar_description: "" # Breve descrição do público-alvo
```

---

## Workflow

### FASE 1: Leitura Completa do CPL

**CRÍTICO: Ler o arquivo COMPLETO antes de analisar.**

Se o arquivo for grande:
1. Ler em partes de 500 linhas
2. Processar cada parte
3. Consolidar entendimento antes de avaliar

```
Parte 1: Linhas 1-500
Parte 2: Linhas 501-1000
Parte 3: Linhas 1001-1500
... continuar até o fim
```

### FASE 2: Identificação de Estrutura

**Para CPL1 (The Opportunity):**
```
[ ] HOOK - Primeiros 30 segundos
    - Onde começa: linha ___
    - O que fala: ___
    - Score (1-10): ___

[ ] AUTORIDADE/ORIGIN STORY - 2-3 minutos
    - Onde começa: linha ___
    - História contada: ___
    - Vulnerabilidade presente? ___
    - Score (1-10): ___

[ ] OPORTUNIDADE REVELADA - 5-7 minutos
    - Onde começa: linha ___
    - Qual oportunidade: ___
    - Clareza (1-10): ___

[ ] PRIMEIRO ENSINO - 7-10 minutos
    - Onde começa: linha ___
    - O que ensina: ___
    - Acionável? ___
    - Score (1-10): ___

[ ] ANTECIPAÇÃO CPL2 - 2-3 minutos
    - Onde começa: linha ___
    - O que teasea: ___
    - Cria curiosidade? ___
    - Score (1-10): ___

[ ] CTA FINAL
    - Qual CTA: ___
    - Claro? ___
```

**Para CPL2 (The Transformation):**
```
[ ] RECAP CPL1 - 1-2 minutos
[ ] CASE STUDY PRINCIPAL - 5-7 minutos
[ ] CASES ADICIONAIS (2-3) - 5 minutos
[ ] ENSINO PROFUNDO - 7-10 minutos
[ ] TRATAMENTO DE OBJEÇÕES - 3-5 minutos
[ ] ANTECIPAÇÃO CPL3 - 2-3 minutos
[ ] CTA FINAL
```

**Para CPL3 (The Ownership):**
```
[ ] RECAP DA JORNADA - 2-3 minutos
[ ] VISÃO DE OWNERSHIP - 5-7 minutos
[ ] DAY-IN-THE-LIFE - 3-5 minutos
[ ] ENSINO FINAL - 10-15 minutos
[ ] BRIDGE PARA OFERTA - 5 minutos
[ ] PREVIEW DO PRODUTO - 3-5 minutos
[ ] SETUP ESCASSEZ - 2-3 minutos
[ ] CTA E FECHAMENTO
```

**Para CPL4 (Pivot to Offer - Challenge Format):**
```
[ ] RECAP DE TUDO APRENDIDO
[ ] POSICIONAMENTO DO PRODUTO
[ ] ENSINO FINAL (vendas/implementação)
[ ] MECANISMO DE CONVERSÃO (quiz, prova)
[ ] ANTECIPAÇÃO ABERTURA CARRINHO
[ ] SETUP DE ESCASSEZ
[ ] CTA FINAL
```

### FASE 3: Avaliação dos 9 Mental Triggers

Para cada trigger, documentar:
1. Está presente? (Sim/Não/Parcial)
2. ONDE exatamente aparece (citar linha e trecho)
3. Intensidade (1-10)
4. Como poderia ser mais forte

```
TRIGGER 1: AUTHORITY
- Presente: ___
- Onde: "___" (linha ___)
- Intensidade: ___/10
- Para melhorar: ___

TRIGGER 2: RECIPROCITY
- Presente: ___
- Onde: "___" (linha ___)
- Intensidade: ___/10
- Para melhorar: ___

TRIGGER 3: TRUST
- Presente: ___
- Onde: "___" (linha ___)
- Intensidade: ___/10
- Para melhorar: ___

TRIGGER 4: ANTICIPATION
- Presente: ___
- Onde: "___" (linha ___)
- Intensidade: ___/10
- Para melhorar: ___

TRIGGER 5: LIKABILITY
- Presente: ___
- Onde: "___" (linha ___)
- Intensidade: ___/10
- Para melhorar: ___

TRIGGER 6: EVENTS
- Presente: ___
- Onde: "___" (linha ___)
- Intensidade: ___/10
- Para melhorar: ___

TRIGGER 7: COMMUNITY
- Presente: ___
- Onde: "___" (linha ___)
- Intensidade: ___/10
- Para melhorar: ___

TRIGGER 8: SOCIAL PROOF
- Presente: ___
- Onde: "___" (linha ___)
- Intensidade: ___/10
- Para melhorar: ___

TRIGGER 9: SCARCITY
- Presente: ___
- Onde: "___" (linha ___)
- Intensidade: ___/10
- Para melhorar: ___
```

### FASE 4: Extração de Frameworks

Listar todos os:
- Métodos com nome (ex: Método RETINA, Plano F)
- Acrônimos explicados
- Frameworks com passos numerados
- Analogias memoráveis
- Frases de efeito repetidas

### FASE 5: Análise de Storytelling

```
ORIGIN STORY:
- Presente? ___
- Momento de vulnerabilidade? ___
- Virada/transformação clara? ___
- Conexão emocional? ___
- Citação marcante: "___"

CASE STUDIES:
- Quantidade: ___
- Específicos (nome, cidade, números)? ___
- Relatáveis com avatar? ___
- Before/after claro? ___
- Melhor case: ___

ANALOGIAS:
- Quais usadas: ___
- Mais efetiva: ___
```

### FASE 6: Identificação de Gaps

**Gaps de Estrutura:**
- [ ] ___

**Gaps de Triggers:**
- [ ] ___

**Gaps de Conteúdo:**
- [ ] ___

**Gaps de Transição:**
- [ ] ___

**Objeções Não Tratadas:**
- [ ] ___

### FASE 7: Cálculo de Score

```
ESTRUTURA (25 pontos)
- Hook: ___/5
- Desenvolvimento: ___/10
- Transição: ___/5
- CTA: ___/5
SUBTOTAL: ___/25

MENTAL TRIGGERS (45 pontos - 5 por trigger)
- Authority: ___/5
- Reciprocity: ___/5
- Trust: ___/5
- Anticipation: ___/5
- Likability: ___/5
- Events: ___/5
- Community: ___/5
- Social Proof: ___/5
- Scarcity: ___/5
SUBTOTAL: ___/45

QUALIDADE DE CONTEÚDO (15 pontos)
- Valor entregue: ___/5
- Clareza: ___/5
- Aplicabilidade: ___/5
SUBTOTAL: ___/15

STORYTELLING (10 pontos)
- Origin story: ___/3
- Cases: ___/4
- Analogias: ___/3
SUBTOTAL: ___/10

TRANSIÇÃO (5 pontos)
- Antecipação próximo CPL: ___/5
SUBTOTAL: ___/5

SCORE TOTAL: ___/100
```

**Classificação:**
- 90-100: Excelente - Pronto para lançamento
- 80-89: Bom - Pequenos ajustes necessários
- 70-79: Adequado - Melhorias recomendadas
- 60-69: Precisa trabalho - Gaps significativos
- <60: Requer revisão completa

---

## Output Format

**FORMATO: Texto corrido para WhatsApp (SEM MARKDOWN)**

```
AVALIAÇÃO CPL[X] - [NOME DO PRODUTO]
Criador: [NOME]
Score: XX/100 - [CLASSIFICAÇÃO]

---

RESUMO EXECUTIVO
[5 linhas resumindo a avaliação geral]

---

ESTRUTURA (XX/25)
[O que está bom]
[O que falta]

---

MENTAL TRIGGERS (XX/45)

Authority (X/5): [status]
[onde aparece ou o que falta]

Reciprocity (X/5): [status]
[onde aparece ou o que falta]

Trust (X/5): [status]
[onde aparece ou o que falta]

Anticipation (X/5): [status]
[onde aparece ou o que falta]

Likability (X/5): [status]
[onde aparece ou o que falta]

Events (X/5): [status]
[onde aparece ou o que falta]

Community (X/5): [status]
[onde aparece ou o que falta]

Social Proof (X/5): [status]
[onde aparece ou o que falta]

Scarcity (X/5): [status]
[onde aparece ou o que falta]

---

FRAMEWORKS IDENTIFICADOS
[lista]

---

STORYTELLING (XX/10)
[análise]

---

TOP 5 PONTOS FORTES
1. [ponto] - "[citação]"
2. [ponto] - "[citação]"
3. [ponto] - "[citação]"
4. [ponto] - "[citação]"
5. [ponto] - "[citação]"

---

TOP 10 PONTOS DE MELHORIA

1. [GAP]
Como melhorar: [sugestão específica]

2. [GAP]
Como melhorar: [sugestão específica]

[... até 10]

---

PRIORIDADES (o que fazer primeiro)
1. [ação prioritária]
2. [ação prioritária]
3. [ação prioritária]
```

---

## References

### Critical Files (Load First)
- `checklists/plf/cpl-evaluation-execution-checklist.md` — **MANDATORY before evaluating**
- `workflows/wf-evaluate-cpl.yaml` — Complete workflow with 6 phases

### Production Aids (Load Based on CPL#)
- `checklists/plf/plc1-complete-production-aid.md` — 590 lines, 10 sections
- `checklists/plf/plc2-complete-production-aid.md` — 827 lines, 10 sections
- `checklists/plf/plc3-complete-production-aid.md` — 943 lines, 10 sections
- `checklists/plf/sales-video-complete-production-aid.md` — 1126 lines

### Output Templates
- `templates/plf/cpl-evaluation-report-tmpl.md` — 350 lines
- `templates/plf/rubric-scores-tmpl.yaml` — 10 dimensions with weights
- `templates/plf/beat-analysis-tmpl.yaml` — Beat-by-beat structure

### Quick Checklists (For Reference)
- `checklists/plf/cpl1-opportunity-checklist.md`
- `checklists/plf/cpl2-transformation-checklist.md`
- `checklists/plf/cpl3-ownership-checklist.md`
- `checklists/plf/cpl4-enrollment-checklist.md`

### Related Tasks
- `tasks/plf/diagnose-failed-launch.md`
- `tasks/plf/map-mental-triggers.md`
- `tasks/plf/create-plc-sequence.md`

---

*Task Version: 2.0*
*Updated: 2026-02-01 — Added infrastructure loading requirements*
*Framework: Product Launch Formula - CPL Evaluation*
