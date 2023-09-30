'''Faça um programa para ler dois valores numéricos e apresentar a diferença do maior pelo
menor.'''

numero_01 = int(input("Dígite o primeiro número: "))
numero_02 = int(input("Dígite o segundo número: "))
if numero_01 > numero_02:
    diferenca = numero_01 - numero_02
    print(f"O número 1 é o maior, a diferença do segundo é de {diferenca}")
elif numero_02 > numero_01:
    diferenca = numero_02 - numero_01
    print(f"O número 2 é o maior, a diferença é de {diferenca}")