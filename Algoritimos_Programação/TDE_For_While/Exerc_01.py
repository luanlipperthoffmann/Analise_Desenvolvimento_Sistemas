'''Faça um algoritmo que leia a nota de vários alunos de uma turma. Ao final, deve ser escrita a média geral da turma. A leitura das médias somente encerra quando uma nota negativa for digitada.'''

nota=0
quantidade=0
total_notas=0
while nota >= 0:
    nota=float(input("Digite a nota do aluno: "))
    if (nota<0):
        break
    total_notas=total_notas+nota
    quantidade+=1
media = total_notas/quantidade
print(media)