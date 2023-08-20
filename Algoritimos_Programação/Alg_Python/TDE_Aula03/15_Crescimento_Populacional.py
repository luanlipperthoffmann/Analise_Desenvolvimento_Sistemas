# 15. Crescimento Populacional: Peça ao usuário a população atual e a taxa de crescimento anual de duas cidades. Calcule a população de cada cidade após um ano e mostre os novos valores.

populacao_atual = int (input("dígite a popupacao atual: "))
crescimento_cidade_01 = float (input("Dígite a taxa de crescimento anual da 1ª cidade: "))
crescimento_cidade_02 = float (input("Dígite a taxa de crescimento anual da 2ª cidade: "))
populacao_cidade_01 = (populacao_atual*crescimento_cidade_01)/100 + populacao_atual
populacao_cidade_02 =  (populacao_atual*crescimento_cidade_02)/100 + populacao_atual
print (f"O Crescimento da população na cidade 1 é de: {populacao_cidade_01} | Da cidade 02 é de: {populacao_cidade_02}")
