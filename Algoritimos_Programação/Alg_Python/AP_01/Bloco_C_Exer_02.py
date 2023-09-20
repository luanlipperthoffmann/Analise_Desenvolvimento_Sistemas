'''2. Ponto de Congelamento:
Com as mudanças climáticas, uma cidade está experimentando temperaturas extremas. O departamento de meteorologia quer alertar os cidadãos quando a temperatura se aproxima do ponto de congelamento.
Entrada:
O programa deve solicitar ao usuário a temperatura atual em graus Celsius.
Saída:
O programa deve informar se está "Seguro", "Próximo ao ponto de congelamento" ou "Abaixo do
ponto de congelamento".
* Seguro: Acima de 5°C
* Próximo ao ponto de congelamento: Entre 0°C e 5°C
* Abaixo do ponto de congelamento: Menos de 0°C'''

celsius = float(input("Informe a temperatura em graus celsius: \n"))
if celsius > 5:
    print(f"A temperatura de {celsius}º celsius é segura")
elif celsius <= 5 and celsius >=0:
    print(f"A temperatura de {celsius}º celsius está proxima ao ponto de congelamento")
else:
    print(f"A temperatura de {celsius}º celsius está abaixo do ponto de congelamento")
    