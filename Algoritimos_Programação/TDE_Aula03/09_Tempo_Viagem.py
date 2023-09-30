# 9. Tempo de Viagem: Solicite ao usuário a distância de uma viagem em km e a velocidade média esperada em km/h. Calcule o tempo da viagem como Tempo = Distância / Velocidade. #Mostre o tempo previsto.

distancia = float (input("Dígite a distÂncia da viagem em km: "))
velocidade_media = int (input ("Dígite a velocidade média esperada em km/h: "))
tempo = distancia/velocidade_media
print (f"O Tempo previsto da viagem é de: {tempo} horas")