'''2. Média de Notas:
    - Crie um programa que permita ao usuário calcular a média de um conjunto de notas. O programa deve oferecer as seguintes opções no menu:
    1. Adicionar notas à lista.
    2. Calcular a média das notas.
    3. Exibir a média calculada.
'''
nota=[]
media=0
opcao=0
aluno=0
soma=0
while opcao !=9:
    print("\n=========================================================================")
    print("1 - Para add notas a lista ")
    print("2 - Para calcular a média das notas ")
    print("3 - Para exibir a média calculada ")
    print("9  - Para sair")
    print("=========================================================================")
    opcao = int(input("Informe a opção desejada: "))
    if opcao==1:
        nota.append(float(input(f"\nDigite a nota do aluno {aluno}: ")))
        soma = sum(nota)
        aluno+=1
    elif opcao==2:
        media=soma/aluno
    elif opcao==3:
        print(f"A média dos {aluno} é: {media}")
    elif opcao==9:
        print("Obrigado, \nAté mais!")