'''Escrever um programa que lê as 3 notas obtidas por ele em provas. Para cada aluno, calcular a
média de aproveitamento, usando a fórmula:
MA = (Nl + N2 + N3)/3
A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
>= 9.0 A
>= 7.5 e < 9.0 B
>= 6.0 e < 7.5 C
>= 4.0 e < 6.0 D
< 4.0 E '''

nota_01 = float (input("Dígite a primeira nota do aluno: "))
nota_02 = float (input("Dígite a segunda nota do aluno: "))
nota_03 = float (input("Dígite a terceira nota do aluno: "))
media= (nota_01 + nota_02 + nota_03)/3

if media >= 9.0:
    print(f"A média do aluno foi de: {media:.2f}. \nO seu aproveitamento foi: A")
elif media >= 7.5 and media < 9.0:
    print(f"A média do aluno foi de: {media:.2f}. \nO seu aproveitamento foi: B")
elif media >= 6.0 and media < 7.5:
    print(f"A média do aluno foi de: {media:.2f}. \nO seu aproveitamento foi: C")
elif media >= 4.0 and media < 6.0:
    print(f"A média do aluno foi de: {media:.2f}. \nO seu aproveitamento foi: D")
else:
    print(f"A média do aluno foi de: {media:.2f}. \nO seu aproveitamento foi: E")