# Create Premium LP Copy

## Metadata

```yaml
task_id: create-premium-lp-copy
version: "1.0.0"
category: creation
elicit: true
estimated_time: "15-30 min"
difficulty: intermediate
output_format: yaml
output_schema: "squads/design/templates/premium-lp-content-schema.yaml"
handoff_to: "@premium-design *generate"
```

## Purpose

Gerar copy completa para uma Landing Page Premium (dark theme) atraves de elicitacao
estruturada. O output e um payload YAML que alimenta diretamente o comando `*generate`
do agente @premium-design no Design Squad.

**Pipeline:** Elicitacao → Copy Generation → Schema Formatting → Design Handoff

---

## Inputs

```yaml
required:
  - client_name: "Nome completo do profissional/marca"
  - client_expertise: "Area de atuacao principal (1-2 frases)"

optional:
  - brand_initials: "Iniciais para nav (ex: JCA). Default: derivado do nome"
  - photo_url: "URL ou path para foto. Default: photo.png"
  - scheduling_url: "URL de agendamento (cal.com, calendly, etc.)"
  - social_links: "LinkedIn, Instagram, etc."
  - existing_copy: "Copy existente para reaproveitamento"
  - tone: "premium_elegant | premium_bold | premium_minimal. Default: premium_elegant"
  - lang: "pt-BR | en | es. Default: pt-BR"
  - template: "nocturne_cian | obsidian_gold | carbon_blue | midnight_violet | eclipse_rose | stealth_emerald | crimson_noir | arctic_frost. Default: nocturne_cian"
  - tier: "base | enhanced | maximum. Default: enhanced"
```

---

## Copywriter Selection

Esta task usa **David Ogilvy** como copywriter primario:
- Tom elegante e sofisticado = LP premium
- Pesquisa profunda informa copy factual
- Headlines com beneficio especifico
- Credibilidade atraves de numeros

**Blend opcional com:**
- **Eugene Schwartz** — Para calibrar nivel de awareness do publico
- **Gary Bencivenga** — Para bullets nas expertise cards

---

## Workflow

### PHASE 1: ELICITATION (Interactive)

**CRITICAL: Todas as perguntas sao obrigatorias. Use AskUserQuestion tool.**

#### Step 1.1: Identidade & Posicionamento

```yaml
questions:
  - id: full_name
    question: "Qual o nome completo para o hero da LP?"
    example: "Jose Carlos Amorim"
    maps_to: hero.name

  - id: labels
    question: "Quais sao seus 2-4 titulos/papeis profissionais? (separados por virgula)"
    example: "AI Architect, Brand Strategist, Systems Thinker"
    maps_to: hero.labels
    validation: "1-4 items"

  - id: hero_description
    question: "Descreva em 1-2 frases o que voce faz e para quem. (max 200 chars)"
    example: "Transformo especialistas em marcas pessoais premium com IA e sistemas que escalam."
    maps_to: hero.description
    validation: "max_length: 200"

  - id: brand_initials
    question: "Quais iniciais usar na nav? (max 5 chars)"
    example: "JCA"
    maps_to: nav.brand
    default: "Derivado automaticamente do nome"
    validation: "max_length: 5"
```

#### Step 1.2: Prova Social & Metricas

```yaml
questions:
  - id: proof_metrics
    question: |
      Liste 3-6 metricas de prova social. Para cada uma, informe:
      - Numero (ex: 150)
      - Sufixo opcional (ex: +, %, M+, k)
      - Label (ex: Clientes Atendidos)

      Formato: numero sufixo | label
    example: |
      150+ | Clientes Atendidos
      12 | Anos de Experiencia
      97% | Taxa de Satisfacao
      50M+ | Revenue Gerado
    maps_to: proof.items
    validation: "2-6 items"
```

#### Step 1.3: Expertise & Especialidades

```yaml
questions:
  - id: expertise_cards
    question: |
      Liste 2-6 areas de expertise. Para cada uma:
      - Titulo curto (ex: AI Systems)
      - Descricao em 1 frase (max 150 chars)
      - Tags de tecnologia/skill (2-4 tags)
      - Marque [DESTAQUE] se for a principal (apenas 1)

      Formato: Titulo | Descricao | tag1, tag2, tag3 | [DESTAQUE]
    example: |
      AI Systems | Arquiteturas de IA que transformam operacoes manuais em sistemas autonomos. | Claude, GPT-4, LangChain | [DESTAQUE]
      Brand Strategy | Posicionamento premium para especialistas que querem dominar seu nicho. | Positioning, Messaging
      Sales Systems | Funis e automacoes que convertem trafego em receita previsivel. | Funnels, CRM
    maps_to: expertise.cards
    validation: "2-8 items, max 1 featured"
```

#### Step 1.4: Filosofia & Quote

```yaml
questions:
  - id: quote_text
    question: "Qual sua frase/filosofia que define sua abordagem? (max 300 chars)"
    example: "Technology is the amplifier. The human is the signal."
    maps_to: quote.text
    validation: "max_length: 300"

  - id: quote_role
    question: "Qual titulo/cargo para a atribuicao da frase?"
    example: "Founder, MMOS"
    maps_to: quote.attribution.role
```

#### Step 1.5: Stack Profissional

```yaml
questions:
  - id: stack_items
    question: |
      Liste 3-8 areas do seu stack profissional. Para cada:
      - Nome da area (ex: AI Architecture)
      - Detalhes/tecnologias (ex: Claude, GPT-4, LangChain)

      Formato: Nome | Detalhes
    example: |
      AI Architecture | Claude, GPT-4, LangChain, Vector DBs
      Web Development | Next.js, React, TypeScript, Tailwind
      Marketing | Funnels, Email, Paid Traffic, SEO
      Design | Figma, Framer, Design Systems
    maps_to: stack.items
    validation: "2-10 items"
```

#### Step 1.6: CTA & Links

```yaml
questions:
  - id: cta_heading
    question: "Qual o heading da secao final de CTA?"
    example: "Vamos Conversar?"
    maps_to: cta.heading
    default: "Vamos Conversar?"

  - id: cta_description
    question: "Descricao curta do CTA (max 200 chars). Deixe vazio para gerar automaticamente."
    example: "Agende uma conversa para explorar como posso ajudar a transformar sua marca pessoal."
    maps_to: cta.description
    validation: "max_length: 200"

  - id: scheduling_url
    question: "URL de agendamento (cal.com, calendly, etc.)"
    example: "https://cal.com/joseamorim"
    maps_to: cta.primary.href

  - id: cta_label
    question: "Texto do botao principal de CTA"
    example: "Agendar Agora"
    maps_to: cta.primary.label
    default: "Agendar Agora"

  - id: social_links
    question: |
      Quais links sociais incluir no footer? (1-4)
      Formato: label | url
    example: |
      LinkedIn | https://linkedin.com/in/joseamorim
      Instagram | https://instagram.com/joseamorim
    maps_to: footer.links
    validation: "0-4 items"
```

#### Step 1.7: Preferencias Visuais

```yaml
questions:
  - id: template_choice
    question: |
      Qual template visual? Opcoes:
      1. Nocturne Cian (ciano vibrante sobre preto)
      2. Obsidian Gold (dourado sobre preto)
      3. Carbon Blue (azul sobre preto)
      4. Midnight Violet (violeta sobre preto)
      5. Eclipse Rose (rosa sobre preto)
      6. Stealth Emerald (verde sobre preto)
      7. Crimson Noir (vermelho sobre preto)
      8. Arctic Frost (azul claro sobre preto)
    maps_to: config.template
    default: "nocturne_cian"

  - id: tier_choice
    question: |
      Qual nivel de efeitos visuais?
      1. Base — CSS puro, sem JavaScript (carregamento rapido)
      2. Enhanced — + scroll reveals, grain, progress bar, gradient text (recomendado)
      3. Maximum — + cursor custom, text split, counters, parallax, magnetic buttons
    maps_to: config.tier
    default: "enhanced"

  - id: photo_url
    question: "URL ou path da foto profissional (PNG com fundo transparente preferido)"
    example: "photo.png"
    maps_to: photo.url
    default: "photo.png"

  - id: photo_treatment
    question: |
      Tratamento da foto:
      1. Cinematic — Mascara + aura + aneis (padrao)
      2. Clean — Apenas mascara, sem efeitos
      3. Raw — Sem tratamento, imagem como esta
    maps_to: photo.treatment
    default: "cinematic"
```

---

### PHASE 2: COPY GENERATION

**Executor: Agent (Ogilvy style)**

Apos coletar todas as respostas, gerar copy refinada para cada secao.

#### Step 2.1: Refinar Hero Copy

```yaml
process:
  input: hero_description (raw do usuario)
  action: |
    Aplicar estilo Ogilvy:
    - Tom premium e sofisticado
    - Beneficio claro em 1-2 frases
    - Sem jargao tecnico excessivo
    - Palavras precisas, nenhuma desperdicada
  output: hero.description (refined, max 200 chars)

  also_generate:
    - hero.eyebrow: { number: "01", label: "Personal Brand" }
    - hero.cta_primary.label: "Derivar do contexto (ex: Agendar Conversa)"
    - hero.cta_secondary: { label: "Ver Portfolio", href: "#expertise" }
```

#### Step 2.2: Refinar Proof Metrics

```yaml
process:
  input: proof_metrics (raw do usuario)
  action: |
    - Validar que numeros sao impactantes
    - Ajustar labels para tom premium
    - Garantir 3-4 metricas (cortar se >4 para manter impacto)
    - Ordenar: mais impressionante primeiro
  output: proof.items[]

  also_generate:
    - proof.eyebrow: { number: "02", label: "Track Record" }
```

#### Step 2.3: Refinar Expertise Cards

```yaml
process:
  input: expertise_cards (raw do usuario)
  action: |
    Para cada card, aplicar Ogilvy + Bencivenga blend:
    - Titulo: Curto, impactante (2-3 palavras)
    - Descricao: Transformar em micro-bullet Bencivenga
      → Resultado especifico, nao feature
      → Max 150 chars
    - Tags: Manter tecnicas, curtas
    - Featured: Validar apenas 1 card marcado
  output: expertise.cards[]

  also_generate:
    - expertise.eyebrow: { number: "03", label: "Expertise" }
```

#### Step 2.4: Refinar Quote

```yaml
process:
  input: quote_text (raw do usuario)
  action: |
    - Manter autenticidade da voz do cliente
    - Ajustar ritmo e impacto se necessario
    - Garantir max 300 chars
    - Nao alterar se ja for forte
  output: quote.text

  also_generate:
    - quote.eyebrow: { number: "04", label: "Philosophy" }
    - quote.attribution: { name: "{client_name}", role: "{quote_role}" }
```

#### Step 2.5: Refinar Stack

```yaml
process:
  input: stack_items (raw do usuario)
  action: |
    - Ordenar por relevancia para o publico-alvo
    - Garantir detalhes tecnicos concisos
    - 4-6 items ideal (cortar se >6)
  output: stack.items[]

  also_generate:
    - stack.eyebrow: { number: "05", label: "Stack" }
    - stack.heading: "Professional Stack"
```

#### Step 2.6: Gerar CTA & Nav

```yaml
process:
  input: cta_heading, cta_description, scheduling_url, cta_label
  action: |
    - Se cta_description vazio, gerar com Ogilvy:
      "Agende uma conversa para explorar como posso ajudar."
    - Gerar nav links baseado nas secoes presentes
    - Gerar CTA secundario se social_links disponivel
  output: cta{}, nav{}

  auto_generate:
    nav:
      brand: "{brand_initials}"
      links:
        - { label: "Expertise", href: "#expertise" }
        - { label: "Stack", href: "#stack" }
        - { label: "Contato", href: "#cta" }
      cta: { label: "Agendar", href: "#cta" }

    cta:
      eyebrow: { number: "06", label: "Next Step" }
      heading: "{cta_heading}"
      description: "{cta_description or generated}"
      primary: { label: "{cta_label}", href: "{scheduling_url}" }
      secondary: "First social link if available"
```

#### Step 2.7: Gerar Footer

```yaml
process:
  input: social_links
  action: |
    - Copyright: "auto" (gera automaticamente com ano + nome)
    - Links: Mapear social_links para footer format
  output: footer{}
```

---

### PHASE 3: FORMAT (Schema Compliance)

**CRITICAL: O output DEVE seguir exatamente `premium-lp-content-schema.yaml`**

#### Step 3.1: Montar Payload

```yaml
assemble_payload:
  reference: "squads/design/templates/premium-lp-content-schema.yaml"

  structure:
    config:
      template: "{template_choice}"
      tier: "{tier_choice}"
      lang: "{lang}"

    nav:
      brand: "{brand_initials}"
      links: "[generated from sections]"
      cta: "{ label: 'Agendar', href: '#cta' }"

    hero:
      eyebrow: "{ number: '01', label: 'Personal Brand' }"
      name: "{full_name}"
      labels: "[from elicitation]"
      description: "[refined copy]"
      cta_primary: "{ label: '{cta_label}', href: '{scheduling_url}' }"
      cta_secondary: "{ label: 'Ver Portfolio', href: '#expertise' }"

    photo:
      url: "{photo_url}"
      alt: "{full_name}"
      treatment: "{photo_treatment}"

    proof:
      eyebrow: "{ number: '02', label: 'Track Record' }"
      items: "[from elicitation, refined]"

    expertise:
      eyebrow: "{ number: '03', label: 'Expertise' }"
      cards: "[from elicitation, refined]"

    quote:
      eyebrow: "{ number: '04', label: 'Philosophy' }"
      text: "[refined quote]"
      attribution: "{ name: '{full_name}', role: '{quote_role}' }"

    stack:
      eyebrow: "{ number: '05', label: 'Stack' }"
      heading: "Professional Stack"
      items: "[from elicitation, refined]"

    cta:
      eyebrow: "{ number: '06', label: 'Next Step' }"
      heading: "{cta_heading}"
      description: "[refined or generated]"
      primary: "{ label: '{cta_label}', href: '{scheduling_url}' }"
      secondary: "[first social link or null]"

    footer:
      copyright: "auto"
      links: "[from social_links]"
```

#### Step 3.2: Validate Payload

```yaml
validation_rules:
  required_fields:
    - config.template (must be in enum)
    - config.tier (must be in enum)
    - nav.brand (max 5 chars)
    - hero.name (non-empty)
    - hero.labels (1-4 items)
    - hero.description (max 200 chars)
    - hero.cta_primary.label
    - hero.cta_primary.href
    - photo.url
    - proof.items (2-6 items, each with number + label)
    - expertise.cards (2-8 items, each with title + description)
    - quote.text (max 300 chars)
    - stack.items (2-10 items, each with name + detail)
    - cta.heading
    - cta.primary.label
    - cta.primary.href

  constraints:
    - proof.items: "2-6 items"
    - expertise.cards: "2-8 items, max 1 featured"
    - stack.items: "2-10 items"
    - nav.links: "0-5 items"
    - footer.links: "0-4 items"
    - hero.labels: "1-4 items"
    - All descriptions: "max_length enforced"

  on_validation_error:
    - Log specific field and constraint violated
    - Auto-fix if possible (truncate, limit items)
    - Ask user only if required field is missing
```

---

### PHASE 4: OUTPUT & HANDOFF

#### Step 4.1: Output Payload

```yaml
output:
  format: yaml
  location: "outputs/premium-design/{template}/content-payload.yaml"

  display: |
    Apresentar o payload completo ao usuario em YAML formatado.
    Perguntar: "Payload pronto. Deseja:"
    1. Enviar direto para @premium-design *generate
    2. Revisar e ajustar alguma secao
    3. Salvar payload e parar aqui
```

#### Step 4.2: Handoff to Design Squad

```yaml
handoff:
  target_agent: "@premium-design"
  target_command: "*generate"

  handoff_message: |
    ## Handoff: CopywriterOS → Design Squad

    **Task:** create-premium-lp-copy (COMPLETE)
    **Payload:** [content-payload.yaml]
    **Template:** {config.template}
    **Tier:** {config.tier}

    **Quality Gate:**
    - [x] All required fields present
    - [x] All constraints validated
    - [x] Copy refined with Ogilvy style
    - [x] Schema compliance verified

    **Next:** @premium-design *generate --payload content-payload.yaml
```

---

## Quality Checklist

```yaml
copy_quality:
  - "[ ] Hero description comunica beneficio em <3 segundos"
  - "[ ] Labels sao especificos (nao genericos como 'Expert')"
  - "[ ] Proof metrics sao verificaveis e impactantes"
  - "[ ] Expertise cards tem resultados, nao features"
  - "[ ] Quote e autentica e memoravel"
  - "[ ] Stack items sao relevantes para o publico-alvo"
  - "[ ] CTA e claro e com baixa friccao"
  - "[ ] Tom e consistente (premium, sofisticado)"

schema_compliance:
  - "[ ] Todos os campos required preenchidos"
  - "[ ] Todos os constraints de length respeitados"
  - "[ ] Todos os enums validos"
  - "[ ] Estrutura YAML identica ao schema"

handoff_ready:
  - "[ ] Payload salvo em outputs/"
  - "[ ] Validacao completa sem erros"
  - "[ ] Usuario aprovou o conteudo"
```

---

## Error Handling

```yaml
errors:
  missing_required_field:
    action: "Perguntar ao usuario diretamente"
    retry: true

  constraint_violation:
    action: "Auto-fix se possivel, informar usuario"
    examples:
      - "description > 200 chars → truncar com ... e perguntar"
      - "proof.items > 6 → apresentar top 6 por impacto"
      - "labels > 4 → perguntar quais manter"

  invalid_enum:
    action: "Apresentar opcoes validas"
    retry: true

  scheduling_url_missing:
    action: "Usar '#cta' como fallback, avisar usuario"
    warning: "Sem URL de agendamento, o CTA nao tera link funcional"
```

---

## Usage Examples

### Via Copy Chief

```
User: @copy-chief
User: *premium-lp

Copy Chief: Vou iniciar o processo de criacao de copy para sua LP Premium.
            Usando David Ogilvy como copywriter principal.
            Vamos comecar com a elicitacao...

[Phase 1: 7 steps de perguntas]
[Phase 2: Refinamento automatico]
[Phase 3: Formatacao do payload]
[Phase 4: Handoff para @premium-design]
```

### Via Direct Task

```
User: @premium-design
User: *generate --elicit

premium-design: Preciso do payload de conteudo. Vou chamar o CopywriterOS...
[Executa create-premium-lp-copy]
[Recebe payload]
[Executa *generate]
```

### Via Workflow (Autonomous)

```
User: Criar LP premium para Maria Silva, consultora de RH
[Workflow premium-lp-complete executa tudo autonomamente]
[Output: HTML renderizado em outputs/premium-design/{template}/]
```

---

## Integration Points

```yaml
integrations:
  copywriter_os:
    agents_used: ["david-ogilvy", "gary-bencivenga"]
    tasks_extended: ["create-landing-page"]

  design_squad:
    agent_target: "premium-design"
    command_target: "*generate"
    schema_reference: "squads/design/templates/premium-lp-content-schema.yaml"
    tokens_reference: "squads/design/templates/premium-lp-tokens.yaml"
    template_reference: "squads/design/templates/premium-lp-template.html"

  copy_chief:
    new_command: "*premium-lp"
    routing: "Direct to create-premium-lp-copy task"
```

---

*Task Version: 1.0.0*
*Created: 2026-02-15*
*Output Schema: premium-lp-content-schema.yaml v1.0*
*Handoff Target: @premium-design *generate*
