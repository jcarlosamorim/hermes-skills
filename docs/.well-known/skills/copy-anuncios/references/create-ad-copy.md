# Create Ad Copy Task

## Purpose
Criar anúncios de alta conversão para Facebook, Instagram, Google, e outras plataformas.

## Inputs

```yaml
required:
  - platform: facebook | instagram | google | youtube | tiktok | linkedin
  - objective: awareness | traffic | leads | sales
  - product_name: Produto/serviço
  - target_audience: Público-alvo
  - hook: Gancho principal (ou pedir sugestões)

optional:
  - budget: Orçamento diário
  - existing_ads: Anúncios anteriores (para melhorar)
  - competitor_reference: Anúncios de concorrentes
  - tone: Tom desejado
  - copywriter_preference: Estilo preferido
```

## Platform Specifications

### Facebook/Instagram Feed
```yaml
primary_text: 125 chars (antes de "ver mais")
headline: 40 chars
description: 30 chars
image_ratio: 1:1 ou 4:5
```

### Facebook/Instagram Stories
```yaml
text_overlay: Mínimo possível
duration: 15 segundos
vertical: 9:16
cta_placement: Bottom
```

### Google Search
```yaml
headlines: 3x 30 chars cada
descriptions: 2x 90 chars cada
display_url: 15 chars path
```

### YouTube
```yaml
hook: 5 segundos (antes do skip)
script: 30-60 segundos
cta: Verbal + visual
```

### TikTok
```yaml
hook: 1-3 segundos
duration: 15-60 segundos
style: Nativo, não "ad"
trending_sounds: Considerar
```

### LinkedIn
```yaml
intro_text: 150 chars (antes de "ver mais")
headline: 70 chars
tone: Profissional mas humano
```

## Ad Frameworks

### PAS (Problem-Agitate-Solution)
```
[PROBLEMA] Você está lutando com X?
[AGITAÇÃO] E toda vez que tenta, Y acontece...
[SOLUÇÃO] Descobri um método que...
[CTA] Clique para saber mais
```

### AIDA (Attention-Interest-Desire-Action)
```
[ATENÇÃO] Hook visual/verbal
[INTERESSE] Benefício específico
[DESEJO] Prova/resultado
[AÇÃO] CTA claro
```

### BAB (Before-After-Bridge)
```
[ANTES] Sua situação atual
[DEPOIS] Onde você quer estar
[PONTE] Como nosso produto te leva lá
```

### 4Ps (Picture-Promise-Prove-Push)
```
[PICTURE] Pinte o cenário
[PROMISE] Faça a promessa
[PROVE] Mostre prova
[PUSH] Empurre para ação
```

## Copywriter Styles for Ads

### Claude Hopkins Style
- Headline com benefício específico
- Números e dados
- Oferta clara
- Testável A/B

### Dan Kennedy Style
- Urgência imediata
- Escassez real
- CTA agressivo
- Direct response puro

### David Ogilvy Style
- Elegante e factual
- Long-form quando apropriado
- Credibilidade primeiro
- Brand + response

### Frank Kern Style
- Casual e autêntico
- Storytelling curto
- "Cara, você precisa ver isso"
- Native feel

## Hook Formulas

### Curiosity Hooks
- "Ninguém te contou isso sobre [TÓPICO]"
- "O erro de R$X que você está cometendo"
- "Por que [CRENÇA COMUM] está errado"

### Result Hooks
- "[RESULTADO] em [TEMPO] - sem [OBJEÇÃO]"
- "Como [AVATAR] conseguiu [RESULTADO]"
- "De [ANTES] para [DEPOIS] em [TEMPO]"

### Question Hooks
- "Você comete esse erro com [TÓPICO]?"
- "Quer [RESULTADO] mesmo [OBJEÇÃO]?"
- "Sabe por que [PROBLEMA] acontece?"

### Story Hooks
- "Eu estava [SITUAÇÃO] quando..."
- "3 anos atrás eu [PROBLEMA]..."
- "Meu cliente [NOME] tinha [PROBLEMA]..."

## Output Format

```yaml
per_ad:
  - platform
  - hook (+ 2 variações)
  - primary_text
  - headline
  - description (se aplicável)
  - cta_button
  - image_direction (sugestão visual)
  - audience_suggestion
  - a_b_test_recommendation
```

## Deliverables

```
Para cada plataforma solicitada:
- 3 variações de hook
- Copy completo formatado
- Sugestões de imagem/vídeo
- Recomendações de segmentação
- Métricas para acompanhar
```

## Quality Checklist

- [ ] Hook prende em <3 segundos
- [ ] Benefício claro e específico
- [ ] Copy adequado ao platform (caracteres, tom)
- [ ] CTA impossível de ignorar
- [ ] Imagem e copy se complementam
- [ ] Segmentação alinhada com avatar
- [ ] Tracking configurável

---

*Task Version: 1.0*
