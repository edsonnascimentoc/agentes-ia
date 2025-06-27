import json
import pytest

@pytest.mark.parametrize("entrada", [
    {"id": "agente_backend", "task": "Criar endpoint RESTful"},
    {"id": "agente_dados", "task": "Gerar migration Prisma"},
])
def test_simulacao_execucao_agente(entrada):
    assert "id" in entrada and "task" in entrada
    assert entrada["task"] != ""
    print(f"✅ Agente {entrada['id']} processando tarefa: {entrada['task']}")
