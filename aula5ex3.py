# 3)	Faça um programa que leia as dimensões de duas matrizes A e B,
#  depois leia as duas matrizes (os elementos devem ser inteiros).
# Se as matrizes forem de tamanhos compatíveis para multiplicação,
#  multiplique as matrizes.
# Imprima as matrizes A, B e a matriz resultante da multiplicação.

matrizA = []
matrizB = []
matrizC = []
def pedeDimencoes():
    return input('Digite a dimenção da Matriz (AxB): ')

def pedeDados( dimencaoY,dimencaoX):
    matriz = []
    for i in range(0,dimencaoX ):
        matriz2 = []
        for j in range(0, dimencaoY):
            matriz2.append(int(input(f"({i} - {j}) Digite um numero inteiro:\n")))
        matriz.append(matriz2)
    return matriz


def isPossible(dimA, dimB):
    dimAy = dimA.split("x")[1]
    dimBx = dimB.split("x")[0]
    return dimAy == dimBx

def multiplicaMatriz(matrizA, matrizB):
    matrizC = []
    for i in range(0, len(matrizA)):
        matrizAux =[]
        mult = 0
        for j in range(0, len(matrizA[i])):
            mult += matrizA[i][j]* matrizB[j][i]
        matrizAux.append(mult)
        matrizC.append(matrizAux)
    return matrizC

dimA = pedeDimencoes()
dimB = pedeDimencoes()

if(isPossible(dimA, dimB)):
    matA = pedeDados(int(dimA.split("x")[0]),int(dimA.split("x")[1]))
    matB = pedeDados(int(dimB.split("x")[0]),int(dimB.split("x")[1]))
    matC = multiplicaMatriz(matA,matB)

print(matA)
print(matB)
print(matC)