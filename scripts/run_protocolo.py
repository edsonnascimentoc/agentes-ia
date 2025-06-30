import sys
import json
import requests

def run(agente, tenant):
    response = requests.post("http://localhost:3000/protocolo", json={
        "agente": agente,
        "tarefa": "executar tarefa atribuída ao agente",
        "tenant": tenant
    })
    return {"protocolo": response.json()["instrucoes"]}

if __name__ == "__main__":
    args = json.loads(sys.stdin.read())
    result = run(**args)
    print(json.dumps(result))
