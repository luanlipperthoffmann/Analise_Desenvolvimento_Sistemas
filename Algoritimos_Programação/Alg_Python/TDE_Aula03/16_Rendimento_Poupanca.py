# 16. Rendimento de Poupança: Solicite ao usuário um valor depositado na poupança. Calcule o valor após um mês, considerando uma taxa de rendimento fixa. Mostre o valor atualizado.

valor_depositado = float (input("Dígite o valor depositados da poupança R$"))
valor_atualizado = (valor_depositado*0.5)/100 + valor_depositado
print(f"O valor atualizado da poupança após 1 mês é de R${valor_atualizado}")