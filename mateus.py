# Responsável: Mateus
# Responsabilidade: registrar e exibir o histórico das decisões.


def registrar_historico(historico, ciclo, escolha, estado):
    """Registra o ciclo, a escolha feita e uma cópia do estado atual no histórico."""
    registro = {
        "ciclo": ciclo,
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
    print("\n=== HISTÓRICO DOS CICLOS ===")

    if len(historico) == 0:
        print("Nenhuma decisão foi registrada.")
    else:
        for registro in historico:
            print(f"Ciclo {registro['ciclo']}")
            print(f"Escolha feita: {registro['escolha']}")
            print(formatar_estado(registro["estado"]))
