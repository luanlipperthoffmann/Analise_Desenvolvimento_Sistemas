'''Calculadora Simples: Crie uma função que realize operações de adição, subtração, multiplicação e divisão com dois números fornecidos como entrada e retorne o resultado.'''

numero_um = int(input("Informe o primeiro número: "))
numero_dois = int(input("Informe o segundo número: "))

def adicao(numero_um, numero_dois):
    resultado = numero_um+numero_dois
    return resultado

def subtracao(numero_um, numero_dois):
    resultado = numero_um-numero_dois
    return resultado

def multiplicacao(numero_um, numero_dois):
    resultado = numero_um*numero_dois
    return resultado

def divisao(numero_um, numero_dois):
    resultado = numero_um/numero_dois
    return resultado

opcao=0
while opcao!=9:
    opcao = int(input("\nSelecione as opções desejadas: \n1- ADIÇÃO \n2- SUBTRAÇÃO \n3- MULTIPLICAÇÃO \n4- DIVISÃO \n9- SAIR \n"))
    if opcao==1:
        print(f"Resultado da adição é: {adicao(numero_um,numero_dois)}")
    
    if opcao==2:
        print(f"Resultado da subtração é: {subtracao(numero_um,numero_dois)}")
    
    if opcao==3:
        print(f"Resultado da multiplicação é: {multiplicacao(numero_um,numero_dois)}")

    if opcao==4:
        print(f"Resultado da divião é: {divisao(numero_um,numero_dois)}")