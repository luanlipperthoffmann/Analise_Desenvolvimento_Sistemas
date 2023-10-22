'''Cálculo de média: Escreva um programa que leia três notas e calcule a média do aluno. Se a média for maior ou igual a 7, exiba a mensagem "Aprovado". Caso contrário, exiba "Reprovado". O programa encerra ao efetuar 10 leituras ou até o usuário digitar 3 notas zero.'''


contador = 0
for media in range (1,11):
    nota01= float (input("Dígite  a primeira nota do aluno: "))
    nota02= float (input("Dígite  a segunda nota do aluno: "))
    nota03= float (input("Dígite  a terceira nota do aluno: "))
    media =(nota01+nota02+nota03)/3
    contador +=1
    if (nota01==0 and nota02==0 and nota03==0):
        break
    elif media >=7:
        print(f"A sua média do aluno {contador} é: {media:.2f} \nAprovado\n")
    else:
        print(f"A sua média do aluno {contador} é: {media:.2f} \nReprovado\n")