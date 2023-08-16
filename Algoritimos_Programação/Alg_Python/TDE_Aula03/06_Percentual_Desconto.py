#6. Percentual de Desconto: Peça ao usuário o preço original de um produto e um desconto em porcentagem. Calcule o valor com desconto usando ValorComDesconto = ValorOriginal - (ValorOriginal * Desconto / 100). Mostre o valor após o desconto.

valor_original = float(input("Informe o valor original do produto R$"))
desconto = float(input("Informe a porcentagem do desconto:"))
valor_com_desconto =  valor_original - (valor_original*desconto/100)
print(f"O valor do seu produto com desconto é de R$ {valor_com_desconto}")