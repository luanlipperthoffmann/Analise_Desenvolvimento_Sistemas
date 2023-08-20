# 31. Declive de uma Linha: Solicite ao usuário os pontos x1, y1, x2 e y2 de uma linha no plano. Calcule o declive. Apresente o declive da linha.

x_01 = float (input("Dígite o ponto x1: "))
y_01 = float (input("Dígite o ponto y1: "))
x_02 = float (input("Dígite o ponto x2: "))
y_02 = float (input("Dígite o ponto y2: "))
declive = (y_02-y_01)/(x_02-x_01)
print(f"O declive da linha é de: {declive}")