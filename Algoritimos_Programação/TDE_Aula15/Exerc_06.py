'''Verificação de idade para votação: Escreva um programa que peça a idade do usuário e verifique se ele pode votar ou não. Se a idade for igual ou superior a 16 anos, exiba a mensagem "Você pode votar". Caso contrário, exiba "Você ainda não pode votar".'''


idade = int(input("Informe sua idade: "))
if idade>=16:
    print("Voçê pode votar!")
else:
    print("Voçê não pode votar!")