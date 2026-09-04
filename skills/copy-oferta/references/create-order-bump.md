# Create Order Bump Task

## Purpose
Criar order bumps de alta conversão que aumentam o ticket médio no momento do checkout, oferecendo complemento irresistível com um clique.

## When to Use
- Página de checkout/pagamento
- Carrinho de compras
- Processo de finalização de pedido
- Qualquer momento pré-compra onde pode adicionar valor

## Inputs

```yaml
required:
  - main_product: Produto principal sendo comprado
  - main_price: Preço do produto principal
  - bump_product: Produto do order bump
  - bump_price: Preço do order bump
  - target_avatar: Quem é o cliente

optional:
  - relationship: Como bump complementa o principal
  - perceived_value: Valor percebido do bump
  - urgency_element: Se há escassez específica
  - copywriter_preference: Copywriter específico desejado
```

## Workflow

### Step 1: Bump Strategy Selection
```
Escolher tipo de order bump:

1. ACELERADOR
   - Faz o resultado chegar mais rápido
   - "Atalho" para o sucesso
   Ex: Templates prontos, checklists, quick-start

2. COMPLEMENTO ESSENCIAL
   - Algo que "falta" no produto principal
   - Melhora significativamente a experiência
   Ex: Workbook, guia de implementação

3. VERSÃO PREMIUM
   - Upgrade do produto principal
   - Mais features/acesso
   Ex: Acesso VIP, módulo extra, comunidade

4. FERRAMENTA
   - Software, template, recurso prático
   - Uso imediato
   Ex: Planilha, script, checklist

5. SUPORTE
   - Ajuda adicional
   - Contato direto
   Ex: Sessão de consultoria, grupo privado

6. CONTEÚDO BÔNUS
   - Material extra exclusivo
   - Aprofundamento
   Ex: Masterclass, entrevistas, case studies
```

### Step 2: Pricing Psychology
```
Definir preço do bump:

REGRA DE OURO: 10-25% do produto principal

EXEMPLOS:
- Produto R$297 → Bump R$37-67
- Produto R$997 → Bump R$97-197
- Produto R$1997 → Bump R$197-397

ANCORAGEM:
- Mostre valor original do bump
- "De R$197 por apenas R$47"
- Economia clara e específica

JUSTIFICATIVA:
- "Preço especial porque você já está comprando [principal]"
- "Disponível apenas durante o checkout"
```

### Step 3: Copy Structure
```
Estrutura do box de order bump:

┌─────────────────────────────────────────┐
│ ☐ SIM! Adicione [Bump] por apenas R$X  │
├─────────────────────────────────────────┤
│ [HEADLINE chamativa]                     │
│                                          │
│ [2-3 linhas descrevendo o bump]          │
│                                          │
│ • Benefício 1                            │
│ • Benefício 2                            │
│ • Benefício 3                            │
│                                          │
│ ~~De R$Y~~ → Apenas R$X (Economia de Z%) │
│                                          │
│ ⚠️ Oferta exclusiva do checkout          │
└─────────────────────────────────────────┘
```

### Step 4: Headline Formulas
```
Fórmulas de headline para order bump:

ONE-TIME OFFER:
"Oferta única: [Bump] por R$X"
"Só durante o checkout: [Bump]"

ENHANCEMENT:
"Turbine seu [produto principal] com [bump]"
"Maximize seus resultados com [bump]"

ACCELERATION:
"Chegue em [resultado] 2x mais rápido"
"O atalho para [benefício]"

FEAR OF MISSING:
"Não perca: [Bump] por apenas R$X"
"Última chance de adicionar [bump]"

EXCLUSIVE:
"Exclusivo para quem está comprando agora"
"Disponível apenas neste momento"
```

### Step 5: Description Copy
```
Fórmulas para descrição curta:

PROBLEMA → SOLUÇÃO (2 linhas)
"Muitos [avatares] travam em [problema específico].
[Bump] resolve isso com [solução]."

RESULTADO ESPECÍFICO (2 linhas)
"[Bump] te ajuda a [resultado 1] e [resultado 2]
em [tempo curto] — sem [dificuldade comum]."

COMPLEMENTO NATURAL (2 linhas)
"[Produto principal] te ensina [o quê].
[Bump] te dá [ferramenta/atalho] para aplicar mais rápido."

SOCIAL PROOF (2 linhas)
"[X]% dos nossos clientes adicionam [bump].
Eles conseguem [resultado] em metade do tempo."
```

### Step 6: Bullet Points
```
3-5 bullets de alto impacto:

FORMATO: ✓ [Benefício específico e tangível]

EXEMPLOS:
✓ Templates prontos para copiar e colar
✓ Economize [X] horas de trabalho
✓ Funciona mesmo se você é iniciante
✓ Atualizações incluídas para sempre
✓ Usado por [número] de [avatares] com sucesso
```

### Step 7: Visual Design Guidelines
```
Elementos visuais do box:

CHECKBOX
- Grande e clicável
- Cor que destaca (mas não grita)
- Estado checked = verde/azul

DESTAQUE
- Borda colorida ou fundo diferenciado
- Deve parecer "especial" mas não spam
- Consistente com design da página

POSIÇÃO
- Logo acima do botão de compra
- Visível sem scroll excessivo
- Fácil de notar e fácil de marcar

TAMANHO
- Compacto mas legível
- Não pode parecer "escondido"
- Mobile-friendly (botão grande)
```

### Step 8: A/B Test Variations
```
Criar variações para teste:

VARIAÇÃO A: Headline focada em atalho
VARIAÇÃO B: Headline focada em economia
VARIAÇÃO C: Headline focada em exclusividade

ELEMENTOS PARA TESTAR:
- Preço do bump (R$47 vs R$67)
- Posição do checkbox (início vs fim)
- Comprimento do copy (curto vs médio)
- Com/sem timer de urgência
```

### Step 9: Quality Check
```
Verificar order bump:

RELEVÂNCIA
- [ ] Bump complementa naturalmente o principal?
- [ ] Faz sentido para o avatar?
- [ ] Resolve problema real?

PREÇO
- [ ] Preço entre 10-25% do principal?
- [ ] Economia está clara?
- [ ] Valor percebido > preço?

COPY
- [ ] Headline chama atenção?
- [ ] Benefícios claros em 5 segundos?
- [ ] CTA impossível de ignorar?

UX
- [ ] Fácil de adicionar (1 clique)?
- [ ] Visível mas não invasivo?
- [ ] Funciona em mobile?

ÉTICA
- [ ] Oferece valor real?
- [ ] Não é enganoso?
- [ ] Cliente ficaria feliz em ter comprado?
```

## Output

```yaml
format: markdown
sections:
  - bump_strategy
  - complete_bump_copy
  - headline_variations (3)
  - bullet_variations
  - design_guidelines
  - ab_test_plan
  - quality_checklist
```

## Copywriter Recommendations

| Contexto | Copywriter Ideal | Por quê |
|----------|------------------|---------|
| Bump de alto valor | Alex Hormozi | Value stacking, pricing |
| Bump com urgência | Dan Kennedy | Escassez, ação imediata |
| Bump de ferramenta | Joe Sugarman | Demonstração lógica |
| Bump premium/sofisticado | David Ogilvy | Elegância, aspiracional |
| Bump com story | Gary Halbert | Conexão emocional |

## Order Bump Templates

### Template 1: Acelerador
```markdown
☐ SIM! Adicione o [Nome do Bump] por apenas R$47

### Chegue em [resultado] 2x mais rápido

[Produto principal] te ensina o método completo.
[Bump] te dá os atalhos que economizam [X] horas.

✓ [X] templates prontos para copiar e colar
✓ Checklists de implementação passo-a-passo
✓ [Bônus específico] incluído

~~De R$197~~ → Apenas R$47 (76% OFF)

⚠️ Oferta exclusiva do checkout — não disponível depois
```

### Template 2: Complemento Essencial
```markdown
☐ SIM! Quero o [Nome] junto!

### O complemento perfeito para [produto principal]

Enquanto [produto] te ensina a [habilidade],
[bump] te dá [ferramenta] para aplicar imediatamente.

✓ [Benefício tangível 1]
✓ [Benefício tangível 2]
✓ [Benefício tangível 3]

Por apenas R$67 (valor de R$197)

💡 85% dos nossos clientes adicionam este item
```

### Template 3: Versão VIP
```markdown
☐ UPGRADE: Acesso VIP por +R$97

### Transforme sua experiência em algo exclusivo

Tudo que vem no [produto principal], MAIS:

✓ Acesso à comunidade privada
✓ [X] sessões de Q&A ao vivo
✓ Suporte prioritário por [canal]
✓ [Bônus exclusivo VIP]

Valor total: R$497 → Seu upgrade: apenas R$97

⚡ Disponível APENAS durante o checkout
```

### Template 4: Ferramenta Prática
```markdown
☐ Adicionar [Nome da Ferramenta] — R$37

### A ferramenta que faz [resultado] em [tempo]

Chega de [problema comum]. Com [ferramenta]:

✓ [Funcionalidade 1] — economize [X] horas
✓ [Funcionalidade 2] — elimine [dor]
✓ [Funcionalidade 3] — garanta [resultado]

Inclui atualizações para sempre.

~~R$97~~ → R$37 (só no checkout)
```

### Template 5: Suporte Premium
```markdown
☐ SIM! Quero suporte direto por +R$147

### Nunca fique travado: suporte 1-a-1

Além do [produto principal], você terá:

✓ [X] minutos de consultoria individual
✓ Revisão personalizada do seu [projeto]
✓ Acesso direto por [WhatsApp/email] por [período]

De R$497 → Apenas R$147 (economize 70%)

🎯 Perfeito para quem quer resultado garantido
```

## Metrics to Track

```yaml
order_bump_metrics:
  take_rate: "% que adiciona o bump"
  revenue_per_order: "Aumento médio do ticket"
  refund_rate: "% de reembolso do bump vs principal"
  target_take_rate: "20-40% é considerado bom"
```

## Quick Reference: Bump Formulas

```
HEADLINE:
- "Oferta única: [Bump] por R$X"
- "Turbine seu [principal] com [bump]"
- "Chegue em [resultado] mais rápido"

DESCRIÇÃO:
- "[Avatar] travam em [problema]. [Bump] resolve."
- "[Bump] te ajuda a [resultado] em [tempo]."

BULLETS:
- ✓ [Benefício tangível e específico]
- ✓ Economize [X] horas/dinheiro
- ✓ Usado por [número] de [avatares]

URGÊNCIA:
- "Oferta exclusiva do checkout"
- "Não disponível depois"
- "X% dos clientes adicionam"
```

---

*Task Version: 1.0*
*Primary Framework: Value Stacking (Alex Hormozi) + One-Time Offer (Dan Kennedy)*
