# Faça um programa que leia duas matrizes A e B de números inteiros
# verifica se ambas são inversas (ou seja, se a multiplicação de A por B é a matriz identidade).


matrizA = []
matrizB = []
matrizC = []
def verificaIdentidade(matriz1):
    matriz =[]
    dimensaoX = len(matriz1)
    dimensaoY = len(matriz1[0])
    for i in range(dimensaoX):
        matrizAux =[]
        for j in range(dimensaoY):
            if i == j:
                matrizAux.append(1)
            else:
                matrizAux.append(0)
        matriz.append(matrizAux)
    return matriz == matriz1

def pedeDimencoes():
    return input('Digite a dimenção da Matriz (AxB): ')

def pedeDados(dimencaoX,dimencaoY):
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
        for j in range(len(matB[0])):
            for k in range(0,len(matB)):
                print(f"{matrizA[i][k]} * {matrizB[k][j]} = {matrizA[i][k]* matrizB[k][j]}")
                mult += matrizA[i][k]* matrizB[k][j]
            matrizAux.append(mult)
            print(mult)
            mult = 0
        matrizC.append(matrizAux)
    return matrizC


print("Matriz 1")
dimA = pedeDimencoes()
print("matriz 2")
dimB = pedeDimencoes()

if(isPossible(dimA, dimB)):
    matA = pedeDados(int(dimA.split("x")[0]),int(dimA.split("x")[1]))
    matB = pedeDados(int(dimB.split("x")[0]),int(dimB.split("x")[1]))
    matC = multiplicaMatriz(matA, matB)

print(matA)
print(matB)
print(matC)

if(verificaIdentidade(matC)):
    print("A matriz é identidade")
else:           
    print("A matriz não é identidade")
