'''Faça um programa para ler dois números. Se os números forem iguais imprimir a mensagem: "NÚMEROS IGUAIS" e encerrar a execução; caso contrário, imprimir o de maior valor.'''

numero_01 = int(input("Dígite o primeiro número: "))
numero_02 = int(input("dígite o segundo número: "))
if numero_01 == numero_02:
    print("NÚMEROS IGUAIS!")
elif numero_01 != numero_02 and numero_01 > numero_02:
    print(f"O maior número é o numero 1: {numero_01}")
else:
    print(f"O maior número é o numero 2: {numero_02}")