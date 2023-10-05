#Crie um programa que solicite ao usuário um número e, em seguida, conte e exiba a quantidade de dígitos desse número usando um loop while.

#Usando for:
numero = str(input("Dígite o numero desejado: "))

contador = 0
for digito in numero:
    contador += 1
print(f"O número digitado tem {contador} dígitos")


#Usando while:
numero = int(input("Dígite o numero desejado: "))

contador = 0
while numero > 0:
    contador += 1
    numero //= 10
print(f"O número digitado tem {contador} dígitos")
