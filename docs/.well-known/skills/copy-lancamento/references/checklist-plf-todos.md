# Checklists: plf

<!-- cpl-evaluation-execution-checklist.md -->
# CPL Evaluation Execution Checklist

> **Purpose**: Garantir que toda avaliação de CPL use a infraestrutura completa do PLF
> **Framework**: Product Launch Formula (Jeff Walker)
> **Version**: 1.0
> **Created**: 2026-02-01

---

## BEFORE Starting Evaluation

### 1. Load Production Aid COMPLETELY

**CRITICAL: Carregar o Production Aid completo ANTES de avaliar.**

| CPL # | Production Aid File | Lines |
|-------|---------------------|-------|
| 1 | `checklists/plf/plc1-complete-production-aid.md` | ~590 |
| 2 | `checklists/plf/plc2-complete-production-aid.md` | ~827 |
| 3 | `checklists/plf/plc3-complete-production-aid.md` | ~943 |
| 4 | `checklists/plf/sales-video-complete-production-aid.md` | ~1126 |

- [ ] Li o Production Aid COMPLETO para este CPL number
- [ ] Identifiquei as 10 seções principais
- [ ] Extraí os critérios específicos de avaliação

### 2. Load Launch Context

- [ ] Nome do produto
- [ ] Nome do criador/expert
- [ ] Avatar/público-alvo
- [ ] Contexto do lançamento (se disponível)

### 3. Prepare Transcript

- [ ] Arquivo de transcrição disponível
- [ ] Estratégia de chunking definida (500 linhas / 50 overlap)

---

## DURING Beat Analysis (Phase 2)

### Expected Beats for Each CPL

**CPL1 (The Opportunity):**
1. Opening (30-90 segundos)
2. Show the Opportunity (2-4 min)
3. Position Yourself (2-3 min)
4. Teach (3-5 min)
5. Raise Objections (1-3 min)
6. Foreshadow CPL2 (30-60 sec)
7. Call to Action (30-60 sec)

**CPL2 (The Transformation):**
1. Opening + Recap CPL1
2. Case Studies (transformations)
3. Teaching (deeper)
4. Objection Handling
5. Foreshadow CPL3
6. CTA

**CPL3 (The Ownership):**
1. Recap Journey
2. Ownership Vision
3. Day-in-the-Life
4. Final Teaching
5. Bridge to Offer
6. Product Preview
7. Scarcity Setup
8. CTA + Close

**For EACH beat, document:**
- [ ] Start line number
- [ ] End line number
- [ ] Evidence quote (citação direta)
- [ ] Copy framework used (Strategy A, B, or C)
- [ ] Score (1-5)
- [ ] Gaps identified

---

## DURING Rubric Scoring (Phase 3)

### 10 Dimensions with Weights (PLC1)

| # | Dimension | Weight | Critical? |
|---|-----------|--------|-----------|
| 1 | Empathy | 1.0 | No |
| 2 | Opportunity clarity | 1.2 | **Yes** |
| 3 | Positioning | 1.0 | No |
| 4 | Teaching value | 1.2 | **Yes** |
| 5 | Objection handling | 0.8 | No |
| 6 | Anticipation | 1.0 | **Yes** |
| 7 | CTA | 0.8 | No |
| 8 | Zero pitch | 1.5 | **Yes** |
| 9 | Emotional arc | 1.0 | No |
| 10 | Rewatchability | 0.5 | No |

**For EACH dimension:**
- [ ] Read definition of 1 (Weak), 3 (Solid), 5 (Exceptional) from Production Aid
- [ ] Find evidence in transcript
- [ ] Assign score (1-5, no decimals)
- [ ] Document justification with quote
- [ ] Identify gap to next level

### Score Calculation

```
weighted_score = Σ(dimension_score × weight) / Σ(weights)
overall_score = weighted_score × 2  # Convert to 0-10 scale
```

---

## DURING Mistake Detection (Phase 4)

### Top 15 Mistakes (Ranked by Damage)

**Critical (#1-5): Damage Multiplier 3x**

| # | Mistake | Detection Pattern |
|---|---------|-------------------|
| 1 | Opening with credentials instead of empathy | First 30 sec mentions "I am...", titles, without pain acknowledgment |
| 2 | Teaching too little | No actionable content, just teasers |
| 3 | Selling or hinting at product | ANY mention of product, price, offer, or "buy" |
| 4 | Abstract transformation | "Better life", "success" without specifics |
| 5 | Skipping empathy layer in positioning | Credentials without "I was where you are" |

**Significant (#6-10): Damage Multiplier 2x**

| # | Mistake | Detection Pattern |
|---|---------|-------------------|
| 6 | No foreshadow of CPL2 | No mention of "next video" or tease |
| 7 | No call to action for comments | No engagement request at end |
| 8 | Ignoring objections | No "you might be thinking..." language |
| 9 | Trying to cover everything | CPL too long, no strategic restraint |
| 10 | Over-produced, under-authentic | Scripted feel, no personality |

**Minor (#11-15): Damage Multiplier 1x**

| # | Mistake | Detection Pattern |
|---|---------|-------------------|
| 11 | Teaching theory instead of actionable | Concepts without "do this today" |
| 12 | Making transformation unachievable | Story too extraordinary |
| 13 | Too long on positioning | >20% of total time on "who I am" |
| 14 | Flat emotional pacing | Same energy throughout |
| 15 | Ending weakly | Abrupt or low-energy close |

**For EACH mistake:**
- [ ] Check presence in transcript
- [ ] Classify: DETECTED / AVOIDED / UNCLEAR
- [ ] Document evidence (quote + line number)
- [ ] Apply damage multiplier

### Damage Score Calculation

```
total_damage = Σ(detected_mistakes × damage_multiplier)
penalty = total_damage / max_possible_damage
```

---

## DURING Trigger Analysis (Phase 5)

### 9 Triggers by Beat

| Beat | Expected Triggers |
|------|-------------------|
| Opening | Likability, Trust |
| Opportunity | Hope, Desire |
| Positioning | Authority, Likability, Trust |
| Teaching | Authority, Reciprocity |
| Objections | Trust, Likability |
| Foreshadow | Anticipation |
| CTA | Community, Commitment |

### Primary Triggers for CPL1

| Trigger | Critical? | Expected Intensity |
|---------|-----------|-------------------|
| Authority | Yes | 4-5 |
| Reciprocity | Yes | 4-5 |
| Anticipation | Yes | 4-5 |
| Likability | Yes | 3-4 |
| Trust | No | 3-4 |

**For EACH trigger:**
- [ ] Verify activation (Yes/No/Partial)
- [ ] Document mechanism used
- [ ] Rate intensity (1-5)
- [ ] Note evidence quote

---

## FOR Report Generation (Phase 6)

### Use Template

- [ ] Using `templates/plf/cpl-evaluation-report-tmpl.md`
- [ ] All handlebars variables populated

### Score Formula (MUST USE)

```yaml
# Score composition:
beat_score = average(beat_scores) × 2  # 0-10 scale
rubric_score = weighted_rubric_score   # 0-10 scale
trigger_score = (activated_triggers / expected_triggers) × 10

# Final calculation:
base_score = (beat_score × 0.3) + (rubric_score × 0.4) + (trigger_score × 0.3)
final_score = base_score - mistake_penalty

# Clamp to 0-10
overall_score = max(0, min(10, final_score))
```

### Status Thresholds

| Score | Status |
|-------|--------|
| >= 8.5 | LAUNCH WINNING |
| >= 7.0 | PASS |
| >= 5.0 | NEEDS WORK |
| < 5.0 | FAIL |

### Required Report Sections

- [ ] Executive Summary with scores
- [ ] Beat-by-Beat Analysis with evidence
- [ ] Rubric Scores with justification
- [ ] Mistakes Detected with damage
- [ ] Trigger Analysis with intensity
- [ ] Prioritized Recommendations
- [ ] Rewrite Suggestions (for beats < 3)

---

## VETO Conditions (Stop Evaluation)

### Fatal (Auto-FAIL)
- [ ] Product/offer mentioned in CPL 1, 2, or 3
- [ ] No teaching content in CPL that requires it

### Critical (Flag + Require Attention)
- [ ] Any rubric dimension scores 1
- [ ] Top 5 mistake detected
- [ ] Anticipation trigger missing in CPL 1 or 2

### Warning (Document + Continue)
- [ ] Overall score < 7.0
- [ ] More than 5 mistakes detected
- [ ] More than 2 beats absent

---

## Post-Evaluation Verification

- [ ] 6+ beats identified with evidence (citações)
- [ ] 10 dimensions pontuadas with justification
- [ ] All 15 mistakes checked
- [ ] 9 triggers mapped by beat
- [ ] Score calculated with formula (not estimated)
- [ ] Report follows template structure

---

## Quick Reference: Files to Load

```yaml
# For CPL 1 evaluation:
production_aid: "squads/copy/checklists/plf/plc1-complete-production-aid.md"
rubric_template: "squads/copy/templates/plf/rubric-scores-tmpl.yaml"
beat_template: "squads/copy/templates/plf/beat-analysis-tmpl.yaml"
report_template: "squads/copy/templates/plf/cpl-evaluation-report-tmpl.md"
workflow: "squads/copy/workflows/wf-evaluate-cpl.yaml"

# Chunking for large transcripts:
chunk_size: 500
overlap: 50
```

---

*Checklist Version: 1.0*
*Created: 2026-02-01*
*Framework: Product Launch Formula - CPL Evaluation*
*Purpose: Ensure complete infrastructure usage*


---

<!-- cpl1-opportunity-checklist.md -->
# CPL1 - The Opportunity Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Source**: Launch (Original + Updated 2021 Edition)
> **Theme**: WHY - Por que o prospect deve prestar atenção?

---

## Core Purpose

Grab your prospects' attention and draw them in. Answer:
- Why should your prospect care?
- Why should they spend their precious time paying attention to you?
- What can you do for them?

---

## ESTRUTURA OBRIGATÓRIA

### 1. Mostrar a Oportunidade
- [ ] Mostra/conta como a vida do prospect vai mudar
- [ ] Pinta o quadro da transformação disponível
- [ ] Conecta com dores, desejos, frustrações e sonhos do avatar
- [ ] Responde claramente: "O que isso pode fazer por mim?"

### 2. Posicionar Autoridade
- [ ] Estabelece credibilidade de forma natural
- [ ] Menciona credenciais DENTRO do contexto de ajudar (não como auto-promoção vazia)
- [ ] Usa a própria história como prova (origin story)
- [ ] Mostra que entende a dor do prospect porque já viveu algo similar

### 3. Ensinar (CRÍTICO)
- [ ] Entrega valor REAL (não apenas teaser)
- [ ] Vai além de falar da oportunidade
- [ ] Ensina algo que as pessoas podem usar imediatamente
- [ ] Conteúdo acionável (5-10 minutos de ensino prático)

### 4. Levantar Objeções
- [ ] Menciona as principais objeções do avatar
- [ ] Responde algumas objeções diretamente
- [ ] Promete responder outras objeções nos próximos vídeos
- [ ] Não ignora ou evita as objeções óbvias

### 5. Antecipar CPL2 (Foreshadow)
- [ ] Avisa que tem outro vídeo/conteúdo vindo
- [ ] Revela um pouco do que vai ensinar no CPL2
- [ ] Cria curiosidade genuína para o próximo conteúdo
- [ ] Usa linguagem como "Wait until you see..." ou "No próximo vídeo..."

### 6. Call to Action
- [ ] Pede comentário no blog/post/vídeo
- [ ] Pede para compartilhar com alguém que precisa
- [ ] Convida para fazer uma pergunta
- [ ] Inicia a "Launch Conversation"

---

## MENTAL TRIGGERS QUE DEVEM ESTAR PRESENTES

| Trigger | Como Verificar | Score |
|---------|----------------|-------|
| **Authority** | Posiciona-se como alguém que vale a pena ouvir? | ___/5 |
| **Reciprocity** | Dá conteúdo valioso gratuitamente? | ___/5 |
| **Anticipation** | Cria expectativa para o CPL2? | ___/5 |
| **Community** | Engaja com comentários/perguntas? | ___/5 |
| **Likability** | Mostra personalidade e se conecta? | ___/5 |

---

## O QUE NÃO PODE TER (Red Flags)

- [ ] **NÃO vende ou faz pitch de nada**
- [ ] **NÃO dá dica de mensagem de vendas ou oferta**
- [ ] **NÃO usa linguagem corporativa/formal demais**
- [ ] **NÃO economiza no ensino - deve dar valor real**
- [ ] **NÃO assume que o prospect sabe quem você é**
- [ ] **NÃO se gaba sem contexto de ajudar**

---

## DURAÇÃO RECOMENDADA

| Formato | Duração |
|---------|---------|
| Vídeo editado | 15-25 minutos |
| Live/Broadcast | ~40 minutos |
| Segmento de ensino | 5-10 minutos (dentro do total) |

---

## EXEMPLO DO LIVRO: Barry Friedman

**Contexto:** Entertainer ensinando outros entertainers a conseguir shows bem pagos.

**O que ele fez:**
1. Construiu rapport mostrando que entendia a dor (ele viveu isso)
2. Mostrou que tinha os mesmos sonhos e medos que eles
3. Pintou a oportunidade de construir um negócio sério com as skills existentes
4. Contou sua história: o orientador do colégio disse que ele ia fracassar, depois ele se apresentou no Tonight Show

**Mensagem-chave:**
> "Sou muito parecido com você. Encontrei uma paixão por malabarismo quando era criança mas me disseram que não poderia viver disso. Meu orientador do colégio disse que eu seria falido e sem-teto. Provei que ele estava errado."

**Resultado:** Gerou engajamento enorme e estabeleceu autoridade.

---

## SCORING

### Elementos Obrigatórios (30 pontos)
| Elemento | Presente | Score |
|----------|----------|-------|
| Mostra oportunidade | [ ] | ___/5 |
| Posiciona autoridade | [ ] | ___/5 |
| Ensina valor real | [ ] | ___/5 |
| Levanta objeções | [ ] | ___/5 |
| Antecipa CPL2 | [ ] | ___/5 |
| Call to Action | [ ] | ___/5 |
**Subtotal Estrutura:** ___/30

### Mental Triggers (25 pontos)
| Trigger | Score |
|---------|-------|
| Authority | ___/5 |
| Reciprocity | ___/5 |
| Anticipation | ___/5 |
| Community | ___/5 |
| Likability | ___/5 |
**Subtotal Triggers:** ___/25

### Qualidade de Conteúdo (20 pontos)
| Critério | Score |
|----------|-------|
| Valor acionável entregue | ___/5 |
| Clareza da oportunidade | ___/5 |
| Conexão emocional | ___/5 |
| Linguagem do avatar | ___/5 |
**Subtotal Conteúdo:** ___/20

### Red Flags (25 pontos - começa com 25, perde por violação)
| Red Flag | Presente? | Penalidade |
|----------|-----------|------------|
| Vende/faz pitch | [ ] | -10 |
| Linguagem corporativa | [ ] | -5 |
| Não ensina nada útil | [ ] | -5 |
| Auto-promoção vazia | [ ] | -5 |
**Subtotal Red Flags:** ___/25

---

## SCORE FINAL CPL1

| Categoria | Score |
|-----------|-------|
| Estrutura | ___/30 |
| Triggers | ___/25 |
| Conteúdo | ___/20 |
| Red Flags | ___/25 |
| **TOTAL** | **___/100** |

### Classificação
- 90-100: Excelente - CPL1 pronto
- 80-89: Bom - Pequenos ajustes
- 70-79: Adequado - Melhorias necessárias
- 60-69: Precisa trabalho - Gaps significativos
- <60: Requer revisão completa

---

## CITAÇÃO-CHAVE DE JEFF WALKER

> "I want to emphasize that part about VALUABLE content—this isn't just about taking a sales pitch and stretching it out over a couple of weeks. That's not going to grab and hold anyone's attention. Through this process you deliver real value to your prospects."

---

*Checklist Version: 2.0*
*Source: Launch (Jeff Walker) - Original + Updated 2021 Edition*
*Framework: Product Launch Formula*


---

<!-- cpl2-transformation-checklist.md -->
# CPL2 - The Transformation Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Source**: Launch (Original + Updated 2021 Edition)
> **Theme**: WHAT - O que é essa transformação e como muda a vida do prospect?

---

## Core Purpose

Show WHAT this transformation or opportunity is and how it's going to change or transform your prospects' lives. This is more about teaching.

**Objetivo-chave:**
> "If PLC #2 can get your prospect to SEE THEMSELVES having the transformation that you promised in PLC #1, then you've done your job." - Jeff Walker

---

## ESTRUTURA OBRIGATÓRIA

### 1. Agradecer e Recapitular
- [ ] Agradece pelos comentários e perguntas do CPL1
- [ ] Reconhece o engajamento da audiência
- [ ] Faz transição natural do CPL1

### 2. Recap da Oportunidade
- [ ] Rapidamente recapitula a oportunidade do CPL1
- [ ] **NÃO assume que o prospect viu o CPL1**
- [ ] Não gasta tanto tempo quanto no CPL1, mas não pula
- [ ] Lembra: "Sua vida pode mudar assim..."

### 3. Recap do Posicionamento
- [ ] Lembra quem você é e por que devem ouvir você
- [ ] Faz rapidamente - não demora muito
- [ ] Reforça credenciais relevantes

### 4. Case Study OU Ensino Real (CRÍTICO)
- [ ] Apresenta Case Study detalhado OU
- [ ] Ensina algo REAL que podem usar imediatamente
- [ ] Entrega valor substancial (não teaser)
- [ ] Faz o prospect SE VER tendo a transformação
- [ ] Ensina pelo menos uma coisa "cool" que podem aplicar rápido

### 5. Esmagar Objeções
- [ ] Fala sobre as 2-3 principais objeções
- [ ] Responde as objeções diretamente
- [ ] Ataca as objeções à transformação prometida no CPL1
- [ ] Usa provas/exemplos para derrubar objeções

### 6. Antecipar CPL3 (Foreshadow)
- [ ] Avisa que tem outro vídeo vindo em breve
- [ ] Conta um pouco sobre o que vai ensinar no CPL3
- [ ] Cria antecipação genuína
- [ ] "Wait until you see what I'm going to show you..."

### 7. Call to Action
- [ ] Pede comentário no blog/post/vídeo
- [ ] Encoraja perguntas
- [ ] Mantém a "Launch Conversation" ativa

---

## MENTAL TRIGGERS QUE DEVEM ESTAR PRESENTES

| Trigger | Como Verificar | Score |
|---------|----------------|-------|
| **Authority** | Demonstra expertise através do ensino? | ___/5 |
| **Reciprocity** | Dá valor massivo que cria obrigação? | ___/5 |
| **Trust** | Constrói relacionamento através de interação repetida? | ___/5 |
| **Social Proof** | Mostra outros tendo sucesso (cases, comentários)? | ___/5 |
| **Anticipation** | Cria expectativa para o CPL3? | ___/5 |

---

## O QUE NÃO PODE TER (Red Flags)

- [ ] **NÃO vende ou faz pitch de nada**
- [ ] **NÃO dá dica de mensagem de vendas ou oferta**
- [ ] **NÃO assume que assistiram ao CPL1**
- [ ] **NÃO economiza no ensino - deve dar valor acionável**
- [ ] **NÃO se preocupa em "dar demais" de graça**
- [ ] **NÃO usa linguagem corporativa**

---

## QUALIDADE DO CASE STUDY (se usado)

| Critério | Case 1 | Case 2 | Case 3 |
|----------|--------|--------|--------|
| Similar ao avatar | [ ] | [ ] | [ ] |
| Resultados específicos | [ ] | [ ] | [ ] |
| Before/after claro | [ ] | [ ] | [ ] |
| Quote/depoimento incluído | [ ] | [ ] | [ ] |
| Timeline mencionado | [ ] | [ ] | [ ] |
| Prospect pode se ver nele | [ ] | [ ] | [ ] |

---

## DURAÇÃO RECOMENDADA

| Formato | Duração |
|---------|---------|
| Vídeo editado | 15-25 minutos |
| Segmento de ensino | 5-10 minutos mínimo |
| Exemplo Jeff Walker | ~18 minutos ensinando Seed Launch |

---

## EXEMPLO DO LIVRO: Barry Friedman

**O que ele fez:**
1. Revisitou a dor potencial de fracassar no negócio
2. Focou pesadamente no ENSINO
3. Deu princípios fundamentais de marketing para entertainers
4. Nenhuma dica de venda - só conteúdo sólido e excelente

**Mensagem-chave:**
> "E se tudo isso desmoronar e seus pais estavam certos? E se você não conseguir viver como entertainer? Se você quer ter sucesso nesse negócio, precisa tratá-lo como um negócio. Você passou centenas de horas trabalhando na sua arte, mas isso é só parte da equação..."

---

## EXEMPLO DO LIVRO: Jeff Walker PLF

**O que ele fez:**
- Ensinou o conceito COMPLETO do Seed Launch em ~18 minutos
- Pessoas fizeram Seed Launches com sucesso só com esse vídeo gratuito
- Não guardou nada - deu o método completo

---

## ERRO COMUM A EVITAR

> "The mistake I see far more often is NOT giving away enough high-quality content." - Jeff Walker

**O medo:** "Se eu der demais, ninguém vai comprar."
**A realidade:** Quanto mais valor você dá, mais reciprocidade cria. Pessoas que têm sucesso com seu conteúdo gratuito se tornam os melhores compradores.

---

## SCORING

### Elementos Obrigatórios (35 pontos)
| Elemento | Presente | Score |
|----------|----------|-------|
| Agradece e recapitula | [ ] | ___/5 |
| Recap da oportunidade | [ ] | ___/5 |
| Recap do posicionamento | [ ] | ___/5 |
| Case study OU ensino real | [ ] | ___/5 |
| Esmaga objeções | [ ] | ___/5 |
| Antecipa CPL3 | [ ] | ___/5 |
| Call to Action | [ ] | ___/5 |
**Subtotal Estrutura:** ___/35

### Mental Triggers (25 pontos)
| Trigger | Score |
|---------|-------|
| Authority | ___/5 |
| Reciprocity | ___/5 |
| Trust | ___/5 |
| Social Proof | ___/5 |
| Anticipation | ___/5 |
**Subtotal Triggers:** ___/25

### Qualidade de Conteúdo (20 pontos)
| Critério | Score |
|----------|-------|
| Valor acionável entregue | ___/5 |
| Prospect pode se ver na transformação | ___/5 |
| Cases são relatáveis | ___/5 |
| Objeções bem respondidas | ___/5 |
**Subtotal Conteúdo:** ___/20

### Red Flags (20 pontos - começa com 20, perde por violação)
| Red Flag | Presente? | Penalidade |
|----------|-----------|------------|
| Vende/faz pitch | [ ] | -10 |
| Assume que viram CPL1 | [ ] | -5 |
| Ensino fraco/teaser | [ ] | -5 |
**Subtotal Red Flags:** ___/20

---

## SCORE FINAL CPL2

| Categoria | Score |
|-----------|-------|
| Estrutura | ___/35 |
| Triggers | ___/25 |
| Conteúdo | ___/20 |
| Red Flags | ___/20 |
| **TOTAL** | **___/100** |

### Classificação
- 90-100: Excelente - CPL2 pronto
- 80-89: Bom - Pequenos ajustes
- 70-79: Adequado - Melhorias necessárias
- 60-69: Precisa trabalho - Gaps significativos
- <60: Requer revisão completa

---

## CITAÇÃO-CHAVE DE JEFF WALKER

> "If PLC #2 can get your prospect to see themselves having the transformation that you promised in PLC #1, then you've done your job."

---

*Checklist Version: 2.0*
*Source: Launch (Jeff Walker) - Original + Updated 2021 Edition*
*Framework: Product Launch Formula*


---

<!-- cpl3-ownership-checklist.md -->
# CPL3 - The Ownership Experience Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Source**: Launch (Original + Updated 2021 Edition)
> **Theme**: HOW - Como eles vão ter essa transformação?

---

## Core Purpose

Start to answer the "HOW" question. You've shown the potential transformation but they still don't see HOW they're really going to have that change. PLC #3 is about them taking OWNERSHIP of that future change.

**Elemento Crítico:**
> "This is where you make the PIVOT to the sale. By the end of PLC #3, you will have started to show them the answer (buy your product) and prepare them for the upcoming offer." - Jeff Walker

---

## ESTRUTURA OBRIGATÓRIA

### 1. Agradecer e Criar Excitação
- [ ] Agradece pelos comentários e perguntas do CPL2
- [ ] Mostra excitação genuína
- [ ] Menciona como todos estão animados
- [ ] "Vocês estão ficando empolgados? Eu também!"

### 2. Recap Rápido
- [ ] Rapidamente recapitula a oportunidade
- [ ] Rapidamente relembra seu posicionamento
- [ ] **NÃO assume que viram os vídeos anteriores**
- [ ] Move rápido - não demora muito aqui

### 3. Case Study Curto (Opcional)
- [ ] Se tiver, apresenta um case study breve
- [ ] Reforça que a transformação é real
- [ ] Mostra mais uma prova de que funciona

### 4. Responder Perguntas/Objeções Principais
- [ ] Responde as perguntas mais frequentes
- [ ] Endereça objeções mesmo se já respondeu antes
- [ ] As pessoas fazem as mesmas perguntas de formas diferentes
- [ ] Finaliza as últimas dúvidas

### 5. Explicar a Visão Grande (Big Picture)
- [ ] Dá um passo atrás e olha o quadro completo
- [ ] Mostra o que é REALMENTE possível
- [ ] Qual a transformação máxima se comprarem?
- [ ] Projeta o futuro transformado do prospect
- [ ] Usa Future Pacing - "Imagine daqui 6 meses..."

### 6. PIVOT PARA A OFERTA (CRÍTICO)
- [ ] **Timing: Últimos 10% do conteúdo (ou 25% na versão original)**
- [ ] Menciona que no próximo vídeo terá uma oferta
- [ ] Cria "soft landing" - não vai de amigo para vendedor abruptamente
- [ ] Prepara o prospect para o que está por vir
- [ ] "Se você está pronto para levar isso pro próximo nível..."

### 7. Seed Scarcity (Plantar Escassez)
- [ ] Menciona que a oferta será limitada
- [ ] **NÃO exagera - a oferta ainda não foi revelada**
- [ ] "Fique de olho no próximo email porque vai ser limitado"
- [ ] Escassez sutil, não pesada

### 8. Call to Action
- [ ] Pede comentário final
- [ ] Mantém engajamento até a abertura do carrinho
- [ ] "Me conta nos comentários: você está pronto?"

---

## O PIVOT - ELEMENTO MAIS IMPORTANTE

### O que é o Pivot:
> "By now prospects have fallen in love with you because you've given them huge value. It's time to start preparing them for the offer - that's the 'soft landing.'"

### Como fazer:
- [ ] Não vai de "melhor amigo" para "vendedor de carros usados"
- [ ] Transição natural e suave
- [ ] "Eu tenho algo especial para vocês..."
- [ ] "No próximo vídeo, vou fazer uma oferta para quem está pronto..."
- [ ] Mantém o tom de ajuda, não de venda

### Timing:
- **Edição Atualizada (2021):** Últimos 10% do vídeo
- **Edição Original:** Últimos 25% do vídeo

---

## ERRO MAIS COMUM (CRÍTICO)

> "Making the pivot to the sale in the final piece of Prelaunch Content is critical, and leaving out that pivot is a mistake a lot of people make." - Jeff Walker

**Por que acontece:** Pessoas ficam tão envolvidas em entregar conteúdo incrível que não querem "estragar o clima" falando de venda.

**Consequência:** Prospects não estão preparados para a oferta e conversões caem drasticamente.

---

## MENTAL TRIGGERS QUE DEVEM ESTAR PRESENTES

| Trigger | Como Verificar | Score |
|---------|----------------|-------|
| **Authority** | Continua demonstrando expertise? | ___/5 |
| **Reciprocity** | Culminação de todo valor entregue? | ___/5 |
| **Trust** | Construído através de toda a sequência? | ___/5 |
| **Anticipation** | Cria expectativa para o lançamento? | ___/5 |
| **Scarcity** | Planta escassez de forma sutil? | ___/5 |
| **Events/Ritual** | Data do lançamento vira um evento? | ___/5 |
| **Community** | Launch Conversation forte? | ___/5 |

---

## O QUE NÃO PODE TER (Red Flags)

- [ ] **NÃO pula o pivot para a venda** (erro mais grave)
- [ ] **NÃO faz transição abrupta de amigo para vendedor**
- [ ] **NÃO exagera na escassez antes de mostrar a oferta**
- [ ] **NÃO esquece de construir excitação/tensão**
- [ ] **NÃO assume que lembram dos CPLs anteriores**

---

## DURAÇÃO RECOMENDADA

| Formato | Duração |
|---------|---------|
| Vídeo total | 15-30 minutos |
| Pivot timing | Últimos 10% (ou 25%) |

---

## EXEMPLO DO LIVRO: Barry Friedman

**O que ele fez:**
1. Revisou a história do lançamento
2. Intensificou ainda mais o ensino
3. Analisou websites de vários entertainers, mostrou erros
4. Mostrou como esses erros podiam ser facilmente corrigidos
5. **ENTÃO fez o pivot:** Falou sobre guiar pessoalmente 15 pessoas pelo seu Showbiz Blueprint

**Momento do Pivot:**
> "He talked about how he was going to personally guide 15 people through his Showbiz Blueprint, which was the exact promotional system that helped land the highest-paying gigs in the industry, including Johnny Carson and The White House. This was the first mention of an upcoming product, the first hint that there was a sale coming."

**Resultado:**
> "Barry didn't want to put the pivot in - he was loving the teaching and didn't want to mess with the good vibes. But he followed PLF and included it. The launch succeeded."

---

## SCORING

### Elementos Obrigatórios (40 pontos)
| Elemento | Presente | Score |
|----------|----------|-------|
| Agradece e cria excitação | [ ] | ___/5 |
| Recap rápido | [ ] | ___/5 |
| Case study (se aplicável) | [ ] | ___/5 |
| Responde perguntas/objeções | [ ] | ___/5 |
| Explica visão grande | [ ] | ___/5 |
| **PIVOT PARA OFERTA** | [ ] | ___/10 |
| Seed scarcity | [ ] | ___/5 |
**Subtotal Estrutura:** ___/40

### Mental Triggers (35 pontos)
| Trigger | Score |
|---------|-------|
| Authority | ___/5 |
| Reciprocity | ___/5 |
| Trust | ___/5 |
| Anticipation | ___/5 |
| Scarcity | ___/5 |
| Events/Ritual | ___/5 |
| Community | ___/5 |
**Subtotal Triggers:** ___/35

### Qualidade do Pivot (15 pontos)
| Critério | Score |
|----------|-------|
| Timing correto (últimos 10-25%) | ___/5 |
| Transição suave (soft landing) | ___/5 |
| Prepara sem vender pesado | ___/5 |
**Subtotal Pivot:** ___/15

### Red Flags (10 pontos - começa com 10, perde por violação)
| Red Flag | Presente? | Penalidade |
|----------|-----------|------------|
| Pula o pivot | [ ] | -10 (fatal) |
| Transição abrupta | [ ] | -5 |
| Escassez exagerada | [ ] | -3 |
**Subtotal Red Flags:** ___/10

---

## SCORE FINAL CPL3

| Categoria | Score |
|-----------|-------|
| Estrutura | ___/40 |
| Triggers | ___/35 |
| Qualidade do Pivot | ___/15 |
| Red Flags | ___/10 |
| **TOTAL** | **___/100** |

### Classificação
- 90-100: Excelente - CPL3 pronto
- 80-89: Bom - Pequenos ajustes
- 70-79: Adequado - Melhorias necessárias
- 60-69: Precisa trabalho - Gaps significativos
- <60: Requer revisão completa

---

## CITAÇÃO-CHAVE DE JEFF WALKER

> "Making the pivot to the sale in the final piece of Prelaunch Content is critical, and leaving out that pivot is a mistake a lot of people make."

---

*Checklist Version: 2.0*
*Source: Launch (Jeff Walker) - Original + Updated 2021 Edition*
*Framework: Product Launch Formula*


---

<!-- cpl4-enrollment-checklist.md -->
# CPL4 - Enrollment / Open Cart Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Source**: Launch (Original + Updated 2021 Edition)
> **Theme**: BUY/ENROLL - Convide-os a se inscrever no futuro deles

---

## Nota sobre CPL4

O Jeff Walker tradicionalmente usa 3 PLCs + Open Cart. Porém, muitos lançamentos modernos (especialmente no formato "Desafio") usam 4-5 CPLs antes do carrinho abrir.

Este checklist cobre:
- **Formato Tradicional:** Sales Video no Open Cart
- **Formato Desafio:** CPL4 como "Bridge to Offer"

---

## Core Purpose

> "By enrollment, you're asking prospects to enroll in their future - to take the action that will give them the transformation."

Se você seguiu a fórmula até aqui:
- PLC conectou com as pessoas da sua lista
- Mental triggers criaram autoridade, prova social, comunidade
- Escassez foi plantada
- Prospects sabem que uma oferta está vindo
- CPL3 teve pivot forte preparando para a oferta

---

## FORMATO TRADICIONAL: OPEN CART / SALES VIDEO

### Elementos Obrigatórios

#### 1. Abertura Forte
- [ ] Recapitula a jornada dos últimos dias
- [ ] Agradece pelo engajamento
- [ ] Cria excitação: "Chegou o momento!"
- [ ] Reforça a transformação prometida

#### 2. Apresentação da Oferta
- [ ] Nome do produto/programa
- [ ] O que está incluído (módulos, bônus, etc.)
- [ ] Como funciona a entrega
- [ ] Quanto tempo leva para ver resultados

#### 3. Prova e Validação
- [ ] Cases de sucesso finais
- [ ] Depoimentos de compradores anteriores
- [ ] Resultados específicos com números
- [ ] "Pessoas como você conseguiram..."

#### 4. Resposta a Objeções Finais
- [ ] "E se não funcionar para mim?"
- [ ] "E se eu não tiver tempo?"
- [ ] "E se for muito caro?"
- [ ] Apresenta garantia como resposta

#### 5. Garantia
- [ ] Garantia clara e específica
- [ ] Remove o risco da decisão
- [ ] "Se não funcionar, você não paga nada"

#### 6. Preço e Condições
- [ ] Apresenta o preço
- [ ] Ancora valor antes de mostrar preço
- [ ] Opções de pagamento (à vista, parcelado)
- [ ] Bônus por ação rápida (se houver)

#### 7. Escassez Real
- [ ] Data/hora que o carrinho fecha
- [ ] Por que é limitado (razão real)
- [ ] O que acontece se perder
- [ ] **NUNCA escassez falsa**

#### 8. Call to Action Claro
- [ ] Link/botão para compra
- [ ] Instrução clara: "Clique aqui para garantir sua vaga"
- [ ] Urgência: "As vagas estão limitadas"

---

## FORMATO DESAFIO: CPL4 COMO BRIDGE

Quando o CPL4 NÃO é o vídeo de vendas, mas sim uma aula de "ponte" antes do Open Cart:

### Elementos Obrigatórios

#### 1. Recap Completo da Jornada
- [ ] Resume o que aprenderam no CPL1, CPL2, CPL3
- [ ] Mostra o progresso que fizeram
- [ ] "Olha o quanto você já evoluiu!"

#### 2. Ensino Final (Geralmente sobre Vendas/Implementação)
- [ ] Ensina algo que os prepare para usar o conhecimento
- [ ] Muitas vezes é sobre "como vender" ou "como aplicar"
- [ ] Completa o quadro de conhecimento

#### 3. Estabelecer o Gap
- [ ] Mostra onde eles estão agora
- [ ] Mostra onde querem chegar
- [ ] Identifica o que falta para cruzar o gap
- [ ] "Você tem o conhecimento, mas precisa de X para ir mais rápido"

#### 4. Posicionar o Produto como Ponte
- [ ] O produto preenche o gap
- [ ] É o próximo passo lógico
- [ ] Não é "compre meu produto" - é "se você quer acelerar..."

#### 5. Mecanismo de Engajamento (Quiz, Prova, etc.)
- [ ] Se usar quiz/prova: explica as regras
- [ ] Se usar sorteio: explica como participar
- [ ] Gamifica a experiência
- [ ] Aumenta comprometimento

#### 6. Setup de Escassez
- [ ] Quando o carrinho abre
- [ ] Quando o carrinho fecha
- [ ] Por que é limitado
- [ ] Bônus que vão embora

#### 7. Antecipação Final
- [ ] Cria excitação máxima para a abertura
- [ ] "Amanhã/Segunda eu vou abrir as portas..."
- [ ] "Você precisa estar lá às X horas"

#### 8. Call to Action
- [ ] Pede para marcar na agenda
- [ ] Pede para ativar notificações
- [ ] "Fique de olho no seu email"

---

## MENTAL TRIGGERS NO CPL4/OPEN CART

| Trigger | Como Verificar | Score |
|---------|----------------|-------|
| **Scarcity** | Escassez REAL com deadline? | ___/5 |
| **Events** | Lançamento é um EVENTO? | ___/5 |
| **Social Proof** | Mostra outros comprando/tendo sucesso? | ___/5 |
| **Authority** | Reforça credibilidade uma última vez? | ___/5 |
| **Anticipation** | Atingiu o pico de antecipação? | ___/5 |
| **Community** | "Junte-se a nós", senso de pertencimento? | ___/5 |
| **Trust** | Garantia forte, transparência? | ___/5 |

---

## O QUE NÃO PODE TER (Red Flags)

- [ ] **NÃO usa escassez falsa**
- [ ] **NÃO promete resultados impossíveis**
- [ ] **NÃO esquece de incluir garantia**
- [ ] **NÃO deixa o preço sem âncora de valor**
- [ ] **NÃO faz transição abrupta do ensino para venda**
- [ ] **NÃO assume que todos viram os CPLs anteriores**

---

## PADRÃO DE VENDAS ESPERADO

| Fase | % das Vendas |
|------|-------------|
| Dia 1 (abertura) | 25% |
| Dias 2-4 (meio) | 25% |
| Último dia | 50% |

> "25% on day one, 50% on the last day" - Jeff Walker

---

## SCORING - FORMATO TRADICIONAL (SALES VIDEO)

### Elementos da Oferta (40 pontos)
| Elemento | Score |
|----------|-------|
| Abertura forte | ___/5 |
| Apresentação da oferta | ___/5 |
| Prova e validação | ___/5 |
| Objeções respondidas | ___/5 |
| Garantia clara | ___/5 |
| Preço bem apresentado | ___/5 |
| Escassez REAL | ___/5 |
| CTA claro | ___/5 |
**Subtotal Oferta:** ___/40

### Mental Triggers (35 pontos)
| Trigger | Score |
|---------|-------|
| Scarcity | ___/5 |
| Events | ___/5 |
| Social Proof | ___/5 |
| Authority | ___/5 |
| Anticipation | ___/5 |
| Community | ___/5 |
| Trust | ___/5 |
**Subtotal Triggers:** ___/35

### Red Flags (25 pontos - começa com 25)
| Red Flag | Penalidade |
|----------|------------|
| Escassez falsa | -15 |
| Sem garantia | -5 |
| Preço sem âncora | -5 |
**Subtotal:** ___/25

---

## SCORING - FORMATO DESAFIO (BRIDGE CPL4)

### Elementos de Bridge (40 pontos)
| Elemento | Score |
|----------|-------|
| Recap da jornada | ___/5 |
| Ensino final | ___/5 |
| Gap estabelecido | ___/5 |
| Produto como ponte | ___/5 |
| Mecanismo de engajamento | ___/5 |
| Setup de escassez | ___/5 |
| Antecipação final | ___/5 |
| CTA claro | ___/5 |
**Subtotal Bridge:** ___/40

### Mental Triggers (35 pontos)
| Trigger | Score |
|---------|-------|
| Scarcity (seeded) | ___/5 |
| Events | ___/5 |
| Social Proof | ___/5 |
| Authority | ___/5 |
| Anticipation | ___/5 |
| Community | ___/5 |
| Trust | ___/5 |
**Subtotal Triggers:** ___/35

### Red Flags (25 pontos - começa com 25)
| Red Flag | Penalidade |
|----------|------------|
| Vende pesado sem soft landing | -10 |
| Não estabelece gap | -5 |
| Escassez forçada | -5 |
| Não cria antecipação | -5 |
**Subtotal:** ___/25

---

## SCORE FINAL CPL4

| Categoria | Score |
|-----------|-------|
| Elementos | ___/40 |
| Triggers | ___/35 |
| Red Flags | ___/25 |
| **TOTAL** | **___/100** |

### Classificação
- 90-100: Excelente - Pronto para converter
- 80-89: Bom - Pequenos ajustes
- 70-79: Adequado - Melhorias necessárias
- 60-69: Precisa trabalho - Conversão será comprometida
- <60: Requer revisão completa

---

## CITAÇÃO-CHAVE DE JEFF WALKER

> "By enrollment, you're asking prospects to enroll in their future - to take the action that will give them the transformation."

---

*Checklist Version: 2.0*
*Source: Launch (Jeff Walker) - Original + Updated 2021 Edition*
*Framework: Product Launch Formula*


---

<!-- evergreen-setup.md -->
# Evergreen Launch Setup Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Setup evergreen/automated launch sequence
> **Prerequisite**: At least one successful live launch

---

## Pre-Evergreen Validation

### Live Launch Completed
- [ ] Live launch done successfully
- [ ] Conversion rate proven: ____%
- [ ] Revenue generated: R$______
- [ ] Content validated (PLCs work)
- [ ] Objections documented and addressed

### Jeff's Recommendation
> "I recommend doing live launches first before evergreen.
> You need to know your content works and converts."

- [ ] This advice followed: [ ] Yes

---

## Content Adaptation

### PLC Video Editing
| PLC | Action | Status |
|-----|--------|--------|
| PLC1 | Remove live references | [ ] |
| PLC1 | Remove date mentions | [ ] |
| PLC1 | Edit for evergreen | [ ] |
| PLC2 | Remove live references | [ ] |
| PLC2 | Remove date mentions | [ ] |
| PLC2 | Edit for evergreen | [ ] |
| PLC3 | Remove live references | [ ] |
| PLC3 | Remove date mentions | [ ] |
| PLC3 | Edit for evergreen | [ ] |

### Content Updates Needed
- [ ] "This Thursday" → "In the next video"
- [ ] Specific dates removed
- [ ] "Join us live" → Generic CTA
- [ ] Comments on engagement adjusted
- [ ] Sales page dates removed

### New Recordings Needed
- [ ] New intros (if referencing time)
- [ ] New outros (if referencing time)
- [ ] Additional FAQ content
- [ ] Updated testimonials

---

## Email Automation Setup

### Sequence Structure
| Day | Email | Trigger |
|-----|-------|---------|
| 0 | Welcome/Opt-in confirm | Opt-in |
| 1 | PLC1 announcement | Time-based |
| 2 | PLC1 reminder | Time-based |
| 3 | PLC2 announcement | Time-based |
| 4 | PLC2 reminder | Time-based |
| 5 | PLC3 announcement | Time-based |
| 6 | PLC3 reminder | Time-based |
| 7 | Cart open #1 | Time-based |
| 7 | Cart open #2 | Time-based |
| 8 | Case study | Time-based |
| 9 | FAQ | Time-based |
| 10 | Pre-close | Time-based |
| 11 | Final day #1 | Time-based |
| 11 | Final day #2 | Time-based |
| 11 | Final day #3 | Time-based |
| 12 | Cart closed | Time-based |

### Email Adaptations
- [ ] All emails adapted for evergreen
- [ ] Dates → "Today", "Tomorrow", "In X days"
- [ ] Live references removed
- [ ] Urgency maintained but generic
- [ ] Links updated for tracking

---

## Deadline/Scarcity Tech

### Deadline System
- [ ] Platform selected: ______
- [ ] Deadline Funnel / Thrivecart / Custom
- [ ] Account setup complete
- [ ] Integration tested

### How It Works
- [ ] Each subscriber gets unique deadline
- [ ] Countdown timer personalized
- [ ] Cart actually closes for that user
- [ ] No way to bypass (real scarcity)

### Deadline Configuration
- [ ] Cart open duration: ______ days
- [ ] Timer display locations: ______
- [ ] Redirect after close: ______
- [ ] Email triggers on close: [ ] Yes / [ ] No

### Testing
- [ ] Test subscriber through full sequence
- [ ] Deadline timer accurate
- [ ] Cart closes at right time
- [ ] Post-close page works

---

## Funnel Pages Setup

### Opt-in Page
- [ ] URL: ______
- [ ] Tracking pixel: ______
- [ ] Thank you redirect: ______
- [ ] Mobile optimized: [ ] Yes

### PLC Pages
| Page | URL | Status |
|------|-----|--------|
| PLC1 | | [ ] Live |
| PLC2 | | [ ] Live |
| PLC3 | | [ ] Live |

### Sales Page
- [ ] URL: ______
- [ ] Deadline timer integrated: [ ] Yes
- [ ] Evergreen language: [ ] Yes
- [ ] Mobile optimized: [ ] Yes

### Checkout
- [ ] URL: ______
- [ ] Payment processing: [ ] Working
- [ ] Order confirmation: [ ] Working
- [ ] Access delivery: [ ] Working

### Post-Deadline Page
- [ ] URL: ______
- [ ] Message: "Cart closed, join waitlist"
- [ ] Waitlist capture: [ ] Yes

---

## Traffic Strategy

### Traffic Sources
| Source | Budget | Notes |
|--------|--------|-------|
| Facebook/Meta | R$/day | |
| Google | R$/day | |
| YouTube | R$/day | |
| Email (existing list) | N/A | |
| Content marketing | N/A | |

### Opt-in Ads
- [ ] Ad creative ready
- [ ] Targeting defined
- [ ] Landing page tested
- [ ] Tracking configured

### Retargeting Setup
- [ ] Pixel on all funnel pages
- [ ] Audiences created:
  - [ ] Opt-in visitors (no opt-in)
  - [ ] PLC viewers
  - [ ] Sales page visitors (no buy)
  - [ ] Buyers (exclude)

### Traffic Testing Plan
- [ ] Start budget: R$____/day
- [ ] Test duration: ______ days
- [ ] Success metrics: CPL < R$____
- [ ] Scale if: ______

---

## Automation Testing

### Full Sequence Test
- [ ] Create test email
- [ ] Opt-in to funnel
- [ ] Receive all emails on schedule
- [ ] PLCs accessible
- [ ] Deadline timer works
- [ ] Cart opens correctly
- [ ] Cart closes correctly
- [ ] Purchase works
- [ ] Post-purchase works

### Edge Cases
- [ ] What if email bounces?
- [ ] What if deadline passes without action?
- [ ] What if multiple opt-ins?
- [ ] What if refund requested?

---

## Tracking & Analytics

### Key Metrics to Track
- [ ] Opt-in conversion rate
- [ ] PLC view rates
- [ ] Email open/click rates
- [ ] Sales page conversion
- [ ] Cart abandonment
- [ ] Purchase conversion
- [ ] Cost per lead (CPL)
- [ ] Cost per acquisition (CPA)
- [ ] Return on ad spend (ROAS)

### Dashboard Setup
- [ ] Analytics platform: ______
- [ ] Conversion tracking: ______
- [ ] Automated reporting: [ ] Yes / [ ] No

### Benchmark Targets
| Metric | Target |
|--------|--------|
| Opt-in rate | ___% |
| Email open rate | ___% |
| Sales page conversion | ___% |
| Overall funnel conversion | ___% |
| Max CPL | R$___ |
| Target CPA | R$___ |
| Target ROAS | ___x |

---

## Ongoing Management

### Daily Tasks
- [ ] Check ad performance
- [ ] Monitor CPL/CPA
- [ ] Review support tickets

### Weekly Tasks
- [ ] Analyze funnel metrics
- [ ] Optimize underperforming areas
- [ ] Update ads if needed
- [ ] Review testimonials/feedback

### Monthly Tasks
- [ ] Full funnel review
- [ ] A/B test planning
- [ ] Content freshness check
- [ ] P&L analysis

---

## Optimization Plan

### A/B Tests to Run
| Test | Element | Status |
|------|---------|--------|
| | Opt-in headline | [ ] |
| | Email subjects | [ ] |
| | Sales page headline | [ ] |
| | CTA buttons | [ ] |
| | Pricing display | [ ] |

### Iteration Schedule
- [ ] Week 1-2: Launch and gather data
- [ ] Week 3-4: First optimizations
- [ ] Month 2: Major A/B tests
- [ ] Month 3+: Ongoing refinement

---

## Financial Projections

### Break-Even Analysis
| Item | Value |
|------|-------|
| Product price | R$ |
| Cost per lead | R$ |
| Conversion rate | % |
| Leads to break-even | |
| Ad spend to break-even | R$ |

### Monthly Projections
| Scenario | Leads | Sales | Revenue | Ad Spend | Profit |
|----------|-------|-------|---------|----------|--------|
| Conservative | | | R$ | R$ | R$ |
| Target | | | R$ | R$ | R$ |
| Optimistic | | | R$ | R$ | R$ |

---

## Launch Checklist

### Pre-Launch
- [ ] All content adapted
- [ ] All pages live
- [ ] All automation tested
- [ ] Tracking working
- [ ] Team briefed

### Soft Launch (Test)
- [ ] Send 10-20 test subscribers
- [ ] Monitor full sequence
- [ ] Fix any issues
- [ ] Validate conversion

### Full Launch
- [ ] Turn on traffic
- [ ] Start small and scale
- [ ] Monitor closely first week
- [ ] Optimize continuously

---

## Evergreen Launch Approval

**Live launch proven:** [ ] Yes / [ ] No
**Content adapted:** [ ] Yes / [ ] No
**Automation tested:** [ ] Yes / [ ] No
**Deadline tech working:** [ ] Yes / [ ] No
**Traffic strategy ready:** [ ] Yes / [ ] No
**Tracking configured:** [ ] Yes / [ ] No

**PROCEED WITH EVERGREEN:** [ ] Yes / [ ] No

**Date:** ______
**Signed:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Evergreen*


---

<!-- jv-launch-partner.md -->
# JV Launch Partner Management Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Manage JV/Affiliate partners for launch
> **Prerequisite**: Successful Internal Launch first

---

## Pre-JV Validation

### Internal Launch Completed
- [ ] Internal launch done
- [ ] Conversion rate proven: ____%
- [ ] EPC calculated: $______
- [ ] Offer validated
- [ ] Tech proven to work

### Jeff's Rule
> "Don't test with your partners' lists.
> Do an Internal Launch first to prove your offer converts."

- [ ] This rule followed: [ ] Yes

---

## Partner Recruitment

### Ideal Partner Profile
- [ ] List size: ______ minimum
- [ ] Audience alignment: ______
- [ ] Relationship quality: ______
- [ ] Promotion history: ______

### Target Partners List
| Partner | List Size | Relationship | Status | Notes |
|---------|-----------|-------------|--------|-------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

### Outreach Status
- [ ] Target list: ______ partners
- [ ] Outreach sent: ______
- [ ] Responses received: ______
- [ ] Confirmed partners: ______

---

## Commission Structure

### Standard Commission
- [ ] Commission rate: ____% (typically 40-50%)
- [ ] Cookie duration: ______ days
- [ ] Second tier: [ ] Yes / [ ] No
- [ ] If yes, rate: ____%

### Payment Terms
- [ ] Payment method: ______
- [ ] Payment timing: ______ days after launch
- [ ] Refund handling: ______
- [ ] Minimum payout: R$______

---

## Prize/Incentive Structure

### Leaderboard Prizes
| Place | Prize | Value |
|-------|-------|-------|
| 1st | | R$ |
| 2nd | | R$ |
| 3rd | | R$ |
| 4th-5th | | R$ |
| 6th-10th | | R$ |

### Bonus Incentives
- [ ] Early bird bonus: ______
- [ ] Sales milestone bonus: ______
- [ ] Content bonus: ______

### Total Prize Pool
- [ ] Total budget: R$______
- [ ] ROI justified: [ ] Yes

---

## Partner Resources

### Affiliate Portal
- [ ] Portal URL: ______
- [ ] Login instructions ready
- [ ] Link tracking working
- [ ] Dashboard accessible

### Swipe Copy Provided
- [ ] Pre-prelaunch email (1)
- [ ] PLC announcement emails (3)
- [ ] Open cart emails (5+)
- [ ] Social media swipes
- [ ] Quick wins swipes

### Creative Assets
- [ ] Banner ads (sizes: _______)
- [ ] Social images
- [ ] Video assets (if any)
- [ ] Logo files
- [ ] Headshot/photos

### Product Information
- [ ] Product description
- [ ] FAQ document
- [ ] Objection handling guide
- [ ] Target audience description
- [ ] Key selling points

---

## Partner Communication Schedule

### Pre-Launch
| Date | Communication | Status |
|------|--------------|--------|
| -4 weeks | Initial recruitment | [ ] |
| -3 weeks | Follow-up outreach | [ ] |
| -2 weeks | Partner welcome + assets | [ ] |
| -1 week | Final prep + calendar | [ ] |
| -3 days | Reminder + hype | [ ] |

### During Launch
| Date | Communication | Status |
|------|--------------|--------|
| Day 1 | Cart open + leaderboard | [ ] |
| Day 2 | Update + encouragement | [ ] |
| Day 3 | Mid-launch stats | [ ] |
| Day 4 | Final push reminder | [ ] |
| Day 5 | Close cart + results | [ ] |

### Post-Launch
| Date | Communication | Status |
|------|--------------|--------|
| +1 day | Thank you + results | [ ] |
| +1 week | Final stats + payment info | [ ] |
| +30 days | Payment confirmation | [ ] |

---

## Coordination Calendar

### Pre-Launch Dates
- [ ] Swipes delivered: ______
- [ ] Prelaunch starts: ______
- [ ] Partners begin promotion: ______

### Launch Dates
- [ ] PLC1: ______
- [ ] PLC2: ______
- [ ] PLC3: ______
- [ ] Cart Open: ______
- [ ] Cart Close: ______

### Promotion Windows
- [ ] Partners can promote PLCs: [ ] Yes / [ ] No
- [ ] Pre-cart promotion allowed: [ ] Yes / [ ] No
- [ ] Direct to sales page: [ ] Yes / [ ] No

---

## Tracking & Reporting

### Tracking Setup
- [ ] Affiliate tracking system: ______
- [ ] Unique links generated
- [ ] Conversion tracking working
- [ ] Sales attribution accurate

### Reporting Schedule
- [ ] Daily leaderboard updates
- [ ] Real-time dashboard access
- [ ] EPC updates
- [ ] Final report timing: ______

### Key Metrics to Track
| Metric | Target | Actual |
|--------|--------|--------|
| Total partner traffic | | |
| Total partner sales | | |
| EPC | $______ | |
| Conversion rate | ___% | |
| Total partner revenue | R$______ | |
| Total commissions | R$______ | |

---

## Partner Support

### Support Channels
- [ ] Email: ______
- [ ] WhatsApp/Telegram: ______
- [ ] Response time: ______ hours

### Common Questions Prepared
- [ ] Commission questions
- [ ] Tracking questions
- [ ] Asset questions
- [ ] Promotional guidelines

### Escalation
- [ ] Primary contact: ______
- [ ] Backup contact: ______
- [ ] Emergency contact: ______

---

## Compliance & Guidelines

### Promotional Guidelines
- [ ] Approved claims only
- [ ] No false scarcity
- [ ] Income claims policy
- [ ] Testimonial rules
- [ ] Social media disclosure

### Prohibited Practices
- [ ] List documented
- [ ] Communicated to partners
- [ ] Monitoring plan

---

## Post-Launch Actions

### Results Communication
- [ ] Final results email sent
- [ ] Leaderboard published
- [ ] Thank you to all partners

### Payment Processing
- [ ] Sales verified
- [ ] Refunds processed
- [ ] Net commissions calculated
- [ ] Payments scheduled
- [ ] Tax documents (if needed)

### Relationship Maintenance
- [ ] Personal thank you to top partners
- [ ] Feedback collected
- [ ] Future launch interest noted
- [ ] Relationship documented

---

## JV Launch Success Metrics

### Financial Goals
- [ ] Gross revenue goal: R$______
- [ ] Net revenue (after commission): R$______
- [ ] Partner commission budget: R$______
- [ ] Prize budget: R$______
- [ ] Break-even point: R$______

### Results
- [ ] Gross revenue achieved: R$______
- [ ] Total commissions paid: R$______
- [ ] Total prizes paid: R$______
- [ ] Net profit: R$______
- [ ] List growth: ______

---

## JV Launch Approval

**Internal Launch completed:** [ ] Yes / [ ] No
**Partner recruitment complete:** [ ] Yes / [ ] No
**Resources prepared:** [ ] Yes / [ ] No
**Tracking working:** [ ] Yes / [ ] No
**Support ready:** [ ] Yes / [ ] No

**PROCEED WITH JV LAUNCH:** [ ] Yes / [ ] No

**Date:** ______
**Signed:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - JV Launch*


---

<!-- launch-day-execution.md -->
# Launch Day Execution Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Day-of-launch execution guide
> **Goal**: Flawless execution, maximum sales

---

## Pre-Launch Day (Night Before)

### Final Checks
- [ ] Sales page live and tested
- [ ] Checkout working (test purchase)
- [ ] All emails loaded and scheduled
- [ ] Links verified in all emails
- [ ] Social posts scheduled
- [ ] Team briefed
- [ ] Support ready
- [ ] Backup plans confirmed

### Personal Prep
- [ ] Good night's sleep
- [ ] Alarm set for early morning
- [ ] Coffee/water ready
- [ ] Workspace clean
- [ ] Phone charged

---

## Launch Day Timeline

### 7:00 AM - Pre-Launch
- [ ] Wake up and prepare
- [ ] Check all systems online
- [ ] Review day's schedule
- [ ] Mental preparation

### 7:30 AM - Final Systems Check
- [ ] Email platform online
- [ ] Sales page loading
- [ ] Checkout processing
- [ ] Analytics tracking
- [ ] Support channels open

### 8:00 AM - Email #1 Goes Out
- [ ] Confirm email sent
- [ ] Verify delivery (spot check)
- [ ] Monitor open rates
- [ ] Check for bounces
- [ ] Respond to any tech issues

### 8:30 AM - Social Media Push
- [ ] Post announcement
- [ ] Stories/reels live
- [ ] Engage with comments
- [ ] Monitor mentions

### 9:00-10:00 AM - Monitor First Hour
- [ ] Track first sales
- [ ] Monitor support inbox
- [ ] Answer urgent questions
- [ ] Check for tech issues
- [ ] Document any problems

### 10:00 AM - First Check-In
| Metric | Target | Actual |
|--------|--------|--------|
| Email opens | ___% | |
| Clicks | ___% | |
| Sales | ___ | |
| Support tickets | | |

### 12:00 PM - Midday Review
- [ ] Sales on track?
- [ ] Tech issues resolved?
- [ ] Support caught up?
- [ ] Energy sustained?

### 2:00 PM - Email #2 Goes Out
- [ ] Confirm email sent
- [ ] Verify delivery
- [ ] Monitor response
- [ ] Update social proof if applicable

### 3:00 PM - Afternoon Check
| Metric | Target | Actual |
|--------|--------|--------|
| Email #2 opens | ___% | |
| Cumulative sales | ___ | |
| Revenue | R$___ | |

### 5:00 PM - Support Review
- [ ] All tickets addressed
- [ ] FAQ additions needed?
- [ ] Common questions noted
- [ ] Team status check

### 7:00 PM - Evening Push
- [ ] Social media update
- [ ] Personal engagement
- [ ] Prep for Email #3

### 8:00 PM - Email #3 Goes Out
- [ ] Confirm email sent
- [ ] Monitor response
- [ ] Behind-the-scenes content
- [ ] Build momentum

### 10:00 PM - End of Day Review
| Metric | Target | Actual |
|--------|--------|--------|
| Total sales Day 1 | ___ | |
| Total revenue Day 1 | R$___ | |
| % of launch goal | ___% | |
| Email performance | | |

### Before Bed
- [ ] Day 1 stats documented
- [ ] Day 2 emails confirmed scheduled
- [ ] Any issues escalated
- [ ] Team debrief (brief)
- [ ] Rest and recharge

---

## Real-Time Monitoring Dashboard

### Key Metrics to Watch
| Metric | Check Every | Alert If |
|--------|-------------|----------|
| Sales | 30 min | 0 for 2+ hours |
| Email opens | 1 hour | Below 20% |
| Checkout errors | 30 min | Any errors |
| Support tickets | 1 hour | Overwhelming |
| Page load | 2 hours | Slow/down |

### Tracking Sheet
| Time | Sales | Revenue | Notes |
|------|-------|---------|-------|
| 9 AM | | | |
| 10 AM | | | |
| 11 AM | | | |
| 12 PM | | | |
| 1 PM | | | |
| 2 PM | | | |
| 3 PM | | | |
| 4 PM | | | |
| 5 PM | | | |
| 6 PM | | | |
| 7 PM | | | |
| 8 PM | | | |
| 9 PM | | | |
| 10 PM | | | |

---

## Emergency Protocols

### If Sales Page Goes Down
1. [ ] Check hosting status
2. [ ] Clear cache/CDN
3. [ ] Activate backup page
4. [ ] Email list about temporary issue
5. [ ] Post on social about fix

### If Email Doesn't Deliver
1. [ ] Check ESP status
2. [ ] Verify send completed
3. [ ] Resend if needed
4. [ ] Use backup ESP if available
5. [ ] Social media as backup channel

### If Checkout Fails
1. [ ] Test checkout yourself
2. [ ] Check payment processor
3. [ ] Activate backup processor
4. [ ] Manual order process
5. [ ] Communicate issue + solution

### If Overwhelmed with Support
1. [ ] Prioritize buyers
2. [ ] Use canned responses
3. [ ] Post FAQ publicly
4. [ ] Set expectations on response time
5. [ ] Call in backup support

---

## Support Management

### Priority Levels
| Priority | Type | Response Time |
|----------|------|---------------|
| P1 | Payment issues | < 1 hour |
| P2 | Access problems | < 2 hours |
| P3 | General questions | < 4 hours |
| P4 | Feature requests | End of day |

### Canned Responses Ready
- [ ] "How do I buy?"
- [ ] "Is there a payment plan?"
- [ ] "When does it close?"
- [ ] "What's included?"
- [ ] "Technical issue response"

---

## Social Media Management

### Platforms to Monitor
- [ ] Instagram
- [ ] Facebook
- [ ] LinkedIn
- [ ] Twitter/X
- [ ] YouTube (if applicable)

### Engagement Tasks
- [ ] Respond to comments
- [ ] Answer DMs
- [ ] Share buyer excitement
- [ ] Post updates
- [ ] Stories throughout day

---

## Team Communication

### Roles Assigned
| Role | Person | Contact |
|------|--------|---------|
| Launch Lead | | |
| Tech Support | | |
| Customer Support | | |
| Social Media | | |
| Emergency Contact | | |

### Check-in Schedule
- [ ] 10 AM brief update
- [ ] 2 PM team sync
- [ ] 6 PM status report
- [ ] 10 PM day recap

### Communication Channel
- [ ] Primary: ______
- [ ] Backup: ______

---

## Day 1 Success Criteria

### Minimum Targets
- [ ] Email #1 open rate > 35%
- [ ] Sales page visits > ___
- [ ] Day 1 sales > ___ (25% of goal)
- [ ] Support response < 4 hours
- [ ] Zero major tech issues

### Actual Results
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Email opens | | | [ ] Hit |
| Page visits | | | [ ] Hit |
| Sales | | | [ ] Hit |
| Revenue | R$___ | | [ ] Hit |

---

## End of Day Debrief

### What Worked
-
-
-

### What Needs Improvement
-
-
-

### Actions for Day 2
- [ ]
- [ ]
- [ ]

### Team Recognition
-

---

## Day 1 Sign-Off

**All emails sent:** [ ] Yes
**Sales on track:** [ ] Yes / [ ] Behind / [ ] Ahead
**Tech stable:** [ ] Yes
**Support managed:** [ ] Yes
**Team status:** [ ] Good

**Day 1 Status:** [ ] SUCCESS / [ ] NEEDS ATTENTION

**Notes:**

**Signed:** ______
**Time:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Launch Day*


---

<!-- launch-stack-completeness.md -->
# Launch Stack Completeness Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Verify complete offer stack before Open Cart
> **Use**: Final check before revealing offer

---

## Core Product

### Definition
- [ ] Product name finalized
- [ ] One-line description clear
- [ ] Transformation statement defined
- [ ] Target avatar specified

### Structure
- [ ] Number of modules/components set
- [ ] Each module named
- [ ] Each module content outlined
- [ ] Delivery format confirmed
- [ ] Access duration defined

### Value Articulation
| Module | Name | What They Get | Value |
|--------|------|--------------|-------|
| 1 | | | R$ |
| 2 | | | R$ |
| 3 | | | R$ |
| 4 | | | R$ |
| 5 | | | R$ |
| **Total Core** | | | **R$** |

---

## Bonus Stack

### Bonus Checklist

**Bonus #1: Fast Action**
- [ ] Name: ______
- [ ] Type: Fast Action
- [ ] Description written
- [ ] Value assigned: R$___
- [ ] Deadline/limit set
- [ ] Delivery method clear

**Bonus #2: Objection Killer**
- [ ] Name: ______
- [ ] Objection it solves: ______
- [ ] Description written
- [ ] Value assigned: R$___
- [ ] Clear connection to objection

**Bonus #3: Complementary**
- [ ] Name: ______
- [ ] Type: Complementary
- [ ] Description written
- [ ] Value assigned: R$___
- [ ] Adds value (doesn't compete)

**Bonus #4 (Optional):**
- [ ] Name: ______
- [ ] Description written
- [ ] Value assigned: R$___

**Bonus #5 (Optional):**
- [ ] Name: ______
- [ ] Description written
- [ ] Value assigned: R$___

### Bonus Quality Check
| Criteria | B1 | B2 | B3 | B4 | B5 |
|----------|----|----|----|----|----|
| Has independent value | [ ] | [ ] | [ ] | [ ] | [ ] |
| Solves specific problem | [ ] | [ ] | [ ] | [ ] | [ ] |
| Believable price anchor | [ ] | [ ] | [ ] | [ ] | [ ] |
| Complements (not competes) | [ ] | [ ] | [ ] | [ ] | [ ] |
| Attractive name | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## Guarantee

### Type Selected
- [ ] Money Back (unconditional)
- [ ] Conditional (action-based)
- [ ] Result-Based
- [ ] Hybrid

### Guarantee Details
- [ ] Duration: ___ days
- [ ] Conditions clear (if any)
- [ ] Process simple
- [ ] Contact method defined
- [ ] Copy written

### Guarantee Quality Check
- [ ] Removes purchase risk
- [ ] Shows confidence in product
- [ ] Not positioned as "exit"
- [ ] Terms are honor-able

---

## Pricing Structure

### Main Price
- [ ] Single payment: R$___
- [ ] Payment plan available: [ ] Yes / [ ] No
- [ ] Payment plan: ___x de R$___
- [ ] Payment plan total: R$___

### Price Positioning
- [ ] Value stack calculated
- [ ] Stack total: R$___
- [ ] Actual price: R$___
- [ ] Discount shown: ___%
- [ ] Comparison anchors set

### Price Validation
- [ ] Competitive with market
- [ ] ROI calculable for buyer
- [ ] Payment plan accessible
- [ ] No hidden fees

---

## Scarcity Elements

### Type of Scarcity
- [ ] Cart close (time-based)
- [ ] Limited spots (quantity)
- [ ] Price increase after deadline
- [ ] Bonus removal after deadline

### Scarcity Details
- [ ] Cart open date: ______
- [ ] Cart close date: ______
- [ ] Cart close time: ______
- [ ] Timezone specified: ______
- [ ] Limited spots number (if any): ______

### Scarcity Validation
- [ ] 100% REAL (not fabricated)
- [ ] Reason explained
- [ ] Will be honored
- [ ] No planned "extensions"

---

## Stack Summary

### Value Stack Table
| Item | Value |
|------|-------|
| {{Module 1}} | R$___ |
| {{Module 2}} | R$___ |
| {{Module 3}} | R$___ |
| {{Module 4}} | R$___ |
| {{Module 5}} | R$___ |
| {{Bonus 1}} | R$___ |
| {{Bonus 2}} | R$___ |
| {{Bonus 3}} | R$___ |
| **TOTAL VALUE** | **R$___** |
| **YOUR INVESTMENT** | **R$___** |
| **YOU SAVE** | **R$___ (__%)** |

### Offer Summary Copy
```
What You Get:
✓ {{Core Product}}
✓ {{Module 1}}
✓ {{Module 2}}
✓ {{Module 3}}
+ BONUS: {{Bonus 1}} (Value: R$___)
+ BONUS: {{Bonus 2}} (Value: R$___)
+ BONUS: {{Bonus 3}} (Value: R$___)
+ {{Guarantee}} Guarantee

Total Value: R$___
Your Investment: R$___ (or _x de R$___)
```

---

## Sales Page Integration

### Stack Section Ready
- [ ] Stack section written
- [ ] Value anchoring clear
- [ ] Visual presentation clean
- [ ] CTA buttons present
- [ ] Price clearly displayed
- [ ] Payment options shown

### Pre-Close Elements
- [ ] Recap of transformation
- [ ] Final objection handler
- [ ] Risk reversal (guarantee)
- [ ] Urgency statement

---

## Final Validation

### Stack Completeness Score

| Component | Complete |
|-----------|----------|
| Core Product | [ ] |
| 3+ Bonuses | [ ] |
| Guarantee | [ ] |
| Pricing | [ ] |
| Scarcity | [ ] |

### Quality Checks

**Value Test:**
- [ ] Stack total > 10x price
- [ ] Each bonus has real value
- [ ] Transformation is clear

**Risk Test:**
- [ ] Guarantee removes friction
- [ ] Payment plan accessible
- [ ] Process is simple

**Urgency Test:**
- [ ] Scarcity is REAL
- [ ] Deadline is specific
- [ ] Will be honored

---

## Ready to Launch

**All components complete:** [ ] Yes / [ ] No

**Stack passes quality checks:** [ ] Yes / [ ] No

**Approved for Open Cart:** [ ] Yes / [ ] No

**Date:** ______
**Approved by:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Launch Stack*


---

<!-- live-launch-readiness.md -->
# Live Launch Readiness Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Prepare for live broadcast launches
> **Use**: Before going live with PLCs or Open Cart

---

## Tech Setup

### Streaming Platform
- [ ] Platform selected (Zoom/StreamYard/YT Live/FB Live)
- [ ] Account in good standing
- [ ] Streaming limits verified
- [ ] Backup platform identified

### Equipment
| Item | Ready | Tested |
|------|-------|--------|
| Camera | [ ] | [ ] |
| Microphone | [ ] | [ ] |
| Lighting | [ ] | [ ] |
| Internet (wired preferred) | [ ] | [ ] |
| Computer | [ ] | [ ] |
| Backup device | [ ] | [ ] |

### Audio Quality
- [ ] Microphone tested and clear
- [ ] No background noise
- [ ] Echo eliminated
- [ ] Backup audio option ready

### Video Quality
- [ ] Camera positioned correctly
- [ ] Lighting flattering
- [ ] Background clean/professional
- [ ] No distracting elements
- [ ] Test recording reviewed

### Internet
- [ ] Speed test completed: ___ Mbps up
- [ ] Minimum 10 Mbps upload
- [ ] Wired connection if possible
- [ ] Backup internet (mobile hotspot)

---

## Pre-Broadcast Checklist

### 1 Hour Before
- [ ] Equipment powered on
- [ ] All tests completed
- [ ] Water nearby
- [ ] Phone on silent/airplane mode
- [ ] "Do Not Disturb" sign up
- [ ] Notifications disabled on computer
- [ ] Browser tabs closed
- [ ] Outline/notes ready

### 30 Minutes Before
- [ ] Streaming software open
- [ ] Test stream completed
- [ ] Audio levels checked
- [ ] Lighting final check
- [ ] Appearance checked
- [ ] Energy up (warmup)

### 5 Minutes Before
- [ ] Go live early for buffer
- [ ] Confirm stream is working
- [ ] Welcome early viewers
- [ ] Final deep breath

---

## Content Preparation

### Live PLC Structure
- [ ] Opening hook memorized
- [ ] Key points outlined (not scripted)
- [ ] Transitions clear
- [ ] Q&A moments planned
- [ ] Close and CTA clear
- [ ] Backup content if tech fails

### Support Materials
- [ ] Slides ready (if using)
- [ ] Screen share tested
- [ ] Demo ready (if applicable)
- [ ] Links in chat ready
- [ ] Moderator briefed

---

## Engagement Setup

### Chat Management
- [ ] Moderator assigned
- [ ] Chat enabled
- [ ] Spam filter active
- [ ] FAQ responses ready
- [ ] Pinned message prepared

### Engagement Prompts
- [ ] Opening engagement question
- [ ] Mid-stream poll/question
- [ ] Comment request moments
- [ ] CTA moments planned

---

## Compressed Live Launch Schedule

### Day 1 - PLC1 Live
- [ ] Time: ______
- [ ] Duration: 45-60 min
- [ ] Focus: Opportunity + Authority
- [ ] Teaser for Day 2

### Day 2 - PLC2 Live
- [ ] Time: ______
- [ ] Duration: 60-75 min
- [ ] Focus: Transformation + Cases
- [ ] Teaser for Day 3

### Day 3 - PLC3 Live
- [ ] Time: ______
- [ ] Duration: 60-75 min
- [ ] Focus: Ownership + Preview
- [ ] Teaser for Cart Open

### Day 4 - Cart Open Live
- [ ] Time: ______
- [ ] Duration: 60-90 min
- [ ] Focus: Offer Reveal + Q&A
- [ ] Link in chat

---

## Extended Open Cart Lives

### Day 1 - Enrollment Live
- [ ] Scheduled: ______
- [ ] Full offer presentation
- [ ] Q&A heavy
- [ ] Link ready

### Day 3 - FAQ Live
- [ ] Scheduled: ______
- [ ] Questions collected
- [ ] Objections addressed
- [ ] Testimonials ready

### Day 4 - Case Study Live
- [ ] Scheduled: ______
- [ ] Guest arranged (optional)
- [ ] Story prepared
- [ ] Results highlighted

### Day 5 - Closing Live
- [ ] Scheduled: ______
- [ ] Final Q&A
- [ ] Celebration energy
- [ ] Clear deadline

---

## Replay Strategy

### Replay Setup
- [ ] Auto-record enabled
- [ ] Replay page ready
- [ ] Replay email drafted
- [ ] Edit plan (trim start/end)

### Replay Email
- [ ] Subject line ready
- [ ] "If you missed it..." framing
- [ ] Key highlights listed
- [ ] Replay link prominent
- [ ] Expiration if applicable

---

## Emergency Protocols

### If Stream Fails
1. [ ] Don't panic (viewers understand)
2. [ ] Restart stream
3. [ ] If can't restart: email/social announcement
4. [ ] Reschedule if necessary

### If Audio Fails
1. [ ] Switch to backup mic
2. [ ] If no backup: announce in chat, reschedule
3. [ ] Send recorded version later

### If Internet Fails
1. [ ] Switch to mobile hotspot
2. [ ] If no backup: reschedule
3. [ ] Email list about delay

### Emergency Contacts
| Role | Name | Contact |
|------|------|---------|
| Tech support | | |
| Backup host | | |
| Moderator | | |

---

## Post-Live Checklist

### Immediately After
- [ ] Save recording
- [ ] Thank chat participants
- [ ] Note technical issues
- [ ] Capture chat highlights

### Within 2 Hours
- [ ] Edit replay (if needed)
- [ ] Upload to replay page
- [ ] Send replay email
- [ ] Post on social media

### Review
- [ ] View count: ______
- [ ] Peak concurrent: ______
- [ ] Comments/engagement: ______
- [ ] Tech issues: ______
- [ ] Improvements for next: ______

---

## Quality Benchmarks

### Viewership Goals
| Live | Goal | Actual |
|------|------|--------|
| PLC1 | ___% of list | |
| PLC2 | ___% of list | |
| PLC3 | ___% of list | |
| Cart Open | ___% of list | |

### Engagement Goals
- [ ] 50+ comments per live
- [ ] Questions answered live
- [ ] High energy maintained
- [ ] Clear CTA conversion

---

## Final Pre-Live Sign-Off

**Tech Ready:** [ ] Yes / [ ] No
**Content Ready:** [ ] Yes / [ ] No
**Support Ready:** [ ] Yes / [ ] No
**Backup Plans Ready:** [ ] Yes / [ ] No

**GO LIVE APPROVED:** [ ] Yes / [ ] No

**Date:** ______
**Signed:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Live Launch*


---

<!-- mental-triggers-activation.md -->
# Mental Triggers Activation Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Verify all 9 mental triggers are activated in the launch
> **Use**: Map triggers across entire launch sequence

---

## Trigger 1: Authority

### Required Activations
- [ ] Origin story told (PLC1)
- [ ] Credentials/experience mentioned
- [ ] Results demonstrated
- [ ] Expert positioning established

### Where Activated
| Location | How Activated | Check |
|----------|--------------|-------|
| PLC1 | Origin story | [ ] |
| PLC2 | Results proof | [ ] |
| Sales Page | About section | [ ] |
| Open Cart | "X years experience" | [ ] |

### Quality Check
- [ ] Credibility established without arrogance
- [ ] Vulnerability included (humble beginnings)
- [ ] Specific numbers used
- [ ] Third-party validation if available

---

## Trigger 2: Reciprocity

### Required Activations
- [ ] Real value in PLC1
- [ ] More value in PLC2
- [ ] Complete value in PLC3
- [ ] Free tools/templates offered

### Where Activated
| Location | What Given | Value Level |
|----------|-----------|-------------|
| PLC1 | {{TEACHING}} | [ ] High [ ] Medium |
| PLC2 | {{TEACHING}} | [ ] High [ ] Medium |
| PLC3 | {{TEACHING}} | [ ] High [ ] Medium |
| Bonus | {{FREEBIE}} | [ ] High [ ] Medium |

### Quality Check
- [ ] Value is REAL (not just teaser)
- [ ] Actionable immediately
- [ ] Worthy of being paid content
- [ ] Prospect thinks "if free is this good..."

---

## Trigger 3: Trust

### Required Activations
- [ ] Consistency throughout sequence
- [ ] Transparency about limitations
- [ ] Promises kept
- [ ] Honesty about who it's NOT for

### Where Activated
| Location | Trust Element | Check |
|----------|--------------|-------|
| All PLCs | Consistent messaging | [ ] |
| PLC2 | Transparent about objections | [ ] |
| PLC3 | Honest about scarcity | [ ] |
| Sales Page | Clear about who shouldn't buy | [ ] |
| Emails | Keeping promises | [ ] |

### Quality Check
- [ ] No exaggerated claims
- [ ] Limitations acknowledged
- [ ] Results timeframe realistic
- [ ] Guarantee genuine

---

## Trigger 4: Anticipation

### Required Activations
- [ ] Pre-prelaunch teasers
- [ ] PLC1 → PLC2 bridge
- [ ] PLC2 → PLC3 bridge
- [ ] PLC3 → Cart Open bridge
- [ ] Countdown created

### Where Activated
| Location | Anticipation Element | Check |
|----------|---------------------|-------|
| Pre-prelaunch | "Something big coming" | [ ] |
| End of PLC1 | Teaser for PLC2 | [ ] |
| End of PLC2 | Teaser for PLC3 | [ ] |
| End of PLC3 | Teaser for cart open | [ ] |
| Day before cart | "Tomorrow" email | [ ] |

### Quality Check
- [ ] Specific teasers (not vague)
- [ ] Creates genuine curiosity
- [ ] Delivers on teased promises
- [ ] Apple iPhone launch feeling

---

## Trigger 5: Likability

### Required Activations
- [ ] Personal storytelling
- [ ] Genuine personality shown
- [ ] Common ground established
- [ ] Human moments included

### Where Activated
| Location | Likability Element | Check |
|----------|-------------------|-------|
| PLC1 | Personal story | [ ] |
| PLC2 | Empathy with struggles | [ ] |
| Emails | Conversational tone | [ ] |
| Social | Real personality | [ ] |

### Quality Check
- [ ] Authentic (not fake persona)
- [ ] Relatable struggles shared
- [ ] Humor appropriate to audience
- [ ] Shows caring for audience

---

## Trigger 6: Events

### Required Activations
- [ ] Launch positioned as EVENT
- [ ] Specific dates that matter
- [ ] Live elements (if applicable)
- [ ] Community participation

### Where Activated
| Location | Event Element | Check |
|----------|--------------|-------|
| Pre-prelaunch | "Save the date" | [ ] |
| PLCs | Scheduled releases | [ ] |
| Cart Open | LAUNCH DAY | [ ] |
| Close Cart | Deadline event | [ ] |
| Lives | Real-time interaction | [ ] |

### Quality Check
- [ ] Feels like something happening NOW
- [ ] Creates FOMO for missing it
- [ ] Community feeling together
- [ ] Not just another email

---

## Trigger 7: Community

### Required Activations
- [ ] Comment engagement
- [ ] "Join us" framing
- [ ] Buyer community shown
- [ ] Shared experience created

### Where Activated
| Location | Community Element | Check |
|----------|------------------|-------|
| PLCs | Comment requests | [ ] |
| PLC2 | Others succeeding | [ ] |
| Open Cart | "X people joined" | [ ] |
| Social | Community interaction | [ ] |
| Post-sale | Group access | [ ] |

### Quality Check
- [ ] Real engagement happening
- [ ] Inclusive language used
- [ ] Movement feeling created
- [ ] Not exclusive/elitist tone

---

## Trigger 8: Social Proof

### Required Activations
- [ ] Case studies in PLC2
- [ ] Testimonials on sales page
- [ ] Buyer momentum in cart
- [ ] Diverse proof types

### Where Activated
| Location | Proof Type | Check |
|----------|-----------|-------|
| PLC1 | Quick mention | [ ] |
| PLC2 | Detailed cases (3+) | [ ] |
| Sales Page | Testimonials (5+) | [ ] |
| Open Cart | "X bought today" | [ ] |
| Mid-launch | New buyer stories | [ ] |

### Proof Diversity Check
- [ ] Different demographics
- [ ] Different starting points
- [ ] Different result levels
- [ ] Similar to target avatar

### Quality Check
- [ ] All proof is REAL
- [ ] Specific results (numbers)
- [ ] Includes "normal" people
- [ ] Before/after clear

---

## Trigger 9: Scarcity

### Required Activations
- [ ] Cart close deadline
- [ ] Real limitation explained
- [ ] Countdown visible
- [ ] No fake urgency

### Where Activated
| Location | Scarcity Element | Check |
|----------|-----------------|-------|
| PLC3 | Deadline announced | [ ] |
| Cart Open | Timeline stated | [ ] |
| Mid-launch | Countdown | [ ] |
| Final Day | Urgency emails | [ ] |
| Sales Page | Timer/deadline | [ ] |

### Scarcity Types Used
- [ ] Time-based (cart close)
- [ ] Quantity-based (limited spots)
- [ ] Bonus removal
- [ ] Price increase

### Quality Check
- [ ] 100% REAL scarcity
- [ ] Reason for limit explained
- [ ] No extensions planned
- [ ] Honoring the deadline

---

## Trigger Mapping Summary

| Trigger | Pre-Pre | PLC1 | PLC2 | PLC3 | Open | Mid | Close |
|---------|---------|------|------|------|------|-----|-------|
| Authority | | [ ] | [ ] | | [ ] | | |
| Reciprocity | | [ ] | [ ] | [ ] | | | |
| Trust | | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Anticipation | [ ] | [ ] | [ ] | [ ] | | | |
| Likability | | [ ] | [ ] | | [ ] | | |
| Events | [ ] | | | | [ ] | | [ ] |
| Community | | [ ] | [ ] | [ ] | [ ] | [ ] | |
| Social Proof | | [ ] | [ ] | | [ ] | [ ] | [ ] |
| Scarcity | | | | [ ] | | | [ ] |

---

## Final Validation

**All 9 triggers activated at least once:** [ ] Yes / [ ] No

**Dominant triggers per phase:**
- Pre-prelaunch: Anticipation
- PLC1: Authority, Anticipation
- PLC2: Social Proof, Reciprocity
- PLC3: Anticipation, Community
- Open Cart: Events, Social Proof
- Close Cart: Scarcity, Events

**Launch ready:** [ ] Yes / [ ] Needs work

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Mental Triggers*


---

<!-- open-cart-sequence.md -->
# Open Cart Email Sequence Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Validate complete open cart email sequence
> **Stats**: Day 1 = 25% sales, Last Day = 50% sales

---

## Day 1 - Launch Day

### Email #1 - OPEN (Morning 8-9 AM)
- [ ] Subject line compelling
- [ ] "It's open" energy
- [ ] Link prominent
- [ ] Stack summary included
- [ ] Scarcity mentioned
- [ ] Deadline stated
- [ ] PS with hook

**Subject used:** ______

### Email #2 - Response (Afternoon 2-3 PM)
- [ ] Social proof (X people entered)
- [ ] First reactions/quotes
- [ ] Reminder of what's included
- [ ] Link prominent
- [ ] PS

**Subject used:** ______

### Email #3 - Q&A/BTS (Evening 7-8 PM)
- [ ] FAQ addressed
- [ ] Behind the scenes element
- [ ] What happens after joining
- [ ] Link prominent
- [ ] Teaser for tomorrow

**Subject used:** ______

### Day 1 Quality Check
- [ ] All 3 emails scheduled
- [ ] Different angles used
- [ ] Links all working
- [ ] Tracking enabled

---

## Day 2 - Case Study

### Email - Case Study
- [ ] Feature one transformation story
- [ ] Before/after clear
- [ ] Specific results
- [ ] Quote from person
- [ ] Connection to reader
- [ ] Link to sales page
- [ ] Days remaining mentioned

**Subject used:** ______

### Day 2 Quality Check
- [ ] Email scheduled
- [ ] Case study compelling
- [ ] Different from PLC2 cases

---

## Day 3 - FAQ

### Email - FAQ/Objections
- [ ] Top 3-5 questions answered
- [ ] Objections addressed
- [ ] Guarantee mentioned
- [ ] Payment plan mentioned
- [ ] Link to sales page
- [ ] Days remaining

**Subject used:** ______

### FAQ Covers
- [ ] Time objection
- [ ] Money objection
- [ ] "Will it work for me" objection
- [ ] Trust objection
- [ ] How-to questions

---

## Day 4 - Pre-Close

### Email - Penultimate Day
- [ ] Tomorrow is last day
- [ ] Recap of what they get
- [ ] Urgency building
- [ ] Final testimonial
- [ ] Link prominent
- [ ] PS with emotional appeal

**Subject used:** ______

### Day 4 Quality Check
- [ ] Urgency feels real
- [ ] Not too aggressive yet
- [ ] Sets up final day

---

## Day 5 - Final Day

### Email #1 - Last Day Morning (8-9 AM)
- [ ] LAST DAY prominent
- [ ] Deadline clear (time + timezone)
- [ ] Full stack reminder
- [ ] Link prominent
- [ ] "This is it" energy

**Subject used:** ______

### Email #2 - Afternoon (2-3 PM)
- [ ] Hours remaining stated
- [ ] Emotional/story angle
- [ ] "If you're on the fence..."
- [ ] Link prominent
- [ ] Lower pressure, higher connection

**Subject used:** ______

### Email #3 - Evening (6-7 PM)
- [ ] X hours remaining
- [ ] Direct urgency
- [ ] No more arguments, just decision
- [ ] Link prominent
- [ ] Teaser for final email

**Subject used:** ______

### Email #4 - Final Push (9-10 PM)
- [ ] Final hours
- [ ] Emotional close
- [ ] "See you on the other side"
- [ ] Link prominent
- [ ] PS with deadline

**Subject used:** ______

### Email #5 - Last Call (11-11:30 PM) [Optional]
- [ ] Minutes remaining
- [ ] Ultra short
- [ ] Just the link
- [ ] "Closing now"

**Subject used:** ______

### Day 5 Quality Check
- [ ] At least 4 emails scheduled
- [ ] Escalating urgency
- [ ] Different angles
- [ ] Links all working
- [ ] Deadline is REAL

---

## Sequence Quality Checks

### Coverage Check
| Element | Covered | Email # |
|---------|---------|---------|
| Stack reveal | [ ] | |
| Social proof | [ ] | |
| Case study | [ ] | |
| FAQ/Objections | [ ] | |
| Guarantee | [ ] | |
| Payment plan | [ ] | |
| Urgency | [ ] | |
| Final deadline | [ ] | |

### Variety Check
| Angle | Used |
|-------|------|
| Announcement | [ ] |
| Social proof | [ ] |
| Story/emotion | [ ] |
| FAQ/objection | [ ] |
| Urgency | [ ] |
| Final call | [ ] |

### Technical Check
- [ ] All emails written
- [ ] All emails loaded in platform
- [ ] All send times set
- [ ] All links tested
- [ ] All tracking enabled
- [ ] Mobile preview checked

---

## Email Metrics to Track

| Email | Day | Time | Subject | Opens | Clicks | Sales |
|-------|-----|------|---------|-------|--------|-------|
| Open #1 | 1 | | | | | |
| Open #2 | 1 | | | | | |
| Open #3 | 1 | | | | | |
| Case | 2 | | | | | |
| FAQ | 3 | | | | | |
| Pre-close | 4 | | | | | |
| Final #1 | 5 | | | | | |
| Final #2 | 5 | | | | | |
| Final #3 | 5 | | | | | |
| Final #4 | 5 | | | | | |
| Last call | 5 | | | | | |

---

## Contingency Emails

### If Day 1 Below Expectations
- [ ] Extra evening email ready
- [ ] Social media post ready
- [ ] Quick wins to highlight

### If Tech Issues
- [ ] Apology template ready
- [ ] Alternative link ready
- [ ] Manual process documented

### If Early Sellout (limited spots)
- [ ] Waitlist email ready
- [ ] Sold out announcement ready

---

## Sequence Approval

**Total emails in sequence:** ___

**Day 1:** ___ emails
**Days 2-4:** ___ emails
**Day 5:** ___ emails

**All emails reviewed:** [ ] Yes

**Sequence approved:** [ ] Yes / [ ] No

**Date:** ______
**Approved by:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Open Cart Emails*


---

<!-- plc-quality.md -->
# PLC Quality Checklist

Bridge checklist for Product Launch Formula pre-launch content. This file exists to give tasks and workflows a stable canonical entrypoint while routing evaluation to the detailed PLF assets that already exist in the squad.

## Use

Apply this checklist when creating or evaluating:

- PLC1
- PLC2
- PLC3
- batch CPL evaluations

This checklist does not replace the deeper PLF checklists. It tells the operator which checklist stack must be loaded.

## Required Companion Checklists

Always load:

- `checklists/plf/cpl-evaluation-execution-checklist.md`
- `checklists/plf/mental-triggers-activation.md`

Then load the stage-specific checklist:

- PLC1 -> `checklists/plf/cpl1-opportunity-checklist.md`
- PLC2 -> `checklists/plf/cpl2-transformation-checklist.md`
- PLC3 -> `checklists/plf/cpl3-ownership-checklist.md`
- CPL4 / sales video -> `checklists/plf/sales-video-complete-production-aid.md`

## Global Quality Gate

- [ ] The correct stage-specific PLF checklist was loaded.
- [ ] The execution checklist was loaded before scoring.
- [ ] Mental trigger activation was reviewed across the sequence.
- [ ] The piece delivers real value and not teaser-only content.
- [ ] The piece does not introduce premature hard selling.
- [ ] The score threshold is at least 80% for the relevant stage checklist.

## Stage Routing

### PLC1 - The Opportunity

- [ ] Use `cpl1-opportunity-checklist.md`
- [ ] Confirm opportunity clarity, authority, teaching, objections, foreshadow, and CTA

### PLC2 - The Transformation

- [ ] Use `cpl2-transformation-checklist.md`
- [ ] Confirm transformation proof, teaching depth, objection handling, and CPL3 anticipation

### PLC3 - The Ownership

- [ ] Use `cpl3-ownership-checklist.md`
- [ ] Confirm ownership vision, pivot to the offer, soft landing, and seed scarcity

### CPL Evaluation / Batch Evaluation

- [ ] Use `cpl-evaluation-execution-checklist.md`
- [ ] Use the relevant production aid for the CPL number
- [ ] Consolidate trigger and scoring logic into the final report

## Pass Rule

- `PASS` when the correct detailed PLF checklist stack was applied and the stage score is 80%+
- `REVISE` when the stack was applied but important quality gaps remain
- `BLOCK` when the wrong checklist stack was used or core PLF structure is missing


---

<!-- plc1-complete-production-aid.md -->
# PLC #1 — THE OPPORTUNITY: COMPLETE PRODUCTION AID

> **Framework**: Product Launch Formula (Jeff Walker)
> **Theme**: "WHY" — Por que o prospect deveria se importar?
> **Source**: Launch (Original + Updated 2021 Edition)

---

## STRATEGIC FOUNDATION

**The single job of PLC #1:** Make your prospect believe that a meaningful transformation is possible AND that you're the right person to guide them toward it — without ever mentioning a product, price, or offer.

**Success criteria:** When PLC #1 is done right, the viewer finishes the video thinking three things simultaneously:
1. "This is real"
2. "This could work for me"
3. "I need to see the next video"

### What PLC #1 Attacks Directly (The 4 Reasons People Don't Buy)

| Reason | Description | PLC #1 Action |
|--------|-------------|---------------|
| **#3** | "I don't believe YOU" (don't trust your ethics or competence) | **PRIMARY TARGET** — Demolished through positioning story, quality of teaching, and empathy demonstrated |
| **#4** | "I believe the product works but not FOR ME" | **BEGINS ATTACKING** — Through relatable stories, achievable framing, and objection raising. PLC #2 finishes the job |
| #1 | Not interested | PLF can't fix this |
| #2 | No money | PLF can't fix this |

---

## PRE-PRODUCTION RESEARCH (Before You Write a Single Word)

### Audience Intelligence Gathering

- [ ] Review all pre-prelaunch survey responses — extract exact language your prospects use
- [ ] Identify the top 5 pain points in their own words (not your interpretation)
- [ ] Identify the top 5 desires/aspirations in their own words
- [ ] List every objection that appeared more than once in survey data
- [ ] Rank objections by frequency — the top 3-5 will be used across the PLC sequence
- [ ] Identify the emotional tone of your audience: Frustrated? Hopeful? Skeptical? Exhausted? Cynical?
- [ ] Note the specific vocabulary and jargon your audience uses — mirror it in your copy

### Transformation Clarity

- [ ] Write the "Before State" in one paragraph: What is their life/business/situation like RIGHT NOW? What's the daily frustration? What have they tried and failed?
- [ ] Write the "After State" in one paragraph: What does their life/business/situation look like AFTER the transformation? Be concrete — not "better life" but specific, tangible changes
- [ ] Identify the GAP between before and after — this gap is the emotional engine of your entire launch
- [ ] Ask yourself: "Am I selling the drill or the hole?" If your transformation statement mentions your tool/method/system, rewrite it around the RESULT

### Positioning Story Development

- [ ] List every credential, result, and experience that establishes your authority
- [ ] Rank them by relatability (not impressiveness) — the best credentials are the ones your audience can connect with emotionally
- [ ] Identify your "I was where you are" moment — the shared struggle that creates affinity
- [ ] Write the turning point: What changed for you? What did you discover/build/learn?
- [ ] Identify the moment of proof: What result validated that the transformation is real?
- [ ] Test: Does your story make you seem human and relatable, or distant and untouchable? If untouchable, add vulnerability

### Content Selection for Teaching Segment

- [ ] List everything you COULD teach about this topic
- [ ] Select 1-2 points that meet ALL of these criteria:
  - (a) genuinely useful on its own
  - (b) creates an "aha" moment
  - (c) naturally leads to wanting more
  - (d) demonstrates your expertise by showing, not claiming
- [ ] Verify: Could someone take action on this teaching today? If not, it's too abstract
- [ ] Verify: Does this teaching open a loop that PLC #2 will deepen? If it closes the loop entirely, you've gone too far

---

## THE EMOTIONAL ARCHITECTURE — How PLC #1 Feels to the Viewer

This is the invisible layer most people miss. The SEQUENCE OF EMOTIONS your viewer should experience, in order:

| Timing | Emotion | Viewer Thought |
|--------|---------|----------------|
| Minute 0-1 | Recognition, feeling seen | "This person gets me." |
| Minute 1-3 | Respect, curiosity | "Wait, they've actually done this?" |
| Minute 3-5 | Hope, excitement | "This is actually possible?" |
| Minute 5-8 | Surprise, gratitude | "Oh wow, I didn't know that." (the teaching moment) |
| Minute 8-10 | Trust, relief | "They even addressed my concern." |
| Minute 10-11 | Anticipation, desire | "There's MORE coming?" |
| Final moment | Engagement, commitment | "I need to comment and come back for the next one." |

**Critical:** If your viewer doesn't move through this emotional sequence, your PLC #1 isn't doing its job — no matter how good the information is.

---

## SCRIPT STRUCTURE — BEAT BY BEAT WITH COPY DEPTH

### THE OPENING (First 30-90 seconds)

You have roughly 30 seconds before the viewer decides to stay or leave. The opening must accomplish one thing: **PATTERN INTERRUPT + RELEVANCE.**

#### Strategy A — Lead with Their Pain (Empathy-First Opening)

Start by describing their current reality so accurately that they feel understood. Not your credentials, not your story — THEIR world.

**Copy framework:**
```
"If you're a [identity], you probably know what it feels like to [specific frustration].
You've probably tried [common failed approach] and wondered if [core doubt].
I know that feeling because [brief bridge to your story]..."
```

**When to use:** When your audience is frustrated, skeptical, or has tried and failed before. This opening says "I see you" before anything else.

#### Strategy B — Lead with the Possibility (Opportunity-First Opening)

Start with a bold but believable statement about what's possible. Not hype — a grounded, specific promise of transformation.

**Copy framework:**
```
"In the next [time], I'm going to show you [specific transformation].
Not theory — I'm going to walk you through [concrete element].
And by the time we're done, you'll see exactly why [reframe of their situation]..."
```

**When to use:** When your audience is hungry for solutions and generally trusts that solutions exist — they just haven't found the right one yet.

#### Strategy C — Lead with a Story (Narrative-First Opening)

Open with a brief, vivid scene that embodies the transformation. Drop the viewer into a moment.

**Copy framework:**
```
"[Vivid scene of the 'after' moment — you or a client experiencing the result].
That moment happened because of [bridge to the method/approach].
And today I want to show you how it's possible for you too..."
```

**When to use:** When you have a powerful personal or client story that immediately captures attention and makes the transformation tangible.

#### Opening Mistakes to Avoid

- [ ] Don't open with "Hi, my name is X and I'm the founder of Y" — nobody cares yet
- [ ] Don't open with a list of your credentials — earn the right to share them later
- [ ] Don't open with vague promises ("I'm going to change your life") — specificity creates belief
- [ ] Don't open with excessive production branding (long intros, logo animations) — get to the human immediately
- [ ] Don't open with "In this video I'm going to..." unless followed by something genuinely compelling

---

### BEAT 1 — SHOW THE OPPORTUNITY (2-4 minutes)

**The core principle:** You are selling the destination, not the transportation.

> "If you have a hardware store and you're selling drills, you're not selling drills — you're selling holes in wood." — Jeff Walker

#### Copy Development Process

**Step 1 — Write the transformation statement:**
```
"By [timeframe/milestone], you could [specific tangible result] instead of [current frustrating reality]."
```

**Step 2 — Make it visual and concrete:**

| DON'T Say | DO Say |
|-----------|--------|
| "You'll have more freedom" | "You'll wake up on a Tuesday morning with no alarm, check your phone, and see that three new sales came in while you were sleeping" |
| "You'll grow your business" | "You'll go from scrambling for clients to having a waitlist of people who already want to work with you" |

**Step 3 — Bridge to their current reality:**
```
"Right now, you're probably [current pain/frustration].
And you've probably been told that [common bad advice or limiting belief].
But what if [reframe]?"
```

**Step 4 — Expand the possibility without crossing into hype:**
- Show multiple dimensions of the transformation (financial, emotional, lifestyle, professional, relational)
- Use "imagine" or "what if" framing to make it safe to dream
- Ground every aspiration with a proof point or example

#### Opportunity Framing Checklist

- [ ] Transformation is stated in terms of THEIR life, not your product features
- [ ] At least one concrete, visual "after" scenario is painted
- [ ] The gap between "before" and "after" is emotionally clear
- [ ] The opportunity feels achievable — not fantasy, not hype
- [ ] No mention of HOW they'll get there (that's PLC #2 and #3) — only WHAT is possible and WHY it matters

---

### BEAT 2 — POSITION YOURSELF (2-3 minutes)

**The order matters:** Empathy → Story → Credentials → Bridge to teaching

**Never lead with credentials.** Lead with shared experience, THEN reveal credentials within the story.

#### The Empathy-Authority Sequence

**Layer 1 — Shared identity:**
```
"I'm a [identity] just like you..."
"I started in the exact same place you are today..."
"I know what it's like to [specific shared struggle]..."
```

**Layer 2 — The struggle (vulnerability):**
```
"I was told [discouraging thing]..."
"I tried [approach] and it didn't work..."
"There was a point where I almost [gave up / quit / accepted the status quo]..."
```

**Layer 3 — The turning point:**
```
"Then I discovered [insight / method / approach]..."
"Everything changed when I [specific action]..."
"The breakthrough came when I realized [key insight]..."
```

**Layer 4 — The credentials (earned through story):**
```
"Since then, I've [impressive results / credentials], including [most impressive proof points]..."
```

**Layer 5 — The bridge back to them:**
```
"And now I want to show you how you can do the same thing..."
"The reason I'm sharing this is because [genuine motivation to help]..."
```

#### The Barry Friedman Positioning Master Class (Deconstructed)

| Layer | What He Said | What It Accomplished |
|-------|--------------|---------------------|
| Shared identity | "I'm a lot like you. I found a passion for juggling when I was a kid" | Establishes common ground |
| Struggle | "...but was told I couldn't do it for a living. My guidance counselor said I'd be broke and homeless" | Vulnerability, relatability, creates affinity |
| Turning point | "Right then, I swore to myself that I would prove him wrong" | Emotional resonance, underdog narrative |
| Credentials (in story) | "A few years later, I was 23, performing on my first Tonight Show" | Authority through narrative, not résumé |
| Deeper credentials | "I've been on over 100 television shows" | Compounds authority |
| Bridge to them | "...and you can do that too! Now, I want to show you how" | Transfers possibility, opens the door |

#### Positioning for Different Authority Levels

**If you have strong credentials:**
- Weave them into story — never present as a list
- Frame every credential as being in service of helping them
- Counter potential "I could never be like them" with: "I wasn't born with this — I learned it, and here's what I figured out"

**If you have moderate credentials:**
- Lead with results (yours or clients') rather than titles
- "I've helped X people do Y" is more powerful than "I have a certification in Z"
- Specificity compensates for scale: "I took one client from A to B in C months" beats vague claims

**If you have limited formal credentials:**
- Position from research and obsession: "I've spent X years studying this and testing every approach..."
- Position from results: "I figured out how to do X, and here's what I learned..."
- Position from empathy: "I went through this exact struggle and found a way out..."
- Your authenticity and depth of understanding IS your credential

#### Positioning Mistakes to Avoid

- [ ] Listing credentials like a résumé — always embed in story
- [ ] Bragging without bridge — every credential must connect back to "and this is how it helps YOU"
- [ ] Being falsely humble — if you have real results, own them. False modesty undermines trust
- [ ] Positioning so high that the prospect can't relate — always bring it back to common ground
- [ ] Spending too long on positioning — this section should establish trust, not be the main event

---

### BEAT 3 — TEACH (3-5 minutes)

**The teaching paradox:** The more you give away, the more they want to buy. This is counterintuitive but consistently proven.

> "Don't just tease them — give them some substance. I have hundreds of people who have done successful launches just based on the free material I've given out during my prelaunch." — Jeff Walker

#### What to Teach in PLC #1 (Selection Criteria)

Teach something that creates a **mindset shift or framework shift**, not necessarily a tactic. PLC #1 teaching should make them see their situation differently. PLC #2 will deliver the tactical depth.

**Good PLC #1 teaching:**
- A new way of looking at their problem that they haven't considered
- A framework or mental model that reframes the opportunity
- One powerful insight that challenges a common misconception
- A principle that, once understood, changes how they approach everything

#### The 3-Layer Teaching Structure

**Layer 1 — The Insight:**
```
"Most people think [common belief]. But the reality is [reframe]..."
```

**Layer 2 — The Evidence:**
```
"Here's why that's true: [example / data / story / demonstration]..."
```

**Layer 3 — The Application:**
```
"What this means for you is [specific implication]. So instead of [old approach], you can [new approach]..."
```

#### Teaching Quality Control

- [ ] Is this genuinely useful on its own? (Not just a teaser for the paid product)
- [ ] Does it create an "aha" or "I never thought of it that way" moment?
- [ ] Can they take at least one action based on this teaching TODAY?
- [ ] Does it demonstrate your expertise by SHOWING it, not just claiming it?
- [ ] Does it naturally leave them wanting more? (Opens a loop for PLC #2)
- [ ] Is it concrete enough to be actionable but not so complete that they don't need PLC #2?

#### Teaching Tone Calibration

- Teach like a generous expert, not a stingy gatekeeper
- Use "here's what I've found works" not "you need to do this"
- Include "why" behind the "what" — people trust teachers who explain reasoning
- If you reference data or research, cite it naturally — authority through rigor
- Avoid jargon unless your audience speaks it — clarity is expertise

---

### BEAT 4 — RAISE OBJECTIONS (1-3 minutes)

**The psychology:** Your prospect is thinking these objections whether you address them or not. By raising them yourself, you accomplish three things:
1. They feel understood
2. You control the framing
3. You establish trust by not hiding from difficult questions

#### Objection Mapping for PLC #1

| Objection Type | Example | How to Handle in PLC #1 |
|----------------|---------|------------------------|
| Identity objection | "I'm not the type of person who can do this" | Address through relatable positioning story + "ordinary people" framing |
| Past failure objection | "I've tried before and failed" | Acknowledge directly, then reframe: "The reason it didn't work before is [insight]" |
| Complexity objection | "This seems too complicated" | Preview that you'll break it down step by step in upcoming videos |
| Time objection | "I don't have time for this" | Reframe: show the cost of NOT doing it, or show how the method is more efficient |
| Skepticism objection | "This sounds too good to be true" | Ground the promise with specific, believable examples. Remove hype language |
| Relevance objection | "This works for others but not my situation" | Promise to address specific scenarios in PLC #2 and #3. Use diverse examples |

#### PLC #1 Objection Strategy

- Raise 2-3 objections maximum in PLC #1
- You don't have to RESOLVE all of them here — raising them and promising to address them in PLC #2 builds anticipation
- Use language: "Now, you might be thinking [objection]. And that's a fair concern. Here's what I want you to consider..."
- Or: "I know some of you are wondering about [objection]. I'm going to address that in detail in my next video, but let me say this right now..."

#### Objection Handling Mistakes

- [ ] Don't skip this beat — it feels uncomfortable but it's essential
- [ ] Don't dismiss objections — validate them before addressing them
- [ ] Don't try to crush every objection in PLC #1 — save the deep destruction for PLC #2
- [ ] Don't create new objections — only address ones your audience actually has (from research)

---

### BEAT 5 — FORESHADOW PLC #2 (30-60 seconds)

**The anticipation trigger:** This is a deliberate, conscious installation of desire for the next piece of content. You are engineering a cliffhanger.

#### Foreshadowing Formula

```
"In my next video, which is coming [timeframe], I'm going to show you [specific tease].
This is where things get really exciting because [reason it matters to them].
You're going to see [preview of the transformation or teaching].
So make sure you [watch for the email / check back here / etc.]"
```

#### What Makes a Good Foreshadow

- **Specific enough** that they can picture what they'll learn → creates desire
- **Vague enough** that they can't guess the full content → maintains curiosity
- **Connected to an objection** or question they have → creates urgency to watch
- **Positions PLC #2 as going DEEPER**, not just continuing → creates escalation

#### Foreshadowing Examples by Offer Type

**For a course/training:**
```
"In the next video, I'm going to walk you through the exact [method/system] that [result].
I'll break it down step by step so you can see exactly how it works..."
```

**For a service:**
```
"Next time, I'm going to show you the [number] biggest mistakes I see [audience] making
and how to fix each one. Number [X] alone could [specific impact]..."
```

**For a software/tool:**
```
"In the next video, I'll do a live walkthrough of [process] and show you how [specific result]
can happen in [timeframe] instead of [current painful timeframe]..."
```

---

### BEAT 6 — CALL TO ACTION (30-60 seconds)

#### Why Comments Matter (Strategic Reasons)

- **Social proof:** new viewers see enthusiasm from others
- **Community:** shared experience creates belonging
- **Launch conversation:** transforms one-way broadcast into dialogue
- **Real-time objection intelligence:** you discover what's really on their minds
- **Micro-commitment:** commenting is a small action that increases likelihood of future actions (consistency principle)
- **When you respond** to comments, you build likability and trust exponentially

#### CTA Design Principles

Don't just say "leave a comment below." Give them a SPECIFIC PROMPT that's easy to answer and emotionally engaging.

**Effective CTA prompts for PLC #1:**
```
"Tell me in the comments: what's the #1 thing holding you back from [transformation]?"

"I'd love to know: what would change in your life if you could [achieve the result]?
Drop your answer below."

"What's the biggest challenge you're facing with [topic] right now?
Tell me in the comments — I read every single one."

"If you could [achieve result] in the next [timeframe], what would that mean for you?
Share below."
```

#### CTA Copy Structure

```
"Now I want to hear from you. [Specific question]. Leave your answer in the comments below —
I read every single one and I'll be responding personally. And don't forget: my next video
is coming in [timeframe], where I'll show you [foreshadow callback]. You don't want to miss it."
```

#### CTA Mistakes

- [ ] Don't skip it — every video must end with a comment CTA
- [ ] Don't make it too broad ("What do you think?") — specificity drives response
- [ ] Don't make it too demanding ("Write 500 words about your journey") — make it easy
- [ ] Don't forget to mention you'll READ and RESPOND — this is a huge trust signal
- [ ] Don't end abruptly after CTA — close with warmth and energy

---

## THE INVISIBLE LAYER — MENTAL TRIGGER ACTIVATION MAP

Each beat activates specific triggers. This map ensures you're not accidentally leaving triggers dormant:

| Beat | Triggers Activated | How |
|------|-------------------|-----|
| Opening | Likability, Trust | Empathy, shared understanding |
| Opportunity | Hope, Desire | Vivid "after" picture, concrete transformation |
| Positioning | Authority, Likability, Trust | Story-based credentials, vulnerability, affinity |
| Teaching | Authority, Reciprocity | Demonstrating expertise, giving real value for free |
| Objections | Trust, Likability | Honesty, showing you understand their doubts |
| Foreshadow | Anticipation | Open loop, specific tease of PLC #2 |
| CTA | Community, Commitment | Shared experience, micro-commitment through commenting |

**Cumulative effect by end of PLC #1:** The viewer feels understood (likability), believes you know what you're talking about (authority), feels they've received something valuable for free (reciprocity), trusts you more than they did 12 minutes ago (trust), and is actively waiting for the next video (anticipation).

---

## TIMING AND PACING GUIDE

**Total recommended duration:** 8-15 minutes

Shorter is fine if your market is impatient. Longer is fine if you're teaching deeply and engagement stays high. Walker's own PLCs sometimes ran 18+ minutes. The content should dictate the length, not an arbitrary timer.

### Pacing Rhythm

| Section | % of Total | For 12-min video |
|---------|------------|------------------|
| Opening + Hook | 5-10% | 0:30 - 1:00 |
| Opportunity (Beat 1) | 20-25% | 2:30 - 3:00 |
| Positioning (Beat 2) | 15-20% | 2:00 - 2:30 |
| Teaching (Beat 3) | 25-35% | 3:00 - 4:00 |
| Objections (Beat 4) | 10-15% | 1:00 - 2:00 |
| Foreshadow (Beat 5) | 5% | 0:30 - 0:45 |
| CTA (Beat 6) | 5% | 0:30 - 0:45 |

**Pacing principle:** Start warm (empathy/story), build energy through the opportunity, sustain it through teaching, bring it down slightly for objections (thoughtful, serious tone), then ramp it back up for the foreshadow and CTA.

---

## FORMAT AND PRODUCTION NOTES

### Screen-capture (slides + voiceover)

- Less intimidating if camera-shy
- Easier to control pacing and visuals
- Good for data-heavy or process-heavy teaching
- **Risk:** can feel impersonal if slides are text-heavy
- **Best practice:** visual slides (images, diagrams, key phrases) — NOT walls of text

### Full-motion video (on camera)

- Stronger personal connection and likability
- Less prep if you know your material
- More engaging for story/positioning beats
- **Risk:** can feel unstructured without preparation
- **Best practice:** use notes/teleprompter for key beats, but let personality come through

### Hybrid approach

- Open and close on camera (personal connection for hook and CTA)
- Switch to screen-capture for teaching segment (better for visual demonstrations)
- This often gives the best of both worlds

**Production quality note:** Good enough is good enough. Waiting for "perfect" production kills launches. Clear audio matters more than perfect lighting. Genuine energy matters more than professional sets.

---

## PLC #1 SELF-ASSESSMENT RUBRIC

After completing your PLC #1, score each dimension. **If any dimension scores below 3, revise before publishing.**

| Dimension | 1 (Weak) | 3 (Solid) | 5 (Exceptional) |
|-----------|----------|-----------|-----------------|
| Empathy | Generic opening, no sign of understanding their world | Addresses their situation specifically, uses their language | Viewer feels "they're inside my head" within first 60 seconds |
| Opportunity clarity | Vague promises, abstract benefits | Clear transformation stated, "after" picture is visible | Vivid, multi-dimensional "after" picture that creates genuine desire |
| Positioning | Credentials listed, no story | Story-based credentials with some vulnerability | Empathy → story → credentials → bridge sequence executed perfectly |
| Teaching value | Teaser only, nothing actionable | One useful insight or framework they can apply | Genuinely valuable content that could generate results on its own |
| Objection handling | Ignored or glossed over | 1-2 objections raised and partially addressed | Top objections raised with honest, specific responses or strategic promises |
| Anticipation | No foreshadow or generic "stay tuned" | Specific tease of PLC #2 content | Tease creates genuine desire to see next video immediately |
| CTA | Generic "leave a comment" | Specific question that's easy to answer | Emotionally engaging prompt that generates quality comments and self-revelation |
| Zero pitch | Product/price/offer mentioned or implied | No explicit pitch but some "salesy" energy leaks through | Completely educational/inspirational — zero hint of selling |
| Emotional arc | Flat energy throughout | Some emotional variation across beats | Clear arc: recognition → respect → hope → surprise → trust → anticipation |
| Rewatchability | One-and-done content | Good enough to recommend to a friend | So valuable that viewers share it unprompted and reference it later |

**Minimum viable PLC #1:** Every dimension at 3 or above.
**Launch-winning PLC #1:** Most dimensions at 4-5, no dimension below 3.

---

## TOP 15 PLC #1 MISTAKES (Ranked by Damage)

1. **Opening with credentials instead of empathy** — Instant disconnect. They don't care who you are until they feel you understand who THEY are

2. **Teaching too little** — The #1 content mistake. Being stingy destroys reciprocity and authority simultaneously

3. **Selling or hinting at a product** — Any whiff of a pitch in PLC #1 collapses trust. Zero. Mentions. Of. Product

4. **Abstract transformation** ("better life," "more success") — If they can't visualize it specifically, they can't desire it

5. **Skipping the empathy layer in positioning** — Going straight to "I did X, Y, Z" without "I was where you are" creates distance, not trust

6. **No foreshadow of PLC #2** — Leaving the anticipation trigger unactivated. You lose the "I'll be back" commitment

7. **No call to action for comments** — The launch conversation never starts. Social proof, community, and real-time intelligence are all lost

8. **Ignoring objections** — They're thinking them anyway. Silence reads as avoidance, not confidence

9. **Trying to cover everything** — PLC #1 opens the story. It doesn't tell the whole story. Strategic restraint is essential

10. **Over-produced, under-authentic** — Polished production with no genuine energy or personality. People connect with humans, not productions

11. **Teaching theory instead of something actionable** — "Here's an interesting concept" vs. "Here's something you can do today" — only the second creates reciprocity

12. **Making the transformation feel unachievable** — If your story is too extraordinary, they disconnect with "I could never do that"

13. **Spending too long on positioning** — More than 20% of total time on "who I am" signals insecurity, not authority

14. **Flat emotional pacing** — Same energy from beginning to end. No arc = no engagement

15. **Ending weakly** — A strong video with a weak close is a missed opportunity. End with energy, specificity, and clear next steps

---

## POST-PRODUCTION CHECKLIST

### Final Quality Gate

- [ ] Zero mention of product, price, or offer anywhere
- [ ] Authority established through story, not claims
- [ ] Empathy comes before credentials
- [ ] At least one genuinely valuable teaching moment included
- [ ] Transformation feels achievable, not aspirational fantasy
- [ ] Clear foreshadow of PLC #2 creates anticipation
- [ ] CTA is present and specific
- [ ] Audio is clear and audible
- [ ] Video quality is acceptable
- [ ] Length is appropriate (8-15 minutes typical)

### Primary Mental Triggers Activated

- [ ] Authority (credentials through story)
- [ ] Reciprocity (free high-value content)
- [ ] Anticipation (foreshadow PLC #2)
- [ ] Likability (empathy, generosity, personal tone)

---

*Production Aid Version: 3.0*
*Source: Launch (Jeff Walker) - Original + Updated 2021 Edition*
*Framework: Product Launch Formula - PLC #1 Complete Guide*


---

<!-- plc2-complete-production-aid.md -->
# PLC #2 — THE TRANSFORMATION: COMPLETE PRODUCTION AID

> **Framework**: Product Launch Formula (Jeff Walker)
> **Theme**: "WHAT" — O que é essa transformação e como ela vai mudar a vida deles?
> **Source**: Launch (Original + Updated 2021 Edition)

---

## SECTION 1 — STRATEGIC FOUNDATION

**The single job of PLC #2:** Get your prospect to SEE THEMSELVES having the transformation you promised in PLC #1 — by teaching them something so valuable and actionable that they experience a real shift in how they view their situation.

**Success criteria:** When PLC #2 ends, the viewer thinks three things simultaneously:
1. "This actually works"
2. "I could do this"
3. "If the free content is this good, what's inside the paid version?"

### What PLC #2 Attacks Directly (The 4 Reasons People Don't Buy)

| Reason | Description | PLC #2 Action |
|--------|-------------|---------------|
| **#4** | "I believe the product works but not FOR ME" | **PRIMARY TARGET** — Demolished through actionable teaching, case studies, and objection crushing |
| **#3** | "I don't believe YOU" | **REINFORCED** — Authority deepened through demonstrated expertise (teaching), not claims |
| #1 | Not interested | PLF can't fix this |
| #2 | No money | PLF can't fix this |

### The Critical Distinction from PLC #1

| PLC #1 | PLC #2 |
|--------|--------|
| Shows the DESTINATION | Shows the VEHICLE |
| "Here's what's possible" | "Here's how it works" |
| Inspiration-heavy | Instruction-heavy |
| Opens the desire loop | Begins closing the "how" loop |
| Creates belief in the opportunity | Creates belief in THEMSELVES |
| Teaches at INSIGHT level | Teaches at TACTICAL level |

**Depth calibration:** PLC #1 taught at the INSIGHT level — a framework, a reframe, a new way of seeing. PLC #2 must teach at the TACTICAL level — a method, a process, a step-by-step, a specific technique. The difference: PLC #1 makes them think differently. PLC #2 makes them capable of acting differently.

### How PLC #2 Creates the "Implementation Gap"

PLC #2 sets up PLC #3 by creating the "implementation gap." The viewer now BELIEVES the transformation is real and SEES how it could work — but they also recognize they need more. They need the full system, the guidance, the structure. This gap is what PLC #3 will address before pivoting to the offer as the bridge that closes it.

---

## SECTION 2 — PRE-PRODUCTION RESEARCH

### Comment Mining from PLC #1

- [ ] Read EVERY comment from PLC #1 — not a sample, ALL of them
- [ ] Categorize PLC #1 comments into buckets:
  - **Enthusiasm/excitement:** "This is amazing, I can't wait for more"
  - **Specific questions:** "How does this work for [their specific situation]?"
  - **Objections/doubts:** "But what about [concern]?"
  - **Personal stories:** "I've been struggling with [problem] for [timeframe]"
  - **Requests:** "Can you show us how to [specific thing]?"
- [ ] Identify the TOP 5 questions asked (exact wording — these inform your teaching content)
- [ ] Identify the TOP 3 objections expressed (exact wording)
- [ ] Note which comments got the most likes/engagement
- [ ] Identify "hyper-responsive" commenters — these are your future buyers
- [ ] Extract exact language and phrases your audience uses — mirror these in PLC #2
- [ ] Note the emotional temperature: Is your audience fired up? Cautiously optimistic? Still skeptical? This calibrates your opening energy
- [ ] Look for patterns: What surprised them? What confused them? What excited them?
- [ ] Find 2-3 specific comments you can reference: "One of you wrote something that really hit me..."

### Objection Prioritization Matrix

| Objection | Frequency | Intensity | Address in PLC #2? |
|-----------|-----------|-----------|-------------------|
| [Fill in from comments] | High/Med/Low | High/Med/Low | Yes/No/Partial |

**Selection criteria:** Address objections that are:
- High frequency AND high intensity
- Blocking belief in the transformation (not belief in you — that was PLC #1)
- Addressable through teaching or case studies

### Teaching Selection for PLC #2

**The 5 Tests for Teaching Content Selection:**

Your teaching content must pass ALL of these tests:

- [ ] **Actionability test:** Can they DO something with this today? If it's purely conceptual, it fails
- [ ] **Shift test:** Does this change how they SEE their situation? Not just add information, but reframe their perspective or capabilities?
- [ ] **Proof test:** Does the act of teaching this demonstrate that the transformation is real and achievable? Does it serve as evidence, not just instruction?
- [ ] **Loop test:** Does this teaching naturally make them want MORE? Does it open the door to PLC #3's deeper content and ultimately the product?
- [ ] **Self-projection test:** After learning this, can the prospect see THEMSELVES executing it? Not "that's cool" but "I could do that"

**The Walker Standard:** Jeff taught the ENTIRE Seed Launch in ~18 minutes in PLC #2. People actually did Seed Launches from that free video. And they STILL bought.

### Case Study Selection (If Using)

- [ ] Case study subject is relatable to your audience (not too exceptional)
- [ ] Results are specific and verifiable
- [ ] Story includes struggle/obstacle (not just success)
- [ ] FTC compliance verified (if US market)
- [ ] Case study demonstrates the TRANSFORMATION, not just results

---

## SECTION 3 — EMOTIONAL ARCHITECTURE

### Emotional Starting Point (Two Viewer States)

The PLC #2 viewer is in one of two states:

| State | Description | Emotional Baseline |
|-------|-------------|-------------------|
| **Returning viewer** (watched PLC #1) | Engaged, cautiously hopeful, curious about what comes next, has some trust in you | **Interested and leaning in** |
| **New viewer** (missed PLC #1) | Neutral to slightly skeptical, needs orientation | **Curious but uncommitted** |

Your opening must serve BOTH — re-engage the returning viewer AND orient the new one — without boring either.

### The Minute-by-Minute Emotional Sequence

| Timing | Emotion | Viewer Thought | Caused By |
|--------|---------|----------------|-----------|
| Minute 0-1 | Recognition, validation | "They actually read my comment / heard my concern." | Thanking commenters, referencing real PLC #1 comments |
| Minute 1-2 | Re-activated hope | "Right, this is what excited me last time." | Quick recap of opportunity and positioning |
| Minute 2-3 | Eagerness, lean-forward | "Oh, they're going to actually SHOW me how." | Transition into teaching with clear promise |
| Minute 3-8 | Surprise → understanding → self-belief | "Wait... I didn't know that. That actually makes sense. I could do that." | Core teaching segment — tactical, concrete, step by step |
| Minute 8-10 | Relief, obstacle removal | "They're right — [objection] isn't really the problem I thought it was." | Objection crushing with specific evidence |
| Minute 10-12 | Heightened anticipation, impatience | "There's STILL more? What's in the next one?" | Foreshadow of PLC #3 with compelling tease |
| Minute 12-13 | Engagement, belonging | "I need to share what I'm thinking about this." | CTA with specific question |

### The Critical Emotional Shift

**The viewer must cross from "This is interesting" to "This is for me."**

That crossing happens during the teaching segment. If they finish PLC #2 still thinking "great content but I'm not sure it applies to my situation," the teaching wasn't concrete enough or relatable enough.

### Emotional Ending Point

- **Confident** — They believe the transformation is achievable
- **Energized** — They want the next video NOW
- **Grateful** — They feel they got real value for free
- **Quietly calculating** — "If the free content is this good, what's inside the paid version?"

---

## SECTION 4 — SCRIPT STRUCTURE (Beat by Beat with Copy Depth)

### THE OPENING: THANKS AND ENGAGEMENT (1-2 minutes)

**Why this matters:** You're transforming a broadcast into a conversation. When you reference their comments, you:
- Prove you're listening (trust)
- Make them feel seen (likability)
- Show social proof (others are engaged too)
- Create a reason for NEW viewers to comment (community)

#### Copy Framework: The Comment Callback

```
"Before I dive in today, I just have to say... the response to my last video blew me away.

[Option A — Quantity focus:]
I got over [number] comments, and I read every single one.

[Option B — Quality focus:]
Some of the questions you asked were incredible. [Name] asked about [specific question].
[Name] shared their story about [specific challenge].

What really struck me was how many of you mentioned [pattern]. That tells me I'm on the
right track — and it actually shaped what I'm going to share with you today..."
```

#### Comment Reference Patterns

| Reference Type | Example | Effect |
|---------------|---------|--------|
| Named reference | "[Name] asked about X..." | Personal, shows real engagement |
| Pattern reference | "So many of you mentioned X..." | Shows scale, normalizes the concern |
| Story reference | "One person shared that they've tried X three times..." | Creates connection |
| Question reference | "The most common question was X..." | Sets up the teaching |

#### Opening Mistakes to Avoid

- [ ] Don't skip the thank you — even if it feels awkward, it matters
- [ ] Don't make it TOO long — 60-90 seconds max, then move
- [ ] Don't thank generically — reference SPECIFIC comments or patterns
- [ ] Don't ignore objections that appeared — you'll address them later, but acknowledge you saw them
- [ ] Don't be fake enthusiastic — genuine appreciation beats performed excitement

---

### BEAT 1 — QUICK RECAP: OPPORTUNITY (30-60 seconds)

**The Walker Rule:** "NEVER assume prospects saw or paid attention to or remembered PLC #1. They have busy lives — your launch isn't nearly as important to them as it is to you."

#### Copy Framework: The 60-Second Reorientation

```
"If you missed my first video, let me catch you up quickly.

We're talking about [transformation/opportunity] — the possibility of [vivid "after" description].

I showed you why this is real and why it's working for people like [brief proof point].

Today, I'm going to go deeper. I'm going to show you [specific teaching preview]..."
```

#### Recap Calibration

| Element | PLC #1 Time | PLC #2 Recap |
|---------|-------------|--------------|
| The opportunity | 3-4 minutes | 30-45 seconds |
| Your positioning | 2-3 minutes | 15-20 seconds |
| The transformation | Expanded | Referenced |

**Principle:** Brief enough for returning viewers, complete enough for new ones.

---

### BEAT 2 — QUICK RECAP: POSITIONING (20-30 seconds)

Don't re-tell your story. Just remind them who you are in one or two sentences.

#### Copy Framework: The Authority Reminder

```
"As I mentioned, I've [brief credential reminder], and I've [result that proves expertise].

But more importantly, I've been exactly where you are today — and I found a way through."
```

#### Positioning Refresh Patterns

| Your situation | Positioning refresh |
|----------------|---------------------|
| Strong credentials | "I've helped [X people] do [Y result]..." |
| Experience-based | "After [X years] figuring this out..." |
| Results-based | "Since [my result], I've focused on..." |
| Research-based | "I've spent [X time] studying..." |

**Rule:** Trust is already building from PLC #1. Don't belabor this — move quickly to the teaching.

---

### BEAT 3 — THE CORE TEACHING (5-10 minutes)

This is the heart of PLC #2. Everything else supports this section.

#### The Teaching Philosophy

> "Don't just tease them — give them some substance. I have hundreds of people who have done successful launches just based on the free material I've given out during my prelaunch." — Jeff Walker

**The counterintuitive truth:** The more you give away, the more they want to buy. People who get results from your free content become your most enthusiastic paid customers.

#### What to Teach in PLC #2 (Selection Criteria)

**Ideal PLC #2 teaching:**
- **Actionable:** Something they can DO today
- **Complete:** Enough to generate a result (not just awareness)
- **Demonstrable:** You can show it, not just describe it
- **Loop-opening:** Creates natural desire for "what else" and "what next"
- **Objection-dissolving:** When they understand this, their doubts shrink

#### The 3 Teaching Structure Options

**Option A — The Single Method Deep Dive**

Teach one complete method, process, or technique in enough depth that they could execute it.

Structure:
1. Name the method/process
2. Explain WHY it works (the principle underneath)
3. Walk through it step by step
4. Show an example of it in action (case study, your own experience, or live demonstration)
5. Summarize: "If you did nothing else but [this method], you'd already [specific result]"

*When to use:* When you have one powerful methodology that perfectly embodies the transformation. Walker used this approach — teaching the entire Seed Launch in 18 minutes.

**Option B — The Common Mistakes Framework**

Show the 3-5 biggest mistakes people make and how to fix each one.

Structure:
1. "Most [audience] make [number] critical mistakes that keep them from [result]"
2. Mistake #1: What it is → Why it's damaging → How to fix it
3. Mistake #2: Same structure
4. Mistake #3: Same structure
5. "Fix these, and you're already ahead of [percentage] of [audience]"

*When to use:* When your audience has been trying and failing. This approach validates their effort ("you were on the right track") while showing why it didn't work ("but this specific thing was holding you back"). Barry Friedman used elements of this: "Here's what works and what doesn't work. And if you're making these common mistakes, here's how you fix them."

**Option C — The Before/After Transformation Walkthrough**

Take a real scenario and walk through the transformation live.

Structure:
1. "Let me show you what this looks like in practice"
2. Present the "before" state (relatable, specific)
3. Apply the method/principle step by step
4. Reveal the "after" state
5. "That's the difference between [before] and [after]. And the only thing that changed was [key insight]."

*When to use:* When you can do a live demonstration, a side-by-side comparison, or a concrete walkthrough. Barry did this powerfully: he actually reviewed entertainers' websites, showed the mistakes, and showed how to fix them.

---

#### The 4-Layer Teaching Structure (For Any Option)

**Layer 1 — The Setup (What most people get wrong):**
```
"Most people approach [topic] like this: [common approach].

And here's why that doesn't work: [specific reason].

I used to do this too, until I realized [insight]..."
```

**Layer 2 — The Framework/Method:**
```
"Here's what actually works. I call it [name if applicable].

It has [X] parts: [list them].

Let me walk you through each one..."
```

**Layer 3 — The Walkthrough:**
```
"The first part is [element].

Here's what that looks like in practice: [example/demonstration].

The key thing most people miss is [specific insight]..."
```

**Layer 4 — The Application:**
```
"So if you're dealing with [their situation], here's how you'd use this:

Step one: [specific action]
Step two: [specific action]
Step three: [specific action]

When you do this, what happens is [result]..."
```

#### Teaching Quality Checklist

- [ ] Is this genuinely useful on its own? (Not just a teaser)
- [ ] Could someone take action on this TODAY?
- [ ] Does it create an "aha" or "I never knew that" moment?
- [ ] Does it demonstrate your expertise by SHOWING, not claiming?
- [ ] Does it open a natural loop for "what else is there"?
- [ ] Is it concrete enough to apply, not just conceptual?
- [ ] Does it dissolve at least one major objection?

#### Teaching Mistakes to Avoid

- [ ] Don't teach theory without application — every concept needs a "here's how you use this"
- [ ] Don't withhold the "good stuff" — the fear of giving too much is almost always unfounded
- [ ] Don't make it about you — keep returning to THEIR situation and THEIR application
- [ ] Don't skip the demonstration — showing beats telling every time
- [ ] Don't assume they know the basics — brief context prevents confusion
- [ ] Don't teach too much — pick one powerful thing and go deep, not five things shallow

#### Barry Friedman's PLC #2 Teaching — Deconstructed

| Element | What Barry Did | Strategic Function |
|---------|---------------|-------------------|
| Revisited the pain | "What if this all falls apart and your parents were right?" | Re-opened the emotional wound to make the teaching feel urgent |
| Named the gap | "You need to treat it like a business... being great at your craft is only part of the equation" | Reframed the problem — their skill isn't the issue, their business approach is |
| Positioned the solution | "I've figured out how to do both — put on a great show AND build a great business" | Authority through accomplishment, not claim |
| Taught the actual methods | "Started teaching his audience the fundamental principles and methods of marketing themselves" | Real, tactical, actionable content — not teaser, not theory |
| No product mention | "No mention of a product. No hint of a sale. Just solid, great content" | Trust protected. Reciprocity maximized |

**Result:** Built authority and reciprocity simultaneously. Made prospects feel like they were already getting results. Demonstrated that selling yourself as a highly paid entertainer was a **learnable skill.**

---

### BEAT 4 — CASE STUDY (Optional but Powerful) (2-3 minutes)

If you have a case study, this is where it goes. If not, extend the teaching section.

#### Why Case Studies Work

They provide the proof that makes your prospect think: "If they did it, maybe I can too."

The power is in **relatability** — the more your case study subject resembles your prospect, the more powerful it is.

#### The 5-Part Case Study Structure

```
1. BEFORE: "When [Name] came to me, they were dealing with [specific struggle].
   They had tried [failed approaches] and were feeling [emotional state]."

2. OBSTACLE: "The biggest challenge was [specific obstacle].
   This is probably familiar to you if you've ever [relatable experience]."

3. SHIFT: "What changed was [specific insight or action].
   Once they understood [key concept], everything shifted."

4. ACTION: "Here's exactly what they did: [specific steps].
   The key was [specific element]."

5. AFTER: "Today, [Name] is [specific result].
   [Vivid detail that makes the transformation tangible]."
```

#### Case Study Selection Criteria

- [ ] Subject is relatable (not exceptionally talented or advantaged)
- [ ] Story includes real struggle (not just "I tried it and it worked")
- [ ] Results are specific and verifiable
- [ ] Transformation is the type your audience desires
- [ ] FTC compliant (if US market) — verify claims

#### The "Ordinary Person" Principle

> "If my case study seems too exceptional, my prospect thinks 'Good for them, but I could never do that.' If my case study seems like a regular person who figured it out, my prospect thinks 'If they can do it, maybe I can too.'"

---

### BEAT 5 — OBJECTION CRUSHING (2-4 minutes)

This is where you directly attack the belief: "This works, but not for ME."

#### Objection Strategy for PLC #2

In PLC #1, you RAISED objections. In PLC #2, you CRUSH them.

**The target:** The viewer who believes the opportunity is real but has specific doubts about their own ability to achieve it.

#### The 3-Step Objection Crush

**Step 1 — Name it explicitly:**
```
"Now, a lot of you mentioned in the comments something like: '[exact objection in their words].'

I hear this all the time. And I want to address it directly."
```

**Step 2 — Validate before destroying:**
```
"First, I get it. This is a real concern. When you've [related experience], it makes sense to wonder if [objection].

But here's what I've found..."
```

**Step 3 — Destroy with evidence:**
```
"The reality is [evidence that dismantles the objection].

[Example/story/data that proves the objection wrong].

What this means for you is [specific implication]..."
```

#### Detailed Copy Frameworks by Objection Type

**"I don't have time" objection:**
```
"One of the most common things I heard from you was 'I don't have time.' And I respect that —
your time is valuable. But here's what's interesting: [method/approach] actually takes LESS time
than what you're currently doing. The reason is [explanation]. [Case study person] was working
[long hours] and thought they couldn't add anything else. But when they applied [method], they
actually freed up [time] because [mechanism]."
```

**"My situation is different" objection:**
```
"Several of you said, 'This sounds great, but my [specific niche/situation] is different.'
Let me address that directly. [Method/principle] works because of [underlying mechanism that's
universal]. It doesn't matter if you're in [situation A] or [situation B] — the principle is
the same. Here's an example: [diverse case study that proves universality]."
```

**"I've tried before and failed" objection:**
```
"I know some of you have tried [approaches] before and they didn't work. I want you to hear
this: the problem wasn't you. The problem was [misdiagnosis of what went wrong]. Here's why
[your approach] is fundamentally different: [specific distinction]. And that distinction is
why [results]."
```

**"I'm not [experienced/technical/qualified] enough" objection:**
```
"Some of you told me you're worried you don't have enough [experience/skill/knowledge] for this.
Here's what I want you to know: [relatable example of someone who started with zero and achieved
the transformation]. The starting point doesn't determine the outcome — the method does. And the
method I'm going to share with you was designed specifically for people who are starting from
[their level]."
```

#### Common Objection Types Quick Reference

| Objection Type | Example | Destruction Strategy |
|----------------|---------|---------------------|
| Time | "I don't have time for this" | Show efficiency, show cost of NOT doing it |
| Skill | "I'm not tech-savvy / good at X" | Show how others without the skill succeeded |
| Past failure | "I've tried and failed before" | Show what was different, why this approach works |
| Unique situation | "My industry/market/situation is different" | Show diverse examples, principles that transcend specifics |
| Starting point | "I'm too far behind / don't have X" | Show people who started with less |
| Age | "I'm too old/young for this" | Show age-diverse success stories |

#### Objection Crushing Mistakes

- [ ] Don't dismiss objections — validate them first, then address them
- [ ] Don't be defensive — treat objections as intelligent questions, not attacks
- [ ] Don't create new objections — only address ones they actually have
- [ ] Don't try to crush every objection — pick 2-3 most important, promise to address others
- [ ] Don't be vague — specific examples beat general reassurances

---

### BEAT 6 — FORESHADOW PLC #3 (30-60 seconds)

This is where you install the anticipation trigger for the next video.

#### Copy Framework: The PLC #3 Tease

```
"In my next video, which is coming [timeframe], I'm going to show you [specific tease].

This is where things get really powerful because [reason it matters].

I'll also be revealing [additional tease] — and this is the piece that [specific impact].

Make sure you watch for that email because this next video is going to change how you think about [topic]."
```

#### What Makes a Powerful Foreshadow

| Element | Weak Example | Strong Example |
|---------|--------------|----------------|
| Specificity | "I'll share more" | "I'll show you the exact 5-step process" |
| Stakes | "It's going to be good" | "This is the piece that makes everything click" |
| Tease | "More great content" | "I'll reveal the biggest mistake I see people make — and it's probably the one you're making right now" |
| Urgency | "Check back soon" | "This next video is going to be released [date] — make sure you don't miss it" |

#### The Strategic Purpose

PLC #3 contains the PIVOT to the offer. Your foreshadow needs to set up:
- The expectation of more valuable content
- The anticipation of learning "how" (the complete picture)
- A natural transition toward the offer (without revealing there IS an offer)

---

### BEAT 7 — CALL TO ACTION (30-60 seconds)

#### Why the CTA Matters Even More in PLC #2

- **Deepening commitment:** They commented before, commenting again reinforces engagement
- **Different question:** You can now ask a more specific, deeper question
- **Objection surfacing:** The comments reveal what's still blocking them
- **Community building:** Returning commenters see familiar names, feel part of something
- **Content for PLC #3:** You'll reference these comments in the next video

#### CTA Question Progression

| PLC | Question Type | Example |
|-----|---------------|---------|
| PLC #1 | Broad, opening | "What's your biggest challenge with [topic]?" |
| PLC #2 | Deeper, specific | "After seeing this, what's the ONE thing that would need to change for you to [transformation]?" |

#### Copy Framework: The PLC #2 CTA

```
"Now I want to hear from you.

After watching this video, what's [specific question related to their transformation/objections]?

Drop your answer in the comments below. I read every single one, and I'll be responding.

And remember: my next video is coming [timeframe]. It's going to cover [callback to foreshadow].

See you in the comments."
```

#### Effective CTA Questions for PLC #2

- "What's the ONE thing holding you back from [transformation]?"
- "If this could work for you, what would be the first thing you'd do with [result]?"
- "What question do you still have after watching this?"
- "Where are you in your [topic] journey right now?"
- "What was your biggest 'aha' from today's video?"

---

## SECTION 5 — MENTAL TRIGGER ACTIVATION MAP

| Beat | Triggers Activated | Mechanism |
|------|-------------------|-----------|
| Thanks/Comments | **Social Proof**, **Likability**, **Events/Ritual** | Referencing comment volume + quality, reflecting community energy, showing this is a shared experience |
| Recap Opportunity | **Hope**, **Desire** (reactivated) | Quick re-painting of the "after" picture |
| Recap Positioning | **Authority** (reinforced) | Compressed credential reminder |
| Teaching | **Authority** (deepened), **Reciprocity** (maximized) | Proving expertise through demonstration. Giving massive value for free creates reciprocity imbalance |
| Case Study | **Social Proof**, **Trust** | Real proof from real people |
| Objections | **Trust** (deepened), **Likability** | Honesty about obstacles. Validating concerns before addressing them |
| Foreshadow | **Anticipation** (escalated) | Specific tease with higher stakes than PLC #1's foreshadow |
| CTA | **Community**, **Commitment/Consistency** | Deepened dialogue, micro-commitment through commenting |

### NEW Triggers Activated for the First Time in PLC #2

- **Social Proof** (through referencing PLC #1 comments — this wasn't possible before PLC #1)
- **Events/Ritual** (the launch is now becoming a recurring shared experience)

### Carry-Forward Triggers Reinforced/Compounded from PLC #1

- **Authority** — compounded by actual teaching (the strongest authority-builder)
- **Reciprocity** — compounded by even more free value (the imbalance grows)
- **Trust** — compounded by second contact and objection handling (familiarity + honesty)
- **Anticipation** — compounded by foreshadowing PLC #3 from a higher emotional baseline
- **Likability** — compounded by responding to comments and showing genuine care

**Cumulative effect by end of PLC #2:** The viewer trusts you (authority + repeated contact + honesty about objections), feels indebted to you (massive reciprocity from free teaching), sees themselves succeeding (teaching created self-projection), feels part of something (community through comments), and is eagerly waiting for PLC #3 (anticipation at its highest level yet). The invisible question forming: "If the free content is this good, what's in the paid version?"

---

## SECTION 6 — TIMING AND PACING GUIDE

**Total recommended duration:** 12-20 minutes

### Pacing Rhythm

| Section | % of Total | For 15-min video |
|---------|------------|------------------|
| Opening + Thanks | 5-10% | 0:45 - 1:30 |
| Recap Opportunity | 3-5% | 0:30 - 0:45 |
| Recap Positioning | 2-3% | 0:20 - 0:30 |
| Teaching (Core) | 35-50% | 5:00 - 7:30 |
| Case Study (optional) | 10-15% | 1:30 - 2:15 |
| Objection Crushing | 15-20% | 2:15 - 3:00 |
| Foreshadow PLC #3 | 3-5% | 0:30 - 0:45 |
| CTA | 3-5% | 0:30 - 0:45 |

**Pacing principle:** Teaching is the main event — spend most of your time there. The recaps are quick (viewers are oriented), and the objection crushing is focused (2-3 specific objections, not comprehensive).

---

## SECTION 7 — FORMAT AND PRODUCTION NOTES

### When to Switch Formats

| Section | Best Format | Why |
|---------|-------------|-----|
| Thanks/Opening | On camera | Personal, warm, connection |
| Recap | Either | Keep it quick |
| Teaching | Screen-capture OR demo | Visual aids help comprehension |
| Case Study | On camera OR slides with images | Personal stories feel better on camera |
| Objections | On camera | Sincerity matters, eye contact helps |
| Foreshadow | On camera | Energy, anticipation |
| CTA | On camera | Personal ask, invitation |

### The Hybrid Sweet Spot for PLC #2

1. Open on camera (thanks, warmth)
2. Brief recap on camera or slides
3. Teaching with screen-capture or visual demonstration
4. Case study with slides + photos or on camera
5. Objections on camera (sincerity)
6. Foreshadow and CTA on camera (energy)

---

## SECTION 8 — PLC #2 SELF-ASSESSMENT RUBRIC

After completing your PLC #2, score each dimension. **If any dimension scores below 3, revise before publishing.**

| Dimension | 1 (Weak) | 3 (Solid) | 5 (Exceptional) |
|-----------|----------|-----------|-----------------|
| Comment engagement | Generic thanks | References specific comments/patterns | Names individuals, shows impact on content |
| Recap efficiency | Too long (re-doing PLC #1) | Brief and clear | Perfect for new viewers, not boring for returning |
| Teaching depth | Teaser only, vague concepts | One actionable framework/method | Complete enough that some could succeed from this alone |
| Teaching clarity | Confusing, abstract | Clear and followable | "Aha" moment guaranteed, immediately applicable |
| Objection destruction | Ignored or dismissed | Top 2-3 addressed with evidence | Objections named, validated, and destroyed with specificity |
| Case study power | No case study or weak one | Relatable story with clear results | Viewer thinks "If they did it, I can too" |
| Foreshadow strength | Generic "stay tuned" | Specific tease of PLC #3 | Creates genuine anticipation, they'll watch for the email |
| CTA specificity | "Leave a comment" | Specific, answerable question | Question that reveals their situation and surfaces remaining objections |
| Zero pitch | Product mentioned or implied | No pitch but some "salesy" moments | Pure education and value, no hint of selling |
| Self-projection | Teaching is interesting | Viewer starts to see themselves succeeding | Complete belief shift: "This could work for ME" |
| Generosity calibration | Clearly holding back "the good stuff" | Solid content that feels fair | So generous the viewer is genuinely shocked they're getting this for free |
| Continuity with PLC #1 | Feels like a standalone video with no connection | References PLC #1 and builds on it | Seamlessly continues the story — returning viewers feel the momentum build |
| Emotional arc | Flat energy, feels like an information dump | Some emotional variation across beats | Clear arc: warmth → focus → insight → relief → anticipation |

**Minimum viable PLC #2:** Every dimension at 3 or above.
**Launch-winning PLC #2:** Teaching depth and self-projection at 5. No dimension below 3.

---

## SECTION 9 — TOP 15 PLC #2 MISTAKES (Ranked by Damage)

1. **Not giving enough value** — The #1 mistake. Being stingy with teaching destroys reciprocity and authority. Give more than feels comfortable.

2. **Teaching theory without application** — "Here's an interesting concept" vs. "Here's what you DO with this" — only the second creates value.

3. **Skipping the comment acknowledgment** — You had a conversation started. Ignoring it kills the community energy.

4. **Assuming they watched PLC #1** — Your launch is not as important to them as it is to you. Always recap.

5. **Ignoring objections** — They expressed doubts in comments. Ignoring them feels like you don't care or can't answer.

6. **Teaching too much breadth, not enough depth** — Five shallow topics < one topic with real depth. Go deep.

7. **No case study or a weak one** — Case studies are powerful proof. If you have one, use it. If you don't, the teaching needs to be even stronger.

8. **Not crushing objections specifically** — Vague reassurances ("Don't worry, it works") don't move the needle. Specific examples do.

9. **Weak foreshadow** — "Stay tuned for more" doesn't create anticipation. "Here's exactly what you'll learn" does.

10. **Same CTA question as PLC #1** — The conversation should DEEPEN, not repeat. Ask something new.

11. **Selling or hinting at a product** — Still too early. Any whiff of pitch collapses trust.

12. **Making the case study subject too exceptional** — If they can't relate, they can't project themselves.

13. **Flat energy throughout** — Teaching is interesting; connection is emotional. Vary the energy.

14. **Too long on recaps** — Get through them efficiently. The teaching is the main event.

15. **Not demonstrating the teaching** — Showing is more powerful than telling. Whenever possible, demonstrate.

---

## POST-PRODUCTION CHECKLIST

### Final Quality Gate

- [ ] Still zero mention of product, price, or offer anywhere
- [ ] Comments from PLC #1 are acknowledged and referenced
- [ ] Opportunity and positioning are recapped (briefly)
- [ ] Teaching is genuinely actionable — someone could apply this today
- [ ] Teaching goes DEEP, not wide — better one powerful thing than five surface things
- [ ] Case study (if used) is relatable and specific
- [ ] Top 2-3 objections are named, validated, and crushed with evidence
- [ ] PLC #3 is foreshadowed with specific, compelling tease
- [ ] CTA includes a deeper, more specific question than PLC #1
- [ ] Viewer can realistically SEE THEMSELVES having the transformation

### Primary Mental Triggers Activated

- [ ] Authority (deepened by actual teaching — demonstrated, not claimed)
- [ ] Reciprocity (massive value given — significant imbalance created)
- [ ] Trust (second contact, familiarity grows, you listened to comments)
- [ ] Social Proof (comments referenced, community visible)
- [ ] Anticipation (PLC #3 foreshadowed, loop opened)

### The Walker Test

> "If PLC #2 can get your prospect to SEE THEMSELVES having the transformation that you promised in PLC #1, then you've done your job."

Ask yourself: After watching this, does my prospect believe this could work FOR THEM — not just "in general" but specifically for their situation, with their constraints, starting from where they are?

If yes, you're ready.

---

## SECTION 10 — TRANSITION PROTOCOL: How PLC #2 Connects to PLC #3

### Story Threads That Must Remain Open

By the end of PLC #2, these loops should be open, creating pull toward PLC #3:

1. **The "Implementation Gap":** They know WHAT to do but need the full HOW (system, guidance, support). This gap is intentional — PLC #3 will address it before pivoting to the offer as the bridge that closes it.

2. **The "What's Next" Loop:** Your teaching gave them one powerful element. But they can sense there's more — a complete system/approach. PLC #3 will reveal the full picture.

3. **The "Is This For Me" Loop:** You crushed the top objections, but there are still lingering doubts. PLC #3 will address what remains AND show them an opportunity to get help.

4. **The "If the free content is this good..." Loop:** The silent question forming: "What's in the paid version?" This creates natural pull toward the offer that PLC #3 will reveal.

### Viewer's Psychological State at End of PLC #2

When they finish PLC #2, they should be in this state:

| Dimension | State |
|-----------|-------|
| **Belief in opportunity** | Strong (established in PLC #1, reinforced) |
| **Belief in YOU** | Strong (demonstrated through teaching) |
| **Belief in THEMSELVES** | Growing but not complete (the target for PLC #3) |
| **Curiosity** | High (what's the complete picture?) |
| **Reciprocity imbalance** | Significant (you've given massive value) |
| **Purchase intent** | Beginning to form, though no offer mentioned |
| **Trust** | Deep (two contacts, listened to their comments) |

**This psychological state becomes the STARTING POINT for PLC #3's emotional architecture.**

### Content From PLC #2 That Will Be Referenced in PLC #3

- [ ] Top comments and questions from PLC #2 (for the thanks/acknowledgment beat)
- [ ] Objections that were raised but promised to be addressed later
- [ ] New questions that emerged from the teaching
- [ ] Enthusiasm/excitement expressed (to reflect back energy)
- [ ] Specific names/stories that can be called back

### The Gap Between PLC #2 and PLC #3

**What happens in this gap:**

| Element | Action |
|---------|--------|
| **Email sequence** | 1-2 emails: Value-add, answer FAQ, build anticipation for PLC #3 |
| **Comment engagement** | Respond to comments, ask follow-up questions, surface objections |
| **Social media** | Continue conversation, share snippets, countdown to PLC #3 |
| **Anticipation building** | Tease PLC #3 content, create urgency to watch |

**Gap duration:** Typically 2-4 days.

**Monitor comment tone:** Are people asking increasingly specific questions? Are any asking about "how to get more help"? These are pre-buying signals that indicate the sequence is working.

**The gap should feel like:** The pause before the final act — tension building, not momentum losing.

### The Handoff Statement

The final moments of PLC #2 should set up PLC #3 perfectly:

```
"In my next video, I'm going to show you [the complete picture / the how / the deeper level].

I'll also be [addressing the questions you've been asking / revealing something I've never shared publicly /
showing you what this looks like when it all comes together].

This is the video where everything clicks — and where I'll share how you can [hint at the opportunity
without revealing the offer].

Watch for that email. It's coming [timeframe], and you don't want to miss it."
```

---

*Production Aid Version: 3.0*
*Source: Launch (Jeff Walker) - Original + Updated 2021 Edition*
*Framework: Product Launch Formula - PLC #2 Complete Guide*


---

<!-- plc3-complete-production-aid.md -->
# PLC #3 — THE OWNERSHIP EXPERIENCE: COMPLETE PRODUCTION AID

> **Framework**: Product Launch Formula (Jeff Walker)
> **Theme**: "HOW" — Como eles vão ter essa transformação? + PIVOT para a oferta
> **Source**: Launch (Original + Updated 2021 Edition)

---

## SECTION 1 — STRATEGIC FOUNDATION

**The single job of PLC #3:** Deliver peak teaching value while pivoting to the offer — transforming the prospect from "viewer" to "ready buyer" without losing trust.

**Success criteria:** When PLC #3 is done right, the viewer finishes thinking:
1. "This is the most valuable content I've seen — they really delivered"
2. "I can see exactly how this could work for me"
3. "Wait — there's a way to go even deeper? I want to know more about that offer"

### What PLC #3 Attacks Directly (The 4 Reasons People Don't Buy)

| Reason | Description | PLC #3 Action |
|--------|-------------|---------------|
| **#4** | "I believe the product works but not FOR ME" | **COMPLETED** — Full ownership of the transformation through big-picture projection |
| **#3** | "I don't believe YOU" | **CONSOLIDATED** — Peak authority through best teaching + honest transition to offer |
| #1 | Not interested | PLF can't fix this |
| #2 | No money | PLF can't fix this |

### How PLC #3 Connects to PLC #2

**Story thread picked up:**
- PLC #2 showed WHAT the transformation looks like (tactical depth)
- PLC #3 answers HOW — the complete picture, the full system, the ultimate possibility
- PLC #2 left the viewer thinking "I can see myself doing this"
- PLC #3 takes them to "I see exactly how my life changes AND there's help available"

### How PLC #3 Sets Up the Sales Video

**Story thread opened:**
- The pivot reveals an offer is coming (no surprise on Sales Video day)
- Scarcity is seeded (they know the offer is limited — builds urgency to watch)
- The offer is positioned as "the next level" (not a sales pitch, but a natural evolution)
- Viewer psychology shifts from "learning" to "ready to decide"

### The Critical Element: THE PIVOT

> "Making the pivot to the sale in the final piece of Prelaunch Content is CRITICAL, and leaving out that pivot is a mistake a lot of people make." — Jeff Walker

The pivot is NOT the sale. The pivot is the BRIDGE — transitioning from pure educator to "I have an offer for those ready to go deeper." Done right, it feels like a generous invitation, not a sales trick.

---

## SECTION 2 — PRE-PRODUCTION RESEARCH

### Sub-block A — Audience Intelligence (What You Need to KNOW)

**From PLC #1 & #2 comments:**
- [ ] Read EVERY comment from PLC #1 and PLC #2 — not samples, ALL of them
- [ ] Categorize comments into buckets:
  - **Enthusiasm/excitement:** "This is amazing, can't wait for more"
  - **Specific questions:** "How does X work for my situation?"
  - **Objections/doubts:** "But what about [concern]?"
  - **Personal stories:** "I've been struggling with [problem]"
  - **Buying signals:** "How can I work with you?" "When is this available?"
- [ ] Identify recurring questions (these become the FAQ section of PLC #3)
- [ ] Identify remaining objections not yet addressed
- [ ] Note the emotional tone shift: Are comments moving from "interesting" to "excited"?
- [ ] Identify hyper-responsives: Who's commented on BOTH videos? These are your prime buyers
- [ ] Look for the buying signal shift: Comments asking about "how to work with you" or "when is this available" = high purchase intent

**New insights needed:**
- [ ] What's the #1 question people STILL have after two PLCs?
- [ ] What objection keeps resurfacing even after being addressed?
- [ ] What language are they using to describe their desired transformation?
- [ ] Are they asking about price, details, "how to join"? These signal readiness for the offer

### Sub-block B — Content Clarity (What You Need to DECIDE)

**The core content choice: The Big Picture Teaching**

PLC #3 teaching must:
- [ ] Be the STRONGEST teaching of all three PLCs (save your best for last)
- [ ] Project into their future — what's REALLY possible if they go all in?
- [ ] Look at the transformation from all angles (financial, lifestyle, emotional, professional)
- [ ] Create the "maximum inspiration" moment just before the pivot

**The 5 Tests for PLC #3 Content Selection:**

Your Big View teaching must pass ALL of these tests:

- [ ] **Escalation test:** Is this STRONGER than PLC #2? (Save your best for last)
- [ ] **Vision test:** Does it make them feel the FULL possibility of the transformation across multiple life dimensions?
- [ ] **Ownership test:** After this, do they feel like the transformation is THEIRS to have? (Not just possible in general, but possible for THEM)
- [ ] **Bridge test:** Does it naturally lead to "I want help implementing this"? (Creates the gap the offer will fill)
- [ ] **Peak test:** Is this the moment of maximum inspiration in the entire sequence?

**What to include vs. hold back:**

| Include in PLC #3 | Hold for Product |
|-------------------|------------------|
| The complete framework/vision | The detailed implementation system |
| The "why it works" depth | The step-by-step walkthroughs |
| Case study proof | Personal coaching/support |
| Big-picture transformation | Tools, templates, done-for-you |

**Strategic restraint boundary:** 75% of PLC #3 is peak teaching. The final 25% is the pivot. Don't let the pivot leak into the teaching section.

### Sub-block C — Structural Preparation (What You Need to WRITE/BUILD Before Scripting)

**Critical copy elements to draft before scripting:**

1. **The Big View projection:**
   - [ ] Write the 2-3 paragraph vision of their transformed future (financial, lifestyle, emotional, professional angles)
   - [ ] Make it specific and vivid — not "better life" but concrete changes

2. **The Pivot transition language:**
   - [ ] Draft the exact sentences that transition from teaching to offer tease
   - [ ] Test for tone: Does it feel like "generous invitation" or "sales pitch"?
   - [ ] Include the soft landing: "If you're ready to take this to the next level..."

3. **The Scarcity seed:**
   - [ ] Draft the language that plants scarcity without hammering it
   - [ ] Be specific: limited spots? limited time? limited bonuses?
   - [ ] Verify: Is the scarcity REAL? (Fake scarcity destroys trust permanently)

4. **FAQ prep:**
   - [ ] List top 5-10 questions from PLC #1 and #2 comments
   - [ ] Draft clear, specific answers to each
   - [ ] Identify which to address in video vs. save for email/FAQ page

**Assets needed:**
- [ ] Case study (brief — PLC #3 has a lot of work to do)
- [ ] Data points that support the "big view" projection
- [ ] Testimonials/proof points (if available)
- [ ] Clear description of what the offer IS (you need to know it to tease it)

---

## SECTION 3 — EMOTIONAL ARCHITECTURE

### Emotional Starting Point (Where They Are When They Press Play)

PLC #3 viewers are NOT curious newcomers. They're INVESTED prospects:

| Baseline | Description |
|----------|-------------|
| **Trust level** | High — you've delivered twice, they feel they know you |
| **Anticipation** | Strong — they've been waiting for this video |
| **Belief in opportunity** | Solid — PLC #1 and #2 established this |
| **Belief in themselves** | Growing — this is what PLC #3 completes |
| **Purchase consideration** | Beginning — some are already thinking "how do I get more" |

### Emotional Arc Across PLC #3

| Timing | Emotion | Viewer Thought | Cause |
|--------|---------|----------------|-------|
| Minute 0-2 | Validation, belonging | "They saw my comment! This is my community." | Thanks and engagement callback |
| Minute 2-3 | Reorientation, recall | "Right, this is the journey we're on." | Brief recap |
| Minute 3-5 | Proof, confidence | "These results are real. People like me are doing this." | Case study |
| Minute 5-10 | Relief, resolution | "Finally! My specific question answered." | FAQ/objection section |
| Minute 10-15 | Inspiration, vision | "Oh wow... THIS is what's really possible?" | Big View projection |
| Minute 15-18 | Anticipation, desire | "Wait — there's a way to get help with this?" | The Pivot |
| Minute 18-20 | Urgency, readiness | "It's limited? I need to watch for that email." | Scarcity seed + CTA |

### The Critical Emotional Shift That Must Happen in PLC #3

**The viewer must cross from "I understand this" to "I want help with this."**

This shift happens in two stages:
1. **During the Big View:** They move from "I can see myself doing this" to "I WANT this transformation NOW"
2. **During the Pivot:** They move from "great free content" to "there's a way to go deeper and I want to know about it"

If they finish PLC #3 without wanting to see the offer, the Big View wasn't inspiring enough or the pivot wasn't compelling enough.

### Emotional Ending Point

When they finish PLC #3, they should feel:
- **Grateful** — You gave them more value than they expected
- **Inspired** — The full vision is clear and compelling
- **Ready** — "If there's an offer to help me do this, I want to see it"
- **Urgent** — "It's limited, I need to act when it opens"
- **Curious** — "What exactly IS the offer? What's included?"

**This emotional state becomes the starting point for the Sales Video.** Viewers will arrive at the Sales Video in a state of "ready eagerness" — not cold, not skeptical, but primed to make a decision.

---

## SECTION 4 — SCRIPT STRUCTURE (Beat by Beat with Copy Depth)

---

### BEAT 1 — THANKS AND EXCITEMENT (1-2 minutes)

#### 4a — Duration Target
- Time: 1-2 minutes
- Percentage: 5-8% of total

#### 4b — Strategic Purpose
Express genuine excitement about the community response AND reflect that excitement back to them. This beat transforms "your audience" into "our community."

#### 4c — Copy Framework

**Standard approach:**
```
"Wow. Before I dive into today's video, I have to tell you — the response to this series
has been incredible.

I've been reading through your comments, and [specific observation about the community energy].

[Name] wrote: '[actual comment or paraphrase]'
[Name] shared: '[actual story or question]'

I can feel the momentum building. And today... today is special.

This is the video where everything comes together."
```

**High-energy approach (for launches with strong engagement):**
```
"I am so fired up right now.

After reading through the hundreds of comments on my last two videos, seeing the questions
you're asking, the shifts you're already experiencing...

This community is ALIVE. And today, I'm going to give you the most valuable content
I've ever shared — the piece that makes everything click.

Let's go."
```

#### 4d — Examples / Deconstructions

| Walker Example | What He Did | Why It Worked |
|---------------|-------------|---------------|
| Referenced specific comment volume | "I got over 200 comments" | Social proof — others are engaged |
| Quoted individual comments | Named actual commenters | Personal recognition, deepens loyalty |
| Reflected excitement | "I can feel how excited you are" | Mirroring creates connection |
| Created event energy | "Today is special" | Ritual/event trigger activation |

#### 4e — Quality Control Checklist
- [ ] Do I reference specific comments or patterns from PLC #2?
- [ ] Does the energy level match or exceed PLC #2's opening?
- [ ] Have I made individuals feel seen (naming commenters if possible)?
- [ ] Does the opening create "event" energy — this video feels important?
- [ ] Am I expressing genuine excitement (not performed hype)?

#### 4f — Common Mistakes for This Beat
1. **Generic thanks** — "Thanks for watching" without specificity
2. **Skipping entirely** — Going straight to content loses community connection
3. **Fake enthusiasm** — Over-the-top energy that doesn't match your normal tone
4. **Too long** — More than 2 minutes loses momentum

---

### BEAT 2 — QUICK RECAP: OPPORTUNITY + POSITIONING (30-60 seconds)

#### 4a — Duration Target
- Time: 30-60 seconds
- Percentage: 3-5% of total

#### 4b — Strategic Purpose
Brief reorientation for new viewers or those who forgot. By PLC #3, this should be FAST — trust is established, they know you.

#### 4c — Copy Framework

```
"Quick reminder of where we are:

We're talking about [transformation/opportunity] — the possibility of [vivid one-line "after"].

In my first video, I showed you why this is real. In my second, I showed you what it
actually looks like in practice.

Today, I'm going to show you the complete picture — how this all comes together,
what's REALLY possible, and [tease for the pivot section].

Let's dive in."
```

#### 4d — Examples / Deconstructions

Barry Friedman's PLC #3 recap was minimal — by video three, his audience knew who he was and what the opportunity was. The recap was under 30 seconds.

#### 4e — Quality Control Checklist
- [ ] Is this under 60 seconds?
- [ ] Does it orient new viewers without boring returning ones?
- [ ] Does it connect all three videos into one arc?
- [ ] Does it tease what's unique about PLC #3?

#### 4f — Common Mistakes for This Beat
1. **Too long** — Re-doing PLC #1 and #2 loses momentum
2. **Too short** — New viewers get lost
3. **No arc connection** — Treating PLC #3 as standalone, not climax

---

### BEAT 3 — SHORT CASE STUDY (2-3 minutes, optional but powerful)

#### 4a — Duration Target
- Time: 2-3 minutes (if used)
- Percentage: 8-12% of total

#### 4b — Strategic Purpose
Concrete proof that the transformation is real and achievable for people like them. Keep it brief — PLC #3 has a lot of work to do.

#### 4c — Copy Framework

```
"Before I go deeper, let me show you what this looks like in practice.

[Name] came to me [timeframe] ago. They were dealing with [specific struggle that mirrors
your audience].

They had tried [failed approaches] and honestly, they were [emotional state].

What changed? [Specific insight or action that created the shift].

Today, [Name] is [specific result]. [One vivid detail that makes it tangible].

And here's what I want you to notice: [the principle this illustrates for your audience]."
```

#### 4d — Examples / Deconstructions

| Case Study Element | Effect | Why It Matters |
|-------------------|--------|----------------|
| Relatable starting point | "I was like them" belief | Projection becomes possible |
| Specific struggle | Emotional resonance | They see their own situation |
| Clear turning point | "That could be MY turning point" | Hope activation |
| Tangible result | Belief in the transformation | Proof the opportunity is real |

#### 4e — Quality Control Checklist
- [ ] Is the case study subject relatable (not exceptional)?
- [ ] Does the story include struggle, not just success?
- [ ] Are results specific and verifiable?
- [ ] FTC compliant (if US market)?
- [ ] Under 3 minutes? (PLC #3 can't afford a long case study)

#### 4f — Common Mistakes for This Beat
1. **Too long** — Steals time from big view and pivot
2. **Unrelatable subject** — "Exceptional" people don't create projection
3. **Results-only** — No struggle = no emotional connection
4. **Fabricated or vague** — Destroys trust if discovered

---

### BEAT 4 — ANSWER TOP RECURRING QUESTIONS (3-5 minutes)

#### 4a — Duration Target
- Time: 3-5 minutes
- Percentage: 15-20% of total

#### 4b — Strategic Purpose
Address the remaining objections and questions surfaced in PLC #1 and #2 comments. This is your final chance to clear the path before the pivot.

#### 4c — Copy Framework

**The Question Acknowledgment:**
```
"Now, I've been reading your comments carefully, and there are some questions that keep
coming up. I want to address them directly.

The first one I see a lot is: '[exact question from comments]'

Here's my answer: [direct, specific response].

Another one that came up multiple times: '[exact question]'

Here's what I've found: [evidence-based answer]..."
```

**The Objection Re-Crush:**
```
"I know some of you are still wondering about [objection that was addressed before but
keeps resurfacing].

I talked about this in my last video, but let me go deeper because it's important.

The reason this comes up so often is [validate the concern].

But here's what most people don't realize: [evidence that dissolves the objection].

[Example or story that proves the point]."
```

#### 4d — Examples / Deconstructions

Walker specifically notes: "Do this even if you've already raised and answered them in earlier PLC. People raise the same objections in different ways by asking different questions."

Why repetition works:
- They may not have seen the earlier answer
- Hearing it twice compounds belief
- Different framing reaches different people
- Shows you're thorough and listening

#### 4e — Quality Control Checklist
- [ ] Are questions/objections taken directly from comments (their words)?
- [ ] Are answers specific and evidence-based (not vague reassurances)?
- [ ] Are the TOP concerns addressed (not random questions)?
- [ ] Does this clear the final hurdles before they're asked to consider an offer?

#### 4f — Common Mistakes for This Beat
1. **Skipping because "I already addressed it"** — Repetition is strategic
2. **Generic answers** — "Don't worry, it works" doesn't move the needle
3. **Defensive tone** — Objections are questions, not attacks
4. **Too many questions** — Pick the top 3-5, not everything

---

### BEAT 5 — THE BIG VIEW: Maximum Inspiration (3-5 minutes)

#### 4a — Duration Target
- Time: 3-5 minutes
- Percentage: 15-20% of total

#### 4b — Strategic Purpose
Step back and show the FULL possibility of the transformation. This is the moment of maximum inspiration — the peak before the pivot.

> "Step back and look at what's really possible. What's the ultimate transformation or change they can have if they buy? Look at it from all angles and project out into their future." — Jeff Walker

#### 4c — Copy Framework

**The Multi-Angle Projection:**
```
"Now I want to step back and look at the full picture. What's really possible here.

FINANCIALLY: Imagine [specific financial transformation]. Not 'more money' in the abstract —
I'm talking about [vivid, specific scenario].

PROFESSIONALLY: Think about what it would mean to [professional transformation].
To wake up knowing [specific shift in their work life].

EMOTIONALLY: Consider the feeling of [emotional transformation]. No more [current pain].
Instead, [desired state].

IN YOUR RELATIONSHIPS: What happens when [relational transformation]? When you're no longer
[current constraint] and instead you're [desired state].

THIS is what we're really talking about. Not just [surface benefit] — but a complete
shift in how you experience [relevant life domain]."
```

**The "What If" Frame:**
```
"What if, six months from now, you looked back and realized THIS was the turning point?

What if the things you're learning in these videos are the beginning of [transformation]?

What if [specific achievable milestone] became your reality?

I've seen it happen for [reference case studies]. I've experienced it myself [if applicable].

And I believe it's possible for you too — not because of hype or wishful thinking,
but because [specific reason based on what you've taught]."
```

#### 4d — Examples / Deconstructions

The Big View works because it:
- Activates all senses (vivid, specific scenarios)
- Covers multiple life dimensions (financial, emotional, relational)
- Projects into their future (makes them feel the transformation as real)
- Creates desire before the offer is even mentioned

#### 4e — Quality Control Checklist
- [ ] Does the vision cover multiple life dimensions (not just one benefit)?
- [ ] Is each scenario specific and vivid (not abstract)?
- [ ] Does it feel achievable, not fantasy?
- [ ] Does it create genuine desire/longing before the pivot?
- [ ] Is it grounded in what you've taught (not random promises)?

#### 4f — Common Mistakes for This Beat
1. **Abstract benefits** — "Better life" vs. specific scenarios
2. **Single dimension** — Only talking about money when transformation is broader
3. **Hype without grounding** — Big claims without connection to the teaching
4. **Too short** — Rushing to the pivot loses the inspiration peak
5. **Crossing into pitch** — The Big View is about THEIR vision, not your product

---

### BEAT 6 — THE PIVOT: Soft Landing to the Offer (2-3 minutes)

#### 4a — Duration Target
- Time: 2-3 minutes
- Percentage: 10-15% of total
- **Timing:** Last 10-25% of the video (Walker originally said 25%, updated edition says last 10%)

#### 4b — Strategic Purpose
Transition from educator to offer-maker WITHOUT losing trust. This is the BRIDGE — not the sale, not a pitch, but a generous invitation.

> "You don't want to go from being their best friend in one video to a used-car salesman in the next." — Jeff Walker

#### 4c — Copy Framework

**The Bridge Approach:**
```
"So here's where we are.

Over these three videos, I've shown you [summary of what you've covered].

I've given you [specific elements] — content that some people have used to [results
achieved from free content alone].

And if that's enough for you, amazing. Take what you've learned and run with it.

But I know that for some of you, you're thinking: 'This is incredible — but I want
more. I want help implementing this. I want support.'

If that's you, I have something coming that you're going to want to see."
```

**The "For Those Ready" Approach:**
```
"Now, what I've shared in these videos is real and valuable. But I've only been able
to scratch the surface.

The truth is, [what the product provides that free content can't].

And that's why I've created [product name or description].

In my next video, I'm going to share all the details — what's included, how it works,
and who it's for.

If you're ready to take this to the next level — if you're not just interested but
COMMITTED to [transformation] — then you'll want to watch that video."
```

**The Soft Landing:**
```
"I want to be clear: this isn't for everyone.

If you're happy with what you've learned and want to go implement on your own,
I fully support that. These videos were designed to give you real value, and they have.

But if you're someone who wants [deeper benefit], who wants [additional support],
who's ready to [commitment level]...

Then what I'm going to share next is exactly for you."
```

#### 4d — Examples / Deconstructions

**Barry Friedman's Pivot (Deconstructed):**

| What He Said | What It Accomplished |
|--------------|---------------------|
| "I'm going to personally guide 15 people through my Showbiz Blueprint" | First mention of upcoming product |
| "...which was the exact promotional system that helped land the highest-paying gigs" | Positioned product as proven system |
| "...including Johnny Carson and The White House" | Authority reinforcement through results |
| "This was the first mention of an upcoming product, the first hint that there was a sale coming" | Soft landing — no hard sell, just announcement |

**What made it work:**
- Came after peak teaching value (he'd just done live website reviews)
- Positioned as "personal guidance" (not just content)
- Limited spots (15 people) — scarcity seeded naturally
- Connected to his credentials through story, not claims

#### 4e — Quality Control Checklist
- [ ] Does the pivot come AFTER peak teaching (not before)?
- [ ] Does it feel like a generous invitation, not a sales pitch?
- [ ] Is there a soft landing (acknowledging the free content has value on its own)?
- [ ] Is the product positioned as "next level" (not replacement for free content)?
- [ ] Does it create curiosity about the offer without revealing all details?
- [ ] Is it clear there's a video coming with the full offer?

#### 4f — Common Mistakes for This Beat
1. **Skipping the pivot entirely** — The #1 PLC #3 mistake according to Walker
2. **Pivoting too early** — Before delivering peak value destroys trust
3. **Going full sales mode** — Pivot is a bridge, not a pitch
4. **Abrupt tonal shift** — "Best friend → used car salesman" effect
5. **Apologizing for having an offer** — Undermines authority and value
6. **Revealing full offer details** — Save that for the Sales Video

---

### BEAT 7 — SEED THE SCARCITY (30-60 seconds)

#### 4a — Duration Target
- Time: 30-60 seconds
- Percentage: 3-5% of total

#### 4b — Strategic Purpose
Plant the awareness that the offer is LIMITED without hammering it. They haven't seen the offer yet — scarcity here is about creating urgency to WATCH the Sales Video.

#### 4c — Copy Framework

**Limited Spots:**
```
"One thing I should mention: this isn't going to be available to everyone.

I can only work with [number] people, and based on the response to these videos,
I know there will be more demand than spots.

So if you're interested, make sure you watch for my next email."
```

**Limited Time:**
```
"This offer will only be available for [timeframe]. After that, [consequence].

If you want in, you'll need to act during the [launch window name].

Watch for that email — it's coming [timeframe]."
```

**Limited Bonuses:**
```
"I'll also be including some special bonuses that are only available during this launch.

These won't be part of the offer later — they're exclusively for people who join now.

I'll tell you all about them in my next video."
```

#### 4d — Examples / Deconstructions

**Why Scarcity Works Here:**
- Creates urgency to watch the Sales Video (not to buy — they haven't seen the offer)
- Plants the "I might miss out" awareness
- Positions the launch as an EVENT (not just another sales pitch)
- Primes them to act quickly when the cart opens

**The Walker Warning:**
> "The scarcity MUST BE REAL. If you say the offer closes, it CLOSES."

Fake scarcity destroys trust permanently. Only seed scarcity you can back up.

#### 4e — Quality Control Checklist
- [ ] Is the scarcity REAL? (Critical — no fake urgency)
- [ ] Is it mentioned, not hammered? (They haven't seen the offer yet)
- [ ] Does it create urgency to WATCH the Sales Video?
- [ ] Is the specific type of scarcity clear (time, spots, bonuses)?
- [ ] Does it feel like information sharing, not manipulation?

#### 4f — Common Mistakes for This Beat
1. **Fake scarcity** — Will destroy trust when discovered
2. **Hammering it** — Too much urgency before they see the offer feels pushy
3. **Vague scarcity** — "Limited" without specifics doesn't motivate
4. **Skipping it** — Loses urgency, lower Sales Video attendance
5. **Over-explaining** — Keep it brief, save details for Sales Video

---

### BEAT 8 — CALL TO ACTION (30-60 seconds)

#### 4a — Duration Target
- Time: 30-60 seconds
- Percentage: 3-5% of total

#### 4b — Strategic Purpose
Final engagement ask + transition setup for Sales Video.

**Watch for the buying signal shift:** In PLC #3 comments, you should see questions moving from content ("How does X work?") to offer ("How much is it? When can I sign up?"). This means the pivot worked.

#### 4c — Copy Framework

```
"Before I go, I want to hear from you.

After watching these three videos, [specific question that surfaces their readiness].

Drop your answer in the comments. I'm reading every single one.

And remember: my next video is coming [timeframe]. This is the one where I'll share
all the details about [offer description].

If you're ready to [transformation], you don't want to miss it.

See you soon."
```

**CTA Questions That Surface Buying Intent:**
- "What would it mean for you to finally [achieve transformation]?"
- "If you could get personalized help with this, what would you want the most?"
- "What's the ONE thing you'd want to accomplish if you had support?"
- "After everything you've seen, what's still holding you back?"

#### 4e — Quality Control Checklist
- [ ] Does the CTA question surface buying intent?
- [ ] Is there a clear callback to the upcoming Sales Video?
- [ ] Does it create anticipation for the offer reveal?
- [ ] Does it maintain the event energy of the launch?

#### 4f — Common Mistakes for This Beat
1. **Same question as previous PLCs** — Conversation should deepen
2. **No Sales Video preview** — They need to know what's coming
3. **Weak close** — Ending with low energy loses momentum
4. **Forgetting comment CTA** — Comments reveal buying signals

---

## SECTION 5 — MENTAL TRIGGER ACTIVATION MAP

| Beat | Triggers Activated | Mechanism |
|------|-------------------|-----------|
| Thanks + Excitement | **Community**, **Likability**, **Social Proof** | Showing the tribe, naming individuals, reflecting energy |
| Quick Recap | **Anticipation**, **Ritual** | "This is where it all comes together" — peak moment framing |
| Case Study | **Social Proof**, **Trust** | Real proof from real people |
| Answer Questions | **Trust**, **Likability** | Showing you listened, addressing concerns honestly |
| Big View | **Anticipation**, **Desire** | Maximum vision of the transformation |
| The Pivot | **Anticipation**, **Authority** | Revealing there's more, positioning as guide |
| Seed Scarcity | **Scarcity** (seeded) | Limited nature of offer planted |
| CTA | **Community**, **Commitment** | Final engagement, preparing for decision |

### Cumulative Effect by End of PLC #3

By the end of this video, the viewer has experienced:
- **Authority** — Compounded through three videos of demonstrated expertise
- **Reciprocity** — Massive imbalance created through peak value delivery
- **Trust** — Deep relationship from three high-quality interactions
- **Social Proof** — Visible community, case studies, engagement
- **Anticipation** — Maximum (they're waiting for the offer)
- **Scarcity** — Seeded (awareness that offer is limited)
- **Community** — Strong (they feel part of something)
- **Events/Ritual** — Launch day is an EVENT, not just a sales pitch

**Psychological state:** Ready to receive an offer, primed to act, trusting you completely.

### New Triggers in PLC #3 (vs. Previous)

| Trigger | PLC #1 | PLC #2 | PLC #3 |
|---------|--------|--------|--------|
| Scarcity | None | None | **Seeded** (first time) |
| Events/Ritual | Beginning | Growing | **Peak** (launch day feels important) |
| Anticipation | For PLC #2 | For PLC #3 | **For the offer** (biggest shift) |

---

## SECTION 6 — TIMING AND PACING GUIDE

**Total recommended duration:** 15-25 minutes

### When Shorter vs Longer is Appropriate

**Shorter (~15-18 min) is appropriate when:**
- Your market has shorter attention spans
- The Big View can be painted quickly (simpler transformation)
- You have fewer recurring questions to address
- The pivot is straightforward

**Longer (~20-25 min) is appropriate when:**
- The Big View requires multiple angles to be compelling
- You have many recurring questions from comments that need addressing
- The case study deserves more time for impact
- Your audience is highly engaged and hungry for depth
- The pivot needs careful setup (high-ticket offer, skeptical market)

### Percentage Allocation Table

| Section | % of Total | For 20-min video |
|---------|------------|------------------|
| Thanks + Excitement | 5-8% | 1:00 - 1:30 |
| Quick Recap | 3-5% | 0:30 - 1:00 |
| Case Study (optional) | 8-12% | 1:30 - 2:30 |
| Answer Questions | 15-20% | 3:00 - 4:00 |
| Big View | 15-20% | 3:00 - 4:00 |
| The Pivot | 10-15% | 2:00 - 3:00 |
| Seed Scarcity | 3-5% | 0:30 - 1:00 |
| CTA | 3-5% | 0:30 - 1:00 |

### Pacing Rhythm

```
START: High energy (thanks, excitement, community)
   ↓
MIDDLE: Substantive (case study, Q&A) — authoritative, helpful tone
   ↓
PEAK: Maximum inspiration (Big View) — emotional high point
   ↓
TRANSITION: Measured but confident (Pivot) — sincere, generous
   ↓
CLOSE: Urgent but warm (Scarcity, CTA) — anticipation, invitation
```

### Comparison to Previous PLCs

| Element | PLC #1 | PLC #2 | PLC #3 |
|---------|--------|--------|--------|
| **Opening energy** | Curious | Engaged | Excited |
| **Recap length** | N/A | 60 sec | 30 sec |
| **Teaching portion** | 40% | 50% | 35% (Big View replaces some teaching) |
| **New elements** | None | None | Pivot + Scarcity seed |
| **Closing energy** | Anticipation (for PLC #2) | Anticipation (for PLC #3) | Anticipation (for OFFER) |

---

## SECTION 7 — FORMAT AND PRODUCTION NOTES

### Best Format for PLC #3

| Section | Recommended Format | Why |
|---------|-------------------|-----|
| Thanks + Excitement | **On camera** | Personal energy, community connection |
| Quick Recap | Either | Keep it brief |
| Case Study | **On camera** or slides with images | Stories feel better on camera |
| Answer Questions | **On camera** | Sincerity, eye contact matters |
| Big View | **On camera** | This is the emotional peak — human connection is essential |
| The Pivot | **On camera** (critical) | Authenticity is everything for the pivot |
| Scarcity + CTA | **On camera** | Personal invitation, warm close |

**Key insight:** PLC #3 is the MOST personal video. The pivot requires trust and authenticity that screen-capture can't deliver. Go on camera for the pivot and Big View at minimum.

### Unique Production Considerations for PLC #3

1. **The pivot must feel natural:** Practice the transition language until it feels conversational, not scripted
2. **Big View requires visual imagination:** Some creators use subtle music or imagery to enhance the vision projection
3. **Energy management:** This is a longer video with an emotional arc — pace your energy
4. **Lighting/framing for pivot:** Some creators shift framing slightly for the pivot (closer, more intimate) to signal the tonal shift

### Minimum Viable Production Quality

Same as PLC #1 and #2 — clear audio, acceptable video. But for PLC #3 specifically:
- The pivot section should be your BEST on-camera delivery
- If you can only improve production for one section, improve the pivot

---

## SECTION 8 — SELF-ASSESSMENT RUBRIC

| Dimension | 1 (Weak) | 3 (Solid) | 5 (Exceptional) |
|-----------|----------|-----------|-----------------|
| **Community reflection** | Generic thanks | References specific comments/patterns | Creates "I'm part of this" feeling |
| **FAQ quality** | Generic answers | Specific, evidence-based answers | Viewer thinks "they really heard me" |
| **Big View power** | Abstract benefits | Multi-dimensional, specific vision | Creates genuine longing for the transformation |
| **Pivot naturalness** | Abrupt, salesy | Smooth but noticeable transition | Feels like generous invitation, not pitch |
| **Pivot timing** | Too early (before value) or too late (rushed) | Appropriate placement | Peak value delivered, then perfect bridge |
| **Scarcity authenticity** | Fake or missing | Real but briefly mentioned | Real, specific, creates urgency without manipulation |
| **Teaching peak** | Same as PLC #2 | Stronger than previous | Best content of the sequence (escalation achieved) |
| **Offer positioning** | Full sales pitch | "Next level" framing | Product feels like natural evolution, not hard sell |
| **Zero full pitch** | Reveals price/details | Teases without full reveal | Creates curiosity, leaves Sales Video work to do |
| **Buying signal indicators** | No shift in comments | Some offer questions | Comments shift from content to offer questions |
| **Emotional arc** | Flat energy throughout | Builds to Big View peak, then graceful pivot | Clear crescendo to inspiration, smooth transition to anticipation |
| **Continuity with PLC #2** | Feels disconnected | References PLC #2, builds on teaching | Seamless continuation — returning viewers feel the arc complete |

**Minimum viable PLC #3:** Every dimension at 3 or above.
**Launch-winning PLC #3:** Most dimensions at 4-5, no dimension below 3.

**Unique PLC #3 threshold:** The pivot dimension MUST be 4 or above. A weak pivot is the #1 PLC #3 failure mode. The Big View power dimension should also be 4+ for maximum conversion.

---

## SECTION 9 — TOP MISTAKES (Ranked by Damage)

1. **Skipping the pivot entirely** — The #1 PLC #3 mistake. Walker explicitly calls this out: "Leaving out that pivot is a mistake a lot of people make." You must bridge to the offer.

2. **Pivoting before peak value** — Transitioning to the offer before delivering your best teaching destroys trust. Give the value FIRST, then pivot.

3. **Used-car salesman transition** — Going from warm educator to aggressive seller creates whiplash. The pivot must feel like a generous invitation.

4. **Fake scarcity** — Saying the offer is limited when it's not will destroy your reputation. Scarcity must be REAL.

5. **Revealing full offer details** — PLC #3 teases the offer, it doesn't present it. Save price, bonuses, and full details for the Sales Video.

6. **Weak Big View** — Abstract benefits ("better life") instead of specific, multi-dimensional vision. This is the emotional peak — don't waste it.

7. **Not answering recurring questions** — Objections that keep appearing in comments need to be addressed directly, even if you've addressed them before.

8. **Teaching regression** — PLC #3 teaching should be your STRONGEST, not weaker than PLC #2. Escalation principle must hold.

9. **Apologizing for the offer** — "I hope you don't mind that I have something to sell" undermines your authority. You've earned the right to make an offer.

10. **No scarcity seed** — Without scarcity awareness, there's no urgency to watch the Sales Video immediately.

11. **Skipping community acknowledgment** — After two videos of building community, ignoring their engagement in PLC #3 feels like abandonment.

12. **Case study too long** — PLC #3 has a lot of work to do. A 10-minute case study steals time from the pivot.

13. **Flat emotional arc** — PLC #3 should build to a peak (Big View) then transition gracefully. Same energy throughout loses impact.

14. **CTA that doesn't surface buying intent** — Ask questions that reveal readiness to buy, not just general engagement.

15. **No callback to Sales Video** — End must create anticipation for the offer reveal. Don't just say "see you next time."

---

## SECTION 10 — TRANSITION PROTOCOL: How PLC #3 Connects to the Sales Video

### Story Threads That Must Remain Open

By the end of PLC #3, these loops should be open, creating pull toward the Sales Video:

1. **The "What's the Offer" Loop:** You've teased that there's a way to go deeper. They want to know exactly what it is, what it includes, and what it costs.

2. **The "Am I Right for This" Loop:** You've described who the offer is for ("those ready to take this to the next level"). They're wondering if they qualify.

3. **The "What's the Deadline" Loop:** You've seeded scarcity (limited spots/time/bonuses). They want to know exactly when they need to decide.

4. **The "Will I Miss Out" Loop:** The combination of value delivered + scarcity seeded creates urgency to watch the Sales Video immediately.

### Viewer's Psychological State at End of PLC #3

| Dimension | State |
|-----------|-------|
| **Belief in opportunity** | Complete (established across all three PLCs) |
| **Belief in YOU** | Complete (demonstrated through teaching, deepened through listening) |
| **Belief in THEMSELVES** | Strong (Big View created ownership of the transformation) |
| **Purchase intent** | Forming (they know there's an offer, they want to see it) |
| **Urgency** | Activated (scarcity seeded, they don't want to miss out) |
| **Readiness** | Ready to decide (not to buy yet, but to evaluate) |
| **Trust** | Peak (three high-value interactions, no sales pressure) |

**This psychological state becomes the STARTING POINT for the Sales Video.**

### Content From PLC #3 That Will Be Referenced in Sales Video

- [ ] The Big View vision (callback to what they'll achieve)
- [ ] Objections addressed (can be briefly referenced as "I already answered this")
- [ ] Community energy (reference the comments, the excitement)
- [ ] The transformation arc (everything you've shown them across 3 videos)

### The Gap Between PLC #3 and Sales Video

**What happens in this gap:**

| Element | Action |
|---------|--------|
| **Email sequence** | 1-2 emails: Final anticipation building, "tomorrow is the day" energy |
| **Comment monitoring** | Watch for buying signal questions (price, details, "when can I join?") |
| **Scarcity reminder** | Email may include scarcity callback ("remember, this is limited") |
| **Expectation setting** | "Watch for my email tomorrow — this is where I'll share everything" |

**The gap serves:** To let anticipation peak. The shorter this gap, the hotter the leads. Many launches do PLC #3 → Sales Video within 24-48 hours.

### The Handoff Statement

The final moments of PLC #3 should set up the Sales Video perfectly:

```
"My next video is the one where I share everything.

What's included. How it works. Who it's for. And how you can join.

It's coming [timeframe], and based on what I've seen from this community,
spots are going to go fast.

Watch for that email. This is the one you don't want to miss.

See you soon."
```

---

*Production Aid Version: 3.0*
*Source: Launch (Jeff Walker) - Original + Updated 2021 Edition*
*Framework: Product Launch Formula - PLC #3 Complete Guide*


---

<!-- post-launch-analysis.md -->
# Post-Launch Analysis Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Analyze launch performance and document learnings
> **Timing**: Complete within 7 days of cart close

---

## Revenue Analysis

### Final Numbers
| Metric | Result |
|--------|--------|
| Gross Revenue | R$ |
| Total Sales | |
| Average Order Value | R$ |
| Payment Plan Sales | |
| Full Pay Sales | |
| Refunds | |
| Net Revenue | R$ |

### Revenue by Day
| Day | Sales | Revenue | % of Total |
|-----|-------|---------|------------|
| Day 1 | | R$ | % |
| Day 2 | | R$ | % |
| Day 3 | | R$ | % |
| Day 4 | | R$ | % |
| Day 5 | | R$ | % |
| **Total** | | **R$** | **100%** |

### Jeff's Benchmark Check
- [ ] Day 1 = ~25% of sales
- [ ] Last Day = ~50% of sales
- [ ] Pattern matches: [ ] Yes / [ ] No

---

## List Performance

### List Metrics
| Metric | Result |
|--------|--------|
| Launch list size | |
| Engaged subscribers (opened 1+ email) | |
| Buyers | |
| Conversion rate | % |
| Earnings per subscriber | R$ |

### Email Performance Summary
| Email | Opens | Open Rate | Clicks | CTR |
|-------|-------|-----------|--------|-----|
| PLC1 Announce | | % | | % |
| PLC2 Announce | | % | | % |
| PLC3 Announce | | % | | % |
| Cart Open #1 | | % | | % |
| Cart Open #2 | | % | | % |
| Case Study | | % | | % |
| FAQ | | % | | % |
| Final Day #1 | | % | | % |
| Final Day #2 | | % | | % |
| Final Day Final | | % | | % |

### Best Performing Emails
1. _______ (___% open, ___% click)
2. _______ (___% open, ___% click)
3. _______ (___% open, ___% click)

### Worst Performing Emails
1. _______ (___% open, ___% click)
2. _______ (___% open, ___% click)

---

## Traffic Analysis

### Traffic Sources
| Source | Visitors | Sales | Conv Rate |
|--------|----------|-------|-----------|
| Email | | | % |
| Organic Social | | | % |
| Paid Ads | | | % |
| Affiliates | | | % |
| Direct | | | % |
| **Total** | | | **%** |

### Sales Page Performance
| Metric | Result |
|--------|--------|
| Total page views | |
| Unique visitors | |
| Add to cart | |
| Checkout initiated | |
| Purchases completed | |
| Page conversion rate | % |
| Cart abandonment rate | % |

---

## PLC Performance

### PLC Metrics
| PLC | Views | Engagement | Lead to Sale |
|-----|-------|------------|--------------|
| PLC1 | | comments | % |
| PLC2 | | comments | % |
| PLC3 | | comments | % |

### PLC Quality Assessment
| Criteria | PLC1 | PLC2 | PLC3 |
|----------|------|------|------|
| Hook effectiveness | /5 | /5 | /5 |
| Value delivered | /5 | /5 | /5 |
| Engagement created | /5 | /5 | /5 |
| Anticipation built | /5 | /5 | /5 |

---

## Objection Analysis

### Objections Encountered
| Objection | Frequency | Addressed In | Resolution Rate |
|-----------|-----------|--------------|-----------------|
| | | | |
| | | | |
| | | | |
| | | | |

### Objections to Better Address Next Time
1.
2.
3.

---

## Refund Analysis

### Refund Data
| Metric | Result |
|--------|--------|
| Total refunds | |
| Refund rate | % |
| Refund reasons | |
| Timing of refunds | |

### Refund Reasons Breakdown
| Reason | Count | % |
|--------|-------|---|
| Changed mind | | |
| Didn't meet expectations | | |
| Financial reasons | | |
| Wrong fit | | |
| Other | | |

### Learnings from Refunds
-
-

---

## Support Analysis

### Support Volume
| Metric | Result |
|--------|--------|
| Total tickets | |
| Pre-purchase questions | |
| Purchase issues | |
| Post-purchase questions | |
| Average response time | |

### Top Questions Asked
1.
2.
3.
4.
5.

### FAQ Additions Needed
- [ ]
- [ ]
- [ ]

---

## What Worked Well

### Top 3 Wins
1. **Win:**
   - Evidence:
   - Replicate:

2. **Win:**
   - Evidence:
   - Replicate:

3. **Win:**
   - Evidence:
   - Replicate:

### Successful Elements
- [ ] Pre-prelaunch engagement
- [ ] PLC content quality
- [ ] Email sequence effectiveness
- [ ] Social media impact
- [ ] Offer/stack appeal
- [ ] Scarcity execution
- [ ] Support responsiveness
- [ ] Tech stability

---

## What Needs Improvement

### Top 3 Areas to Fix
1. **Issue:**
   - Impact:
   - Fix:

2. **Issue:**
   - Impact:
   - Fix:

3. **Issue:**
   - Impact:
   - Fix:

### Elements to Improve
- [ ] List building
- [ ] PLC engagement
- [ ] Email copywriting
- [ ] Sales page conversion
- [ ] Checkout process
- [ ] Support capacity
- [ ] Tech reliability
- [ ] Other: ______

---

## Testimonial Collection

### Testimonials Gathered
| Name | Type | Result | Usable |
|------|------|--------|--------|
| | Video / Text | | [ ] |
| | Video / Text | | [ ] |
| | Video / Text | | [ ] |
| | Video / Text | | [ ] |
| | Video / Text | | [ ] |

### Testimonial Requests Sent
- [ ] Thank you + request email
- [ ] Follow-up reminder
- [ ] Incentive offered (if any)

### Case Studies Identified
1.
2.
3.

---

## Financial Summary

### Revenue Breakdown
| Item | Amount |
|------|--------|
| Gross Revenue | R$ |
| - Refunds | R$ |
| - Payment Fees (~3%) | R$ |
| - Affiliate Commissions | R$ |
| **Net Revenue** | **R$** |

### Costs
| Item | Amount |
|------|--------|
| Advertising | R$ |
| Tools/Software | R$ |
| Contractor/Team | R$ |
| Affiliate Prizes | R$ |
| Other | R$ |
| **Total Costs** | **R$** |

### Profit
| Item | Amount |
|------|--------|
| Net Revenue | R$ |
| - Total Costs | R$ |
| **Net Profit** | **R$** |
| **Profit Margin** | **%** |

---

## Goals vs Actuals

### Original Goals
| Goal | Target | Actual | Hit |
|------|--------|--------|-----|
| Revenue | R$ | R$ | [ ] |
| Sales | | | [ ] |
| Conversion Rate | % | % | [ ] |
| List Growth | | | [ ] |

### Analysis
- Goals exceeded because:
- Goals missed because:

---

## Next Launch Planning

### Immediate Actions (Week 1)
- [ ]
- [ ]
- [ ]

### Medium-term Actions (Month 1)
- [ ]
- [ ]
- [ ]

### Next Launch Considerations
- [ ] Relaunch timing: ______
- [ ] Evergreen setup: [ ] Yes / [ ] No
- [ ] Product updates needed: [ ] Yes / [ ] No
- [ ] List building focus: ______

---

## Final Assessment

### Overall Launch Grade: ___/10

### Key Takeaway:


### Most Important Change for Next Launch:


---

**Analysis Completed By:** ______
**Date:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Post-Launch*


---

<!-- preprelaunch-readiness.md -->
# Pre-Prelaunch Readiness Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Phase**: Pre-Prelaunch
> **Purpose**: Validate readiness before beginning prelaunch sequence

---

## Product/Offer Readiness

### Core Product
- [ ] Product concept clearly defined
- [ ] Main transformation articulated
- [ ] Unique mechanism identified
- [ ] Delivery format decided
- [ ] Pricing structure set
- [ ] Product outline/curriculum complete

### Offer Stack
- [ ] Core modules/components defined
- [ ] Bonuses selected (3-5)
- [ ] Fast action bonus ready
- [ ] Guarantee terms defined
- [ ] Payment plan options ready
- [ ] Value anchoring calculated

---

## Avatar/Market Research

### Avatar Definition
- [ ] Primary avatar documented
- [ ] Top 3 frustrations identified
- [ ] Top 3 desires identified
- [ ] Top 5 objections mapped
- [ ] Language patterns collected
- [ ] Day-in-the-life understood

### Market Intelligence
- [ ] Competitor launches analyzed
- [ ] Price points benchmarked
- [ ] Positioning differentiated
- [ ] Market sophistication assessed

---

## List/Audience Readiness

### List Health
- [ ] List size: {{X}} subscribers
- [ ] List cleaned (removed bounces/inactive)
- [ ] Engagement rate > 20% opens
- [ ] Email deliverability tested
- [ ] SPF/DKIM/DMARC configured

### Warming Activities
- [ ] Regular content sent in past 30 days
- [ ] Engagement emails sent
- [ ] Reply rate measured
- [ ] No major sends in past week (avoid fatigue)

---

## Survey/Research Campaign

### Survey Preparation
- [ ] Survey questions written
- [ ] Survey mechanism ready (email reply or form)
- [ ] Survey email drafted
- [ ] Reminder email drafted
- [ ] Response tracking setup

### Survey Goals
- [ ] Target response rate: 5-15%
- [ ] Minimum responses needed: {{X}}
- [ ] Analysis template ready

---

## Tech Infrastructure

### Email Platform
- [ ] Account in good standing
- [ ] Automation capabilities verified
- [ ] Segmentation/tagging ready
- [ ] Deliverability tested

### Landing Pages
- [ ] Opt-in page ready (if building launch list)
- [ ] Thank you page ready
- [ ] PLC hosting pages ready (or planned)
- [ ] Mobile responsiveness verified

### Payment/Checkout
- [ ] Payment processor active
- [ ] Checkout page template ready
- [ ] Payment plan setup capable
- [ ] Test transaction completed

### Video Hosting (if using video PLCs)
- [ ] Video platform selected
- [ ] Account setup
- [ ] Embedding tested
- [ ] Privacy settings configured

---

## Content Preparation

### PLC Planning
- [ ] PLC1 topic defined
- [ ] PLC2 topic defined
- [ ] PLC3 topic defined
- [ ] Content format decided (video/text/audio)
- [ ] Production timeline realistic

### Sales Page
- [ ] Sales page outline created
- [ ] Key sections identified
- [ ] Testimonials collected
- [ ] Images/graphics planned

### Email Sequences
- [ ] Prelaunch email topics mapped
- [ ] Open cart email structure planned
- [ ] Email templates ready

---

## Timeline Validation

### Key Dates Set
- [ ] Survey launch date: {{DATE}}
- [ ] PLC1 release date: {{DATE}}
- [ ] PLC2 release date: {{DATE}}
- [ ] PLC3 release date: {{DATE}}
- [ ] Cart open date: {{DATE}}
- [ ] Cart close date: {{DATE}}

### Buffer Time
- [ ] At least 3 days buffer for content creation
- [ ] At least 1 day buffer before cart open
- [ ] No conflicts with holidays/major events

---

## Team/Support Readiness

### Resources
- [ ] Content creator assigned/confirmed
- [ ] Tech support available
- [ ] Customer support plan in place
- [ ] Designer available (if needed)

### Contingency
- [ ] Backup contacts identified
- [ ] Emergency procedures documented
- [ ] Tech failure plan exists

---

## Pre-Prelaunch Score

**Required for Launch:**
- Product/Offer: 6/6 items
- Avatar/Market: 4/4 items
- List Readiness: 5/5 items
- Tech Infrastructure: 10/10 items (critical)

**Recommended:**
- Survey: 5/5 items
- Content: 6/6 items
- Timeline: 3/3 items
- Team: 4/4 items

---

## Go/No-Go Decision

| Area | Status | Notes |
|------|--------|-------|
| Product Ready | [ ] Go / [ ] No-Go | |
| Avatar Clear | [ ] Go / [ ] No-Go | |
| List Ready | [ ] Go / [ ] No-Go | |
| Tech Working | [ ] Go / [ ] No-Go | |
| Timeline Realistic | [ ] Go / [ ] No-Go | |

**Final Decision:** [ ] PROCEED TO PRE-PRELAUNCH

**Date:** {{DATE}}
**Signed:** {{NAME}}

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula*


---

<!-- sales-page-plf.md -->
# Sales Page PLF Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Validate sales page for launch
> **Style**: Relationship-focused, post-PLC context

---

## Above the Fold

### Headline
- [ ] Clear benefit/transformation
- [ ] Speaks to avatar's desire
- [ ] Not hype-y or scammy
- [ ] Under 15 words

### Subheadline
- [ ] Expands on headline
- [ ] Addresses objection or curiosity
- [ ] Includes specifics (numbers, time)

### Hero Section
- [ ] Strong visual (if used)
- [ ] CTA visible without scrolling
- [ ] No distractions
- [ ] Mobile-friendly

---

## Opening Section

### Hook
- [ ] Grabs attention
- [ ] Creates curiosity or connection
- [ ] Relates to avatar's situation
- [ ] Bridges to problem

### Problem Articulation
- [ ] Avatar's pain described
- [ ] Uses their language
- [ ] Creates nodding/recognition
- [ ] Shows understanding

---

## Solution Section

### Your Approach
- [ ] Unique mechanism explained
- [ ] Why different from others
- [ ] Why it works
- [ ] Simple to understand

### Authority/About
- [ ] Your story (brief)
- [ ] Credibility established
- [ ] Connection to their journey
- [ ] Not arrogant

---

## Stack Section

### Core Product
- [ ] Product name clear
- [ ] What it is
- [ ] What's included
- [ ] Value assigned

### Modules/Components
| # | Name | Description | Value |
|---|------|-------------|-------|
| 1 | [ ] Clear | [ ] Benefit-focused | R$___ |
| 2 | [ ] Clear | [ ] Benefit-focused | R$___ |
| 3 | [ ] Clear | [ ] Benefit-focused | R$___ |
| 4 | [ ] Clear | [ ] Benefit-focused | R$___ |
| 5 | [ ] Clear | [ ] Benefit-focused | R$___ |

### Bonuses
| # | Name | Type | Value |
|---|------|------|-------|
| 1 | [ ] Attractive | [ ] Useful | R$___ |
| 2 | [ ] Attractive | [ ] Useful | R$___ |
| 3 | [ ] Attractive | [ ] Useful | R$___ |

### Value Stack
- [ ] Total value calculated
- [ ] Price revealed after value
- [ ] Discount/savings shown
- [ ] Payment plan mentioned

---

## Social Proof Section

### Testimonials
- [ ] Minimum 5 testimonials
- [ ] Diverse (different situations)
- [ ] Specific results
- [ ] Include photos (if available)
- [ ] Mix of formats (text, video)

### Testimonial Quality
| # | Specific Result | Relatable | Photo |
|---|----------------|-----------|-------|
| 1 | [ ] | [ ] | [ ] |
| 2 | [ ] | [ ] | [ ] |
| 3 | [ ] | [ ] | [ ] |
| 4 | [ ] | [ ] | [ ] |
| 5 | [ ] | [ ] | [ ] |

### Other Proof
- [ ] Case study summary
- [ ] Results numbers
- [ ] Media mentions (if any)
- [ ] Client logos (if B2B)

---

## FAQ Section

### Objections Addressed
- [ ] Time objection
- [ ] Money objection
- [ ] "Will it work for me"
- [ ] Trust/legitimacy
- [ ] Technical questions

### FAQ Quality
- [ ] Questions are real (from research)
- [ ] Answers are thorough
- [ ] Overcomes hesitation
- [ ] Doesn't create new objections

---

## Guarantee Section

### Guarantee Presented
- [ ] Type clear (30/60/90 day)
- [ ] Process simple
- [ ] Terms honest
- [ ] Contact method included

### Guarantee Positioning
- [ ] Framed as confidence
- [ ] Risk reversal clear
- [ ] Not positioned as "escape"

---

## Pricing/CTA Section

### Price Presentation
- [ ] Value anchored first
- [ ] Price revealed after value
- [ ] Payment plan shown
- [ ] Comparison made (daily cost, etc.)

### CTA Buttons
- [ ] Clear action text
- [ ] Contrasting color
- [ ] Above fold CTA
- [ ] Multiple CTAs throughout
- [ ] Final CTA prominent

---

## Urgency/Scarcity Section

### Scarcity Element
- [ ] Cart close deadline shown
- [ ] Timer (if appropriate)
- [ ] Real limitation explained
- [ ] No fake urgency

### Final Push
- [ ] Recap of offer
- [ ] "Two options" close
- [ ] Emotional appeal
- [ ] Final CTA

---

## Technical Checks

### Mobile Responsiveness
- [ ] Readable on mobile
- [ ] Buttons tap-friendly
- [ ] Images scale properly
- [ ] No horizontal scroll

### Load Speed
- [ ] Under 3 seconds
- [ ] Images optimized
- [ ] Videos lazy load
- [ ] No heavy scripts

### Links/Functions
- [ ] All CTAs link correctly
- [ ] Checkout works
- [ ] Payment processes
- [ ] Confirmation shows

### Cross-Browser
- [ ] Chrome tested
- [ ] Safari tested
- [ ] Firefox tested
- [ ] Mobile browsers tested

---

## Copy Quality

### Voice/Tone
- [ ] Conversational
- [ ] Matches brand
- [ ] Not hype-y
- [ ] Authentic

### Clarity
- [ ] No jargon
- [ ] Short paragraphs
- [ ] Scannable
- [ ] Clear hierarchy

### Persuasion
- [ ] Benefits over features
- [ ] Emotional connection
- [ ] Logical justification
- [ ] Social proof integrated

---

## Legal/Compliance

### Required Elements
- [ ] Privacy policy linked
- [ ] Terms of service linked
- [ ] Earnings disclaimer (if applicable)
- [ ] Refund policy stated

### Claims Verification
- [ ] All claims truthful
- [ ] Results typical or noted as exceptional
- [ ] Testimonials real

---

## Final Review

### Page Flow
- [ ] Logical progression
- [ ] No dead ends
- [ ] Clear path to purchase
- [ ] Objections handled before CTA

### Overall Assessment
- [ ] Would I buy from this page?
- [ ] Does it feel trustworthy?
- [ ] Is the value clear?
- [ ] Is urgency real?

---

## Sales Page Approval

**Above the fold effective:** [ ] Yes / [ ] No
**Stack complete and valued:** [ ] Yes / [ ] No
**Social proof sufficient:** [ ] Yes / [ ] No
**FAQs address objections:** [ ] Yes / [ ] No
**Guarantee clear:** [ ] Yes / [ ] No
**Technical working:** [ ] Yes / [ ] No
**Copy quality high:** [ ] Yes / [ ] No

**SALES PAGE APPROVED:** [ ] Yes / [ ] No

**Date:** ______
**Reviewer:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Sales Page*


---

<!-- sales-video-complete-production-aid.md -->
# SALES VIDEO (OPEN CART): COMPLETE PRODUCTION AID

> **Framework**: Product Launch Formula (Jeff Walker)
> **Theme**: "BUY/ENROLL" — Apresentação completa da oferta com ativação total de escassez
> **Source**: Launch (Original + Updated 2021 Edition)

---

## SECTION 1 — STRATEGIC FOUNDATION

**The single job of the Sales Video:** Present the complete offer, activate all mental triggers at full force, and convert prepared prospects into buyers.

**Success criteria:** When the Sales Video is done right, the viewer finishes thinking:
1. "I know exactly what this is, what I get, and what it costs"
2. "The value is clear — this is worth more than the price"
3. "I need to act NOW before this closes"

### The Sales Video's Position in the PLF Arc

The Sales Video is the CLIMAX of the three-act play:
- PLC #1 opened the story (why care)
- PLC #2 developed the conflict (what's possible, what's in the way)
- PLC #3 reached the peak (ownership, pivot)
- **Sales Video delivers the resolution** (here's how you achieve it)

### What the Sales Video Must Accomplish

Unlike the PLCs (which build desire), the Sales Video must:
- **Present the full offer clearly** — no more mystery, all details revealed
- **Justify the price** — through value anchoring and ROI framing
- **Remove risk** — through guarantee and risk reversal
- **Activate full scarcity** — deadline, limited spots, expiring bonuses
- **Handle final objections** — the purchase-specific resistance
- **Drive action** — clear, urgent call to action

### Psychological Prerequisites from the PLC Sequence

If the PLCs were done correctly, viewers arrive at the Sales Video with:

| Element | State | Built By |
|---------|-------|----------|
| Trust in YOU | Complete | PLC #1-3 positioning and teaching |
| Belief in opportunity | Complete | PLC #1 opportunity, PLC #2 proof |
| Belief in THEMSELVES | Strong | PLC #2 case studies, PLC #3 Big View |
| Anticipation | Peak | PLC #3 pivot and scarcity seed |
| Readiness to decide | High | PLC #3 prepared them for an offer |
| Reciprocity imbalance | Significant | Three videos of free value |

> "By now, if you've followed the formula, your PLC has connected with people on your list. Mental triggers have created authority, social proof, community. Scarcity trigger has been seeded. Prospects know an offer is coming." — Jeff Walker

---

## SECTION 2 — PRE-PRODUCTION RESEARCH

### Sub-block A — Offer Intelligence (What You Need to KNOW)

**From PLC #3 comments:**
- [ ] Identify questions about the offer (price, details, what's included)
- [ ] Note buying signals: "When does it open?" "How much is it?" "Can't wait!"
- [ ] Identify remaining objections specific to PURCHASING (not transformation)
- [ ] Look for price sensitivity indicators (questions about payment plans, ROI)

**From the full PLC sequence:**
- [ ] What transformation language resonated most? (Use in the close)
- [ ] What case studies/examples created the strongest response?
- [ ] What objections were already crushed? (Don't re-address extensively)

### Sub-block B — Offer Clarity (What You Need to DECIDE)

**The complete offer stack:**
- [ ] Core product/program — what is it exactly?
- [ ] Bonuses — what extras are included?
- [ ] Guarantee — what risk reversal do you offer?
- [ ] Price — what's the investment?
- [ ] Payment options — full pay, payment plan?
- [ ] Scarcity elements — what's limited? (spots, time, bonuses, price)

**Value anchoring strategy:**
- [ ] What is the FULL value of everything included?
- [ ] What would this cost if purchased separately?
- [ ] What's the ROI / cost of NOT solving this problem?
- [ ] How does the price compare to alternatives?

**Scarcity specifics (MUST BE REAL):**
- [ ] Deadline: Exact date and time (with timezone)
- [ ] Limited spots: How many? Why limited?
- [ ] Bonus expiry: Which bonuses disappear? When?
- [ ] Price increase: What's the price after launch?
- [ ] Which combination of scarcity types are you using?

### Sub-block C — Structural Preparation (What You Need to BUILD Before Scripting)

**Critical copy elements to draft:**

1. **The offer walkthrough:**
   - [ ] Each component/module with its specific benefit
   - [ ] "What it IS → What it DOES for them → What RESULT it produces" format
   - [ ] Value stack with dollar amounts for anchoring

2. **The price reveal:**
   - [ ] Anchor statement (total value)
   - [ ] Reveal statement (actual price)
   - [ ] Comparison frame (alternatives, DIY cost, cost of inaction)
   - [ ] Payment plan presentation (if applicable)

3. **The guarantee:**
   - [ ] Guarantee terms (duration, conditions)
   - [ ] Confidence framing (why you offer this guarantee)
   - [ ] Process (how to request refund if needed)

4. **Scarcity copy:**
   - [ ] Exact deadline statement
   - [ ] Consequence statement (what happens when deadline passes)
   - [ ] Reminder hooks (for email sequence)

5. **The close:**
   - [ ] Final transformation callback
   - [ ] Fork-in-the-road moment
   - [ ] Direct call to action

**Assets needed:**
- [ ] Sales page URL (live and tested)
- [ ] Order form (functional)
- [ ] Testimonials/case studies (for social proof section)
- [ ] Guarantee badge/seal (if using)
- [ ] Countdown timer (if using on page)
- [ ] Thank you page (configured)
- [ ] Confirmation emails (set up)

---

## SECTION 3 — EMOTIONAL ARCHITECTURE

### Emotional Starting Point (Where They Are When They Press Play)

Sales Video viewers are NOT cold prospects. They're READY prospects:

| Baseline | Description |
|----------|-------------|
| **Trust level** | Peak — you've delivered three times |
| **Anticipation** | Maximum — they've been waiting for this |
| **Desire** | High — the Big View created longing |
| **Belief** | Solid — opportunity, you, and themselves |
| **Decision mode** | Active — they came ready to evaluate and decide |
| **Urgency awareness** | Present — scarcity was seeded |

### Emotional Arc Across the Sales Video

| Timing | Emotion | Viewer Thought | Cause |
|--------|---------|----------------|-------|
| Minute 0-2 | Recognition, recall | "This is the moment. I've been waiting for this." | Journey recap |
| Minute 2-5 | Desire, longing | "Yes — this is what I want." | Transformation reframe |
| Minute 5-10 | Clarity, excitement | "Now I understand exactly what I'm getting." | Offer walkthrough |
| Minute 10-13 | Confidence, belief | "These results are real — people like me are succeeding." | Social proof |
| Minute 13-16 | Surprise, delight | "Wait — it's only that much? This is a no-brainer." | Price reveal |
| Minute 16-18 | Safety, relief | "And if it doesn't work, I'm protected." | Guarantee |
| Minute 18-21 | Urgency, fear of missing out | "I need to act NOW or I'll miss this." | Scarcity activation |
| Minute 21-23 | Doubt resolution | "That was my last concern — and it's handled." | Final objections |
| Minute 23-25 | Determination, decision | "I'm doing this. Where do I click?" | The close |

### The Critical Emotional Shift That Must Happen in the Sales Video

**The viewer must cross from "evaluating" to "deciding."**

This shift happens through cumulative impact:
1. **After Offer Walkthrough:** "I understand what I'm getting" → Clarity
2. **After Social Proof:** "This works for people like me" → Belief
3. **After Price Reveal:** "This is actually worth it" → Value recognition
4. **After Guarantee:** "There's no risk" → Safety
5. **After Scarcity:** "I need to act NOW" → Urgency
6. **At the Close:** "I'm ready to buy" → Decision

If they finish the Sales Video without wanting to click the button, one of these stages failed to land.

### Emotional Ending Point

When they finish the Sales Video, they should feel:
- **Certain** — They know exactly what the offer is
- **Confident** — The value is clear, the risk is removed
- **Urgent** — They need to act now, not later
- **Ready** — They're about to click the button
- **Decisive** — They've made their choice (yes or no, but not "maybe later")

**The goal is immediate action.** Unlike PLCs (which build toward the next video), the Sales Video must drive them to the order page NOW.

---

## SECTION 4 — SCRIPT STRUCTURE (Beat by Beat with Copy Depth)

---

### BEAT 1 — RECAP THE JOURNEY (1-2 minutes)

#### 4a — Duration Target
- Time: 1-2 minutes
- Percentage: 5-8% of total

#### 4b — Strategic Purpose
Orient viewers to the full arc and set the frame: "This is the moment we've been building toward."

#### 4c — Copy Framework

**Standard Journey Recap:**
```
"Over the past [timeframe], we've been on a journey together.

In my first video, I showed you [PLC #1 core message — the opportunity].

In my second video, I went deeper and showed you [PLC #2 core message — the transformation].

In my third video, I revealed [PLC #3 core message — the complete picture and big view].

And I promised you that today, I'd share how you can take this to the next level.

That's exactly what this video is about."
```

**High-Energy Journey Recap:**
```
"This is it.

After three videos of training, after [X] comments from this amazing community,
after showing you what's possible...

Today is the day I share the full picture of how you can [transformation].

If you've been following along, you know what's at stake. You know what's possible.

Now let me show you exactly how to make it happen."
```

#### 4d — Quality Control Checklist
- [ ] Does the recap connect all three PLCs into a clear arc?
- [ ] Does it create "this is the moment" energy?
- [ ] Is it brief? (This is a recap, not a re-presentation)
- [ ] Does it smoothly transition to the transformation reframe?

#### 4f — Common Mistakes for This Beat
1. **Too long** — Spending 5 minutes recapping wastes precious Sales Video time
2. **Disconnected** — Not linking the PLCs into a coherent story arc
3. **Low energy** — This is the climax — start with appropriate intensity
4. **Skipping entirely** — New viewers need orientation; returning viewers need closure

---

### BEAT 2 — RESTATE THE TRANSFORMATION (2-3 minutes)

#### 4a — Duration Target
- Time: 2-3 minutes
- Percentage: 8-12% of total

#### 4b — Strategic Purpose
Reactivate the desire. Before presenting the offer, remind them WHY they want this transformation.

#### 4c — Copy Framework

**Pain → Desire Bridge:**
```
"Let me paint the picture one more time.

Right now, you might be dealing with [specific pain].
You might be frustrated with [specific frustration].
You might be wondering if [specific doubt].

But imagine if instead...

[Vivid "after" scenario — financial]
[Vivid "after" scenario — lifestyle]
[Vivid "after" scenario — emotional]

That's what we're really talking about here. Not just [surface benefit] —
but a fundamental shift in [their core desire]."
```

**The Gap Articulation:**
```
"Here's the gap:

On one side: [current reality — specific and vivid]
On the other side: [transformation — specific and vivid]

What I've shown you in these videos is that the gap is crossable.
The transformation is real. People are doing it.

The question is: How do YOU cross that gap?

That's what I'm about to share with you."
```

#### 4d — Quality Control Checklist
- [ ] Is the "before" state specific and resonant?
- [ ] Is the "after" state vivid and desirable?
- [ ] Does this create or reactivate genuine desire?
- [ ] Does it naturally lead to "show me how"?

#### 4f — Common Mistakes for This Beat
1. **Abstract transformation** — "Better life" doesn't create desire; specifics do
2. **Skipping the pain** — People buy to escape pain as much as gain pleasure
3. **Too similar to PLC content** — Same words feel repetitive; fresh framing maintains attention
4. **Disconnected from offer** — Transformation must lead directly to "this product provides"

---

### BEAT 3 — INTRODUCE THE PRODUCT (1-2 minutes)

#### 4a — Duration Target
- Time: 1-2 minutes
- Percentage: 5-8% of total

#### 4b — Strategic Purpose
Name the product and position it as THE vehicle for the transformation.

#### 4c — Copy Framework

**The Introduction:**
```
"That's why I created [PRODUCT NAME].

[PRODUCT NAME] is [one-sentence description of what it IS].

It's designed specifically for [who it's for] who want to [transformation].

In a moment, I'm going to walk you through everything that's included.
But first, let me tell you what this is really about..."
```

**The Positioning:**
```
"[PRODUCT NAME] isn't just [surface description].

It's the complete [system/program/method] for [achieving transformation].

It's what I wish existed when I was [their starting point].

It's the [adjective] way to [transformation] without [common pain point of alternatives]."
```

#### 4d — Quality Control Checklist
- [ ] Is the product name clear and memorable?
- [ ] Is the one-line description crisp?
- [ ] Is it positioned as the vehicle for the transformation (not the transformation itself)?
- [ ] Does it create curiosity about what's included?

#### 4f — Common Mistakes for This Beat
1. **Burying the name** — Make it clear and prominent
2. **Feature-first** — Position around transformation, not features
3. **Jargon-heavy** — Keep it simple and accessible
4. **Over-promising** — Credible positioning beats hype

---

### BEAT 4 — THE OFFER WALKTHROUGH (5-8 minutes)

#### 4a — Duration Target
- Time: 5-8 minutes
- Percentage: 20-30% of total

#### 4b — Strategic Purpose
Walk through EVERYTHING they get, building value with each component.

#### 4c — Copy Framework

**For Each Component:**
```
"The first thing you get is [COMPONENT NAME].

What this IS: [description]

What it DOES for you: [benefit/function]

The RESULT you'll get: [specific outcome]

This alone is worth [value anchor] because [justification]."
```

**Value Stacking:**
```
"So far, you're getting:
- [Component 1] — Value: $X
- [Component 2] — Value: $X
- [Component 3] — Value: $X

Total value so far: $X"
```

**Bonus Introduction:**
```
"But wait — I'm also including [BONUS NAME].

This is something I normally [sell separately / reserve for private clients / etc.].

[Description of what it is and what it does]

This alone is worth $X because [justification]."
```

#### 4d — Examples / Deconstructions

**The Value Walkthrough Rhythm:**

| Element | Time | Purpose |
|---------|------|---------|
| Core product | 3-4 min | The main thing they're buying |
| Module/component breakdown | 2-3 min | Specificity builds perceived value |
| Bonuses | 1-2 min | Extra value creates "more than expected" feeling |
| Value stack summary | 30 sec | Total value anchors the price reveal |

#### 4e — Quality Control Checklist
- [ ] Is every component explained with the IS → DOES → RESULT formula?
- [ ] Are value amounts assigned to each component?
- [ ] Do bonuses feel genuinely valuable (not filler)?
- [ ] Is there a running value stack?
- [ ] Is the total value significantly higher than the price?

#### 4f — Common Mistakes for This Beat
1. **Feature dumping** — Listing features without connecting to benefits/results
2. **No value anchoring** — If you don't assign values, they can't appreciate the discount
3. **Weak bonuses** — Bonuses should feel valuable, not like afterthoughts
4. **Too fast** — Each component deserves its moment; don't rush
5. **Too slow** — Don't belabor obvious value; keep momentum

---

### BEAT 5 — SOCIAL PROOF: RESULTS (2-3 minutes)

#### 4a — Duration Target
- Time: 2-3 minutes
- Percentage: 8-12% of total

#### 4b — Strategic Purpose
Prove that real people are getting real results. This is the "if they can do it, I can too" section.

#### 4c — Copy Framework

**Testimonial Introduction:**
```
"Now, you might be wondering: does this actually work?

Let me show you what [students/clients/members] are saying..."
```

**Testimonial Presentation:**
```
"[NAME] came to me [situation].

Here's what they said after [timeframe]:

'[Quote — specific result or experience]'

What I love about [Name]'s story is [specific element that's relatable to audience]."
```

**Results Summary:**
```
"And it's not just [Name].

[X number] of people have gone through [PRODUCT NAME] and [result summary].

[Specific data point if available — completion rates, success metrics, etc.]"
```

#### 4d — Quality Control Checklist
- [ ] Are testimonials specific (not vague praise)?
- [ ] Do they include results (not just "I loved it")?
- [ ] Are the testimonial subjects relatable to the audience?
- [ ] Is there variety (different situations, different results)?
- [ ] FTC compliant (if US market)?

#### 4f — Common Mistakes for This Beat
1. **Vague testimonials** — "It was great!" doesn't move the needle
2. **Too many testimonials** — 3-5 powerful ones beat 15 weak ones
3. **Unrelatable subjects** — If testimonials are from "exceptional" people, they don't create projection
4. **No variety** — Same type of result repeated doesn't broaden appeal
5. **Reading too fast** — Let testimonials land; give them weight

---

### BEAT 6 — PRICE REVEAL + VALUE ANCHORING (2-3 minutes)

#### 4a — Duration Target
- Time: 2-3 minutes
- Percentage: 8-12% of total

#### 4b — Strategic Purpose
Present the price in a way that feels like an obvious deal.

#### 4c — Copy Framework

**The Anchor:**
```
"So let's talk about the investment.

When you add up everything I just showed you:
- [Component 1]: $X
- [Component 2]: $X
- [Component 3]: $X
- [Bonus 1]: $X
- [Bonus 2]: $X

The total value is $[TOTAL].

And honestly, at that price, this would still be worth it because [ROI framing]."
```

**The Reveal:**
```
"But I'm not charging $[TOTAL].

I'm not even charging $[Mid-point anchor].

The investment for [PRODUCT NAME] is just $[PRICE].

[If payment plan]: And if you'd prefer to spread it out, there's a [X]-payment option of $[AMOUNT] per [period]."
```

**The Comparison:**
```
"Now, let me put this in perspective.

$[PRICE] is less than [relatable comparison — daily coffee, one month of X, one client].

And what you're getting is [transformation recap].

When you think about the cost of NOT solving this — [cost of inaction] — the investment becomes obvious."
```

#### 4d — Examples / Deconstructions

**The Price Reveal Rhythm:**

| Stage | Copy Element | Psychological Effect |
|-------|--------------|---------------------|
| Stack | List each component with value | "This is a lot of stuff" |
| Total | Sum the values | "Wow, that's a lot of money" |
| Anchor high | "At $X, this would still be worth it" | Sets ceiling expectation |
| Mid-anchor | "I'm not charging $X, or even $Y" | Builds anticipation |
| Reveal | "The investment is just $Z" | Relief, "that's less than I expected" |
| Compare | "$Z is less than [daily coffee/one client]" | Makes price feel small |
| ROI frame | "What's this worth when it works?" | Shifts from cost to investment |

**Why This Works:**
- Anchoring creates a reference point (total value)
- Gap between anchor and price creates perceived deal
- Comparison reframes the price in familiar terms
- ROI shifts from "expense" to "investment" mindset

#### 4e — Quality Control Checklist
- [ ] Is the total value anchor significantly higher than the price?
- [ ] Is the price reveal clear and direct?
- [ ] Is there a payment plan option (if applicable)?
- [ ] Is there a comparison frame that makes the price feel small?
- [ ] Is there ROI framing (what this is worth when it works)?

#### 4f — Common Mistakes for This Beat
1. **No anchor** — Revealing price without context makes it feel arbitrary
2. **Apologizing for price** — Confidence in value matters; don't undercut yourself
3. **Hidden price** — Make the reveal clear; don't bury it
4. **No payment plan** — Losing sales from people who want it but need cash flow flexibility
5. **No comparison** — Abstract number vs. relatable comparison changes perception

---

### BEAT 7 — GUARANTEE / RISK REVERSAL (1-2 minutes)

#### 4a — Duration Target
- Time: 1-2 minutes
- Percentage: 5-8% of total

#### 4b — Strategic Purpose
Remove the perceived risk of buying. Shift risk from buyer to seller.

#### 4c — Copy Framework

**The Guarantee:**
```
"Now, I know making an investment like this might feel like a risk.

That's why I'm including a [X-day] [type] guarantee.

Here's how it works: [specific terms].

If [guarantee conditions], simply [process], and you'll get [refund terms].

No questions asked. No hoops to jump through."
```

**The Confidence Frame:**
```
"Why am I offering this?

Because I'm confident in what [PRODUCT NAME] can do for you.

I've seen it work for [X number] of people. I've seen the results.

And I'd rather you try it risk-free than wonder 'what if' forever."
```

#### 4d — Quality Control Checklist
- [ ] Is the guarantee clear and specific (duration, terms, process)?
- [ ] Is it positioned as confidence, not a safety net for doubt?
- [ ] Does it remove the primary risk objection?
- [ ] Is the process for claiming it straightforward?

#### 4f — Common Mistakes for This Beat
1. **Vague guarantee** — "Satisfaction guaranteed" means nothing; specifics matter
2. **Hidden conditions** — Surprising terms destroy trust
3. **Weak guarantee** — A 7-day guarantee on a 6-week program doesn't provide real safety
4. **Apologetic framing** — Guarantee should feel confident, not defensive
5. **Skipping entirely** — No guarantee = unnecessary friction

---

### BEAT 8 — FULL SCARCITY ACTIVATION (2-3 minutes)

#### 4a — Duration Target
- Time: 2-3 minutes
- Percentage: 8-12% of total

#### 4b — Strategic Purpose
Activate all scarcity elements at full force. Create URGENCY to act NOW.

> "One absolute, cardinal rule for creating a successful launch is setting a definitive close for your launch. And there must be some negative consequence if people don't buy during that limited open cart window." — Jeff Walker

#### 4c — Copy Framework

**The Deadline:**
```
"Here's what you need to know:

This offer closes on [DATE] at [TIME] [TIMEZONE].

After that, [consequence — price increase / cart closes / bonuses disappear].

I'm serious about this. When the deadline hits, it's done."
```

**The Limited Spots:**
```
"I can only take [X] people into [PRODUCT NAME].

Why? [Reason — personal attention, community quality, resource limits].

Right now, [X] spots are already spoken for based on the interest from my videos.

When they're gone, they're gone."
```

**The Bonus Expiry:**
```
"Remember the bonuses I showed you earlier?

[Bonus 1] worth $X
[Bonus 2] worth $X

Those are ONLY available during this launch.

After [deadline], they're not part of the offer anymore."
```

**The Layered Scarcity:**
```
"So let's be clear:

- The price of $[PRICE] is only available until [deadline]
- The bonuses worth $[VALUE] disappear after [deadline]
- [Limited spots element if applicable]

This is your window. [Deadline] is the line."
```

#### 4d — Examples / Deconstructions

**The 3 Types of Scarcity (Layering Strategy):**

| Type | What It Is | Copy Pattern | When to Use |
|------|-----------|--------------|-------------|
| **Time** | Deadline closes | "Closes [date] at [time]" | Always — most fundamental |
| **Spots** | Limited capacity | "Only [X] spots available" | When you have genuine limits |
| **Bonuses** | Bonuses expire | "Bonuses disappear after [deadline]" | To add urgency layer |
| **Price** | Price increases | "After [deadline], price goes to $X" | When evergreening |

**Scarcity Layering Formula:**
```
Layer 1: The deadline (always)
   ↓
Layer 2: The consequence (price/bonuses/availability)
   ↓
Layer 3: The social proof ("spots are filling fast")
   ↓
Layer 4: The personal urgency ("don't wait")
```

**The Walker Rule on Scarcity:**
> "The scarcity MUST BE REAL. If you say the offer closes, it CLOSES. If you say there are only 50 spots, there are only 50 spots. Fake scarcity will destroy your reputation faster than almost anything else."

#### 4e — Quality Control Checklist
- [ ] Is every scarcity element REAL? (Critical — fake scarcity destroys reputation)
- [ ] Is the deadline specific (date, time, timezone)?
- [ ] Are the consequences clear (what happens if they don't act)?
- [ ] Are multiple scarcity types layered (time, bonuses, price)?
- [ ] Does it create genuine urgency without feeling manipulative?

#### 4f — Common Mistakes for This Beat
1. **Fake scarcity** — The #1 trust destroyer. If you say it closes, it MUST close
2. **Vague deadline** — "Limited time" doesn't motivate; specific deadline does
3. **No consequences** — Why act now if nothing changes tomorrow?
4. **Over-scaring** — Urgency, yes. Fear-mongering, no
5. **Weak scarcity** — If the only consequence is "price goes up $10," it doesn't move

---

### BEAT 9 — FINAL OBJECTION HANDLING (2-3 minutes)

#### 4a — Duration Target
- Time: 2-3 minutes
- Percentage: 8-12% of total

#### 4b — Strategic Purpose
Handle the final purchase-specific objections that might prevent someone ready to buy.

#### 4c — Copy Framework

**The Time Objection:**
```
"Now, you might be thinking: 'I don't have time for this.'

Here's what I've found: [reframe about time investment].

And here's the real question: What's the cost of NOT making time?

How much longer will you [current pain] because you don't prioritize [transformation]?"
```

**The Money Objection:**
```
"Maybe you're thinking: 'I can't afford this right now.'

I understand. And here's what I want you to consider:

What is this costing you right now? Every [time period] that you don't [transformation],
you're leaving [specific cost — money, time, opportunity] on the table.

The question isn't 'Can I afford this?' The question is 'Can I afford NOT to?'"
```

**The "Not Ready" Objection:**
```
"Some of you might be thinking: 'I'm not ready yet. Maybe later.'

Here's the truth about 'ready':

Nobody is ever fully ready. [Example of your own or client's 'not ready' moment].

The people who get results aren't the ones who wait until conditions are perfect.
They're the ones who start before they feel ready."
```

**The "Will It Work for Me?" Objection:**
```
"And maybe you're wondering: 'This sounds great, but will it work for ME?'

Remember [case study / testimonial name] from earlier? They had the same doubt.

[Brief callback to their situation and result].

The method works. The system works. The question is: will you give it a chance to work for you?"
```

#### 4d — Quality Control Checklist
- [ ] Are objections specific to PURCHASE resistance (not transformation belief)?
- [ ] Is each objection validated before being addressed?
- [ ] Are responses specific, not generic reassurances?
- [ ] Do you reference proof (case studies, testimonials) where possible?
- [ ] Does handling objections lead naturally to the close?

#### 4f — Common Mistakes for This Beat
1. **Re-addressing PLC objections** — Those were about transformation; these are about purchase
2. **Dismissive responses** — "Don't worry about it" doesn't help
3. **Too many objections** — Pick the top 3-4 purchase blockers
4. **Argumentative tone** — Understand, don't fight
5. **Ending on objections** — Always transition to the close with positive energy

---

### BEAT 10 — THE CLOSE (2-3 minutes)

#### 4a — Duration Target
- Time: 2-3 minutes
- Percentage: 8-12% of total

#### 4b — Strategic Purpose
The final push. Make them feel the fork in the road and drive the action.

#### 4c — Copy Framework

**The Fork in the Road:**
```
"Here's where we are.

You have two paths in front of you.

Path one: You close this video, go back to [current reality], and [consequence of inaction].
Maybe you'll try again later. Maybe you won't. And [projection of unchanged future].

Path two: You click the button below, join [PRODUCT NAME], and [transformation].
[Timeframe] from now, you're [specific "after" scenario].

The path you choose is up to you."
```

**The Final Transformation Callback:**
```
"Remember what we talked about:

[The transformation — vivid, specific, emotional].

That's not a fantasy. That's what's possible when you [what the product enables].

And it starts with one decision. Today."
```

**The Direct CTA:**
```
"If you're ready, here's what to do:

Click the button below [or go to URL] right now.

Complete your registration.

And I'll see you inside [PRODUCT NAME].

The deadline is [deadline]. Don't wait.

I'll see you on the other side."
```

#### 4d — Examples / Deconstructions

**The Fork in the Road Anatomy:**

| Element | Copy Function | Why It Works |
|---------|---------------|--------------|
| "Two paths" | Creates binary choice | Forces decision (not "maybe") |
| Path 1: Status quo | Paint unchanged future | Activates loss aversion |
| Path 2: Transformation | Paint changed future | Activates desire |
| "Your choice" | Give agency | They own the decision |
| Final callback | Vivid transformation | Last emotional hit |
| Direct CTA | Exact instructions | Remove friction |
| Deadline reminder | Scarcity restated | Urgency boost |

**The Close Progression:**
1. **Create the moment:** "Here's where we are" — signals importance
2. **Fork in the road:** "Two paths" — forces choice
3. **Path 1 (inaction):** Vivid negative future — loss aversion
4. **Path 2 (action):** Vivid positive future — desire activation
5. **Callback:** The transformation one more time — emotional peak
6. **Direct CTA:** "Click the button below" — clear instruction
7. **Deadline:** One final urgency trigger — action driver
8. **Confident close:** "I'll see you inside" — assumes the sale

#### 4e — Quality Control Checklist
- [ ] Is there a clear fork-in-the-road moment?
- [ ] Is the transformation callback vivid and emotional?
- [ ] Is the CTA crystal clear (exactly what to do)?
- [ ] Is the deadline restated?
- [ ] Does it end with confidence and energy?

#### 4f — Common Mistakes for This Beat
1. **Weak close** — After all that buildup, ending weakly loses sales
2. **No fork in the road** — People need to feel the choice
3. **Unclear CTA** — "Buy now" is less clear than "Click the button below and complete your registration"
4. **Forgetting the deadline** — Final scarcity reminder matters
5. **Apologetic tone** — You've earned this moment. Close with confidence

---

## SECTION 5 — MENTAL TRIGGER ACTIVATION MAP

| Beat | Triggers Activated | Mechanism |
|------|-------------------|-----------|
| Journey Recap | **Anticipation** (fulfilled), **Trust** | Closure of the arc, reminder of relationship |
| Transformation Restate | **Desire**, **Hope** | Reactivating the "after" picture |
| Product Introduction | **Authority**, **Anticipation** | Positioning as the solution |
| Offer Walkthrough | **Reciprocity**, **Value** | Showing what they get, building perceived value |
| Social Proof | **Social Proof**, **Trust** | Real people, real results |
| Price Reveal | **Scarcity** (implied), **Value** | Anchor vs. price creates "deal" perception |
| Guarantee | **Trust**, **Safety** | Risk removed |
| Scarcity Activation | **Scarcity** (full), **Urgency** | Deadline, limited spots, expiring bonuses |
| Final Objections | **Trust**, **Empathy** | Addressing final resistance |
| The Close | **Commitment**, **Decision** | Fork in the road, final push |

### Cumulative Effect by End of Sales Video

By the end of this video, all nine mental triggers are firing at maximum:

| Trigger | State |
|---------|-------|
| Authority | Complete — demonstrated across four videos |
| Reciprocity | Time to collect — massive imbalance created |
| Trust | Peak — relationship solidified |
| Anticipation | Fulfilled — this is what they've been waiting for |
| Likability | Strong — you've been generous and authentic |
| Events/Ritual | Peak — this is THE day, THE moment |
| Community | Active — they're part of something |
| Social Proof | Visible — testimonials and community energy |
| Scarcity | Full activation — deadline, limits, consequences |

**Psychological state:** Ready to buy NOW. The triggers are aligned for immediate action.

---

## SECTION 6 — TIMING AND PACING GUIDE

**Total recommended duration:** 20-30 minutes

### When Shorter vs Longer is Appropriate

**Shorter (~20 min) is appropriate when:**
- Lower price point (less justification needed)
- Simple offer (fewer components to explain)
- Market already knows you well (less proof needed)
- Shorter launch sequence (less recap needed)

**Longer (~25-30 min) is appropriate when:**
- Higher price point (more value anchoring needed)
- Complex offer (multiple components, bonuses)
- More skeptical market (more social proof needed)
- Multiple objections to address (more objection handling)
- Layered scarcity (multiple types to explain)

### Comparison to PLCs

| Element | PLC #1 | PLC #2 | PLC #3 | Sales Video |
|---------|--------|--------|--------|-------------|
| **Primary job** | Open desire | Build belief | Complete ownership + pivot | Present offer + close |
| **Teaching** | 35% | 45% | 35% (Big View) | 0% (no new teaching) |
| **Selling** | 0% | 0% | 25% (pivot) | 100% |
| **Energy arc** | Curious → hopeful | Engaged → believing | Invested → ready | Ready → decisive |
| **End state** | Want PLC #2 | Want PLC #3 | Want the offer | Want to BUY |

### Percentage Allocation Table

| Section | % of Total | For 25-min video |
|---------|------------|------------------|
| Journey Recap | 5-8% | 1:15 - 2:00 |
| Transformation Restate | 8-12% | 2:00 - 3:00 |
| Product Introduction | 5-8% | 1:15 - 2:00 |
| Offer Walkthrough | 20-30% | 5:00 - 7:30 |
| Social Proof | 8-12% | 2:00 - 3:00 |
| Price Reveal | 8-12% | 2:00 - 3:00 |
| Guarantee | 5-8% | 1:15 - 2:00 |
| Scarcity Activation | 8-12% | 2:00 - 3:00 |
| Final Objections | 8-12% | 2:00 - 3:00 |
| The Close | 8-12% | 2:00 - 3:00 |

### Pacing Rhythm

```
OPENING: Recognition, anticipation (recap + transformation)
   ↓
BUILD: Clarity, excitement (product intro + offer walkthrough)
   ↓
PROOF: Confidence, belief (social proof)
   ↓
DECISION: Evaluation (price reveal + guarantee)
   ↓
URGENCY: Pressure, resolution (scarcity + objections)
   ↓
ACTION: Determination, commitment (the close)
```

---

## SECTION 7 — FORMAT AND PRODUCTION NOTES

### Best Format for Sales Video

| Section | Recommended Format | Why |
|---------|-------------------|-----|
| Journey Recap | **On camera** | Personal connection, warmth |
| Transformation | **On camera** | Emotional content needs human delivery |
| Product Intro | Either | Can transition to slides |
| Offer Walkthrough | **Slides/screen-capture** | Visual breakdown helps comprehension |
| Social Proof | **Slides with testimonials** OR **video testimonials** | Visual proof is powerful |
| Price Reveal | **On camera** | Confidence in delivery matters |
| Guarantee | **On camera** | Sincerity matters |
| Scarcity | **On camera** | Eye contact for urgency |
| Final Objections | **On camera** | Sincerity, connection |
| The Close | **On camera** | This is the moment — human connection essential |

### The Sales Video Sweet Spot

1. Open on camera (warmth, recognition)
2. Transition to slides for offer walkthrough (clarity)
3. Mix in testimonial visuals or video clips
4. Return to on camera for price reveal through close (confidence, connection)

### Production Quality for Sales Video

This is where production quality matters MOST:
- Clear audio is essential
- Good lighting for on-camera sections
- Professional-looking slides for offer breakdown
- Timer/countdown visual if using

---

## SECTION 8 — SELF-ASSESSMENT RUBRIC

| Dimension | 1 (Weak) | 3 (Solid) | 5 (Exceptional) |
|-----------|----------|-----------|-----------------|
| **Journey connection** | No recap | Brief recap that connects PLCs | Creates "this is the moment" energy |
| **Offer clarity** | Confusing, incomplete | Everything included is clear | Viewer knows exactly what they get |
| **Value anchoring** | Price with no anchor | Total value stated, clear discount | Price feels like obvious deal |
| **Testimonials** | Generic or none | Specific results from relatable people | Viewer thinks "I can do this too" |
| **Price reveal confidence** | Apologetic | Confident, clean reveal | Price feels like a steal |
| **Guarantee strength** | Weak or missing | Clear, specific, removes risk | "No reason not to try" feeling |
| **Scarcity authenticity** | Fake or missing | Real, specific deadline | Genuine urgency, "I need to act now" |
| **Objection handling** | Dismissed or ignored | Top 3-4 addressed | Final resistance dissolved |
| **CTA clarity** | Vague | Clear next step | Viewer knows exactly what to do |
| **Close power** | Weak ending | Fork in the road + clear CTA | Viewer is ready to click immediately |
| **Emotional arc** | Flat energy throughout | Builds through offer, peaks at scarcity | Clear progression: clarity → belief → value → urgency → action |
| **Continuity with PLCs** | Feels like a separate sales pitch | References the journey | Feels like the natural conclusion of a 4-part story |

**Minimum viable Sales Video:** Every dimension at 3 or above.
**Launch-winning Sales Video:** Most dimensions at 4-5, no dimension below 3.

**Critical dimensions that MUST be 4+:**
- **Scarcity authenticity** — Fake scarcity destroys the entire launch
- **Offer clarity** — Confusion kills conversion
- **CTA clarity** — They must know exactly how to buy

---

## SECTION 9 — TOP MISTAKES (Ranked by Damage)

1. **Fake scarcity** — Will destroy your reputation and future launches. If you say it closes, it CLOSES.

2. **Vague offer** — If they're confused about what they get, they won't buy. Clarity is essential.

3. **No value anchoring** — Price without context feels arbitrary. Always anchor high first.

4. **Weak guarantee** — A risky purchase gets considered; a risk-free purchase gets decided.

5. **No deadline** — Without urgency, they'll "think about it" forever. Set a specific close.

6. **Skipping social proof** — Testimonials and results prove it works. Don't assume they'll trust your word.

7. **Apologetic tone** — You've delivered three videos of value. You've EARNED the right to sell. Don't apologize.

8. **Too long** — Sales Video can run 20-30 minutes, but not 60. Respect their time.

9. **Feature dumping** — Features are what it IS; benefits are what it DOES FOR THEM. Lead with benefits.

10. **Weak close** — The end is the climax. Strong call to action, fork in the road, confidence.

11. **Not addressing money objection** — Price is always a consideration. Frame it properly.

12. **Disconnected from PLCs** — Sales Video should feel like the natural conclusion, not a separate pitch.

13. **Buried CTA** — Make it crystal clear how to buy. Don't make them search.

14. **No consequences** — "Offer closes" means nothing if no negative consequence follows.

15. **One shot** — Don't rely on Sales Video alone. Email sequence during Open Cart is critical.

---

## SECTION 10 — TRANSITION PROTOCOL: The Open Cart Sequence

### From Sales Video to Cart Close

The Sales Video launches the Open Cart period. What happens next:

**Expected sales pattern:**
| Phase | % of Sales |
|-------|------------|
| Day 1 (Open) | 25% |
| Days 2-4 (Middle) | 25% |
| Day 5 (Close) | 50% |

> "Don't make the mistake of letting up on the last day. Send at least 2 emails. Most people are terrible procrastinators, and they'll wait until the last minute." — Jeff Walker

### The 5-Day Email Sequence

**Day 1 — Open Cart:**
- Email 1: Cart open (short, direct, link-focused)
- Email 2: ~4 hours later, confirmation everything is working

**Day 2 — Social Proof:**
- Talk about the great response
- Share early buyer testimonials
- "People are joining" momentum

**Day 3 — FAQ:**
- Longer email answering top questions
- Address remaining objections
- Include mini case study

**Day 4 — Scarcity Warning (24h):**
- Message shifts to SCARCITY
- Absolutely clear about when it closes
- What they lose if they don't act

**Day 5 — Close Cart:**
- Email 1: Morning — "Closing TODAY"
- Email 2: 6-8 hours before close
- Email 3: Optional — 1-2 hours before

### Post-Launch: What Comes After

**For buyers:**
- Surprise bonuses (not mentioned during launch)
- World-class onboarding
- Over-deliver on promise

**For non-buyers:**
- Don't abandon (invested energy in the relationship)
- Send valuable content in the days after close
- Set up the next launch

---

*Production Aid Version: 3.0*
*Source: Launch (Jeff Walker) - Original + Updated 2021 Edition*
*Framework: Product Launch Formula - Sales Video Complete Guide*


---

<!-- seed-launch-checklist.md -->
# Seed Launch Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Validate before running Seed Launch
> **Best For**: Validating new product/idea, small list, getting started

---

## Seed Launch Overview

### What Makes It Different
- [ ] Product created WHILE delivering
- [ ] Small audience (100-500 people)
- [ ] Simplified PLF sequence
- [ ] Live delivery with feedback
- [ ] Validation before scaling

### Goals
- [ ] Primary: Validate product/market fit
- [ ] Secondary: Generate initial revenue
- [ ] Tertiary: Collect testimonials
- [ ] Bonus: Build product with feedback

---

## Pre-Seed Validation

### Idea Validation
- [ ] Problem clearly identified
- [ ] Solution conceptualized
- [ ] Audience exists and reachable
- [ ] Willingness to pay assumed/tested

### Minimum Requirements
- [ ] Email list exists (even small)
- [ ] Or: Access to audience (group, following)
- [ ] Basic email capability
- [ ] Way to collect payment
- [ ] Delivery method planned (Zoom, etc.)

---

## Audience Preparation

### List Building (If Needed)
- [ ] Lead magnet created (simple)
- [ ] Opt-in page live
- [ ] Traffic source identified
- [ ] Goal: 100-500 subscribers minimum

### List Warming
- [ ] Survey sent (optional but helpful)
- [ ] Engagement content sent
- [ ] Relationship established
- [ ] Problem/solution teased

---

## Offer Definition

### Product Concept
- [ ] Product name: ______
- [ ] Core transformation: ______
- [ ] Delivery format: [ ] Live calls [ ] Cohort [ ] Mixed
- [ ] Duration: ______
- [ ] Number of sessions: ______

### Pricing
- [ ] Seed price (discount from future): R$______
- [ ] Future price indicated: R$______
- [ ] Payment plan option (if needed)

### What's Included
- [ ] Live sessions (X calls)
- [ ] Recording access
- [ ] Support/community
- [ ] Bonus materials (optional)

---

## Simplified PLC Sequence

### Option A: Email-Only Seed

**Email 1: The Problem**
- [ ] Date: ______
- [ ] Articulate the problem
- [ ] Show you understand
- [ ] Hint at solution

**Email 2: The Solution Exists**
- [ ] Date: ______
- [ ] Reveal there's a solution
- [ ] Brief case/proof (even if yours)
- [ ] Build anticipation

**Email 3: Your Opportunity**
- [ ] Date: ______
- [ ] Present the offer
- [ ] Explain Seed format
- [ ] Open for enrollment

### Option B: Video + Email Seed

- [ ] PLC1 (video): Opportunity + Authority
- [ ] PLC2 (video): Proof + Teaching
- [ ] PLC3 (video or email): Offer

### Sequence Checklist
- [ ] All content created
- [ ] Emails written
- [ ] Links working
- [ ] Payment ready

---

## Open Cart (Seed Version)

### Duration
- [ ] Cart open: 3-5 days
- [ ] Deadline clear

### Emails
- [ ] Open announcement
- [ ] Follow-up/FAQ
- [ ] Urgency
- [ ] Final call

### Scarcity Options
- [ ] Limited spots (real - 10-30)
- [ ] Seed price expires
- [ ] Both

---

## Delivery Preparation

### Platform
- [ ] Zoom or similar set up
- [ ] Recording capability
- [ ] Calendar invites ready
- [ ] Backup plan if tech fails

### Content Outline
- [ ] Session 1 topic: ______
- [ ] Session 2 topic: ______
- [ ] Session 3+ topics: ______
- [ ] Flexibility for student questions

### Feedback Collection
- [ ] Survey after each session
- [ ] Questions before sessions
- [ ] Final feedback form
- [ ] Testimonial request process

---

## Revenue Expectations

### Realistic Seed Goals
| List Size | Conversion | Sales | Revenue (R$500 avg) |
|-----------|------------|-------|---------------------|
| 100 | 5-10% | 5-10 | R$2,500-5,000 |
| 250 | 5-10% | 12-25 | R$6,000-12,500 |
| 500 | 5-10% | 25-50 | R$12,500-25,000 |

### Your Projections
- [ ] List size: ______
- [ ] Target conversion: ____%
- [ ] Target sales: ______
- [ ] Target revenue: R$______

---

## Success Criteria

### Minimum Viable Launch
- [ ] At least 5-10 paying students
- [ ] Enough to justify live delivery
- [ ] Feedback collected
- [ ] Product improved

### Validation Achieved When
- [ ] People pay for the concept
- [ ] Students engage and participate
- [ ] Results/transformations occur
- [ ] Testimonials collected
- [ ] Product refined based on feedback

---

## Post-Seed Actions

### Immediately After
- [ ] Thank you email to buyers
- [ ] Calendar invites sent
- [ ] Community/group set up
- [ ] Session 1 prepared

### During Delivery
- [ ] Collect feedback each session
- [ ] Adjust content as needed
- [ ] Document what works
- [ ] Note testimonial-worthy moments

### After Completion
- [ ] Request testimonials
- [ ] Survey for improvements
- [ ] Document final product
- [ ] Plan Internal Launch

---

## Seed to Scale Pathway

### After Successful Seed
1. [ ] Product finalized based on feedback
2. [ ] Testimonials collected
3. [ ] Price adjusted for full launch
4. [ ] Internal Launch planned
5. [ ] Eventually: JV Launch

### Timeline
- [ ] Seed Launch: Month 1
- [ ] Internal Launch: Month 2-3
- [ ] JV Launch: Month 4-6 (optional)

---

## Jeff's Seed Launch Story

> "After my partnership breakup in 2005, I started over from scratch.
> Spoke at conference, sold 6 spots in 'Product Launch Workshop'.
> Invited entrepreneurial friends to join for free to reach ~30 people.
> Surveyed students before each call about their burning questions.
> Ended up doing 9-10 calls instead of promised 5.
> This became the first Product Launch Formula course."

### Key Lessons
- [ ] Start small, refine big
- [ ] Feedback is gold
- [ ] Overdeliver on first cohort
- [ ] Use students' questions to shape product

---

## Seed Launch Go/No-Go

**Audience exists:** [ ] Yes / [ ] No
**Product concept clear:** [ ] Yes / [ ] No
**Delivery method ready:** [ ] Yes / [ ] No
**Payment collection ready:** [ ] Yes / [ ] No
**Time to deliver live:** [ ] Yes / [ ] No

**PROCEED WITH SEED LAUNCH:** [ ] Yes / [ ] No

**Date:** ______
**Signed:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Seed Launch*


---

<!-- social-media-launch.md -->
# Social Media Launch Strategy Checklist

> **Framework**: Product Launch Formula (Jeff Walker)
> **Purpose**: Social media support for launch
> **Cardinal Rule**: "Don't build on rented land" - use social to build email list

---

## Jeff's Cardinal Rule

> "Social media shouldn't be your list, but you should use it
> to build your list. In the same way you wouldn't build your
> dream home on rented land."

- [ ] Primary goal is EMAIL list building
- [ ] Social amplifies, not replaces, email strategy

---

## Platform Strategy

### Primary Platforms
| Platform | Priority | Content Type |
|----------|----------|--------------|
| Instagram | [ ] High / [ ] Med / [ ] Low | |
| Facebook | [ ] High / [ ] Med / [ ] Low | |
| YouTube | [ ] High / [ ] Med / [ ] Low | |
| LinkedIn | [ ] High / [ ] Med / [ ] Low | |
| TikTok | [ ] High / [ ] Med / [ ] Low | |
| Twitter/X | [ ] High / [ ] Med / [ ] Low | |

### Platform-Specific Prep
| Platform | Profile Updated | Links Updated | Bio Clear |
|----------|-----------------|---------------|-----------|
| Instagram | [ ] | [ ] | [ ] |
| Facebook | [ ] | [ ] | [ ] |
| YouTube | [ ] | [ ] | [ ] |
| LinkedIn | [ ] | [ ] | [ ] |

---

## Pre-Prelaunch Social

### Content Calendar
| Day | Content | Platform | Status |
|-----|---------|----------|--------|
| -14 | Teaser #1 | | [ ] |
| -12 | Behind scenes | | [ ] |
| -10 | Teaser #2 | | [ ] |
| -7 | Countdown starts | | [ ] |
| -5 | "Something coming" | | [ ] |
| -3 | Final teaser | | [ ] |
| -1 | Tomorrow announcement | | [ ] |

### Content Types
- [ ] Teaser posts (curiosity)
- [ ] Behind-the-scenes content
- [ ] Personal story related to topic
- [ ] "Save the date" graphics
- [ ] Countdown stories

---

## Prelaunch Social

### PLC Promotion
| PLC | Feed Post | Stories | Live | Reels |
|-----|-----------|---------|------|-------|
| PLC1 | [ ] | [ ] | [ ] | [ ] |
| PLC2 | [ ] | [ ] | [ ] | [ ] |
| PLC3 | [ ] | [ ] | [ ] | [ ] |

### PLC1 Day
- [ ] Feed post announcing PLC1
- [ ] 3-5 stories sequence
- [ ] Link in bio updated
- [ ] Engagement in comments
- [ ] DM replies active

### PLC2 Day
- [ ] Feed post announcing PLC2
- [ ] 3-5 stories sequence
- [ ] Social proof content
- [ ] Engagement active

### PLC3 Day
- [ ] Feed post announcing PLC3
- [ ] 3-5 stories sequence
- [ ] "Tomorrow" anticipation
- [ ] Link in bio updated

---

## Open Cart Social

### Day 1 Content
| Time | Platform | Content | Status |
|------|----------|---------|--------|
| AM | All | "Doors Open" post | [ ] |
| Mid | Stories | Behind scenes | [ ] |
| PM | All | Social proof | [ ] |
| Night | Stories | Day 1 recap | [ ] |

### Day 2-4 Content
- [ ] Daily testimonial/result post
- [ ] FAQ content
- [ ] Behind the scenes
- [ ] Social proof updates
- [ ] Countdown to close

### Final Day Content
| Time | Content | Status |
|------|---------|--------|
| AM | "Last day" post | [ ] |
| Mid | Urgency stories | [ ] |
| PM | Final push | [ ] |
| Close | "Closing" stories | [ ] |
| Post | "Closed" announcement | [ ] |

---

## Content Templates

### Announcement Post
```
[Hook about transformation]

The wait is over.

[PRODUCT NAME] is officially available.

If you want to [RESULT]:
↓ Link in bio

Doors close [DATE].
```

### Social Proof Post
```
[Before/After or Result]

"[Testimonial quote]" - [Name]

This is what's possible when [method/product].

Want your own transformation?
↓ Link in bio

[Only X days left / Doors close DATE]
```

### Urgency Post
```
[X] hours left.

The [PRODUCT] doors close at [TIME] tonight.

After that? I don't know when they reopen.

If you're still thinking about it...
↓ Link in bio

This is your last chance.
```

### Final Post
```
Doors closed.

Thank you to everyone who joined [PRODUCT].

[X] people took the leap.

To everyone who didn't make it in time:
We'll let you know when it opens again.

For now, stay tuned for free content.
```

---

## Stories Strategy

### Daily Stories During Launch
- [ ] 3-5 stories minimum per day
- [ ] Mix of content types
- [ ] Always include link sticker/swipe
- [ ] Save important stories to highlights

### Story Types
- [ ] Personal/talking to camera
- [ ] Screenshots (testimonials, sales)
- [ ] Behind the scenes
- [ ] Countdown timers
- [ ] Q&A responses
- [ ] Reposts (user content)

### Highlights to Create/Update
- [ ] [PRODUCT] highlight
- [ ] Testimonials highlight
- [ ] FAQ highlight

---

## Engagement Strategy

### Daily Engagement Tasks
- [ ] Reply to all comments
- [ ] Reply to all DMs
- [ ] Engage with relevant posts
- [ ] Thank shares and tags

### Comment Response Templates
```
Thank you! If you have any questions, DM me!

Glad this resonated! Link in bio if you want to learn more.

So happy to hear this! 🙏
```

### DM Response Templates
```
Hey! Thanks for reaching out. [ANSWER QUESTION].
The link to learn more is [LINK]. Let me know if you have other questions!

I appreciate you! Yes, [PRODUCT] includes [ANSWER].
Here's the link: [LINK]
```

---

## Paid Social (Optional)

### Ad Types
- [ ] Traffic to opt-in
- [ ] Traffic to PLC (retargeting)
- [ ] Traffic to sales page (warm)
- [ ] Cart abandonment retargeting

### Audiences
| Audience | Platform | Status |
|----------|----------|--------|
| Lookalike buyers | | [ ] |
| Engaged followers | | [ ] |
| Email list upload | | [ ] |
| Website visitors | | [ ] |
| Video viewers | | [ ] |

### Budget
- [ ] Daily budget: R$______
- [ ] Total launch budget: R$______
- [ ] Spend allocation: ______

---

## Cross-Platform Targeting

### Email List Upload
- [ ] Upload to Facebook/Meta
- [ ] Upload to LinkedIn
- [ ] Upload to YouTube
- [ ] Create custom audiences
- [ ] Create lookalikes

### Retargeting Pixels
- [ ] Facebook pixel on all pages
- [ ] LinkedIn insight tag (if B2B)
- [ ] Google tag on all pages

---

## Community Management

### Groups/Communities
- [ ] Own group notifications on
- [ ] Post launch content in groups
- [ ] Engage with members
- [ ] Answer questions

### User-Generated Content
- [ ] Encourage shares
- [ ] Repost testimonials
- [ ] Thank taggers
- [ ] Create share-worthy content

---

## Metrics to Track

### Daily Tracking
| Metric | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|--------|-------|-------|-------|-------|-------|
| Reach | | | | | |
| Engagement | | | | | |
| Link clicks | | | | | |
| DMs | | | | | |
| Followers gained | | | | | |

### Post-Launch Analysis
- [ ] Total reach during launch
- [ ] Total engagement
- [ ] Link clicks from social
- [ ] Sales attributed to social
- [ ] Best performing content

---

## Warning from Jeff

> "The big social media companies have some of the smartest engineers
> in the world, and they're using it to make their platforms incredibly
> addictive. And you're not immune to that addiction."

### Time Protection
- [ ] Set specific social media time blocks
- [ ] Use scheduling tools when possible
- [ ] Delegate engagement if possible
- [ ] Don't let social distract from core tasks

---

## Social Media Launch Approval

**Platforms selected:** [ ] Yes
**Content calendar ready:** [ ] Yes
**Templates prepared:** [ ] Yes
**Scheduling tools set:** [ ] Yes
**Team/support ready:** [ ] Yes

**SOCIAL STRATEGY APPROVED:** [ ] Yes / [ ] No

**Date:** ______
**Signed:** ______

---

*Checklist Version: 1.0*
*Framework: Product Launch Formula - Social Media*


---

<!-- video-production-complete-checklist.md -->
# COMPLETE VIDEO PRODUCTION CHECKLIST — PRODUCT LAUNCH FORMULA

> **Framework**: Product Launch Formula (Jeff Walker)
> **Source**: Launch (Original + Updated 2021 Edition)
> **Purpose**: Definitive checklist for CPL video production and Sales Video

---

## PLC #1 — THE OPPORTUNITY ("Why")

**Strategic objective:** Answer "Why should I care?" Build authority, create reciprocity, open the story loop.

### Pre-production

- [ ] Define the core transformation/opportunity in one sentence (pain removal OR pleasure delivery)
- [ ] Identify the "after" picture — what does their life look like post-transformation?
- [ ] Prepare your positioning story (credentials through narrative, not claims)
- [ ] Select 1-2 teaching points that deliver real value without covering everything
- [ ] List the top objections from pre-launch survey or audience research
- [ ] Decide which objections to address now vs. promise for later videos
- [ ] Write the PLC #2 foreshadow/tease — specific enough to create desire, vague enough to maintain curiosity
- [ ] Prepare your call-to-action prompt (specific question to drive comments)

### Script Structure / Shot List

**Beat 1 — Show the Opportunity**
- [ ] Paint the vivid "after" picture — concrete, not abstract
- [ ] Focus on the result/destination, not the tool/vehicle
- [ ] Use language of transformation, change, or impact
- [ ] Make it feel achievable for ordinary people

**Beat 2 — Position Yourself**
- [ ] Lead with empathy BEFORE authority ("I understand your world because...")
- [ ] Establish credibility through story, not résumé
- [ ] Frame credentials within desire to help (creates affinity, avoids bragging)
- [ ] If no formal credentials: position from experience and results

**Beat 3 — Teach**
- [ ] Deliver real, usable content — not just teasing
- [ ] Err on giving MORE, not less
- [ ] Demonstrate expertise by showing it, not claiming it
- [ ] Content should be valuable enough that some people get results from this alone

**Beat 4 — Raise Objections**
- [ ] Address top objections head-on (from survey/research)
- [ ] Either answer directly or promise to answer in upcoming videos
- [ ] Don't pretend objections don't exist

**Beat 5 — Foreshadow PLC #2**
- [ ] Reveal something cool they'll learn in PLC #2
- [ ] Create the anticipation trigger — make them mark their calendar

**Beat 6 — Call to Action**
- [ ] Ask for a comment (specific question works best)
- [ ] Frame it as starting a conversation, not just engagement bait

### Post-production Check

- [ ] Zero mention of product, price, or offer anywhere
- [ ] Authority established through story, not claims
- [ ] Empathy comes before credentials
- [ ] At least one genuinely valuable teaching moment included
- [ ] Transformation feels achievable, not aspirational fantasy
- [ ] Clear foreshadow of PLC #2 creates anticipation
- [ ] CTA is present and specific

### Primary Mental Triggers Activated

- [ ] Authority (credentials through story)
- [ ] Reciprocity (free high-value content)
- [ ] Anticipation (foreshadow PLC #2)
- [ ] Likability (empathy, generosity, personal tone)

### Duration
- **Edited video:** 15-25 minutes
- **Live broadcast:** ~40 minutes
- **Teaching segment:** 5-10 minutes minimum

---

## PLC #2 — THE TRANSFORMATION ("What")

**Strategic objective:** Teach something actionable that makes them SEE THEMSELVES having the transformation. Deepen authority and reciprocity. Zero pitch.

### Pre-production

- [ ] Identify the one key teaching that can create a shift in 5-18 minutes
- [ ] Ask: "What can I teach that will make an impact and get them moving?"
- [ ] Review ALL comments from PLC #1 — extract questions, objections, enthusiasm
- [ ] Select top 2-3 objections to crush directly
- [ ] Prepare a case study or concrete example if available
- [ ] Write the PLC #3 foreshadow/tease
- [ ] Prepare comment-referencing lines ("Many of you asked about X...")

### Script Structure / Shot List

**Beat 1 — Thanks and Recap**
- [ ] Thank people for comments and questions from PLC #1
- [ ] Reference specific comments or patterns ("Your questions about X were amazing...")
- [ ] Quick recap of PLC #1 (30-60 seconds max)
- [ ] Show you're listening — use real data from comments

**Beat 2 — Recap the Opportunity**
- [ ] Never assume they watched or remember PLC #1
- [ ] Brief re-orientation for anyone coming in cold
- [ ] Shorter than PLC #1 but still clear

**Beat 3 — Recap Your Positioning**
- [ ] Quick reminder of who you are and why they should listen
- [ ] Don't linger — trust is already building from PLC #1
- [ ] Just enough for new viewers to orient

**Beat 4 — Teach (Core of PLC #2)**
- [ ] Deliver real, actionable value — something they can DO
- [ ] Not theory, not motivation — tactical and practical
- [ ] Deep enough that some people could get results from just this
- [ ] Goal: prospect sees themselves having the transformation
- [ ] Don't hold back the "good stuff" — the fear of giving too much is almost always unfounded
- [ ] Case study or concrete example reinforces teaching

**Beat 5 — Objection Crushing**
- [ ] Address top 2-3 objections directly
- [ ] Target: "I believe it works, but not for ME"
- [ ] Be specific and direct — vague reassurances don't work
- [ ] Use evidence, examples, or stories to dismantle each objection

**Beat 6 — Foreshadow PLC #3**
- [ ] Build anticipation for next video
- [ ] Tease specific enough to create desire, vague enough for curiosity
- [ ] Make them feel the sequence is building toward something big

**Beat 7 — Call to Action**
- [ ] Ask for a comment (different/deeper question than PLC #1)
- [ ] Continue the Launch Conversation
- [ ] Comments deepen social proof and community

### Post-production Check

- [ ] Still zero mention of product, price, or offer
- [ ] Teaching is genuinely actionable, not just motivational
- [ ] Prospect can realistically see themselves having the transformation
- [ ] PLC #1 comments were referenced (shows listening)
- [ ] Objections addressed are specific, not generic
- [ ] Foreshadow of PLC #3 creates escalating anticipation
- [ ] The teaching IS the selling — authority and reciprocity built simultaneously

### Primary Mental Triggers Activated

- [ ] Authority (deepened by actual teaching)
- [ ] Reciprocity (even more free value)
- [ ] Social Proof (reference PLC #1 comments)
- [ ] Trust (second contact, familiarity grows)
- [ ] Anticipation (foreshadow PLC #3)

### Duration
- **Edited video:** 15-25 minutes
- **Teaching segment:** 5-10 minutes minimum
- **Example:** Jeff Walker taught entire Seed Launch in ~18 minutes

---

## PLC #3 — THE OWNERSHIP EXPERIENCE ("How" + Pivot to Offer)

**Strategic objective:** Deliver peak teaching value, then pivot to the offer with a soft landing. Seed scarcity. This is the climax of the three-act play.

### Pre-production

- [ ] Review ALL comments from PLC #1 and PLC #2 — extract recurring questions and objections
- [ ] Prepare your strongest teaching yet (first 75% of video)
- [ ] Prepare case study if available (brief — PLC #3 has a lot of work to do)
- [ ] Write the PIVOT copy — transition from educator to offer-maker
- [ ] Define the scarcity element of your launch offer (limited spots, deadline, bonus expiry, etc.)
- [ ] Write scarcity seed language (mention, don't hammer)
- [ ] Prepare the "big view" projection — what's the ULTIMATE transformation if they go all-in?
- [ ] Draft the soft landing language bridging free content to paid offer

### Script Structure / Shot List

**Beat 1 — Express Thanks and Excitement**
- [ ] Thank viewers for comments and questions from PLC #2
- [ ] Express genuine excitement (yours AND theirs)
- [ ] Reflect the community's energy back to them
- [ ] Not fake enthusiasm — genuine momentum from the launch conversation

**Beat 2 — Quick Recap of Opportunity + Positioning**
- [ ] Don't assume they saw PLC #1 or #2
- [ ] Brief orientation: opportunity + who you are
- [ ] Move through quickly — familiar territory by now

**Beat 3 — Short Case Study (optional but powerful)**
- [ ] Concrete proof the transformation is real and achievable
- [ ] Keep it brief
- [ ] FTC compliance check if using results-based claims (US market)

**Beat 4 — Answer Top Recurring Questions**
- [ ] Address objections EVEN IF already answered in PLC #1 or #2
- [ ] Use the exact questions from comments
- [ ] Repetition is strategic — reinforces answers, shows you care
- [ ] Be thorough — this is your last teaching before the offer

**Beat 5 — The Big View (Maximum Inspiration)**
- [ ] Step back — what's REALLY possible?
- [ ] Project into their future — make them visualize the full transformation
- [ ] Look at it from all angles (financial, lifestyle, emotional, professional)
- [ ] This is the moment of maximum inspiration before the pivot
- [ ] Paint the most compelling "after" picture — full possibility, not incremental

**Beat 6 — THE PIVOT + Soft Landing (last ~25% of the video)**
- [ ] Acknowledge the value delivered across all 3 PLCs (without self-congratulation)
- [ ] Frame the product as the "next level" beyond free content
- [ ] Language: "I've shown you the what and the why. If you're ready to go deeper and actually implement this..."
- [ ] Position the product as the natural, logical next step
- [ ] Tell them an offer is coming in the next email/video
- [ ] Tell them to watch/read IF they're ready to take transformation to the next level
- [ ] Don't be apologetic — you've earned the right to make the offer
- [ ] Don't go from "best friend" to "used-car salesman" — the bridge must feel natural

**Beat 7 — Seed the Scarcity**
- [ ] Mention the offer will be limited (spots, time, pricing — whatever applies)
- [ ] Don't over-explain or hammer it — just plant the seed
- [ ] Tell them to watch for the next email
- [ ] Examples: "limited number of spots," "special pricing only during launch," "I can only work with X people"

**Beat 8 — Call to Action**
- [ ] Ask for a comment (final round — will be the most energized)
- [ ] Watch for the buying signal shift: comments moving from content questions to offer/price questions
- [ ] If they're asking about price and details → you've won

### Post-production Check

- [ ] First 75% is peak teaching value — strongest content of the entire sequence
- [ ] Pivot happens and feels natural, not forced
- [ ] Product is positioned as logical next step, not hard sell
- [ ] Scarcity is mentioned but not hammered
- [ ] Big view projection is vivid and inspiring
- [ ] Soft landing bridges education to offer without tonal whiplash
- [ ] They should finish the video actively wanting to see the offer

### Primary Mental Triggers Activated

- [ ] ALL previous triggers compounded
- [ ] Scarcity (seeded for first time)
- [ ] Events/Ritual (launch becomes a shared event)
- [ ] Community (active and vocal through comments)
- [ ] Anticipation (maximum — they're waiting for the offer)

### Duration
- **Edited video:** 15-30 minutes
- **Pivot timing:** Last 10% (Updated Edition) or 25% (Original Edition)

### Critical Warning

> "Making the pivot to the sale in the final piece of Prelaunch Content is CRITICAL, and leaving out that pivot is a mistake a lot of people make." — Jeff Walker

---

## SALES VIDEO (VV — Vídeo de Vendas / Open Cart Video)

**Strategic objective:** Present the full offer, activate all scarcity triggers, drive the sale. This is the climax the entire sequence has been building toward.

### Pre-production

- [ ] Finalize the complete offer stack (core product + bonuses + guarantee)
- [ ] Define all scarcity elements (deadline, limited spots, bonus expiry, early-bird pricing)
- [ ] Write the full offer breakdown copy
- [ ] Prepare the price reveal and justification/anchoring
- [ ] Define the guarantee and risk-reversal language
- [ ] Prepare FAQ section based on PLC #1-3 comment analysis
- [ ] Set the open cart and close cart dates/times
- [ ] Prepare the order page / checkout flow
- [ ] Write urgency-based email sequence to support the SV

### Script Structure / Shot List

**Beat 1 — Recap the Journey**
- [ ] Brief recap of what you've covered across all 3 PLCs
- [ ] Remind them of the transformation/opportunity
- [ ] Re-establish positioning in one line
- [ ] Set the frame: "I promised I'd show you how to take this to the next level — here it is"

**Beat 2 — Re-State the Core Problem and Transformation**
- [ ] Articulate the pain/frustration they're still experiencing
- [ ] Contrast with the "after" picture you've been painting
- [ ] Bridge: "The gap between where you are and where you want to be — that's what this is designed to close"

**Beat 3 — Introduce the Product by Name**
- [ ] Reveal the product name
- [ ] One-line positioning statement: what it IS and who it's FOR
- [ ] Frame it as the vehicle for the transformation (they buy the destination, you provide the vehicle)

**Beat 4 — Walk Through the Offer (What They Get)**
- [ ] Break down each component/module with its specific benefit
- [ ] For each element: what it IS → what it DOES for them → what result it produces
- [ ] Stack value — each item adds to the perceived total value
- [ ] Include bonuses and explain why each bonus matters
- [ ] If applicable: community access, live calls, templates, tools, support

**Beat 5 — Social Proof / Results**
- [ ] Testimonials from past buyers or beta users
- [ ] Case studies showing real results
- [ ] Reference the energy and excitement from PLC comments
- [ ] Screenshots, numbers, specific outcomes wherever possible

**Beat 6 — Price Reveal + Value Anchoring**
- [ ] Anchor the value high first (total value of everything included)
- [ ] Reveal the actual price
- [ ] If offering payment plans, present them
- [ ] Frame the price against the transformation value ("What is this worth to you if it works?")
- [ ] Compare to alternatives (coaching, courses, DIY time cost)

**Beat 7 — Guarantee / Risk Reversal**
- [ ] State the guarantee clearly and confidently
- [ ] Remove the perceived risk of buying
- [ ] Make the guarantee specific (duration, terms, process)
- [ ] Position it as confidence in the product, not a safety net for doubt

**Beat 8 — Activate Full Scarcity**
- [ ] Fire all scarcity triggers at full force (seeded in PLC #3, now unleashed)
- [ ] Limited spots / limited time / limited bonuses / limited pricing
- [ ] State the exact deadline (date + time + timezone)
- [ ] Explain what happens when the deadline passes (price goes up, bonuses disappear, cart closes)
- [ ] Make scarcity REAL — don't manufacture fake urgency

**Beat 9 — Final Objection Handling**
- [ ] Address any remaining objections not yet covered
- [ ] "If you're thinking X, here's why that won't be an issue..."
- [ ] Target the final resistance: "Is this really for me?" → Yes, because...
- [ ] Handle the time objection, money objection, "not ready" objection

**Beat 10 — The Close (Call to Action)**
- [ ] Direct, clear CTA: "Click the button below / Go to [URL] / Register now"
- [ ] Repeat the core transformation one final time
- [ ] Paint one last vivid picture of their life after the transformation
- [ ] Create the fork-in-the-road moment: "You can keep doing what you've been doing... or you can..."
- [ ] End with confidence — you've earned this moment across 3 PLCs of pure value

### Post-production Check

- [ ] Offer is crystal clear — no confusion about what they get
- [ ] Price is justified through value anchoring
- [ ] Guarantee removes risk
- [ ] Scarcity is real and clearly stated with a specific deadline
- [ ] CTA is unmistakable — they know exactly what to do
- [ ] All links tested and working
- [ ] Order form functional
- [ ] Thank you page ready
- [ ] Confirmation emails configured

### Primary Mental Triggers Activated

- [ ] Scarcity (full force)
- [ ] Social Proof (testimonials, buyer momentum)
- [ ] Authority (consolidated through entire sequence)
- [ ] Events/Ritual (launch day is THE event)
- [ ] Community ("join the others who are already in")
- [ ] Trust (guarantee, transparency)

---

## OPEN CART EMAIL SEQUENCE (5-Day)

### Day 1 — Open Cart

**Email 1: Cart Open (morning)**
- [ ] Short, direct, link-focused
- [ ] "We're live" energy
- [ ] Primary CTA to sales page

**Email 2: Confirmation (~4h later)**
- [ ] Everything is working
- [ ] Address any early questions
- [ ] Secondary CTA

### Day 2 — Social Proof

- [ ] Talk about the great response
- [ ] Share early buyer testimonials if available
- [ ] "People are joining" momentum
- [ ] Link to sales page

### Day 3 — FAQ / Objections

- [ ] Longer email answering top questions
- [ ] Address remaining objections
- [ ] Always include link to sales page
- [ ] Can include mini-case study

### Day 4 — Scarcity Warning (24h)

- [ ] Message shifts to SCARCITY
- [ ] Absolutely clear about when closes
- [ ] What they lose if they don't act
- [ ] Urgency language increases

### Day 5 — Close Cart

**Email 1: Morning**
- [ ] "Closing TODAY"
- [ ] Reiterate deadline
- [ ] Final push

**Email 2: 6-8h before close**
- [ ] Last chance
- [ ] Countdown energy
- [ ] Strong urgency

**Email 3: Optional (1-2h before)**
- [ ] Final reminder
- [ ] "Doors closing in X hours"

### Critical Rule

> "Don't make the mistake of letting up on the last day. Send at least 2 emails. Most people are terrible procrastinators. You will see orders right up until the very last minute." — Jeff Walker

### Expected Sales Pattern

| Phase | % of Sales |
|-------|------------|
| Day 1 (Open) | 25% |
| Days 2-4 | 25% |
| Day 5 (Close) | 50% |

---

## SCARCITY TYPES (Choose 1-3)

### Type 1: Price Increase
- [ ] Launch price vs. regular price
- [ ] Clear deadline for price change
- [ ] Specific amount of increase

### Type 2: Bonus Removal
- [ ] Specific bonuses that disappear
- [ ] Value of bonuses stated
- [ ] Clear deadline

### Type 3: Offer Disappears
- [ ] Cart closes completely
- [ ] Next opportunity is [date] or never
- [ ] Most powerful form of scarcity

### Layering
- [ ] Can combine all 3 types for maximum effect
- [ ] Each layer adds urgency

### Critical Rule
> "The scarcity MUST BE REAL. If you say the offer closes, it CLOSES."

---

*Checklist Version: 3.0*
*Source: Launch (Jeff Walker) - Original + Updated 2021 Edition*
*Framework: Product Launch Formula - Complete Video Production*
