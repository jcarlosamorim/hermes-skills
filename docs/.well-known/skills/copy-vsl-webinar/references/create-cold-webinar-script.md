# Create Cold Webinar Script

## Purpose

Criar scripts de webinar otimizados para **audiências COLD** - pessoas que não conhecem você, não confiam em você, e são "cruéis" com seu tempo. Este framework é fundamentalmente diferente de webinars para audiências warm.

> "Cold audiences são cruéis. Eles não são seus amigos ainda. Se você começar com 'Oi pessoal, de onde vocês estão?', eles vão te destruir no chat. IMEDIATAMENTE pule para valor."
> — Jeremy Haynes

---

## Cold vs Warm: Diferenças Fundamentais

```yaml
cold_audience_reality:

  mindset:
    - "Não dão a mínima para você"
    - "São rápidos em julgar"
    - "Vão embora se não receberem valor IMEDIATAMENTE"
    - "Não toleram enrolação"

  what_they_want:
    - "Resultados e outcomes"
    - "Informação densa e valiosa"
    - "Provar que seu tempo vale a pena"
    - "Entender rapidamente se é para eles"

  what_they_hate:
    - "Welcome, where are you from?"
    - "Drop a 1 in the chat if..."
    - "Framing content (secrets, beliefs)"
    - "Qualquer coisa que pareça enrolação"

comparison_table:
  | Aspecto | Cold Audience | Warm Audience |
  |---------|---------------|---------------|
  | Frequência | Semanal ou 2x/semana | Mensal |
  | Intro | ZERO small talk | Pode ter um pouco |
  | Framing | Evitar | Pode usar |
  | Character content | Não | Sim, ser você mesmo |
  | Pitches | 3 pitches estratégicos | Pitch no final |
  | Duração | 60-90 min | Pode ser maior |
  | Show rate típico | 15-45% | 40-60% |
```

---

## Tier 0: Diagnostic Questions

```yaml
tier_0_diagnosis:

  audience_clarity:
    - Esta é realmente uma audiência COLD? (nunca interagiu com você?)
    - Você está excluindo warm audiences no targeting?
    - Qual o tamanho do mercado endereçável?

  offer_clarity:
    - Qual é o produto/preço?
    - É para affluent ($150k+/ano) ou general public?
    - O preço é $3,500 ou menos (direct checkout) ou mais (call)?

  content_readiness:
    - Você tem exemplos concretos para mostrar?
    - Tem case studies com números específicos?
    - Consegue entregar valor REAL em 20 minutos?

  logistics:
    - Quanto tempo de promoção? (máx 7 dias para cold)
    - Qual plataforma? (Zoom recomendado)
    - Tem alguém para plantar perguntas estratégicas?
```

---

## Inputs

```yaml
required:
  - webinar_title: "Título focado em RESULTADO (não em método)"
  - product_name: "Nome do produto/programa"
  - price: "Preço principal"
  - target_avatar: "Descrição do público-alvo"
  - main_outcome: "O resultado #1 que você entrega"
  - three_topics: "3 tópicos de valor que você vai cobrir"
  - case_studies: "Mínimo 3 case studies com números"

optional:
  - audience_type: "affluent | general_public (default: general_public)"
  - call_or_checkout: "call | checkout (default: call se >$3,500)"
  - duration: "60 | 90 minutos (default: 60)"
  - planted_questions: "Perguntas para plantar no Q&A"
```

---

## The 3-Pitch Cold Webinar Structure

### Overview Visual

```
┌─────────────────────────────────────────────────────────────────────┐
│              COLD WEBINAR - 3 PITCH STRUCTURE                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  SECTION 1: FIRST THIRD (0-20 min)                                  │
│  ├── Intro IMEDIATO (30 segundos máx)                               │
│  ├── Conteúdo Surface Level (alta visão)                            │
│  ├── PITCH #1 (2-5 min) - Introdução da oferta                      │
│  └── Q&A curto (2-5 min)                                            │
│                                                                      │
│  SECTION 2: SECOND THIRD (20-40 min)                                │
│  ├── Conteúdo com EXEMPLOS                                          │
│  ├── Case studies e provas                                          │
│  ├── PITCH #2 (2-5 min) - Framing (comprar velocidade)              │
│  └── Q&A curto (2-5 min)                                            │
│                                                                      │
│  SECTION 3: FINAL THIRD (40-60 min)                                 │
│  ├── Conteúdo mais PROFUNDO / exercício                             │
│  ├── Fazer eles COMEÇAREM a agir                                    │
│  ├── PITCH #3 (10-15 min) - Objection handling + full pitch         │
│  └── Q&A extenso (quanto precisar)                                  │
│                                                                      │
│  RETENTION GOAL:                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │ 100%|████                                                    │   │
│  │     |  ████                                                  │   │
│  │ 50% |      ████████                                          │   │
│  │     |              ██████████████████                        │   │
│  │   0%|────────────────────────────────────────────────────────│   │
│  │     0min        20min        40min        60min              │   │
│  └──────────────────────────────────────────────────────────────┘   │
│  (Drop suave, não íngreme no início)                                │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Section 1: First Third (0-20 minutes)

### 1.1 The Cold Intro (30 segundos MÁXIMO)

```markdown
## O que NÃO fazer:

"E aí pessoal, tudo bem? Meu nome é [Nome], é muito bom ter vocês aqui.
De onde vocês estão assistindo? Manda aí no chat!
Quem aqui quer [resultado]? Manda um 1 no chat!"

❌ Isso DESTRÓI sua credibilidade com cold audiences.

---

## O que FAZER:

"E aí, [Nome] aqui.

Nos próximos [60] minutos, vou te mostrar como [RESULTADO ESPECÍFICO] -
mesmo que você [OBJEÇÃO COMUM].

Vou passar por [TÓPICO 1], [TÓPICO 2], e [TÓPICO 3].

Vou mostrar exemplos reais de pessoas que [RESULTADO].

Sem enrolação. Direto ao ponto.

Vamos começar."

✅ Value density desde o primeiro segundo.
```

### 1.2 Surface Level Content

```yaml
first_third_content:

  approach: "Visão de alto nível - O QUÊ e POR QUÊ"

  structure:
    - "Introduzir o framework/método em alto nível"
    - "Explicar por que funciona (sem entrar em táticas)"
    - "Mostrar o resultado que é possível"
    - "Dar 1-2 exemplos rápidos"

  for_affluent:
    - "Manter em nível de ESTRATÉGIA"
    - "Ricos não querem táticas - querem ideia"
    - "Falar sobre outcomes, não processos"

  for_general_public:
    - "Pode peperar algumas táticas"
    - "Mas manter majoritariamente high-level"
    - "Público geral precisa de mais detalhes para confiar"

  time_allocation: "12-15 minutos de conteúdo"
```

### 1.3 Pitch #1: Introdução da Oferta

```markdown
## Slide: Transição para Pitch

"Antes de continuar e ir mais fundo nesses tópicos, quero fazer uma pausa.

Sei que alguns de vocês já estão prontos para dar o próximo passo.
Não quero fazer vocês esperarem.

Me dá 2 minutos para apresentar como podemos trabalhar juntos,
e depois volto direto pro conteúdo.

Pode ser?"

---

## Pitch #1 Script (2-5 minutos)

"[NOME DO PRODUTO] é [DESCRIÇÃO EM UMA FRASE].

Custa [PREÇO].
[Se tiver parcelamento: Ou [X]x de [VALOR].]

Aqui está o que você recebe:
- [COMPONENTE 1]
- [COMPONENTE 2]
- [COMPONENTE 3]

Para quem está pronto, o link está [NO CHAT / ABAIXO].
[Se for call: Você vai preencher uma aplicação rápida e agendar uma conversa.]
[Se for checkout: É só clicar e finalizar a compra.]

Agora, voltando ao conteúdo..."

---

## Notas do Pitch #1:
- Pedir PERMISSÃO para pitchar (cold audiences apreciam)
- Ser direto: produto, preço, o que recebe
- NÃO fazer pitch longo
- Voltar IMEDIATAMENTE para conteúdo
```

### 1.4 Q&A #1 (2-5 minutos)

```yaml
qa_1_strategy:

  purpose: "Transição suave de volta para conteúdo"

  ideal_questions:
    planted:
      - "Para quem isso é ideal?"
      - "Para quem NÃO é?"
    natural:
      - Qualquer pergunta sobre o conteúdo surface
      - Evitar deep dives - guardar para depois

  handling:
    - "Responder de forma que leva ao próximo tópico"
    - "Se pergunta for muito específica: 'Ótima pergunta, vou cobrir isso daqui a pouco'"

  transition: "Ótimas perguntas. Agora vamos mais fundo em [TÓPICO]..."
```

---

## Section 2: Second Third (20-40 minutes)

### 2.1 Content with Examples

```yaml
second_third_content:

  approach: "Mostrar COMO funciona com EXEMPLOS"

  structure:
    - "Pegar cada tópico do first third"
    - "Mostrar exemplos reais de cada um"
    - "Demonstrar, não só falar"
    - "Case studies detalhados"

  elements_to_include:
    - "Screenshots de resultados"
    - "Números específicos (não vagos)"
    - "Histórias de clientes"
    - "Demonstração se possível"

  for_affluent:
    - "Exemplos de pessoas em situações similares"
    - "Foco em outcomes, não processos"
    - "Manter relativamente high-level"

  for_general_public:
    - "Mais detalhes táticos"
    - "Passo a passo quando relevante"
    - "Mais hand-holding"

  time_allocation: "12-15 minutos de conteúdo"
```

### 2.2 Pitch #2: Framing Pitch

```markdown
## Pitch #2 Script (2-5 minutos)

"Já falei sobre a oferta, então não vou repetir tudo.

Mas deixa eu te fazer uma pergunta:

Você pode sair daqui e fazer tudo isso sozinho.
Eu te dei informação suficiente para começar.

Mas quanto tempo isso vai levar?
Quantos erros você vai cometer no caminho?
Quanto vai custar esses erros?

O que estou oferecendo é VELOCIDADE.
É SUPORTE enquanto você faz.
É a CERTEZA de que está fazendo certo.

Porque aqui está a verdade:
Você está aqui de graça.
Quanto dessa informação você vai lembrar amanhã?
Quanto você vai realmente implementar?

Sabe o que faria você implementar?
Ter investido dinheiro nisso.

Não é sobre a informação - você tem a informação.
É sobre o COMPROMETIMENTO.

Quem paga, presta atenção.
Quem paga, implementa.
Quem paga, tem skin in the game.

Para quem está pronto para comprar velocidade,
para comprar suporte,
para investir no próprio comprometimento...

O link está [NO CHAT].

Próxima seção..."
```

### 2.3 Q&A #2 (2-5 minutos)

```yaml
qa_2_strategy:

  purpose: "Validar interesse e resolver dúvidas"

  ideal_questions:
    planted:
      - "Faz sentido para quem está começando do zero?"
      - "E se eu não tiver muito tempo?"
    natural:
      - Perguntas sobre os exemplos mostrados
      - Dúvidas sobre aplicação

  handling:
    - "Usar perguntas como segue para próximo tópico"
    - "Se for objeção, reconhecer e seguir"

  transition: "Agora vamos para a parte mais importante..."
```

---

## Section 3: Final Third (40-60 minutes)

### 3.1 Deep Content / Getting Them Started

```yaml
third_third_content:

  approach: "Fazer eles COMEÇAREM a agir"

  structure:
    - "O conteúdo mais profundo"
    - "Um exercício ou demonstração prática"
    - "Fazê-los experimentar o processo"
    - "Mostrar onde vão travar sem ajuda"

  key_insight: |
    Se você conseguir fazer eles COMEÇAREM a implementar,
    eles vão rapidamente perceber que precisam de ajuda.

    O objetivo é "edging" - dar suficiente para começar,
    mas não tanto que conseguem fazer sozinhos.

  examples:
    - "Um exercício rápido que podem fazer agora"
    - "Uma mini-avaliação do negócio deles"
    - "Um diagnóstico que revela problemas"
    - "Um primeiro passo que mostra a complexidade"

  time_allocation: "10-15 minutos de conteúdo"
```

### 3.2 Pitch #3: Full Objection Handling + Close

```markdown
## Pitch #3 Structure (10-15 minutos)

### Parte A: Objection Handling (5-7 min)

"Antes de finalizar, deixa eu abordar algumas coisas que você
provavelmente está pensando.

**'É muito caro'**
[Resposta completa]

**'Não tenho tempo'**
[Resposta completa]

**'Já tentei antes'**
[Resposta completa]

**'Preciso pensar'**
[Resposta completa]"

---

### Parte B: Full Pitch (5-7 min)

"Então, recapitulando.

[NOME DO PRODUTO] inclui:

✅ [COMPONENTE 1] - [valor R$]
✅ [COMPONENTE 2] - [valor R$]
✅ [COMPONENTE 3] - [valor R$]
✅ [BÔNUS 1] - [valor R$]
✅ [BÔNUS 2] - [valor R$]

Valor total: R$ [SOMA]

Seu investimento hoje: R$ [PREÇO]

[Garantia]

[Urgência/Escassez se houver]

O link está [ONDE].

[Se for call]: Preenche a aplicação, agenda uma conversa,
e vamos ver se faz sentido para você.

[Se for checkout]: Clica, finaliza, e você tem acesso imediato."

---

### Parte C: Final Push

"Duas opções agora:

1. Você fecha essa página, volta pra sua vida,
   e daqui 6 meses está no mesmo lugar.

2. Você toma uma decisão, investe em você,
   e daqui 6 meses tem [RESULTADO].

A escolha é sua.

Para quem está pronto, o link está no chat.

Vou abrir para perguntas agora."
```

### 3.3 Q&A Final (sem limite de tempo)

```yaml
qa_final_strategy:

  purpose: "Converter quem ainda está em dúvida"

  approach:
    - "Começar perguntando: Quem já clicou e entrou?"
    - "Celebrar quem comprou (social proof)"
    - "Responder objeções como oportunidades de close"

  objection_handling_pattern:
    1: "Reconhecer a preocupação"
    2: "Reframar a pergunta"
    3: "Responder direcionando para a oferta"
    4: "Fechar: 'Isso responde? Então vai lá.'"

  planted_questions_ideal:
    - "Alguém pergunta sobre garantia"
    - "Alguém pergunta sobre suporte"
    - "Alguém compartilha que comprou"

  closing_urgency:
    - "Lembrar de deadlines se houver"
    - "Lembrar de bônus que expiram"
    - "Última chamada antes de encerrar"
```

---

## Duration Guidelines

```yaml
duration_by_audience:

  affluent_audience:
    recommended: "60-90 minutos MÁXIMO"
    reason: "Ricos valorizam tempo, não toleram enrolação"
    content_style: "High-level, estratégico"

  general_public:
    recommended: "90-180 minutos"
    reason: "Precisam de mais hand-holding e confiança"
    content_style: "Mais tático, mais detalhado"

cold_webinar_specifics:
  max_duration: "90 minutos"
  reason: "Cold não tem paciência para mais que isso"
  ideal_for_most: "60 minutos"
```

---

## Promotion Timeline

```yaml
cold_webinar_promotion:

  max_lead_time: "7 dias"
  ideal_lead_time: "3-4 dias"

  reason: |
    Cold audiences têm interesse que decai rapidamente.
    Quanto mais perto do webinar, maior o show rate.
    Pessoas que registram no dia anterior têm MAIOR show rate.

  ads_strategy:
    - "Não mencionar datas específicas nos ads"
    - "Não mencionar 'webinar' - usar 'training' ou 'workshop'"
    - "Evergreen creative que direciona para página de registro"
    - "Página de registro atualiza automaticamente para próxima data"

  budget_allocation:
    - "Lifetime budget para período de promoção"
    - "OU daily budget se webinar é semanal/perpétuo"
```

---

## Show Rate Optimization

```yaml
show_rate_tactics:

  expected_baseline:
    cold: "15-20%"
    with_optimization: "40-50%"

  tactics:
    - "Hammer Them Strategy (retargeting + content)"
    - "6 emails per day sequence"
    - "Confirmation page com video"
    - "SMS reminders"
    - "Setter calls se tiver equipe"

  confirmation_page_elements:
    - "Video de 2-3 min sobre o que esperar"
    - "Add to calendar prominente"
    - "Reforço do que vão aprender"
    - "Testimonial ou two de webinars anteriores"
```

---

## Quality Checklist

```yaml
pre_webinar_checklist:

  content:
    - "[ ] Intro ZERO small talk (30 seg máx)"
    - "[ ] Conteúdo value-dense desde o início"
    - "[ ] 3 pitches estruturados"
    - "[ ] Case studies com números específicos"
    - "[ ] Exercício/demonstração no third third"
    - "[ ] Objection handling completo"

  logistics:
    - "[ ] Perguntas plantadas preparadas"
    - "[ ] Link de compra/aplicação testado"
    - "[ ] Slides sem enrolação"
    - "[ ] Timer para não passar do tempo"

  mindset:
    - "[ ] Lembrar: cold não dá a mínima para você"
    - "[ ] Lembrar: value density é tudo"
    - "[ ] Lembrar: 3 pitches, não só 1 no final"
```

---

## Output Deliverables

```yaml
deliverables:

  primary:
    - complete_script: |
        Script palavra por palavra
        3 seções claramente divididas
        3 pitches completos
        Q&A strategy para cada seção

    - slide_outline: |
        Títulos dos slides
        Notas de tempo por seção
        Indicações de quando pitchar

  secondary:
    - objection_responses: |
        Top 5 objeções com respostas completas

    - planted_questions: |
        10 perguntas para plantar no Q&A
        Momento ideal para cada uma

  optional:
    - promotion_plan: |
        Timeline de promoção (7 dias)
        Ads e landing page guidelines
```

---

## Version History

```yaml
version: "1.0"
created: "2025-01-24"
source: "Jeremy Haynes - Cold vs Warm Webinar Best Practices"
key_insight: |
  Cold webinars são fundamentalmente diferentes de warm.
  O maior erro é tratar cold como warm.
  Value density + 3 pitches = alta conversão de cold.
```

---

*Task: Create Cold Webinar Script*
*Version: 1.0*
*Framework: Jeremy Haynes Cold Webinar System*
