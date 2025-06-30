import sys
import json
import requests

def run(topico, perfil):
    response = requests.get("http://localhost:8000/contexto", params={"topico": topico, "perfil": perfil})
    return {"contexto": response.json()["conteudo"]}

if __name__ == "__main__":
    args = json.loads(sys.stdin.read())
    result = run(**args)
    print(json.dumps(result))
