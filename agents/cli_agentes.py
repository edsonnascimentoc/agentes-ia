import json
import argparse
from pathlib import Path

def carregar_agentes(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    return dados.get("agents", [])

def listar_agentes(agentes):
    print(f"📦 Total de agentes: {len(agentes)}\n")
    for a in agentes:
        print(f"🔹 ID: {a['id']}")
        print(f"   Persona: {a['persona']}")
        print(f"   Versão: {a['version']}")
        print(f"   Ferramentas: {', '.join(a['tools'])}")
        print(f"   Formatos: {', '.join(a['format'])}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI para listar agentes técnicos de IA")
    parser.add_argument("--arquivo", "-a", type=str, default="estrutura_agentes_v1.json", help="Caminho para o arquivo JSON")
    args = parser.parse_args()

    caminho_arquivo = Path(args.arquivo)
    if not caminho_arquivo.exists():
        print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
    else:
        agentes = carregar_agentes(caminho_arquivo)
        listar_agentes(agentes)
