# Simulador: Missão Orbital: Decisões na Nave
# Grupo: Roberto, Eduardo, João e Mateus
# Entrega 3: versão com repetição, encerramento e histórico.

from roberto import exibir_titulo, exibir_status, exibir_menu, exibir_resultado
from eduardo import aplicar_decisao, aplicar_desgaste_ciclo, escolha_valida
from joao import verificar_limites, verificar_encerramento, obter_resultado
from mateus import registrar_historico, exibir_historico

# Dicionário com as 5 variáveis principais do estado da nave.
estado = {
    "oxigenio": 100,
    "energia": 100,
    "integridade": 100,
    "moral": 80,
    "distancia": 0
}

# Lista usada para guardar as decisões tomadas pelo usuário.
historico = []

# Tupla com as 3 opções fixas do menu.
OPCOES = (
    "Manter rota segura",
    "Acelerar motores",
    "Fazer manutenção e cuidar da tripulação"
)

LIMITE_CICLOS = 10
ciclo = 1

# Fluxo principal da Entrega 3: repete ciclos até vitória, derrota ou limite.
exibir_titulo()

while ciclo <= LIMITE_CICLOS and not verificar_encerramento(estado):
    print(f"\n******** CICLO {ciclo} DE {LIMITE_CICLOS} ********")
    exibir_status(estado)
    exibir_menu(OPCOES)

    escolha = input("\nSua escolha (1, 2 ou 3): ")

    if not escolha_valida(escolha):
        exibir_resultado("Opção inválida. Digite apenas 1, 2 ou 3.")
        continue

    mensagem_decisao = aplicar_decisao(estado, escolha)
    mensagem_desgaste = aplicar_desgaste_ciclo(estado, escolha)

    verificar_limites(estado)
    registrar_historico(historico, ciclo, escolha, estado)

    exibir_resultado(mensagem_decisao)
    print(mensagem_desgaste)

    ciclo += 1

exibir_status(estado)
exibir_resultado(obter_resultado(estado, ciclo - 1, LIMITE_CICLOS))
exibir_historico(historico)

print("\nsimulador com repetição executado.")
