#!/usr/bin/env python3
"""Conector de LEITURA da Marketing API da Meta.

Versão para o Hub de Skills do Hermes: credencial SÓ por variável de ambiente (META_AUTH),
definida no ambiente onde o script roda (no Hermes, pela configuração da skill) e nunca mostrada ao modelo.

Garantias:
  - so faz GET. Nao cria, nao edita, nao ativa, nao gasta.
  - credencial vai no header Authorization, nunca na query string.
  - o token nunca aparece em stdout, stderr ou log.

Uso:
    python3 meta_api.py contas
    python3 meta_api.py campanhas act_123
    python3 meta_api.py insights act_123 --nivel campaign --preset last_7d
    python3 meta_api.py get act_123/adsets --query "fields=name,effective_status"
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API = os.environ.get("META_API_VERSION", "v23.0")
BASE = f"https://graph.facebook.com/{API}"
UA = "hermes-skills-ads-otimizar/0.3 (+https://github.com/AgentsFlix/hermes-skills)"


def credencial() -> str:
    """Lê a credencial da variável de ambiente META_AUTH. Nunca a devolve para o stdout."""
    valor = os.environ.get("META_AUTH")
    if not valor:
        sys.exit("META_AUTH ausente no ambiente. Defina-a onde o script roda (no Hermes, pela configuração da skill) e abra nova sessão.")
    return valor.strip()


def get(path: str, query: str = "", auth: str = None) -> dict:
    auth = auth or credencial()
    url = f"{BASE}/{path.lstrip('/')}"
    if query:
        url += "?" + query
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {auth}",
        "User-Agent": UA,
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as err:
        corpo = err.read().decode(errors="replace")
        try:
            erro = json.loads(corpo).get("error", {})
            msg = f"{erro.get('type')}: {erro.get('message')} (code {erro.get('code')})"
        except Exception:
            msg = corpo[:400]
        sys.exit(f"Meta recusou {path} -> HTTP {err.code} | {msg}")


def paginado(path: str, query: str = "", auth: str = None, teto: int = 20) -> list:
    """Segue paginacao por cursor. `teto` limita o numero de paginas."""
    auth = auth or credencial()
    itens, pagina = [], 0
    resp = get(path, query, auth)
    while True:
        itens.extend(resp.get("data", []))
        pagina += 1
        proxima = (resp.get("paging") or {}).get("cursors", {}).get("after")
        if not proxima or pagina >= teto or not resp.get("paging", {}).get("next"):
            break
        q = query + ("&" if query else "") + f"after={urllib.parse.quote(proxima)}"
        resp = get(path, q, auth)
    return itens


CAMPOS_CAMPANHA = "name,objective,effective_status,daily_budget,lifetime_budget,bid_strategy,created_time,start_time"
CAMPOS_ADSET = "name,campaign_id,effective_status,daily_budget,optimization_goal,bid_strategy,learning_stage_info,created_time"
CAMPOS_INSIGHT = (
    "campaign_id,campaign_name,adset_id,adset_name,spend,impressions,reach,frequency,"
    "clicks,ctr,cpm,cpc,actions,cost_per_action_type,purchase_roas,date_start,date_stop"
)


def main() -> None:
    ap = argparse.ArgumentParser(description="leitura da Marketing API da Meta")
    ap.add_argument("comando", choices=["contas", "campanhas", "adsets", "insights", "get", "testar"])
    ap.add_argument("alvo", nargs="?", default=None, help="act_XXX, id de campanha/adset, ou path para `get`")
    ap.add_argument("--nivel", default="campaign", choices=["account", "campaign", "adset", "ad"])
    ap.add_argument("--preset", default="last_7d", help="today|yesterday|last_7d|last_14d|last_30d|maximum")
    ap.add_argument("--query", default="", help="querystring extra para o comando `get`")
    args = ap.parse_args()
    auth = credencial()

    if args.comando == "testar":
        eu = get("me", "fields=id,name", auth)
        contas = paginado("me/adaccounts", "fields=account_id,name,account_status,currency", auth)
        print(f"token valido -> {eu.get('name')} | {len(contas)} conta(s) de anuncio visiveis")
        return

    if args.comando == "contas":
        dados = paginado(
            "me/adaccounts",
            "fields=account_id,name,account_status,currency,amount_spent,funding_source_details",
            auth,
        )
    elif args.comando == "campanhas":
        dados = paginado(f"{args.alvo}/campaigns", f"fields={CAMPOS_CAMPANHA}&limit=100", auth)
    elif args.comando == "adsets":
        dados = paginado(f"{args.alvo}/adsets", f"fields={CAMPOS_ADSET}&limit=100", auth)
    elif args.comando == "insights":
        q = f"fields={CAMPOS_INSIGHT}&level={args.nivel}&date_preset={args.preset}&limit=200"
        dados = paginado(f"{args.alvo}/insights", q, auth)
    else:  # get
        dados = get(args.alvo, args.query, auth)

    print(json.dumps(dados, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
