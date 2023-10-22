'''2. Verificação de idade: Escreva um programa que peça a idade do usuário e verifique se ele é maior de idade ou não. Se for maior de idade, exiba a mensagem "Você é maior de idade" Caso contrário, exiba "Você é menor de idade". .O Programa deve perguntar "Deseja efetuar nova validação (S/N)" O programa encerra ao digitar N'''

efetuar = "S"
while efetuar == "S":
    idade = int(input("qual a sua idade: "))
    if idade >= 18:
        print(f"Você é maior de idade")
    else:
        print(f"Você é menor de idade")
    efetuar = input("voce deseja efetuar uma nova validação? S/N: ")