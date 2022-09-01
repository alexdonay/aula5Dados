# 7)	Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
# a)	o maior elemento da matriz e sua respectiva posição (linha e coluna);
# b)	o menor elemento da matriz e sua respectiva posição.
dados = {
    "maiorNumero": 0,
    "maiorX": 0,
    "mariorY": 0,
    "menorNumero": 0,
    "menorX": 0,
    "menorY": 0,
}
def maiorNumero(array = []):
    for i in range(0, 2):
        for j in range(0, 2):
            if array[i][j] > dados["maiorNumero"]:
                dados["maiorNumero"] = array[i][j]
                dados["maiorX"] = i
                dados["mariorY"] = j
def menorNumero(array = []):
    for i in range(0, 2):
        for j in range(0, 2):
            if (array[i][j] < dados["menorNumero"] or dados['menorNumero'] ==0):
                    dados["menorNumero"] = array[i][j]
                    dados["menorX"] = i
                    dados["menorY"] = j
def pedeDados():
    matriz = []
    for i in range(0, 2):
        matriz2 = []
        for j in range(0, 2):
            numero = float(input(f"Digite um numero inteiro:\n"))
            matriz2.append(numero)
        matriz.append(matriz2)
    return matriz

data = pedeDados()
maiorNumero(data)
menorNumero(data)
print(dados)
