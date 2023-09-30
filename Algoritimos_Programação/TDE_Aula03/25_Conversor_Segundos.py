# 25. Conversor de Segundos: Solicite ao usuário um valor em segundos. Converta esse valor para horas, minutos e segundos. Mostre o resultado.

segundos = int (input("dígite os segundos: "))
horas = segundos/3600
minutos = segundos/60
print (f"A quantidade de segundos dígitada equivale a: {horas}h| {minutos}m | {segundos}s")