#5. Conversor de Moeda: Solicite ao usuário um valor em dólares. Converta este valor para reais considerando uma taxa de câmbio fixa. Mostre o valor convertido.

dolares = float(input("Dígite a quantidade de dolares desejada para conversão: $"))
taxa_cambio = 5.64
reais = dolares*taxa_cambio
print(f"O valor total a ser recebido em reias é de R${reais}")