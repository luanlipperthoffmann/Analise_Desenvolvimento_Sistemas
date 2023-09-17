'''3. Jantar Especial:
Para um jantar em família, além do espaguete, agora você também deseja servir um molho especial para pessoas veganas.
Entrada:
O programa deve perguntar quantos membros da família vão participar do jantar e quantos deles são veganos.
Saída
O programa deve informar a quantidade de espaguete (em gramas) e a quantidade de molho (em
litros) que você precisa preparar.
* Espaguete: 100g por pessoa
* Molho: 0,5 litros para cada vegano'''

pessoas_totais = int(input("Informe a quantidade de pessoas participantes: \n"))
pessoas_veganas = int(input("Informe a quantidade de pessoas veganas: \n"))
espaguete_total = pessoas_totais*100
molho_vegano = pessoas_veganas*0.5
if pessoas_totais > pessoas_veganas:
    print(f"O total de espaguete necessário para {pessoas_totais} pessoas é de {espaguete_total}g \nO total de molho especial para {pessoas_veganas} veganos é de {molho_vegano:.2f} litros ")
else:
    print("O número de pessoas veganas informado é maior que o número de pessoas totais no jantar. \nDigite novamente os dados!")