# Faça um programa para ler três valores quaisquer e escrever o maior dos 3

numero_01 = int(input("Dígite o primeiro número: "))
numero_02 = int(input("dígite o segundo número: "))
numero_03 = int(input("dígite o terceiro número: "))
if numero_01 > numero_02 and numero_01 > numero_03:
    print(f"O número 1: {numero_01} é o maior")
elif numero_02 > numero_01 and numero_02 > numero_03:
    print(f"O número 2: {numero_02} é o maior")
elif numero_03 > numero_01 and numero_03 > numero_02:
    print(f"O número 2: {numero_03} é o maior")
else:
    print(f"A dois  números dígitados iguais")

