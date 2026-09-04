# simple-writing-audit

Task de auditoria de copy usando o Simple Writing System de John Carlton.

## TASK METADATA

```yaml
task:
  name: Simple Writing Audit
  id: simple-writing-audit
  category: copy_editing
  origin: John Carlton - Simple Writing System
  version: 1.0
  output:
    format: markdown
    filename: "audit-{{copy_name}}.md"
```

---

## OVERVIEW

Esta task aplica o Simple Writing System de John Carlton para auditar e melhorar qualquer peça de copy. O objetivo é transformar copy complexa, corporativa ou confusa em copy clara, conversacional e persuasiva.

**Filosofia Central:**
> "Nothing good will ever happen in your business until your sales message gets written. And the best sales messages are the ones anyone can understand."

---

## PHASE 1: INITIAL ASSESSMENT

### 1.1 Copy Intake

**Input Required:**
- [ ] Copy a ser auditada (texto completo)
- [ ] Contexto do produto/serviço
- [ ] Avatar/público-alvo
- [ ] Objetivo da copy (vendas, leads, etc.)

### 1.2 First Impression Test

Leia a copy UMA vez, rapidamente. Responda:

| Pergunta | Resposta |
|----------|----------|
| Você entendeu do que se trata em 10 segundos? | SIM / NÃO |
| Você sabe o que fazer depois de ler? | SIM / NÃO |
| Você SENTIU algo (emoção)? | SIM / NÃO |
| Você leria mais se visse isso numa timeline? | SIM / NÃO |

**Score:** ___/4

- 4/4 = Bom fundamento, refinar
- 2-3/4 = Precisa trabalho significativo
- 0-1/4 = Reescrever do zero

---

## PHASE 2: THE FIVE AUDIT PASSES

O Simple Writing System usa 5 passes de edição. Execute cada um separadamente.

### PASS 1: THE WORD ASSASSIN

**Objetivo:** Eliminar toda palavra que não contribui.

**Targets para Eliminação:**

| Categoria | Exemplos | Ação |
|-----------|----------|------|
| Advérbios fracos | muito, realmente, bastante, extremamente | CORTAR |
| Redundâncias | "Em ordem de" → "para" | SIMPLIFICAR |
| Expressões vazias | "O fato é que" → (remover) | CORTAR |
| Opiniões não solicitadas | "Eu acho", "Na minha opinião" | CORTAR ou AFIRMAR |
| "That" desnecessário | "Acredito que você pode" → "Acredito você pode" | CORTAR |

**Checklist Pass 1:**

```markdown
## WORD ASSASSIN AUDIT

### Palavras Cortadas:
| Original | Edição | Razão |
|----------|--------|-------|
| [palavra/frase] | [corte ou substituição] | [razão] |

### Estatísticas:
- Palavras antes: ___
- Palavras depois: ___
- Redução: ___%

### Exemplo de Transformação:
ANTES: "Eu realmente acredito que é muito importante para você entender que este sistema é extremamente eficaz."
DEPOIS: "Este sistema é eficaz."
```

**Regra de Ouro:** Se remover a palavra não muda o significado, CORTE.

---

### PASS 2: THE SENTENCE SPLITTER

**Objetivo:** Garantir UMA IDEIA por sentença.

**Sinais de Sentença para Dividir:**
- Contém "e" conectando duas ideias completas
- Contém "mas" no meio
- Você precisa respirar no meio quando lê em voz alta
- Tem mais de 20 palavras
- Tem mais de uma vírgula

**Técnica de Divisão:**

```markdown
## SENTENCE SPLITTER AUDIT

### Sentenças Divididas:

**Sentença #1:**
ANTES: "Nosso sistema revolucionário combina tecnologia de ponta com princípios testados pelo tempo para entregar resultados que vão transformar seu negócio enquanto economiza tempo e dinheiro."

DEPOIS:
"Nosso sistema é revolucionário.
Combina tecnologia de ponta com princípios testados.
Os resultados vão transformar seu negócio.
Você vai economizar tempo.
Você vai economizar dinheiro."

**Análise:**
- Ideias originais: 4 em 1 sentença
- Ideias após: 4 em 5 sentenças ✓

---

**Sentença #2:**
[repetir para cada sentença complexa]
```

**Regra de Ouro:** Se a sentença tem mais de uma ideia, DIVIDA.

---

### PASS 3: THE JARGON KILLER

**Objetivo:** Substituir toda palavra "corporativa" por linguagem simples.

**Dicionário de Substituição:**

| Jargão | Substituição |
|--------|--------------|
| utilizar | usar |
| implementar | fazer, aplicar |
| otimizar | melhorar |
| alavancar | usar |
| sinergia | trabalho em equipe |
| paradigma | forma de pensar |
| empoderar | dar poder, capacitar |
| deliverables | entregas |
| stakeholders | interessados, envolvidos |
| feedback | retorno, opinião |
| insights | percepções |
| acessar | usar, ver |
| viabilizar | permitir, possibilitar |
| estratégico | importante |
| robusto | forte, completo |
| inovador | novo |
| solução | produto, serviço |
| plataforma | sistema, ferramenta |
| escalável | que cresce |
| disruptivo | diferente, novo |
| holístico | completo |

**Checklist Pass 3:**

```markdown
## JARGON KILLER AUDIT

### Substituições Realizadas:
| Jargão Original | Substituição | Contexto |
|-----------------|--------------|----------|
| [palavra] | [substituição] | [frase onde aparece] |

### Estatísticas:
- Jargões encontrados: ___
- Jargões substituídos: ___
- Termos técnicos necessários mantidos: ___
```

**Regra de Ouro:** Se seu avô não entenderia a palavra, SUBSTITUA.

---

### PASS 4: THE CONVERSATIONAL PASS

**Objetivo:** Fazer a copy soar como conversa, não como documento.

**Técnicas de Conversacionalização:**

| Técnica | Exemplo ANTES | Exemplo DEPOIS |
|---------|---------------|----------------|
| Usar contrações | "Você não vai" | "Você não vai" ✓ |
| Fragmentos | "É importante." | "Importante." |
| Perguntas | "Considere que..." | "Já pensou que...?" |
| Você direto | "Os clientes podem..." | "Você pode..." |
| Início informal | "Portanto, é essencial..." | "Olha, isso é essencial..." |

**Testes de Conversação:**

```markdown
## CONVERSATIONAL AUDIT

### Teste do Bar
Para cada parágrafo, pergunte: "Eu diria isso para um amigo num bar?"

| Parágrafo | Passaria no Teste do Bar? | Edição Sugerida |
|-----------|---------------------------|-----------------|
| #1 | SIM / NÃO | [se não, como tornar mais conversacional] |
| #2 | SIM / NÃO | [edição] |

### Teste de Leitura em Voz Alta
Leia toda a copy em voz alta. Marque onde:
- [ ] Você tropeçou (reescrever)
- [ ] Você ficou sem ar (dividir)
- [ ] Soou estranho (tornar mais natural)

### Marcadores de Conversa Adicionados:
- "Olha..."
- "Veja bem..."
- "O negócio é o seguinte..."
- "Sabe o que mais?"
- "Deixa eu te contar..."
```

**Regra de Ouro:** Se você não diria assim numa conversa, REESCREVA.

---

### PASS 5: THE LIZARD BRAIN CHECK

**Objetivo:** Garantir que a copy atinge os instintos primais ANTES da lógica.

**Gatilhos do Cérebro Reptiliano:**

| Gatilho | Pergunta de Verificação | Presente? |
|---------|------------------------|-----------|
| **Sobrevivência/Medo** | Há uma ameaça clara ao bem-estar? | SIM / NÃO |
| **Ganância/Desejo** | Há uma promessa de ganho específico? | SIM / NÃO |
| **Luxúria/Atração** | Há apelo à atratividade/desejo? | SIM / NÃO |
| **Vaidade/Status** | Há promessa de elevação social? | SIM / NÃO |
| **Preguiça/Facilidade** | Há promessa de caminho fácil? | SIM / NÃO |
| **Curiosidade** | Há informação incompleta que gera necessidade de saber? | SIM / NÃO |

**Checklist Lizard Brain:**

```markdown
## LIZARD BRAIN AUDIT

### Análise de Gatilhos:

**Headline:**
- Gatilho primário usado: ___________
- Força do gatilho (1-10): ___
- Sugestão de amplificação: ___________

**Abertura (primeiras 3 frases):**
- Gatilho primário usado: ___________
- Conecta emocionalmente em até 3 segundos? SIM / NÃO
- Sugestão de amplificação: ___________

**Antes de apresentar lógica/benefícios:**
- O leitor já está SENTINDO algo? SIM / NÃO
- Se não, adicionar: ___________

### Sequência Emocional:
1. HOOK (emoção inicial): ___________
2. AGITAÇÃO (intensificar emoção): ___________
3. SOLUÇÃO (alívio): ___________
```

**Regra de Ouro:** Se não atinge o cérebro reptiliano nos primeiros 5 segundos, REESCREVA o início.

---

## PHASE 3: STRUCTURAL AUDIT

### 3.1 Headline Audit

**Critérios Carlton para Headlines:**

| Critério | Presente? | Se NÃO, Sugestão |
|----------|-----------|------------------|
| Para o leitor IMEDIATAMENTE? | SIM / NÃO | |
| Promessa específica? | SIM / NÃO | |
| Gera curiosidade irresistível? | SIM / NÃO | |
| Tem "one-legged golfer" (elemento inesperado)? | SIM / NÃO | |
| Seria ignorado se visto numa timeline? | SIM / NÃO | |

**Templates de Melhoria:**

```markdown
### HEADLINE AUDIT

**Headline Original:**
"[headline atual]"

**Análise:**
- Pontos fortes: ___
- Pontos fracos: ___
- Gatilho principal: ___

**3 Headlines Alternativas:**

1. Template "One-Legged Golfer":
"[elemento surpreendente] [benefício específico] [em quanto tempo]"
→ "_____________________________"

2. Template "How To":
"Como [resultado desejado] Sem [sacrifício esperado]"
→ "_____________________________"

3. Template "Discovery":
"Descoberta Incrível: [fonte inesperada] Revela [segredo para resultado]"
→ "_____________________________"

**Recomendação Final:**
[Qual headline usar e por quê]
```

---

### 3.2 Opening Audit

**Critérios Carlton para Aberturas:**

| Critério | Presente? | Se NÃO, Sugestão |
|----------|-----------|------------------|
| Hook nos primeiros 3 segundos? | SIM / NÃO | |
| Estabelece rapport/identificação? | SIM / NÃO | |
| O leitor sabe "o que tem pra mim"? | SIM / NÃO | |
| Usa história real (não ficção)? | SIM / NÃO | |
| Flui naturalmente para o corpo? | SIM / NÃO | |

**Análise de Abertura:**

```markdown
### OPENING AUDIT

**Abertura Original (primeiras 5 frases):**
"[copiar abertura]"

**Análise:**
- Tempo até o hook: ___ segundos/palavras
- Tipo de abertura: [história/problema/novidade/pergunta/declaração]
- Emoção gerada: ___
- Conexão com avatar: ___

**Abertura Reescrita:**
"[nova abertura seguindo princípios Carlton]"

**Justificativa da Mudança:**
[Por que a nova versão é melhor]
```

---

### 3.3 Body Audit

**Critérios para o Corpo:**

| Critério | Presente? | Se NÃO, Sugestão |
|----------|-----------|------------------|
| Benefícios > Features? | SIM / NÃO | |
| Cada benefício tem prova? | SIM / NÃO | |
| Histórias reais incluídas? | SIM / NÃO | |
| Objeções endereçadas? | SIM / NÃO | |
| Fluxo lógico e emocional? | SIM / NÃO | |

**Análise do Corpo:**

```markdown
### BODY AUDIT

**Estrutura Atual:**
1. [seção 1] - ___ palavras
2. [seção 2] - ___ palavras
3. [etc.]

**Análise por Seção:**

**Seção 1:** [nome/tema]
- Propósito claro? SIM / NÃO
- Uma ideia por parágrafo? SIM / NÃO
- Transição suave? SIM / NÃO
- Sugestão: ___

[repetir para cada seção]

**Elementos Faltando:**
- [ ] Mais histórias reais
- [ ] Mais especificidade
- [ ] Mais prova
- [ ] Melhor transições
- [ ] Outros: ___
```

---

### 3.4 Close Audit

**Critérios Carlton para Fechamento:**

| Critério | Presente? | Se NÃO, Sugestão |
|----------|-----------|------------------|
| CTA impossível de perder? | SIM / NÃO | |
| Razão para agir AGORA? | SIM / NÃO | |
| Risco removido (garantia)? | SIM / NÃO | |
| Recap de benefícios? | SIM / NÃO | |
| Instrução clara do próximo passo? | SIM / NÃO | |

**Análise do Close:**

```markdown
### CLOSE AUDIT

**Close Original:**
"[copiar fechamento]"

**Análise:**
- CTA presente? SIM / NÃO
- CTA claro? SIM / NÃO
- Urgência presente? SIM / NÃO
- Urgência justificada? SIM / NÃO
- Garantia mencionada? SIM / NÃO

**Close Reescrito:**
"[novo fechamento]"

**Elementos Adicionados:**
- [ ] Urgência específica
- [ ] Recap de benefícios
- [ ] Garantia clara
- [ ] Instrução passo-a-passo
```

---

## PHASE 4: THE HOOK MINING AUDIT

### 4.1 Identificação do Hook Atual

**Perguntas para encontrar o "One-Legged Golfer":**

| Pergunta | Resposta |
|----------|----------|
| Qual é a história de origem do produto? | |
| Há algum fato surpreendente ou contra-intuitivo? | |
| O que o expert menciona "de passagem" que é fascinante? | |
| Qual detalhe faria um estranho numa festa dizer "espera, o quê?"? | |
| O que os concorrentes NÃO estão falando? | |

### 4.2 Hook Mining Report

```markdown
## HOOK MINING REPORT

**Hook Atual Identificado:**
"[qual é o hook usado atualmente]"

**Força do Hook (1-10):** ___

**Hooks Alternativos Encontrados:**

**Hook #1:** [descrição]
- Tipo: [história/descoberta/contradição/especificidade]
- Força: ___/10
- Como usar: ___

**Hook #2:** [descrição]
- Tipo: [história/descoberta/contradição/especificidade]
- Força: ___/10
- Como usar: ___

**Hook #3:** [descrição]
- Tipo: [história/descoberta/contradição/especificidade]
- Força: ___/10
- Como usar: ___

**Recomendação:**
[Qual hook usar e por quê]

**Nova Headline com Hook Recomendado:**
"[headline usando o hook mais forte]"
```

---

## PHASE 5: COMPREHENSIVE SCORING

### 5.1 Scoring Matrix

| Critério | Peso | Score (1-10) | Score Ponderado |
|----------|------|--------------|-----------------|
| **Clareza** | 25% | ___ | ___ |
| **Conversacionalidade** | 20% | ___ | ___ |
| **Hook/Abertura** | 20% | ___ | ___ |
| **Lizard Brain Appeal** | 15% | ___ | ___ |
| **CTA/Fechamento** | 10% | ___ | ___ |
| **Prova/Credibilidade** | 10% | ___ | ___ |
| **TOTAL** | 100% | | ___ |

**Interpretação:**
- 90-100: Excelente - pronta para publicar
- 80-89: Boa - ajustes menores necessários
- 70-79: Aceitável - melhorias significativas recomendadas
- 60-69: Fraca - reescrever seções principais
- Abaixo de 60: Reescrever do zero

---

### 5.2 Carlton Simplicity Score

**Métricas de Simplicidade:**

| Métrica | Valor | Target | Status |
|---------|-------|--------|--------|
| Palavras por sentença (média) | ___ | ≤15 | ✓/✗ |
| Sentenças com mais de 1 ideia | ___ | 0 | ✓/✗ |
| Palavras de jargão | ___ | 0 | ✓/✗ |
| Contrações usadas | ___ | ≥5 | ✓/✗ |
| Perguntas diretas ao leitor | ___ | ≥3 | ✓/✗ |
| Histórias/exemplos | ___ | ≥2 | ✓/✗ |
| Nível de leitura (Flesch) | ___ | ≤8º ano | ✓/✗ |

**Carlton Simplicity Score:** ___/7 targets atingidos

---

## PHASE 6: FINAL DELIVERABLES

### 6.1 Executive Summary

```markdown
## SIMPLE WRITING AUDIT - RESUMO EXECUTIVO

**Copy Auditada:** [nome/descrição]
**Data:** [data]
**Auditor:** [nome]

### VEREDICTO GERAL:
[PRONTA / PRECISA AJUSTES / REESCREVER SEÇÕES / REESCREVER TUDO]

### SCORE FINAL: ___/100

### TOP 3 PROBLEMAS:
1. [problema mais crítico]
2. [segundo problema]
3. [terceiro problema]

### TOP 3 PONTOS FORTES:
1. [ponto forte]
2. [ponto forte]
3. [ponto forte]

### AÇÕES PRIORITÁRIAS:
1. [ação 1] - Impacto: ALTO/MÉDIO/BAIXO
2. [ação 2] - Impacto: ALTO/MÉDIO/BAIXO
3. [ação 3] - Impacto: ALTO/MÉDIO/BAIXO

### HOOK RECOMENDADO:
"[hook identificado como mais forte]"

### HEADLINE RECOMENDADA:
"[headline usando o hook]"
```

---

### 6.2 Before/After Comparison

```markdown
## COMPARAÇÃO ANTES/DEPOIS

### HEADLINE:
**ANTES:** "[original]"
**DEPOIS:** "[revisada]"
**Melhoria:** [o que mudou e por quê]

### ABERTURA:
**ANTES:** "[original - primeiras 3 frases]"
**DEPOIS:** "[revisada]"
**Melhoria:** [o que mudou e por quê]

### EXEMPLO DE PARÁGRAFO:
**ANTES:** "[parágrafo original mais problemático]"
**DEPOIS:** "[parágrafo revisado]"
**Melhoria:** [o que mudou e por quê]

### CLOSE:
**ANTES:** "[original]"
**DEPOIS:** "[revisado]"
**Melhoria:** [o que mudou e por quê]
```

---

### 6.3 Checklist Final

```markdown
## CHECKLIST FINAL - SIMPLE WRITING AUDIT

### Clareza
- [ ] Toda sentença tem apenas UMA ideia
- [ ] Nenhuma sentença tem mais de 20 palavras
- [ ] Zero jargão ou palavras corporativas
- [ ] Um estudante do 8º ano entenderia

### Conversacionalidade
- [ ] Usa contrações naturalmente
- [ ] Soa como conversa, não documento
- [ ] Passa no "teste do bar"
- [ ] Flui bem quando lido em voz alta

### Hook & Abertura
- [ ] Headline para imediatamente
- [ ] Abertura prende em 3 segundos
- [ ] "One-legged golfer" identificado e usado
- [ ] Promessa específica clara

### Lizard Brain
- [ ] Atinge instintos primais primeiro
- [ ] Emoção antes de lógica
- [ ] Gatilhos de medo/desejo/curiosidade presentes
- [ ] Visualização sensorial incluída

### Fechamento
- [ ] CTA impossível de perder
- [ ] Urgência presente e justificada
- [ ] Risco removido (garantia)
- [ ] Próximo passo 100% claro

### Prova
- [ ] Histórias reais (não ficção)
- [ ] Números específicos
- [ ] Testemunhos com detalhes
- [ ] Credibilidade estabelecida

**TOTAL:** ___/24 itens ✓
```

---

## QUICK REFERENCE

### Carlton's Core Rules

1. **One idea per sentence**
2. **Write like you talk**
3. **Find the one-legged golfer**
4. **Hit the lizard brain first**
5. **Every word must earn its place**
6. **Read it out loud**
7. **If it doesn't FEEL right, rewrite**

### Red Flags (Stop & Revise)

- ❌ Sentenças com mais de 25 palavras
- ❌ Jargão corporativo
- ❌ Headline sem hook
- ❌ Abertura sem emoção
- ❌ CTA vago ou ausente
- ❌ Sem histórias reais
- ❌ Sem prova específica

### Signs of Excellence

- ✅ Flui como conversa
- ✅ Cada sentença puxa para a próxima
- ✅ Hook inesperado e memorável
- ✅ Emoção palpável
- ✅ Ação clara e urgente
- ✅ Leitura prazerosa em voz alta

---

## APPENDIX: TRANSFORMATION EXAMPLES

### Example 1: Jargon → Simple

**ANTES:**
> "Nossa solução inovadora utiliza tecnologia de ponta para alavancar sinergias entre stakeholders e otimizar seus processos de negócio de forma holística."

**DEPOIS:**
> "Nossa ferramenta faz sua equipe trabalhar melhor junta. É isso."

### Example 2: Complex → Clear

**ANTES:**
> "A metodologia proprietária desenvolvida por nossa equipe de especialistas combina décadas de experiência com as mais recentes pesquisas científicas para criar um sistema único que tem demonstrado resultados consistentes em diversos contextos de aplicação."

**DEPOIS:**
> "Nosso sistema funciona.
> Testamos por 10 anos.
> Funciona toda vez.
> Em qualquer situação."

### Example 3: Boring → Conversational

**ANTES:**
> "É importante considerar que os benefícios deste programa incluem economia de tempo, aumento de produtividade e melhoria na qualidade de vida."

**DEPOIS:**
> "Olha, vou te contar o que você ganha:
> Seu tempo de volta.
> Mais coisas feitas.
> E sabe aquele estresse? Some."

---

*Task Version: 1.0*
*Created: 2026-01-23*
*Based on: John Carlton's Simple Writing System*
