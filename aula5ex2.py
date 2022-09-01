#Faça um programa que leia duas matrizes A e B 2x2 de inteiros 
#imprima a matriz C que é a soma das matrizes A e B.

matrizA = [[0,0],[0,0]]
matrizB = [[0,0],[0,0]]
matrizC = [[0,0],[0,0]]

def pedeDados(matriz):
    for i in range(0,2):
        for j in range(0,2):
            matriz[i][j] = int(input(f"Digite um numero inteiro:\n"))

pedeDados(matrizA)
pedeDados(matrizB)

for i in range(0,2):
    for j in range(0,2):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

print("Matriz destino")
for i in range(0,2):
    print(f'{matrizC[i]}') 
