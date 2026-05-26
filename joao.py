# Responsável: João
# Responsabilidade: verificar limites, vitória e derrota do simulador.


def verificar_limites(estado):
    """Corrige os valores do estado para não ficarem abaixo de 0 ou acima de 100."""
    for chave in estado:
        if estado[chave] < 0:
            estado[chave] = 0
        elif estado[chave] > 100:
            estado[chave] = 100


def verificar_encerramento(estado):
    """Verifica se a missão terminou por vitória ou derrota."""
    if estado["distancia"] >= 100:
        return True

    if estado["oxigenio"] <= 0 or estado["energia"] <= 0 or estado["integridade"] <= 0 or estado["moral"] <= 0:
        return True

    return False


def verificar_limite_ciclos(ciclos_realizados, limite_ciclos):
    """Verifica se o simulador atingiu o limite máximo de ciclos."""
    return ciclos_realizados >= limite_ciclos


def obter_resultado(estado, ciclos_realizados=0, limite_ciclos=0):
    """Retorna uma mensagem explicando o resultado atual da missão."""
    if estado["distancia"] >= 100:
        return "Vitória! A nave chegou ao destino final."

    if estado["oxigenio"] <= 0:
        return "Derrota! O oxigênio acabou."

    if estado["energia"] <= 0:
        return "Derrota! A energia da nave acabou."

    if estado["integridade"] <= 0:
        return "Derrota! A nave perdeu sua integridade."

    if estado["moral"] <= 0:
        return "Derrota! A moral da tripulação chegou ao nível crítico."

    if limite_ciclos > 0 and verificar_limite_ciclos(ciclos_realizados, limite_ciclos):
        return "Fim da missão! O limite de ciclos foi atingido antes da chegada ao destino."

    return "A missão continua."
