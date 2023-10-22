'''Verificação de número positivo: Escreva um programa que leia um número e verifique se ele é positivo ou negativo. Se for positivo, exiba a mensagem "O número é positivo". Caso contrário, exiba "O número é negativo". O Programa encerra ao digitar 0, Ao fim deve exibir a quantidade dos numero pares e a soma de números impares.'''


contador = 0
somador = 0

num = float(input(f"digite o numero:"))
while num != 0:
    if num > 0:
        print(f"o numero é positivo:")
    elif num < 0:
        print (f"o numero é negativo:")

    if num%2 != 0:
        somador += num
    elif num%2 == 0:
        contador += 1
    num = int(input("digite o numero:"))    
print(f"a quantidade dos numeros pares é:{contador}\nas somas de numeros ímpares é:{somador}")