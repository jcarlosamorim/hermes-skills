# Create Abandoned Cart Task

## Purpose
Criar sequências de email para recuperar carrinhos abandonados, reengajando compradores que demonstraram interesse mas não finalizaram a compra.

## When to Use
- Checkout iniciado mas não finalizado
- Visitou página de vendas mas não comprou
- Adicionou ao carrinho mas abandonou
- Começou processo de pagamento e parou

## Inputs

```yaml
required:
  - product_name: Nome do produto
  - product_price: Preço do produto
  - checkout_page: URL do checkout
  - target_avatar: Quem é o cliente ideal

optional:
  - abandonment_point: Onde abandonaram (checkout, pagamento, form)
  - time_since_abandonment: Quanto tempo desde abandono
  - incentive_available: Se pode oferecer desconto/bônus
  - product_type: Tipo de produto (curso, SaaS, físico)
  - urgency_element: Se há escassez real
  - copywriter_preference: Copywriter específico desejado
```

## Workflow

### Step 1: Abandonment Analysis
```
Identificar provável motivo do abandono:

OBJEÇÃO DE PREÇO
- Viu o preço e hesitou
- Solução: Mostrar valor, oferecer parcelamento

OBJEÇÃO DE CONFIANÇA
- Não tem certeza se funciona
- Solução: Prova social, garantia

OBJEÇÃO DE TEMPO
- "Vou pensar"
- Solução: Urgência, custo de esperar

DISTRAÇÃO
- Simplesmente se distraiu
- Solução: Lembrete simples, sem pressão

FRICÇÃO TÉCNICA
- Problema no checkout
- Solução: Oferecer ajuda, link direto
```

### Step 2: Sequence Timing
```
Timing recomendado:

EMAIL 1: 1 hora após abandono
- Lembrete gentil
- "Esqueceu algo?"

EMAIL 2: 24 horas após
- Valor + objeções
- Por que vale a pena

EMAIL 3: 48-72 horas após
- Prova social
- Resultados de outros

EMAIL 4: 5-7 dias após
- Urgência/incentivo
- Última chance

REGRAS:
- Mais agressivo = produtos de baixo ticket
- Mais espaçado = high-ticket
- Sempre ter opção de opt-out
```

### Step 3: Email Templates

#### EMAIL 1: LEMBRETE GENTIL (1h)
```markdown
Assunto: Esqueceu algo?

[Nome],

Percebi que você estava finalizando sua compra de [Produto]
mas algo te interrompeu.

Seu carrinho ainda está salvo.

Se quiser continuar de onde parou:
→ [Link direto para checkout]

Caso tenha encontrado algum problema técnico,
me avisa que ajudo você.

[Assinatura]

P.S. [Benefício rápido do produto]
```

#### EMAIL 2: VALOR + OBJEÇÕES (24h)
```markdown
Assunto: Antes de decidir sobre [Produto]...

[Nome],

Vi que você visitou [Produto] ontem mas não finalizou.

Sem problema — quero ter certeza que você tem todas
as informações para tomar a melhor decisão.

**Por que [Produto] funciona:**
[2-3 bullets de benefícios principais]

**Se você está pensando...**

"E se não funcionar para mim?"
→ Garantia de [X] dias. Se não curtir, devolvemos tudo.

"É muito caro"
→ [Argumento de valor ou parcelamento]

"Não é o momento"
→ [Custo de esperar / urgência]

Alguma dúvida que não respondi? Me conta.

→ [Link para checkout]

[Assinatura]
```

#### EMAIL 3: PROVA SOCIAL (48-72h)
```markdown
Assunto: [Nome do cliente] também tinha dúvidas...

[Nome],

Deixa eu te contar sobre [Nome do cliente].

[Ele/Ela] também hesitou. Também pensou se valia a pena.

Mas decidiu experimentar.

[Resultado]:
"[Depoimento]"

[Ele/Ela] não é exceção. [X] pessoas já passaram
por [Produto] e conseguiram [resultado].

Você pode ser o próximo.

→ [Link]

[Assinatura]

P.S. Seu carrinho ainda está salvo.
```

#### EMAIL 4: URGÊNCIA/INCENTIVO (5-7 dias)
```markdown
Assunto: [Incentivo] expira hoje

[Nome],

Esta é minha última mensagem sobre seu carrinho.

Não vou te encher de emails.

Mas queria te avisar:

[SE TIVER INCENTIVO:]
O desconto especial de [X]% que reservei para você
expira hoje às [horário].

Depois disso, volta ao preço normal.

[SE NÃO TIVER INCENTIVO:]
Seu carrinho salvo vai expirar.

Se [Produto] faz sentido para você, agora é a hora.

→ [Link]

Se não fizer, tudo bem. Só me avisa para eu parar
de enviar lembretes.

[Assinatura]
```

### Step 4: Subject Line Formulas
```
Por tipo de email:

LEMBRETE (Email 1):
- "Esqueceu algo?"
- "Seu carrinho está esperando"
- "Ainda está aí?"
- "[Nome], um minuto..."

VALOR (Email 2):
- "Antes de decidir..."
- "Uma coisa que não mencionei"
- "Sobre [Produto]..."
- "Respondendo sua dúvida"

PROVA SOCIAL (Email 3):
- "[Cliente] também tinha dúvidas"
- "Olha o que [Nome] conseguiu"
- "Você não está sozinho"
- "O que [X] pessoas descobriram"

URGÊNCIA (Email 4):
- "Última chance: [incentivo]"
- "Seu carrinho vai expirar"
- "Antes que desapareça"
- "24 horas e acabou"
```

### Step 5: Incentive Strategies
```
Estratégias de incentivo para recuperação:

DESCONTO
- 10-20% off (não desvalorize muito)
- Código exclusivo: VOLTA10
- "Reservei para você"

BÔNUS EXTRA
- Adicione bônus não incluído antes
- "Por voltar, ganhe [bônus]"
- Funciona melhor que desconto

PARCELAMENTO ESPECIAL
- Mais parcelas
- Primeira parcela menor
- "Facilitar para você"

TRIAL/SAMPLE
- Teste gratuito de X dias
- Primeiro módulo grátis
- Baixa barreira de entrada

URGÊNCIA REAL
- Preço sobe em [data]
- Bônus expira
- Vagas acabando

IMPORTANTE:
- Não use incentivos sempre (treina comportamento)
- Alterne estratégias
- Alguns abandonos são bons (qualificação)
```

### Step 6: Advanced Tactics
```
Táticas avançadas:

SEGMENTAÇÃO POR ABANDONMENT POINT
- Abandonou no checkout → email de facilidade
- Abandonou no preço → email de valor
- Abandonou no form → email de ajuda técnica

PERSONALIZAÇÃO
- Nome do produto específico
- Quanto faltou para completar
- Valor do carrinho

MULTI-CANAL
- Email + Retargeting ads
- Email + SMS (se permitido)
- Email + Push notification

TIMING DINÂMICO
- Abandono à noite → email de manhã
- Abandono no trabalho → email fim do dia
- Teste horários diferentes

GAMIFICAÇÃO
- "Seu carrinho está chorando"
- "Salvamos seu lugar"
- Visual de produto esperando
```

### Step 7: Quality Check
```
Verificar sequência:

TOM
- [ ] Não é desesperado/spammy?
- [ ] Respeita a decisão do usuário?
- [ ] Tom é de serviço, não pressão?

VALOR
- [ ] Cada email adiciona algo novo?
- [ ] Objeções são tratadas?
- [ ] Benefícios claros?

TÉCNICO
- [ ] Links funcionam?
- [ ] Personalização correta?
- [ ] Opt-out fácil?

TIMING
- [ ] Espaçamento adequado?
- [ ] Total de emails razoável?
- [ ] Para após X dias sem resposta?
```

## Output

```yaml
format: markdown
sections:
  - abandonment_analysis
  - complete_email_sequence (4 emails)
  - subject_line_variations
  - incentive_strategy (if applicable)
  - quality_checklist
```

## Copywriter Recommendations

| Contexto | Copywriter Ideal | Por quê |
|----------|------------------|---------|
| Recuperação urgente | Dan Kennedy | Escassez, deadline |
| Tom amigável/casual | Frank Kern | Autenticidade |
| Foco em valor | Alex Hormozi | Valor vs preço |
| Prova social pesada | Gary Bencivenga | Credibilidade |
| High-ticket | David Ogilvy | Sofisticação |

## Metrics to Track

```yaml
abandoned_cart_metrics:
  recovery_rate: "% de carrinhos recuperados"
  revenue_recovered: "R$ recuperado"
  email_1_conversion: "% que converte no email 1"
  time_to_recovery: "Tempo médio até recuperação"
  unsubscribe_rate: "% que dá unsubscribe"

benchmarks:
  good_recovery_rate: "5-15%"
  great_recovery_rate: "15-25%"
```

## Sequence Comparison

```yaml
low_ticket:
  timing: "1h → 24h → 48h → 72h"
  total_emails: 4
  tone: "Mais direto, mais urgência"
  incentive: "Desconto funciona bem"

high_ticket:
  timing: "1h → 48h → 5 dias → 10 dias"
  total_emails: 4
  tone: "Mais consultivo, menos pressão"
  incentive: "Bônus > desconto"

saas:
  timing: "1h → 24h → 72h → 7 dias"
  total_emails: 4
  tone: "Trial gratuito, demonstração"
  incentive: "Extensão de trial, feature extra"
```

---

*Task Version: 1.0*
*Primary Framework: Recovery Sequence (Ryan Deiss/Digital Marketer)*
