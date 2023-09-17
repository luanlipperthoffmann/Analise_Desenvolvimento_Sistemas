'''Missão Espacial de Abastecimento:
Você faz parte da equipe de logística de uma missão espacial que está planejando uma viagem à
Lua. Sua tarefa é determinar a quantidade de suprimentos e combustível necessários,
considerando vários fatores.
1. `numAstronautas`: Número de astronautas na missão.
2. `diasMissao`: Duração total da missão em dias.
3. `consumoOxigenio`: Consumo diário médio de oxigênio por astronauta em litros.
4. `consumoAgua`: Consumo diário médio de água por astronauta em litros.
5. `consumoComida`: Consumo diário médio de comida por astronauta em quilogramas.
6. `pesoFoguete`: Peso do foguete vazio em quilogramas.
7. `eficienciaCombustivel`: Eficiência do combustível (quantos quilômetros por litro).
8. `distanciaLua`: Distância média da Terra à Lua em quilômetros (384.400 km).
9. `reservaEmergencia`: Porcentagem de suprimentos extras para emergências.
10. `capacidadeTanque`: Capacidade máxima do tanque de combustível em litros.
Fórmulas:
1. Suprimentos de oxigênio: `numAstronautas * diasMissao * consumoOxigenio * (1 +
reservaEmergencia/100)`
2. Suprimentos de água: `numAstronautas * diasMissao * consumoAgua * (1 +
reservaEmergencia/100)`
3. Suprimentos de comida: `numAstronautas * diasMissao * consumoComida * (1 +
reservaEmergencia/100)`
4. Combustível necessário para a viagem (ida e volta): `(2 * distanciaLua / eficienciaCombustivel)`
Entrada:
O programa deve coletar todas as 10 variáveis acima do usuário.
Saída:
O programa deve informar:
1. A quantidade total de oxigênio, água e comida necessária para a missão.
2. Se a quantidade de combustível necessária para a viagem (considerando ida e volta) excede a
capacidade do tanque.
3. O peso total dos suprimentos e se isso pode ser uma preocupação para o lançamento (uma
simplificação: considere um problema se o peso total dos suprimentos exceder 10% do peso do
foguete).'''

numAstronautas = int(input("Número de astronautas na missão\n"))
diasMissao = int (input("Duração total da missão em dias\n"))
consumoOxigenio = float(input("Consumo diário médio de oxigênio por astronauta em litros\n"))
consumoAgua = float(input("Consumo diário médio de água por astronauta em litros\n"))
consumoComida = float(input("Consumo diário médio de comida por astronauta em quilogramas\n"))
pesoFoguete = float (input("Peso do foguete vazio em quilogramas\n"))
eficienciaCombustivel = float (input("Eficiência do combustível (quantos quilômetros por litro)\n"))
distanciaLua = int (input("Distância média da Terra à Lua em quilômetros (384.400 km)\n"))
reservaEmergencia = int (input("Porcentagem de suprimentos extras para emergências\n"))
capacidadeTanque = int (input("Capacidade máxima do tanque de combustível em litros \n"))
suprimentosOxigenio = (numAstronautas * diasMissao * consumoOxigenio * (1 +
reservaEmergencia/100))
suprimentosAgua = (numAstronautas * diasMissao * consumoAgua * (1 +
reservaEmergencia/100))
suprimentosComida = (numAstronautas * diasMissao * consumoComida * (1 +
reservaEmergencia/100))
quantidadeTotal = suprimentosOxigenio + suprimentosAgua + suprimentosComida
idaVolta = (2 * distanciaLua / eficienciaCombustivel)
exesso = ((pesoFoguete*0.1) + pesoFoguete)
print(f"A quantidade total de comida para a missão é de {quantidadeTotal:.2f}")
if idaVolta <= capacidadeTanque and quantidadeTotal <= exesso:
    print(f"A quantidade de combustível de {idaVolta:.2f} necessária para a viagem, considerando ida e volta, está dentro da capacidade do tanque de {capacidadeTanque:.2f} \nO peso total dos suprimentos de {quantidadeTotal:.2f} está dentro do maximo permitido pelo foguete de {exesso:.2f}")
else:
    print(f"A quantidade de combustível de {idaVolta:.2f} necessária para a viagem, considerando ida e volta, está acima da capacidade do tanque de {capacidadeTanque:.2f} ou 0 peso total dos suprimentos de {quantidadeTotal:.2f} está acima do maximo permitido pelo foguete de {exesso:.2f}")