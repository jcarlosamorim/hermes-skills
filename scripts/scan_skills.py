#!/usr/bin/env python3
"""Roda o scanner de segurança do PRÓPRIO Hermes Agent contra cada skill deste repositório.

Baixa `tools/skills_guard.py` da tag pinada (a versão que a instância roda) e chama `scan_skill()`
com trust `community`, que é o trust que este repositório tem em qualquer Hermes do mundo.
Falha o build se QUALQUER skill sair com veredito diferente de `safe`: em `community`, `caution`
já bloqueia a instalação, e `dangerous` bloqueia sem `--force`.

Uso:
    python3 scripts/scan_skills.py                 # baixa o guard da tag pinada
    SKILLS_GUARD_PATH=/caminho/skills_guard.py python3 scripts/scan_skills.py   # offline
Exige Python 3.10+ (o guard usa `X | None`).
"""
from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
import urllib.request
from pathlib import Path

HERMES_TAG = "v2026.8.27"  # 0.20.6, a versão medida na instância de referência em 2026-08-31
GUARD_URL = f"https://raw.githubusercontent.com/NousResearch/hermes-agent/{HERMES_TAG}/tools/skills_guard.py"
ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

if sys.version_info < (3, 10):
    sys.exit("scan_skills.py exige Python 3.10+")


def load_guard():
    path = os.environ.get("SKILLS_GUARD_PATH")
    if path:
        src = Path(path)
    else:
        tmp = Path(tempfile.mkdtemp()) / "skills_guard.py"
        with urllib.request.urlopen(GUARD_URL, timeout=30) as r:
            tmp.write_bytes(r.read())
        src = tmp
    spec = importlib.util.spec_from_file_location("skills_guard", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    guard = load_guard()
    dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    if not dirs:
        print("nenhuma skill encontrada"); return 1
    blocked = 0
    for d in dirs:
        res = guard.scan_skill(d, source="community")
        ok, reason = guard.should_allow_install(res, force=False)
        flag = "OK " if ok else "BLOQUEADA"
        print(f"{flag:9} {d.name:30} verdict={res.verdict:9} findings={len(res.findings)}")
        for f in res.findings:
            mark = "  !!" if f.severity in ("critical", "high") else "  ·"
            print(f"{mark} [{f.severity}] {f.pattern_id} {f.file}:{f.line} {f.match[:80]!r}")
        if not ok:
            blocked += 1
    print(f"\nscan: {len(dirs)} skills · {blocked} bloqueada(s) · guard {HERMES_TAG} · trust community")
    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())
