from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import json

app = FastAPI(title="Protocol Gateway", version="1.0")

PROTOCOL_BASE = os.path.join(os.path.dirname(__file__), "protocolos")


class ProtocoloRequest(BaseModel):
    agente: str
    tarefa: str
    tenant: str = "default"


@app.post("/protocolo")
def aplicar_protocolo(req: ProtocoloRequest):
    caminho_tenant = os.path.join(PROTOCOL_BASE, req.tenant, f"{req.agente}.json")
    caminho_default = os.path.join(PROTOCOL_BASE, "default", f"{req.agente}.json")

    caminho_arquivo = caminho_tenant if os.path.exists(caminho_tenant) else caminho_default

    if not os.path.exists(caminho_arquivo):
        raise HTTPException(status_code=404, detail="Protocolo não encontrado para o agente requisitado.")

    with open(caminho_arquivo, encoding="utf-8") as f:
        protocolo = json.load(f)

    instrucoes = f"""
🔐 Persona: {protocolo.get("persona")}
🌍 Idioma: {protocolo.get("idioma")}
📤 Formato de saída: {protocolo.get("formato_saida")}
🔒 Segurança: {protocolo.get("seguranca")}
🧱 Estilo: {protocolo.get("estilo")}
📚 Profundidade: {protocolo.get("profundidade")}
❗ Restrições: {', '.join(protocolo.get('restricoes', []))}
"""

    return {
        "agente": req.agente,
        "tenant": req.tenant,
        "tarefa": req.tarefa,
        "persona": protocolo.get("persona"),
        "instrucoes": instrucoes.strip()
    }
