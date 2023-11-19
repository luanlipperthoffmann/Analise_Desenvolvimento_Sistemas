'''
Escreva um programa em Python que solicita ao usuário que digite uma lista de números separados por espaços. O programa deve então processar a lista, ignorando valores inválidos e calculando a soma dos números válidos.

O programa deve:
Solicitar ao usuário que digite uma lista de números separados por espaços.
Processar a entrada, tratando valores inválidos.
Exibir os valores válidos que foram lidos da entrada.
Calcular a soma dos valores válidos e exibir o resultado.
'''

import exemplo_funcoes

lista_numero=[]

valores =exemplo_funcoes.ler_string("Dígite uma lista de números: \n")
valores=valores.split()

for valor in valores:
    try:
        numero=float(valor)
        lista_numero.append(numero)
    except ValueError:
        print(f" o valor {valor} é invalido")
    except MemoryError:
        print(f" Busca um padre")
    except:
        print("Except generica")
    else:
        print(f"Exbindo proximo valor {valor}")

soma=0

for item in lista_numero:
    soma+=item
print(f"A soma dos números válido é de: {soma}")