# Create Upsell Page Task

## Purpose
Criar páginas de upsell/downsell de alta conversão para maximizar valor do cliente.

## Inputs

```yaml
required:
  - upsell_type: upsell | downsell | order_bump | cross_sell
  - main_product: Produto que acabou de comprar
  - upsell_product: Produto sendo oferecido
  - upsell_price: Preço do upsell
  - main_benefit: Benefício principal do upsell

optional:
  - relationship: Como upsell complementa produto principal
  - discount: Desconto especial (se houver)
  - urgency: Limite de tempo
  - copywriter_preference: Estilo preferido
```

## Upsell Types

### 1. Upsell (Mais do Mesmo/Melhor)
```yaml
timing: Imediatamente após compra
price: 30-50% do produto principal
example: "Quer a versão premium com [EXTRAS]?"
conversion: 10-30%
```

### 2. Downsell (Versão Menor)
```yaml
timing: Após recusar upsell
price: 50-70% menor que upsell
example: "Que tal só [COMPONENTE] por [PREÇO MENOR]?"
conversion: 15-40%
```

### 3. Order Bump (Checkout)
```yaml
timing: Na página de checkout
price: R$7-47 (impulso)
example: "Adicione [ITEM] por apenas R$X"
conversion: 20-50%
```

### 4. Cross-Sell (Complementar)
```yaml
timing: Pós-compra ou thank you page
price: Varia
example: "Clientes que compraram X também adoram Y"
conversion: 5-15%
```

## Page Structure

### Upsell Page (OTO - One Time Offer)
```markdown
# ESPERA! Seu Pedido Não Está Completo...

## [HEADLINE - Oferta especial exclusiva]

[VIDEO ou IMAGEM do produto]

### Por que isso importa:

Você acabou de adquirir [PRODUTO PRINCIPAL].

Mas existe um problema: [PROBLEMA QUE UPSELL RESOLVE]

É por isso que criei [UPSELL PRODUCT]...

### O que você recebe:

✅ [Componente 1] - Valor R$[X]
✅ [Componente 2] - Valor R$[X]
✅ [Componente 3] - Valor R$[X]

**Valor Total: R$[SOMA]**
**Apenas para você agora: R$[PREÇO]**

⏰ Esta oferta expira quando você sair desta página

[BOTÃO: SIM! Adicionar ao Meu Pedido por R$X]

[Link menor: Não, obrigado. Continuar para meu pedido.]
```

### Downsell Page
```markdown
# Entendo... Que tal uma opção mais acessível?

## [VERSÃO REDUZIDA] por apenas R$[PREÇO MENOR]

Percebi que [UPSELL COMPLETO] pode não ser pra todo mundo agora.

Por isso, separei apenas [COMPONENTE ESSENCIAL]:

✅ [O que inclui]

Por apenas R$[PREÇO] (economia de [%] sobre o valor original)

[BOTÃO: Quero Esta Opção por R$X]

[Link: Não, obrigado. Finalizar meu pedido.]
```

### Order Bump Copy (Checkbox)
```markdown
☐ SIM! Adicione [PRODUTO] por apenas R$[PREÇO]

[DESCRIÇÃO em 1-2 linhas do benefício principal]

(Economize [%] - preço normal: R$[PREÇO CHEIO])
```

## Copywriter Styles for Upsells

### Dan Kennedy Style (Recommended)
```
- Urgência forte (página expira)
- Escassez real
- Stack de valor claro
- "Esta é sua única chance"
```

### Joe Sugarman Style
```
- Storytelling curto
- Trigger de reciprocidade
- "Já que você está aqui..."
- Conversational
```

### Claude Hopkins Style
```
- Oferta testável
- Números específicos
- Comparação de valor
- Garantia destacada
```

## Key Principles

### 1. Relevância
O upsell DEVE complementar o produto principal.

### 2. Valor Óbvio
Economia ou benefício deve ser imediatamente claro.

### 3. Simplicidade
Decisão deve levar <30 segundos.

### 4. Sem Fricção
Um clique para aceitar.

### 5. Saída Fácil
Caminho claro para recusar sem culpa.

## CTA Variations

### Accept CTAs
```
- "SIM! Adicionar por R$X"
- "Quero Este Upgrade"
- "Incluir no Meu Pedido"
- "Aproveitar Esta Oferta"
```

### Decline CTAs
```
- "Não, obrigado. Continuar."
- "Pular esta oferta"
- "Não preciso disso agora"
- "Continuar para meu pedido"
```

## Output Deliverables

```yaml
deliverables:
  - upsell_page_copy:
      - headline
      - video_script (se aplicável)
      - body_copy
      - value_stack
      - cta_buttons
  - downsell_page_copy (variação)
  - order_bump_copy (se solicitado)
  - a_b_variations: 2 versões de headline
```

## Quality Checklist

- [ ] Upsell é relevante para produto principal
- [ ] Valor é óbvio em <5 segundos
- [ ] Urgência é clara (página expira)
- [ ] CTA é impossível de perder
- [ ] Recusa é fácil e sem culpa
- [ ] Preço parece justo pelo valor
- [ ] Copy é curto e scannable

## Metrics to Track

```yaml
metrics:
  - upsell_take_rate: % que aceita
  - downsell_take_rate: % que aceita após recusar upsell
  - average_order_value: Antes vs depois de upsells
  - refund_rate: Por produto
```

---

*Task Version: 1.0*
