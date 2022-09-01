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
def pedeDados():
    matriz = []
    for i in range(0, 2):
        matriz2 = []
        for j in range(0, 2):
            numero = float(input(f"Digite um numero inteiro:\n"))
            if numero > dados["maiorNumero"]:
                dados["maiorNumero"] = numero
                dados["maiorX"] = i
                dados["mariorY"] = j
            if (numero < dados["menorNumero"] or dados['menorNumero'] ==0):
                dados["menorNumero"] = numero
                dados["menorX"] = i
                dados["menorY"] = j
            matriz2.append(numero)
        matriz.append(matriz2)
    return matriz
print(pedeDados())
print(dados)