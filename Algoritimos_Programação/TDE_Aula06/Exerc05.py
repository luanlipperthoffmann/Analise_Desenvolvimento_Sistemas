#Verificar se um número é múltiplo de 5
numero = int(input("Informe um número: "))
resto = numero%5
if resto == 0:
    print(f"O numero {numero} é multiplo por 5")
elif resto > 0:
    print(f"O numero {numero} não é multiplo por 5")