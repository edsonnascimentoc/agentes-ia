from langgraph.graph import StateGraph
from nodes.contexto_node import contexto_node
from nodes.protocolo_node import protocolo_node
from nodes.model_node import model_node

builder = StateGraph()
builder.add_node("protocolo", protocolo_node)
builder.add_node("contexto", contexto_node)
builder.add_node("model", model_node)

builder.set_entry_point("protocolo")
builder.add_edge("protocolo", "contexto")
builder.add_edge("contexto", "model")

graph = builder.compile()

resposta = graph.invoke({
    "topico": "backend",
    "perfil": "professor",
    "pergunta": "crie endpoint para notas",
    "agente": "agente_backend_api"
})

print(resposta["resposta"])
