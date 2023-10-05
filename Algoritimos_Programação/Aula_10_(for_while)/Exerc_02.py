'''Crie um programa que peça ao usuário para digitar um número e, em seguida, exiba a tabuada desse número de 1 a 10 usando um loop wilhe'''


#Usando o for:
numero = int (input("Dígite o número da tabuada desejada: "))
for multiplicador in range (1,11):
    tabuada = numero * multiplicador
    multiplicador*=1
    print(f"{numero} x {multiplicador}= {tabuada}")
print("FIM")

#Usando o while:
numero = int (input("Dígite o número da tabuada desejada: "))
multiplicador = 0
while multiplicador <10:
    multiplicador +=1
    tabuada = numero * multiplicador
    print(f"{numero} x {multiplicador}= {tabuada}")
print("FIM")