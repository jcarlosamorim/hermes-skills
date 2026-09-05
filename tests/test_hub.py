"""Testes das funções puras que sustentam as três distribuições. Rodar: python3 -m unittest discover -s tests -v"""
import importlib.util, io, sys, tempfile, unittest, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import hub_common as hc  # noqa: E402

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

bd = load("build_docs")


class Cap200(unittest.TestCase):
    def test_curta_passa_intacta(self):
        self.assertEqual(hc.cap200("Uma descrição curta."), "Uma descrição curta.")

    def test_normaliza_espacos(self):
        self.assertEqual(hc.cap200("a  b\n c"), "a b c")

    def test_corta_na_palavra_e_nunca_passa_do_limite(self):
        longa = " ".join(["palavra"] * 40)
        out = hc.cap200(longa)
        self.assertTrue(out.endswith("…")); self.assertLessEqual(len(out), hc.DESC_MAX + 1)
        self.assertNotIn("palavr…", out, "cortou no meio da palavra")


class StrictFrontmatter(unittest.TestCase):
    FM = {"name": "x-skill", "description": "d " * 150, "license": "MIT", "author": "A", "version": "9.9.9",
          "metadata": {"hermes": {"tags": ["a", "b"], "requires_toolsets": ["terminal"], "config": [{"key": "k", "description": "desc"}]}},
          "required_environment_variables": [{"name": "META_AUTH"}]}

    def test_so_chaves_do_spec_e_metadata_string(self):
        out = bd.strict_frontmatter(self.FM, "x-skill", "0.4.1")
        self.assertTrue(set(out) <= set(bd.SPEC_KEYS))
        self.assertLessEqual(len(out["description"]), hc.DESC_MAX + 1)
        self.assertTrue(all(isinstance(v, str) for v in out["metadata"].values()))
        self.assertIn("META_AUTH", out["compatibility"]); self.assertIn("Requer: terminal", out["compatibility"])
        self.assertEqual(out["metadata"]["hub"], hc.HUB_URL)


class Referencias(unittest.TestCase):
    def test_lista_arquivos_da_secao(self):
        body = "texto\n\n## Arquivos desta skill\n\n- `references/a.md`\n- `templates/b.yaml`\n\n## Outra\n"
        self.assertEqual(bd.referenced_files(body), ["references/a.md", "templates/b.yaml"])

    def test_sem_secao_devolve_vazio(self):
        self.assertEqual(bd.referenced_files("nada aqui"), [])


class Prune(unittest.TestCase):
    def test_remove_blocos_de_ativacao_e_nota_mmos(self):
        txt = "activation-instructions:\n  - a\n  - b\nname: fulano\nACTIVATION-NOTICE: x\ncorpo\n## MMOS Integration Note\nresto\n"
        out = bd.prune(txt, "references/x.md")
        self.assertNotIn("activation-instructions", out); self.assertNotIn("ACTIVATION-NOTICE", out)
        self.assertNotIn("resto", out); self.assertIn("name: fulano", out); self.assertIn("corpo", out)

    def test_nao_mexe_em_py_e_json(self):
        self.assertEqual(bd.prune("x = 1\n", "scripts/a.py"), "x = 1\n")


class Ativacao(unittest.TestCase):
    def test_texto_cita_arquivo_e_gatilho(self):
        t = hc.activation_text("copy-oferta", "monta a oferta")
        self.assertIn("`copy-oferta.md`", t); self.assertIn('"monta a oferta"', t); self.assertIn("## Verification", t)


class ZipReprodutivel(unittest.TestCase):
    def test_mesmo_conteudo_mesmos_bytes(self):
        def build():
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
                zi = zipfile.ZipInfo("s/SKILL.md", date_time=(1980, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED; zi.external_attr = 0o644 << 16
                z.writestr(zi, b"---\nname: s\n---\n")
            return buf.getvalue()
        self.assertEqual(build(), build())


if __name__ == "__main__":
    unittest.main()
