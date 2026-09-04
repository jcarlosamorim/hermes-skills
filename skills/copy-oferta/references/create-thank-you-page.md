# Create Thank You Page Task

## Purpose
Criar páginas de obrigado estratégicas que confirmam a compra, reduzem buyer's remorse, apresentam upsell e iniciam o relacionamento de forma positiva.

## When to Use
- Após finalização de compra
- Após captura de lead (lead magnet)
- Após inscrição em webinar/evento
- Qualquer conversão que merece confirmação

## Inputs

```yaml
required:
  - conversion_type: O que o usuário fez (compra, lead, inscrição)
  - product_name: Nome do produto/oferta
  - next_steps: O que acontece agora
  - access_info: Como/quando terá acesso

optional:
  - upsell_offer: Oferta de upsell (One-Time Offer)
  - community_link: Link para comunidade/grupo
  - social_sharing: Se quer incentivar compartilhamento
  - referral_program: Se há programa de indicação
  - copywriter_preference: Copywriter específico desejado
```

## Workflow

### Step 1: Thank You Page Type Selection
```
Escolher tipo de página:

1. CONFIRMAÇÃO SIMPLES
   - Apenas confirma a ação
   - Próximos passos claros
   - Sem oferta adicional
   Uso: Leads, inscrições simples

2. THANK YOU + OTO (One-Time Offer)
   - Confirma + apresenta upsell
   - Oferta única, só agora
   - Timer de urgência
   Uso: Após compras, leads qualificados

3. THANK YOU + PRÓXIMOS PASSOS
   - Confirma + onboarding detalhado
   - Checklists, vídeo de boas-vindas
   - Prepara para consumo
   Uso: Produtos complexos, cursos

4. THANK YOU + COMUNIDADE
   - Confirma + convida para grupo
   - Links de acesso
   - Expectativas claras
   Uso: Programas com comunidade

5. THANK YOU + REFERRAL
   - Confirma + incentiva indicação
   - Programa de referência
   - Benefícios claros
   Uso: Produtos com potencial viral
```

### Step 2: Confirmation Block
```
Elementos de confirmação:

HEADLINE DE SUCESSO
- "Parabéns! Sua compra foi confirmada!"
- "Você está dentro!"
- "Bem-vindo(a) à [comunidade/produto]!"

RESUMO DO PEDIDO
- O que comprou
- Quanto pagou
- Número do pedido/confirmação

PRÓXIMOS PASSOS
- O que acontece agora
- Quando terá acesso
- O que fazer primeiro

EXPECTATIVAS
- Quando receberá email
- Como acessar
- Suporte se precisar
```

### Step 3: Buyer's Remorse Prevention
```
Elementos para reduzir arrependimento:

VALIDAÇÃO DA DECISÃO
"Você tomou a decisão certa. [Produto] já ajudou [X] pessoas a [resultado]."
"Esta é uma das melhores decisões que você poderia tomar para [área da vida]."

ANTECIPAÇÃO DE RESULTADO
"Nos próximos [tempo], você vai [benefício 1], [benefício 2] e [benefício 3]."
"Em breve você estará [estado desejado]."

PROVA SOCIAL IMEDIATA
"Assim como [Nome], que conseguiu [resultado] em [tempo]."
Depoimento curto de cliente satisfeito.

REFORÇO DE GARANTIA
"Lembre-se: você tem [X] dias de garantia. Zero risco."
```

### Step 4: One-Time Offer (OTO) Block
```
Se incluir upsell:

HEADLINE DE OTO
"Espera! Oferta especial só para novos membros"
"Uma última coisa antes de acessar..."
"Exclusivo para quem acabou de comprar"

PROPOSTA DE VALOR
- O que é o upsell
- Por que faz sentido AGORA
- Como complementa a compra

PREÇO ESPECIAL
- Desconto significativo (30-60%)
- Só válido agora
- Timer visível

CTA CLARO
"Sim, adicione por R$X!"
"Não, só quero meu [produto original]"

POSICIONAMENTO
- NÃO bloqueia acesso ao produto
- É oportunidade, não barreira
- Fácil de recusar sem culpa
```

### Step 5: Next Steps Block
```
Instruções claras de próximos passos:

FORMATO NUMERADO
1. Confira seu email para [o quê]
2. Acesse [plataforma] com [credenciais]
3. Comece por [módulo/ação]
4. Se precisar de ajuda, [contato]

QUICK WIN IMEDIATO
"Enquanto espera o email, faça isso:"
[Ação simples que dá resultado rápido]

EXPECTATIVAS DE TEMPO
"Em até [X] minutos você receberá..."
"Seu acesso estará disponível em..."
```

### Step 6: Community/Social Block
```
Convite para comunidade:

CONVITE PARA GRUPO
"Participe do nosso grupo exclusivo:"
[Link para grupo/comunidade]

EXPECTATIVAS DO GRUPO
- O que encontrará lá
- Regras básicas
- Como se apresentar

INCENTIVO A COMPARTILHAR
"Compartilhe sua conquista:"
[Botões de social share]

PROGRAMA DE INDICAÇÃO
"Indique amigos e ganhe [benefício]"
[Link de referência único]
```

### Step 7: Consumo Inicial
```
Ajudar a começar imediatamente:

VÍDEO DE BOAS-VINDAS
- Breve (2-5 min)
- Orientação de como começar
- Tom acolhedor

CHECKLIST DE INÍCIO
□ Acessar área de membros
□ Completar módulo 1
□ Entrar na comunidade
□ Agendar primeira [ação]

RECURSO PARA COMEÇAR
- PDF de quick start
- Primeiro módulo desbloqueado
- Template inicial
```

### Step 8: Page Structure
```
Estrutura completa:

┌────────────────────────────────────────┐
│ [CONFIRMAÇÃO]                          │
│ Headline de sucesso + resumo           │
├────────────────────────────────────────┤
│ [VALIDAÇÃO]                            │
│ Reforço da decisão + prova social      │
├────────────────────────────────────────┤
│ [OTO - OPCIONAL]                       │
│ Oferta única especial                  │
├────────────────────────────────────────┤
│ [PRÓXIMOS PASSOS]                      │
│ 1. Email  2. Acesso  3. Começar        │
├────────────────────────────────────────┤
│ [COMUNIDADE]                           │
│ Link do grupo + regras                 │
├────────────────────────────────────────┤
│ [QUICK WIN]                            │
│ Algo para fazer agora                  │
├────────────────────────────────────────┤
│ [SUPORTE]                              │
│ Contato se precisar de ajuda           │
└────────────────────────────────────────┘
```

### Step 9: Quality Check
```
Verificar página:

CONFIRMAÇÃO
- [ ] Fica claro que a compra foi confirmada?
- [ ] Resumo do pedido presente?
- [ ] Próximos passos claros?

EMOÇÃO
- [ ] Tom é acolhedor e positivo?
- [ ] Valida a decisão do comprador?
- [ ] Cria antecipação pelo produto?

OTO (se houver)
- [ ] Complementa a compra?
- [ ] Não bloqueia acesso?
- [ ] Fácil de recusar?
- [ ] Urgência genuína?

AÇÃO
- [ ] Comprador sabe exatamente o que fazer?
- [ ] Há quick win imediato?
- [ ] Suporte está acessível?
```

## Output

```yaml
format: markdown
sections:
  - confirmation_block
  - validation_copy
  - oto_offer (if applicable)
  - next_steps
  - community_block (if applicable)
  - complete_page
  - quality_checklist
```

## Copywriter Recommendations

| Contexto | Copywriter Ideal | Por quê |
|----------|------------------|---------|
| Thank you + OTO agressivo | Dan Kennedy | Urgência, escassez |
| Thank you premium/elegante | David Ogilvy | Tom sofisticado |
| Thank you com story | Gary Halbert | Conexão emocional |
| Thank you de curso | Frank Kern | Casual, acolhedor |
| Thank you high-ticket | Alex Hormozi | Value reinforcement |

## Page Templates

### Template 1: Confirmação Simples (Lead)
```markdown
# ✅ Você está dentro!

Parabéns, [Nome]! Sua inscrição foi confirmada.

## O que acontece agora:

1. **Confira seu email** — Você receberá [material] em até 5 minutos
2. **Verifique spam** — Se não encontrar, olhe na pasta de spam
3. **Adicione nosso email** — Assim garantimos que nada se perde

## Enquanto isso...

[Link para conteúdo gratuito relevante]

---

Dúvidas? Entre em contato: [email de suporte]

Bem-vindo(a)! 🎉
```

### Template 2: Thank You + OTO
```markdown
# 🎉 Compra Confirmada!

Parabéns! Você agora tem acesso ao [Produto].

**Resumo do pedido:**
- Produto: [Nome]
- Investimento: R$[valor]
- Acesso: [como/quando]

---

## ⚡ ESPERA! Oferta única para novos membros

Como você acabou de entrar, quero te fazer uma oferta especial:

### [Nome do Upsell]

[2-3 linhas sobre o upsell]

✓ [Benefício 1]
✓ [Benefício 2]
✓ [Benefício 3]

**De R$[preço original] → Apenas R$[preço OTO]**

⏰ Esta oferta expira em: [TIMER]

[BOTÃO: Sim, adicionar por R$X!]

[Link: Não, obrigado. Quero só meu acesso.]

---

## Próximos Passos:

1. Confira o email com seus dados de acesso
2. Entre na área de membros
3. Comece pelo [módulo/ação]
4. Entre no grupo exclusivo: [link]

Bem-vindo(a) à [comunidade/produto]! 🚀
```

### Template 3: Thank You com Onboarding
```markdown
# 🎊 Bem-vindo(a) ao [Produto]!

[Nome], sua jornada começa agora.

Você fez uma excelente escolha. [Produto] já ajudou [X] pessoas a [resultado].

---

## 🎬 Comece por aqui:

### Passo 1: Acesse a área de membros
→ [Link para login]
→ Login: [email]
→ Senha: [enviada por email]

### Passo 2: Assista o vídeo de boas-vindas
[Video embed ou link]

### Passo 3: Complete seu primeiro módulo
Recomendamos: "[Nome do Módulo 1]"

### Passo 4: Entre na comunidade
→ [Link do grupo]
→ Se apresente usando: [formato sugerido]

---

## ✅ Seu checklist de início:

- [ ] Acessar área de membros
- [ ] Assistir vídeo de boas-vindas
- [ ] Completar Módulo 1
- [ ] Entrar no grupo
- [ ] Fazer primeira [ação]

---

## Precisa de ajuda?

📧 Email: [suporte]
💬 Chat: [link]
📱 WhatsApp: [número]

Estamos aqui para garantir seu sucesso! 💪
```

### Template 4: Thank You + Referral
```markdown
# ✨ Parabéns pela sua compra!

Você agora faz parte de um grupo seleto de [avatares] que decidiram [transformação].

---

## Seu acesso está confirmado!

Em até [tempo] você receberá um email com:
- Dados de login
- Guia de início rápido
- Link da comunidade

---

## 🎁 Indique e ganhe!

Amou o [produto]? Compartilhe com amigos!

**Seu link exclusivo:**
[Link de referência único]

**Sua recompensa:**
- 1 indicação = [benefício 1]
- 3 indicações = [benefício 2]
- 5 indicações = [benefício 3]

[BOTÕES: WhatsApp | Telegram | Copiar Link]

---

## Compartilhe sua conquista:

"Acabei de investir no meu [área] com [Produto]! 🚀"

[Botões de compartilhamento social]

---

Bem-vindo(a)! 🎉
```

## Metrics to Track

```yaml
thank_you_metrics:
  oto_conversion: "% que aceita OTO"
  community_join: "% que entra na comunidade"
  quick_win_completion: "% que completa ação inicial"
  support_tickets: "Tickets abertos após thank you (menor = melhor)"
  refund_rate: "Taxa de reembolso (thank you bom reduz)"
```

---

*Task Version: 1.0*
*Primary Framework: Reinforcement + OTO (Dan Kennedy/Russell Brunson)*
