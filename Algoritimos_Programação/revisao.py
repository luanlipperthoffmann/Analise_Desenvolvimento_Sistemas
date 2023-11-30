'''
1 - e
2 - b
3 - b / c
4 - c
5 - a
6 - c


#Exercicio 07

lista = []
opcao = 0
maior = 0

while opcao != 9:
    try:
        opcao = int(input("1 - add numeros \n2 - Mostrar o maior número \n9 - sair \n"))
        if opcao == 1:
            lista.append (int(input("Digite um numero: ")))
            print(lista)
        elif opcao == 2:  
            maior = max(lista)
            print(f"O maior número digitado é: {maior}")
        elif opcao == 9:
            break
    except:
        print("Valor inválido!")


#Exercicio 08

lista = []
numeros = 0
pares = []
opcao = 0

while opcao !=9:
    try:
        opcao = int(input("1 - add numeros \n2 - Mostrar os números pares \n9 - sair \n"))
        if opcao == 1:
            lista.append (int(input("Digite um numero: ")))
            print(lista)
        elif opcao == 2:  
            for numeros in lista:
                if (numeros % 2 == 0):
                    pares.append(numeros)
            print(f"Os números pares são: {pares}")
        elif opcao == 9:
            break
    except:
        print("Valor inválido!") 


#Exercicio 09
lista = []
opcao = 0
maior = 0

while opcao != 9:
    try:
        opcao = int(input("1 - add numeros \n2 - Remover itens \n3 - Mostrar lista atualizada \n9 - sair \n"))
        if opcao == 1:
            lista.append (int(input("Digite um numero: ")))
            print(lista)
        elif opcao == 2:  
            lista.remove (int(input("Qual número deseja remover da lista: ")))
        elif opcao == 3:
            print(lista)
        elif opcao == 9:
            break
    except:
        print("Valor inválido!")

'''