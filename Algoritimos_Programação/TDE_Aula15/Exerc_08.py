'''Verificação de ano bissexto: Escreva um programa que peça ao usuário um ano e verifique-se ele é bissexto ou não. Um ano é bissexto se for divisível por 4 e não for divisível por 100, exceto quando é divisível por 400. Se o ano for bissexto, exiba a mensagem "O ano é bissexto". Caso contrário, exiba "O ano não é bissexto". O Programa encerra ao digitar 3 anos consecutivos não bissextos.'''


contador = 0
while contador <3:
    ano=int(input("Informe o ano: "))
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        print("Ano Bissexto")
        contador=0
    else:
        print("Não é Ano Bissexto")
        contador+=1