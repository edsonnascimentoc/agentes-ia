import argparse
from agente_loader import carregar_agente
from protocolo_cliente import obter_protocolo
from contexto_cliente import obter_contexto
from simulador_model import gerar_resposta

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--agente', required=True)
    parser.add_argument('--topico', required=True)
    parser.add_argument('--perfil', default='aluno')
    parser.add_argument('--pergunta', required=True)
    args = parser.parse_args()

    agente = carregar_agente(args.agente)
    protocolo = obter_protocolo(agente['id'], agente['protocol'])
    contexto = obter_contexto(args.topico, args.perfil)

    resposta = gerar_resposta(
        pergunta=args.pergunta,
        contexto=contexto,
        protocolo=protocolo,
        agente=agente
    )

    print('\n🔽 Resposta Final 🔽\n')
    print(resposta)

if __name__ == '__main__':
    main()
