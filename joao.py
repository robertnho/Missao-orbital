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


def obter_resultado(estado):
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

    return "A missão continua. Esta versão executa apenas 1 ciclo completo."