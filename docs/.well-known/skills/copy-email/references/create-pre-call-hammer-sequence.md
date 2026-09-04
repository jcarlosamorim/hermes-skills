# Create Pre-Call Hammer Email Sequence

## Purpose

Criar sequência de emails de alta conversão usando o sistema "Hammer Them" de Jeremy Haynes. Este sistema envia **6 emails por dia** entre o momento que alguém agenda uma call e o momento que a call acontece, resultando em **20-40% de aumento em show rate**.

> "Quando alguém agenda uma call, eles NÃO estão vendidos em aparecer. Estão apenas interessados o suficiente para explorar. O ponto da sales call é converter. Se closers reclamam que leads não chegam prontos para comprar, o gap está na sequência pré-call."
> — Jeremy Haynes

---

## Tier 0: Diagnostic Questions

```yaml
tier_0_diagnosis:

  offer_clarity:
    - Qual é o produto/serviço sendo vendido?
    - Qual é o preço e modelo de pagamento?
    - Qual é a transformação prometida?
    - Quem é o cliente ideal (avatar específico)?

  call_funnel_metrics:
    - Qual o show rate atual? (benchmark: 50% = ruim, 70%+ = bom)
    - Quanto tempo entre agendamento e call? (24h, 48h, 72h?)
    - Quantos emails de lembrete você envia atualmente?
    - Qual o open rate dos emails atuais?

  common_questions:
    - Quais perguntas seus closers respondem TODA call?
    - Quais objeções aparecem repetidamente?
    - O que os leads NÃO sabem que deveriam saber antes da call?
    - Por que pessoas não aparecem às calls?

  content_inventory:
    - Você tem VSL/video de vendas?
    - Tem testimonials em video?
    - Tem case studies documentados?
    - Tem FAQ respondido em algum lugar?
```

---

## The "Hammer Them" Philosophy

### Por que 6 emails por dia?

```yaml
mindset_shift:
  wrong_thinking: "6 emails é spam, vão me odiar"
  right_thinking: "Se eles estão genuinamente interessados, QUEREM essa informação"

  analogy: |
    Imagine você considerando investir $10,000+ em algo.
    Você NÃO quer saber:
    - Como funciona em detalhes?
    - Quem mais fez e teve resultado?
    - Quanto tempo leva?
    - Quais são os riscos?
    - Como o pagamento funciona?

    Se a empresa te mandasse 6 emails por dia respondendo ESSAS perguntas,
    você reclamaria? Ou agradeceria por não ter que esperar a call para saber?

  result_benchmark:
    before: "30-50% show rate"
    after: "70-80% show rate"
    improvement: "20-40% increase"
```

### Os 4 Pilares do Conteúdo

```yaml
content_pillars:

  pillar_1_objections:
    what: "Objeções que surgem na sales call"
    examples:
      - "É muito caro"
      - "Não tenho tempo"
      - "Já tentei antes e não funcionou"
      - "Preciso falar com meu sócio/cônjuge"
    email_approach: "Abordar proativamente antes da call"

  pillar_2_questions:
    what: "Perguntas gerais sobre a oferta"
    examples:
      - "Como funciona?"
      - "Para quem é isso?"
      - "Quanto custa?"
      - "Quanto tempo leva?"
    email_approach: "Responder de forma educacional"

  pillar_3_questions_from_questions:
    what: "Perguntas que surgem das respostas anteriores"
    examples:
      - "Você disse X, mas e se Y?"
      - "Ok, mas como isso funciona para [minha situação]?"
      - "Quais são as opções de pagamento?"
    email_approach: "Antecipar follow-ups naturais"

  pillar_4_expectations:
    what: "O que esperar do processo e resultados"
    examples:
      - "Quanto tempo até ver resultados?"
      - "O que eu preciso fazer?"
      - "Qual o comprometimento necessário?"
      - "O que acontece depois que eu compro?"
    email_approach: "Definir expectativas realistas"
```

---

## Inputs

```yaml
required:
  - offer_name: "Nome do produto/programa"
  - price: "Preço principal"
  - target_avatar: "Descrição do cliente ideal"
  - time_to_call: "Tempo médio entre agendamento e call (24h, 48h, 72h)"
  - top_5_questions: "5 perguntas mais frequentes que closers respondem"
  - top_3_objections: "3 objeções mais comuns"
  - transformation_promise: "O resultado específico que entregam"

optional:
  - case_studies: "Histórias de sucesso com detalhes específicos"
  - testimonials: "Depoimentos de clientes"
  - video_assets: "VSL, videos de testimonial, etc."
  - faq_document: "FAQ existente"
  - sales_team_feedback: "Input dos closers sobre gaps de conhecimento"
  - payment_options: "Opções de pagamento (à vista, parcelado, financiamento)"
```

---

## Email Structure Framework

### Anatomia de um Email "Hammer"

```yaml
email_anatomy:

  subject_line:
    style: "Casual, como se fosse de pessoa para pessoa"
    length: "< 50 caracteres"
    examples:
      - "pergunta rápida"
      - "sobre sua call amanhã"
      - "isso é importante"
      - "esqueci de mencionar"
    avoid:
      - "URGENTE!!!"
      - "Não perca!!!"
      - "Oferta especial!!!"

  opening:
    style: "Direto, sem enrolação"
    examples:
      - "Uma coisa que muita gente pergunta..."
      - "Antes da nossa call, queria esclarecer..."
      - "Muita gente fica em dúvida sobre..."

  body:
    style: "Conversacional, educacional"
    length: "200-400 palavras"
    format: "Parágrafos curtos (1-3 linhas)"
    elements:
      - "Responde UMA pergunta/objeção por email"
      - "Usa exemplos concretos"
      - "Inclui números específicos quando possível"
      - "Pode linkar para conteúdo de suporte"

  closing:
    style: "Soft, sem pressão"
    examples:
      - "Nos vemos na call!"
      - "Qualquer dúvida, responde aqui."
      - "Te vejo [dia] às [hora]."

  signature:
    format: "Pessoal, não corporativo"
    example: |
      - [Nome]

      PS: [Teaser do próximo email ou lembrete útil]
```

---

## 72-Hour Sequence Template

### Para calls com 72h de antecedência (18 emails total)

```yaml
day_1_emails:
  # 6 emails no primeiro dia

  email_1:
    timing: "Imediatamente após agendamento"
    pillar: "expectations"
    subject: "sua call está confirmada"
    focus: "Confirmação + o que esperar da call"
    content_points:
      - "Call confirmada para [data/hora]"
      - "O que vamos cobrir na call"
      - "Como se preparar"
      - "Quanto tempo vai durar"

  email_2:
    timing: "+2 horas"
    pillar: "questions"
    subject: "como funciona [oferta]"
    focus: "Explicação high-level do processo"
    content_points:
      - "Visão geral do método/programa"
      - "Os principais pilares"
      - "O que você vai aprender/receber"

  email_3:
    timing: "+4 horas"
    pillar: "questions"
    subject: "para quem é isso (e para quem NÃO é)"
    focus: "Qualificação/desqualificação"
    content_points:
      - "O perfil ideal de cliente"
      - "Quem NÃO deveria comprar"
      - "Pré-requisitos se houver"

  email_4:
    timing: "+6 horas"
    pillar: "objections"
    subject: "sobre o investimento"
    focus: "Preço e ROI"
    content_points:
      - "O investimento é [preço]"
      - "Por que esse valor?"
      - "O retorno típico"
      - "Opções de pagamento"

  email_5:
    timing: "+8 horas"
    pillar: "questions_from_questions"
    subject: "e se eu não tiver [objeção comum]?"
    focus: "Responder dúvida derivada"
    content_points:
      - "Muita gente pergunta X depois de saber Y"
      - "A resposta é..."
      - "Exemplo de alguém na mesma situação"

  email_6:
    timing: "+10 horas"
    pillar: "expectations"
    subject: "quanto tempo até ver resultados?"
    focus: "Timeline realista"
    content_points:
      - "Expectativa realista de timeline"
      - "O que determina velocidade"
      - "Exemplo de caso real"

day_2_emails:
  # 6 emails no segundo dia

  email_7:
    timing: "Manhã"
    pillar: "objections"
    subject: "já tentei outras coisas..."
    focus: "Diferenciação"
    content_points:
      - "Por que outros métodos falham"
      - "O que torna isso diferente"
      - "Case study de alguém que também tinha tentado"

  email_8:
    timing: "+2 horas"
    pillar: "questions"
    subject: "o que eu preciso fazer?"
    focus: "Comprometimento necessário"
    content_points:
      - "Tempo semanal necessário"
      - "O que você faz vs. o que nós fazemos"
      - "O nível de suporte incluído"

  email_9:
    timing: "+4 horas"
    pillar: "expectations"
    subject: "case study: [nome] de [situação] para [resultado]"
    focus: "Prova social detalhada"
    content_points:
      - "História completa de um cliente"
      - "Situação antes"
      - "O que fez"
      - "Resultado específico"

  email_10:
    timing: "+6 horas"
    pillar: "objections"
    subject: "não tenho tempo..."
    focus: "Objeção de tempo"
    content_points:
      - "Reconhecer a preocupação"
      - "Quanto tempo REALMENTE leva"
      - "Exemplo de alguém ocupado que conseguiu"

  email_11:
    timing: "+8 horas"
    pillar: "questions_from_questions"
    subject: "e a garantia?"
    focus: "Remoção de risco"
    content_points:
      - "Detalhes da garantia"
      - "Como funciona o processo"
      - "Por que oferecemos isso"

  email_12:
    timing: "+10 horas"
    pillar: "expectations"
    subject: "amanhã é o dia"
    focus: "Lembrete + preparação"
    content_points:
      - "Sua call é amanhã"
      - "Como se preparar"
      - "O que ter em mãos"
      - "Venha com perguntas"

day_3_emails:
  # 6 emails no dia da call

  email_13:
    timing: "Manhã cedo"
    pillar: "expectations"
    subject: "hoje é o dia"
    focus: "Lembrete + motivação"
    content_points:
      - "Sua call é HOJE"
      - "Horário: [hora]"
      - "Animado para conversar"

  email_14:
    timing: "+2 horas"
    pillar: "objections"
    subject: "última coisa antes da call"
    focus: "Objeção final"
    content_points:
      - "Uma última preocupação que muitos têm"
      - "Como abordamos isso"

  email_15:
    timing: "2 horas antes"
    pillar: "expectations"
    subject: "em 2 horas"
    focus: "Lembrete logístico"
    content_points:
      - "Call em 2 horas"
      - "Link: [link]"
      - "Esteja em lugar quieto"

  email_16:
    timing: "1 hora antes"
    pillar: "questions"
    subject: "última chance de perguntas"
    focus: "Abertura para dúvidas"
    content_points:
      - "Alguma dúvida antes da call?"
      - "Responde esse email que leio"

  email_17:
    timing: "30 min antes"
    pillar: "expectations"
    subject: "30 minutos"
    focus: "Urgência suave"
    content_points:
      - "Começamos em 30 min"
      - "Te vejo lá"

  email_18:
    timing: "No horário"
    pillar: "expectations"
    subject: "estamos ao vivo"
    focus: "Call to action final"
    content_points:
      - "Estou te esperando"
      - "Clica aqui: [link]"
```

---

## 48-Hour Sequence (Adaptado)

```yaml
adaptation_48h:
  total_emails: 12
  distribution:
    day_1: 6 emails
    day_2: 6 emails

  priority_topics:
    - "Confirmação + expectativas"
    - "Como funciona"
    - "Preço e ROI"
    - "Para quem é/não é"
    - "Case study principal"
    - "Objeção #1 (preço)"
    - "Objeção #2 (tempo)"
    - "Garantia"
    - "Lembretes (manhã, 2h, 1h, agora)"
```

---

## 24-Hour Sequence (Mínimo Viável)

```yaml
adaptation_24h:
  total_emails: 6
  priority_order:
    1: "objections" # Preço - mais importante
    2: "questions" # Como funciona
    3: "expectations" # Timeline/resultados
    4: "objections" # Outra objeção comum
    5: "questions_from_questions" # Follow-up natural
    6: "expectations" # Lembrete final

  note: |
    Com apenas 24h, priorize as objeções mais críticas primeiro.
    Se só uma coisa ficar na cabeça deles, que seja o preço e o ROI.
```

---

## Integration with Hammer Them Strategy

### Cross-Channel Approach

```yaml
hammer_them_integration:

  principle: |
    Os MESMOS tópicos dos emails devem virar:
    - Short-form content (Reels, TikTok, Shorts)
    - Retargeting ads
    - SMS (se tiver)
    - DMs (se setter team)

  workflow:
    1: "Escrever o email sobre [tópico]"
    2: "Converter em script de 30-60 segundos"
    3: "Gravar como short-form"
    4: "Usar como retargeting ad para lista de calls agendadas"
    5: "Bombardear de todos os ângulos"

  result: |
    Lead agendado vê a mensagem:
    - No email
    - No feed do Instagram
    - No feed do TikTok
    - No YouTube Shorts
    - Em ads de retargeting

    É IMPOSSÍVEL não absorver a informação.
```

---

## Quality Validation

```yaml
validation_checklist:

  per_email:
    - "[ ] Subject line < 50 caracteres e casual?"
    - "[ ] Responde UMA pergunta/objeção específica?"
    - "[ ] Tom conversacional (não corporativo)?"
    - "[ ] Parágrafos curtos (1-3 linhas)?"
    - "[ ] Inclui exemplo concreto ou número específico?"
    - "[ ] Fechamento suave (não agressivo)?"

  sequence_complete:
    - "[ ] Cobre todas as 4 categorias (obj/quest/quest²/expect)?"
    - "[ ] Aborda as top 3 objeções?"
    - "[ ] Inclui pelo menos 1 case study detalhado?"
    - "[ ] Explica o preço e ROI claramente?"
    - "[ ] Tem lembretes estratégicos nos momentos certos?"
    - "[ ] Tom consistente em todos os emails?"

  metrics_to_track:
    - "Open rate por email (benchmark: 45%+)"
    - "Show rate antes vs depois (benchmark: +20%)"
    - "Close rate na call (deve aumentar também)"
    - "Tempo médio de call (deve diminuir)"
```

---

## Output Deliverables

```yaml
deliverables:

  primary:
    - complete_sequence: |
        Todos os emails escritos, palavra por palavra
        Organizados por dia e timing

    - implementation_guide: |
        Como configurar no CRM/ESP
        Triggers e automações necessárias

  secondary:
    - content_scripts: |
        Versão short-form de cada email
        Para usar no Hammer Them Strategy

    - tracking_dashboard: |
        Métricas para acompanhar
        Benchmarks esperados

  optional:
    - sms_adaptations: |
        Versão SMS dos emails-chave
        Para quem tem SMS marketing
```

---

## Common Mistakes to Avoid

```yaml
mistakes:

  mistake_1:
    wrong: "Enviar emails genéricos de 'lembrete'"
    right: "Enviar emails educacionais que respondem perguntas reais"

  mistake_2:
    wrong: "Ter medo de enviar 6 emails por dia"
    right: "Entender que quem está considerando investir QUER a informação"

  mistake_3:
    wrong: "Usar tom corporativo e formal"
    right: "Escrever como se fosse um amigo mandando do celular"

  mistake_4:
    wrong: "Colocar múltiplos tópicos em um email"
    right: "UM email = UMA pergunta/objeção respondida"

  mistake_5:
    wrong: "Não mencionar o preço até a call"
    right: "Ser transparente sobre preço, ROI e opções de pagamento"
```

---

## Version History

```yaml
version: "1.0"
created: "2025-01-24"
source: "Jeremy Haynes - 6 Emails Per Day System"
validated_results:
  - "20-40% increase in show rate"
  - "45-50% open rate on emails"
  - "Higher close rate on calls (leads arrive pre-sold)"
```

---

*Task: Create Pre-Call Hammer Email Sequence*
*Version: 1.0*
*Framework: Jeremy Haynes Hammer Them System*
