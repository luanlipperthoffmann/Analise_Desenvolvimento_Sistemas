# Verificar se uma pessoa é maior ou menor de idade.
idade = int(input("Dígite sua idade: "))
if idade >= 0 and idade < 18:
    print("Voçê é menor de idade")
elif idade >= 18:
    print("Voçê é maior de idade")
else:
    print("Está não é uma idade valida")