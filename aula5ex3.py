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

def multiplicaMatriz(matrizA, matrizB):
    matriz = []
    for i in range(0,len(matrizA)):
        matriz2 = []
        for j in range(0,len(matrizA[i])):
            matriz2.append(matrizA[i][j] * matrizB[i][j])
        matriz.append(matriz2)
        matriz2 =[]
    return matriz

def exibeDados(matriz, matrizNome):
    print(f'a matriz é a {matrizNome}')
    for i in range(0,len(matriz)):
        print (matriz[i])

dimencaoA = input('Digite a dimentecao da matriz A fomato AXB')
dimencaoB = input('digite a dimentecao da matriz B formato AXB')

if(dimencaoA != dimencaoB):
    print('a matriz A não é compativel com a matriz B')
else:
    dimencaoX = int(dimencaoA.split('x')[0])
    dimencaoY = int(dimencaoA.split('x')[1])
    matrizA = pedeDados(dimencaoX, dimencaoY)
    matrizB = pedeDados(dimencaoX, dimencaoY)
    matrizC = multiplicaMatriz(matrizA, matrizB)
    exibeDados(matrizA, "MatrizA")
    exibeDados(matrizB, "matrizB")
    exibeDados(matrizC, "matrizC")