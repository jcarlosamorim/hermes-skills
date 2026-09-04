# create-soap-opera-sequence

Task para criar Soap Opera Sequences no estilo Andre Chaperon - sequências de emails story-driven que convertem cold traffic em compradores.

## Metadata

```yaml
task:
  name: Create Soap Opera Sequence
  id: create-soap-opera-sequence
  version: "2.0"
  category: email_marketing
  primary_agent: andre-chaperon
  supporting_agents:
    - ben-settle
    - dan-kennedy
  estimated_time: "2-4 hours for complete sequence"
  output_format: markdown

dependencies:
  checklists:
    - soap-opera-checklist.md
  templates:
    - soap-opera-tmpl.yaml
```

---

## Overview

Este task guia a criação de uma Soap Opera Sequence (SOS) completa - uma sequência de 5 emails que conta uma história envolvente enquanto constrói relacionamento e converte leitores em compradores.

## Philosophy

> "People don't read emails. They watch stories unfold."
> — Andre Chaperon

A Soap Opera Sequence trata emails como episódios de uma série. Cada email deixa o leitor querendo mais, criando uma jornada emocional que culmina naturalmente na venda.

---

## PHASE 1: FOUNDATION

### Step 1.1: Define Your Sequence Context

Antes de escrever, responda estas perguntas:

```yaml
sequence_context:
  audience:
    who: "[Descreva seu avatar - quem vai ler esses emails]"
    pain_points: "[Quais dores/problemas eles enfrentam]"
    desires: "[O que eles realmente querem]"
    current_beliefs: "[O que eles acreditam atualmente]"
    new_belief_needed: "[O que eles precisam acreditar para comprar]"

  product:
    what: "[O que você está vendendo]"
    main_benefit: "[Principal benefício/transformação]"
    price_point: "[Faixa de preço]"
    unique_mechanism: "[O que faz seu produto diferente]"

  entry_point:
    lead_magnet: "[O que eles baixaram/receberam para entrar na lista]"
    awareness_level: "[Schwartz: Unaware/Problem-aware/Solution-aware/Product-aware/Most-aware]"
    temperature: "[Cold/Warm/Hot]"
```

### Step 1.2: Map Your Story Arc

A SOS precisa de uma história com arco completo:

```
ESTRUTURA DO ARCO:

          3. EPIPHANY
              /\
             /  \
            /    \
   2. DRAMA       4. BENEFITS
          /            \
         /              \
        /                \
1. STAGE                  5. URGENCY
    |__________________________|
            JORNADA
```

**Mapeie sua história:**

| Email | Elemento | Sua Versão |
|-------|----------|------------|
| 1 | Setup - status quo | [Onde começa?] |
| 2 | Conflito - o problema | [Qual foi o problema/dor?] |
| 3 | Virada - a descoberta | [O que você descobriu?] |
| 4 | Resultado - a transformação | [O que mudou?] |
| 5 | Chamada - a oferta | [Qual é a solução?] |

### Step 1.3: Choose Your Story Type

Qual história você vai contar?

| Tipo | Descrição | Quando Usar |
|------|-----------|-------------|
| **Origin Story** | Sua jornada pessoal | Quando você é o expert |
| **Client Story** | Transformação de um cliente | Quando tem case forte |
| **Discovery Story** | Como você descobriu a solução | Quando o método é o herói |
| **Industry Story** | Revelação sobre o mercado | Quando expõe mitos |
| **Underdog Story** | Superação contra as odds | Quando audiência se identifica |

### Step 1.4: Plan Your Open Loops

Cada email (exceto o último) precisa de um open loop.

**Planeje seus loops:**

```yaml
open_loops:
  email_1_loop:
    opens: "[O que você vai deixar incompleto]"
    closes_in: "Email 2 ou 3"

  email_2_loop:
    opens: "[Nova curiosidade criada]"
    closes_in: "Email 3 ou 4"

  email_3_loop:
    opens: "[Promessa de revelação]"
    closes_in: "Email 4 ou 5"

  email_4_loop:
    opens: "[Teaser da oferta]"
    closes_in: "Email 5"

  main_story_loop:
    opens: "Email 1 (história começa)"
    closes_in: "Email 5 (resolução completa)"
```

---

## PHASE 2: WRITING EMAIL 1 - SET THE STAGE

### Purpose

Introduzir o personagem, estabelecer a situação inicial e criar curiosidade para o próximo email.

### Structure

```
[SUBJECT LINE: Curiosidade ou intrigue]

[HOOK: 1-2 linhas que capturam atenção]

[CONTEXT: Onde/quando esta história começa]

[CHARACTER INTRODUCTION: Quem é o protagonista]
- Detalhes que tornam relatable
- Situação inicial (status quo)
- Hint de que algo está para mudar

[TENSION BUILDING: Sinais de conflito chegando]
- Pequenos problemas se acumulando
- Dúvidas ou medos surgindo
- "Algo não estava certo..."

[OPEN LOOP: Cliffhanger para Email 2]
- Não revele o conflito completo
- Deixe curiosidade no ar
- Promise valor no próximo email

[SIGN-OFF]

[P.S.: Reforço do cliffhanger ou teaser]
```

### Email 1 Template

```markdown
Subject: [Algo intrigante sobre o início da história]

[Hook - começa com ação ou momento intrigante]

Três anos atrás, eu estava [situação específica].

[Detalhes do contexto - onde, quando, com quem]

Na superfície, tudo parecia [como parecia].

Mas por baixo, [sinal de problema se formando].

[2-3 parágrafos desenvolvendo a situação inicial]

[Momento que indica mudança chegando]
"Foi quando eu percebi que algo estava errado..."

O que aconteceu depois mudou tudo.

Mas antes de eu te contar, preciso explicar uma coisa
que você provavelmente nunca ouviu sobre [tema].

Amanhã eu vou te mostrar [teaser específico].

[Assinatura]

P.S. Se você já sentiu [dor do avatar], o email de amanhã
vai fazer muito sentido. Não perde.
```

### Email 1 Checklist

- [ ] Hook captura atenção em 1-2 linhas
- [ ] Personagem é apresentado de forma relatable
- [ ] Status quo está claro
- [ ] Há hints de conflito chegando
- [ ] Open loop criado para Email 2
- [ ] Cliffhanger é específico, não genérico
- [ ] Leitor quer saber o que aconteceu

---

## PHASE 3: WRITING EMAIL 2 - HIGH DRAMA

### Purpose

Intensificar o conflito, fazer o leitor SENTIR a dor e criar empatia através do sofrimento compartilhado.

### Structure

```
[SUBJECT LINE: Relacionado ao drama/conflito]

[BRIDGE: Conexão com Email 1]
"Ontem eu comecei a te contar sobre..."

[DIVE INTO CONFLICT: O problema se manifesta]
- O que deu errado
- Como afetou o protagonista
- As consequências

[EMOTIONAL DEPTH: Faça-os SENTIR]
- Detalhes sensoriais
- Diálogo interno
- Momentos de desespero

[STAKES: O que estava em risco]
- Perdas potenciais
- Medos realizados
- "Se eu não resolvesse isso..."

[FAILED ATTEMPTS: O que NÃO funcionou]
- Soluções convencionais tentadas
- Por que falharam
- Frustração crescente

[TURNING POINT TEASE: Luz no fim do túnel]
- Hint de que algo vai mudar
- Mas não revele ainda

[OPEN LOOP: Cliffhanger para Email 3]

[SIGN-OFF]
```

### Email 2 Template

```markdown
Subject: [Algo relacionado ao conflito/drama]

Ontem eu comecei a te contar sobre [recap rápido].

Hoje vai ficar mais intenso.

[Desenvolvimento do conflito]

Eu lembro de olhar para [detalhe específico] e pensar:
"Como eu cheguei aqui?"

[2-3 parágrafos de drama emocional]

As noites sem dormir.
[Consequência específica].
[Outra consequência].

Eu tentei [solução convencional 1].
Não funcionou.

Tentei [solução convencional 2].
Piorou.

[Momento de desespero máximo]

Estava pronto para desistir quando [hint de virada].

O que eu descobri naquele momento...
é algo que a maioria das pessoas nunca vai saber.

Amanhã eu vou te contar exatamente o que foi.

[Assinatura]

P.S. Se você já [experiência similar], você vai entender
por que o email de amanhã é tão importante.
```

### Email 2 Checklist

- [ ] Bridge conecta ao Email 1
- [ ] Conflito é intensificado (não resolvido)
- [ ] Leitor SENTE a dor (não apenas entende)
- [ ] Stakes são claros (o que está em risco)
- [ ] Tentativas falhas mostram que soluções comuns não funcionam
- [ ] Open loop criado para Email 3
- [ ] Há esperança de virada (mas não revelada)

---

## PHASE 4: WRITING EMAIL 3 - EPIPHANY

### Purpose

O momento de "aha!" - a descoberta que muda tudo. Este é o coração da sequência.

### Structure

```
[SUBJECT LINE: Relacionado à descoberta]

[BRIDGE: Recap rápido do drama]
"Eu estava no fundo do poço..."

[THE MOMENT: Descreva o momento exato da epifania]
- Onde você estava
- O que aconteceu
- A realização

[THE INSIGHT: O que você descobriu]
- Explicação clara do insight
- Por que isso muda tudo
- Como isso desafia o senso comum

[VALIDATION: Por que isso funciona]
- Princípio ou lógica por trás
- Por que ninguém mais ensina isso
- Conexão com problema da audiência

[TRANSFORMATION TEASE: O que mudou depois]
- Primeiros resultados
- Sensação de esperança
- "Mas eu ainda não sabia o melhor..."

[OPEN LOOP: Cliffhanger para Email 4]

[SIGN-OFF]
```

### Email 3 Template

```markdown
Subject: [Algo sobre a descoberta/virada]

Eu estava [situação do Email 2, resumida].

Pronto para desistir.

E então aconteceu.

[Descreva o momento da epifania]
- Onde você estava
- O que você viu/ouviu/percebeu
- O clique mental

Foi como se uma luz se acendesse.

[A realização em 2-3 frases claras]

"E se [insight principal]?"

[Desenvolvimento do insight]

Parece simples agora, mas pense nisso:
[Por que isso muda a perspectiva]

A maioria das pessoas [abordagem comum].
Mas eu descobri que [abordagem diferente].

[Primeiros resultados da aplicação]

Em [período], [resultado específico].

Mas isso era só o começo.

O que aconteceu depois foi ainda melhor -
e é algo que você provavelmente nunca considerou.

Amanhã eu vou te mostrar [teaser específico].

[Assinatura]

P.S. A epifania que tive vale ouro.
Mas a aplicação que vou mostrar amanhã?
Isso vale muito mais.
```

### Email 3 Checklist

- [ ] O momento da epifania é vívido e específico
- [ ] O insight é claro e compreensível
- [ ] Há explicação de POR QUE funciona
- [ ] Desafia a sabedoria convencional
- [ ] Mostra primeiros resultados (mas não todos)
- [ ] Open loop para Email 4
- [ ] Leitor quer aplicar o insight

---

## PHASE 5: WRITING EMAIL 4 - HIDDEN BENEFITS

### Purpose

Mostrar a transformação completa e benefícios inesperados que vieram com a aplicação do insight.

### Structure

```
[SUBJECT LINE: Relacionado a resultados/transformação]

[BRIDGE: Recap da epifania]
"Depois que eu descobri [insight]..."

[TRANSFORMATION: O que mudou]
- Resultados específicos (números, se possível)
- Mudanças no dia a dia
- Como a vida é diferente agora

[HIDDEN BENEFITS: O que você não esperava]
- Benefícios além do óbvio
- Efeitos colaterais positivos
- "O que eu não antecipei foi..."

[SOCIAL PROOF: Outros que aplicaram]
- Resultados de outras pessoas (se tiver)
- Validação do método
- "Não sou só eu..."

[OBJECTION HANDLING: Através da história]
- Endereça dúvidas naturalmente
- "Eu também pensei que..."
- "O que me surpreendeu foi..."

[PRODUCT TEASE: Começa a transição para oferta]
- Menciona que sistematizou o método
- Hint de que há uma forma de acelerar
- "Depois de tanto pedir..."

[OPEN LOOP: Cliffhanger para Email 5]

[SIGN-OFF]
```

### Email 4 Template

```markdown
Subject: [Resultado ou benefício inesperado]

Depois que eu descobri [insight do Email 3],
tudo começou a mudar.

[Primeiros resultados concretos]

Em [período], [resultado específico].
[Outro resultado].
[Mais um resultado].

Mas aqui está o que eu não esperava:

[HIDDEN BENEFIT 1]
Além de [benefício óbvio], eu também [benefício escondido].

[HIDDEN BENEFIT 2]
E mais: [outro benefício que não era o objetivo principal].

[SOCIAL PROOF - se disponível]
Quando compartilhei isso com [pessoa/grupo],
eles também [resultado similar].

[Nome] disse: "[Depoimento ou resultado]"

Eu sei o que você está pensando:
"[Objeção comum]"

Eu também pensei isso.
[Resposta através da própria experiência]

Depois que tantas pessoas pediram,
eu finalmente organizei tudo em [formato].

Amanhã eu vou te dar a chance de [benefício principal].

Mas há uma coisa que você precisa saber antes...

[Assinatura]

P.S. O email de amanhã é diferente dos outros.
É onde tudo faz sentido. Não perca.
```

### Email 4 Checklist

- [ ] Transformação é mostrada com especificidade
- [ ] Benefícios escondidos surpreendem positivamente
- [ ] Há prova social (se disponível)
- [ ] Objeções são tratadas através da história
- [ ] Transição para oferta começa naturalmente
- [ ] Open loop para Email 5
- [ ] Leitor quer o que você tem

---

## PHASE 6: WRITING EMAIL 5 - URGENCY

### Purpose

Fechar todos os loops, apresentar a oferta e dar razão para agir AGORA.

### Structure

```
[SUBJECT LINE: Relacionado à oportunidade/decisão]

[RECAP: Resumo da jornada]
"Nos últimos dias, eu te contei..."
- Email 1: Onde eu estava
- Email 2: O que deu errado
- Email 3: O que eu descobri
- Email 4: O que mudou

[CLOSE ALL LOOPS: Resolva tudo]
- Loops menores fechados
- História principal concluída
- Satisfação emocional

[THE OFFER: Apresente a solução]
- O que é
- O que está incluído
- Principal benefício

[VALUE STACK: O que eles ganham]
- Lista de componentes
- Valor de cada um (se apropriado)
- Bônus (se houver)

[RISK REVERSAL: Remova o medo]
- Garantia
- Por que não há risco

[URGENCY: Razão para agir agora]
- Deadline real
- Escassez real
- Consequência de esperar

[CTA: Chamada para ação clara]
- O que fazer
- Link direto
- Simplicidade

[SIGN-OFF]

[P.S.: Último reforço]
```

### Email 5 Template

```markdown
Subject: [Oportunidade/Decisão/Última chance]

Nos últimos 4 dias, eu te contei uma história.

Uma história sobre [recap em uma linha].

Você viu como eu fui de [ponto A] para [ponto B].

E mais importante: você entendeu [insight principal].

Agora é sua vez.

[TRANSIÇÃO PARA OFERTA]

Depois de [pessoas/tempo] pedindo,
eu finalmente criei [Nome do Produto].

É um [formato] que [principal benefício].

Aqui está o que você recebe:

✅ [Componente 1] - [benefício]
✅ [Componente 2] - [benefício]
✅ [Componente 3] - [benefício]
✅ BÔNUS: [Se houver] - [benefício]

[GARANTIA]
E você não arrisca nada.
Se não [resultado esperado] em [período],
você recebe 100% do dinheiro de volta.

[URGÊNCIA]
Mas preciso ser honesto:
[Razão genuína para urgência].

Depois de [deadline], [consequência].

[CTA]
Se você quer [transformação], clica aqui:
[LINK]

[Assinatura]

P.S. Lembra do [elemento da história]?
[Conexão com a oferta].
Clica aqui para começar: [LINK]

P.P.S. [Última urgência ou benefício]
```

### Email 5 Checklist

- [ ] Todos os loops estão fechados
- [ ] Recap conecta a jornada completa
- [ ] Oferta é apresentada como conclusão natural
- [ ] Value stack é claro
- [ ] Há garantia/reversão de risco
- [ ] Urgência é GENUÍNA
- [ ] CTA é claro e direto
- [ ] Leitor sabe exatamente o que fazer

---

## PHASE 7: SEQUENCE REVIEW

### Pre-Send Checklist

Antes de ativar a sequência:

```yaml
story_arc_check:
  - [ ] História tem início, meio e fim claros
  - [ ] Personagem é relatable
  - [ ] Conflito é real e doloroso
  - [ ] Epifania é clara e compreensível
  - [ ] Transformação é específica e crível

open_loop_check:
  - [ ] Cada email (1-4) tem cliffhanger
  - [ ] Todos os loops fecham no Email 5
  - [ ] Cliffhangers são específicos, não genéricos
  - [ ] Promessas são cumpridas

engagement_check:
  - [ ] Hooks capturam atenção
  - [ ] Parágrafos são curtos
  - [ ] Linguagem é conversacional
  - [ ] Leitor quer o próximo email

conversion_check:
  - [ ] Oferta conecta à história
  - [ ] Value stack é claro
  - [ ] Urgência é genuína
  - [ ] CTA é impossível de ignorar

technical_check:
  - [ ] Subject lines < 50 caracteres
  - [ ] Links funcionam
  - [ ] Timing entre emails está correto (24h recomendado)
  - [ ] Segmentação configurada
```

### Common Mistakes to Avoid

| Erro | Por que é problema | Como evitar |
|------|-------------------|-------------|
| Vender muito cedo | Quebra confiança | Espere até Email 5 |
| Loops não fechados | Frustração do leitor | Checklist de loops |
| História genérica | Não cria conexão | Use detalhes específicos |
| Drama artificial | Parece manipulação | Seja autêntico |
| Urgência falsa | Destrói credibilidade | Só use urgência real |

---

## PHASE 8: TIMING & DELIVERY

### Recommended Schedule

```
Day 0: Opt-in + Lead Magnet Delivery
Day 1: Email 1 - Set the Stage
Day 2: Email 2 - High Drama
Day 3: Email 3 - Epiphany
Day 4: Email 4 - Hidden Benefits
Day 5: Email 5 - Urgency
```

### Alternative Schedules

**Aggressive (para lançamentos):**
```
Day 0: Opt-in
Day 0 (PM): Email 1
Day 1: Email 2
Day 2: Email 3
Day 3: Email 4
Day 4: Email 5
```

**Extended (para high-ticket):**
```
Day 0: Opt-in + Lead Magnet
Day 2: Email 1
Day 4: Email 2
Day 6: Email 3
Day 8: Email 4
Day 10: Email 5
```

### Post-Sequence Options

Após Email 5:
1. **Compradores** → Sequence de onboarding/upsell
2. **Não-compradores** → Sequence de nutrição
3. **Engajados mas não compraram** → Re-engagement em 7-14 dias

---

## OUTPUT FORMAT

Ao entregar a sequência, use este formato:

```yaml
soap_opera_sequence:
  name: "[Nome da Sequência]"
  target_audience: "[Descrição do avatar]"
  product: "[O que está sendo vendido]"

  emails:
    email_1:
      subject: "[Subject line]"
      body: |
        [Corpo do email completo]
      open_loop: "[Descrição do loop aberto]"
      word_count: [número]

    email_2:
      subject: "[Subject line]"
      body: |
        [Corpo do email completo]
      open_loop: "[Descrição do loop aberto]"
      word_count: [número]

    email_3:
      subject: "[Subject line]"
      body: |
        [Corpo do email completo]
      open_loop: "[Descrição do loop aberto]"
      word_count: [número]

    email_4:
      subject: "[Subject line]"
      body: |
        [Corpo do email completo]
      open_loop: "[Descrição do loop aberto]"
      word_count: [número]

    email_5:
      subject: "[Subject line]"
      body: |
        [Corpo do email completo]
      loops_closed: "[Lista de loops fechados]"
      word_count: [número]

  metadata:
    total_words: [número]
    story_type: "[origin/client/discovery/etc]"
    timing: "[standard/aggressive/extended]"

  checklist_passed: true/false
```

---

*Task Version: 2.0*
*Primary Agent: Andre Chaperon*
*Lines: 600+*
