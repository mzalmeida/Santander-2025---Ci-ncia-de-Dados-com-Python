import os
import csv

BASE_DIR = "extratos"
CSV_SAIDA = "transacoes_unificadas.csv"


# ======================================================
# NUBANK CRÉDITO (CSV separado por VÍRGULA)
# ======================================================
def parser_nubank_credito(pasta, arquivo):
    dados = []
    with open(os.path.join(pasta, arquivo), encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        for r in reader:
            dados.append({
                "banco": "nubank",
                "tipo": "credito",
                "data": r["date"],
                "descricao": r["title"],
                "valor": float(r["amount"]),
                "arquivo": arquivo
            })
    return dados


# ======================================================
# NUBANK DÉBITO (TAB + encoding quebrado)
# ======================================================

def parser_nubank_debito(pasta, arquivo):
    dados = []
    with open(os.path.join(pasta, arquivo), encoding="utf-8") as f:
        sample = f.read(2048)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters="\t;|,")

        reader = csv.DictReader(f, dialect=dialect)

        for r in reader:
            if not r:
                continue

            dados.append({
                "banco": "nubank",
                "tipo": "debito",
                "data": r.get("Data") or r.get("\ufeffData"),
                "descricao": (
                r.get("DescriÃ§Ã£o")
                or r.get("\ufeffDescriÃ§Ã£o")
                or r.get("Descrição")
                or r.get("\ufeffDescrição")
                or ""
                ).strip(),
                "valor": float(str(r.get("Valor", "0")).replace(",", ".")),
                "arquivo": arquivo
            })
    return dados




# ======================================================
# INTER DÉBITO (pula lixo antes do cabeçalho)
# ======================================================
def parser_inter(pasta, arquivo):
    dados = []

    with open(os.path.join(pasta, arquivo), encoding="latin-1") as f:
        linhas = f.readlines()

    inicio = None
    for i, linha in enumerate(linhas):
        if linha.startswith("Data LanÃ§amento"):
            inicio = i
            break

    if inicio is None:
        return dados

    reader = csv.DictReader(linhas[inicio:], delimiter=";")

    for r in reader:
        if not r.get("Valor"):
            continue

        valor = r["Valor"].replace(".", "").replace(",", ".")

        dados.append({
            "banco": "inter",
            "tipo": "debito",
            "data": r["Data LanÃ§amento"],
            "descricao": r["DescriÃ§Ã£o"],
            "valor": float(valor),
            "arquivo": arquivo
        })

    return dados


# ======================================================
# MERCADO PAGO CRÉDITO
# ======================================================
def parser_mercadopago_credito(pasta, arquivo):
    dados = []
    with open(os.path.join(pasta, arquivo), encoding="latin-1", errors="ignore") as f:
        reader = csv.DictReader(f, delimiter=";")
        for r in reader:
            valor = r["Valor"].replace(",", ".")
            dados.append({
                "banco": "mercadopago",
                "tipo": "credito",
                "data": r["Data"] + "/2025",
                "descricao": r["Descrição"],
                "valor": float(valor),
                "arquivo": arquivo
            })
    return dados


# ======================================================
# MAIN
# ======================================================
todas_transacoes = []

for banco in os.listdir(BASE_DIR):
    caminho_banco = os.path.join(BASE_DIR, banco)
    if not os.path.isdir(caminho_banco):
        continue

    for tipo in ["credito", "debito"]:
        caminho_tipo = os.path.join(caminho_banco, tipo)
        if not os.path.isdir(caminho_tipo):
            continue

        for arquivo in os.listdir(caminho_tipo):
            if not arquivo.lower().endswith(".csv"):
                continue

            if banco == "nubank" and tipo == "credito":
                transacoes = parser_nubank_credito(caminho_tipo, arquivo)

            elif banco == "nubank" and tipo == "debito":
                transacoes = parser_nubank_debito(caminho_tipo, arquivo)

            elif banco == "inter" and tipo == "debito":
                transacoes = parser_inter(caminho_tipo, arquivo)

            elif banco == "mercadopago" and tipo == "credito":
                transacoes = parser_mercadopago_credito(caminho_tipo, arquivo)

            else:
                transacoes = []

            print(
                f"DEBUG -> banco={banco} tipo={tipo} "
                f"arquivo={arquivo} registros={len(transacoes)}"
            )

            todas_transacoes.extend(transacoes)


# ======================================================
# SAÍDA FINAL
# ======================================================
if todas_transacoes:
    with open(CSV_SAIDA, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=todas_transacoes[0].keys())
        writer.writeheader()
        writer.writerows(todas_transacoes)

    print(f"\nProcesso finalizado. {len(todas_transacoes)} transações geradas.")
else:
    print("Nenhuma transação encontrada.")
