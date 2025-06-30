import sys
import json
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def run(pergunta, contexto, protocolo):
    prompt = f"""
Você é um agente educacional.

Contexto:
{contexto}

Protocolo:
{protocolo}

Pergunta:
{pergunta}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente técnico educacional."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )
    return {"resposta": response.choices[0].message.content}

if __name__ == "__main__":
    args = json.loads(sys.stdin.read())
    result = run(**args)
    print(json.dumps(result))
