#Verificar se um número é um quadrado perfeito.

numero = int(input("Informe o numero desejado: \n"))
raiz = numero ** (1/2)
print(raiz)
if ((raiz ** 2) == numero):
    print(f"O número {numero} é um quadrado perfeito")
else:
    print(f"O número {numero} não é um quadrado perfeito")