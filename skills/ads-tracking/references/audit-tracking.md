---
task: Audit Tracking
responsavel: '@pixel-specialist'
responsavel_type: agent
atomic_layer: task
status: active
squad: media-buyer-squad
version: 1.0.0
Entrada: |
  - website_url: URL do site para auditar
  - platform: Plataforma de ads (meta|google|both)
  - events_expected: Eventos esperados
Saida: |
  - audit_report: Relatório de auditoria
  - issues_found: Problemas encontrados
  - fixes_recommended: Correções recomendadas
Checklist:
  - '[ ] Verificar Pixel instalado'
  - '[ ] Testar eventos padrão'
  - '[ ] Verificar parâmetros'
  - '[ ] Checar CAPI status'
  - '[ ] Validar deduplicação'
  - '[ ] Testar em múltiplos navegadores'
---

# Audit Tracking Task

## Objetivo

Auditar configuração de tracking para garantir dados precisos para otimização.

## Ferramentas Necessárias

- Meta Pixel Helper (extensão Chrome)
- Meta Events Manager
- Google Tag Assistant (se Google Ads)
- Console do navegador (F12)

## Processo de Auditoria

### Step 1: Verificar Instalação Base

**Meta Pixel:**

```
1. Abrir site com Pixel Helper ativo
2. Verificar: Pixel ID correto
3. Verificar: PageView disparando
4. Verificar: Sem erros no console
```

**Status:**

- [ ] Pixel detectado
- [ ] Pixel ID correto
- [ ] Sem erros JavaScript

### Step 2: Testar Eventos do Funil

| Página        | Evento Esperado  | Disparou? | Parâmetros OK? |
| ------------- | ---------------- | --------- | -------------- |
| Produto/Venda | ViewContent      |           |                |
| Carrinho      | AddToCart        |           |                |
| Checkout      | InitiateCheckout |           |                |
| Obrigado      | Purchase/Lead    |           |                |

**Para cada evento verificar:**

- [ ] Evento dispara uma vez
- [ ] `content_type` presente
- [ ] `content_ids` presente
- [ ] `value` correto (para Purchase)
- [ ] `currency: BRL` configurado

### Step 3: Verificar CAPI

Acessar: Events Manager → Data Sources → [Pixel] → Overview

- [ ] CAPI status: Ativo
- [ ] Match rate: >50%
- [ ] Deduplicação: Configurada

**Se CAPI inativo:**
→ Recomendar setup via `*capi-setup`

### Step 4: Testar Deduplicação

```
1. Realizar conversão teste
2. Verificar no Events Manager
3. Deve aparecer UMA vez (não duplicado)
4. Verificar event_id presente
```

### Step 5: Cross-Browser Test

Testar em:

- [ ] Chrome (normal)
- [ ] Chrome (incógnito)
- [ ] Safari (iOS simulator)
- [ ] Firefox

**Atenção:** Bloqueadores podem afetar resultados

## Relatório de Auditoria

```markdown
## Tracking Audit Report

**Site:** [URL]
**Data:** [DATA]
**Auditor:** @pixel-specialist

### Status Geral: ✅ OK | ⚠️ Parcial | ❌ Crítico

### Pixel Base

- Status: ✅ Instalado
- Pixel ID: [ID]
- PageView: ✅ Funcionando

### Eventos

| Evento           | Status | Notas           |
| ---------------- | ------ | --------------- |
| ViewContent      | ✅     | Parâmetros OK   |
| AddToCart        | ⚠️     | Sem content_ids |
| InitiateCheckout | ✅     | OK              |
| Purchase         | ❌     | Não dispara     |

### CAPI

- Status: ❌ Inativo
- Match Rate: N/A
- Recomendação: Implementar CAPI

### Problemas Críticos

1. Purchase event não dispara
2. CAPI não configurado

### Ações Recomendadas

1. Corrigir Purchase event no checkout
2. Implementar CAPI via [método]
3. Adicionar content_ids no AddToCart

### Próximos Passos

→ Reportar para @media-strategist
→ Agendar correções com @dev
```

---

_Task: Audit Tracking | @pixel-specialist_
