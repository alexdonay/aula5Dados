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

def jogada(jogador, tabuleiro):
    jogadavalida = False
    while(jogadavalida == False):
        posicao = input(f"Jogador {jogador['nome']} Digite a cordenada para jogar no formado X,Y ")
        jogadavalida = movimentoValido(tabuleiro, posicao)
    x = int(posicao.split(",")[0])
    y = int(posicao.split(",")[1])
    tabuleiro[x][y] = jogador['simbulo']
    return tabuleiro

def movimentoValido(tabuleiro, posicao):
    x = int(posicao.split(",")[0])
    y = int(posicao.split(",")[1])
    if x > 2 or x < 0 or y > 2 or y < 0 or tabuleiro[x][y] != "":
        return False
    else:
        return True

def verificaVencedor(tabuleiro):
    fim = False
    for i in range(len(tabuleiro)):
        if(tabuleiro[0][i]==tabuleiro[1][i]==tabuleiro[2][i]!="" or
        tabuleiro[i][0]==tabuleiro[i][1]==tabuleiro[i][2]!="" or
        tabuleiro[0][0]==tabuleiro[1][1]==tabuleiro[2][2]!="" or
        tabuleiro[0][2]==tabuleiro[1][1]==tabuleiro[2][0]!=""
        ):
            fim = True
            break
    return fim
    


def trocaJogador(jogadorAtivo, jogadores):
    if jogadorAtivo["nome"] == jogadores[0]["nome"]:
        return jogadores[1]
    else:
        return jogadores[0]


def inicio():
    tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]
    fimJogo = False
    regras()
    
    jogadores = pedeNomeJogador()
    jogadorAtivo = jogadores[0]
    while(fimJogo==False):
        imprimeTabuleiro(tabuleiro)
        tabuleiro = jogada(jogadorAtivo, tabuleiro)
        fimJogo = verificaVencedor(tabuleiro)
        jogadorAtivo = trocaJogador(jogadorAtivo, jogadores)
        
    print("fim do jogo")

  
inicio()
