# 29. Perímetro de um Triângulo: Solicite ao usuário os três lados de um triângulo. Calcule o perímetro. Mostre o resultado.

lado_01 = float (input("Dígite o valor do lado 01 do triângulo: "))
lado_02 = float (input("Dígite o valor do lado 02 do triângulo: "))
lado_03 = float (input("Dígite o valor do lado 03 do triângulo: "))
perimetro = lado_01+lado_02+lado_03
print(f"O perímetro do triângulo é de: {perimetro}")