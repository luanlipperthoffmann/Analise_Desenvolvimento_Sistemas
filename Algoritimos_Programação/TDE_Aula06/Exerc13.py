# Calcular e exibir o maior de quatro números.

numero1 = int(input("Informe o número 1: "))
numero2 = int(input("Informe o número 2: "))
numero3 = int(input("Informe o número 3: "))
numero4 = int(input("Informe o número 4: "))
if numero1 > numero2 and numero1 > numero3 and numero1 > numero4:
    print(f"O numero 1 é o maior")
elif numero2 > numero1 and  numero2 >numero3 and numero2 > numero4:
    print(f"O numero 2 é o maior")
elif numero3 > numero2 and numero3 > numero1 and numero3 > numero4:
    print(f"O numero 3 é o maior")
elif numero4 > numero1 and numero4 > numero2 and numero4 > numero3:
    print(f"O numero 4 é o maior")