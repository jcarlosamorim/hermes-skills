#!/usr/bin/env python3
"""Small offline validator for the community skill repository."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("validate_skills.py precisa de PyYAML: pip install -r requirements.txt")

from hub_common import DESC_MAX  # o mesmo limite do portable, do gerador e do validador

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

errors: list[str] = []
files = sorted(SKILLS.glob("*/SKILL.md"))
if not files:
    errors.append("no SKILL.md files found")

for path in files:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: frontmatter must start at byte zero")
        continue
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        errors.append(f"{path}: frontmatter is not closed")
        continue
    frontmatter, body = parts[1], parts[2]
    for field in ("name", "description", "version", "license"):
        if not re.search(rf"^{field}:\s*.+$", frontmatter, re.MULTILINE):
            errors.append(f"{path}: missing {field}")
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if description and len(description.group(1).strip().strip('"')) > DESC_MAX:
        errors.append(f"{path}: description must be {DESC_MAX} characters or fewer")
    if description and len(description.group(1).strip().strip('"')) < 40:
        errors.append(f"{path}: description too short to be found by skills search (min 40 chars)")
    if not re.search(r"^## When to use", body, re.MULTILINE | re.IGNORECASE) or "## Verification" not in body:
        errors.append(f"{path}: requires When to Use and Verification sections")
    # "Arquivos desta skill" é o contrato do que o Hermes copia e do que o colável embute: tudo listado tem que existir e ficar dentro da skill
    listed = re.search(r"## Arquivos desta skill\n\n((?:- `[^`]+`\n?)+)", body)
    for rel in (re.findall(r"- `([^`]+)`", listed.group(1)) if listed else []):
        if ".." in rel.split("/") or rel.startswith("/"):
            errors.append(f"{path}: arquivo listado fora da skill: {rel}")
        elif not (path.parent / rel).exists():
            errors.append(f"{path}: arquivo listado não existe: {rel}")
    # mesmos formatos que o scanner do Hermes reprova; com fronteira, para "risk-free" ou "task-" não dispararem
    if "[REDACTED]" not in text and re.search(r"(?<![A-Za-z0-9])(?:AIza[0-9A-Za-z_-]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|ntn_[A-Za-z0-9]{20,}|secret_[A-Za-z0-9]{20,})", text):
        errors.append(f"{path}: possible secret-like string")

# distribuição portable (docs/.well-known): frontmatter estrito ao spec agentskills.io e ao upload do Claude.ai
SPEC = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
for path in sorted((ROOT / "docs" / ".well-known" / "skills").glob("*/SKILL.md")):
    text = path.read_text(encoding="utf-8")
    try:
        fm = yaml.safe_load(text.split("---\n", 2)[1])
    except Exception as exc:
        errors.append(f"{path}: portable frontmatter inválido: {exc}"); continue
    extra = set(fm) - SPEC
    if extra: errors.append(f"{path}: portable com chave fora do spec: {sorted(extra)}")
    if len(fm.get("description", "")) > DESC_MAX: errors.append(f"{path}: portable description > {DESC_MAX} (Claude.ai rejeita)")
    if any(not isinstance(x, str) for x in (fm.get("metadata") or {}).values()): errors.append(f"{path}: portable metadata precisa ser string->string")
    if fm.get("name") != path.parent.name: errors.append(f"{path}: portable name != pasta")

if errors:
    print("validation=failed")
    print("\n".join(errors))
    raise SystemExit(1)
print("validation=ok")
print("skills=" + str(len(files)))
