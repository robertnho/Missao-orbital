# Responsável: Eduardo
# Responsabilidade: aplicar as decisões escolhidas pelo usuário.


def aplicar_decisao(estado, escolha):
    """Aplica as consequências da escolha do usuário no dicionário estado."""
    if escolha == "1":
        estado["distancia"] += 10
        estado["energia"] -= 8
        estado["oxigenio"] -= 6
        return "Você manteve uma rota segura. A nave avançou de forma equilibrada."

    elif escolha == "2":
        estado["distancia"] += 20
        estado["energia"] -= 20
        estado["integridade"] -= 10
        return "Você acelerou os motores. A nave avançou mais rápido, mas sofreu desgaste."

    elif escolha == "3":
        estado["integridade"] += 15
        estado["moral"] += 10
        estado["energia"] -= 12
        estado["oxigenio"] -= 5
        return "Você fez manutenção e cuidou da tripulação. A nave ficou mais estável."

    else:
        return "Opção inválida. Nenhuma alteração foi aplicada ao estado da nave."


def aplicar_desgaste_ciclo(estado, escolha):
    """Informa que o ciclo foi concluído após a decisão escolhida."""
    if escolha == "1" or escolha == "2" or escolha == "3":
        return "Ciclo concluído. O desgaste foi aplicado pela decisão escolhida."

    return "Sem desgaste de ciclo, pois a escolha foi inválida."


def escolha_valida(escolha):
    """Verifica se a escolha digitada existe no menu do simulador."""
    return escolha == "1" or escolha == "2" or escolha == "3"
