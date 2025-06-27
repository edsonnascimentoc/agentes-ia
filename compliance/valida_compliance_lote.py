import re
import os

regras = {
    "secrets-in-code": {
        "pattern": r"(AKIA|AIza|ghp_|eyJ[A-Za-z0-9_\-]+)",
        "desc": "Segredo encontrado"
    },
    "personal-data": {
        "pattern": r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\w+@\w+\.\w+\b",
        "desc": "Dado pessoal exposto"
    }
}

def verificar_arquivo(path):
    try:
        with open(path, encoding="utf-8") as f:
            conteudo = f.read()
        for rid, regra in regras.items():
            if re.search(regra["pattern"], conteudo):
                print(f"🚨 {rid} em {path} → {regra['desc']}")
                return True
    except Exception as e:
        print(f"⚠️ Erro ao ler {path}: {e}")
    return False

def varrer_diretorio(base_dir="."):
    extensoes = (".json", ".yml", ".yaml", ".ts", ".tsx")
    encontrou = False
    for root, _, files in os.walk(base_dir):
        for nome in files:
            if nome.endswith(extensoes):
                caminho = os.path.join(root, nome)
                if verificar_arquivo(caminho):
                    encontrou = True
    if encontrou:
        exit(1)

if __name__ == "__main__":
    varrer_diretorio()
