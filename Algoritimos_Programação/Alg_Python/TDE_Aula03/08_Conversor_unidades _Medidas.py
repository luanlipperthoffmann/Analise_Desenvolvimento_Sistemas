#8. Conversor de Unidades de Medida: Peça ao usuário uma distância em metros. Converta essa distância para centímetros e milímetros. Apresente ambos os valores convertidos.

metros = float(input("Dígite a distância em metros:"))
centrimetros = metros*100
print(f"A distância digitada de: {metros} metros, equivalem a: {centrimetros} centrimetros")
milimetros = metros*1000
print(f"A distância digitada de: {metros} metros, equivalem a: {milimetros} milimetros")