# Pedro Augusto Lemos
# Análise e desenvolvimento de sistemas

import random
from pickle import TRUE

#Informações de Jogadores
qtdJogadores = 0
listaJogadores = []
jogadorAtual = 0

#Pontuações e rodada
tiros = 0
cerebros = 0
passos = 0
rodada = 1

#Informações dos dados
dadoVerde = 'CPCTPC'
dadoAmarelo = 'TPCTPC'
dadoVermelho = 'TPTCPT'
listaDados = []

#Adicionando dados no tubo
for i in range(0, 6):
    listaDados.append(dadoVerde)
for i in range(0, 4):
    listaDados.append(dadoAmarelo)
for i in range(0, 3):
    listaDados.append(dadoVermelho)

#Apresentação do jogo
print("\n"f'{"Z O M B I E     D I C E":^50}')
print(f'{"Bem vindo ao jogo Zombie Dice!":^50}' "\n")

#Adicionando jogadores com limite mínimo de 2
while (qtdJogadores < 2):
    qtdJogadores = int(input("Digite a quantidade de jogadores participantes: "))

    if (qtdJogadores < 2):
        print("\nATENÇÃO: Você precisa de no mínimo 2 jogadores\n")

#Nomeando jogadores e os incluindo na lista de jogadores
for i in range(qtdJogadores):
    nomeJogador = input("Informe o nome do jogador " + str(i + 1) + ": ")

    listaJogadores.append(nomeJogador)

while(TRUE):
    #Mensagem de inicio do turno com numero da rodada
    print("\nRodada ",rodada)
    print("Turno do jogador: ",listaJogadores[jogadorAtual])

    for i in range (3):
        tiraDado = random.choice(listaDados) #Escolha aleatória de dados

        if tiraDado == 'CPCTPC':
            corDado = 'Verde'

        elif tiraDado == 'TPCTPC':
            corDado = 'Amarelo'

        else:
            corDado = 'Vermelho'

        print("\nDado sorteado: ",corDado) #Imprime os dados sorteados e identifica a cor
        rolaDado = random.choice(tiraDado) #Escolha aleatória da face dos dados tirados

        #Imprime o lado sorteado e adiciona os pontos de cérebro e tiro
        if rolaDado == 'C':
            print("Lado sorteado: ",rolaDado)
            print("Céééérebro")
            cerebros += 1

        elif rolaDado == 'T':
            print("Lado sorteado: ",rolaDado)
            print("TIRO! Um tiro o atingiu, cuidado!")
            tiros += 1

        else:
            print("Lado sorteado: ",rolaDado)
            print("Você encontrou apenas pegadas")
            passos +=1

    #Imprime pontuação de cérebro e tiro do turno
    print("\nPontuação atual:")
    print("Cérebros: ",cerebros)
    print("Tiros: ",tiros)

    #Escolha entre continuar ou parar o turno e dar a vez ao próximo jogador (*ou finalizar o jogo*)
    continuarTurno = input("\nDeseja continuar jogando? (s = sim / n = não / p = parar jogo): ")
    if continuarTurno == 'n':
        jogadorAtual += 1
        #Reseta os dados para o próximo jogador caso decida parar o turno
        tiros = 0
        cerebros = 0
        passos = 0

        #Condição para passar para proximo jogador ou reinicar uma nova rodada
        if jogadorAtual == qtdJogadores:
            print("\nFim da rodada" ,rodada)
            jogadorAtual = 0
            rodada += 1

    #Reinicia o turno atual caso queira continuar a jogar
    elif continuarTurno == 's':
        print("\nIniciando mais uma rodada do turno atual")
        dadosSorteados = []
    
    #Para o jogo
    else:
        print("\nFim de jogo.")
        break
