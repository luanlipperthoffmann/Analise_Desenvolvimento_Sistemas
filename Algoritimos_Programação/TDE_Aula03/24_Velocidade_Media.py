# 24. Velocidade Média: Peça ao usuário o espaço percorrido em metros e o tempo gasto em segundos. Calcule a velocidade média. Apresente o resultado.

metros = float(input("Dígite o espaço percorrido em metros: "))
tempo = int (input("Dígite o tempo gasto em segundos: "))
velocidade_media = tempo/metros
print(f"A velocidade média percorrida é de {velocidade_media}m/s")