#4. Média de Notas: Peça ao usuário quatro notas. Determine a média usando Média = (n1 + n2 + n3 + n4) / 4 e mostre a média obtida.

nota_01 = float (input("Dígite a primeira nota:"))
nota_02 = float (input("Dígite a segunda nota:"))
nota_03 = float (input("Dígite a terceira nota:"))
nota_04 = float (input("Dígite a quarta nota:"))
media = (nota_01+nota_02+nota_03+nota_04)/4
print(f"A média das 4 notar inseridas é de:{media}")