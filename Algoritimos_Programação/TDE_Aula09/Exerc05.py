'''Elabore um programa que lê dois valores e escreve cada um com a mensagem: “É múltiplo de 2” ou “Não é múltiplo de dois”.'''

numero_01 = int(input("Dígite o primeiro número: "))
numero_02 = int(input("dígite o segundo número: "))

resto_1 = numero_01 % 2
if resto_1 == 0:
    print(f"O numero 1: {numero_01}, é multiplo de 2")
else:
    print(f"O numero 1: {numero_01}, não é multiplo de 2")

resto_2 = numero_02 % 2
if resto_2 == 0:
    print(f"O numero 2: {numero_02}, é multiplo de 2")
else:
    print(f"O numero 2: {numero_02}, não é multiplo de 2")