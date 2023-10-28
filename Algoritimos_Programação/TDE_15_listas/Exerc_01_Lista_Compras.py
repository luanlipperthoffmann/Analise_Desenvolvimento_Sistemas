'''1. Lista de Compras:
    - Desenvolva um programa que permita ao usuário criar uma lista de compras. O programa deve oferecer as seguintes opções no menu:
    1. Adicionar um item à lista.
    2. Remover um item da lista.
    3. Exibir a lista de compras.
'''

frutas=[]
opcao=0
while opcao !=9:
    print("\n=========================================================================")
    print("1 - Para add frutas")
    print("2 - Para remover frutas")
    print("3 - Para mostrar a quantidade")
    print("4 - Para mostrar a lista")
    print("9  - Para sair")
    print("=========================================================================")
    opcao=int(input("O que voçê quer fazer? "))
    if opcao==1:
        frutas.append(input("Qual fruta adicionar? "))
    elif opcao==2:
        frutas.remove(input("Qual fruta remover? "))
    elif opcao==3:
        print(f"Tamanho da lista:{len(frutas)} ")
    elif opcao==4:
        print(f"Frutas: {frutas}")
        for fruta in frutas:
            print(f"Frutas:{fruta}")
    elif opcao==9:
        print("Obrigado, \nAté mais!")
    else: 
        print("Comando invalido!")