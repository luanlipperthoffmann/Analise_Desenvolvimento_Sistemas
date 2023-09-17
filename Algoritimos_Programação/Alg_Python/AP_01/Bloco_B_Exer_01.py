'''1. Conversão de Temperatura:
Você foi contratado para fazer um software meteorológico. Uma das funcionalidades mais pedidas pelos usuários é a conversão de temperaturas de Celsius para Fahrenheit.
Entrada:
O programa deve solicitar ao usuário uma temperatura em graus Celsius.
Saída:
O programa deve mostrar a temperatura convertida em Fahrenheit.
Fórmula:
F = (C * 9/5) + 32'''

celsius = float(input("Informe a temperatuera em graus celsius: \n"))
fahrenheit = (celsius*9/5) + 32
print(f"A temperatura em fehrenheit é de {fahrenheit:.2f} graus")