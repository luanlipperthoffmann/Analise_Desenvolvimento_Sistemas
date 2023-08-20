# 23. Calculadora de IMC: Solicite ao usuário seu peso em quilogramas e altura em metros. Calcule o IMC. Mostre o IMC calculado.

peso = float(input("Dígite o seu peso em kg: "))
altura = float (input("Dígite a sua altura em metros: "))
imc = peso/(altura*altura)
print (f"O Seu IMC é de: {imc}")
if imc<18.5:
    print("Voçê está magro")
elif imc==18.5 or imc<24.9:
    print("Voçê está no peso ideal")
elif imc==24.9 or imc<29.9:
    print("Voçê está acima do peso")
elif imc>=29.9:
    print("Voçê está obeso")


