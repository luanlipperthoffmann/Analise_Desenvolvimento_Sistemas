'''Fatorial de um Número: Peça ao usuário para inserir um número e calcule seu fatorial usando um loop while. (Exemplo: 5! = 5x4x3x2x1 = 120)'''

n=int(input("Digite o valor para calcular o fatorial"))
numero=n
if n==0:
    print("Nao da pra fazer")
else:
    fatorial=1
    while n>1:
        fatorial*=n
        n=n-1
print(f"Fatorial de {numero} é igual a {fatorial}")