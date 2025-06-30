import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def model_node(state):
    contexto = state.get("contexto", "")
    protocolo = state.get("protocolo", "")
    pergunta = state.get("pergunta", "")
    prompt = f'''
Contexto:
{contexto}

Protocolo:
{protocolo}

Pergunta:
{pergunta}
'''

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente técnico educacional."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=700
        )
        state["resposta"] = resposta.choices[0].message.content
    except Exception as e:
        state["resposta"] = f"[ERRO modelo] {str(e)}"
    return state
