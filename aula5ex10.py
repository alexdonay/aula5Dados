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
        aluno = {'nome':'', 'notas':[0,0,0]}
        aluno['nome'] = input('Digite o nome do aluno: ')
        aluno['notas'][0] = (float(input('Digite a primeira nota: ')))
        aluno['notas'][1] = (float(input('Digite a segunda nota: ')))
        aluno['notas'][2] = (aluno['notas'][0] + aluno['notas'][1] / 2)
        turma['alunos'].append(aluno)
    somaNota += aluno['notas'][2] 
    turma['media'] = somaNota / 3
    m.append(turma)

for i in m:
    print(f" A turma: {i['nome']} tem a média : {i['media']}")
    for j in i['alunos']:
        o = 0
        if(i['media']<j['notas'][o]):
            print(f" O aluno: {j['nome']} teve a média maior que a média da turma {j['notas'][o]}")
        o += 1
            
            