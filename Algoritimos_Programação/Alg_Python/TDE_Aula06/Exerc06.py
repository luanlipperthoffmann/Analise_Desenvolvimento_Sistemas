#Calcular e exibir o maior de três números
numero1 = int(input("Informe o número 1: "))
numero2 = int(input("Informe o número 2: "))
numero3 = int(input("Informe o número 3: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"O numero 1 é o maior")
elif numero2 > numero1 and  numero2 >numero3:
    print(f"O numero 2 é o maior")
elif numero3 > numero2 and numero3 > numero1:
    print(f"O numero 3 é o maior")