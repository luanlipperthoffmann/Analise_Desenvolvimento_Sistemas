'''Soma de Números Ímpares: Calcule a soma de todos os números ímpares de 1 a 100 usando um loop while.'''

#Usando o for:
soma = 0
for numero in range (1,101, 2):
    soma+= numero
print(soma)

# Usando o While:
soma = 0
numero = 1
while numero <= 100:
    soma+= numero
    numero += 2
print(soma)