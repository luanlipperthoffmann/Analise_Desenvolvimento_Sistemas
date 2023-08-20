# 14. Dias, Horas e Minutos: Solicite ao usuário uma quantidade em minutos. Converta essa quantidade para dias, horas e minutos, considerando que um dia tem 24 horas e uma hora tem 60 minutos. Mostre o resultado da conversão.

minutos = int (input("dígite os minutos: "))
dia= (minutos/60)/24
horas= minutos/60
print (f"A quantidade digitada equivale a: {dia} Dias | {horas} Horas | {minutos} Minutos")