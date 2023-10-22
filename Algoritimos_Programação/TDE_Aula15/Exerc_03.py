'''Verificação de números pares: Escreva um programa que leia um número inteiro e verifique se ele é par ou ímpar. Se for par, exiba a mensagem "O número é par". Caso contrário, exiba "O número é ímpar". O Programa encerra ao digitar 0, Ao fim deve exibir a soma dos numero pares e a quantidade de numeros impares.'''

contador = 0
somador = 0
num = int(input(f"digite o numero"))
while num != 0:
    if num%2 == 0:
        somador += num
        print(f"o numero é par:")
    elif num%2 != 0:
        contador+=1
        print (f"o numero é ímpar:")
    num = int(input("digite o numero"))    
print(f"as somas dos numeros pares é:{somador}\na quatidade de numeros ímpares é:{contador}")