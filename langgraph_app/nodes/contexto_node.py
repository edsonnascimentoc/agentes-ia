import requests

def contexto_node(state):
    topico = state.get("topico")
    perfil = state.get("perfil", "aluno")
    try:
        response = requests.get("http://localhost:8000/contexto", params={"topico": topico, "perfil": perfil})
        state["contexto"] = response.json()["conteudo"]
    except Exception as e:
        state["contexto"] = f"[ERRO contexto] {str(e)}"
    return state
