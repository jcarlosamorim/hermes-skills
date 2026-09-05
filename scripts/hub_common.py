"""Constantes e funções que o gerador (mmos/outputs/hermes-hub/build_hub.py) e os scripts deste repo compartilham.

Uma fonte só para: tag/commit do Hermes de referência, URLs base, limite da description, skills que exigem
terminal e o texto de ativação da versão colável. O gerador importa este módulo pelo caminho do repo.
"""
from __future__ import annotations

HERMES_VERSION = "0.20.6"
HERMES_TAG = "v2026.8.27"                                            # a versão medida na instância de referência em 2026-08-31
HERMES_SHA = "5fc308a70719a83cccdbba4c0e39c23f5a8239d5"             # commit da tag: a tag pode ser movida, o commit não
GUARD_SHA256 = "e99c4b7967474ba7a5a29109717b00aa21f1d4535f52fe3df2771aa203156ce6"  # tools/skills_guard.py nesse commit

REPO_SLUG = "AgentsFlix/hermes-skills"                               # transferido de jcarlosamorim em 05/09/2026; o GitHub redireciona o slug antigo
WELLKNOWN = "https://agentsflix.github.io/hermes-skills"             # host técnico: catálogo, .well-known, coláveis
HUB_URL = "https://agentsflix.ai"                                     # a página (agentflix.nexialismo.ai redireciona para cá)

DESC_MAX = 200                                                        # Claude.ai rejeita description maior; `hermes skills search` lê os primeiros chars
RUNTIME_ONLY = {"ads-otimizar", "hybrid-etl"}                         # exigem terminal e rede: só onde há máquina (Hermes, Claude Code, Codex)


def cap200(desc: str) -> str:
    """Normaliza espaços e corta na última palavra inteira antes de DESC_MAX, com reticência."""
    desc = " ".join(desc.split())
    return desc if len(desc) <= DESC_MAX else desc[:DESC_MAX].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def activation_text(slug: str, trig: str) -> str:
    """Texto que o usuário cola nas instruções de um Projeto (ChatGPT/Claude) para a versão colável funcionar."""
    return (f"Você tem no arquivo `{slug}.md` uma skill chamada {slug}. Quando eu pedir algo como \"{trig}\", siga o `## Procedure` desse arquivo à risca, "
            f"use as seções `Referência:` dele no lugar dos arquivos que ele cita, e termine pela `## Verification`. Se faltar informação, pergunte antes de escrever.")
