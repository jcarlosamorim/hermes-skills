#!/usr/bin/env python3
"""Gera a superfície publicada em docs/ a partir de skills/ e catalog.json.

- docs/catalog.json               cópia do catálogo (a página lê daqui)
- docs/.well-known/skills/        índice e cópia de cada skill no formato que o Hermes lê com
                                  `hermes skills search https://<dominio>` (WellKnownSkillSource)
Rode depois de mudar qualquer skill ou o catálogo. Idempotente.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS, DOCS = ROOT / "skills", ROOT / "docs"
WK = DOCS / ".well-known" / "skills"


def main() -> None:
    cat = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").touch()  # GitHub Pages serve .well-known só sem Jekyll
    shutil.copyfile(ROOT / "catalog.json", DOCS / "catalog.json")
    if WK.exists():
        shutil.rmtree(WK)
    WK.mkdir(parents=True)
    index = []
    for d in sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").exists()):
        files = sorted(str(f.relative_to(d)) for f in d.rglob("*") if f.is_file() and not f.name.startswith("."))
        shutil.copytree(d, WK / d.name, ignore=shutil.ignore_patterns(".*", "__pycache__"))
        meta = next((s for s in cat["skills"] if s["name"] == d.name), {})
        index.append({"name": d.name, "description": meta.get("description", ""), "files": files})
    (WK / "index.json").write_text(json.dumps({"skills": index}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"docs: catalog.json + .well-known/skills ({len(index)} skills)")


if __name__ == "__main__":
    main()
