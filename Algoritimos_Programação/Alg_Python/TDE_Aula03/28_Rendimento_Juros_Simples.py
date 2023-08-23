# 28. Rendimento de Juros Simples: Peça ao usuário um valor principal, a taxa de juros e o tempo em anos. Calcule o juro simples. Mostre o valor de juros.

valor = float(input("Dígite o valor desejado R$"))
taxa_juros = float(input("Dígite a taxa de juros: "))
tempo_anos = float (input("Dígite o tempo em anos: "))
valor_juros = ((valor*taxa_juros)/100)*tempo_anos
print(f"O valor dos juros é de R${valor_juros:.2f}")