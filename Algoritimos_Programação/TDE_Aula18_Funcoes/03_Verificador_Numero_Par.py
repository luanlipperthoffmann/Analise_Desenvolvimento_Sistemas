'''Verificador de Número Par: Crie uma função que determine se um número é par ou ímpar e retorne uma mensagem indicando o resultado.'''

numero = int (input("Informe o número desejado: "))
def verificaPar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")
    return numero
print(verificaPar(numero))