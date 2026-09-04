# Create Downsell Page Task

## Purpose
Criar páginas de downsell eficazes que recuperam vendas perdidas oferecendo alternativa mais acessível, mantendo o relacionamento e maximizando revenue per visitor.

## When to Use
- Após recusa de oferta principal (exit intent)
- Carrinho abandonado
- Quem clicou mas não comprou
- Oferta alternativa para budget menor
- Recuperação de leads qualificados

## Inputs

```yaml
required:
  - main_offer: Oferta principal que foi recusada
  - main_price: Preço da oferta principal
  - downsell_offer: O que está oferecendo como alternativa
  - downsell_price: Preço do downsell
  - target_avatar: Quem é o cliente ideal

optional:
  - rejection_reason: Motivo provável da recusa (preço, timing, confiança)
  - relationship_context: Como chegaram até aqui (ad, email, referral)
  - future_upsell: Se há caminho para oferta maior depois
  - urgency_element: Se há escassez/deadline
  - copywriter_preference: Copywriter específico desejado
```

## Workflow

### Step 1: Rejection Analysis
```
Identificar motivo provável da recusa:

OBJEÇÃO DE PREÇO
- "Muito caro para mim agora"
- Solução: Oferta mais barata, parcelamento, versão lite

OBJEÇÃO DE TEMPO
- "Não é o momento certo"
- Solução: Mini-produto de início rápido, trial

OBJEÇÃO DE CONFIANÇA
- "Não tenho certeza se funciona para mim"
- Solução: Versão de menor risco, garantia estendida

OBJEÇÃO DE OVERWHELM
- "Parece muito complexo"
- Solução: Versão simplificada, passo-a-passo

OBJEÇÃO DE COMMITMENT
- "Não quero me comprometer agora"
- Solução: Produto único (não recorrente), trial
```

### Step 2: Downsell Strategy Selection
```
Escolher tipo de downsell:

1. VERSÃO LITE
   - Menos módulos/features
   - Core value mantido
   - Preço 30-50% menor
   Ex: "Curso completo" → "Módulo principal apenas"

2. PAYMENT PLAN
   - Mesmo produto
   - Dividido em mais parcelas
   - Facilita cash flow
   Ex: "R$997 à vista" → "12x de R$97"

3. TRIAL/SAMPLE
   - Acesso temporário
   - Primeira parte do produto
   - Upgrade posterior
   Ex: "Acesso completo" → "7 dias grátis"

4. PRODUTO ALTERNATIVO
   - Produto diferente, mais barato
   - Mesmo problema, solução menor
   Ex: "Mentoria" → "Curso gravado"

5. ONE-TIME vs RECURRING
   - Remove compromisso de longo prazo
   - Pagamento único
   Ex: "Assinatura mensal" → "Acesso vitalício"

6. DIY VERSION
   - Sem suporte/comunidade
   - Apenas conteúdo core
   - Para quem quer fazer sozinho
   Ex: "Com mentoria" → "Self-study"
```

### Step 3: Psychological Framing (Dan Kennedy)
```
Reframe a oferta para maximizar conversão:

ANCHOR & CONTRAST
"Você viu que [oferta principal] custa [preço alto].
Mas eu entendo que nem todo mundo pode investir isso agora.
Por isso criei [downsell] por apenas [preço baixo]."

LOSS AVERSION
"Antes de ir embora de mãos vazias, deixa eu te mostrar
uma opção que cabe no seu bolso e ainda te dá [benefício principal]."

FOOT IN THE DOOR
"Começa por aqui. Depois, quando tiver resultados,
você pode fazer upgrade para [oferta completa]."

SCARCITY MAINTAINED
"Esta oferta especial só aparece agora.
Se fechar esta página, volta ao preço normal."

SOCIAL PROOF RELEVANT
"[X] pessoas começaram assim e depois fizeram upgrade.
Algumas delas hoje faturam [resultado]."
```

### Step 4: Page Structure
```
Estrutura da página de downsell:

1. HEADLINE DE RECUPERAÇÃO
   "Espera! Antes de ir..."
   "Uma última coisa antes de você sair..."
   "Oferta especial só para você"

2. ACKNOWLEDGE THE REJECTION
   "Eu entendo que [oferta principal] pode não ser para você agora."
   "Talvez [preço] seja muito para investir hoje."
   (Validar sem julgar)

3. BRIDGE/TRANSITION
   "Mas eu não quero que você saia de mãos vazias."
   "Por isso, preparei algo especial..."

4. PRESENT DOWNSELL
   "[Nome do downsell]"
   - O que é
   - O que inclui
   - Como ajuda

5. VALUE COMPARISON
   [Oferta principal] = R$X
   [Downsell] = R$Y
   Você economiza [Z]% e ainda consegue [benefício core]

6. WHAT'S INCLUDED
   - Lista clara do que recebe
   - Bullets de benefícios
   - Valor de cada item

7. GUARANTEE
   - Mesma garantia ou melhor
   - Remove todo risco
   - "Se não gostar, devolvemos"

8. URGENCY
   - Esta oferta é só agora
   - Não verá de novo
   - Timer/deadline

9. CTA PRINCIPAL
   "Sim, quero o [downsell] por [preço]!"

10. SKIP OPTION
    "Não, obrigado. Prefiro sair."
    (Texto que causa loss aversion)
```

### Step 5: Copy Elements

#### Headlines de Downsell
```
WAIT-BASED:
- "Espera! Não vai embora ainda..."
- "Antes de sair, veja isso..."
- "Uma última oportunidade..."

UNDERSTANDING-BASED:
- "Entendo. [Preço] é muito agora."
- "Talvez não seja o momento para [oferta completa]."
- "Nem todo mundo pode investir [preço] hoje."

ALTERNATIVE-BASED:
- "E se eu te oferecesse uma versão mais acessível?"
- "Tenho algo especial para você..."
- "Uma opção que cabe no seu bolso..."

LOSS AVERSION:
- "Não saia de mãos vazias."
- "Não perca tudo que viu até aqui."
- "Leva pelo menos isso contigo."
```

#### CTAs de Downsell
```
ACCEPTANCE:
- "Sim! Quero o [produto] por apenas [preço]!"
- "Aceito esta oferta especial!"
- "Quero começar com [downsell]!"

REJECTION (Cause Loss Aversion):
- "Não, prefiro perder esta oportunidade única."
- "Não, não preciso de ajuda com [problema]."
- "Não, vou continuar fazendo do jeito errado."
```

### Step 6: Urgency Elements
```
Criar urgência genuína:

TIMER
"Esta oferta expira em [countdown]"
(Timer visível, real)

ONE-TIME OFFER
"Esta página não vai aparecer de novo"
"Oferta exclusiva para quem viu [oferta principal]"

LIMITED SPOTS
"Restam apenas [X] vagas nesta condição"
(Se for verdade)

PRICE INCREASE
"Depois desta página, volta para [preço normal]"
```

### Step 7: Quality Check
```
Verificar página:

PSICOLOGIA
- [ ] Valida a recusa (não julga)?
- [ ] Apresenta alternativa genuinamente útil?
- [ ] Cria loss aversion sem manipulação?

CLAREZA
- [ ] Fica claro o que está recebendo?
- [ ] Preço é obviamente menor?
- [ ] Diferença para oferta principal é clara?

CONVERSÃO
- [ ] CTA é impossível de ignorar?
- [ ] Urgência é real?
- [ ] Garantia remove risco?

RELACIONAMENTO
- [ ] Mantém porta aberta para futuro?
- [ ] Tom é respeitoso?
- [ ] Oferece valor real (não sobra)?
```

## Output

```yaml
format: markdown
sections:
  - rejection_analysis
  - downsell_strategy
  - complete_page_copy
  - headline_variations (3)
  - cta_variations (3)
  - urgency_elements
  - quality_checklist
```

## Copywriter Recommendations

| Contexto | Copywriter Ideal | Por quê |
|----------|------------------|---------|
| Downsell com urgência | Dan Kennedy | Mestre em escassez e fechamento |
| Downsell de high-ticket | Alex Hormozi | Value stacking, pricing psychology |
| Downsell empático | Frank Kern | Tom casual, relacionamento |
| Downsell com story | Gary Halbert | Conecta emocionalmente |
| Downsell sofisticado | David Ogilvy | Premium mesmo em preço menor |

## Page Templates

### Template 1: Price Objection Downsell
```markdown
# Espera! Eu entendo.

R$[preço principal] é um investimento considerável.

Nem todo mundo pode fazer isso agora, e tudo bem.

**Mas eu não quero que você saia de mãos vazias.**

Por isso, criei uma versão especial só para quem chegou até aqui:

## [Nome do Downsell]

[Descrição em 2-3 linhas]

### O que você recebe:

✓ [Componente 1] — Valor: R$X
✓ [Componente 2] — Valor: R$Y
✓ [Componente 3] — Valor: R$Z

**Valor Total: R$[soma]**

### Seu investimento hoje:

~~R$[preço original]~~ → **Apenas R$[preço downsell]**

### Garantia de 30 dias

Se não gostar, devolvemos 100% do seu dinheiro. Sem perguntas.

---

⚠️ **Esta oferta é exclusiva para esta página.**
Quando fechar, não verá de novo.

[BOTÃO: Sim, quero por R$[preço]!]

[Link menor: Não, obrigado. Prefiro sair sem nada.]
```

### Template 2: Lite Version Downsell
```markdown
# Uma última coisa antes de você ir...

Eu vi que você se interessou por [oferta principal] mas decidiu não seguir.

Talvez seja o preço. Talvez o timing. Talvez você queira testar antes.

**E se eu te oferecesse apenas o essencial?**

## [Nome] — Versão Essencial

A versão [lite/essencial/core] do [produto principal] com:

• [Feature principal 1]
• [Feature principal 2]
• [Feature principal 3]

**Sem** [feature removida que justifica preço menor]

Perfeito para quem quer começar e depois fazer upgrade.

### Comparativo:

| | Completo | Essencial |
|---|---|---|
| [Feature 1] | ✓ | ✓ |
| [Feature 2] | ✓ | ✓ |
| [Feature 3] | ✓ | ✗ |
| Preço | R$X | **R$Y** |

[BOTÃO: Quero a versão essencial!]
```

### Template 3: Payment Plan Downsell
```markdown
# O investimento é a única barreira?

Eu entendo. R$[preço] de uma vez pode pesar no orçamento.

**E se você pudesse dividir?**

## Mesmo [Produto], Parcelas Menores

Tudo que você viu na oferta principal:
[Lista rápida de benefícios]

**Agora em [X]x de R$[valor menor]**

Mesma garantia. Mesmo acesso. Só o pagamento que fica mais leve.

---

💡 **Na prática:**
- Menos de R$[valor/dia] por dia
- Começa a ter resultados antes de terminar de pagar
- Pode cancelar a qualquer momento

[BOTÃO: Quero parcelar em [X]x!]

[Link: Prefiro não, mesmo assim.]
```

## Metrics to Track

```yaml
downsell_metrics:
  - conversion_rate: "% que aceita downsell"
  - revenue_recovered: "R$ recuperado que seria perdido"
  - upgrade_rate: "% de downsell que faz upgrade depois"
  - ltv_comparison: "LTV de quem entra por downsell vs oferta principal"
```

---

*Task Version: 1.0*
*Primary Framework: Loss Aversion + Foot in the Door (Dan Kennedy)*
