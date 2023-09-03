#Verificar se um número é divisível por 3 e 5 ao mesmo tempo.

numero = int(input("Informe o numero desejado: \n"))
divisao3 = numero%3
divisao5 = numero%5

if divisao3 == 0 and divisao5 == 0 and numero > 0:
    print(f"O número {numero} é divisivel por 3 e 5.")
elif divisao3 > 0 or divisao5 > 0:
    print(f"O número {numero} não é divisivel por 3 e 5.")
elif numero == 0:
    print(f"O número {numero} não é um valor divisivel por nada!")