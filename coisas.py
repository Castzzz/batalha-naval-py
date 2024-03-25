#Trabalho Final - Batalha Naval


import random

print("Batalha Naval\n")

regras = input("Digite R para ver as regras ou então aperte qualquer outra tecla para começar: ")
if regras == "R":
    print("Batalha naval é um jogo de tabuleiro de dois jogadores, no qual os jogadores têm de adivinhar em que quadrados estão os navios do oponente;\n\n"
    "* O jogador1 começa atacando alguma cordenada dada por uma letra entre A e J e logo em seguida um numero de 0 a 9;\n"
    "* Se o jogador1 acertar ele jogará de novo, se não a vez é passada ao jogador2;\n"
    "* O jogo acaba quando o primeiro jogador afundar todas as embarcações;\n" 
    "* Use o comando: 'sair' se deseja sair da partida;\n"
    "* Use o comando: reiniciar se deseja 'reiniciar' a partida;\n"
    "* Use o comando embarcacoes se deseja ver quantas embarcações foram afundadas.\n\n")

input("Digite qualquer tecla para continuar...")

linhas = 10
colunas = 10
vet = [0] * colunas
vet_mapa = ["~"] * colunas
matriz = []
matriz2 = []
mapa = []
mapa2 = []
cont = 0

#Tamanho das embarcações
porta_aviao = 5
navio_tanque = 4
contra_torpedeiros = 3
submarino = 2

#Contador de embarcações
cont_porta_aviao = 0
cont_navio_tanque = 0
cont_contra_torpedeiros = 0
cont_submarino = 0

p_jog01 = 0
P_jog02 = 0

cont_port = 1
cont_navTanque = 2
cont_contraTorp = 3
cont_sub = 4

def imprimi_mapa(mapa, mapa2):
    abecedario = "ABCDEFGHIJKLMNOPQRST"
    print("jogador 1")
    for i in range(len(mapa)):
        letra = abecedario[i]
        print(f"   {(letra)}", end=" ")
    print()
    for fila in range(len(mapa)):
        print(f"{fila} {mapa[fila]}")
    print("-"*52)
    print("jogador 2")
    for i in range(len(mapa2)):
        letra = abecedario[i]
        print(f"   {(letra)}", end=" ")
    print()
    for fila in range(len(mapa2)):
        print(f"{fila} {mapa2[fila]}")

while cont < linhas:
    matriz.append(vet.copy())
    mapa.append(vet_mapa.copy())
    matriz2.append(vet.copy())
    mapa2.append(vet_mapa.copy())
    cont += 1
    
def gerar_embarcações(matriz):
    while cont_porta_aviao < porta_aviao:
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
        matriz[lin][col] = 5
        cont_porta_aviao += 1

    while cont_navio_tanque < navio_tanque:
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
        while(matriz[lin][col] == 1):
            lin = random.randint(0, linhas - 1)
            col = random.randint(0, colunas - 1)
        matriz[lin][col] = 4
        cont_navio_tanque += 1

    while cont_contra_torpedeiros < contra_torpedeiros:
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
        while(matriz[lin][col] == 1):
            lin = random.randint(0, linhas - 1)
            col = random.randint(0, colunas - 1)
        matriz[lin][col] = 3
        cont_contra_torpedeiros += 1

    while cont_submarino < submarino:
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
        while(matriz[lin][col] == 1):
            lin = random.randint(0, linhas - 1)
            col = random.randint(0, colunas - 1)
        matriz[lin][col] = 2
        cont_submarino += 1
    return matriz

def jogo1(linha, coluna):
    jog_01 = 0
    if matriz2[linha -1][coluna - 1] == 0:
        print("Você acertou a água... trouxa")
        matriz2[lin_jog-1][col_jog-1] = "*"
        mapa2[lin_jog-1][col_jog-1] = "*"
        acertou = False
    elif matriz2[linha - 1][coluna - 1] == 5:
        print("(っ◕‿◕)っ Você acertou um porta aviões!!!")
        matriz2[lin_jog-1][col_jog-1] = "x"
        mapa2[lin_jog-1][col_jog-1] = "x"
        acertou = True
    elif matriz2[linha - 1][coluna - 1] == 4:
        print("(っ◕‿◕)っ Você acertou minha casa!!!")
        matriz2[lin_jog-1][col_jog-1] = "x"
        mapa2[lin_jog-1][col_jog-1] = "x"
        acertou = True
    elif matriz2[linha - 1][coluna - 1] == 3:
        print("(っ◕‿◕)っ Você acertou um contra torpedeiro!!!")
        matriz2[lin_jog-1][col_jog-1] = "x"
        mapa2[lin_jog-1][col_jog-1] = "x"
        acertou = True
    elif matriz2[linha - 1][coluna - 1] == 2:
        print("(っ◕‿◕)っ Você acertou um submarino!!!")
        matriz2[lin_jog-1][col_jog-1] = "x"
        mapa2[lin_jog-1][col_jog-1] = "x"
        acertou = True
    elif matriz2[linha - 1][coluna - 1] == "*" or matriz2[linha - 1][coluna - 1] == "x":
        print("Essa posição já foi bombardeada! Você está sendo burro")
        print("Aguarde a próxima jogada")
        acertou = False
    elif matriz2[linha - 1][coluna - 1] <= 0 and matriz2[linha - 1][coluna - 1] >= 11:
        print("Essa posição não existe no mapa! Tá perdido meu parceiro?\nDigite uma posição de 0 até 10")
        print("Você se fudeu")
        acertou = False
    return(jog_01, acertou)

def jogo2(linha, coluna):
    jog_02 = 0
    if matriz[linha -1][coluna - 1] == 0:
        print("Você acertou a água... trouxa")
        matriz[lin_jog-1][col_jog-1] = "*"
        mapa[lin_jog-1][col_jog-1] = "*"
        acertou = False
    elif matriz[linha - 1][coluna - 1] == 5:
        print("(っ◕‿◕)っ Você acertou um porta aviões!!!")
        matriz[lin_jog-1][col_jog-1] = "x"
        mapa[lin_jog-1][col_jog-1] = "x"
        acertou = True
    elif matriz[linha - 1][coluna - 1] == 4:
        print("(っ◕‿◕)っ Você acertou minha casa!!!")
        matriz[lin_jog-1][col_jog-1] = "x"
        mapa[lin_jog-1][col_jog-1] = "x"
        acertou = True
    elif matriz[linha - 1][coluna - 1] == 3:
        print("(っ◕‿◕)っ Você acertou um contra torpedeiro!!!")
        matriz[lin_jog-1][col_jog-1] = "x"
        mapa[lin_jog-1][col_jog-1] = "x"
        acertou = True
    elif matriz[linha - 1][coluna - 1] == 2:
        print("(っ◕‿◕)っ Você acertou um submarino!!!")
        matriz[lin_jog-1][col_jog-1] = "x"
        mapa[lin_jog-1][col_jog-1] = "x"
        acertou = True
    elif matriz[linha - 1][coluna - 1] == "*" or matriz[linha - 1][coluna - 1] == "x":
        print("Essa posição já foi bombardeada! Você está sendo burro")
        print("Aguarde a próxima jogada")
        acertou = False
    elif matriz[linha - 1][coluna - 1] <= 0 and matriz[linha - 1][coluna - 1] >= 11:
        print("Essa posição não existe no mapa! Tá perdido meu parceiro?\nDigite uma posição de 0 até 10")
        print("Você se fudeu")
        acertou = False
    return(jog_02, acertou)


while True:
    print("")
    print("Player 1 é sua vez!")
    imprimi_mapa(mapa, mapa2)
    print("Letras maiusculas, por favor :)")
    print("Siga esse formato de coordenada: X,Y")
    col_jog = input("Digite uma coordenada: ")
    if col_jog == "sair":
        exit()
    elif col_jog == "reiniciar":
        jogo1(lin_jog, int(col_jog))
    c = col_jog.split(",")
    col_jog = c[0]
    lin_jog = int(c[1]) + 1
    if col_jog == "A":
        col_jog = 1
    elif col_jog == "B":
        col_jog = 2
    elif col_jog == "C":
        col_jog = 3
    elif col_jog == "D":
        col_jog = 4
    elif col_jog == "E":
        col_jog = 5
    elif col_jog == "F":
        col_jog = 6
    elif col_jog == "G":
        col_jog = 7
    elif col_jog == "H":
        col_jog = 8
    elif col_jog == "I":
        col_jog = 9
    elif col_jog == "J":
        col_jog = 10
    print("-"*30)
    jogador01 = int(jogo1(lin_jog, int(col_jog))[0])
    matriz[lin_jog-1][col_jog-1] = "x"
    p_jog01 += jogador01
    if jogador01 == 5:
        cont_port -= 1
    if jogador01 == 4:
        cont_navTanque -= 1
    if jogador01 == 3:
        cont_contraTorp -= 1
    if jogador01 == 2:
        cont_sub -= 1
    print(f"O player 1 tem {p_jog01} pontos")

    print("-"*30)

    print("Player 2, é a sua vez!!!")
    imprimi_mapa(mapa, mapa2)
    print("Letras minusculas, por favor :)")
    col_jog = input("Digite uma coordenada: ")
    if col_jog == "sair":
        exit()
    elif col_jog == "reiniciar":
        jogo2(lin_jog, int(col_jog))
    c = col_jog.split(",")
    col_jog = c[0]
    lin_jog = int(c[1]) + 1
    if col_jog == "A":
        col_jog = 1
    elif col_jog == "B":
        col_jog = 2
    elif col_jog == "C":
        col_jog = 3
    elif col_jog == "D":
        col_jog = 4
    elif col_jog == "E":
        col_jog = 5
    elif col_jog == "F":
        col_jog = 6
    elif col_jog == "G":
        col_jog = 7
    elif col_jog == "H":
        col_jog = 8
    elif col_jog == "I":
        col_jog = 9
    elif col_jog == "J":
        col_jog = 10
    print("-"*30)
    jogador02 = int(jogo2(lin_jog, int(col_jog))[0])
    matriz[lin_jog-1][col_jog-1] = "x"
    P_jog02 += jogador02
    if jogador02 == 5:
        cont_port -= 1
    if jogador02 == 4:
        cont_navTanque -= 1
    if jogador02 == 3:
        cont_contraTorp -= 1
    if jogador02 == 2:
        cont_sub -= 1
    print(f"O player 2 tem {P_jog02} pontos")
    print("")
    print("-"*30)   
    print(f"porta aviões {cont_port}")
    print(f"navio tanque {cont_navTanque}")
    print(f"contra torpedeiro {cont_contraTorp}")
    print(f"sumarino {cont_sub}")
    if cont_port == 0 and cont_navTanque == 0 and cont_contraTorp == 0 and cont_sub == 0:
        final = input("O jogo acabou, digite sair ou reiniciar para começar um novo jogo...")
        if final == "sair":
            exit()
        elif final == "reiniciar":
            jogo2(lin_jog, int(col_jog))

#coisas a adicionar 
# def mostrar_mapa(tablero):
#     abecedario = "ABCDEFGHIJKLMNOPQRST"
#     for i in range(len(tablero)):
#         letra = abecedario[i]
#         print(f"   {(letra)}", end=" ")
#     print()
#     for fila in range(len(tablero)):
#         print(f"{fila+1} {tablero[fila]}")
        

