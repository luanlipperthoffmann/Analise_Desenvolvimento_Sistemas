#Calcular e exibir a área de um círculo ou de um retângulo (base e altura fornecidas)

base = float (input("Dígite base desejada: "))
altura = float(input("Dígite a altura desejada: "))
raio = float(input("Dígite o raio do circulo desejado: ")) 
circulo = 3.14*(raio*raio)
retangulo = base*altura
print(f"A área do circulo é de: {circulo}, a do retangulo é de: {retangulo}")