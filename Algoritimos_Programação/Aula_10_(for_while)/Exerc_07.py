'''Média de Notas: Peça ao usuário para inserir uma série de notas e, em seguida, calcule a média das notas usando um loop while. O loop deve continuar até que o usuário insira uma nota negativa'''
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