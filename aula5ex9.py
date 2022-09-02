# Faça um programa que leia uma matriz 3x3 que representa um tabuleiro de jogo da velha
# indique qual posição deveria ser jogada para ganhar o jogo (se possível) ou ao menos evitar uma derrota.


def pedeNomeJogador():
    nome1 = input("Informe o nome do jogador 1: ")
    nome2 = input("informe o nome do Jogador 2: ")
    jogador1 = {"nome": nome1, "simbulo": "X"}
    jogador2 = {"nome": nome2, "simbulo": "O"}
    return [jogador1,jogador2]


def regras():
    print("\nBem vindo ao jogo da Velha\n")
    print("O jogador que preencher uma linha, coluna ou eixo veritical ganha!")
    print("\nDigite as cordenadas da jogada no formato x,y\n")

def imprimeTabuleiro (tabuleiro):
    for linha in tabuleiro:
        print(linha)

def trocaJogador(jogadorAtivo, jogador1, jogador2):
    if jogadorAtivo["nome"] == jogador1["nome"]:
        return jogador2
    else:
        return jogador1

def movimentoValido(tabuleiro, posicao):
    x = posicao.split(",")[0]
    y = posicao.split(",")[1]
    if x > 2 or x < 0 or y > 2 or y < 0 or tabuleiro[x][y] != "":
        return False
    else:
        return True

def verificaVencedor(tabuleiro):
    for i in range(tabuleiro):
        if (tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]) or (
            tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i]
            or (
                tabuleiro[0, 0] == tabuleiro[1, 1] == tabuleiro[2][2]
                or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[1][0]
            )
        ):
            return True
        else:
            return False

def jogada(jogador):
    cordenadas = input(f"Jogador {jogador['nome']} Digite a cordenada para jogar")
    return cordenadas

def inicio():
    regras()
    jogadores = pedeNomeJogador()
    jogadorAtivo = jogadores[0]
    fimJogo = False
    while(fimJogo != True):
        tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]
        evalidMov = False
        while(evalidMov != True):
            imprimeTabuleiro(tabuleiro)
            evalidMov = 
        fimJogo = True

inicio()
