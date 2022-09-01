#Faça um programa que leia a ordem de uma matriz quadrada A (até 10), 
# leia seus valores e 
# escreva sua transposta AT, onde AT[i][j] = A[j][i].
# Imprimas as matrizes A e AT


matrizA =[]
matrizB =[]
matrizC =[]
def pedeDados(dimencaoX, dimencaoY):
    matriz =[]
    for i in range(0,dimencaoX):
        matriz2 =[]
        for j in range(0,dimencaoY):
            matriz2.append(int(input(f"Digite um numero inteiro:\n")))
        matriz.append(matriz2)
    return matriz

def transpoeMatriz(matrizA):
    matriz = []
    for i in range(0,len(matrizA)):
        matriz2 = []
        for j in range(0,len(matrizA[i])):
            matriz2.append(matrizA[j][i])
        matriz.append(matriz2)
        matriz2 =[]
    return matriz

def exibeDados(matriz, matrizNome):
    print(f'a matriz é a {matrizNome}')
    for i in range(0,len(matriz)):
        print (matriz[i])

dimencaoA = input('Digite a dimentecao da matriz A fomato AXB')
dimencaoX = int(dimencaoA.split('x')[0])
dimencaoY = int(dimencaoA.split('x')[1])

if(dimencaoX != dimencaoY):
    print('a matriz A não é compativel com a matriz B')
else:
    
    matrizA = pedeDados(dimencaoX, dimencaoY)
    matrizC = transpoeMatriz(matrizA)
    exibeDados(matrizA, "A")
    exibeDados(matrizC, "AT")