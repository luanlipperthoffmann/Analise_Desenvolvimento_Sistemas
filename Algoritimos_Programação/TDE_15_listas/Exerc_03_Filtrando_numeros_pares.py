'''Filtrando Números Pares
    - Construa um programa que permita ao usuário criar uma lista de números e, em seguida, criar uma nova lista contendo apenas os números pares da lista original. O programa deve oferecer as seguintes opções no menu:
    1. Adicionar números à lista.
    2. Criar uma nova lista apenas com os números pares.
    3. Exibir a lista com números pares.
'''

lista=[]
numeros=0
pares=[]
opcao=0
while opcao!=9:
    print("\n=========================================================================")
    print("1 - Para add numeros a lista ")
    print("2 - Para criar uma nova lista apenas usando os números pares digitados ")
    print("3 - Para exibir a lista com so números pares ")
    print("9  - Para sair")
    print("=========================================================================")
    opcao=int(input("O que voçê quer fazer? "))
    if opcao==1:
        lista.append(int(input("Insira um número inteiro: ")))
    elif opcao==2:
        for numeros in lista:
            if numeros%2==0:
                pares.append(numeros)
    elif opcao==3:
        print(pares)
    elif opcao==9:
        print("Obrigado, \nAté mais!")
    else: 
        print("Comando invalido!")