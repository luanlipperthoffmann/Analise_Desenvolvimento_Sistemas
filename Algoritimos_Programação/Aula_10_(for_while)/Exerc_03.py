'''Escreva um programa que calcule a soma de todos os números pares de 1 a 100 usando um loop while'''

#Usando o for:
soma = 0
for numero in range (2,101, 2):
    soma+= numero
print(soma)

# Usando o While:
soma = 0
numero = 2
while numero <= 100:
    soma+= numero
    numero += 2
print(soma)
