'''5. Contagem de Palavras
    - Crie um programa que conte quantas vezes cada palavra aparece em uma frase inserida pelo usuário. O programa deve oferecer as seguintes opções no menu:
    1. Inserir uma frase.
    2. Contar e exibir quantas vezes cada palavra aparece.
'''
frase=0
palavras=0
opcao=0
while opcao!=9:
    print("\n=========================================================================")
    print("1 - Insira uma frase")
    print("2- Contar e exibir quantas vezes cada palavra aparece")
    print("=========================================================================")
    opcao=int(input("O que voçê quer fazer? "))   
    if opcao==1:
        frase=(input("Insira uma frase: \n"))
    elif opcao==2:
            palavras=len(frase.split())
            print(f"A quandidade de palavras da frase: {frase}; \né de: {palavras} palavras")
    elif opcao==9:
        print("Obrigado, \nAté mais!")
    else: 
        print("Comando invalido!") 