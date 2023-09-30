#Verificar se um número é positivo, negativo ou zero

numero = int(input("Informe um número: "))
if numero > 0:
    print(f"o número {numero} é positivo")
elif numero < 0:
    print(f"o número {numero} é negativo")
elif numero == 0:
    print(f"o número é {numero}")