''' Ler uma quantidade indeterminada de duplas de valores (2 valores de cada vez). Escrever para cada dupla uma mensagem que indique se ela foi informada em ordem crescente ou decrescente. A repetição será encerrada ao ser fornecido, para os elementos da dupla, valores iguais.

[Para os dados de entrada abaixo]
[Deve ser gerada a seguinte saída]
5   4
7   2
3   8
2   2
Decrescente
Decrescente
Crescente '''


valor_01=1
valor_02=0
while valor_01!=valor_02:
    valor_01 = int(input("Dígite o primeiro valor: "))
    valor_02 = int(input("Dígite o segundo valor: ")) 
    if valor_01>valor_02:
        print("Ordem decrescente")
    elif valor_01==valor_02:
        print("Valores iguais")
    else:
        print("Ordem crescente")