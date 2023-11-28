'''Conversor de Celsius para Fahrenheit: Escreva uma função que converta uma temperatura em graus Celsius para graus Fahrenheit.'''

celsius = float(input("Informe a temperatura em graus Celsius: "))
def comversorFahrenheit(celsius):
    fahrenheit = (celsius*1.8) + 32
    return fahrenheit

print(f"A temperature em fahrenheit é de: {comversorFahrenheit(celsius)}ºF")