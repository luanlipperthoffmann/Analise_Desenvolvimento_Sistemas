'''Desafio dia 03 Sextou! Galera, dizem que devemos calcular numa festa o chopp para uma festa da seguinte forma. 2 litros pra cada homem . 1.5 litros pra cada mulher.Me ajuda aí um algoritmo pra calcular quantos litros de chopp dão necessários pra um happy hour'''

chopp_homen = int(input("Informe quantas pessoas do sexo masculino irão comparecer a festa: \n"))
chopp_mulher = int(input("Informe quantas pessoas do sexo feminino irão comparecer a festa: \n"))
total_chopp = (chopp_homen*2) + (chopp_mulher*1.5)
print(f"O Total de chop a ser comprado é de: {total_chopp:.2f}LT's")