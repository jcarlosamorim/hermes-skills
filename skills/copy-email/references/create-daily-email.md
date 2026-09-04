# create-daily-email

Task para criar emails diários no estilo Ben Settle - infotainment marketing.

## Metadata

```yaml
task:
  name: Create Daily Email
  id: create-daily-email
  version: "2.0"
  category: email_marketing
  primary_agent: ben-settle
  supporting_agents:
    - dan-kennedy
    - andre-chaperon
  estimated_time: "15-30 minutes per email"
  output_format: markdown

dependencies:
  checklists:
    - email-infotainment-checklist.md
  templates:
    - daily-email-tmpl.yaml
```

---

## Overview

Este task guia a criação de emails diários no estilo Ben Settle - combinando entretenimento, informação e vendas em cada mensagem. O objetivo é construir relacionamento com a lista enquanto vende consistentemente.

## Philosophy

> "Daily emails build relationship faster than anything else."
> — Ben Settle

O email diário não é sobre bombardear sua lista. É sobre criar conteúdo que as pessoas QUEREM ler. Quando seus emails são esperados e apreciados, você pode vender todos os dias sem ser "salesy".

---

## PHASE 1: PREPARATION

### Step 1.1: Understand Your Context

Antes de escrever, responda:

```yaml
context_checklist:
  audience:
    - [ ] Quem está lendo? (avatar específico)
    - [ ] O que eles querem? (desejo principal)
    - [ ] O que os mantém acordados à noite? (medos)
    - [ ] Qual linguagem eles usam? (vocabulário)

  product:
    - [ ] O que você está vendendo hoje?
    - [ ] Qual o principal benefício?
    - [ ] Qual a chamada para ação?

  relationship:
    - [ ] É o primeiro email? (welcome sequence)
    - [ ] Quantos emails já receberam?
    - [ ] Qual foi o último email sobre?
```

### Step 1.2: Choose Your Story Source

Todo email começa com uma história. Fontes de histórias:

| Categoria | Exemplos | Quando Usar |
|-----------|----------|-------------|
| **Vida Pessoal** | Família, hobbies, viagens, observações | Mais relatable, usa diariamente |
| **Vida Profissional** | Clientes, resultados, erros, lições | Para autoridade e prova |
| **Pop Culture** | Filmes, séries, notícias, celebridades | Para relevância e timing |
| **História** | Figuras históricas, eventos, paralelos | Para profundidade e credibilidade |
| **Observação** | Coisas que você nota no dia a dia | Para originalidade |
| **Ficção Ilustrativa** | Histórias criadas para ilustrar ponto | Quando não tem história real |

### Step 1.3: Find the Connection

A história DEVE conectar ao que você vende. Se não conecta, é a história errada.

**Exercício de Conexão:**
```
HISTÓRIA: [sua história]
LIÇÃO: [o que ela ensina]
CONEXÃO: [como isso se relaciona com seu produto]
BRIDGE: [frase de transição]
```

**Exemplo:**
```
HISTÓRIA: Meu cachorro destruiu meu sofá ontem
LIÇÃO: Comportamento não treinado gera destruição
CONEXÃO: Marketing não sistematizado também destrói negócios
BRIDGE: "E é exatamente por isso que criei o [Produto]..."
```

---

## PHASE 2: WRITING THE EMAIL

### Step 2.1: The Hook (Primeiras 1-2 linhas)

O hook tem um único objetivo: fazer o leitor continuar lendo.

**Tipos de Hook:**

#### 1. Mid-Action Hook
Comece no meio da ação, sem setup:
```
❌ "Deixa eu te contar uma história. Ontem eu estava no mercado..."
✅ "O segurança veio na minha direção e eu sabia que tinha problema..."
```

#### 2. Curiosity Hook
Crie uma pergunta que precisa de resposta:
```
❌ "Quero compartilhar algo importante com você..."
✅ "O email que quase destruiu meu negócio..."
```

#### 3. Controversy Hook
Desafie uma crença comum:
```
❌ "Muitos especialistas dizem que..."
✅ "O pior conselho de marketing que já ouvi..."
```

#### 4. Personal Hook
Algo íntimo ou vulnerável:
```
❌ "Tive uma experiência interessante..."
✅ "Minha esposa acha que eu sou louco..."
```

**Teste do Hook:**
- [ ] Cria curiosidade?
- [ ] É específico (não genérico)?
- [ ] Faz o leitor querer saber mais?
- [ ] Está em 1-2 linhas?

### Step 2.2: The Story/Content (Corpo do email)

Desenvolva a história com detalhes específicos.

**Elementos de uma boa história:**
- **Personagens**: Pessoas reais com nomes (quando apropriado)
- **Diálogo**: Citações diretas tornam mais vívido
- **Detalhes sensoriais**: O que você viu, ouviu, sentiu
- **Tensão**: Um problema, conflito ou desafio
- **Resolução**: Como terminou (ou não terminou)

**Estrutura sugerida:**
```
[Hook - 1-2 linhas]

[Contexto - 2-3 linhas]
Onde você estava, quando, com quem.

[Desenvolvimento - 3-5 parágrafos curtos]
O que aconteceu. Use parágrafos de 1-3 frases.
Inclua diálogo quando possível.
Mantenha a tensão.

[Lição/Insight - 1-2 parágrafos]
O que isso significa.
A conexão com seu assunto.
```

**Formatação:**
- Parágrafos curtos (1-3 frases)
- Linhas em branco entre parágrafos
- Sem blocos de texto densos
- Ocasionalmente uma linha só

### Step 2.3: The Bridge (Transição para venda)

A transição deve ser natural, não forçada.

**Frases de transição efetivas:**
```
"O que me leva ao ponto de hoje..."
"E é exatamente isso que [Produto] faz..."
"Essa é a razão pela qual criei..."
"Se você quer [resultado da história]..."
"Falando nisso..."
"E é por isso que estou escrevendo..."
```

**Má transição:**
```
"Mas chega de história. Vou falar do produto agora."
"Mudando de assunto..."
"Agora a parte comercial..."
```

### Step 2.4: The Pitch (Vendendo sem ser "salesy")

Seja direto. Não peça desculpas por vender.

**Elementos do pitch:**
1. **O que é**: Nome e descrição em uma frase
2. **Por que agora**: Conexão com a história
3. **Benefício principal**: O que eles ganham
4. **Call to Action**: Exatamente o que fazer

**Exemplo de pitch:**
```
É por isso que criei o [Nome do Produto].

Ele te ensina exatamente como [benefício principal]
sem precisar [dor que ele resolve].

Clica aqui pra ver: [link]
```

**Palavras a EVITAR no pitch:**
- "Se você tiver interesse..."
- "Sem pressão..."
- "Fique à vontade para..."
- "Talvez você queira..."

**Palavras a USAR:**
- "Clica aqui"
- "Pega o teu"
- "Começa agora"
- "Não perde"

### Step 2.5: The Sign-Off (Assinatura)

Sua assinatura deve ter personalidade.

**Exemplos de sign-offs:**
```
Seu [adjetivo engraçado ou controverso] amigo,
[Nome]

Abraço e boas vendas,
[Nome]

Até amanhã,
[Nome]

Fui,
[Nome]

P.S. [Algo relevante - urgência, bônus, ou piada]
```

---

## PHASE 3: THE P.S. STRATEGY

O P.S. é a segunda parte mais lida do email (depois do assunto).

### Tipos de P.S.

#### 1. P.S. de Reforço
Repete a oferta ou deadline:
```
P.S. Lembrando que o preço sobe à meia-noite.
Depois disso, vai de R$297 para R$497.
```

#### 2. P.S. de Prova Social
Adiciona credibilidade:
```
P.S. "Esse email me fez ganhar R$12.000 em uma semana"
— João, aluno do [Produto]
```

#### 3. P.S. de Bônus
Oferece algo extra:
```
P.S. Se você entrar hoje, ainda ganha [Bônus]
que não vou oferecer depois.
```

#### 4. P.S. Pessoal
Algo não relacionado à venda:
```
P.S. Terminei de assistir Breaking Bad ontem.
Entendo agora o hype. Top 3 séries da minha vida.
```

#### 5. P.S. de Curiosidade
Cria expectativa para amanhã:
```
P.S. Amanhã vou contar a história do email que me rendeu
R$87.000 em 24 horas. Não perde.
```

---

## PHASE 4: SUBJECT LINE

### Princípio Central

O assunto tem UM objetivo: fazer o email ser aberto.

Não precisa explicar o email. Não precisa vender. Só abrir.

### Tipos de Assunto

#### 1. Curiosidade Pura
```
"O erro de R$50.000"
"O que achei no meu spam"
"Ele disse não"
"Estranho"
```

#### 2. Controvérsia
```
"Por que eu odeio templates"
"Sua lista é grande demais"
"O pior conselho que já ouvi"
```

#### 3. Teaser de História
```
"A vez que quase fui preso"
"Minha esposa acha que sou louco"
"O que aconteceu no café"
```

#### 4. Direto ao Ponto
```
"Pergunta rápida"
"Sobre seus emails"
"Importante"
```

#### 5. Pessoal/Casual
```
"re: nossa conversa"
"estava pensando em você"
"isso me lembrou de você"
```

### Regras de Assunto

1. **Curto** - Menos de 50 caracteres
2. **Minúsculas** - Muitas vezes performa melhor
3. **Sem clickbait** - Deve conectar ao conteúdo
4. **Sem emojis excessivos** - Um máximo, se usar
5. **Teste seu swipe file** - Compare com o que funciona

---

## PHASE 5: REVIEW & REFINEMENT

### Checklist de Qualidade

Antes de enviar, verifique:

```yaml
hook_check:
  - [ ] Captura atenção em 1-2 linhas?
  - [ ] É específico, não genérico?
  - [ ] Cria curiosidade?

story_check:
  - [ ] Tem personagens e detalhes?
  - [ ] Usa parágrafos curtos?
  - [ ] É entretido de ler?

lesson_check:
  - [ ] Há um insight ou aprendizado?
  - [ ] Conecta naturalmente ao produto?

pitch_check:
  - [ ] É direto sem pedir desculpas?
  - [ ] Tem call to action claro?
  - [ ] Evita linguagem fraca?

personality_check:
  - [ ] Soa como eu falando?
  - [ ] Tem minha personalidade (3x)?
  - [ ] É diferente de emails corporativos?

technical_check:
  - [ ] Assunto com menos de 50 chars?
  - [ ] Links funcionando?
  - [ ] Formatação correta no preview?
```

### O Teste do Amigo

Pergunte:
> "Se eu não estivesse vendendo nada, eu leria isso?"

Se não, reescreva até que a resposta seja sim.

### O Teste da Identidade

Pergunte:
> "Se removessem meu nome, saberiam que fui eu que escrevi?"

Se não, adicione mais personalidade.

---

## PHASE 6: EMAIL CALENDAR

### Estrutura Semanal Sugerida

| Dia | Tipo de Email | Foco |
|-----|---------------|------|
| Segunda | História pessoal | Conexão/Relacionamento |
| Terça | Lição/Técnica | Valor/Autoridade |
| Quarta | Controvérsia/Opinião | Polarização |
| Quinta | Case study/Resultado | Prova social |
| Sexta | Behind-the-scenes | Intimidade |
| Sábado | Curiosidade/Teaser | Engajamento |
| Domingo | Reflexão/Pessoal | Conexão profunda |

### Variação de Pitch

Não precisa variar o produto todo dia. Pode ser:
- Mesmo produto, ângulo diferente
- Lead magnet diferente
- Chamada para reply
- Teaser de produto futuro

---

## TEMPLATES

### Template 1: História Pessoal → Venda

```
[ASSUNTO: algo curioso da história]

[HOOK: Começa no meio da ação]

[HISTÓRIA: 3-5 parágrafos curtos com detalhes]

[LIÇÃO: 1-2 parágrafos - o que isso significa]

[BRIDGE: Transição natural]

[PITCH: O que é, por que, CTA]

[SIGN-OFF: Sua assinatura]

[P.S.: Reforço ou teaser]
```

### Template 2: Controvérsia → Venda

```
[ASSUNTO: declaração controversa]

[HOOK: Sua opinião forte]

[ARGUMENTO: Por que você pensa assim]

[PROVA: Exemplos ou dados]

[BRIDGE: Como isso conecta]

[PITCH: A solução]

[SIGN-OFF]

[P.S.]
```

### Template 3: Lição Rápida → Venda

```
[ASSUNTO: benefício direto]

[HOOK: O problema comum]

[SOLUÇÃO: A técnica/insight em 2-3 passos]

[EXEMPLO: Como usar na prática]

[BRIDGE: Para ir mais fundo]

[PITCH: Onde aprender mais]

[SIGN-OFF]
```

---

## COMMON MISTAKES TO AVOID

### Mistake 1: Pedir Desculpas por Vender
```
❌ "Desculpa pelo email comercial, mas..."
✅ "Vou direto ao ponto..."
```

### Mistake 2: Começar com Setup
```
❌ "Deixa eu te contar uma história sobre algo que aconteceu..."
✅ "O policial veio na minha direção..."
```

### Mistake 3: Parágrafos Longos
```
❌ [Bloco de 10 linhas]
✅ [2-3 linhas]

   [2-3 linhas]
```

### Mistake 4: Linguagem Corporativa
```
❌ "Prezado cliente, gostaríamos de informar..."
✅ "E aí, tudo bem?"
```

### Mistake 5: Não Ter Opinião
```
❌ "Alguns dizem X, outros dizem Y, ambos têm mérito..."
✅ "X é besteira. Aqui está o porquê..."
```

---

## ADVANCED TECHNIQUES

### Technique 1: Open Loops

Crie curiosidade para o próximo email:
```
"Amanhã vou contar o que aconteceu depois.
Spoiler: envolveu a polícia e um hamster."
```

### Technique 2: Running Jokes

Referências recorrentes que seus leitores entendem:
```
"Você sabe como eu sou sobre [tema recorrente]..."
```

### Technique 3: Reader Involvement

Peça respostas:
```
"Me responde esse email: qual é seu maior desafio com X?"
```

### Technique 4: Pattern Break

Ocasionalmente, quebre o padrão:
```
"Hoje não vou te vender nada.
Só queria dizer obrigado por ler meus emails."
```

### Technique 5: Callback

Referencie emails anteriores:
```
"Lembra do email da semana passada sobre [X]?
Tive uma atualização..."
```

---

## FINAL CHECKLIST

Antes de enviar seu email diário:

- [ ] Hook captura atenção imediatamente
- [ ] História é específica e interessante
- [ ] Lição conecta naturalmente ao produto
- [ ] Pitch é direto sem ser agressivo
- [ ] Personalidade está presente em cada linha
- [ ] Assunto é curto e cria curiosidade
- [ ] P.S. adiciona valor ou urgência
- [ ] Você leria esse email se recebesse

---

## OUTPUT FORMAT

Ao executar este task, entregue:

```yaml
email_output:
  subject_line: "[Assunto do email]"
  preview_text: "[Texto de preview - opcional]"

  body: |
    [Corpo completo do email formatado]

  p_s: "[Texto do P.S.]"

  metadata:
    story_source: "[pessoal/profissional/pop culture/etc]"
    pitch_type: "[produto/lead magnet/reply/etc]"
    infotainment_score: "[1-10]"
    personality_level: "[1-10]"

  notes:
    - "[Notas sobre o email]"
    - "[Variações sugeridas]"
```

---

*Task Version: 2.0*
*Primary Agent: Ben Settle*
*Lines: 600+*
