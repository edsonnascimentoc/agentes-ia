import requests

def obter_protocolo(agente_id, caminho_protocolo):
    tenant = caminho_protocolo.split('/')[0]
    try:
        response = requests.post("http://localhost:3000/protocolo", json={
            "agente": agente_id,
            "tarefa": "executar tarefa atribuída ao agente",
            "tenant": tenant
        })
        return response.json()["instrucoes"]
    except Exception as e:
        return f"[ERRO protocolo] {str(e)}"
