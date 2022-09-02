# Faça um programa que leia duas matrizes A e B de números inteiros
# verifica se ambas são inversas (ou seja, se a multiplicação de A por B é a matriz identidade).


def pedeDados():
    matriz = []
    for i in range(0, 4):
        matriz2 = []
        for j in range(0, 4):
            numero = float(input(f"Digite um numero inteiro:\n"))
            matriz2.append(numero)
        matriz.append(matriz2)
    return matriz


matriz1 = pedeDados()
print(matriz1)
