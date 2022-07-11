velha = 0
rodadas = 0
jogador1 = 0 
jogador2 = 0
placa_jogador1 = 0
placa_jogador2 = 0
jogardnv = 1
#Entrada
print("------------------------------------------------------")
print("     Seja bem vindo ao jogo Pedra Papel Tesoura")
print("------------------------------------------------------")
print("Obções de Ferramentas")
print("1 - Tesoura")
print("2 - Papel")
print("3 - Pedra")
print("4 - Regras")
print("------------------------------------------------------")


jogador1 = int(input("Jogador 1 - Escolha sua ferramenta:"))

#Processamento
if (jogador1 == 4):
    print("------------------------------------------------------")
    print("As regras são essas")
    print("Tedoura Ganha de papel")
    print("Papel Ganha de Pedra")
    print("Pedra Ganha de tesoura")
    print("Quando é escolhem o mesmo da ninguem ganha")
    print("------------------------------------------------------")
    print("Agora que entendeu  o jogo, bora jogar")
    print("Obções de Ferramentas:")
    print("1 - Tesoura")
    print("2 - Papel")
    print("3 - Pedra")
    print("4 - Regras")   
    print("------------------------------------------------------")
    jogador1 = int(input("Jogador 1 - Escolha sua ferramenta:"))
    jogador2 = int(input("Jogador 2 - Escolha sua ferramenta:"))
else:
    jogador2 = int(input("Jogador 2 - Escolha sua ferramenta:"))

while jogardnv !=2:
    if (jogador1 == 1) and (jogador2 == 2):
        
        print("Jogador 1 Cortou a vitoria do jogador 2")
        print("Jogador 1 WIN")
        placa_jogador1 = placa_jogador1 + 1
        rodadas = rodadas + 1
    elif jogador1 == 2 and jogador2 == 3:
        print("------------------------------------------------------")
        print("Jogador1 sufocou a vitoria do jogador2")
        print("Jogador 1 WIN")
        placa_jogador1 = placa_jogador1 + 1
        rodadas = rodadas + 1
    elif jogador1 == 3 and jogador2 == 1:
        print("------------------------------------------------------")
        print("Jogador1 quebrou a vitoria do jogador2")
        print("Jogador 1 WIN")
#WIN JOGADOR 2   
        placa_jogador1 = placa_jogador1 + 1
        rodadas = rodadas + 1
    elif (jogador2 == 1) and (jogador1 == 2):
        print("------------------------------------------------------")
        print("Jogador 2 Cortou a vitoria do jogador 1")
        print("Jogador 2 WIN")
        placa_jogador2 = placa_jogador2 + 1
        rodadas = rodadas + 1
    elif jogador2 == 2 and jogador1 == 3:
        print("------------------------------------------------------")
        print("Jogador1 sufocou a vitoria do jogador2")
        print("Jogador 2 WIN")
        placa_jogador2 = placa_jogador2 + 1
        rodadas = rodadas + 1
    elif jogador2 == 3 and jogador1 == 1:
        print("------------------------------------------------------")
        print("Jogador1 quebrou a vitoria do jogador2")
        print("Jogador 2 WIN")
        placa_jogador2 = placa_jogador2 + 1
        rodadas = rodadas + 1
#DEU VELHA
    if jogador2 == jogador1 and jogador1 == jogador2:
        print("------------------------------------------------------")
        print("DEU VELHA")
        velha = velha + 1
        rodadas = rodadas + 1
    print("------------------------------------------------------")
    jogardnv=int(input("Deseja jogar novamente? \n 1-Sim \n 2-Não \n Respota: "))
    print("------------------------------------------------------")
#SAIDA
else: 
    print("Em um total de {0} rodada(s) teve:".format(rodadas))
    print("------------------------------------------------------")
    print("Total de {0} Velha1".format(velha))
    print("Total de {0} Vitoria do Jogador 1".format(placa_jogador1))
    print("Total de {0} Vitoria do Jogador 2".format(placa_jogador2))
    print("------------------------------------------------------")
    if placa_jogador1 > placa_jogador2:
        print("Jogador 1 ganhou :)")
    elif placa_jogador1 < placa_jogador2:
        print("Jogador 2 ganhou :)")
    elif placa_jogador1 == 0  or (placa_jogador2 == 0):
        print("------------------------------------------------------")
        print("NINGUEM GANHOU")