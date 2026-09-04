# Create Ghosted Lead Recovery System

## Purpose

Criar sistema de recuperação de leads "ghosted" - pessoas que entraram no funil, demonstraram interesse, mas não converteram. Este task implementa táticas "break-the-glass" para reviver leads mortos e capturar receita que está vazando do funil.

> "Seu funil é como um balde furado. A maioria da água que você coloca simplesmente vaza pelo fundo. Você precisa de um sistema embaixo para capturar essa receita perdida."
> — Jeremy Haynes

---

## The Leaky Bucket Philosophy

```yaml
leaky_bucket_reality:

  typical_funnel:
    leads_in: 1000
    show_to_call: 500  # 50% show rate
    close_rate: 20%    # of those who show
    actual_buyers: 100 # only 10% of original

  question: "O que acontece com os outros 900 leads?"

  wrong_answer: "Eles estão perdidos"
  right_answer: "Eles estão em diferentes níveis de interesse que precisam de diferentes abordagens"

interest_spectrum:
  level_1: "Curioso" # Optou in mas não engajou
  level_2: "Interesse geral" # Engajou um pouco
  level_3: "Muito interessado" # Quase converteu
  level_4: "Convicto" # Pronto para comprar

  key_insight: |
    Deals acontecem acima da linha de convicção.
    Seu trabalho é elevar leads de níveis inferiores
    até que cruzem essa linha.

    O ERRO é abandonar leads que não converteram imediatamente.
```

---

## Types of Ghosted Leads

```yaml
ghosted_lead_categories:

  category_1_no_show:
    description: "Agendou call, não apareceu"
    interest_level: "Curiosidade → Interesse geral"
    recovery_potential: "ALTO"

  category_2_no_close:
    description: "Apareceu na call, não comprou"
    interest_level: "Interesse geral → Muito interessado"
    recovery_potential: "MUITO ALTO"

  category_3_webinar_no_show:
    description: "Registrou no webinar, não apareceu"
    interest_level: "Curiosidade"
    recovery_potential: "MÉDIO"

  category_4_webinar_no_buy:
    description: "Assistiu webinar, não comprou"
    interest_level: "Interesse geral → Muito interessado"
    recovery_potential: "ALTO"

  category_5_abandoned_checkout:
    description: "Chegou no checkout, não finalizou"
    interest_level: "Muito interessado → Quase convicto"
    recovery_potential: "MUITO ALTO"

  category_6_long_dead:
    description: "Leads antigos que esfriaram"
    interest_level: "Provavelmente zero"
    recovery_potential: "BAIXO mas volume compensa"
```

---

## Inputs

```yaml
required:
  - lead_sources: "De onde vêm os leads (call funnel, webinar, etc.)"
  - average_lead_age: "Há quanto tempo estão no sistema"
  - current_reactivation_efforts: "O que já estão fazendo"
  - offer_details: "Produto, preço, opções de pagamento"
  - sales_team_size: "Quantos vendedores + capacidade"

optional:
  - crm_data: "Dados de onde leads estão travando"
  - sales_feedback: "Por que leads não fecham segundo vendedores"
  - alternative_offers: "Outros produtos para oferecer"
  - content_assets: "Videos, emails, posts existentes"
```

---

## The Two-Layer Recovery System

### Layer 1: Systematic (Sempre Rodando)

```yaml
systematic_recovery:

  purpose: "Sistema automatizado que roda continuamente"

  components:

    1_weekly_owner_call:
      what: "Mini webinar semanal do owner"
      who: "Leads não convertidos das últimas 2-4 semanas"
      format: "20 slides, 30-45 min"
      flow:
        - "Apresentação curta (15 min)"
        - "Pitch"
        - "Q&A"
        - "Re-pitch"
        - "Mais Q&A"
      result: "Low 6-figures adicionais/mês"

    2_cleaner_role:
      what: "Vendedor dedicado a leads frios"
      who: "Leads após X dias sem atividade"
      responsibility: |
        - Recebe leads que closers principais abandonaram
        - Trabalha lista de leads antigos
        - Usa táticas break-the-glass
        - Convida para owner calls
        - Envia para funnels alternativos

    3_alternative_funnels:
      what: "Múltiplos caminhos de conversão"
      principle: |
        Se o funil original falhou, tente outro.
        Nem todo mundo quer webinar.
        Nem todo mundo quer call.
        Alguns preferem ler.
        Alguns preferem comprar direto.
      options:
        - "Call funnel para quem veio de webinar"
        - "Webinar para quem veio de call funnel"
        - "Low ticket para quem não pode high ticket"
        - "Oferta alternativa para quem rejeitou a principal"
        - "In-person event para quem precisa de mais toque"
```

### Layer 2: Break-the-Glass Tactics (Quando Precisa de Boost)

```yaml
break_the_glass_tactics:

  purpose: "Táticas pontuais para criar spikes de revenue"

  when_to_use:
    - "Calendário dos vendedores está vazio"
    - "Revenue está abaixo da meta"
    - "Período tipicamente lento (férias, etc.)"
    - "Precisa de cash injection rápido"

  when_NOT_to_use:
    - "Já tem muito momentum"
    - "Sales team sobrecarregado"
    - "Revenue está em alta"
```

---

## Break-the-Glass Tactic #1: "Sent from iPhone" Email

```yaml
sent_from_iphone:

  history: |
    Esta tática gerou 40.000+ respostas em 48 horas
    quando usada pela primeira vez no Grant Cardone's office.
    Literalmente parou a empresa por 2 dias para processar.

  how_it_works:
    subject: "following up"  # tudo minúsculo
    body: |
      are you still interested in [product/topic]?

      - [first name]

      Sent from my iPhone

    key_elements:
      - "Subject line: tudo minúsculo, casual"
      - "Body: uma linha só, tudo minúsculo"
      - "Assinatura: só primeiro nome com dash"
      - "Footer: 'Sent from my iPhone'"
      - "Empurrar unsubscribe/address para bem embaixo (dar vários enters)"

  why_it_works:
    - "Parece email pessoal, não marketing"
    - "Curiosidade sobre quem está mandando"
    - "Simplicidade desarma defesas"
    - "Parece urgente/importante"

  expected_response:
    - "Sim, ainda estou interessado"
    - "Não, obrigado" (pelo menos você sabe)
    - "Quem é você?" (oportunidade de reconectar)

  warning: |
    NÃO use quando já tem muito volume.
    Isso pode criar um TSUNAMI de respostas.
    Tenha equipe pronta para processar.
```

### Email Template Completo

```markdown
## Subject: following up

## Body:

are you still interested in [nome do produto/tópico]?

- [seu primeiro nome]

Sent from my iPhone









[Seu endereço comercial]
[Link de unsubscribe]
```

---

## Break-the-Glass Tactic #2: "Where Did We Lose You?" Email

```yaml
where_did_we_lose_you:

  purpose: "Reviver leads que ghostaram"

  psychology: |
    A maioria das respostas NÃO é feedback real.
    A maioria diz: "Você não me perdeu! Desculpa, estava ocupado..."
    E então voltam para o processo de compra.

  how_it_works:
    subject: "quick question"  # ou "pergunta rápida"
    body: |
      Hey [nome],

      Wondering if I could get a quick one-sentence feedback
      from you on where we lost you.

      Would really appreciate it.

      - [seu nome]

  variations:
    version_pt_br: |
      Oi [nome],

      Queria pedir um feedback rápido:
      onde foi que perdemos você?

      Uma frase só já ajuda.

      Obrigado,
      [seu nome]

    version_direct: |
      [nome],

      Percebi que não tivemos mais contato.

      Me ajuda a entender: o que aconteceu?

      - [seu nome]

  expected_responses:
    response_1:
      type: "Feedback real"
      example: "O preço estava acima do meu orçamento"
      action: "Oferecer alternativa ou pagamento"

    response_2:
      type: "Reativação"
      example: "Não me perderam! Estava viajando, mas ainda quero"
      action: "Reagendar imediatamente"

    response_3:
      type: "Fechamento"
      example: "Já comprei outra solução"
      action: "Remover da lista, talvez pedir feedback"
```

---

## Break-the-Glass Tactic #3: "For the Dogs" Sequence

```yaml
for_the_dogs:

  purpose: "Capturar os poucos que trabalham em períodos mortos"

  when_to_use:
    - "Black Friday weekend"
    - "Entre Natal e Ano Novo"
    - "Feriados prolongados"
    - "Qualquer período tipicamente 'morto'"

  philosophy: |
    Todo mundo assume que ninguém trabalha nesses períodos.
    MAS: existe uma minoria de pessoas altamente motivadas
    que estão justamente trabalhando quando outros descansam.

    Essas pessoas respondem a messaging que fala diretamente com elas.

  email_template:
    subject: "for the hungry ones"  # ou "para os famintos"
    body: |
      [Nome],

      Eu sei que a maioria das pessoas está descansando agora.

      Mas você não é a maioria, é?

      Se você é uma das poucas pessoas que está trabalhando
      enquanto outros tiram folga...

      Se você está usando esse tempo para se preparar
      para [próximo ano/trimestre]...

      Então tenho uma oportunidade para você.

      [OFERTA com deadline curto]

      Só para quem agir entre [data] e [data].

      Para os outros: aproveitem as férias.
      Para você: vamos conversar.

      [CTA]

      - [Nome]

  variations:
    incentive_version: |
      + Bônus especial para quem fechar nesse período
      + Desconto exclusivo (real, não fake)
      + Acesso antecipado a algo novo
```

---

## Break-the-Glass Tactic #4: Preferred Channel Discovery

```yaml
preferred_channel:

  purpose: "Descobrir onde o lead realmente vê mensagens"

  problem: |
    Você pode estar mandando emails mas ele só vê DM.
    Você pode estar mandando SMS mas ele odeia SMS.
    Cada pessoa tem um canal preferido.

  approach: |
    Quando nada funciona, BLAST em todos os canais:
    - Email
    - SMS
    - DM Instagram
    - DM LinkedIn
    - DM Facebook
    - WhatsApp (se tiver)

    Com UMA mensagem simples.

  message_template: |
    Oi [Nome],

    Tentei contato algumas vezes sem sucesso.

    Qual o melhor canal para falar com você?

    - [Seu nome] da [Empresa]

  expected_responses:
    - "Me manda no WhatsApp: [número]"
    - "Prefiro email: [email]"
    - "Para de me mandar mensagem" (pelo menos você sabe)

  important: |
    Isso pode parecer "agressivo" mas:
    1. Se eles realmente não querem, vão dizer
    2. Se querem mas não viram, você descobre onde veem
    3. Melhor do que perder o lead completamente
```

---

## Systematic Recovery: Weekly Owner Cleanup Call

```yaml
weekly_owner_call:

  format: "Mini webinar de 20-30 slides"
  duration: "30-45 minutos"
  frequency: "1-2x por semana"
  audience: "Leads não convertidos"

  structure:
    section_1:
      name: "Apresentação"
      duration: "15 minutos"
      content: "Versão condensada do pitch principal"

    section_2:
      name: "Pitch"
      duration: "5 minutos"
      content: "Oferta clara e direta"

    section_3:
      name: "Q&A"
      duration: "5 minutos"
      content: "Perguntas (algumas plantadas)"

    section_4:
      name: "Re-pitch"
      duration: "3 minutos"
      content: "Urgência e última chamada"

    section_5:
      name: "Mais Q&A"
      duration: "Quanto precisar"
      content: "Objection handling ao vivo"

  result_benchmark: |
    Brez & Pierre adicionaram low 6-figures/mês
    apenas com essa tática.

  templates_to_use:
    - "Mini Webinar 1.0 (genérico)"
    - "Mini Webinar 2.0 (make money offers)"
    - "DSL (Deck Sales Letter) format"
```

---

## Alternative Funnel Strategy

```yaml
alternative_funnels:

  principle: |
    "O mecanismo de conversão original FALHOU.
    Tente um mecanismo diferente até encontrar o que funciona."
    — Richard Bandler (VAK System adaptado para marketing)

  funnel_rotation:

    if_came_from_call_funnel:
      try_next:
        - "Webinar (talvez prefira ver antes de falar)"
        - "VSL longo (talvez precise de mais info)"
        - "Low ticket primeiro (talvez preço seja barreira)"
        - "Oferta diferente (talvez produto errado)"

    if_came_from_webinar:
      try_next:
        - "Call funnel (talvez prefira falar)"
        - "Direct checkout (talvez não queira webinar)"
        - "Weekly owner call (talvez precise de owner)"
        - "In-person event (talvez precise de presença)"

    if_price_is_issue:
      try_next:
        - "Drop sell (oferta menor)"
        - "Payment plan (parcelamento)"
        - "Financing (financiamento externo)"
        - "Starter offer (versão básica)"

    if_timing_is_issue:
      try_next:
        - "Nurture sequence longo"
        - "Conteúdo educacional"
        - "Newsletter"
        - "Retargeting de longo prazo"
```

---

## The Cleaner Role

```yaml
cleaner_role:

  definition: |
    Vendedor dedicado a trabalhar leads que os
    closers principais já desistiram.

  ideal_profile:
    - "Novo vendedor provando seu valor"
    - "Vendedor com mais paciência"
    - "Alguém bom em reconectar relacionamentos"

  responsibilities:
    - "Receber leads após X dias sem atividade"
    - "Trabalhar lista de leads antigos"
    - "Usar táticas break-the-glass"
    - "Convidar para owner calls"
    - "Rotear para funnels alternativos"
    - "Descobrir canal preferido"

  handoff_criteria:
    timing: "Após 14-30 dias sem atividade (depende do ciclo)"
    documentation: "Notas do closer original"

  tools_available:
    - "Break-the-glass emails"
    - "Multi-channel outreach"
    - "Owner call invites"
    - "Alternative offers"
    - "Content assets"
```

---

## Implementation Timeline

```yaml
implementation:

  phase_1_week_1:
    name: "Quick Wins"
    actions:
      - "Configurar 'Where did we lose you' email"
      - "Configurar 'Sent from iPhone' email"
      - "Identificar lista de leads ghosted"
      - "Enviar primeiro blast"
    expected_result: "Spike imediato de reativações"

  phase_2_week_2_3:
    name: "Systematic Setup"
    actions:
      - "Configurar Weekly Owner Call"
      - "Criar slides para mini webinar"
      - "Agendar primeiro call"
      - "Configurar invite automation"
    expected_result: "Sistema recorrente funcionando"

  phase_3_week_4_plus:
    name: "Full System"
    actions:
      - "Definir cleaner role"
      - "Configurar funnels alternativos"
      - "Criar multi-channel sequences"
      - "Estabelecer rotina de break-the-glass"
    expected_result: "Sistema completo de recuperação"
```

---

## Metrics to Track

```yaml
metrics:

  reactivation_metrics:
    - "Taxa de resposta dos emails break-the-glass"
    - "% de leads reativados que convertem"
    - "Revenue de leads reativados"

  owner_call_metrics:
    - "Attendance rate"
    - "Conversion rate"
    - "Revenue por call"

  cleaner_metrics:
    - "Leads processados por semana"
    - "Taxa de reativação"
    - "Revenue gerado"

  system_health:
    - "% de leads que chegam ao cleaner"
    - "Tempo médio até reativação"
    - "LTV de leads reativados vs. originais"
```

---

## Quality Checklist

```yaml
checklist:

  before_break_the_glass:
    - "[ ] Lista de leads segmentada por tipo de ghost"
    - "[ ] Equipe preparada para volume de respostas"
    - "[ ] Sistema de atribuição configurado"
    - "[ ] Respostas padrão prontas"

  weekly_owner_call:
    - "[ ] Slides prontos e testados"
    - "[ ] Perguntas plantadas definidas"
    - "[ ] Lista de convite segmentada"
    - "[ ] Link de registro funcionando"
    - "[ ] Follow-up sequence configurado"

  cleaner_role:
    - "[ ] Handoff process definido"
    - "[ ] Treinamento em táticas"
    - "[ ] Acesso a ferramentas necessárias"
    - "[ ] Metas e compensação claros"
```

---

## Output Deliverables

```yaml
deliverables:

  primary:
    - email_templates: |
        - Sent from iPhone
        - Where did we lose you
        - For the dogs
        - Preferred channel discovery

    - owner_call_setup: |
        - Slides template
        - Invite sequence
        - Follow-up sequence

  secondary:
    - cleaner_playbook: |
        - Processo de handoff
        - Scripts de reativação
        - Rotina diária

    - alternative_funnel_map: |
        - Qual funil usar quando
        - Triggers de rotação

  optional:
    - automation_flows: |
        - CRM sequences
        - Trigger rules
        - Reporting dashboards
```

---

## Version History

```yaml
version: "1.0"
created: "2025-01-24"
source: "Jeremy Haynes - Killer Follow-Up System"
key_results:
  - "40,000+ respostas em 48h (sent from iPhone)"
  - "Low 6-figures/mês adicionais (owner calls)"
  - "Maioria dos 'where did we lose you' reativa o lead"
```

---

*Task: Create Ghosted Lead Recovery System*
*Version: 1.0*
*Framework: Jeremy Haynes Killer Follow-Up System*
