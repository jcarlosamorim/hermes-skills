---
task: Analyze Creatives
responsavel: '@creative-analyst'
responsavel_type: agent
atomic_layer: task
status: active
squad: media-buyer-squad
version: 1.0.0
Entrada: |
  - creative_data: Métricas dos criativos
  - ad_library: Acesso aos criativos
  - period: Período de análise
Saida: |
  - creative_report: Relatório de performance de criativos
  - winners: Criativos vencedores
  - patterns: Padrões identificados
  - recommendations: Próximos testes
Checklist:
  - '[ ] Coletar métricas por criativo'
  - '[ ] Analisar hooks (primeiros 3s)'
  - '[ ] Identificar padrões vencedores'
  - '[ ] Detectar fadiga'
  - '[ ] Gerar recomendações'
---

# Analyze Creatives Task

## Objetivo

Analisar performance de criativos para identificar padrões vencedores e oportunidades.

## Métricas por Criativo

### Solicitar ao Usuário

| Criativo   | Impressões | CTR | Hook Rate | ThruPlay | CPM | CPA |
| ---------- | ---------- | --- | --------- | -------- | --- | --- |
| Video 1    |            |     |           |          |     |     |
| Video 2    |            |     |           |          |     |     |
| Image 1    |            |     |           |          |     |     |
| Carousel 1 |            |     |           |          |     |     |

### Métricas-Chave

- **CTR (Link):** Qualidade geral do criativo
- **Hook Rate:** % que assiste 3+ segundos (vídeo)
- **ThruPlay Rate:** % que assiste até o fim
- **CPM:** Qualidade percebida pelo algoritmo
- **CPA:** Resultado final

## Análise de Hooks

Para vídeos, avaliar primeiros 3 segundos:

| Criativo | Hook Type | Hook Rate | Veredicto      |
| -------- | --------- | --------- | -------------- |
| Video 1  | Problema  | 25%       | ✅ Winner      |
| Video 2  | Resultado | 12%       | ❌ Testar novo |
| Video 3  | Tutorial  | 18%       | ⚠️ OK          |

**Benchmarks Hook Rate:**

- Excelente: >25%
- Bom: 15-25%
- Fraco: <15%

## Identificar Padrões

### O que os Winners têm em comum?

```markdown
## Padrões Identificados

### Formato

- [ ] Vídeo supera imagem?
- [ ] UGC supera produzido?
- [ ] Vertical supera quadrado?

### Hook

- [ ] Qual tipo de hook performa melhor?
- [ ] Duração ideal do hook?
- [ ] Texto no início ajuda?

### Copy

- [ ] Headline curta ou longa?
- [ ] Emojis ajudam?
- [ ] CTA direto ou indireto?

### Visual

- [ ] Cores predominantes?
- [ ] Presença de rosto?
- [ ] Movimento vs estático?
```

## Detector de Fadiga

| Sinal       | Threshold      | Status |
| ----------- | -------------- | ------ |
| CTR caindo  | >20% em 7 dias | ⚠️     |
| CPM subindo | >30% em 7 dias | ⚠️     |
| Frequência  | >3.0           | ❌     |
| CPA subindo | >25% em 7 dias | ❌     |

**Se 2+ sinais:** Criativo em fadiga → Novo brief necessário

## Relatório de Criativos

```markdown
## Creative Analysis Report

**Período:** [DATA] a [DATA]
**Total Criativos:** [N]
**Analyst:** @creative-analyst

### Performance Geral

| Categoria | Quantidade | CTR Médio | Melhor     |
| --------- | ---------- | --------- | ---------- |
| Vídeo     | X          | Y%        | Video 3    |
| Imagem    | X          | Y%        | Image 2    |
| Carrossel | X          | Y%        | Carousel 1 |

### Top 3 Winners 🏆

1. **[Nome]** - CTR: X%, CPA: R$Y
   - Hook: [tipo]
   - Por que funciona: [análise]

2. **[Nome]** - CTR: X%, CPA: R$Y
   - Hook: [tipo]
   - Por que funciona: [análise]

3. **[Nome]** - CTR: X%, CPA: R$Y
   - Hook: [tipo]
   - Por que funciona: [análise]

### Bottom 3 (pausar) 🚫

1. **[Nome]** - CTR: X%, CPA: R$Y
   - Problema: [diagnóstico]

### Padrões Identificados

- Hooks de [tipo] performam 2x melhor
- UGC supera produzido em CTR
- Vídeos <30s têm melhor ThruPlay

### Recomendações

1. **Criar variações** do Winner 1 com novos hooks
2. **Pausar** Bottom 3
3. **Testar** formato [X] baseado em padrões

### Próximo Brief

→ Via `*brief` com foco em:

- Hook tipo: [recomendado]
- Formato: [recomendado]
- Ângulo: [novo a testar]
```

---

_Task: Analyze Creatives | @creative-analyst_
