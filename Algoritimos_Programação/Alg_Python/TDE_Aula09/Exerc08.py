'''Faça um programa para efetuar a leitura de quatro números e apresentar os números divisíveis por 2 e por 3'''

numero_01 = int(input("Dígite o número 1: "))
numero_02 = int(input("Dígite o número 2: "))
numero_03 = int(input("Dígite o número 3: "))
numero_04 = int(input("Dígite o número 4: "))

if (numero_01%2)==0 and (numero_01%3)==0:
    print(f"O número 1: {numero_01}. É dívisivel por 2 e 3")
else:
    print("O número 1 não é divisivel por 2 e 3 ")

if (numero_02%2)==0 and (numero_02%3)==0:
    print(f"O número 2: {numero_02}. É dívisivel por 2 e 3")
else:
    print("O número 2 não é divisivel por 2 e 3 ")

if (numero_03%2)==0 and (numero_03%3)==0:
    print(f"O número 3: {numero_03}. É dívisivel por 2 e 3")
else:
    print("O número 3 não é divisivel por 2 e 3 ")

if (numero_04%2)==0 and (numero_04%3)==0:
    print(f"O número 4: {numero_04}. É dívisivel por 2 e 3")
else:
    print("O número 4 não é divisivel por 2 e 3 ")