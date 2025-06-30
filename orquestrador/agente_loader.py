import json
import os

def carregar_agente(agente_id):
    caminho = f"agents/{agente_id}.json"
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Agente '{agente_id}' não encontrado.")
    with open(caminho, encoding='utf-8') as f:
        return json.load(f)
