---
version: "1.0"
date: "2026-03-09"
author:
  agent: "squad-chief"
  squad: "copy"
aios: true
project: "opb-corp"
---

# Task: Create Artifact from KB — Geração de Artefato via Knowledge Base

## Task Anatomy

| Campo | Valor |
|-------|-------|
| task_name | create-artifact-from-kb |
| status | active |
| responsible_executor | agent identificado pelo gap detection |
| execution_type | autonomous |
| elicit | false (já aprovado pelo usuário em self-improve) |

## Objetivo

Gerar um artefato (template, checklist, workflow, SOP) usando os frameworks
reais do KB de um agente. O artefato é criado PELO agente que domina o assunto,
não genericamente.

## Input

```yaml
creation_request:
  artifact_id: "{id from artifact-capability-map}"
  artifact_type: "{template | checklist | workflow | sop}"
  artifact_name: "{display name}"
  agent: "{agent-name}"
  source_frameworks: ["{fw1}", "{fw2}", "{fw3}"]
  kb_path: "squads/copy/data/books/{agent}/frameworks_inventory.yaml"
  output_path: "squads/copy/{templates|checklists|workflows}/{artifact_id}.md"
```

## Execution Flow

### Step 1: Load Agent KB
```
Read: squads/copy/data/books/{agent}/frameworks_inventory.yaml
Extract: source_frameworks listados no creation_request
```

### Step 2: Activate Agent
```
Ativar: /copy:agents:{agent-name}
Instrução: "Usando seus frameworks {fw1, fw2, fw3}, crie um {type} para {channel}.
O artefato deve refletir SUA metodologia — não genérica.
Incluir: structure, steps, quality criteria, examples."
```

### Step 3: Generate Artifact

**Se template:**
```markdown
---
version: "1.0"
date: "{today}"
author:
  agent: "{agent-name}"
  squad: "copy"
generated_from:
  kb: "squads/copy/data/books/{agent}/frameworks_inventory.yaml"
  frameworks: ["{fw1}", "{fw2}", "{fw3}"]
tags: ["{tag1}", "{tag2}"]
---

# Template: {name}

## Baseado em: {frameworks}

{conteúdo gerado pelo agent usando seus frameworks}
```

**Se checklist:**
```markdown
---
version: "1.0"
date: "{today}"
author:
  agent: "{agent-name}"
  squad: "copy"
generated_from:
  kb: "squads/copy/data/books/{agent}/frameworks_inventory.yaml"
  frameworks: ["{fw1}", "{fw2}", "{fw3}"]
tags: ["{tag1}", "{tag2}"]
---

# Checklist: {name}

## Baseado em: {frameworks}

{items derivados dos frameworks do agent}
```

**Se workflow:**
```yaml
---
version: "1.0"
date: "{today}"
author:
  agent: "{agent-name}"
  squad: "copy"
generated_from:
  kb: "squads/copy/data/books/{agent}/frameworks_inventory.yaml"
  frameworks: ["{fw1}", "{fw2}", "{fw3}"]
tags: ["{tag1}", "{tag2}"]
---

# Workflow: {name}
# phases derivadas dos SOPs/frameworks do agent
```

### Step 4: Save & Register

1. Salvar artefato no path correto (`templates/`, `checklists/`, `workflows/`)
2. Atualizar `config.yaml` → components section com novo arquivo
3. Log: "Artefato {name} criado por {agent} usando {N} frameworks"

## Quality Gate

O artefato gerado DEVE:
- [ ] Referenciar frameworks source no header (`generated_from`)
- [ ] Ter tags corretas para gap detection futura
- [ ] Refletir a metodologia do agent (não ser genérico)
- [ ] Ser funcional (usável imediatamente na próxima produção)
- [ ] Seguir o formato padrão do squad (metadata header Hybrid)

## Veto Conditions

- NÃO criar artefato sem carregar o KB do agent primeiro
- NÃO criar artefato genérico que não usa frameworks — deve ter `generated_from`
- NÃO sobrescrever artefato existente sem confirmação
- NÃO criar se agent tem menos de 3 frameworks relevantes para o artefato

## Output

```yaml
creation_result:
  artifact_id: "{id}"
  artifact_path: "{path}"
  agent: "{agent-name}"
  frameworks_used: ["{fw1}", "{fw2}", "{fw3}"]
  tags: ["{tag1}", "{tag2}"]
  status: "created"
```

## Handoff

→ Copy Chief registra no config.yaml → artefato disponível para próxima produção
