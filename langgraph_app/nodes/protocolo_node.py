import requests

def protocolo_node(state):
    agente = state.get("agente", "agente_backend_api")
    tenant = "default"
    try:
        response = requests.post("http://localhost:3000/protocolo", json={
            "agente": agente,
            "tarefa": "executar tarefa atribuída ao agente",
            "tenant": tenant
        })
        state["protocolo"] = response.json()["instrucoes"]
    except Exception as e:
        state["protocolo"] = f"[ERRO protocolo] {str(e)}"
    return state
