#!/usr/bin/env python3
"""Small offline validator for the community skill repository."""
from __future__ import annotations

import re
import sys
from pathlib import Path

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
    if description and len(description.group(1).strip().strip('"')) > 220:
        errors.append(f"{path}: description must be 220 characters or fewer")
    if description and len(description.group(1).strip().strip('"')) < 40:
        errors.append(f"{path}: description too short to be found by skills search (min 40 chars)")
    if not re.search(r"^## When to use", body, re.MULTILINE | re.IGNORECASE) or "## Verification" not in body:
        errors.append(f"{path}: requires When to Use and Verification sections")
    # mesmos formatos que o scanner do Hermes reprova; com fronteira, para "risk-free" ou "task-" não dispararem
    if "[REDACTED]" not in text and re.search(r"(?<![A-Za-z0-9])(?:AIza[0-9A-Za-z_-]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|ntn_[A-Za-z0-9]{20,}|secret_[A-Za-z0-9]{20,})", text):
        errors.append(f"{path}: possible secret-like string")

if errors:
    print("validation=failed")
    print("\n".join(errors))
    raise SystemExit(1)
print("validation=ok")
print("skills=" + str(len(files)))
