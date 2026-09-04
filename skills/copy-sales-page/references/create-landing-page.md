# Create Landing Page Task

## Purpose
Criar landing pages de captura de alta conversão para geração de leads.

## Inputs

```yaml
required:
  - page_goal: lead_capture | webinar_registration | waitlist | quiz | demo_request
  - offer: O que pessoa recebe (lead magnet, acesso, etc.)
  - target_avatar: Público-alvo
  - main_benefit: Benefício principal

optional:
  - traffic_source: paid_ads | organic | email | social
  - urgency: Se há limite de tempo/vagas
  - social_proof: Números, logos, testimonials
  - copywriter_preference: Estilo preferido
```

## Landing Page Types

### 1. Lead Magnet Page
```yaml
goal: Capturar email em troca de conteúdo
elements: headline, bullet_points, form, cta
conversion: 20-50%
```

### 2. Webinar Registration
```yaml
goal: Inscrições para webinar
elements: headline, date/time, speaker_bio, form, cta
conversion: 30-50%
```

### 3. Waitlist Page
```yaml
goal: Construir lista de espera
elements: headline, teaser, form, cta
conversion: 40-60%
```

### 4. Quiz/Assessment
```yaml
goal: Engajamento + segmentação
elements: headline, quiz_preview, start_button
conversion: 50-70%
```

### 5. Demo/Call Request
```yaml
goal: Agendar demonstração ou call
elements: headline, benefits, form, calendar_embed
conversion: 5-20%
```

## Page Structure

### Squeeze Page (Mínimo Viável)
```markdown
# [HEADLINE - Benefício principal]

[IMAGEM/MOCKUP do que recebe]

[FORM]
- Email (obrigatório)
- Nome (opcional)

[BOTÃO CTA]
```

### Standard Landing Page
```markdown
# [HEADLINE - Benefício principal]

## [SUBHEADLINE - Especifica ou qualifica]

[IMAGEM/VIDEO]

### O Que Você Vai Receber/Aprender:

- ✅ [Benefício 1]
- ✅ [Benefício 2]
- ✅ [Benefício 3]

[FORM]

[BOTÃO CTA]

---

### Social Proof
[Números, logos, mini-testimonials]

### Sobre [VOCÊ]
[Mini bio + foto]
```

### Long-Form Landing Page
```markdown
# [HEADLINE]

## [SUBHEADLINE]

[HERO IMAGE/VIDEO]

---

## O Problema

[Descreva a dor do avatar]

## A Solução

[Como seu offer resolve]

## O Que Você Recebe

[Detalhamento do valor]

## Para Quem É

[Qualificação do avatar]

## Social Proof

[Testimonials, números, logos]

## FAQ

[Perguntas comuns]

---

[FORM + CTA]
```

## Headline Formulas

### Benefit-Focused
```
- "Como [RESULTADO] em [TEMPO]"
- "[NÚMERO] Maneiras de [BENEFÍCIO]"
- "O Guia Completo para [RESULTADO]"
```

### Curiosity-Focused
```
- "O Segredo de [AUTORIDADE] para [RESULTADO]"
- "Por Que [CRENÇA COMUM] Está Errado"
- "O Que [EXPERTS] Não Querem Que Você Saiba"
```

### Webinar-Specific
```
- "Masterclass Gratuita: [RESULTADO] em [TEMPO]"
- "Workshop Ao Vivo: [TEMA]"
- "Treinamento: Como [RESULTADO] (Mesmo Se [OBJEÇÃO])"
```

### Waitlist-Specific
```
- "Seja o Primeiro a Saber Quando [PRODUTO] Lançar"
- "Lista VIP: Acesso Antecipado a [PRODUTO]"
- "Entre na Lista de Espera para [BENEFÍCIO]"
```

## Form Optimization

### Minimum Fields (Higher Conversion)
```
- Email only: 40-60% conversion
- Email + First Name: 30-50% conversion
```

### Additional Fields (Lower Conversion, Better Leads)
```
- + Phone: -10-20% conversion
- + Company: -10-15% conversion
- + Role: -5-10% conversion
```

### Field Labels
```
❌ "Email Address"
✅ "Seu melhor email"

❌ "First Name"
✅ "Como posso te chamar?"

❌ "Submit"
✅ "Quero Meu [LEAD MAGNET]"
```

## CTA Button Copy

### Download CTAs
```
- "Baixar Agora (Grátis)"
- "Quero Meu [NOME DO LEAD MAGNET]"
- "Enviar Para Meu Email"
```

### Registration CTAs
```
- "Reservar Minha Vaga"
- "Quero Participar (Grátis)"
- "Garantir Meu Lugar"
```

### Waitlist CTAs
```
- "Entrar na Lista VIP"
- "Me Avise Quando Lançar"
- "Quero Acesso Antecipado"
```

## Copywriter Styles

### David Ogilvy Style
```
- Elegante e profissional
- Headline com benefício específico
- Copy informativo
- Credibilidade através de fatos
```

### Dan Kennedy Style
```
- Urgência (vagas limitadas)
- Bullet points agressivos
- CTA direto
- Escassez real
```

### Frank Kern Style
```
- Casual e autêntico
- "Cara, você precisa ver isso"
- Storytelling curto
- Zero hype
```

## Output Deliverables

```yaml
deliverables:
  - landing_page_copy:
      - headline (+ 3 variações)
      - subheadline
      - body_copy
      - bullet_points
      - cta_button (+ 2 variações)
      - form_fields_recommendation
  - above_fold_mockup_description
  - thank_you_page_copy
  - confirmation_email
```

## Quality Checklist

- [ ] Headline comunica benefício em <3 segundos
- [ ] Uma única ação clara (sem distrações)
- [ ] Form pede mínimo necessário
- [ ] CTA usa linguagem de ação
- [ ] Mobile-friendly (scannable)
- [ ] Social proof presente (se disponível)
- [ ] Carregamento rápido (sem vídeo autoplay pesado)

## Conversion Optimization Tips

1. **Remove Navigation:** Zero links externos
2. **Single CTA:** Uma ação, repetida
3. **Above the Fold:** Tudo importante visível
4. **Social Proof:** Números, logos, faces
5. **Urgency:** Se genuína, destaque
6. **Mobile First:** 60%+ do tráfego é mobile

---

*Task Version: 1.0*
