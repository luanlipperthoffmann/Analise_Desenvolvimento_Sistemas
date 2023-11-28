'''Média de uma Lista: Escreva uma função que calcule a média de uma lista de números.'''

lista = []
tamanho = 0
soma = 0
opcao = 0
media = 0 

def media (lista):
    soma = sum(lista)
    tamanho = len(lista)
    resultado = soma/tamanho
    return resultado

while opcao!=9:
    opcao = int(input("\nSelecione as opções desejadas: \n1- ADICIONAR NÚMEROS A LISTA \n2- EXIBIR A MÉDIA DA LISTA \n9- SAIR \n"))
    if opcao==1:
        lista.append(int(input("Informe o número: ")))
     
    elif opcao==2:
        print(f"A média da lista é {media(lista):.2f}")