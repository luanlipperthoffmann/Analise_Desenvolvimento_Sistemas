'''Faça um programa para repetir a leitura de um número enquanto o valor fornecido for diferente de 0. Para cada número fornecido, escrever se ele é NEGATIVO ou POSITIVO. Quando o número 0 for fornecido a repetição deve ser encerrada sem escrever mensagem alguma.'''

numero=1
contador = 0
while numero <0 or numero>0:
    numero=int(input("Digite um numero : "))
    if (numero >0):
        print(f"O número {numero} é positivo")
    elif (numero <0):
        print(f"O número {numero} é negativo")
    contador+=1
