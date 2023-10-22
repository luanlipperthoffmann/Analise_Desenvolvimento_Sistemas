''' Cálculo de imposto: Escreva um programa que leia o salário de um funcionário e calcule o valor do imposto a ser pago, considerando as seguintes faixas salariais: até R$ 1.000,00, isento de imposto; de R$ 1.000,00 a R$ 2.000,00, 10% de imposto; acima de R$ 2.000,00, 20% de imposto. O Programa encerra ao calular 20 funcionários ou se o salario for 0.'''

contador = 0 
for salario in range(1,21):
    salario = float(input("qual o seu salario?"))
    if salario == 0:
        break
    contador+=1
    if salario <= 1000:
        print(f"insento de imposto o funcionario {contador}")
    elif salario > 1000 and salario <=2000:
        imposto = salario*0.1
        print(f"o imposto a ser pago pelo funcionario {contador} é:{imposto}")
    elif salario > 2000:
        imposto =salario*0.2
        print(f"o imposto a ser pago pelo funcionario {contador} é:{imposto}")