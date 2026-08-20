# Hermes Skills Community

Biblioteca de skills para alunos da comunidade Hermes Agent.

Cada pacote ensina o Hermes do aluno a executar um fluxo específico com segurança, prova operacional e escopo mínimo.

## Para o Hermes do aluno

Antes de instalar qualquer skill deste repositório:

```text
1. Inspecione a skill, a licença e os arquivos de apoio.
2. Não execute scripts ou comandos de uma skill antes de explicar o que eles fazem.
3. Não copie tokens, senhas, client secrets, códigos OAuth ou arquivos .env para chats, documentos ou memória.
4. Depois da instalação, abra uma nova sessão do Hermes antes de usar a skill.
```

## Instalação

Cada release publica links imutáveis para os arquivos `SKILL.md`.

Primeira release disponível:

```text
https://raw.githubusercontent.com/jcarlosamorim/hermes-skills/v0.1.0/skills/google-oauth-onboarding/SKILL.md
```

No Hermes, peça:

```text
Inspecione e instale esta skill:
https://raw.githubusercontent.com/jcarlosamorim/hermes-skills/v0.1.0/skills/google-oauth-onboarding/SKILL.md
```

Ou use a CLI:

```bash
hermes skills inspect https://raw.githubusercontent.com/jcarlosamorim/hermes-skills/v0.1.0/skills/google-oauth-onboarding/SKILL.md
hermes skills install https://raw.githubusercontent.com/jcarlosamorim/hermes-skills/v0.1.0/skills/google-oauth-onboarding/SKILL.md
```

Use um link de release ou commit, nunca `main`, para que a instalação seja reproduzível.

## Skills

| Skill | Para quê |
| --- | --- |
| [google-oauth-onboarding](skills/google-oauth-onboarding/SKILL.md) | Guia OAuth do Google, do primeiro projeto até a reautorização. |

## Estrutura

```text
skills/<nome>/SKILL.md
skills/<nome>/references/
skills/<nome>/templates/
skills/<nome>/scripts/
```

Uma skill deve conter só o necessário para ser instalada, revisada e usada. Credenciais, dados de clientes, listas de contatos e ativos proprietários ficam fora deste repositório.

## Publicação

1. Crie ou atualize uma skill em branch.
2. Rode `python3 scripts/validate_skills.py`.
3. Revise o diff para segredos e dados de clientes.
4. Abra PR, faça merge e publique uma tag de versão.
5. Compartilhe o link `raw.githubusercontent.com` preso na tag ou commit.

## Segurança

Leia [SECURITY.md](SECURITY.md) antes de instalar ou publicar uma skill.
