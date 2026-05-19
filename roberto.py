# Responsável: Roberto
# Responsabilidade: exibição de título, status, menu e mensagens do simulador.


def exibir_titulo():
    """Exibe o título inicial do simulador."""
    print("=" * 45)
    print("   MISSÃO ORBITAL: DECISÕES NA NAVE")
    print("=" * 45)
    print("Você é o comandante da nave e precisa tomar uma decisão.\n")


def exibir_status(estado):
    """Exibe as 5 variáveis atuais do dicionário estado."""
    print("\n=== STATUS ATUAL DA NAVE ===")
    print(f"Oxigênio: {estado['oxigenio']}")
    print(f"Energia: {estado['energia']}")
    print(f"Integridade: {estado['integridade']}")
    print(f"Moral da tripulação: {estado['moral']}")
    print(f"Distância percorrida: {estado['distancia']}")


def exibir_menu(opcoes):
    """Mostra as opções de decisão disponíveis para o usuário."""
    print("\n=== ESCOLHA UMA DECISÃO ===")
    for numero, opcao in enumerate(opcoes, start=1):
        print(f"{numero}. {opcao}")


def exibir_resultado(mensagem):
    """Mostra uma mensagem final após a decisão do usuário."""
    print("\n=== RESULTADO DA DECISÃO ===")
    print(mensagem)