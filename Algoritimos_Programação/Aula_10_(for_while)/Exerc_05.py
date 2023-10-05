#Crie um programa que gere a tabuada de multiplicação de um número inserido pelo usuário usando um loop while.

ate = int(input("Até qual número: "))
numero = int (input("Dígite o número da tabuada desejada: "))
multiplicador = 0
while multiplicador < ate:
    multiplicador +=1
    tabuada = numero * multiplicador
    print(f"{numero} x {multiplicador}= {tabuada}")
print("FIM")