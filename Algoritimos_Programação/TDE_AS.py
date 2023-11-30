'''Descrição: Escreva uma função que recebe dois parâmetros, uma lista com dez números inteiros e um número inteiro. A função deve verificar quantas vezes este número aparece na lista. Por fim, a função deve retornar esta contagem. Por exemplo, se a lista for [1, 3, 7, 8, 7, 5, 6, 7, 9, 0] e o número a ser buscado for 7, o algoritmo deve imprimir 3, pois o número 7 aparece três vezes na lista. 

Objetivo: Este exercício testa a capacidade dos alunos de combinar laços de repetição com operações de lista para realizar buscas e contagens, habilidades importantes em programação.

Dica: Você pode usar esse "snipet" de código para escrever a sua função e chamá-la.

# Lista de números
numeros = [1, 3, 7, 8, 7, 5, 6, 7, 9, 0]

# Número a ser buscado
numero_buscado = 7

def conta_ocorrencias(numeros, numero_buscado):
    resultado = numeros.count(numero_buscado)
    return resultado

# chame a funçao
resultado = conta_ocorrencias(numeros, numero_buscado)

# Imprimindo o resultado
print(f"O número {numero_buscado} aparece {resultado} vezes na lista.")
'''

notas = []
notas_tamanho = 0 
pesos = []
pesos_tamanho = 0
resultado = 0
opcao = 0
def media_ponderada(notas, pesos):
    while opcao != 9:
        try:  
            opcao = int(input("\nInforme a opção desejada: \n1 - inserir nota \n2 - Inserir peso  \n9 - Sair \n"))
            if opcao == 1:
                notas.append(float(input("Dígite a nota desejada: ")))
                notas_tamanho = len(notas)
            elif opcao == 2:
                pesos.append(float(input("Dígite o peso desejado: ")))
                pesos_tamanho = len(pesos)
        except:
            if notas_tamanho != pesos_tamanho:
                print("Erro: As listas de notas e pesos têm tamanhos diferentes.")
            elif notas_tamanho == 0:
                print("Erro: As listas de notas está vazia.")
            elif pesos_tamanho == 0:
                print("Erro: As listas de pesos está vazia.")
    return
resultado = (notas*pesos)/pesos
print(f"A média ponderada das notas é: {resultado:.2f}")