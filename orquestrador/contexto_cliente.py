import requests

def obter_contexto(topico, perfil):
    try:
        response = requests.get("http://localhost:8000/contexto", params={"topico": topico, "perfil": perfil})
        return response.json()["conteudo"]
    except Exception as e:
        return f"[ERRO contexto] {str(e)}"
