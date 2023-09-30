'''3. Organização de Festa:
Você está planejando uma festa de aniversário e quer garantir que não falte bebida. Decide criar um programa que calcule a quantidade de bebida necessária.
Entrada:
O programa deve solicitar o número de convidados.
Saída:
O programa deve informar a quantidade total de bebida (em litros) que você precisa comprar.
Nota:
Estime que cada convidado consuma 500ml de bebida.'''

convidados = int(input("Informe o numero de convidados: \n"))
bebida_total = (convidados*500)/1000
print(f"O total de bebia necessária é de {bebida_total} litros")