# Create Launch Emails Task

## Purpose

Criar sequências completas de email para lançamentos que constroem antecipação no pré-lançamento, geram momentum no carrinho aberto, e maximizam conversões durante o fechamento usando a metodologia Product Launch Formula (Jeff Walker) e princípios de psicologia de urgência.

## When to Use

- Lançamento de produto novo (digital, físico, serviço)
- Abertura de carrinho para cursos/programas
- Lançamento semente (primeira vez vendendo)
- Lançamento interno (para lista existente)
- Lançamento de afiliados/JV
- Lançamento perpétuo/evergreen
- Campanhas de tempo limitado
- Reabertura de produto existente

## Theoretical Foundation

### The Product Launch Formula (Jeff Walker)

O PLF gerou mais de $1 bilhão em vendas. A metodologia baseia-se em três elementos fundamentais:

1. **Stories** - Narrativas autênticas que criam conexões emocionais
2. **Sequences** - Eventos de marketing estrategicamente cronometrados
3. **Triggers** - Mecanismos psicológicos que influenciam decisões de compra

> "The launch isn't won at the opening. It's won at the close."

### The Four Launch Phases

**Phase 1: Pre-Prelaunch (2-4 semanas antes)**
- Construir antecipação com sneak peeks
- Obter feedback sobre a oferta
- Criar curiosidade e engajamento

**Phase 2: Prelaunch (7-10 dias)**
- Entregar 3 conteúdos sequenciais (PLCs)
- Educar enquanto constrói desejo
- Criar ownership mental do resultado

**Phase 3: Open Cart (5-7 dias)**
- Lançar vendas com engajamento diário
- Emailar lista todos os dias
- Construir momentum para o fechamento

**Phase 4: Cart Close (24-48 horas finais)**
- Gera aproximadamente 50% do total de vendas
- 3-4 emails no último dia
- Última mensagem 90 minutos antes do fim

### Psychology of Urgency & Scarcity

**Por que funciona (neurológico):**
- Escassez aumenta valor percebido
- Loss aversion ativa resposta de ameaça
- FOMO dispara mecanismos de sobrevivência evolutivos

**Princípios de Cialdini em Launches:**
1. Authority (expertise via PLCs)
2. Reciprocity (valor gratuito cria obrigação)
3. Social Proof (testemunhos e comunidade)
4. Scarcity (disponibilidade limitada)
5. Commitment/Consistency (pequenos engajamentos)
6. Liking (histórias criam conexão)

---

## Inputs

```yaml
required:
  product_name: "Nome do produto"
  launch_type: "Tipo (semente, interno, PLF completo, perpétuo, JV)"
  cart_open_date: "Data de abertura do carrinho"
  cart_close_date: "Data de fechamento"
  main_offer: "Oferta principal com preço"
  target_avatar: "Descrição do cliente ideal"
  transformation: "De [estado atual] para [estado desejado]"

optional:
  price: "Preço do produto"
  payment_options: "Opções de pagamento disponíveis"
  bonuses: "Lista de bônus com valores"
  bonus_deadlines: "Quando cada bônus expira"
  testimonials: "Depoimentos com nome, resultado, tempo"
  guarantee: "Garantia oferecida"
  plc_topics: "Tópicos dos 3 PLCs (se aplicável)"
  urgency_elements: "Elementos reais de escassez"
  prelaunch_dates: "Datas dos PLCs"
  list_size: "Tamanho da lista"
  previous_launches: "Dados de lançamentos anteriores"
  copywriter_preference: "Copywriter específico desejado"
```

---

## Workflow

### Step 1: Launch Type Selection & Timeline Mapping

```yaml
launch_types:

  seed_launch:
    description: "Primeiro lançamento, criando enquanto vende"
    list_size: "<2000"
    timeline:
      prelaunch: "5-7 dias"
      cart_open: "3-5 dias"
    characteristics:
      - Tom mais pessoal e conversacional
      - "Estou criando isso com você"
      - Caps menores (escassez legítima)
      - Posicionamento de co-criação
    email_volume: "Menor, mais íntimo"

  internal_launch:
    description: "Lançamento para lista existente"
    list_size: "2000+"
    timeline:
      prelaunch: "7-10 dias"
      cart_open: "5-7 dias"
    characteristics:
      - Leverage testemunhos existentes
      - Referência sucesso passado
      - Volume maior no cart close
      - Múltiplos bônus com deadlines escalonados
    email_volume: "Alto, especialmente no close"

  jv_affiliate_launch:
    description: "Tráfego de parceiros/afiliados"
    timeline:
      prelaunch: "10-14 dias"
      cart_open: "7 dias"
    characteristics:
      - Swipe copy para afiliados
      - Mensagens coordenadas
      - Leaderboards para afiliados
      - Prelaunch estendido para warm-up
    email_volume: "Alto + suporte a afiliados"

  evergreen_perpetual:
    description: "Sequência automatizada, sempre disponível"
    timeline:
      prelaunch: "Automático baseado em trigger"
      cart_open: "5-7 dias do trigger"
    characteristics:
      - Deadlines personalizados
      - Webinar automatizado integrado
      - Sequências behavior-triggered
      - A/B testing contínuo
    email_volume: "Automatizado, otimizado"
```

**Launch Timeline Template:**
```
PRÉ-PRELAUNCH (Dias -14 a -8)
├── Dia -14: Seed email (criar curiosidade)
├── Dia -11: Tease email (compartilhar o "porquê")
└── Dia -8: Anúncio (revelar data)

PRELAUNCH (Dias -7 a -1)
├── Dia -7: PLC 1 Release
├── Dia -6: PLC 1 Reminder
├── Dia -5: PLC 1 Discussion
├── Dia -4: PLC 2 Release
├── Dia -3: PLC 2 Reminder
├── Dia -2: PLC 3 Release
└── Dia -1: "Amanhã às [hora]"

CART OPEN (Dias 1-5)
├── Dia 1: 2-3 emails (abertura + fast action)
├── Dia 2: Email de valor/mecanismo
├── Dia 3: Email de prova social
├── Dia 4: Email de objeções/FAQ
└── Dia 5: Email de bônus expirando

CART CLOSE (Dias 6-7)
├── Dia 6: 2 emails (24h warning + story)
└── Dia 7: 4 emails (final push)
```

---

### Step 2: Pre-Prelaunch Sequence

```yaml
pre_prelaunch_emails:

  email_seed:
    timing: "Dia -14"
    purpose: "Criar curiosidade, sem revelar nada"
    subject_lines:
      - "Algo está chegando..."
      - "Tenho trabalhado em algo especial"
      - "Você vai querer saber disso"

    template: |
      Assunto: Algo está chegando...

      [Nome],

      Tenho trabalhado em algo pelos últimos [tempo].

      Ainda não posso revelar tudo, mas digamos que se você
      quer [resultado desejado], vai gostar muito do que está vindo.

      Fique de olho na sua caixa de entrada nas próximas semanas.

      [Assinatura]

      P.S. Se você tem lutado com [dor principal], isso é pra você.

  email_tease:
    timing: "Dia -11"
    purpose: "Compartilhar o 'porquê' da criação"
    subject_lines:
      - "Por que eu criei isso"
      - "A história por trás do que está vindo"
      - "Você perguntou, eu ouvi"

    template: |
      Assunto: Por que eu criei isso

      [Nome],

      Sabe aquela [dor/frustração] que você sente com [área]?

      Eu passei por isso também. E durante [tempo], tentei
      [abordagens comuns] sem muito sucesso.

      Foi aí que desenvolvi [método/sistema] que mudou tudo.

      Nos próximos dias, vou mostrar exatamente como funciona.

      Mas por enquanto, quero saber: qual é seu maior desafio
      quando se trata de [área]?

      Responda esse email—eu leio cada resposta.

      [Assinatura]

  email_announcement:
    timing: "Dia -8"
    purpose: "Revelar a data, criar compromisso"
    subject_lines:
      - "Marque no calendário: [data]"
      - "[Data]: O dia que vai mudar sua [área]"
      - "Salve essa data"

    template: |
      Assunto: Marque no calendário: [data]

      [Nome],

      O momento chegou.

      No dia [data], vou lançar [descrição breve do produto].

      É para [avatares] que querem [resultado] sem [dor comum].

      Vou te mandar um link especial quando abrir.

      Por enquanto, marque [data] no calendário.

      Vai valer a pena.

      [Assinatura]
```

---

### Step 3: Prelaunch Content (PLC) Emails

```yaml
plc_framework:

  plc_1_opportunity:
    purpose: "Mostrar O QUE é possível"
    structure: "PSP (Problema-Solução-Problema)"
    content_focus:
      - Revelar a oportunidade
      - Sua história + transformação
      - Cliffhanger para PLC 2
    duration: "15-30 minutos"

    release_email:
      timing: "Dia -7"
      subject: "[PLC 1] - Assista isso"

      template: |
        Assunto: A verdade sobre [tópico] que ninguém conta

        [Nome],

        Acabei de publicar algo que você precisa ver.

        É um vídeo de [X] minutos onde eu revelo:

        → [Ponto 1 que gera curiosidade]
        → [Ponto 2 sobre a oportunidade]
        → Por que a maioria das pessoas falha em [área]

        Se você quer [resultado], isso muda tudo.

        → [Link para PLC 1]

        Assista agora—vou tirar do ar em [tempo].

        [Assinatura]

        P.S. No final do vídeo, mostro [teaser do próximo conteúdo].

    reminder_email:
      timing: "Dia -6"
      subject: "Você assistiu?"

      template: |
        Assunto: Você assistiu?

        [Nome],

        Ontem publiquei [descrição do PLC 1].

        Se você ainda não assistiu, não perca.

        Já tivemos [X] pessoas assistindo e os comentários
        estão incríveis:

        "[Comentário real ou simulado]" - [Nome]

        O vídeo estará disponível até [tempo].

        → [Link]

        [Assinatura]

    discussion_email:
      timing: "Dia -5"
      subject: "O que as pessoas estão dizendo..."

      template: |
        Assunto: O que as pessoas estão dizendo...

        [Nome],

        O [PLC 1] gerou uma reação incrível.

        Olha alguns comentários que recebi:

        "[Comentário 1]" - [Nome]
        "[Comentário 2]" - [Nome]
        "[Comentário 3]" - [Nome]

        Se você ainda não assistiu, corre lá:
        → [Link]

        E amanhã... o próximo vídeo vai te mostrar exatamente
        COMO [transformação] funciona na prática.

        [Assinatura]

  plc_2_transformation:
    purpose: "Mostrar POR QUE funciona (provas)"
    structure: "PSP continuado"
    content_focus:
      - Case studies e transformações
      - Mecanismo por trás dos resultados
      - Prova de que funciona
    duration: "20-40 minutos"

    release_email:
      timing: "Dia -4"
      subject: "Como [Nome] conseguiu [resultado] em [tempo]"

      template: |
        Assunto: Como [Nome] conseguiu [resultado] em [tempo]

        [Nome],

        O segundo vídeo está no ar.

        Nele, você vai conhecer histórias como a de [Nome],
        que foi de [antes] para [depois] em apenas [tempo].

        Eu mostro:
        → O mecanismo exato por trás de [transformação]
        → Por que [abordagem comum] não funciona
        → O que [pessoas de sucesso] fazem diferente

        É a prova de que [resultado] é possível para você também.

        → [Link para PLC 2]

        [Assinatura]

    reminder_email:
      timing: "Dia -3"
      subject: "A transformação de [Nome]"

      template: |
        Assunto: A transformação de [Nome]

        [Nome],

        No vídeo de ontem, mostrei como [Nome] conseguiu
        [resultado específico] usando [método].

        Se você quer o mesmo para você, precisa assistir.

        → [Link]

        Amanhã, vou revelar exatamente COMO você pode
        aplicar isso na sua vida/negócio.

        [Assinatura]

  plc_3_ownership:
    purpose: "Mostrar COMO (criar ownership mental)"
    structure: "PSP fechamento"
    content_focus:
      - O caminho passo a passo
      - Preview da oferta
      - Criar sensação de já possuir
    duration: "25-45 minutos"

    release_email:
      timing: "Dia -2"
      subject: "O caminho completo revelado"

      template: |
        Assunto: O caminho completo revelado

        [Nome],

        Este é o vídeo mais importante da série.

        Hoje eu revelo o caminho completo de [estado atual]
        para [estado desejado].

        Você vai ver:
        → Os [X] passos exatos do processo
        → O que você precisa ter/fazer/ser
        → Como [Produto] se encaixa nisso

        E no final... uma surpresa.

        → [Link para PLC 3]

        Assista até o fim.

        [Assinatura]

  cart_opens_tomorrow:
    timing: "Dia -1"
    subject: "Amanhã às [hora]"

    template: |
      Assunto: Amanhã às [hora]

      [Nome],

      Amanhã, às [hora], o carrinho de [Produto] abre.

      Se você assistiu os vídeos, sabe que isso é diferente
      de tudo que você já viu sobre [área].

      Se você quer [resultado], amanhã é o momento.

      Vou te mandar o link assim que abrir.

      Fique de olho na sua caixa de entrada às [hora].

      [Assinatura]

      P.S. As primeiras [X] pessoas ganham [Fast Action Bonus].
```

---

### Step 4: Cart Open Sequence

```yaml
cart_open_emails:

  day_1_open:
    email_count: 3
    purpose: "Capturar action-takers imediatamente"

    email_1_morning:
      timing: "9h"
      subject_options:
        - "[Produto] está aberto"
        - "É hoje"
        - "Chegou o momento"
        - "Finalmente"

      template: |
        Assunto: [Produto] está aberto

        [Nome],

        Acabou a espera. [Produto] está oficialmente disponível.

        Se você quer [resultado principal] sem [dor comum],
        esse é o momento de agir.

        **O que é [Produto]:**
        [2-3 linhas descrevendo a essência]

        **Para quem é:**
        ✓ [Avatar 1] que quer [resultado 1]
        ✓ [Avatar 2] que quer [resultado 2]
        ✓ [Avatar 3] que quer [resultado 3]

        **O que você recebe:**
        ✓ [Componente 1] (valor R$[X])
        ✓ [Componente 2] (valor R$[X])
        ✓ [Componente 3] (valor R$[X])
        ✓ [Bônus se houver]

        **Investimento:** R$[preço] ou [parcelas]

        O carrinho fica aberto até [data]. Depois disso,
        [consequência real].

        → [Link para página de vendas]

        [Assinatura]

        P.S. As primeiras [X] pessoas que entrarem ganham
        [Fast Action Bonus]. Não espere.

    email_2_afternoon:
      timing: "14h"
      subject: "[Fast Action Bonus] - Últimas horas"

      template: |
        Assunto: [Bônus] para quem entrar até [hora]

        [Nome],

        Lembrete rápido:

        Quem entrar em [Produto] até [hora de hoje] ganha
        [Fast Action Bonus] — de graça.

        É [descrição do bônus] que normalmente custa R$[valor].

        Depois de [hora], esse bônus sai da oferta.

        → [Link]

        [Assinatura]

    email_3_evening:
      timing: "20h"
      subject: "[X] pessoas já entraram"

      template: |
        Assunto: [X] pessoas já entraram

        [Nome],

        [Produto] abriu há [X] horas e [número] pessoas
        já estão dentro.

        Enquanto você lê esse email, mais pessoas estão
        garantindo suas vagas.

        Se você estava esperando um "sinal", esse é ele.

        → [Link]

        [Assinatura]

        P.S. [Fast Action Bonus] expira à meia-noite.

  day_2_value:
    timing: "10h"
    purpose: "Educar sobre o mecanismo/método"
    subject: "Por que [método] funciona"

    template: |
      Assunto: Por que [método] funciona

      [Nome],

      Você pode estar se perguntando: "Como [Produto]
      realmente funciona?"

      Deixa eu explicar o mecanismo por trás:

      [Explicação de 3-5 parágrafos sobre COMO o produto
      gera resultados, focando no diferencial]

      A maioria das pessoas tenta [abordagem comum] e falha
      porque [razão].

      [Produto] resolve isso porque [diferencial único].

      É por isso que [estatística de sucesso ou prova].

      → [Link] Veja exatamente o que você recebe

      [Assinatura]

      P.S. Amanhã vou compartilhar histórias reais de pessoas
      que já passaram por [Produto].

  day_3_social_proof:
    timing: "10h"
    purpose: "Prova social com casos reais"
    subject: "[Nome] conseguiu [resultado] em [tempo]"

    template: |
      Assunto: [Nome] conseguiu [resultado] em [tempo]

      [Nome],

      Quero te mostrar resultados reais de pessoas que
      passaram por [Produto]:

      ---

      **[Cliente 1]**
      "[Depoimento detalhado com resultado específico]"

      → Resultado: [métrica específica]
      → Tempo: [quanto demorou]

      ---

      **[Cliente 2]**
      "[Depoimento detalhado]"

      → Resultado: [métrica]
      → Tempo: [duração]

      ---

      **[Cliente 3]**
      "[Depoimento detalhado]"

      → Resultado: [métrica]
      → Tempo: [duração]

      ---

      [X] pessoas já passaram por [Produto].
      [Y]% conseguiram [resultado específico].

      Você pode ser o próximo.

      → [Link]

      [Assinatura]

      P.S. Carrinho fecha em [X] dias.

  day_4_objections:
    timing: "10h"
    purpose: "Remover barreiras de compra"
    subject: "Suas perguntas respondidas"

    template: |
      Assunto: Suas perguntas respondidas (FAQ)

      [Nome],

      Desde que abri [Produto], recebi muitas perguntas.

      Aqui estão as mais comuns (e minhas respostas honestas):

      ---

      **"E se eu não tiver tempo?"**
      [Resposta que remove essa objeção - tempo necessário,
      flexibilidade, etc.]

      ---

      **"Isso funciona para [minha situação específica]?"**
      [Resposta com exemplos de diferentes situações]

      ---

      **"Quanto tempo até ver resultados?"**
      [Resposta realista com exemplos]

      ---

      **"E se eu não gostar?"**
      Você tem [X] dias de garantia incondicional.
      Se não funcionar para você, devolvo 100% do seu
      investimento. Sem perguntas.

      ---

      **"Posso parcelar?"**
      [Opções de pagamento disponíveis]

      ---

      Alguma outra dúvida? Responde esse email.
      Eu leio e respondo pessoalmente.

      → [Link]

      [Assinatura]

  day_5_bonus_expiring:
    email_count: 2
    purpose: "Criar primeira onda de urgência"

    email_1_morning:
      timing: "10h"
      subject: "[Bônus] expira à meia-noite"

      template: |
        Assunto: [Bônus] expira à meia-noite

        [Nome],

        Lembrete importante:

        O bônus [Nome do Bônus] — que vale R$[valor] —
        sai da oferta hoje à meia-noite.

        Se você quer [benefício do bônus], precisa agir HOJE.

        A partir de amanhã, [Produto] ainda estará disponível,
        mas SEM esse bônus.

        → [Link] Garantir acesso + bônus

        [Assinatura]

        P.S. Já são [X] pessoas dentro. [Reforço de prova social]

    email_2_evening:
      timing: "20h"
      subject: "4 horas para [Bônus]"

      template: |
        Assunto: 4 horas para [Bônus]

        [Nome],

        Só um lembrete rápido:

        Em 4 horas, [Bônus] sai da oferta.

        Se você quer [benefício do bônus], é agora.

        → [Link]

        [Assinatura]
```

---

### Step 5: Cart Close Sequence

```yaml
cart_close_emails:

  day_6_warning:
    email_count: 2
    purpose: "Escalar urgência, preparar para fechamento"

    email_1_morning:
      timing: "9h"
      subject: "24 horas restantes"

      template: |
        Assunto: 24 horas restantes

        [Nome],

        Aviso: [Produto] fecha amanhã.

        Às [hora] de amanhã, o carrinho fecha.

        Não vou reabrir até [próxima data/TBD].

        Se você quer:
        ✓ [Benefício 1]
        ✓ [Benefício 2]
        ✓ [Benefício 3]

        Essa é sua janela.

        → [Link]

        [Assinatura]

        P.S. Mais de [X] pessoas já estão dentro. Junte-se a eles.

    email_2_evening:
      timing: "18h"
      subject: "Minha história (e por que isso importa)"

      template: |
        Assunto: Minha história (e por que isso importa)

        [Nome],

        Antes de [Produto] fechar amanhã, quero compartilhar
        algo pessoal com você.

        [História pessoal - 3-5 parágrafos sobre sua jornada,
        lutas, descobertas, e por que criou o produto]

        É por isso que criei [Produto].

        Não para ser mais uma coisa na internet.

        Mas para dar a pessoas como você o que eu gostaria
        de ter tido quando [estava na mesma situação].

        Se você se vê nessa história... se você quer [resultado]
        como eu consegui... [Produto] é para você.

        → [Link]

        Amanhã é o último dia.

        [Assinatura]

  day_7_final:
    email_count: 4
    purpose: "Máxima conversão nas últimas 24 horas"
    note: "~50% das vendas acontecem neste dia"

    email_1_morning:
      timing: "9h"
      subject: "Última chance para [Produto]"

      template: |
        Assunto: Última chance para [Produto]

        [Nome],

        Esse é o último dia.

        Hoje, às [hora], [Produto] fecha.

        Isso é o que você recebe:

        ✓ [Componente 1] - [benefício]
        ✓ [Componente 2] - [benefício]
        ✓ [Componente 3] - [benefício]
        ✓ [Bônus restante] - [benefício]

        Total de valor: R$[soma dos valores]
        Seu investimento hoje: R$[preço]

        Você economiza R$[diferença].

        E tem garantia de [X] dias. Zero risco.

        → [Link]

        Depois de [hora], essa página sai do ar.

        [Assinatura]

    email_2_afternoon:
      timing: "14h"
      subject: "[X] horas restantes"

      template: |
        Assunto: [X] horas restantes

        [Nome],

        [Produto] fecha em [X] horas.

        Se você estava esperando, esse é o momento.

        "[Depoimento curto e poderoso]" - [Nome]

        Você pode ter o mesmo resultado.

        → [Link]

        [Assinatura]

    email_3_evening:
      timing: "18h"
      subject: "Antes de você decidir..."

      template: |
        Assunto: Antes de você decidir...

        [Nome],

        Se você está na dúvida sobre [Produto], me permita
        ser direto com você:

        Eu não sei se [Produto] é certo para você.
        Só você sabe.

        Mas sei que se você está cansado(a) de [dor]...
        Se você está pronto(a) para [resultado]...
        Se você quer [transformação]...

        ...então essa decisão pode ser uma das melhores
        que você já tomou.

        E com [X] dias de garantia, você não arrisca nada.

        O que você arrisca é não tentar.

        → [Link]

        Fecha às [hora].

        [Assinatura]

    email_4_final:
      timing: "90 minutos antes do fechamento"
      subject: "AVISO FINAL: Fecha em 90 minutos"

      template: |
        Assunto: AVISO FINAL: Fecha em 90 minutos

        [Nome],

        90 minutos.

        É o tempo que resta para [Produto].

        Se você quer [resultado], é agora ou [próxima oportunidade].

        → [Link]

        Depois de [hora], essa página desaparece.

        [Assinatura]
```

---

### Step 6: Post-Launch Sequences

```yaml
post_launch_emails:

  buyers_welcome:
    email_1_welcome:
      timing: "Imediatamente após compra"
      subject: "Você está dentro! Comece aqui"

      template: |
        Assunto: Você está dentro! Comece aqui

        [Nome],

        Parabéns! Você tomou uma decisão incrível.

        Bem-vindo(a) ao [Produto]!

        **Aqui está como começar:**

        1. **Acesse a área de membros:**
           [Link] | Login: [email] | Senha: [enviada por email]

        2. **Comece pelo [módulo/recurso 1]:**
           É o melhor ponto de partida para [resultado rápido].

        3. **Entre na comunidade:**
           [Link] - Se apresente e conheça outros membros.

        **Seu Quick Win:**
        [Ação específica de 5-10 min que gera resultado]

        Qualquer dúvida, responda esse email.

        Estamos juntos nessa jornada!

        [Assinatura]

    email_2_quick_win:
      timing: "Dia +2"
      subject: "Faça isso primeiro (5 minutos)"

      template: |
        Assunto: Faça isso primeiro (5 minutos)

        [Nome],

        Como está indo com [Produto]?

        Se você ainda não começou, aqui está seu quick win:

        → [Ação específica que leva 5 min e gera resultado]

        Isso vai te dar [benefício imediato].

        Depois, me conta como foi!

        [Assinatura]

    email_3_community:
      timing: "Dia +3"
      subject: "Conheça seus colegas"

      template: |
        Assunto: Conheça seus colegas de jornada

        [Nome],

        Você não está sozinho(a) nessa.

        Já entraram [X] pessoas em [Produto] neste lançamento.

        Junte-se à comunidade e se apresente:
        → [Link da comunidade]

        Formato sugerido:
        - Nome
        - De onde você é
        - Qual sua meta #1 com [Produto]

        Nos vemos lá!

        [Assinatura]

  non_buyers_nurture:
    email_1_no_hard_feelings:
      timing: "Dia +1"
      subject: "Sem ressentimentos"

      template: |
        Assunto: Sem ressentimentos

        [Nome],

        O carrinho de [Produto] fechou ontem.

        E eu notei que você não entrou — o que é totalmente ok.

        Eu entendo que nem sempre é o momento certo.

        Mas fiquei curioso: o que te impediu?

        Pode ser qualquer coisa:
        - Timing ruim
        - Preço não cabia
        - Dúvidas não respondidas
        - Ou simplesmente não era para você

        Responde esse email com uma linha só.
        Eu leio cada resposta.

        E quem sabe na próxima vez seja o momento certo.

        [Assinatura]

    email_2_survey:
      timing: "Dia +3"
      subject: "Pergunta rápida (2 min)"

      template: |
        Assunto: Pergunta rápida (2 min)

        [Nome],

        Você me ajudaria com uma pesquisa rápida?

        Quero melhorar [Produto] para a próxima turma.

        [Link da pesquisa]

        Leva menos de 2 minutos.

        Obrigado pelo feedback!

        [Assinatura]

    email_3_future_value:
      timing: "Dia +7"
      subject: "Algo gratuito para você"

      template: |
        Assunto: Algo gratuito para você

        [Nome],

        Mesmo que você não tenha entrado em [Produto] desta vez,
        ainda quero te ajudar com [área/objetivo].

        Preparei [recurso gratuito] que vai te ajudar com [benefício].

        → [Link]

        É meu presente por você ter acompanhado o lançamento.

        Espero que ajude!

        [Assinatura]
```

---

### Step 7: Subject Line Templates

```yaml
subject_line_bank:

  anticipation_pre_launch:
    formulas:
      - "Algo está chegando..."
      - "Tenho trabalhado em algo especial"
      - "Marque no calendário: [data]"
      - "Você vai querer saber disso"
      - "[Data]: Prepare-se"

  education_prelaunch:
    formulas:
      - "O erro de [tópico] que custa [dor]"
      - "Por que [abordagem comum] não funciona"
      - "[X] [avatares] descobriram isso sobre [tópico]"
      - "A verdade sobre [tópico]"
      - "Assista: [benefício específico]"

  launch_cart_open:
    formulas:
      - "[Produto] está aberto"
      - "É hoje"
      - "Finalmente: [promessa]"
      - "Você pediu, eu criei"
      - "As portas abriram"

  proof_mid_launch:
    formulas:
      - "[Nome] conseguiu [resultado] em [tempo]"
      - "O que [X] clientes dizem sobre [Produto]"
      - '"[Citação de depoimento]"'
      - "De [estado A] para [estado B]"
      - "[X]% conseguiram [resultado]"

  urgency_cart_close:
    formulas:
      - "[X] horas restantes"
      - "Fechando hoje às [hora]"
      - "Última chance"
      - "[Bônus] expira em [tempo]"
      - "Só até [horário]"

  final_close:
    formulas:
      - "AVISO FINAL"
      - "Fechando em [X] minutos"
      - "Última mensagem sobre [Produto]"
      - "Tchau."
      - "Acabou (quase)"
```

---

### Step 8: Advanced Tactics

```yaml
advanced_tactics:

  urgency_stack:
    description: "Camadas múltiplas de urgência"
    implementation:
      layer_1:
        name: "Fast Action Bonus"
        deadline: "48h após abertura"
        message: "Primeiras [X] pessoas ganham [bônus]"
      layer_2:
        name: "Bonus Expiration"
        deadline: "Dia 5"
        message: "[Bônus X] sai da oferta"
      layer_3:
        name: "Price Increase"
        deadline: "Dia 6 (opcional)"
        message: "Preço sobe para R$[X] amanhã"
      layer_4:
        name: "Cart Close"
        deadline: "Dia 7"
        message: "Carrinho fecha às [hora]"

  real_time_social_proof:
    description: "Atualizar emails com dados em tempo real"
    examples:
      - "[X] pessoas entraram hoje"
      - "Enquanto você lê, [Y] compraram"
      - "Acabamos de dar boas-vindas a [Nome] de [Local]"
      - "[X]% das vagas preenchidas"

  short_email_principle:
    description: "Últimos 2-3 emails máximo 5-7 linhas"
    rationale:
      - Corta através do ruído
      - Transmite urgência pela brevidade
      - Força decisão imediata
      - Zero distrações

  honest_close:
    description: "Se disse que fecha, FECHA"
    principles:
      - Não reabra no dia seguinte
      - Sem "estendemos por demanda"
      - Credibilidade > receita de curto prazo
      - Treina audiência a acreditar em deadlines

  timer_objections:
    description: "Framework T.I.M.E.R. para FAQ"
    objections:
      T_time: "Não tenho tempo para isso"
      I_identity: "Isso não é para pessoas como eu"
      M_money: "Não posso pagar agora"
      E_energy: "Parece muito trabalho"
      R_reputation: "O que os outros vão pensar?"
```

---

### Step 9: Quality Checklist

```yaml
quality_checklist:

  pre_launch:
    - [ ] Emails de antecipação geram curiosidade (sem revelar tudo)?
    - [ ] Cada PLC tem função distinta (Oportunidade/Transformação/Ownership)?
    - [ ] PSP structure está presente nos conteúdos?
    - [ ] Cliffhangers criam antecipação para próximo conteúdo?

  cart_open:
    - [ ] Email de abertura tem todos os elementos essenciais?
    - [ ] Fast Action Bonus tem deadline real?
    - [ ] Prova social é específica (nomes, resultados, tempos)?
    - [ ] FAQ aborda objeções T.I.M.E.R.?

  cart_close:
    - [ ] Urgência aumenta gradualmente?
    - [ ] Múltiplos emails no último dia?
    - [ ] Emails finais são curtos (5-7 linhas)?
    - [ ] Deadline é real e será cumprido?

  subject_lines:
    - [ ] Passam no teste de 3 segundos?
    - [ ] Criam curiosidade OU urgência?
    - [ ] Não são clickbait/spam?
    - [ ] Variações testáveis?

  emails_individuais:
    - [ ] Cada email tem UMA função clara?
    - [ ] CTA único e óbvio?
    - [ ] Scannable (fácil leitura rápida)?
    - [ ] Benefício claro para o leitor?

  sequência_geral:
    - [ ] Não há repetição desnecessária?
    - [ ] Momentum construído corretamente?
    - [ ] Post-launch para buyers E non-buyers?
    - [ ] Timeline realista para tamanho da lista?
```

---

## Complete Email Templates by Phase

### Template Bank: Pre-Prelaunch (3 emails)

[Inclusos na Step 2 acima]

### Template Bank: Prelaunch (7 emails)

[Inclusos na Step 3 acima]

### Template Bank: Cart Open (7-8 emails)

[Inclusos na Step 4 acima]

### Template Bank: Cart Close (6 emails)

[Inclusos na Step 5 acima]

### Template Bank: Post-Launch (6 emails)

[Inclusos na Step 6 acima]

---

## Metrics & Benchmarks

```yaml
launch_metrics:

  email_performance:
    open_rate:
      prelaunch: "30-50%"
      cart_open: "40-60%"
      cart_close: "50-70%"
    click_rate:
      prelaunch: "8-15%"
      cart_open: "15-25%"
      cart_close: "20-35%"

  conversion_metrics:
    plc_watch_rate: "40-60% da lista"
    sales_page_visits: "30-50% da lista"
    enrollment_rate: "2-10% da lista"

  revenue_distribution:
    day_1: "20-30%"
    days_2_5: "20-30%"
    final_day: "40-60%"

  price_point_benchmarks:
    under_100:
      conversion: "5-10%"
      distribution: "30/20/50"
    100_to_500:
      conversion: "3-7%"
      distribution: "25/25/50"
    500_to_2000:
      conversion: "1-4%"
      distribution: "20/30/50"
    above_2000:
      conversion: "0.5-2%"
      distribution: "15/35/50"
```

---

## Copywriter Recommendations

| Contexto | Copywriter | Por quê |
|----------|------------|---------|
| PLF clássico, autêntico | Frank Kern | Mass Control, casual conversational |
| Urgência máxima | Dan Kennedy | Deadline-driven, escassez agressiva |
| High-ticket, lógica | Alex Hormozi | Value stacking, ROI-focused |
| Story-based, emocional | Gary Halbert | Cartas que vendem pela emoção |
| Prova social, credibilidade | Gary Bencivenga | Fascinations, prova científica |
| Email conciso, direto | Ben Settle | Daily emails, personaity-driven |
| Autoridade, sofisticação | David Ogilvy | Brand-building, long-form |

---

## Output

```yaml
deliverables:
  - launch_timeline: "Calendário completo com todas as datas"
  - pre_prelaunch_sequence: "3 emails de antecipação"
  - prelaunch_sequence: "7 emails de PLC"
  - cart_open_sequence: "7-8 emails de abertura"
  - cart_close_sequence: "6 emails de fechamento"
  - post_launch_sequence: "6 emails (buyers + non-buyers)"
  - subject_line_variations: "3 opções por email"
  - urgency_calendar: "Stack de urgência visual"
  - quality_checklist: "Checklist preenchido"

total_emails: "25-30 emails completos"
format: markdown
```

---

*Task Version: 2.0*
*Methodology: Product Launch Formula (Jeff Walker) + Urgency Psychology + Email Conversion*
*Based on: Jeff Walker PLF, Product Launch Strategy, Systeme.io, Viral Loops Research*
*Lines: 1350+*
