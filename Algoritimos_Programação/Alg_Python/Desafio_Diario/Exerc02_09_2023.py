'''Desafio dia 04. Bom tarde, galera esse é o SKY. Sim é O Sky, é um cachorro, nós adotamos e ele ja veio com o nome. O antigo dono do Sky é piloto de avião e precisou se mudar e não pode ficar com ele, o sky possui um medo terrível de balões, para um cão que mora em torres é bem problemático. (o que não combina com seu nome, vamos combinar). Mas além disso, ele come muita ração! e eu preciso me planejar aqui. Sabendo que o Sky come duas vezes no dia 180 gramas de ração. Que o preço medio do saco de ração de 10kg é de 200 reais ( come melhor que eu esse jaguara). Faça um algoritmo que mostre quanto vou gastar de dinheiro em um ano.'''

preco_ração = float(input("Informe o preço em R$ do saco de ração de 10kg para cachorro: \n"))
refeiçoes_dia = int(input("Informe quantas vezes ao dia voçê alimenta seu cachorro: \n"))
peso_porcao = float (input("Informe quantas gramas de ração voçê fornece por refeição: \n"))
racao_ano = ((peso_porcao*refeiçoes_dia)*365)/10000
total_gasto = racao_ano*preco_ração
print(f"Voçê irá gastar em um ano (365 dias), o total de: {racao_ano:.1f} sacos de ração resultando no valor de R${total_gasto:.2f}")