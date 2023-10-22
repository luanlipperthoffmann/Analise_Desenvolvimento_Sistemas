'''Cálculo de desconto: Escreva um programa que leia o valor de um produto e calcule o valor com desconto de 10%. Se o valor do produto for maior que R$ 50,00, aplique um desconto adicional de 5%. Exiba o valor final com desconto.'''


valor_produto= float(input("Dígite o valor do produto: "))
if valor_produto <50:
    desconto=valor_produto-(valor_produto*0.1)
    print(f"R${desconto:.2f}")
else:
    desconto_10=valor_produto-(valor_produto*0.10)
    desconto_05=desconto_10-(desconto_10*0.05)
    print(f"R${desconto_05:.2f}")