import json
import argparse
from abacusai import ApiClient
from pathlib import Path

# -------------------------------------------------
# Configuração da API (defina sua chave abaixo)
API_KEY = "<SEU_TOKEN_AQUI>"
PROJECT_ID = "<SEU_PROJECT_ID>"

# -------------------------------------------------
def load_agents(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("agents", [])

def create_agent(client, agent):
    resp = client.create_agent(
        projectId=PROJECT_ID,
        name=agent["id"],
        description=agent["persona"],
        memory=1,
        packageRequirements=[]
    )
    print(f"✅ Criado: {resp.agentId}")

def list_agents(client):
    resp = client.list_agents(projectId=PROJECT_ID)
    print("🔍 Agentes existentes:")
    for ag in resp:
        print(f"- {ag.agentId}: {ag.name}")

def update_agent(client, agent_id, agent):
    client.update_agent(
        agentId=agent_id,
        description=agent["persona"],
        memory=agent.get("memory", 1)
    )
    print(f"🔄 Atualizado: {agent_id}")

def delete_agent(client, agent_id):
    client.delete_agent(agentId=agent_id)
    print(f"🗑️ Deletado: {agent_id}")

def main():
    parser = argparse.ArgumentParser(description="CLI Abacus AI — Gerenciar Agentes")
    parser.add_argument("--arquivo", "-a", default="estrutura_agentes_v1.json")
    parser.add_argument("action", choices=["create", "list", "update", "delete"])
    parser.add_argument("--id", help="ID do agente (para update/delete)")
    args = parser.parse_args()

    client = ApiClient(API_KEY)

    if args.action == "list":
        list_agents(client)
        return

    agents = load_agents(args.arquivo)

    if args.action == "create":
        for ag in agents:
            create_agent(client, ag)
    elif args.action == "update":
        if not args.id:
            print("❗ Use --id para identificar o agente a ser atualizado")
            return
        ag = next((x for x in agents if x["id"] == args.id), None)
        if ag: update_agent(client, args.id, ag)
    elif args.action == "delete":
        if not args.id:
            print("❗ Use --id para identificar o agente a ser deletado")
            return
        delete_agent(client, args.id)

if __name__ == "__main__":
    main()
