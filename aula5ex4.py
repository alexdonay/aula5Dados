##Faça um programa que leia uma matriz 3x3 de inteiros 
# e retorne a linha de maior soma. 
# Imprima na tela a matriz, a linha de maior soma e a soma.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def pedeDados(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            matriz[i][j] = int(input(f"Digite um numero inteiro:\n"))

def imprimir(matriz):
    for i in range(0, len(matriz)):
        print(f'{matriz[i]}')  

def somarlinha(arr):
    somalinha =[]
    for i in range(0,len(arr)):
        soma = 0
        for j in range(0,len(arr[i])):
            soma += arr[i][j] 
        somalinha.append(soma)
    return somalinha

def retornaMaiorLinha(Matriz):
    maiorlinha = {"Numerolinha": 0, "valor": 0}
    for i in range(0,3):
        if(maiorlinha['valor']< Matriz[i]):
            maiorlinha["Numerolinha"] = i
            maiorlinha["valor"] = Matriz[i]
        else:
            print(maiorlinha['valor']< Matriz[i])
    return maiorlinha

pedeDados(matriz)
imprimir(matriz)
maiorlinha = (retornaMaiorLinha(somarlinha(matriz)))
print(f'a maior linha é {maiorlinha["Numerolinha"]+1}\na soma é {maiorlinha["valor"]}')
print(f'{matriz[maiorlinha["Numerolinha"]]}')
