#Verificar se um número é par ou ímpar.

numero = int(input("Informe um número: "))
resto = numero%2
if resto == 0:
    print(f"O numero {numero} é par")
elif resto > 0:
    print(f"O numero {numero} é impar")
else:
    print("Zero")