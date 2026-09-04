# Create Native Ads Task

## Purpose

Criar anúncios nativos e advertorials que se integram ao conteúdo editorial, parecem artigos genuínos e convertem através de curiosidade e valor. Este task integra metodologias do IAB Native Advertising Playbook, especialistas como David Ogilvy e Gary Bencivenga, e best practices de plataformas como Taboola e Outbrain.

## Research Foundation

Este task é baseado em pesquisa documentada em:
`docs/research/native-ads-methodology-research.md`

**Metodologias Integradas:**
- IAB Native Advertising Playbook 2.0
- David Ogilvy Headline Principles
- Gary Bencivenga Fascinations
- Tabloid Headline Techniques
- Copyblogger Advertorial Framework

---

## When to Use

```yaml
Primary Use Cases:
  - Content discovery platforms (Taboola, Outbrain, MGID, RevContent)
  - Anúncios em portais de notícias
  - Advertorials e pre-sell pages
  - Conteúdo patrocinado
  - Native social ads (Facebook, Instagram, LinkedIn)
  - In-feed advertising
  - Recommendation widgets

Ad Objectives:
  - Content promotion
  - Lead generation
  - Direct response
  - Brand awareness
  - Pre-sell antes de sales page
  - Traffic para funil
```

---

## Inputs

```yaml
required:
  product_or_service:
    description: "Nome e descrição do produto/serviço"
    example: "Suplemento natural para sono - Dormir+Pro"

  target_avatar:
    description: "Descrição detalhada do leitor ideal"
    example: "Mulheres 35-55, executivas, problemas de insônia"

  main_benefit:
    description: "Benefício principal a comunicar"
    example: "Dormir 8 horas seguidas naturalmente"

  ad_platform:
    description: "Plataforma de native ads"
    options:
      - taboola
      - outbrain
      - mgid
      - revcontent
      - facebook_native
      - linkedin_native
      - direct_publisher

  landing_type:
    description: "Tipo de landing page destino"
    options:
      - advertorial_short    # 500-800 palavras
      - advertorial_medium   # 800-1500 palavras
      - advertorial_long     # 1500-3000 palavras
      - sales_page           # Direct to offer
      - lead_capture         # Optin first
      - quiz_funnel          # Personalized path

optional:
  angle:
    description: "Ângulo da história"
    options:
      - discovery            # Nova descoberta
      - warning              # Alerta/perigo
      - scientific           # Baseado em pesquisa
      - personal_story       # História pessoal
      - contrarian           # Contra a maioria
      - local                # Relevância geográfica
      - celebrity_authority  # Endorsement

  news_peg:
    description: "Gancho de notícia atual"
    example: "Novo estudo publicado, mudança de regulação"

  controversy_element:
    description: "Elemento controverso se aplicável"
    example: "Por que médicos não recomendam isso"

  social_proof:
    description: "Provas sociais disponíveis"
    example: "10.000 clientes, estudo clínico, depoimentos"

  copywriter_style:
    description: "Estilo de copywriter preferido"
    options:
      - david_ogilvy         # Editorial elegante
      - gary_halbert         # Story-driven
      - gary_bencivenga      # Curiosity/fascinations
      - dan_kennedy          # Direct response agressivo
      - joe_sugarman         # Demonstração
```

---

## Workflow

### Phase 1: Strategic Foundation

#### Step 1.1: Platform Selection

```yaml
PLATFORM SELECTION MATRIX:

┌─────────────────┬──────────────────────────────────────────────────┐
│ Objetivo        │ Plataforma Recomendada                           │
├─────────────────┼──────────────────────────────────────────────────┤
│ PREMIUM BRANDS  │ Outbrain                                         │
│                 │ → Publishers de alta qualidade (CNN, Time)       │
│                 │ → CPC mais alto, audiência premium               │
├─────────────────┼──────────────────────────────────────────────────┤
│ SCALE/VOLUME    │ Taboola                                          │
│                 │ → Maior reach (500M+ daily users)                │
│                 │ → Boa variedade de publishers                    │
├─────────────────┼──────────────────────────────────────────────────┤
│ BUDGET-FRIENDLY │ MGID                                             │
│                 │ → CPCs mais baixos                               │
│                 │ → Bom para testing                               │
├─────────────────┼──────────────────────────────────────────────────┤
│ QUALITY FOCUS   │ RevContent                                       │
│                 │ → Network seletivo                               │
│                 │ → Performance marketers                          │
├─────────────────┼──────────────────────────────────────────────────┤
│ B2B/PROFESS.    │ LinkedIn Native                                  │
│                 │ → Audiência profissional                         │
│                 │ → Targeting por cargo/indústria                  │
└─────────────────┴──────────────────────────────────────────────────┘

BUDGET GUIDELINES:
  Testing Phase: $50-100/day
  Optimization: $100-300/day
  Scale: $500+/day

CPC EXPECTATIONS:
  Taboola: $0.30-0.80
  Outbrain: $0.40-1.20
  MGID: $0.10-0.50
  RevContent: $0.25-0.70
```

#### Step 1.2: Angle Selection

```yaml
ANGLE SELECTION FRAMEWORK:

DISCOVERY ANGLE:
  ┌──────────────────────────────────────────────────┐
  │ Theme: "Nova descoberta/solução revelada"        │
  │ Emotion: Curiosidade, esperança                  │
  │ Headlines: Descobriu, Revela, Novo método        │
  │ Best For: Maioria dos produtos                   │
  │                                                  │
  │ Example:                                         │
  │ "Dentista de São Paulo Descobre Método Que      │
  │  Clareia Dentes em Casa Sem Produtos Químicos"  │
  └──────────────────────────────────────────────────┘

WARNING ANGLE:
  ┌──────────────────────────────────────────────────┐
  │ Theme: "Perigo oculto/alerta importante"         │
  │ Emotion: Medo, proteção                          │
  │ Headlines: Cuidado, Alerta, O que acontece       │
  │ Best For: Health, financial, security            │
  │                                                  │
  │ Example:                                         │
  │ "Alerta: O Que Acontece Quando Você Toma        │
  │  [Suplemento Comum] Todo Dia"                   │
  └──────────────────────────────────────────────────┘

SCIENTIFIC ANGLE:
  ┌──────────────────────────────────────────────────┐
  │ Theme: "Pesquisa/estudo comprova"                │
  │ Emotion: Confiança, autoridade                   │
  │ Headlines: Estudo revela, Cientistas, Pesquisa   │
  │ Best For: Health, education, tech                │
  │                                                  │
  │ Example:                                         │
  │ "Novo Estudo Revela Por Que 73% das Dietas      │
  │  Falham (E a Solução Surpreendente)"            │
  └──────────────────────────────────────────────────┘

PERSONAL STORY ANGLE:
  ┌──────────────────────────────────────────────────┐
  │ Theme: "Jornada de pessoa real"                  │
  │ Emotion: Identificação, esperança                │
  │ Headlines: Como [pessoa], Minha história         │
  │ Best For: Transformações, info products          │
  │                                                  │
  │ Example:                                         │
  │ "Mãe de 3 Filhos Perde 15kg em 60 Dias Sem      │
  │  Academia — Veja o Método Que Ela Usou"         │
  └──────────────────────────────────────────────────┘

CONTRARIAN ANGLE:
  ┌──────────────────────────────────────────────────┐
  │ Theme: "Contra a sabedoria convencional"         │
  │ Emotion: Curiosidade, validação                  │
  │ Headlines: Por que [maioria] está errada         │
  │ Best For: Produtos diferenciados                 │
  │                                                  │
  │ Example:                                         │
  │ "Por Que Dermatologistas Não Querem Que         │
  │  Você Saiba Sobre Este Tratamento Caseiro"      │
  └──────────────────────────────────────────────────┘

LOCAL ANGLE:
  ┌──────────────────────────────────────────────────┐
  │ Theme: "Acontecendo perto de você"               │
  │ Emotion: Relevância, pertencimento               │
  │ Headlines: [Cidade], Brasileiros                 │
  │ Best For: Geo-targeted campaigns                 │
  │                                                  │
  │ Example:                                         │
  │ "São Paulo: Novo Método de Investimento         │
  │  Viraliza Entre Executivos da Faria Lima"       │
  └──────────────────────────────────────────────────┘
```

### Phase 2: Native Ad Creative

#### Step 2.1: Thumbnail Image Strategy

```yaml
THUMBNAIL BEST PRACTICES:

HIGH-PERFORMING IMAGE TYPES:

1. FACES (30-50% CTR boost):
   ┌──────────────────────────────────────────────┐
   │ ✓ Expressão de surpresa ou curiosidade       │
   │ ✓ Olhar direto para câmera                   │
   │ ✓ "Pessoa real" (não modelo perfeito)        │
   │ ✓ Close-up do rosto                          │
   │ ✓ Emoção autêntica                           │
   │                                              │
   │ ✗ Stock photos genéricos                     │
   │ ✗ Modelos muito polidos                      │
   │ ✗ Grupos grandes (foco difuso)               │
   └──────────────────────────────────────────────┘

2. CURIOSITY OBJECTS:
   ┌──────────────────────────────────────────────┐
   │ ✓ "O que é isso?"                            │
   │ ✓ Close-up misterioso                        │
   │ ✓ Contexto incompleto                        │
   │ ✓ Objeto incomum ou inesperado               │
   │                                              │
   │ Example: Close-up de ingrediente estranho    │
   └──────────────────────────────────────────────┘

3. BEFORE/AFTER (compliance required):
   ┌──────────────────────────────────────────────┐
   │ ✓ Transformação verdadeira e documentada     │
   │ ✓ Não exagerar diferença                     │
   │ ✓ Mesma pessoa, mesmas condições             │
   │ ✓ Disclaimer visível se necessário           │
   │                                              │
   │ ⚠️ Cuidado com health claims                 │
   └──────────────────────────────────────────────┘

4. NEWS-STYLE:
   ┌──────────────────────────────────────────────┐
   │ ✓ Parece screenshot de notícia               │
   │ ✓ Estilo jornalístico                        │
   │ ✓ Autoridade ou expert                       │
   │ ✓ Contexto de reportagem                     │
   └──────────────────────────────────────────────┘

5. PRODUCT IN USE:
   ┌──────────────────────────────────────────────┐
   │ ✓ Demonstração natural                       │
   │ ✓ Contexto de uso real                       │
   │ ✓ Não parece ad de produto                   │
   │ ✓ Pessoa usando (não só produto)             │
   └──────────────────────────────────────────────┘

IMAGES TO AVOID:
  ❌ Stock photos óbvios
  ❌ Muito produzido/profissional
  ❌ Texto excessivo na imagem
  ❌ Logos grandes
  ❌ Call-to-action visual
  ❌ Clickbait enganoso
  ❌ Celebridades sem permissão

TECHNICAL SPECS:
  Taboola: 1200x628 ou 1200x800
  Outbrain: 1200x628 (16:9 ratio)
  MGID: 492x328 minimum
  Facebook: 1200x628
```

#### Step 2.2: Headline Copywriting

```yaml
HEADLINE FRAMEWORKS (David Ogilvy + Tabloid):

OGILVY PRINCIPLES:
  "80% das pessoas leem apenas o headline.
   O headline É sua campanha."

  1. Include benefit (o que o reader ganha)
  2. Use "New" or "Free" (ou equivalentes)
  3. Name your prospect (qualificação)
  4. Add curiosity (informação incompleta)
  5. Local angle when possible (+10-30% CTR)

─────────────────────────────────────────────────────────
HEADLINE FORMULA 1: DISCOVERY
─────────────────────────────────────────────────────────
Pattern:
"[Local/Profissão] Descobre [Solução] Que [Resultado]"

Examples:
• "Médico de Curitiba Descobre Método Que Elimina
   Dores nas Costas em 5 Minutos"
• "Engenheiro Brasileiro Cria App Que Paga
   Para Você Caminhar"
• "Nutricionista Revela Alimento Que Acelera
   Metabolismo 3x Mais"

─────────────────────────────────────────────────────────
HEADLINE FORMULA 2: CONTRARIAN/EXPOSÉ
─────────────────────────────────────────────────────────
Pattern:
"Por Que [Autoridade] [Ação Controversa] [Tema]"

Examples:
• "Por Que Dermatologistas Não Querem Que Você
   Saiba Sobre Este Tratamento"
• "O Que Bancos Não Contam Sobre Seu Dinheiro
   Parado na Poupança"
• "Por Que Médicos Estão Prescrevendo Isso
   Ao Invés de Remédios"

─────────────────────────────────────────────────────────
HEADLINE FORMULA 3: PERSONAL STORY
─────────────────────────────────────────────────────────
Pattern:
"[Pessoa Comum] [Situação Surpreendente] — [Resultado]"

Examples:
• "Aposentado de 67 Anos Fatura R$12k/mês
   Trabalhando de Casa — Veja Como"
• "Professora Emagrece 22kg Sem Dieta Depois
   de Descobrir Isso"
• "Mãe Solteira Sai do Vermelho e Compra
   Apartamento em 18 Meses"

─────────────────────────────────────────────────────────
HEADLINE FORMULA 4: WEIRD TRICK
─────────────────────────────────────────────────────────
Pattern:
"[Resultado] Com [Método Incomum/Truque]"

Examples:
• "Elimine Rugas Com Este Truque de 2 Minutos
   Que Não Requer Botox"
• "Aprenda Inglês Com Método 'Estranho' Que
   Brasileiros Estão Usando"
• "Emagreça Comendo Mais Com Esta Técnica
   Contra-Intuitiva"

─────────────────────────────────────────────────────────
HEADLINE FORMULA 5: SCIENTIFIC
─────────────────────────────────────────────────────────
Pattern:
"Novo Estudo Revela [Descoberta] Sobre [Área]"

Examples:
• "Novo Estudo Revela Por Que Dietas Tradicionais
   Falham em 95% dos Casos"
• "Cientistas Descobrem Por Que Algumas Pessoas
   Nunca Engordam"
• "Pesquisa de Harvard Mostra o Segredo
   de Quem Vive 100+ Anos"

─────────────────────────────────────────────────────────
HEADLINE FORMULA 6: WARNING/ALERT
─────────────────────────────────────────────────────────
Pattern:
"[Aviso/Alerta] Sobre [Prática/Produto Comum]"

Examples:
• "Alerta: O Que Acontece Quando Você Toma
   Café Todo Dia em Jejum"
• "Cuidado: 7 em 10 Brasileiros Fazem Isso
   Errado Ao Escovar os Dentes"
• "Aviso Importante Para Quem Usa
   [Produto/Medicamento Comum]"

─────────────────────────────────────────────────────────
HEADLINE FORMULA 7: LOCAL NEWS
─────────────────────────────────────────────────────────
Pattern:
"[Cidade/Região]: [Notícia/Tendência]"

Examples:
• "São Paulo: Método de Emagrecimento Viraliza
   Entre Mulheres da Zona Sul"
• "Brasil: Governo Anuncia Novo Benefício
   Para Quem Tem Mais de 50 Anos"
• "Rio de Janeiro: App Paga Usuários Para
   Fazer Compras de Supermercado"
```

#### Step 2.3: Gary Bencivenga Fascinations

```yaml
BENCIVENGA FASCINATIONS FOR NATIVE ADS:

Definition:
"Bullets que criam curiosidade tão intensa que o leitor
 PRECISA descobrir a resposta"

─────────────────────────────────────────────────────────
FASCINATION 1: THE SPECIFIC NUMBER
─────────────────────────────────────────────────────────
Pattern: "Os [X] [coisas] que [ação/resultado]"

Examples:
• "Os 7 Alimentos Que Destroem Sua Tireoide
   (O #4 Vai Te Chocar)"
• "3 Palavras Que Fazem Qualquer Homem
   Se Apaixonar Por Você"
• "As 5 Causas Reais de Cabelo Branco
   (Não É Só Genética)"

Why It Works:
  - Números específicos são mais críveis
  - Implica lista organizada
  - Promise de completeness

─────────────────────────────────────────────────────────
FASCINATION 2: THE SECRET
─────────────────────────────────────────────────────────
Pattern: "O segredo que [autoridade] não conta"

Examples:
• "O Segredo Que Dermatologistas Usam
   Mas Não Contam Aos Pacientes"
• "A Técnica Secreta de Vendedores
   Que Faturam R$100k/mês"
• "O Segredo Dos Japoneses Para
   Nunca Ficarem Cansados"

Why It Works:
  - Implica informação privilegiada
  - Exclusividade
  - "Insider" knowledge

─────────────────────────────────────────────────────────
FASCINATION 3: THE MISTAKE
─────────────────────────────────────────────────────────
Pattern: "O erro #1 que [grupo] comete"

Examples:
• "O Erro #1 Que Investidores Iniciantes
   Cometem (E Como Evitar)"
• "Por Que 90% Das Dietas Falham
   (O Erro Que Quase Ninguém Percebe)"
• "O Erro Silencioso Que Destrói
   Relacionamentos Aos Poucos"

Why It Works:
  - Medo de estar errado
  - Auto-diagnóstico
  - Oportunidade de correção

─────────────────────────────────────────────────────────
FASCINATION 4: THE WARNING
─────────────────────────────────────────────────────────
Pattern: "O perigo oculto em [coisa comum]"

Examples:
• "O Perigo Oculto Na Sua Pasta de Dentes
   (E a Alternativa Segura)"
• "O Que Acontece Com Seu Corpo Quando
   Você Fica Sentado 8 Horas"
• "O Ingrediente Tóxico Escondido
   Em 90% Dos Suplementos"

Why It Works:
  - Triggera instinto de proteção
  - Curiosidade defensiva
  - Fear of missing danger
```

### Phase 3: Advertorial Structure

#### Step 3.1: Advertorial Anatomy

```yaml
ADVERTORIAL COMPLETE STRUCTURE:

┌─────────────────────────────────────────────────────────┐
│ 1. HEADER EDITORIAL                                     │
│    ┌─────────────────────────────────────────────────┐  │
│    │ [Logo/Nome do Site]                              │ │
│    │ Categoria: Saúde / Finanças / Lifestyle          │ │
│    │ ⚠️ "Conteúdo Patrocinado" (disclosure)           │ │
│    └─────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────┤
│ 2. HEADLINE                                             │
│    - Estilo jornalístico                               │
│    - Não parece ad                                     │
│    - Continua curiosity do native ad                   │
├─────────────────────────────────────────────────────────┤
│ 3. BYLINE                                              │
│    "Por [Nome] | [Data] | [X] min de leitura"          │
├─────────────────────────────────────────────────────────┤
│ 4. LEAD IMAGE                                          │
│    - Relacionada ao conteúdo                           │
│    - Estilo editorial                                  │
│    - Caption se relevante                              │
├─────────────────────────────────────────────────────────┤
│ 5. OPENING (Hook - 100-200 palavras)                   │
│    - Gancho que prende atenção                         │
│    - Estabelece relevância                             │
│    - Promete valor/revelação                           │
├─────────────────────────────────────────────────────────┤
│ 6. STORY/CONTEXT (200-400 palavras)                    │
│    - História do protagonista                          │
│    - Como o problema surgiu                            │
│    - Tentativas de solução que falharam                │
├─────────────────────────────────────────────────────────┤
│ 7. PROBLEM AGITATION (200-300 palavras)                │
│    - Aprofunda a dor                                   │
│    - Por que soluções comuns não funcionam             │
│    - Consequências de não agir                         │
├─────────────────────────────────────────────────────────┤
│ 8. SOLUTION (300-500 palavras)                         │
│    - Apresenta produto/método                          │
│    - Como funciona (mecanismo)                         │
│    - Por que é diferente                               │
├─────────────────────────────────────────────────────────┤
│ 9. PROOF (150-300 palavras)                            │
│    - Depoimentos                                       │
│    - Estudos/dados                                     │
│    - Resultados específicos                            │
├─────────────────────────────────────────────────────────┤
│ 10. SOFT CTA (50-100 palavras)                         │
│     - Transição natural                                │
│     - Link para próximo passo                          │
│     - Não hard-sell agressivo                          │
├─────────────────────────────────────────────────────────┤
│ 11. DISCLAIMER                                         │
│     - "Resultados podem variar"                        │
│     - Legal compliance                                 │
│     - Links para políticas                             │
└─────────────────────────────────────────────────────────┘
```

#### Step 3.2: Advertorial Templates

```markdown
═══════════════════════════════════════════════════════════════
TEMPLATE 1: DISCOVERY STORY ADVERTORIAL
═══════════════════════════════════════════════════════════════

[HEADER]
[Logo] | SAÚDE & BEM-ESTAR | Conteúdo Patrocinado

─────────────────────────────────────────────────────────────

# [Local]: [Profissão] Descobre [Solução] Que [Resultado] —
  E Agora Está Ajudando Milhares de Pessoas

*Por [Nome] | [Data] | 5 min de leitura*

[IMAGEM: Protagonista em contexto relevante]

**[Cidade]** — O que começou como uma busca pessoal por
[solução] acabou revelando algo que pode [benefício] para
milhões de brasileiros.

[Nome], [idade], [contexto profissional], nunca imaginou
que [descoberta] pudesse [resultado surpreendente].

"[Quote do protagonista sobre a descoberta]", conta
[ele/ela] em entrevista exclusiva.

## A Jornada Até a Descoberta

Tudo começou há [tempo] quando [Nome] enfrentava [problema].

"Eu tentei de tudo", lembra. "[Lista de soluções
convencionais que não funcionaram]. Nada trazia resultados
duradouros."

[2-3 parágrafos desenvolvendo a história, frustrações,
tentativas]

A situação se agravou quando [consequência do problema].

## O Ponto de Virada

Foi então que [Nome] [como encontrou a solução].

"No começo, eu estava cético", admite. "Mas decidi
[dar uma chance] porque [razão]."

O que aconteceu nas semanas seguintes [surpreendeu/
transformou] completamente [sua vida/situação].

## Por Que Funciona

Diferente de [soluções convencionais] que [problema com
elas], [produto/método] funciona porque [mecanismo único].

"[Explicação simples de como funciona]"

[Se aplicável: referência a estudos ou especialistas]

## Os Resultados

[Dados específicos, timeline de resultados]

- Nas primeiras [tempo]: [resultado 1]
- Depois de [tempo]: [resultado 2]
- Atualmente: [resultado atual]

"[Depoimento de outra pessoa que usou]" — [Nome, contexto]

"[Segundo depoimento]" — [Nome, contexto]

## Como Ter Acesso

Atualmente, [produto] está disponível [onde/como].

[Nome] decidiu compartilhar [o método/produto] porque
"[razão altruística]."

**[CTA suave]**: Para saber mais sobre [produto/método]
e como ele pode [benefício], clique no botão abaixo.

[BOTÃO: Quero Saber Mais]

---
*Este é um conteúdo publicitário. Resultados individuais
podem variar. Consulte um profissional antes de iniciar
qualquer tratamento.*

═══════════════════════════════════════════════════════════════
```

```markdown
═══════════════════════════════════════════════════════════════
TEMPLATE 2: EXPERT EXPOSÉ ADVERTORIAL
═══════════════════════════════════════════════════════════════

[HEADER]
[Logo] | INVESTIGAÇÃO | Conteúdo Patrocinado

─────────────────────────────────────────────────────────────

# Por Que [Autoridades/Indústria] Não Querem Que Você
  Saiba Sobre [Solução] — E O Que Fazer Agora

*Por [Nome] | [Data] | 7 min de leitura*

[IMAGEM: Estilo investigativo/jornalístico]

Se você já se perguntou por que [situação comum frustrante],
a resposta pode te surpreender — e incomodar algumas pessoas.

Segundo [fonte/especialista], "[revelação controversa]."

## O Que Não Te Contam

Durante décadas, [indústria/autoridades] promoveram
[abordagem convencional] como a única solução para [problema].

Mas um número crescente de [especialistas/pesquisadores]
está questionando essa narrativa.

"[Quote de expert questionando status quo]"

[2-3 parágrafos desenvolvendo a "conspiração" ou
informação oculta]

## Por Que Isso Importa Para Você

Se você é parte dos [X milhões] de brasileiros que
[sofrem com problema], essa informação pode mudar
sua perspectiva.

[Explicação de como o reader é afetado]

[Dados/estatísticas que suportam o argumento]

## A Alternativa Que Eles Não Querem Que Você Conheça

Enquanto [abordagem convencional] continua sendo
promovida, uma alternativa está ganhando atenção:

[Introdução do produto/método de forma editorial]

[Como funciona diferente das soluções convencionais]

[Porque representa uma "ameaça" ao establishment]

## O Que Pessoas Reais Estão Dizendo

"[Depoimento detalhado de usuário]"
— [Nome], [idade], [cidade]

"[Segundo depoimento]"
— [Nome], [contexto]

## Como Descobrir Se Funciona Para Você

[Produto/Método] está disponível para brasileiros
que querem [benefício] sem [desvantagens de alternativas].

**[CTA]**: Descubra o que [autoridades] não querem que
você saiba. Clique abaixo para acessar [oferta].

[BOTÃO: Quero Descobrir]

---
*Conteúdo patrocinado. As opiniões expressas são do autor.
Resultados podem variar.*

═══════════════════════════════════════════════════════════════
```

```markdown
═══════════════════════════════════════════════════════════════
TEMPLATE 3: PERSONAL CONFESSION ADVERTORIAL
═══════════════════════════════════════════════════════════════

[HEADER]
[Logo] | HISTÓRIA REAL | Conteúdo Patrocinado

─────────────────────────────────────────────────────────────

# "[Resultado Surpreendente]" — A História de [Nome] Que
  Está Inspirando Milhares de Brasileiros

*Depoimento de [Nome] | [Data] | 6 min de leitura*

[IMAGEM: Pessoa real, ambiente autêntico]

Eu preciso te contar uma coisa.

Por [tempo], eu [sofria/lutava] com [problema]. Tentei
de tudo que você pode imaginar:

- [Solução 1 que não funcionou]
- [Solução 2 que não funcionou]
- [Solução 3 que não funcionou]

Nada funcionava. E eu estava [consequência emocional].

## Meu Ponto Mais Baixo

[Descrição do momento difícil, vulnerável]

Eu lembro de [momento específico marcante] e pensar:
"[Pensamento desesperado]."

Foi quando [como chegou ao ponto de virada].

## A Descoberta Que Mudou Tudo

[Como encontrou a solução - deve parecer acidental/
orgânico, não como se estivesse comprando algo]

No começo, eu estava [emoção - cético, com medo, etc.].
Afinal, já tinha [tentado tantas coisas].

Mas algo me fez [dar uma chance]. Talvez [razão].

## O Que Aconteceu

[Timeline detalhada dos resultados]

**Primeira semana:** [Pequena mudança notada]

**Depois de um mês:** [Resultado mais significativo]

**Hoje, [tempo depois]:** [Transformação completa]

Eu olho para trás e não acredito que [situação anterior]
era minha realidade.

## Por Que Estou Compartilhando Isso

Eu sei que existem milhares de pessoas passando pelo
mesmo que eu passei.

Se você está [situação do avatar], eu quero que saiba
que [esperança + existe solução].

[Produto/Método] está disponível [como acessar].

Eu não estou dizendo que vai funcionar para todo mundo
da mesma forma. Cada pessoa é diferente.

Mas se você está [situação], pode valer a pena conhecer.

**[CTA]**: Clique abaixo para saber mais sobre [como acessar].

[BOTÃO: Quero Conhecer]

---
*Depoimento real. Resultados individuais podem variar.
[Produto] não substitui orientação médica/profissional.*

═══════════════════════════════════════════════════════════════
```

### Phase 4: Testing and Optimization

#### Step 4.1: A/B Testing Protocol

```yaml
NATIVE AD TESTING PROTOCOL:

PHASE 1: HEADLINE TESTING (Priority #1)
─────────────────────────────────────────
  Duration: 48-72 hours
  Budget: $50-100 per variation
  Sample: 1,000+ impressions each
  Metric: CTR

  Process:
  1. Create 5-10 headline variations
     - 2-3 Discovery headlines
     - 2-3 Warning/Curiosity headlines
     - 2-3 Personal Story headlines

  2. Launch all with same image
  3. Run for 48-72h
  4. Kill bottom 50% by CTR
  5. Continue top performers
  6. Declare winner when CTR difference >20%

PHASE 2: IMAGE TESTING (Priority #2)
─────────────────────────────────────────
  Duration: 48-72 hours
  Budget: $50-100 per variation
  Metric: CTR

  Process:
  1. Take winning headline
  2. Create 3-5 thumbnail variations
     - Face option
     - Curiosity object option
     - Before/after option (if applicable)
     - News-style option

  3. Test all images with winning headline
  4. Identify best performing image
  5. Create variations of winning type

PHASE 3: ANGLE TESTING
─────────────────────────────────────────
  Duration: 1 week
  Budget: $200-500 total
  Metric: CTR + Conversion Rate

  Process:
  1. Test different angles (discovery vs warning vs personal)
  2. Different emotional triggers
  3. Compare end-to-end performance

PHASE 4: LANDING PAGE TESTING
─────────────────────────────────────────
  Duration: 1-2 weeks
  Budget: Concentrated on winning ads
  Metrics: Time on page, scroll depth, conversion

  Variations to Test:
  - Short (500-800 words) vs Long (1500+ words)
  - Story-heavy vs Fact-heavy
  - Single CTA vs Multiple CTAs
  - Different headlines/angles

PHASE 5: SCALE
─────────────────────────────────────────
  1. Combine all winning elements
  2. Increase budget 20-30% at a time
  3. Monitor CPA stability
  4. Expand to new placements
  5. Refresh creatives every 2-4 weeks
```

#### Step 4.2: Performance Metrics

```yaml
KEY METRICS TO TRACK:

AD-LEVEL METRICS:
  CTR (Click-Through Rate):
    Formula: Clicks / Impressions × 100
    Benchmark: 0.3% average, 0.5%+ good, 1%+ great

  CPC (Cost Per Click):
    Varies by platform/geo
    Track trend over time

  Frequency:
    How often same user sees ad
    Cap at 3-5 to avoid fatigue

LANDING PAGE METRICS:
  Time on Page:
    Target: 2+ minutes for advertorial
    Below 30 seconds = problem

  Scroll Depth:
    Target: 50%+ reach CTA section
    Use heatmaps to visualize

  Bounce Rate:
    Target: 40-60% for cold traffic
    >80% = disconnect ad/LP

CONVERSION METRICS:
  Conversion Rate:
    Advertorial to next step: 5-15% (lead gen)
    Advertorial to sale: 1-5% (direct)

  CPA (Cost Per Acquisition):
    Should be <1/3 of product price
    Track and optimize aggressively

  ROAS (Return on Ad Spend):
    Target: 2x minimum, 3-5x healthy
```

### Phase 5: Quality Assurance

#### Step 5.1: Pre-Launch Checklist

```yaml
PRE-LAUNCH CHECKLIST:

NATIVE AD CREATIVE:
  [ ] Headline cria curiosidade genuína?
  [ ] Headline não é clickbait enganoso?
  [ ] Thumbnail é relevante ao conteúdo?
  [ ] Thumbnail não é stock photo óbvio?
  [ ] Brand name/logo presente (se required)?
  [ ] Texto não excede limites da plataforma?

ADVERTORIAL:
  [ ] Disclosure "Sponsored" visível no topo?
  [ ] Headline continua promessa do ad?
  [ ] Conteúdo entrega valor real?
  [ ] Transição para pitch é suave?
  [ ] CTA é claro mas não agressivo?
  [ ] Disclaimers necessários presentes?

COMPLIANCE:
  [ ] Claims são verificáveis?
  [ ] Não há promessas de resultados garantidos?
  [ ] Depoimentos são reais e documentados?
  [ ] Before/after tem base verdadeira?
  [ ] Não viola políticas da plataforma?
  [ ] Health claims têm base científica?
  [ ] Financial claims têm disclaimer?

TECHNICAL:
  [ ] Tracking pixels instalados?
  [ ] Links funcionando?
  [ ] Mobile responsive?
  [ ] Page speed adequada (<3 segundos)?
  [ ] UTM parameters corretos?

LEGAL:
  [ ] Política de privacidade acessível?
  [ ] Termos de uso claros?
  [ ] Opt-out disponível?
```

#### Step 5.2: Post-Launch Monitoring

```yaml
POST-LAUNCH MONITORING:

FIRST 24 HOURS:
  - Verificar aprovação dos ads
  - Monitorar impressões iniciais
  - Check for policy warnings
  - Verificar tracking funcionando

FIRST 48-72 HOURS:
  - Analisar CTR por variação
  - Identificar ads com baixo CTR (<0.2%)
  - Pausar underperformers
  - Alocar mais budget para winners

FIRST WEEK:
  - Analisar conversion metrics
  - Calcular CPA/ROAS
  - Ajustar bids se necessário
  - Identificar melhores placements

ONGOING:
  - Weekly performance review
  - Creative refresh a cada 2-4 semanas
  - Teste de novos angles
  - Expansion gradual de budget
  - Monitor ad fatigue (CTR dropping)
```

---

## Output Format

```yaml
deliverables:
  primary:
    - native_ad_set:
        includes:
          - 5-10 headline variations
          - 3-5 thumbnail directions
          - Platform-specific specs

    - advertorial:
        format: "Complete advertorial copy"
        length: "Per landing_type selected"
        includes:
          - Full copy with sections marked
          - Disclosure placement
          - CTA variations

  secondary:
    - angle_variations: "2-3 different approaches"
    - headline_bank: "10+ headlines to test"
    - thumbnail_briefs: "Image direction for designer"
    - testing_plan: "A/B testing protocol"

  supporting:
    - compliance_checklist: "Pre-launch verification"
    - metrics_targets: "Success benchmarks"
    - platform_specs: "Technical requirements"

output_structure:
  1_strategy_summary:
    - Platform selected and why
    - Angle selected and why
    - Target audience qualification

  2_native_ad_creatives:
    - Headline variations (10+)
    - Thumbnail direction briefs
    - Ad copy if needed

  3_advertorial_copy:
    - Full advertorial (per length selected)
    - All sections clearly marked
    - CTA variations

  4_testing_plan:
    - What to test first
    - Budget allocation
    - Success metrics

  5_compliance_checklist:
    - All items verified
    - Disclaimers included
    - Legal compliance confirmed
```

---

## Copywriter Recommendations

```yaml
COPYWRITER SELECTION BY CONTEXT:

┌────────────────────┬─────────────────┬─────────────────────────────┐
│ Contexto           │ Copywriter      │ Por Quê                     │
├────────────────────┼─────────────────┼─────────────────────────────┤
│ Editorial elegante │ David Ogilvy    │ Jornalístico, factual,      │
│ Premium brands     │                 │ credibilidade               │
├────────────────────┼─────────────────┼─────────────────────────────┤
│ Story-driven       │ Gary Halbert    │ Narrativa pessoal,          │
│ Personal journey   │                 │ conexão emocional           │
├────────────────────┼─────────────────┼─────────────────────────────┤
│ Headlines/Bullets  │ Gary Bencivenga │ Curiosity irresistível,     │
│ Curiosity hooks    │                 │ fascinations                │
├────────────────────┼─────────────────┼─────────────────────────────┤
│ Direct response    │ Dan Kennedy     │ Urgência, escassez,         │
│ Aggressive sell    │                 │ conversão direta            │
├────────────────────┼─────────────────┼─────────────────────────────┤
│ Product demos      │ Joe Sugarman    │ Explicação persuasiva,      │
│ Explanation-heavy  │                 │ demonstração                │
├────────────────────┼─────────────────┼─────────────────────────────┤
│ Competitive market │ Eugene Schwartz │ Diferenciação,              │
│ High sophistication│                 │ awareness levels            │
└────────────────────┴─────────────────┴─────────────────────────────┘

TIER RECOMMENDATION:
  - Awareness campaigns → Tier 0 (Schwartz) for strategy
  - Editorial advertorials → Tier 1 (Ogilvy, Halbert)
  - Curiosity headlines → Tier 2 (Bencivenga)
  - Direct response → Tier 1 (Kennedy)
```

---

## Benchmarks Reference

```yaml
NATIVE ADS BENCHMARKS 2025-2026:

CTR BENCHMARKS:
  Overall Average: 0.3%
  Good: 0.5-1.0%
  Great: >1.0%

  By Vertical:
    Health/Wellness: 0.4-0.8%
    Finance: 0.3-0.6%
    Education: 0.4-0.7%
    E-commerce: 0.3-0.5%
    B2B: 0.2-0.4%

CPC BENCHMARKS:
  Taboola: $0.30-0.80
  Outbrain: $0.40-1.20
  MGID: $0.10-0.50
  RevContent: $0.25-0.70

  By Geo:
    US: $0.50-1.50
    UK: $0.40-1.00
    Brazil: $0.10-0.40
    Europe: $0.30-0.80

LANDING PAGE BENCHMARKS:
  Time on Page: 2+ minutes (advertorial)
  Scroll Depth: 50%+
  Bounce Rate: 40-60%

CONVERSION BENCHMARKS:
  Lead Gen: 5-15%
  Direct Sale: 1-5%
  CPA Healthy: <1/3 product price
  ROAS Target: 3x+
```

---

## Quick Reference: Headline Bank

```yaml
DISCOVERY HEADLINES:
  - "[Local]: Novo [Produto] Viraliza Entre [Grupo]"
  - "[Profissão] Revela [Segredo] Que [Resultado]"
  - "Método de [Resultado] Descoberto Por [Pessoa Comum]"
  - "Brasileiros Descobrem [Solução] Que [Benefício]"

WARNING HEADLINES:
  - "O Que Acontece Quando Você [Ação Comum]"
  - "[Número] de Brasileiros Não Sabem Disso Sobre [Área]"
  - "Cuidado Com [Prática Comum]: [Consequência]"
  - "Alerta: [Produto/Hábito] Pode Estar [Consequência Negativa]"

PERSONAL STORY HEADLINES:
  - "Como [Resultado] Depois de [Situação Difícil]"
  - "[Pessoa]: '[Quote Surpreendente]'"
  - "De [Antes] Para [Depois] — A História de [Nome]"
  - "[Pessoa Comum] [Resultado Incrível] — Veja Como"

SCIENTIFIC HEADLINES:
  - "Estudo Revela [Descoberta] Sobre [Área]"
  - "Cientistas Descobrem Por Que [Fenômeno]"
  - "Nova Pesquisa Mostra [Insight Contraintuitivo]"
  - "Harvard/USP Confirma: [Descoberta]"
```

---

## Related Resources

- **Research Doc:** `docs/research/native-ads-methodology-research.md`
- **Landing Page Task:** `tasks/create-landing-page.md`
- **Sales Page Task:** `tasks/create-sales-page.md`
- **VSL Task:** `tasks/create-vsl.md`

---

*Task Version: 2.0*
*Lines: 1100+*
*Last Updated: 2026-01-23*
*Primary Frameworks: IAB Native Playbook, Ogilvy Headlines, Bencivenga Fascinations, Tabloid Techniques*
*Research Base: docs/research/native-ads-methodology-research.md*
