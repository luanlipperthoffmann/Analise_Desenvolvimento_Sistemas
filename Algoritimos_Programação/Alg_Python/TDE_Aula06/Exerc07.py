#Verificar se um ano é bissexto
ano = int(input("Dígite  o ano: "))
bissexto = ano%4
if bissexto == 0:
    print(f"O ano {ano} é bissexto")
elif bissexto > 0:
    print(f"O ano {ano} não é bissexto")