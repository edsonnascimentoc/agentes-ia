from fastapi import FastAPI, Query, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
import os
import requests

try:
    import pdfplumber
    import docx
    import pandas as pd
except ImportError:
    pdfplumber = None
    docx = None
    pd = None

app = FastAPI(title="Context Engine", version="2.1")

BASE_PATH = os.path.join(os.path.dirname(__file__), "dados", "base_contexto.json")
DOC_PATH = os.path.join(os.path.dirname(__file__), "docs")


def carregar_contexto(topico: str, perfil: str):
    with open(BASE_PATH, encoding="utf-8") as f:
        base = json.load(f)
    dado = base.get(topico.lower())
    if not dado:
        return None, f"Tópico '{topico}' não encontrado."
    tipo = dado.get("tipo")
    conteudo = dado.get("conteudo", {})

    if tipo == "texto":
        return conteudo.get(perfil) or conteudo.get("aluno") or "Conteúdo indisponível para esse perfil.", None

    elif tipo == "arquivo":
        formato = dado.get("formato")
        caminho = os.path.join(DOC_PATH, os.path.basename(dado.get("local", "")))

        if formato == "pdf" and pdfplumber:
            with pdfplumber.open(caminho) as pdf:
                texto = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
            return texto, None
        elif formato == "docx" and docx:
            doc = docx.Document(caminho)
            texto = "\n".join(p.text for p in doc.paragraphs)
            return texto, None
        elif formato in ("xls", "xlsx") and pd:
            df = pd.read_excel(caminho)
            return df.to_string(index=False), None
        else:
            return None, f"Formato de arquivo '{formato}' não suportado."

    elif tipo == "web":
        link = dado.get("link")
        try:
            resposta = requests.get(link)
            if resposta.status_code == 200:
                return resposta.text[:1000] + "...", None
            else:
                return None, f"Erro ao acessar link: {resposta.status_code}"
        except Exception as e:
            return None, f"Erro ao acessar o link: {str(e)}"

    return None, "Tipo de conteúdo não suportado."


@app.get("/retrieve")
def retrieve(topico: str = Query(...), perfil: str = Query("aluno")):
    conteudo, erro = carregar_contexto(topico, perfil)
    if erro:
        return JSONResponse(status_code=404, content={"erro": erro})
    return {"topico": topico, "perfil": perfil, "conteudo": conteudo}


class PerguntaRequest(BaseModel):
    topico: str
    perfil: str
    pergunta: str


@app.post("/ask")
def ask(req: PerguntaRequest):
    conteudo, erro = carregar_contexto(req.topico, req.perfil)
    if erro:
        return JSONResponse(status_code=404, content={"erro": erro})

    resposta_simulada = f"🔎 Com base no contexto do tópico '{req.topico}' para perfil '{req.perfil}', aqui está uma sugestão para sua pergunta:\n\n'{req.pergunta}'\n\n→ {conteudo[:300]}..."

    return {
        "topico": req.topico,
        "perfil": req.perfil,
        "pergunta": req.pergunta,
        "resposta_simulada": resposta_simulada
    }
