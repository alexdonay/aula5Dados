# Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
# Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor
# e guarde as informações em uma matriz.
# Ao final, o programa deve informar:
# a)	De quem foi a melhor volta da prova, e em que volta
# b)	Classificação final em ordem (1º. o campeão)
# c)	Qual foi a volta com a média mais rápida
corredores = []
dados = {"nome": "", "tempoVolta": []}


def melhorVolta(tempoVolta):
    menorTempo = 0
    for i in range(0, len(tempoVolta)):
        if tempoVolta[i] < menorTempo or menorTempo == 0:
            menorTempo = tempoVolta[i]
    return menorTempo


for y in range(0, 6):
    dados["nome"] = input("Digite o nome do piloto: ")
    for i in range(0, 6):
        dados["tempoVolta"].append(float(input("Digite o tempo da volta: ")))
        dados["menorTempo"] = melhorVolta(dados["tempoVolta"])
    corredores.append(dados)
    dados = {"nome": "", "tempoVolta": []}


def classificar(Classif):
    for i in range(0, len(Classif) - 1):
        for y in range(1, len(Classif)):
            if Classif[i]["menorTempo"] > Classif[y]["menorTempo"]:
                tempoaux = Classif[i]
                Classif[i] = Classif[y]
                Classif[y] = tempoaux
    return corredores


def imprimirGrid(corr):
    print("posiçao - nome - Menor tempo")
    for i in range(0, len(corr)):
        print(f"{i+1} - {corr[i]['nome']} - {corr[i]['menorTempo']}")


imprimirGrid(classificar(corredores))
