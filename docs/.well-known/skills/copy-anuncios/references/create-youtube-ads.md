# Create YouTube Ads Task

## Purpose

Criar scripts de anúncios para YouTube que capturam atenção antes do skip, mantêm engajamento e convertem espectadores em leads ou clientes. Este task integra metodologias dos principais especialistas mundiais: Google ABCD Framework, Tom Breeze (Viewability), Billy Gene Shaw, Aleric Heck (AdOutreach), e Jake Larsen (Video Power Marketing).

## Research Foundation

Este task é baseado em pesquisa documentada em:
`docs/research/youtube-ads-methodology-research.md`

**Metodologias Integradas:**
- Google ABCD Framework (Attention, Branding, Connection, Direction)
- Tom Breeze 5 A's (Attention, Authority, Audience, Action, Ascension)
- Billy Gene Shaw Million-Dollar Formula (Entertainment + Education + Offer)
- Aleric Heck Value-Ad Framework (Hook → Educate → CTA)
- Jake Larsen Video Ad Formula (Capture → Relationship → Action)

---

## When to Use

```yaml
Primary Use Cases:
  - YouTube In-Stream Ads (skippable e non-skippable)
  - YouTube Shorts Ads
  - YouTube Bumper Ads (6s)
  - YouTube Discovery Ads (In-Feed)
  - Demand Gen Campaigns
  - Pre-roll para conteúdo próprio
  - Retargeting via YouTube
  - Video Action Campaigns

Ad Objectives:
  - Brand Awareness
  - Consideration/Engagement
  - Lead Generation
  - Direct Sales
  - App Installs
  - Website Traffic
```

---

## Inputs

```yaml
required:
  product_or_service:
    description: "Nome e descrição do produto/serviço"
    example: "Curso de YouTube Ads para Empreendedores"

  target_avatar:
    description: "Descrição detalhada do espectador ideal"
    example: "Empreendedor digital 25-45 anos, gasta R$5k+/mês em ads"

  ad_format:
    description: "Formato de YouTube Ad"
    options:
      - skippable_in_stream    # TrueView, skip após 5s
      - non_skippable          # 15s máximo, não pode pular
      - bumper                 # 6s máximo, não pode pular
      - shorts                 # Vertical, até 60s
      - discovery              # Thumbnail + título, clique para ver
      - demand_gen             # Multi-format AI-optimized

  ad_objective:
    description: "Objetivo principal"
    options:
      - awareness              # Brand lift, reach
      - consideration          # Engagement, views
      - leads                  # Lead generation
      - sales                  # Direct conversion
      - traffic                # Website visits

  main_cta:
    description: "Ação desejada do viewer"
    example: "Baixar guia grátis, Agendar call, Comprar agora"

optional:
  ad_duration:
    description: "Duração desejada"
    options: [6s, 15s, 30s, 60s, 90s, 120s+]
    default: "60s para skippable, 15s para non-skippable"

  landing_page:
    description: "URL de destino"

  unique_mechanism:
    description: "O que torna sua solução única"

  social_proof:
    description: "Resultados, depoimentos, números"

  budget_context:
    description: "Contexto de budget"
    options: [testing, scaling, established]

  copywriter_style:
    description: "Estilo de copywriter preferido"
    default: "Hybrid (best practices de todos)"

  competitor_ads:
    description: "Links de ads de concorrentes para referência"

  existing_assets:
    description: "Vídeos, depoimentos, resultados existentes"
```

---

## Workflow

### Phase 1: Strategic Foundation

#### Step 1.1: Format Selection Matrix

```yaml
FORMAT SELECTION BY OBJECTIVE:

┌─────────────────┬─────────────────────────────────────────────────┐
│ Objetivo        │ Formato Recomendado                             │
├─────────────────┼─────────────────────────────────────────────────┤
│ AWARENESS       │ Bumper (6s) + Non-Skippable (15s)              │
│                 │ → Máximo reach, mensagem curta                  │
├─────────────────┼─────────────────────────────────────────────────┤
│ CONSIDERATION   │ Skippable In-Stream (60-90s) + Discovery       │
│                 │ → Valor educacional, engajamento               │
├─────────────────┼─────────────────────────────────────────────────┤
│ LEADS           │ Skippable In-Stream (60-120s)                  │
│                 │ → Story + valor + CTA lead magnet              │
├─────────────────┼─────────────────────────────────────────────────┤
│ SALES           │ Skippable In-Stream (90-180s)                  │
│                 │ → Full pitch, prova social, oferta             │
├─────────────────┼─────────────────────────────────────────────────┤
│ TRAFFIC         │ Skippable + Discovery                          │
│                 │ → Curiosity hooks, CTAs claros                 │
├─────────────────┼─────────────────────────────────────────────────┤
│ MOBILE/GEN Z    │ Shorts Ads (vertical 9:16)                     │
│                 │ → Native feel, hook em 0.5s                    │
└─────────────────┴─────────────────────────────────────────────────┘

DURATION GUIDELINES:

Skippable In-Stream:
  - Lead Gen: 60-90s (valor + CTA)
  - Direct Sale: 90-180s (full pitch)
  - Consideration: 30-60s (hook + tease)

Non-Skippable:
  - Always: 15s (máximo permitido)

Bumper:
  - Always: 6s (máximo permitido)

Shorts:
  - Recommended: 15-30s (atenção curta)
  - Maximum: 60s
```

#### Step 1.2: Avatar Deep Dive

```yaml
AVATAR ANALYSIS FRAMEWORK:

Demographics:
  - Idade:
  - Gênero:
  - Localização:
  - Renda/Poder aquisitivo:
  - Ocupação:

Psychographics:
  - O que AMAM:
  - O que ODEIAM:
  - O que TEMEM:
  - O que DESEJAM profundamente:
  - O que os FRUSTRA diariamente:

Behavioral:
  - Onde passam tempo online:
  - Que tipo de conteúdo consomem:
  - Quem seguem/admiram:
  - Que canais assistem no YouTube:
  - Que keywords pesquisam:

Purchase Triggers:
  - O que os faz agir AGORA:
  - Objeções comuns:
  - Processo de decisão:
  - Quem influencia a decisão:

QUALIFICATION STATEMENT:
"Se você é [descrição específica] que [situação atual] e quer [resultado desejado]..."
```

### Phase 2: Script Architecture

#### Step 2.1: The 5-Second Rule (Critical)

```yaml
THE FIRST 5 SECONDS - ONDE ADS VENCEM OU PERDEM:

Statistics:
  - 65-75% dos viewers skipam na primeira oportunidade
  - Decisão de skip: formada em 2-3 segundos
  - Top 25% de ads: <25% skip rate

OBJETIVOS EM 5 SEGUNDOS:
  1. Interromper padrão (ATENÇÃO)
  2. Qualificar o avatar (RELEVÂNCIA)
  3. Prometer valor (BENEFÍCIO)
  4. Criar curiosidade (CONTINUAR)

HOOK FRAMEWORKS (escolha 1-2):

1. PATTERN INTERRUPT
   ┌────────────────────────────────────────────────────┐
   │ "ESPERA. Antes de pular, você precisa ouvir isso" │
   │ "Isso vai parecer estranho, mas funciona..."      │
   │ [Ação visual inesperada + statement provocativo]  │
   └────────────────────────────────────────────────────┘

2. DIRECT QUALIFICATION
   ┌────────────────────────────────────────────────────┐
   │ "Se você é [avatar] que [situação], não pula."    │
   │ "Atenção [avatar]: isso é exclusivo pra você."   │
   │ "Você gasta mais de [X] em [área]? Presta atenção"│
   └────────────────────────────────────────────────────┘

3. BOLD CLAIM
   ┌────────────────────────────────────────────────────┐
   │ "[Resultado] em [tempo]. Parece impossível?"      │
   │ "[X] pessoas já [resultado]. Você é o próximo."   │
   │ "Eu [resultado impressionante] e vou mostrar como"│
   └────────────────────────────────────────────────────┘

4. PROVOCATIVE QUESTION
   ┌────────────────────────────────────────────────────┐
   │ "Por que [maioria] [falha] enquanto [minoria]     │
   │  [sucede]?"                                       │
   │ "Você sabe o erro #1 que [avatares] cometem?"    │
   │ "O que [experts] não querem que você saiba?"      │
   └────────────────────────────────────────────────────┘

5. CURIOSITY GAP
   ┌────────────────────────────────────────────────────┐
   │ "Descobri algo sobre [tema] que muda tudo."       │
   │ "Existe um segredo que [experts] não contam."    │
   │ "Depois de [X anos], finalmente entendi..."       │
   └────────────────────────────────────────────────────┘

6. STORY OPENING
   ┌────────────────────────────────────────────────────┐
   │ "Há [tempo], eu estava exatamente onde você está" │
   │ "Quando [evento aconteceu], tudo mudou."          │
   │ "Eu perdi [algo] até descobrir [solução]."       │
   └────────────────────────────────────────────────────┘

7. STATISTIC SHOCK
   ┌────────────────────────────────────────────────────┐
   │ "93% dos [avatares] cometem este erro..."         │
   │ "Apenas 3% sabem sobre isso..."                   │
   │ "R$[X] bilhões são desperdiçados em..."          │
   └────────────────────────────────────────────────────┘

8. NEGATIVE/CONTROVERSY
   ┌────────────────────────────────────────────────────┐
   │ "Pare de fazer [erro comum]."                     │
   │ "Tudo que te disseram sobre [tema] está errado." │
   │ "[Método popular] está te prejudicando."          │
   └────────────────────────────────────────────────────┘
```

#### Step 2.2: Visual Hook Strategies

```yaml
VISUAL HOOKS (primeiros 2 segundos):

MOVEMENT (Movimento):
  - Comece com movimento, não estático
  - Pessoa entrando em frame
  - Zoom in/out rápido
  - Objeto sendo mostrado/jogado
  - Ação acontecendo

FRAMING (Enquadramento):
  - Close-up de rosto → conexão
  - Unusual angle → curiosidade
  - Before/After setup → prova
  - Product in action → demonstração

COLOR/CONTRAST:
  - Cores vibrantes vs. fundo neutro
  - Highlight no elemento principal
  - Consistência com branding
  - Text overlay contrastante

UNEXPECTED ELEMENTS:
  - Props inusitados
  - Costumes/personagens
  - Locação inesperada
  - Situação absurda

AUDIO HOOKS:
  - Sound effect de abertura
  - Primeira palavra = impactante
  - Não comece com "Oi, meu nome é..."
  - Tom confiante e energético
```

### Phase 3: Script Templates by Format

#### Step 3.1: 6-Second Bumper Template

```markdown
═══════════════════════════════════════════════════════════════
BUMPER AD TEMPLATE (6 SEGUNDOS)
═══════════════════════════════════════════════════════════════

STRUCTURE:
[0-2s] VISUAL IMPACT + HOOK
[2-4s] PRODUCT/BENEFIT (3-5 palavras)
[4-6s] LOGO + TAGLINE + URL

───────────────────────────────────────────────────────────────
TEMPLATE A: PRODUCT FOCUS
───────────────────────────────────────────────────────────────
[VISUAL: Produto em ação]
"[Produto]. [Benefício em 3 palavras]."
[LOGO + URL]

Exemplo:
[VISUAL: App sendo usado]
"FitTrack. Resultados em 30 dias."
[LOGO: FitTrack + fittrack.com]

───────────────────────────────────────────────────────────────
TEMPLATE B: PROBLEM-SOLUTION
───────────────────────────────────────────────────────────────
"[Problema]? [Solução]."
[LOGO + URL]

Exemplo:
"Ads sem resultado? YouTube Ads resolve."
[LOGO + URL]

───────────────────────────────────────────────────────────────
TEMPLATE C: TAGLINE IMPACT
───────────────────────────────────────────────────────────────
[VISUAL: Brand imagery]
"[Tagline memorável]"
[LOGO + URL]

Exemplo:
[VISUAL: Clientes felizes]
"Transforme cliques em clientes."
[LOGO + URL]

═══════════════════════════════════════════════════════════════
```

#### Step 3.2: 15-Second Non-Skippable Template

```markdown
═══════════════════════════════════════════════════════════════
NON-SKIPPABLE TEMPLATE (15 SEGUNDOS)
═══════════════════════════════════════════════════════════════

STRUCTURE:
[0-3s]   HOOK - Interromper + qualificar
[3-10s]  VALUE - Benefício principal + diferencial
[10-15s] CTA - Ação clara + urgência

───────────────────────────────────────────────────────────────
TEMPLATE A: PROBLEM-SOLUTION
───────────────────────────────────────────────────────────────
[HOOK - 0-3s]
"[Avatar]? Cansado de [problema]?"

[VALUE - 3-10s]
"[Produto] resolve [problema] em [tempo].
[Benefício principal] sem [dor evitada]."

[CTA - 10-15s]
"[Ação]. Link na descrição. [Urgência]."

───────────────────────────────────────────────────────────────
EXEMPLO COMPLETO:
───────────────────────────────────────────────────────────────
"Empreendedor? Cansado de leads que não convertem?

Nosso método de YouTube Ads gera leads 3x mais qualificados.
Clientes que já querem comprar.

Clique no link e baixe o guia grátis. Só essa semana."

───────────────────────────────────────────────────────────────
TEMPLATE B: DIRECT PITCH
───────────────────────────────────────────────────────────────
[HOOK - 0-3s]
"[Resultado] em [tempo]. Quer saber como?"

[VALUE - 3-10s]
"[Número] de [avatares] já conseguiram com [Produto].
[Benefício diferenciador]."

[CTA - 10-15s]
"Clique agora e descubra. [Urgência]."

───────────────────────────────────────────────────────────────
TEMPLATE C: SOCIAL PROOF LEAD
───────────────────────────────────────────────────────────────
[HOOK - 0-3s]
"[Cliente] faturou [resultado] usando isso."

[VALUE - 3-10s]
"[Produto] é o método que [descrição simples].
Funciona para [avatares]."

[CTA - 10-15s]
"Quer o mesmo resultado? Link abaixo."

═══════════════════════════════════════════════════════════════
```

#### Step 3.3: 30-Second Skippable Template

```markdown
═══════════════════════════════════════════════════════════════
SKIPPABLE TEMPLATE (30 SEGUNDOS)
═══════════════════════════════════════════════════════════════

STRUCTURE:
[0-5s]   HOOK - Pattern interrupt + qualificação
[5-15s]  PROBLEM - Agitar dor + consequências
[15-25s] SOLUTION - Seu produto + benefício
[25-30s] CTA - Ação + urgência

───────────────────────────────────────────────────────────────
TEMPLATE COMPLETO:
───────────────────────────────────────────────────────────────

[HOOK - 0-5s]
"Se você gasta mais de R$5.000 em ads por mês e não vê retorno,
os próximos 25 segundos podem mudar seu negócio."

[PROBLEM - 5-15s]
"A maioria dos empreendedores desperdiça dinheiro em tráfego frio.
Leads que não atendem. Campanhas que não escalam.
E mês após mês, o mesmo resultado."

[SOLUTION - 15-25s]
"YouTube Ads é diferente. Você anuncia onde seu cliente já está
buscando solução. Leads 3x mais qualificados.
[X] empreendedores já usam nosso método."

[CTA - 25-30s]
"Clique no link abaixo e baixe o guia grátis.
Descubra como escalar com YouTube Ads."

───────────────────────────────────────────────────────────────
VISUAL DIRECTION:
───────────────────────────────────────────────────────────────
[0-5s]   Close-up, olhando para câmera, movimento
[5-15s]  Intercalar talking head com B-roll de frustração
[15-25s] Screenshots de resultados, produto em uso
[25-30s] Tela limpa com URL, seta apontando

═══════════════════════════════════════════════════════════════
```

#### Step 3.4: 60-Second Skippable Template

```markdown
═══════════════════════════════════════════════════════════════
SKIPPABLE TEMPLATE (60 SEGUNDOS)
═══════════════════════════════════════════════════════════════

STRUCTURE:
[0-5s]   HOOK - Capture + qualifique + prometa
[5-15s]  CONTEXT - Story ou credencial
[15-30s] PROBLEM - Aprofunde a dor
[30-45s] SOLUTION - Seu produto + mecanismo
[45-55s] PROOF - Social proof stacking
[55-60s] CTA - Ação + urgência

───────────────────────────────────────────────────────────────
TEMPLATE VALUE-AD (Aleric Heck Style):
───────────────────────────────────────────────────────────────

[HOOK - 0-5s]
"Se você é empreendedor digital que quer escalar com anúncios
mas está cansado de desperdiçar dinheiro... presta atenção."

[CONTEXT - 5-15s]
"Nos últimos 5 anos, ajudei mais de 2.000 empresas a escalar
usando YouTube Ads. E vou te mostrar exatamente o que funciona."

[PROBLEM - 15-30s]
"O problema é que a maioria tenta copiar o que funciona no
Facebook ou Instagram. Mas YouTube é diferente.
As pessoas estão buscando soluções, não scrollando distraídas.
E se você não sabe capturar essa atenção nos primeiros 5 segundos,
está literalmente queimando dinheiro."

[SOLUTION - 30-45s]
"Por isso criei o Método SCALE para YouTube Ads.
É um sistema que identifica seu cliente ideal,
cria hooks que impedem o skip, e otimiza sua campanha
para gerar leads que já querem comprar.
Funciona porque você aparece exatamente quando eles estão
buscando solução."

[PROOF - 45-55s]
"João usou o método e triplicou leads em 30 dias.
Maria reduziu custo por lead em 60%.
Mais de 500 alunos já aplicaram com resultados."

[CTA - 55-60s]
"Quer aprender o método completo?
Clique no link abaixo e acesse a aula gratuita.
Mas corre, fica disponível só por tempo limitado."

───────────────────────────────────────────────────────────────
VISUAL DIRECTION:
───────────────────────────────────────────────────────────────
[0-5s]   Close-up + movimento + energia
[5-15s]  Credenciais visuais (logos, números)
[15-30s] B-roll de frustração + pain points
[30-45s] Demonstração do método/produto
[45-55s] Screenshots de depoimentos, resultados
[55-60s] URL grande + seta + urgência visual

═══════════════════════════════════════════════════════════════
```

#### Step 3.5: 90-Second Skippable Template (Long-Form)

```markdown
═══════════════════════════════════════════════════════════════
SKIPPABLE TEMPLATE (90 SEGUNDOS)
═══════════════════════════════════════════════════════════════

STRUCTURE:
[0-5s]   HOOK - Pattern interrupt forte
[5-20s]  STORY - Sua jornada ou do cliente
[20-40s] PROBLEM - Deep dive na dor
[40-60s] SOLUTION - Mecanismo único
[60-75s] PROOF - Stack de evidências
[75-85s] OFFER - O que recebem
[85-90s] CTA - Fechamento forte

───────────────────────────────────────────────────────────────
TEMPLATE STORYTELLING (Billy Gene Style):
───────────────────────────────────────────────────────────────

[HOOK - 0-5s]
"Há 3 anos, eu estava R$50.000 no negativo.
Hoje faturo 7 dígitos. E tudo começou com um YouTube Ad."

[STORY - 5-20s]
"Eu era como você provavelmente é agora.
Tentava de tudo: Facebook Ads, Instagram, Google.
Gastava milhares por mês e mal pagava os custos.
Cheguei a pensar em desistir do meu negócio."

[PROBLEM - 20-40s]
"O problema não era eu. Era onde eu anunciava.
Facebook te mostra para pessoas que estão distraídas.
Instagram é um mar de scrolling sem fim.
Ninguém está lá para resolver problemas.
Estão lá para passar tempo.
E eu estava pagando caro para interromper quem não queria ser interrompido."

[SOLUTION - 40-60s]
"Então descobri YouTube Ads.
E entendi: aqui as pessoas BUSCAM soluções.
Quando alguém pesquisa 'como escalar meu negócio',
elas QUEREM encontrar algo.
Criei um método para aparecer exatamente nesses momentos.
Com hooks que capturam antes do skip.
Com mensagens que convertem porque são relevantes.
Chamei de Método SCALE."

[PROOF - 60-75s]
"Nos últimos 12 meses:
- Mais de 500 alunos aplicaram
- R$2.4 milhões gerados em vendas combinadas
- Média de 3.2x de retorno sobre investimento
Carlos: 'Primeiro mês, R$47k em vendas.'
Ana: 'Finalmente entendi como escalar.'"

[OFFER - 75-85s]
"Criei uma aula gratuita que mostra o passo a passo.
Você vai aprender os 3 pilares do método.
Como criar hooks que impedem o skip.
E como configurar suas primeiras campanhas."

[CTA - 85-90s]
"Clique no link abaixo agora.
A aula fica disponível por tempo limitado.
Te vejo do outro lado."

═══════════════════════════════════════════════════════════════
```

#### Step 3.6: YouTube Shorts Template

```markdown
═══════════════════════════════════════════════════════════════
YOUTUBE SHORTS AD TEMPLATE (15-30 SEGUNDOS)
═══════════════════════════════════════════════════════════════

SPECS:
- Aspect Ratio: 9:16 (vertical)
- Sound: On by default
- Duration: 15-30s recomendado
- Text: Captions grandes
- Feel: Nativo, não pareça ad

STRUCTURE:
[0-1s]  INSTANT HOOK - Primeiro frame é tudo
[1-5s]  VALUE BOMB - Entregue algo útil imediatamente
[5-20s] EXPAND - Desenvolva o ponto
[20-25s] CTA - Rápido e direto

───────────────────────────────────────────────────────────────
TEMPLATE A: QUICK TIP
───────────────────────────────────────────────────────────────
[0-1s]
[TEXT OVERLAY: "O segredo que ninguém conta"]
"O erro #1 em YouTube Ads..."

[1-5s]
"...é copiar Facebook.
YouTube é busca. Não scroll."

[5-15s]
"Quando alguém pesquisa 'como escalar negócio',
elas QUEREM encontrar você.
Use isso. Crie ads que respondem perguntas."

[15-20s]
"Link na bio pra aula completa.
Segue pra mais dicas."

───────────────────────────────────────────────────────────────
TEMPLATE B: RESULT SHOWCASE
───────────────────────────────────────────────────────────────
[0-1s]
[TEXT OVERLAY: "R$47k em 30 dias"]
"Esse é o resultado do Carlos."

[1-10s]
"Ele aplicou 3 coisas:
1. Hook em 5 segundos
2. Targeting por intenção
3. Oferta irresistível"

[10-20s]
"YouTube Ads mudou o jogo dele.
Quer o mesmo? Link na bio."

───────────────────────────────────────────────────────────────
TEMPLATE C: PATTERN INTERRUPT
───────────────────────────────────────────────────────────────
[0-1s]
[AÇÃO VISUAL INESPERADA]
"NÃO faça YouTube Ads..."

[1-5s]
"...se você quer leads frios que não atendem.

Mas SE você quer..."

[5-15s]
"Leads que JÁ buscam solução.
Que QUEREM falar com você.
Que estão PRONTOS para comprar."

[15-20s]
"Então YouTube Ads é pra você.
Link na bio."

───────────────────────────────────────────────────────────────
SHORTS BEST PRACTICES:
───────────────────────────────────────────────────────────────
✓ Nativo ao formato (não adapte horizontal)
✓ Hook em 0.5 segundos (primeiro frame)
✓ Text overlays GRANDES (leitura rápida)
✓ Som on por default (aproveite)
✓ Captions sempre (muitos leem)
✓ CTA curto e direto
✓ Não pareça um ad tradicional

═══════════════════════════════════════════════════════════════
```

#### Step 3.7: Discovery Ad Template

```markdown
═══════════════════════════════════════════════════════════════
DISCOVERY AD (IN-FEED) TEMPLATE
═══════════════════════════════════════════════════════════════

COMPONENTS:
- Thumbnail (1280x720 recomendado)
- Título (máx 100 caracteres)
- Descrição 1 (máx 35 caracteres)
- Descrição 2 (máx 35 caracteres)
- Vídeo (qualquer duração)

───────────────────────────────────────────────────────────────
THUMBNAIL PRINCIPLES (80% do sucesso):
───────────────────────────────────────────────────────────────
Visual Elements:
  - Rosto com expressão (medo, surpresa, alegria)
  - Contraste alto
  - 3 cores máximo
  - Texto grande e legível
  - Setas/círculos destacando

Text on Thumbnail:
  - 3-5 palavras máximo
  - Fonte bold
  - Contraste com background
  - Complementa (não repete) título

───────────────────────────────────────────────────────────────
TITLE FORMULAS:
───────────────────────────────────────────────────────────────
1. HOW-TO:
   "Como [Resultado] em [Tempo] (Passo a Passo)"
   "Como Escalar com YouTube Ads (Método Completo)"

2. NUMBER LIST:
   "[X] [Coisas] que [Avatares] Precisam Saber sobre [Tema]"
   "5 Erros de YouTube Ads que Custam R$10k/mês"

3. QUESTION:
   "Por Que [Maioria] [Falha] com [Tema]?"
   "Por Que Seus Ads Não Convertem? (A Verdade)"

4. SECRET/REVEAL:
   "O Segredo dos YouTube Ads de 7 Dígitos"
   "O Que [Experts] Não Contam Sobre [Tema]"

5. TRANSFORMATION:
   "De [Estado A] para [Estado B] com [Método]"
   "De R$0 a R$100k com YouTube Ads (Case Real)"

───────────────────────────────────────────────────────────────
DESCRIPTION EXAMPLES:
───────────────────────────────────────────────────────────────
Descrição 1: "Método usado por +500 empresas"
Descrição 2: "Assista e aplique hoje"

Descrição 1: "Grátis por tempo limitado"
Descrição 2: "Clique e descubra"

Descrição 1: "3x mais leads qualificados"
Descrição 2: "Método passo a passo"

───────────────────────────────────────────────────────────────
VIDEO CONTENT FOR DISCOVERY:
───────────────────────────────────────────────────────────────
Discovery ads = viewer CLICA para assistir
O vídeo deve:
  - Entregar o prometido no thumbnail/título
  - Ser educacional/value-first
  - Ter CTA no meio E no final
  - Duração: 5-15 min funciona bem

Structure:
  [0-30s]    Hook + preview do valor
  [30s-5min] Conteúdo educacional
  [5min]     Mid-roll CTA
  [5-10min]  Mais valor
  [Final]    Strong CTA + próximos passos

═══════════════════════════════════════════════════════════════
```

### Phase 4: Advanced Frameworks

#### Step 4.1: ABCD Framework Application

```yaml
GOOGLE ABCD FRAMEWORK - APPLICATION GUIDE:

A - ATTENTION (Atenção):
  ┌──────────────────────────────────────────────┐
  │ CHECKLIST:                                   │
  │ [ ] Hook nos primeiros 2 segundos?          │
  │ [ ] Visual em movimento (não estático)?      │
  │ [ ] Áudio impactante?                        │
  │ [ ] Tight framing (close-up)?               │
  │ [ ] Elemento surpresa?                       │
  └──────────────────────────────────────────────┘

B - BRANDING:
  ┌──────────────────────────────────────────────┐
  │ CHECKLIST:                                   │
  │ [ ] Marca mencionada nos primeiros 5s?       │
  │ [ ] Cores da marca consistentes?             │
  │ [ ] Logo visível?                           │
  │ [ ] Produto integrado à história?           │
  │ [ ] Audio branding (jingle/sonic logo)?     │
  └──────────────────────────────────────────────┘

C - CONNECTION (Conexão):
  ┌──────────────────────────────────────────────┐
  │ CHECKLIST:                                   │
  │ [ ] História humana/relatable?               │
  │ [ ] Emoção autêntica (humor, empatia)?      │
  │ [ ] Linguagem do avatar?                     │
  │ [ ] Problema real, solução real?            │
  │ [ ] Close-ups de rostos?                    │
  └──────────────────────────────────────────────┘

D - DIRECTION (Direção):
  ┌──────────────────────────────────────────────┐
  │ CHECKLIST:                                   │
  │ [ ] CTA específico e claro?                 │
  │ [ ] URL visível na tela?                    │
  │ [ ] Verbal + Visual alignment?              │
  │ [ ] Urgência (se aplicável)?                │
  │ [ ] Próximo passo óbvio?                    │
  └──────────────────────────────────────────────┘
```

#### Step 4.2: Tom Breeze 5 A's Application

```yaml
TOM BREEZE 5 A's FRAMEWORK:

1. ATTENTION:
   Implementation:
     - Pattern interrupt forte
     - Visual hook imediato
     - Statement que para o scroll

   Script Element:
     "Se você é [avatar] que [situação]..."

2. AUTHORITY:
   Implementation:
     - Credenciais logo após hook
     - Números e resultados
     - Por que você?

   Script Element:
     "Nos últimos [X] anos, ajudei [Y] pessoas a..."

3. AUDIENCE:
   Implementation:
     - Targeting preciso
     - Exclusão de não-qualificados
     - Falar diretamente para o avatar

   Script Element:
     "Isso é especificamente para [avatar] que..."

4. ACTION:
   Implementation:
     - CTA cristalino
     - Oferta irresistível
     - Urgência genuína

   Script Element:
     "Clique no link abaixo e [benefício específico]..."

5. ASCENSION:
   Implementation:
     - Funil pós-clique otimizado
     - Jornada do cliente clara
     - Lifetime value focus

   Post-Ad Element:
     Landing page → Lead magnet → Nurture → Offer
```

#### Step 4.3: Billy Gene Entertainment Framework

```yaml
BILLY GENE ENTERTAINMENT + EDUCATION + OFFER:

1. ENTERTAINMENT (0-15 segundos):

   Tactics:
     - Seja INESPERADO
     - Use humor quando apropriado
     - Props inusitados
     - Situações absurdas
     - NÃO pareça um ad tradicional

   Examples:
     - Fantasia de personagem
     - Locação bizarra
     - Ação inesperada
     - Parody de algo conhecido

   Question to Ask:
     "Isso é DIFERENTE de outros ads?"
     "As pessoas compartilhariam?"

2. EDUCATION (15-45 segundos):

   Tactics:
     - Ensine algo ÚTIL
     - Valor que funciona mesmo sem comprar
     - Demonstre expertise
     - "Dê o peixe, venda a vara"

   Structure:
     - O problema real
     - O mito (o que não funciona)
     - A verdade (o que funciona)
     - O método (como fazer)

   Question to Ask:
     "O viewer aprendeu algo valioso?"
     "Isso funciona independente de comprar?"

3. OFFER (45-60 segundos):

   Tactics:
     - Transição natural do valor
     - Oferta específica e clara
     - Por que agora?
     - Próximo passo simples

   Structure:
     - O que recebem
     - Por que é valioso
     - CTA direto
     - Urgência (se real)

   Question to Ask:
     "A oferta é irresistível?"
     "O próximo passo é óbvio?"
```

### Phase 5: A/B Testing Protocol

#### Step 5.1: 24 Variations Method

```yaml
24 VARIATIONS METHOD (Aleric Heck):

STRUCTURE:
  4 Hook variations × 2 Body variations × 3 CTA variations = 24 ads

RECORDING EFFICIENCY:
  1. Grave todos os 4 hooks seguidos (~2 min cada)
  2. Grave os 2 bodies (~3-4 min cada)
  3. Grave os 3 CTAs (~1 min cada)
  4. Total gravação: ~15-20 minutos
  5. Edição combina: 24 variações

HOOK VARIATIONS:
  Hook A: Question (pergunta provocativa)
  Hook B: Statement (afirmação bold)
  Hook C: Story (abertura narrativa)
  Hook D: Statistic (número chocante)

BODY VARIATIONS:
  Body A: Problem-heavy (foca na dor)
  Body B: Solution-heavy (foca no método)

CTA VARIATIONS:
  CTA A: Urgência (tempo limitado)
  CTA B: Scarcity (vagas limitadas)
  CTA C: Value (benefício sem urgência)

TESTING PROTOCOL:
  Phase 1: Rode todas 24 por 48-72h
  Phase 2: Identifique top 5 por View Rate
  Phase 3: Continue top 5 por mais 72h
  Phase 4: Identifique winner por CTR + Conversion
  Phase 5: Scale winner, crie variações do winner
```

#### Step 5.2: Testing Metrics

```yaml
METRICS TO TRACK BY PHASE:

PHASE 1: HOOK TESTING
  Primary Metric: View Rate (% que assiste 30s+)
  Target: >25% (good), >35% (great)

  Secondary: Completion Rate
  Target: >15%

PHASE 2: ENGAGEMENT TESTING
  Primary Metric: Watch Time
  Target: >50% completion

  Secondary: Engagement Rate
  Target: >0.5% likes/comments

PHASE 3: CONVERSION TESTING
  Primary Metric: CTR (Click-Through Rate)
  Target: >0.5% (average), >1% (good)

  Secondary: Conversion Rate
  Target: varies by offer

PHASE 4: SCALE METRICS
  Primary Metric: ROAS / CPA
  Target: >3x ROAS or <target CPA

  Secondary: Scale stability
  Target: Performance within 20% at 2x budget
```

### Phase 6: Quality Assurance

#### Step 6.1: Pre-Launch Checklist

```yaml
PRE-LAUNCH CHECKLIST:

HOOK (0-5 segundos):
  [ ] Interrompe padrão (não parece ad genérico)?
  [ ] Qualifica o avatar claramente?
  [ ] Promete valor ou cria curiosidade?
  [ ] Funciona SEM som (captions)?
  [ ] Visual em movimento?

BRANDING:
  [ ] Marca mencionada nos primeiros 5-10s?
  [ ] Cores consistentes com brand?
  [ ] Logo visível em algum momento?
  [ ] Produto integrado naturalmente?

ESTRUTURA:
  [ ] Flui naturalmente (não robótico)?
  [ ] Cada segundo justifica existir?
  [ ] Não repete informação desnecessariamente?
  [ ] Duração adequada ao formato?

VISUAL:
  [ ] Qualidade de imagem profissional?
  [ ] Iluminação adequada?
  [ ] Áudio claro e limpo?
  [ ] Captions/subtitles inclusos?
  [ ] Funciona em mobile (texto legível)?

CTA:
  [ ] Claro e específico?
  [ ] URL visível na tela?
  [ ] Verbal + visual alignment?
  [ ] Urgência é genuína (não fake)?
  [ ] Próximo passo é óbvio?

COMPLIANCE:
  [ ] Não faz promessas proibidas?
  [ ] Sem antes/depois médico não autorizado?
  [ ] Claims são verificáveis?
  [ ] Dentro das políticas do YouTube?
  [ ] Landing page consistente com ad?

TECHNICAL:
  [ ] Aspect ratio correto para formato?
  [ ] Duração dentro do limite?
  [ ] Arquivo no formato aceito?
  [ ] Resolução adequada (1080p+)?
```

#### Step 6.2: Post-Launch Monitoring

```yaml
POST-LAUNCH MONITORING:

FIRST 24 HOURS:
  - Verificar se ad foi aprovado
  - Monitorar impressões iniciais
  - Check for policy warnings

FIRST 48-72 HOURS:
  - Analisar View Rate por variação
  - Identificar hooks que funcionam
  - Kill variações com View Rate <15%

FIRST WEEK:
  - Analisar CTR e conversões
  - Calcular CPA/ROAS inicial
  - Ajustar bidding se necessário

ONGOING:
  - Weekly performance review
  - Creative refresh a cada 4-6 semanas
  - Audience expansion gradual
  - Scale incrementalmente (20-30%/vez)
```

---

## Output Format

```yaml
deliverables:
  primary:
    - complete_script:
        format: "Markdown with timestamps"
        includes:
          - Hook variations (3-4)
          - Full script by duration
          - Visual direction notes
          - Audio notes

  secondary:
    - hook_variations: "3-4 different approaches"
    - visual_storyboard: "Key visual moments"
    - ab_test_plan: "Testing protocol"
    - thumbnail_concepts: "For Discovery ads"

  supporting:
    - quality_checklist: "Pre-launch verification"
    - targeting_suggestions: "Audience recommendations"
    - metrics_targets: "Success benchmarks"

output_structure:
  1_strategy_summary:
    - Format selected and why
    - Avatar qualification statement
    - Key message hierarchy

  2_main_script:
    - Full script with timestamps
    - Visual/audio directions inline
    - Branding moments marked

  3_hook_variations:
    - Variation A (Question)
    - Variation B (Statement)
    - Variation C (Story)
    - Variation D (Pattern Interrupt)

  4_testing_plan:
    - What to test first
    - Budget allocation
    - Success metrics

  5_quality_checklist:
    - Pre-launch verification
    - Compliance check
    - Technical specs
```

---

## Copywriter Recommendations

```yaml
COPYWRITER SELECTION BY CONTEXT:

┌──────────────────────┬─────────────────┬──────────────────────────────┐
│ Contexto             │ Copywriter      │ Por Quê                      │
├──────────────────────┼─────────────────┼──────────────────────────────┤
│ Storytelling Ads     │ Joe Sugarman    │ Narrativa envolvente,        │
│                      │                 │ demonstração, curiosidade    │
├──────────────────────┼─────────────────┼──────────────────────────────┤
│ Pattern Interrupt    │ Gary Halbert    │ Hooks fortes, urgência,      │
│                      │                 │ copy direto e impactante     │
├──────────────────────┼─────────────────┼──────────────────────────────┤
│ Educacional/Value    │ Frank Kern      │ Casual, value-first,         │
│                      │                 │ build relationship           │
├──────────────────────┼─────────────────┼──────────────────────────────┤
│ Urgência/Escassez    │ Dan Kennedy     │ Direct response forte,       │
│                      │                 │ ação imediata                │
├──────────────────────┼─────────────────┼──────────────────────────────┤
│ Big Idea/Mechanism   │ Todd Brown      │ Diferenciação única,         │
│                      │                 │ mecanismo proprietário       │
├──────────────────────┼─────────────────┼──────────────────────────────┤
│ Problem Agitation    │ Eugene Schwartz │ Sofisticação de mercado,     │
│                      │                 │ awareness levels             │
├──────────────────────┼─────────────────┼──────────────────────────────┤
│ Emotional/Humor      │ Billy Gene      │ Entertainment value,         │
│ (Reference)          │ Style           │ viral potential              │
└──────────────────────┴─────────────────┴──────────────────────────────┘

TIER RECOMMENDATION:
  - Complex campaigns → Tier 0 (Eugene Schwartz) + Tier 1 execution
  - Standard campaigns → Tier 1 (Gary Halbert, Dan Kennedy)
  - Specific formats → Tier 2-3 specialists
```

---

## Metrics Reference

```yaml
YOUTUBE ADS BENCHMARKS 2025-2026:

Overall Platform:
  monthly_active_users: "2.7 bilhões"
  daily_active_users: "~125 milhões"
  mobile_viewership: ">70%"

Performance Averages:
  ctr_average: "0.65%"
  ctr_good: ">1%"
  view_rate_average: "25-30%"
  view_rate_good: ">35%"
  cpv_range: "$0.01-0.15"
  cpm_range: "$4-15"

By Format:
  skippable:
    view_rate_target: ">25%"
    ctr_target: ">0.5%"
    completion_rate: "15-30%"

  non_skippable:
    completion_rate: "100%"
    ctr_average: "0.3-0.7%"

  bumper:
    recall_lift: "+10-20%"
    cpm_efficient: "Yes"

  shorts:
    engagement_rate: "2-5%"
    growing: "Rapidly"

By Industry:
  ecommerce:
    ctr: "0.8-1.5%"
    roas_target: "3-5x"

  info_products:
    ctr: "1-2%"
    roas_target: "4-8x"

  b2b_saas:
    ctr: "0.5-1%"
    cpl_range: "$50-200"
```

---

## Quick Reference Scripts

### Lead Generation (60s)
```
[0-5s] "Se você gasta mais de R$5000 em ads e não vê retorno..."
[5-15s] [Credencial + por que ouvir]
[15-30s] [Problema: maioria desperdiça em tráfego frio]
[30-45s] [Solução: YouTube Ads + seu método]
[45-55s] [Prova: resultados de clientes]
[55-60s] [CTA: baixar guia/aula grátis]
```

### Direct Sale (90s)
```
[0-5s] [Hook: resultado ou story opening]
[5-20s] [Story: sua jornada ou do cliente]
[20-40s] [Problema: deep dive na dor]
[40-60s] [Solução: produto + mecanismo]
[60-75s] [Prova: múltiplos depoimentos]
[75-85s] [Oferta: stack + garantia]
[85-90s] [CTA: comprar agora + urgência]
```

### Brand Awareness (15s)
```
[0-3s] "[Avatar]? [Problema em 3 palavras]?"
[3-10s] "[Produto] resolve. [Benefício]."
[10-15s] "[Tagline]. [URL]."
```

---

## Related Resources

- **Research Doc:** `docs/research/youtube-ads-methodology-research.md`
- **VSL Task:** `tasks/create-vsl.md`
- **Video Script Task:** `tasks/create-video-script.md`
- **Landing Page Task:** `tasks/create-landing-page.md`

---

*Task Version: 2.0*
*Lines: 1200+*
*Last Updated: 2026-01-23*
*Primary Frameworks: Google ABCD, Tom Breeze 5 A's, Billy Gene Entertainment, Aleric Heck Value-Ad, Jake Larsen Video Ad Formula*
*Research Base: docs/research/youtube-ads-methodology-research.md*
