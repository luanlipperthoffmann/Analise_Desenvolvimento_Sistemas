'''
4. Ordenando Números:
    - Escreva um programa que permita ao usuário criar uma lista de números e, em seguida, ordenar essa lista em ordem crescente ou decrescente. O programa deve oferecer as seguintes opções no menu:
    1. Adicionar números à lista.
    2. Ordenar a lista em ordem crescente.
    3. Ordenar a lista em ordem decrescente.
'''

numero=[]
crescente=0
decrescente=0
opcao=0
while opcao!=9:
    print("\n=========================================================================")
    print("1 - Para add numeros a lista ")
    print("2 - Para os numero em ordem crescente ")
    print("3 - Para os numero em ordem decrescente ")
    print("9  - Para sair")
    print("=========================================================================")
    opcao=int(input("O que voçê quer fazer? "))
    if opcao==1:
        numero.append(input("Insira um número inteiro: "))
    elif opcao==2:
            crescente=sorted(numero)
            print(crescente)
    elif opcao==3:
        decrescente=sorted(numero, reverse=True)
        print(decrescente)
    elif opcao==9:
        print("Obrigado, \nAté mais!")
    else: 
        print("Comando invalido!")