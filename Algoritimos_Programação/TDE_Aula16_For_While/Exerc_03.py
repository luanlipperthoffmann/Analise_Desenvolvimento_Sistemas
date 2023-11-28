'''Faça um programa para ler uma quantidade indeterminada de valores inteiros. Para cada valor fornecido escrever uma mensagem que indica se cada valor fornecido é PAR ou ÍMPAR. O programa será encerrado imediatamente após a leitura de um valor NULO (zero) ou NEGATIVO.'''

numero=1
contador = 0
while numero>0:
    numero=int(input("Digite um numero : "))
    if (numero % 0):
        print(f"O número {numero} é par")
    elif (numero % 1):
        print(f"O número {numero} é impar")
    contador+=1
