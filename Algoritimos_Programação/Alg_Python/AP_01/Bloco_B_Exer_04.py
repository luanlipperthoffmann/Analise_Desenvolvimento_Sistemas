'''4. Sistema de Caixa Simples:
Para treinar seus conhecimentos em Python, você decide criar um programa simples de caixa que
ajude a calcular o troco dado ao cliente.
Entrada:
O programa deve perguntar o valor total da compra e o valor entregue pelo cliente para pagar.
Saída:
O programa deve informar o valor do troco que o cliente deve receber.'''

total_compra = float(input("Informe o total da compra: \n"))
total_pago = float(input("Informe o total pago: \n"))
troco = total_pago - total_compra
print(f"O troco será de R${troco:.2f} reais")