# Create Sales Page Task

## Purpose
Criar uma página de vendas de alta conversão, guiando o usuário através de briefing estruturado e recomendando o copywriter ideal para o projeto.

## Inputs

```yaml
required:
  - product_name: Nome do produto/serviço
  - product_description: O que é e o que faz
  - target_avatar: Quem é o cliente ideal
  - main_problem: Problema principal que resolve
  - price: Preço do produto

optional:
  - testimonials: Depoimentos disponíveis
  - guarantee: Tipo de garantia oferecida
  - bonuses: Bônus inclusos
  - deadline: Se há urgência/escassez
  - tone: Tom desejado (agressivo, elegante, casual)
  - copywriter_preference: Copywriter específico desejado
```

## Workflow

### Step 1: Briefing Elicitation
```
Perguntas obrigatórias:
1. Qual o nome do produto?
2. O que exatamente ele faz/entrega?
3. Quem é o cliente ideal? (idade, profissão, situação)
4. Qual o problema #1 que ele resolve?
5. Qual o preço?
6. Tem depoimentos disponíveis?
7. Qual a garantia?
8. Há bônus ou urgência?
```

### Step 2: Copywriter Recommendation
```
Baseado no briefing, recomendar copywriter:

- Produto premium/sofisticado → David Ogilvy
- História forte do produto → Gary Halbert ou Joe Sugarman
- Mercado saturado/sofisticado → Eugene Schwartz
- Precisa de urgência/deadline → Dan Kennedy
- Curso online/digital → Frank Kern
- Precisa de testes A/B → Claude Hopkins
- Muito conteúdo/bullets → Gary Bencivenga
```

### Step 3: Structure Selection
```
Oferecer estruturas:

A. Long-Form Sales Letter (Halbert style)
   - Carta pessoal, storytelling, 3000+ palavras

B. VSL Script (Frank Kern style)
   - Para vídeo de vendas, conversacional

C. Modern Landing (Ogilvy style)
   - Elegante, focado em branding + conversão

D. Urgency Page (Kennedy style)
   - Deadline, escassez, ação imediata
```

### Step 4: Generate Sales Page

#### Structure Template
```markdown
# [HEADLINE - Promessa principal]

## [SUBHEADLINE - Especifica ou qualifica]

[LEAD - 2-3 parágrafos que prendem]

---

## O Problema
[Agite a dor do avatar]

## A Solução
[Apresente o produto como herói]

## Como Funciona
[Explique o mecanismo/processo]

## O Que Você Recebe
[Lista de benefícios/componentes]

## Prova Social
[Depoimentos, resultados, números]

## A Oferta
[Stack de valor + preço]

## Garantia
[Remova o risco]

## CTA
[Chamada para ação clara]

## FAQ
[Objeções comuns respondidas]

## CTA Final
[Última chamada]
```

### Step 5: Variations
```
Gerar alternativas:
- 3 headlines diferentes
- 2 leads diferentes
- 2 CTAs diferentes
```

### Step 6: Quality Check
```
Verificar contra checklist:
- [ ] Headline clara e específica
- [ ] Problema bem articulado
- [ ] Benefícios > Features
- [ ] Prova social presente
- [ ] Garantia clara
- [ ] CTA impossível de perder
- [ ] Urgência (se aplicável)
```

## Output

```yaml
format: markdown
sections:
  - headline_variations (3)
  - complete_sales_page
  - lead_variations (2)
  - cta_variations (2)
  - copywriter_notes (dicas específicas do estilo usado)
```

## Copywriter Styles Reference

### Gary Halbert Style
- Abertura com história pessoal
- Tom direto e provocador
- "Caro amigo" opening
- Urgência natural

### David Ogilvy Style
- Elegante e factual
- Headlines com benefício específico
- Prova em números
- Tom sofisticado

### Eugene Schwartz Style
- Big idea central
- Adequado ao nível de consciência
- Conceito transformador
- Intensificação gradual

### Dan Kennedy Style
- Urgência desde o início
- Deadline inviolável
- Stack de valor explícito
- CTA agressivo

### Frank Kern Style
- Casual e autêntico
- Storytelling relatável
- Valor upfront
- Voz conversacional

---

*Task Version: 1.0*
