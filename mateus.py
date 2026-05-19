# Responsável: Mateus
# Responsabilidade: registrar e exibir o histórico das decisões.


def registrar_historico(historico, escolha, estado):
    """Registra a escolha feita e uma cópia do estado atual no histórico."""
    registro = {
        "escolha": escolha,
        "estado": estado.copy()
    }
    historico.append(registro)


def formatar_estado(estado):
    """Transforma o dicionário estado em um texto simples para exibição."""
    return (
        f"Oxigênio: {estado['oxigenio']} | "
        f"Energia: {estado['energia']} | "
        f"Integridade: {estado['integridade']} | "
        f"Moral: {estado['moral']} | "
        f"Distância: {estado['distancia']}"
    )


def exibir_historico(historico):
    """Exibe todas as decisões registradas no histórico."""
    print("\n=== HISTÓRICO DO CICLO ===")

    if len(historico) == 0:
        print("Nenhuma decisão foi registrada.")
    else:
        for numero, registro in enumerate(historico, start=1):
            print(f"Ciclo {numero}")
            print(f"Escolha feita: {registro['escolha']}")
            print(formatar_estado(registro["estado"]))