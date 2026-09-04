# AgentFlix · Hub de Skills para agentes

Skills instaláveis por comando no [Hermes Agent](https://github.com/NousResearch/hermes-agent): copy,
lançamento, processos (SOP), o **Hybrid Workspace** do seu negócio, operação de time e tráfego pago. Cada skill é um procedimento com verificação, não um prompt.
Código aberto, licença MIT, escaneado pelo mesmo scanner que o Hermes roda na instalação.

**Página do catálogo:** https://jcarlosamorim.github.io/hermes-skills/ (clique num card, copie o comando)

## Instalar

Dois caminhos, do mesmo repositório:

```bash
# 1) o hub inteiro como fonte: descobre, busca e atualiza. Lê o branch main.
hermes skills tap add jcarlosamorim/hermes-skills
hermes skills search copy
hermes skills install jcarlosamorim/hermes-skills/skills/copy-headlines

# 2) uma skill presa numa tag: é o que dá aula reproduzível, todo mundo instala o mesmo arquivo.
hermes skills install https://raw.githubusercontent.com/jcarlosamorim/hermes-skills/v0.2.0/skills/copy-headlines/SKILL.md
```

Ou cole no chat do seu Hermes:

```text
Inspecione e instale esta skill:
https://raw.githubusercontent.com/jcarlosamorim/hermes-skills/v0.2.0/skills/copy-headlines/SKILL.md
Antes de instalar, leia a licença, o SKILL.md e qualquer arquivo de apoio.
Não execute scripts nem forneça credenciais sem explicar antes o que acontecerá.
```

Depois de instalar, abra uma nova sessão.

## O que tem aqui

| linha | skills | o que instala |
|---|---|---|
| **Por objetivo** | `copy-headlines`, `copy-sales-page`, `copy-oferta`, `copy-email`, `copy-anuncios`, `copy-vsl-webinar`, `copy-vendas-por-chamada`, `copy-pesquisa-avatar`, `copy-big-idea-lead-magnet`, `copy-voz`, `copy-auditoria`, `copy-pipeline`, `copy-lancamento` | a peça que você precisa, com as fórmulas dos copywriters por trás em `references/`; `copy-lancamento` traz PLF, Brunson e soap opera |
| **Lendas do copy** | `copy-metodo-halbert`, `-ogilvy`, `-schwartz`, `-hopkins`, `-kennedy`, `-bencivenga`, `-sugarman`, `-kern`, `-benson`, `-sethi`, `-hormozi`, `-koe`, `-khayat`, `-brown` | o método de um copywriter, com frameworks e voz documentados |
| **Hybrid Workspace** | `hybrid-diagnostico`, `hybrid-proxima-acao`, `hybrid-perfil`, `hybrid-fundador`, `hybrid-icp`, `hybrid-marca`, `hybrid-oferta`, `hybrid-cultura`, `hybrid-time`, `hybrid-tech`, `hybrid-etl` | o negócio descrito em YAML, numa pasta sua: elicitação com gate de 85%, sete diagnósticos e a próxima melhor ação |
| **Processos** | `sop-extrair`, `sop-criar`, `sop-auditar` | SOP da cabeça de quem faz para o papel, para o agente, e pela auditoria (Gawande, Toyota, ISO 9001) |
| **Operação** | `ops-rotear-tarefa`, `ops-briefing`, `ops-revisao-semanal`, `ops-avaliar-fit` | gestão de time por zona de genialidade e Kolbe; o perfil do SEU time é a entrada |
| **Tráfego** | `ads-gate-compliance`, `ads-plano`, `ads-otimizar`, `ads-pesquisa`, `ads-criativos`, `ads-tracking` | régua de compliance, unit economics, o motor diário que lê a Graph API, pesquisa em 5 fases, análise de criativos e auditoria de tracking. Nada aqui escreve na plataforma |
| **Base** | `google-oauth-onboarding` | autorização OAuth do Google com escopo mínimo |

Cada skill segue o formato do Hermes: frontmatter, `When to Use`, `Quick Reference`, `Procedure`,
`Pitfalls`, `Verification` com critério binário, e `references/` para o que é longo. Segredo vai em
`required_environment_variables` (`.env`), nunca no corpo.

## Segurança

Este repositório é `community` para o Hermes, por definição (só quatro organizações são `trusted`).
Em `community`, qualquer achado `high` ou `critical` do scanner bloqueia a instalação, e `critical`
não aceita `--force`. O CI roda o scanner real do Hermes (`tools/skills_guard.py`, tag pinada) em
todo PR e reprova o build antes de chegar em alguém. Leia [SECURITY.md](SECURITY.md).

Não ensine `--force` a ninguém. Se uma skill foi bloqueada, o problema é dela.

## Estrutura

```text
skills/<nome>/SKILL.md          procedimento; único arquivo que o loader lê de início
skills/<nome>/references/       fórmulas, métodos, checklists (carregados sob demanda)
skills/<nome>/templates/        modelos que a skill preenche
skills/<nome>/scripts/          código determinístico (só no ads-otimizar)
catalog.json                    o catálogo que a página lê: título, sinopse, comando, gênero
docs/                           a página (GitHub Pages) e o .well-known/skills para busca por domínio
scripts/validate_skills.py      forma do SKILL.md
scripts/scan_skills.py          scanner do Hermes contra cada skill
scripts/build_docs.py           regenera docs/ a partir de skills/ e catalog.json
```

## Publicar uma mudança

1. Branch. Edite ou crie `skills/<nome>/`.
2. `python3 scripts/validate_skills.py && python3 scripts/scan_skills.py` (Python 3.10+).
3. `python3 scripts/build_docs.py` e confira o diff em `docs/`.
4. PR. O CI repete os dois primeiros passos.
5. Merge em `main` (o tap passa a ver) e **tag** (`vX.Y.Z`): os comandos da página apontam para a tag.

## Origem

As skills de copy nasceram do squad `copywriter-os` e as de operação do `nucleo-ops-ia`, do
[Synkra AIOS](https://github.com/SynkraAI/aios-core); o motor de tráfego é o `outputs/meta-ads`. A página do catálogo se chama AgentFlix: marca própria, para não depender do nome de um produto de terceiro. Na v0.3
entraram os squads da imersão (`aiox-copy`, `aiox-sop`, `aiox-workspace`, rebatizado Hybrid Workspace, e
a parte de leitura do `aiox-ads`). Os arquivos de agente e task foram levados para `references/` como
conhecimento, não como persona; caminhos do filesystem de origem viraram uma pasta configurável
(`hybrid.pasta`, `ops.perfis_do_time`); dados de participantes e o que muta plataforma ficaram fora. As
capas da página seguem o padrão de key art da Netflix e são geradas a partir de prompts versionados.

Licença MIT. Autor: José Carlos Amorim.
