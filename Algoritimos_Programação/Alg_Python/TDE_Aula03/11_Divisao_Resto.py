#11. Divisão e Resto: Solicite dois números ao usuário. Calcule o resultado da divisão e o resto. Apresente ambos os valores.

numero_01 = int (input("Dígite o primeiro número: "))
numero_02 = int (input("Dígite o segundo número: "))
divisao = numero_01//numero_02
print(f"O resultado da divisão dos números apresentados é de : {divisao}")
resto = numero_01%numero_02
print(f"O resto da divisão é: {resto}")