'''1. Categoria de Piscinas:
Uma loja vende piscinas retangulares de diferentes tamanhos. Com base na área da piscina, elas são classificadas em três categorias: Pequena, Média e Grande.
Entrada:
O programa deve solicitar ao usuário a altura e a largura de um retângulo representando a piscina.
Saída:
O programa deve informar a área da piscina e sua categoria.
Fórmula:
Área = altura x largura
* Pequena: Até 10 m²
* Média: Mais de 10 m² até 30 m²
* Grande: Acima de 30 m²'''

altura = float(input("Informe a altura da piscina desejada: \n"))
largura = float(input("Informe a largura da  piscina desejada: \n"))
area = altura*largura
if area <= 10:
    print(f"A área da sua piscina é de {area:.2f}m², voçê precisará de uma piscina Pequena")
elif area >10 and area <= 30:
    print(f"A área da sua piscina é de {area:.2f}m², voçê precisará de uma piscina Média")
else:
    print(f"A área da sua piscina é de {area:.2f}m², voçê precisará de uma piscina Grande")