#3. Volume de um Cilindro: Solicite ao usuário o raio e a altura de um cilindro. Calcule o volume usando Volume = π r^2h. Apresente o volume calculado.

raio = float(input("Dígite o raio do cilindro desejado em metros:"))
altura = float(input("Dígite a altura do cilindro desejado em metros:"))
volume = 3.14*raio*raio*altura
print(f"O volume do cilindro é de: {volume} m³")