# Faça um programa para determinar se uma pessoa é maior ou menor de idade.

idade = int (input("Dígite sua idade: "))
if idade >= 18:
    print("Voçê é maior de idade")
elif idade < 0:
    print("A idade dígitada está incorreta. Informe novamente!")
else:
    print("Voçê é menor de idade!")