#Faça um programa que lê 
# duas notas para cada aluno de 
# duas turmas. 
# Cada turma tem 
# 3 alunos.
#  Armazene os dados em uma matriz M. 
# Cada aluno deve ter três notas (as duas digitadas e a média dessas duas). 
# Calcule a média de cada turma e armazene em um vetor TURMA. 
# Informe qual turma tem maior média,
# quais alunos tiveram média maior que a média de sua turma.

m = []

for i in range(2):
    turma = {'nome':'', 'alunos':[], 'media':0 }
    somaNota = 0
    turma['nome'] = input('Digite o nome da turma: ')
    for j in range(2):
        aluno = {'nome':'', 'notas':[]}
        notas = []
        aluno['nome'] = input('Digite o nome do aluno: ')
        notas.append(float(input('Digite a primeira nota: ')))
        notas.append(float(input('Digite a segunda nota: ')))
        notas.append(notas[0] + notas[1] / 2)
        aluno['notas'].append(notas)
        turma['alunos'].append(aluno)
    somaNota += notas[2] 
    turma['media'] = notas[2] / 3
    m.append(turma)

for i in m:
    print(i)