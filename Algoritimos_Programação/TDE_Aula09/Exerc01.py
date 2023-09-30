'''Elabore um programa que leia dois números e some 100 ao maior valor e apresente o resultado.'''

numero_01 = int(input("Dígite o primeiro número: "))
numero_02 = int(input("dígite o segundo número: "))
if numero_01 > numero_02:
    soma = numero_01 + 100
    print(f"O número 1 é o maior, seu resultado total é de {soma}")
elif numero_02 > numero_01:
    soma = numero_02 + 100
    print(f"O número 2 é o maior, seu resultado total é de {soma}")