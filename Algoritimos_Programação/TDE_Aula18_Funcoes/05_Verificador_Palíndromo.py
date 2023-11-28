'''Verificador de Palíndromo: Crie uma função que verifique se uma palavra é um palíndromo (ou seja, pode ser lida da mesma forma da esquerda para a direita e vice-versa).'''

palindromo = 0
palavra = str(input("Dígite a palavra deseja: "))
def verificaPalindromo(palavra):
    if palavra == True:
        
        print(f"A palavra {palavra} é um palíndromo")
    else:
        print(f"A palavra {palavra} não é um palíndromo")
    return 

print(verificaPalindromo(palavra))