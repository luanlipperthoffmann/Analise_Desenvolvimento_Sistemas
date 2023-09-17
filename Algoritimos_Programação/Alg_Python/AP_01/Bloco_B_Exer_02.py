'''2. Preparativos para Jantar:
Você está ajudando na organização de um grande jantar de família. Para comprar os ingredientes, você decide calcular a quantidade de espaguete que será necessário.
Entrada:
O programa deve perguntar quantos membros da família vão participar do jantar.
Saída:
O programa deve informar a quantidade de espaguete (em gramas) necessária para servir a todos.
Nota:
Considere que cada pessoa consome 100g de espaguete.'''

pessoas = int(input("Informe a quantidade de pessoas participantes: \n"))
espaguete_total = pessoas*100
print(f"O total de espaguete necessário é de {espaguete_total}g")