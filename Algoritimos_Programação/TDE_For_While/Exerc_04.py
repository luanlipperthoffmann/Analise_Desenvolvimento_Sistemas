'''Ler dois valores inteiros e escrever o resultado da divisão do primeiro pelo segundo. Se o segundo valor informado for ZERO, deve ser impressa uma mensagem de VALOR INVÁLIDO e ser lido um novo valor. Ao final do programa deve ser impressa a seguinte mensagem: VOCE DESEJA OUTRO CÁLCULO (S/N).  Se a resposta for S o programa deverá retornar ao começo, caso contrário deverá encerrar a sua execução imprimindo quantos cálculos foram feitos. '''


outro_calculo ='s'
contador = 0
while outro_calculo=='s'or 'S':
    numero_01 = int(input("Dígite o primeiro número: "))
    numero_02 = int(input("Dígite o segundo número: ")) 
    while numero_02==0:
        print(f"VALOR INVÁLIDO.")
        numero_02 = int(input("Dígite o segundo número novamente: "))
    resultado=numero_01/numero_02 
    contador=contador+1              
    print(f"O resultado da divisão é {resultado}")
    outro_calculo=input("Deseja realizar outro calculo?")
    print(f"Foram feitos {contador} calculos")