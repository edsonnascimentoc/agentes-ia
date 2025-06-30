📘 README_cursor_mcp.md — Pipeline MCP com Cursor IDE

🔍 Visão Geral
Este pipeline implementa a arquitetura MCP (Model, Context, Protocol) de forma modular e visual utilizando o Cursor IDE, permitindo:

🚀 Execução autônoma de tarefas com agentes IA

🔄 Encadeamento de protocolo, contexto e modelo

🧠 Geração de respostas com LLMs (ex: OpenAI)

📂 Estrutura do Projeto

.cursor/
├── nodes/
│   ├── protocolo_node.json
│   ├── contexto_node.json
│   └── model_node.json
├── pipeline_mcp.cursor.json
scripts/
├── run_protocolo.py
├── run_contexto.py
└── run_model.py

⚙️ Pré-requisitos
Cursor IDE instalado

Python 3.10+

Variável de ambiente OPENAI_API_KEY definida

Servidores locais rodando:

http://localhost:3000/protocolo (protocol-gateway)

http://localhost:8000/contexto (context-engine)

🛠️ Execução no Cursor
Abra o projeto no Cursor

Clique em pipeline_mcp.cursor.json

Preencha os parâmetros:

{
  "agente": "agente_backend_api",
  "tenant": "default",
  "topico": "backend",
  "perfil": "professor",
  "pergunta": "crie um endpoint para notas escolares"
}

Clique em Run para executar o pipeline

🧠 Fluxo MCP Visual

🔐 Aplicar Protocolo: consulta persona e instruções

📘 Recuperar Contexto: acessa conteúdo do tópico/perfil

🧠 Executar Modelo: gera resposta contextual com base no protocolo

✅ Resultado Esperado
A saída final será um JSON como:

{
  "resposta": "Aqui está um endpoint FastAPI seguro para cadastrar notas..."
}

📌 Observações
O pipeline é 100% modular, sendo possível trocar os scripts Python por funções LLM personalizadas.

Pode ser versionado junto com os agentes e protocolos MCP no seu repositório.

Deseja agora que este guia seja incluído como documentação automática na raiz do seu projeto com os agentes, ou deseja avançar para CI/CD com GitHub Actions usando esse pipeline?







