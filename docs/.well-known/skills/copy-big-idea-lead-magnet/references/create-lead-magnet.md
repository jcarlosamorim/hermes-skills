# Create Lead Magnet Task

## Purpose
Criar copy para lead magnets (iscas digitais) que convertem visitantes em leads qualificados.

## Inputs

```yaml
required:
  - lead_magnet_type: ebook | checklist | template | video | webinar | quiz | calculator | swipe_file
  - topic: Tema do lead magnet
  - target_avatar: Público-alvo
  - main_problem: Problema que resolve

optional:
  - next_offer: Produto que será vendido depois
  - urgency: Se há limite de tempo
  - delivery_method: Email | página de obrigado | ambos
  - copywriter_preference: Estilo preferido
```

## Lead Magnet Types

### 1. Ebook/Guide
```yaml
ideal_for: Educação profunda
length: 10-50 páginas
conversion: Alta percepção de valor
example: "O Guia Definitivo para [RESULTADO]"
```

### 2. Checklist
```yaml
ideal_for: Ação rápida
length: 1-3 páginas
conversion: Alta (fácil de consumir)
example: "Checklist de [NÚMERO] Passos para [RESULTADO]"
```

### 3. Template/Swipe File
```yaml
ideal_for: Economia de tempo
length: Varia
conversion: Muito alta (valor imediato)
example: "[NÚMERO] Templates de [TÓPICO] Prontos para Usar"
```

### 4. Video Training
```yaml
ideal_for: Demonstração
length: 10-30 minutos
conversion: Alta (engajamento)
example: "Masterclass: Como [RESULTADO] em [TEMPO]"
```

### 5. Quiz/Assessment
```yaml
ideal_for: Segmentação
length: 5-15 perguntas
conversion: Muito alta (interativo)
example: "Descubra Seu [TIPO/PERFIL] em [TEMPO]"
```

### 6. Calculator/Tool
```yaml
ideal_for: Valor tangível
length: N/A
conversion: Alta (utilidade)
example: "Calculadora de [MÉTRICA]"
```

## Landing Page Structure

### Above the Fold
```markdown
# [HEADLINE - Benefício principal]

[SUBHEADLINE - Especifica ou qualifica]

[IMAGEM/MOCKUP do lead magnet]

[FORM - Nome + Email]
[BOTÃO - CTA específico]
```

### Below the Fold (opcional)
```markdown
## O Que Você Vai Aprender/Receber

- ✅ [Benefício 1]
- ✅ [Benefício 2]
- ✅ [Benefício 3]

## Para Quem É

- [Avatar ideal]
- [Situação específica]

## Sobre [VOCÊ/EMPRESA]

[Mini bio - credibilidade]
```

## Headline Formulas for Lead Magnets

### Template/Checklist Headlines
```
- "Checklist de [NÚMERO] Pontos para [RESULTADO]"
- "[NÚMERO] Templates de [TÓPICO] (Copie e Use)"
- "O [ADJETIVO] Checklist para Nunca Esquecer [AÇÃO]"
```

### Ebook/Guide Headlines
```
- "O Guia [DEFINITIVO/COMPLETO] para [RESULTADO]"
- "Como [RESULTADO] - O Manual Passo-a-Passo"
- "[NÚMERO] Segredos de [AUTORIDADE] para [RESULTADO]"
```

### Video Headlines
```
- "Masterclass Gratuita: [RESULTADO] em [TEMPO]"
- "[NÚMERO] Minutos para Dominar [TÓPICO]"
- "Workshop: De [ANTES] para [DEPOIS]"
```

### Quiz Headlines
```
- "Descubra Seu [TIPO] de [TÓPICO]"
- "Qual [PERFIL] Você É? (Quiz de [TEMPO])"
- "Avaliação: Seu [MÉTRICA] Score"
```

## CTA Variations

### Download-focused
```
- "Baixar Agora (Grátis)"
- "Quero Meu [LEAD MAGNET]"
- "Enviar Para Meu Email"
```

### Access-focused
```
- "Acessar Gratuitamente"
- "Quero Acesso Imediato"
- "Liberar Meu Acesso"
```

### Action-focused
```
- "Começar Agora"
- "Quero [RESULTADO]"
- "Sim, Quero [BENEFÍCIO]"
```

## Thank You Page Copy

```markdown
# 🎉 Pronto! Seu [LEAD MAGNET] Está a Caminho!

Enviamos para [EMAIL] - verifique sua caixa de entrada (e spam, por via das dúvidas).

## Enquanto Isso...

[SOFT PITCH para próximo passo - video, oferta tripwire, agendar call]

---

*Tem alguma dúvida? Responda o email de entrega.*
```

## Email de Entrega

```markdown
Subject: Seu [LEAD MAGNET] chegou! 🎁

[NOME],

Prometido é prometido - aqui está seu [LEAD MAGNET]:

👉 [LINK DE DOWNLOAD]

[1-2 parágrafos sobre como usar/próximos passos]

Qualquer dúvida, é só responder este email.

[ASSINATURA]

PS: [SOFT PITCH - próximo conteúdo ou oferta]
```

## Output Deliverables

```yaml
deliverables:
  - landing_page_copy:
      - headline (+ 3 variações)
      - subheadline
      - bullet_points
      - cta_button
      - mini_bio (se necessário)
  - thank_you_page_copy
  - delivery_email
  - lead_magnet_title (+ variações)
  - follow_up_sequence_outline (3 emails)
```

## Quality Checklist

- [ ] Headline promete benefício específico
- [ ] Lead magnet resolve problema real
- [ ] Value proposition clara em <10 segundos
- [ ] CTA específico e action-oriented
- [ ] Forma pede mínimo necessário
- [ ] Thank you page tem próximo passo
- [ ] Email de entrega prepara para venda

---

*Task Version: 1.0*
