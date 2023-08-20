#1. Conversor de Temperatura: Solicite que o usuário insira uma temperatura em Celsius. Calcule sua conversão para Fahrenheit usando a fórmula F = C * 9/5 + 32. Mostre o resultado.

temperatura= float (input("Dígite a temperatura em celcius:"))
fahrenheit= (temperatura*9)/5 + 32
print(f"A temperatura em Fahrenheit é de : {fahrenheit}")