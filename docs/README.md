# 🧠 Projeto: Agentes Técnicos para Fluxos de IA

Este projeto define uma estrutura padronizada e versionada de agentes especializados em áreas técnicas de engenharia de software, DevOps,
segurança e IA generativa, com o objetivo de automatizar tarefas e fluxos em plataformas como Lovable, Devin AI, Abacus AI, Flowise, Cursor e Replit.

---

## 📦 Estrutura do Projeto

├── estrutura_agentes_v1.json # Agentes em formato JSON

├── estrutura_agentes_v1.yaml # Agentes em YAML

├── schema_agente.json # JSON Schema de validação

├── test_agentes.py # Testes automatizados com pytest

├── cli_agentes.py # CLI de inspeção de agentes

├── cli_agentes_abacus.py # CLI com integração à API do Abacus AI

├── CHANGELOG.md # Histórico de versões

---

## 🚀 Como Usar

### 1. Instale as dependências

```bash
pip install pytest jsonschema abacusai
```

2. Validar estrutura dos agentes
pytest test_agentes.py

3. Listar agentes locais
python cli_agentes.py --arquivo estrutura_agentes_v1.json

4. Provisionar no Abacus AI
Edite cli_agentes_abacus.py e defina suas variáveis:
API_KEY = "<SUA_ABACUS_API_KEY>"
PROJECT_ID = "<SEU_PROJECT_ID>"

Então execute:
python cli_agentes_abacus.py create

🧪 Testes
Todos os agentes são validados automaticamente com jsonschema:

Campos obrigatórios: id, persona, tools, format, version

Versionamento semântico (1.0.0, 1.1.0, etc.)

Tipos corretos de dados

🔐 Segurança e Conformidade
Tokens não são salvos no repositório

Recomenda-se uso de .env ou variáveis de ambiente

Suporte futuro a anonimização e validação LGPD

📚 Próximas Etapas
Suporte a Lovable, Devin, Replit e Cursor

Criação de repositório real com exemplos aplicáveis

Geração de agentes autoexplicativos (RAG, embeddings, etc.)

