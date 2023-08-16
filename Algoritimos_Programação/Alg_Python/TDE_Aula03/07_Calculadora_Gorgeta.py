#7. Calculadora de Gorjeta: Solicite ao usuário o valor de uma refeição. Calcule uma gorjeta de 10% com Gorjeta = Valor * 0.1. Mostre tanto a gorjeta quanto o valor total.

valor_refeicao = float (input("Dígite o valor da refeição:"))
gorjeta = valor_refeicao*0.1
print(f"O Valor pago de  gorjeta foi de R$ {gorjeta}")
valor_total = valor_refeicao + gorjeta
print (f"O valor total pago foi de R${valor_total}")
