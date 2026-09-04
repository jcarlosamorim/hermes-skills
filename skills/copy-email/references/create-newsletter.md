# Create Newsletter Task

## Purpose
Criar newsletters de alto engajamento que entregam valor consistente, constroem relacionamento com a audiência e geram vendas de forma natural.

## When to Use
- Newsletter semanal/quinzenal/mensal
- Email de conteúdo regular
- Nurture sequence
- Relacionamento com base de leads/clientes
- Email marketing de longo prazo

## Inputs

```yaml
required:
  - newsletter_name: Nome da newsletter
  - main_topic: Tema principal desta edição
  - target_avatar: Quem é o leitor ideal
  - frequency: Frequência de envio

optional:
  - value_hook: O que o leitor vai aprender/ganhar
  - personal_story: História pessoal para incluir
  - cta_goal: Objetivo de conversão (se houver)
  - tone: Tom da marca (casual, expert, provocador)
  - copywriter_preference: Copywriter específico desejado
```

## Workflow

### Step 1: Newsletter Strategy Selection
```
Escolher formato de newsletter:

1. CURADORIA
   - Links e recursos selecionados
   - Opiniões sobre cada item
   - Formato: lista com comentários
   Ex: "5 links da semana"

2. ENSAIO PESSOAL
   - Uma ideia desenvolvida
   - Storytelling + insight
   - Formato: texto corrido
   Ex: "Reflexão da semana"

3. TUTORIAL/HOW-TO
   - Ensina algo prático
   - Passo a passo
   - Formato: educacional
   Ex: "Como fazer X em Y passos"

4. STORY + LESSON
   - História (sua ou de outros)
   - Lição extraída
   - Formato: narrativo
   Ex: "O que aprendi quando..."

5. Q&A / PERGUNTAS
   - Responde perguntas da audiência
   - Formato: interativo
   Ex: "Você perguntou, eu respondo"

6. HÍBRIDO
   - Combina 2+ formatos
   - Seções fixas + variáveis
   Ex: "Intro pessoal + Curadoria + CTA"
```

### Step 2: Newsletter Structure Template
```
Estrutura padrão:

┌─────────────────────────────────────┐
│ SUBJECT LINE                        │
│ (Curiosidade + valor)               │
├─────────────────────────────────────┤
│ PREVIEW TEXT                        │
│ (Complementa subject)               │
├─────────────────────────────────────┤
│ ABERTURA (2-3 linhas)               │
│ Hook + contexto                     │
├─────────────────────────────────────┤
│ CORPO PRINCIPAL                     │
│ Conteúdo de valor                   │
│ (300-800 palavras)                  │
├─────────────────────────────────────┤
│ TAKEAWAY                            │
│ Resumo/aplicação prática            │
├─────────────────────────────────────┤
│ CTA (opcional)                      │
│ Produto/ação relacionada            │
├─────────────────────────────────────┤
│ ASSINATURA                          │
│ Pessoal, humanizada                 │
└─────────────────────────────────────┘
```

### Step 3: Opening Hooks (Laura Belgray Style)
```
Fórmulas de abertura que prendem:

STORY HOOK
"Na terça passada, às 3h da manhã, eu acordei com uma ideia."
"Meu pai sempre dizia uma coisa que eu achava boba. Até que..."

PROVOCAÇÃO
"Todo mundo está fazendo [X] errado. Inclusive eu, até semana passada."
"Se você acha que [crença comum], precisa ler isso."

CONFESSION
"Vou te contar algo que me dá vergonha admitir."
"Eu menti pra você. Não intencionalmente, mas..."

CURIOSITY GAP
"Existe um padrão entre as pessoas mais bem-sucedidas que conheço."
"A diferença entre [A] e [B] se resume a uma coisa."

CONTRARIAN
"Vou te dar o conselho que ninguém te dá: [conselho contrário]."
"Ignore [conselho popular]. Aqui está o porquê."

TIMELY/CURRENT
"Você viu o que aconteceu com [evento]? Isso me fez pensar em..."
"Está todo mundo falando de [trending]. Minha opinião impopular:"

QUESTION
"Você já parou pra pensar por que [fenômeno]?"
"Quantas vezes você já [ação comum] e não deu em nada?"
```

### Step 4: Subject Line Formulas
```
Fórmulas de subject para newsletter:

CURIOSITY
- "A coisa sobre [tema] que ninguém fala"
- "Isso mudou como eu penso sobre [área]"
- "O problema com [crença comum]"

BENEFIT
- "Como [resultado] em [tempo curto]"
- "[X] maneiras de [benefício]"
- "O segredo de [pessoas admiradas]"

PERSONAL
- "Uma confissão..."
- "Preciso te contar uma coisa"
- "O que aconteceu na terça"

NUMBERED
- "3 coisas que aprendi essa semana"
- "5 links para você"
- "[X] perguntas que recebi"

PROVOCATIVE
- "Você está fazendo [X] errado"
- "Pare de [ação comum]"
- "A mentira sobre [tema]"

EMOJI (use com moderação)
- "🔥 [Título]"
- "💡 [Insight]"
- Não exagere — teste o que funciona
```

### Step 5: Value Delivery Frameworks
```
Como entregar valor real:

1-3-1 FRAMEWORK (Ramit Sethi)
- 1 história/contexto
- 3 pontos de valor
- 1 call to action

AIDA PARA NEWSLETTER
- Attention: Hook de abertura
- Interest: Desenvolve o tema
- Desire: Mostra benefício
- Action: CTA suave

STORY → LESSON → APPLICATION
- Conta história
- Extrai lição
- Mostra como aplicar

PROBLEM → SOLUTION → PROOF
- Problema que avatar enfrenta
- Sua solução/insight
- Prova que funciona
```

### Step 6: CTA Integration (Soft Sell)
```
Como vender sem ser vendedor:

PS PROMOTION
Conteúdo de valor
[...]
P.S. Se você quer se aprofundar em [tema],
[Produto] pode te ajudar. [Link]

NATURAL BRIDGE
"Por falar em [tema], é exatamente isso que
ensinamos em [Produto]. Se faz sentido pra você: [link]"

VALUE FIRST, OFFER SECOND
70% do email = valor puro
30% (no final) = menção ao produto

SOFT CTA
"Se isso ressoou, você vai gostar de [Produto]."
(Não: "COMPRE AGORA!")

CONTENT UPGRADE
"Quer o checklist completo? [Link para lead magnet]"
```

### Step 7: Newsletter Templates

#### Template 1: Story + Lesson
```markdown
Assunto: O que [evento] me ensinou sobre [tema]

[Nome],

[Story hook - 2-3 linhas]

[Desenvolvimento da história - 4-5 parágrafos]

[Momento de virada/insight]

A lição?

**[Lição em 1-2 frases]**

Como você pode aplicar isso:

1. [Aplicação prática 1]
2. [Aplicação prática 2]
3. [Aplicação prática 3]

[Fechamento pessoal]

[Assinatura]

P.S. [CTA suave ou próxima newsletter]
```

#### Template 2: Curadoria
```markdown
Assunto: [X] coisas que salvei essa semana

[Nome],

[Abertura pessoal - 2-3 linhas]

Aqui está o que chamou minha atenção:

---

**1. [Título do item]**
[Link]

Por que importa: [2-3 linhas de opinião/contexto]

---

**2. [Título do item]**
[Link]

Por que importa: [2-3 linhas de opinião/contexto]

---

**3. [Título do item]**
[Link]

Por que importa: [2-3 linhas de opinião/contexto]

---

O que você achou? Responde esse email.

[Assinatura]
```

#### Template 3: Tutorial/How-To
```markdown
Assunto: Como [resultado] em [X] passos

[Nome],

[Por que isso importa - 2-3 linhas]

Vamos ao passo a passo:

**Passo 1: [Nome do passo]**

[Explicação + exemplo]

**Passo 2: [Nome do passo]**

[Explicação + exemplo]

**Passo 3: [Nome do passo]**

[Explicação + exemplo]

---

**Resumo rápido:**
1. [Passo 1 em uma linha]
2. [Passo 2 em uma linha]
3. [Passo 3 em uma linha]

Tenta e me conta como foi.

[Assinatura]

P.S. Quer mais [tema]? [CTA]
```

#### Template 4: Q&A
```markdown
Assunto: Você perguntou, eu respondo

[Nome],

Recebi muitas perguntas sobre [tema] essa semana.

Vou responder as principais:

---

**Pergunta de [Nome/Anônimo]:**
"[Pergunta]"

**Minha resposta:**
[Resposta detalhada]

---

**Pergunta de [Nome/Anônimo]:**
"[Pergunta]"

**Minha resposta:**
[Resposta detalhada]

---

Sua pergunta não apareceu? Manda aqui que respondo na próxima.

[Assinatura]
```

### Step 8: Quality Check
```
Verificar newsletter:

VALOR
- [ ] Leitor aprende algo útil?
- [ ] Poderia ser cobrado por esse conteúdo?
- [ ] É específico (não genérico)?

ENGAJAMENTO
- [ ] Abertura prende atenção?
- [ ] É fácil de ler (scannable)?
- [ ] Tem personalidade/voz?

RELACIONAMENTO
- [ ] Humaniza você/marca?
- [ ] Convida interação?
- [ ] Tom é consistente?

CTA
- [ ] Se vende, é natural?
- [ ] Não é agressivo/spammy?
- [ ] Faz sentido com conteúdo?
```

## Output

```yaml
format: markdown
sections:
  - newsletter_strategy
  - complete_newsletter
  - subject_line_variations (3)
  - opening_variations (2)
  - cta_options
  - quality_checklist
```

## Copywriter Recommendations

| Contexto | Copywriter Ideal | Por quê |
|----------|------------------|---------|
| Voz pessoal/casual | Laura Belgray | Talking Shrimp, personalidade |
| Value-first, soft sell | Ramit Sethi | Conteúdo premium + vendas naturais |
| Storytelling | Gary Halbert | Cartas pessoais |
| Provocador/contrarian | Dan Kennedy | Opiniões fortes |
| Elegante/sofisticado | David Ogilvy | Tom premium |

## Newsletter Cadence Guide

```yaml
frequency_options:
  daily:
    pros: "Alto engajamento, top of mind"
    cons: "Difícil manter qualidade, burnout"
    best_for: "Notícias, dicas rápidas"

  weekly:
    pros: "Equilibrado, sustentável"
    cons: "Pode perder momentum"
    best_for: "Maioria dos casos"

  biweekly:
    pros: "Mais tempo para qualidade"
    cons: "Menos contato"
    best_for: "Conteúdo denso, long-form"

  monthly:
    pros: "Alta qualidade possível"
    cons: "Esquecimento entre edições"
    best_for: "Curadoria extensiva"
```

---

*Task Version: 1.0*
*Primary Framework: Value-First Email (Laura Belgray/Ramit Sethi)*
