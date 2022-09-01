## Faça um programa que leia uma matriz 3x3 de inteiros
# e multiplique os elementos da diagonal principal da matriz por um número k.
# Imprima a matriz na tela antes e depois da multiplicação.

destino = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
origem = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
k = 2


def imprimir(matriz):
    for i in range(0, 3):
        print(f"{matriz[i]}")


for i in range(0, 3):
    for j in range(0, 3):
        origem[i][j] = int(input(f"Digite um numero inteiro \n"))
        destino[i][j] = origem[i][j] * k

print("Matriz original")
imprimir(origem)
print("Matriz destino")
imprimir(destino)
