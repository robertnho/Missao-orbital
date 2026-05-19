# Simulador: Missão Orbital: Decisões na Nave
# Grupo: Roberto, Eduardo, João e Mateus
# Entrega 2: versão inicial com 1 ciclo completo.

from roberto import exibir_titulo, exibir_status, exibir_menu, exibir_resultado
from eduardo import aplicar_decisao, aplicar_desgaste_ciclo
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

# Fluxo principal da Entrega 2: apenas 1 ciclo completo, sem loop while.
exibir_titulo()
exibir_status(estado)
exibir_menu(OPCOES)

escolha = input("\nSua escolha (1, 2 ou 3): ")

mensagem_decisao = aplicar_decisao(estado, escolha)
mensagem_desgaste = aplicar_desgaste_ciclo(estado, escolha)

verificar_limites(estado)
registrar_historico(historico, escolha, estado)

exibir_resultado(mensagem_decisao)
print(mensagem_desgaste)

exibir_status(estado)
exibir_resultado(obter_resultado(estado))
exibir_historico(historico)

# Nesta entrega ainda não usamos repetição.
# O loop while será adicionado na Entrega 3.
print("\nFim da Entrega 2: 1 ciclo completo executado.")