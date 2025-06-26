import re
import sys

regras = {
    "secrets-in-code": {
        "pattern": r"(AKIA|AIza|ghp_|eyJ[A-Za-z0-9_\-]+)",
        "desc": "Segredo encontrado em código"
    },
    "personal-data-exposure": {
        "pattern": r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\w+@\w+\.\w+\b",
        "desc": "Dados pessoais expostos"
    }
}

def validar(caminho):
    with open(caminho, encoding="utf-8") as f:
        conteudo = f.read()
    for rid, regra in regras.items():
        if re.search(regra["pattern"], conteudo):
            print(f"🚨 {rid}: {regra['desc']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python valida_compliance.py arquivo_alvo.txt")
    else:
        validar(sys.argv[1])
