import json
import pytest
from jsonschema import validate, ValidationError

# Carregar esquema de validação
with open("schema_agente.json", encoding="utf-8") as f:
    schema = json.load(f)

# Carregar arquivo de agentes
with open("estrutura_agentes_v1.json", encoding="utf-8") as f:
    agentes = json.load(f)["agents"]

@pytest.mark.parametrize("agente", agentes)
def test_agente_schema(agente):
    try:
        validate(instance=agente, schema=schema)
    except ValidationError as e:
        pytest.fail(f"Erro de validação no agente '{agente.get('id', 'SEM ID')}': {e.message}")
