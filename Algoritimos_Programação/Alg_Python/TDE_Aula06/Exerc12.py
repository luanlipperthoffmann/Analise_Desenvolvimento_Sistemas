#Verificar se um caractere é uma vogal ou uma consoante.

caractere = input("Dígite um caractere: \n")
if caractere == 'a' or  caractere == 'A' or caractere == 'e' or caractere == 'E' or caractere == 'i' or caractere == 'I' or caractere == 'o' or caractere == 'O'  or caractere == 'u'  or caractere == 'U':
    print("Este caractere é uma vogal")
else:
    print("Este caractere é uma consoante")