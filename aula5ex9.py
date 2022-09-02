# Faça um programa que leia uma matriz 3x3 que representa um tabuleiro de jogo da velha
# indique qual posição deveria ser jogada para ganhar o jogo (se possível) ou ao menos evitar uma derrota.

def regras():
    print("\nBem vindo ao jogo da Velha\n")
    print("O jogador que preencher uma linha, coluna ou eixo veritical ganha!")
    print("\nDigite as cordenadas da jogada no formato x,y\n")

def pedeNomeJogador():
    nome1 = input("Informe o nome do jogador 1: ")
    nome2 = input("informe o nome do Jogador 2: ")
    jogador1 = {"nome": nome1, "simbulo": "X"}
    jogador2 = {"nome": nome2, "simbulo": "O"}
    return [jogador1,jogador2]

def imprimeTabuleiro (tabuleiro):
    for linha in tabuleiro:
        print(linha)

def jogada(jogador):
    cordenadas = input(f"Jogador {jogador['nome']} Digite a cordenada para jogar no formado X,Y ")
    return cordenadas

def movimentoValido(tabuleiro, posicao):
    x = int(posicao.split(",")[0])
    y = int(posicao.split(",")[1])
    if x > 2 or x < 0 or y > 2 or y < 0 or tabuleiro[x][y] != "":
        return False
    else:
        return True

def verificaVencedor(tabuleiro):
    for i in range(len(tabuleiro)):
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



def trocaJogador(jogadorAtivo, jogadores):
    if jogadorAtivo["nome"] == jogadores[0]["nome"]:
        return jogadores[1]
    else:
        return jogadores[0]




def inicio():
    tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]
    regras()
    
    imprimeTabuleiro(tabuleiro)
    jogadores = pedeNomeJogador()
    jogadorAtivo = jogadores[0]
    movimentoValido(tabuleiro, jogada(jogadorAtivo))
    jogadorAtivo = trocaJogador(jogadorAtivo, jogadores)
    print(verificaVencedor(tabuleiro))

  
inicio()
