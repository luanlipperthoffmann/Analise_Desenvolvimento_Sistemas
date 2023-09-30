#10. Consumo de Combustível: Solicite ao usuário a distância percorrida e a quantidade de combustível usado. Calcule o consumo médio usando Consumo = Distância / Combustível. Mostre o consumo em km/l.

distancia = float(input("Dígite a distância percorrida em km: "))
quantidade_combustivel = float(input("Dígite a quantidade de combustivel utilizado em litros: "))
consumo = distancia/quantidade_combustivel
print(f"O consumo de combustivel foi de: {consumo}Km/l")