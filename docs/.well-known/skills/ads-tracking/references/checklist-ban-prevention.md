# Ban Prevention Checklist

> **Enforced by:** @fiscal (Safety Officer)
> **Source:** `docs/research/2026-03-17-claude-code-meta-ads-agent-autonomy/05-meta-api-risks-bans.md` (Ban Wave 2026)
> **References:** `config/safety-rules.yaml`, `config/autonomy-tiers.yaml`
> **Story:** SAIOX-ADS-V5-1.6

Este checklist e OBRIGATORIO antes de qualquer operacao automatizada via API.
O @fiscal valida cada item; falha em item BLOCK impede operacao.

---

## Secao 1 -- Pre-Automacao (5 checks)

Validar ANTES de conectar qualquer agente a conta de ads.

---

### 1.1 Business Manager verificado + identidade confirmada

- **Descricao:** Conta de Business Manager deve estar com verificacao de identidade completa (documento + dominio). Contas nao verificadas tem prioridade BAIXA em appeals e sao flagged mais facilmente pela moderacao AI.
- **Verificacao:** Acessar Business Settings > Security Center > verificar badge "Verified". Confirmar que Identity Verification esta "Complete".
- **Severidade:** BLOCK
- **Remediacao:** Iniciar processo de verificacao em Business Settings > Security Center > Start Verification. Aguardar 2-5 dias uteis. NAO automatizar nenhuma operacao ate verificacao completa.
- **Referencia:** `05-meta-api-risks-bans.md` Secao 6 -- Protocolo de Prevencao de Bans

---

### 1.2 2FA habilitado em todas as contas conectadas

- **Descricao:** Autenticacao de dois fatores (2FA) deve estar ativa em TODAS as contas pessoais conectadas ao Business Manager. Meta flagga contas sem 2FA como vulneraveis e pode restringir funcionalidades.
- **Verificacao:** Acessar Settings > Security > Two-Factor Authentication em cada conta conectada. Confirmar status "On" com metodo de backup configurado.
- **Severidade:** BLOCK
- **Remediacao:** Habilitar 2FA em Settings > Security > Two-Factor Authentication. Configurar metodo primario (app authenticator recomendado) + metodo backup (SMS). Repetir para TODAS as contas conectadas.
- **Referencia:** `05-meta-api-risks-bans.md` Secao 6 -- Protocolo de Prevencao de Bans

---

### 1.3 IP fixo e consistente para chamadas API

- **Descricao:** Todas as chamadas API devem originar do mesmo IP fixo. Trocas de IP sao trigger MEDIO de ban -- o sistema de moderacao interpreta como atividade suspeita (bot em cloud/VPS).
- **Verificacao:** Confirmar IP fixo no ambiente de execucao. Verificar que IP esta documentado em `.env` ou infraestrutura. Rodar `curl ifconfig.me` e comparar com IP registrado.
- **Severidade:** BLOCK
- **Remediacao:** Configurar IP estatico (Elastic IP ou equivalente). Documentar IP em `.env`. Se em cloud, provisionar IP dedicado. Confirmar que regiao do IP e consistente com localizacao do Business Manager.
- **Referencia:** `safety-rules.yaml` -- `ip_consistency: required`; `05-meta-api-risks-bans.md` Trigger: IP inconsistente (MEDIO)

---

### 1.4 Nenhuma VPN ou proxy em uso

- **Descricao:** VPNs e proxies alteram o IP de origem e criam inconsistencia de localizacao. Mesmo VPNs com IP fixo podem ser detectadas por fingerprinting (range de IPs conhecidos de provedores VPN).
- **Verificacao:** Confirmar que VPN esta DESLIGADA no ambiente de execucao. Verificar que nao ha proxy HTTP/HTTPS configurado. Testar: `curl ifconfig.me` deve retornar IP real (nao IP de VPN).
- **Severidade:** BLOCK
- **Remediacao:** Desligar VPN antes de qualquer operacao API. Remover configuracoes de proxy do ambiente. Se VPN e necessaria para outros servicos, isolar ambiente de API em rede separada.
- **Referencia:** `safety-rules.yaml` -- `ip_consistency: required`; `05-meta-api-risks-bans.md` Secao 6

---

### 1.5 Conta com minimo 30 dias de atividade manual

- **Descricao:** Contas novas (< 30 dias) sao classificadas como "new" no tier de seguranca e requerem restricoes severas. Nao deve haver NENHUMA automacao em contas com menos de 30 dias de historico manual.
- **Verificacao:** Consultar data de criacao da conta em Business Manager > Ad Accounts > Account Info. Calcular dias desde criacao. Se < 30 dias, automacao BLOQUEADA.
- **Severidade:** BLOCK
- **Remediacao:** Aguardar ate conta atingir 30 dias com atividade manual organica (criar campanhas manualmente, fazer ajustes manuais). Apos 30 dias, iniciar automacao com restricoes de `account_age_tiers.young` do `safety-rules.yaml`.
- **Referencia:** `safety-rules.yaml` -- `account_age_tiers.new`; `05-meta-api-risks-bans.md` Secao 6; `autonomy-tiers.yaml` -- `activate-first-campaign` (Human Only para contas < 30 dias)

---

## Secao 2 -- Durante Operacao (6 checks)

Validar CONTINUAMENTE enquanto agentes estao operando.

---

### 2.1 Max +20%/dia aumento de budget

- **Descricao:** Spike de ad spend e o trigger #1 (ALTO) de ban na moderacao AI da Meta. Qualquer aumento de budget diario deve respeitar o limite de +20% sobre o valor atual. Aumentos > 20% requerem aprovacao HITL e rampagem obrigatoria.
- **Verificacao:** Antes de qualquer ajuste de budget, calcular: `(novo_budget - budget_atual) / budget_atual * 100`. Se resultado > 20%, bloquear e escalar para HITL. Verificar tambem acumulo semanal (max 50% na semana).
- **Severidade:** BLOCK
- **Remediacao:** Reduzir ajuste para <= 20%. Se aumento maior e necessario, usar rampagem: Day 1 = 25%, Day 3 = 50%, Day 7 = 100% do target. Registrar plano de rampagem no WAL com aprovacao HITL.
- **Referencia:** `safety-rules.yaml` -- `budget_thresholds.max_daily_increase_pct: 20`; `05-meta-api-risks-bans.md` Trigger: Spike de ad spend (ALTO)

---

### 2.2 Max 5 campanhas/dia (contas < 90 dias)

- **Descricao:** Criacao em massa de campanhas e trigger MEDIO de ban. Contas com menos de 90 dias tem limite de 5 novas campanhas por dia (contando campaigns, nao adsets/ads).
- **Verificacao:** Antes de criar campanha, consultar WAL para contar campanhas criadas no dia atual. Se count >= 5 e conta < 90 dias, bloquear criacao. Verificar idade da conta via `account_age_tiers` no `safety-rules.yaml`.
- **Severidade:** BLOCK
- **Remediacao:** Adiar criacao para o dia seguinte. Se urgente, avaliar consolidacao de campanhas (menos campanhas com mais adsets). Para contas mature (>= 91 dias), este limite nao se aplica mas bom senso prevalece.
- **Referencia:** `safety-rules.yaml` -- `max_campaigns_per_day_new_account: 5`; `05-meta-api-risks-bans.md` Trigger: Criacao em massa de ads (MEDIO)

---

### 2.3 Sem spike de API calls

- **Descricao:** Volume alto de chamadas API em curto periodo e trigger MEDIO de ban (padrao de bot detectado). O circuit breaker deve estar ativo e respeitando limites de rate do tier da conta.
- **Verificacao:** Monitorar consumo de pontos da API via `check-rate-limit-status` (Auto). Se consumo > 70% do limite do tier em menos de 30 minutos, desacelerar. Se HTTP 429 recebido, HALT imediato.
- **Severidade:** BLOCK (se HTTP 429 recebido) / WARN (se > 70% do limite)
- **Remediacao:** Implementar backoff exponencial. Usar Batch API para consolidar requests. Reduzir frequencia de polling. Aguardar reset do window antes de retomar. Consultar `data/rate-limits.yaml` para limites do tier.
- **Referencia:** `data/rate-limits.yaml` -- circuit breaker config; `05-meta-api-risks-bans.md` Secao 1 -- Rate Limits; Trigger: Volume alto de API calls (MEDIO)

---

### 2.4 PAUSED-by-default respeitado

- **Descricao:** TODA campanha criada via API DEVE ter status PAUSED. Ativacao e acao HITL separada. Campanhas criadas como ACTIVE sem revisao humana sao padrao bot e trigger de moderacao.
- **Verificacao:** Apos cada `create-campaign-api`, fazer GET de read-back para confirmar status == PAUSED. Se status != PAUSED, HALT imediato e registrar incidente.
- **Severidade:** BLOCK
- **Remediacao:** Se campanha foi criada como ACTIVE por erro, pausar IMEDIATAMENTE via `pause-campaign` (HITL). Investigar causa do erro (bug no template, parametro incorreto). Corrigir antes de retomar operacoes.
- **Referencia:** `safety-rules.yaml` -- `paused_by_default: true`; `autonomy-tiers.yaml` -- `create-campaign-api` constraints

---

### 2.5 Learning Phase nao interrompida

- **Descricao:** Campanhas em learning phase (< 50 conversoes no adset) sao frageis. Alteracoes durante learning phase reiniciam o processo, desperdicando budget e dados acumulados.
- **Verificacao:** Antes de qualquer alteracao em campanha ativa, verificar se adsets estao em learning phase. Acoes proibidas durante learning: alterar budget > 20%, alterar targeting, pausar > 24h, trocar criativo.
- **Severidade:** WARN (com confirmacao obrigatoria)
- **Remediacao:** Se alteracao e necessaria durante learning phase, @fiscal deve alertar: "Campanha em learning phase. Alteracao reiniciara o processo. Confirma? (APROVADO/CANCELAR)". Somente com confirmacao explicita a alteracao prossegue.
- **Referencia:** `safety-rules.yaml` -- `additional_rules.learning_phase`; `05-meta-api-risks-bans.md` contexto de triggers

---

### 2.6 Action ledger atualizado

- **Descricao:** TODA acao API (read ou write) deve ser registrada no action ledger (audit trail). O ledger e evidencia critica em caso de appeal apos ban. Sem ledger, appeal tem taxa de sucesso proxima a zero.
- **Verificacao:** Apos cada operacao, confirmar que entry foi adicionada ao WAL (para writes) e ao audit trail (para todas as acoes). Verificar que ledger nao tem gaps (timestamps sequenciais).
- **Severidade:** WARN
- **Remediacao:** Se ledger tem gaps, reconstruir a partir de logs do MCP. Se impossivel reconstruir, documentar gap com nota explicativa. Configurar alertas para falhas de logging.
- **Referencia:** `safety-rules.yaml` -- `write_ahead_log: required` e `additional_rules.audit_trail`

---

## Secao 3 -- Se Banido (5 checks)

Acoes IMEDIATAS caso conta seja restrita ou banida.

---

### 3.1 NAO criar nova conta (cascata piora)

- **Descricao:** Criar nova conta apos ban PIORA a situacao. O efeito cascata da Meta suspende TODAS as contas conectadas ao mesmo perfil. Nova conta criada pelo mesmo perfil sera imediatamente flagged.
- **Verificacao:** Confirmar que nenhum membro da equipe criou nova conta ou Business Manager como reacao ao ban. Verificar que nao houve tentativa de contornar ban com novos perfis.
- **Severidade:** BLOCK
- **Remediacao:** NAO criar nada novo. Focar 100% no processo de appeal da conta existente. Se equipe ja criou nova conta, isolar imediatamente (desconectar do perfil principal).
- **Referencia:** `05-meta-api-risks-bans.md` Secao 2 -- Efeito Cascata; Secao 6 -- "NAO criar nova conta (cascata piora)"

---

### 3.2 Appeal via Business Support Home com documentacao

- **Descricao:** O sistema de appeal da Meta e majoritariamente automatizado. Documentacao detalhada e a unica forma de diferenciar appeal de spam automatizado. Incluir: historico da conta, acoes realizadas, evidencias de legitimidade.
- **Verificacao:** Confirmar que appeal foi submetido via Business Support Home (nao via formularios genericos). Confirmar que documentacao inclui: action ledger completo, historico de atividade, evidencias de identidade verificada.
- **Severidade:** BLOCK
- **Remediacao:** Preparar pacote de documentacao: (1) Export do action ledger/WAL, (2) Screenshots de Business Manager verificado, (3) Historico de atividade manual pre-automacao, (4) Descricao das acoes automatizadas com justificativa. Submeter via Business Support Home.
- **Referencia:** `05-meta-api-risks-bans.md` Secao 2 -- Sistema de Appeal

---

### 3.3 Documentar todas as acoes automatizadas como evidencia

- **Descricao:** O action ledger e a peca central do appeal. Toda acao automatizada deve estar documentada com timestamp, parametros, e agente responsavel. Isso prova que acoes foram deliberadas e controladas, nao maliciosas.
- **Verificacao:** Exportar WAL completo do periodo relevante. Verificar que cada entry tem: timestamp, action_id, agent, entity_type, operation, params, approval, status. Sem gaps.
- **Severidade:** BLOCK
- **Remediacao:** Se WAL tem gaps, reconstruir a partir de logs do MCP e campaign state files. Formatar em documento human-readable para inclusao no appeal. Incluir nota sobre safety systems ativos (este checklist, safety-rules, autonomy-tiers).
- **Referencia:** `safety-rules.yaml` -- `write_ahead_log` e `additional_rules.audit_trail`; `autonomy-tiers.yaml`

---

### 3.4 Contato via Meta for Business rep (se disponivel)

- **Descricao:** Contas com Business Manager verificado e historico de spend significativo podem ter acesso a representante Meta. Contato direto com rep tem taxa de sucesso MUITO maior que appeal automatizado.
- **Verificacao:** Verificar se conta tem acesso a rep via Business Support Home > Chat/Call options. Se nao tem acesso direto, verificar se existe canal de parceiros ou agencia com acesso.
- **Severidade:** WARN
- **Remediacao:** Se tem acesso a rep: agendar contato com documentacao preparada (item 3.3). Se nao tem acesso: prosseguir com appeal escrito (item 3.2). Considerar parceiros/agencias com relacionamento Meta para intermediar.
- **Referencia:** `05-meta-api-risks-bans.md` Secao 2 -- Sistema de Appeal; Secao 6

---

### 3.5 Aguardar 48-72h antes de re-appeal se rejeitado

- **Descricao:** Re-appeals muito rapidos sao filtrados automaticamente como spam. O sistema da Meta precisa de tempo para processar. Re-appeals antes de 48h sao praticamente ignorados.
- **Verificacao:** Se appeal foi rejeitado, registrar data/hora da rejeicao. Calcular 48h minimas antes de re-submissao. Se segunda rejeicao, aguardar 72h.
- **Severidade:** BLOCK
- **Remediacao:** Aguardar periodo minimo. Usar o tempo para melhorar documentacao do appeal (mais evidencias, melhor formatacao). Considerar ajuda profissional (consultoria Meta Ads) se segundo appeal tambem for rejeitado.
- **Referencia:** `05-meta-api-risks-bans.md` Secao 6 -- "Aguardar 48-72h antes de re-appeal se rejeitado"

---

## Resumo de Severidades

| Severidade | Significado | Acao |
|------------|-------------|------|
| BLOCK | Operacao nao pode prosseguir | @fiscal IMPEDE execucao ate resolucao |
| WARN | Atencao necessaria | @fiscal ALERTA e requer confirmacao explicita |

**Total de checks:** 16
- Pre-automacao: 5 (todos BLOCK)
- Durante operacao: 6 (4 BLOCK, 2 WARN)
- Se banido: 5 (4 BLOCK, 1 WARN)

---

_Checklist: Ban Prevention | @hybrid-ads | Enforced by @fiscal_
_Source: Ban Wave 2026 Research (05-meta-api-risks-bans.md)_
