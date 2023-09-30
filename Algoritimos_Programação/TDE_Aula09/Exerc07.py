'''Realize um programa que lê um conjunto de 4 valores i, a,
c = int(input("dígite o valor c: "))
lista=[ b, c, onde i é um valor inteiro e positivo e a, b, c, são quaisquer valores reais e os escreva. A seguir:
● Se i=1 escrever os 3 valores a, b, c em ordem crescente;
● Se i=2 escrever os 3 valores a, b, c em ordem decrescente;
● Se i=3 escrever os 3 valores de forma que o maior valor entre a, b, c fica entre os outros dois'''

i = int(input("Dígite o valor i: "))
a = int(input("Dígite o valor a: "))
b = int(input("Dígite o valor b: "))
c = int(input("Dígite o valor c: "))
lista = [a, b,c]
if i == 1:
    lista.sort()
    print(lista)
elif i == 2:
    lista.sort(reverse=True)
    print(lista)
elif i == 3:
    maior = max(lista)
    menor = min(lista)
    segundo_maior = ((sorted(lista, reverse=True)[1]))
    print(menor, maior, segundo_maior)