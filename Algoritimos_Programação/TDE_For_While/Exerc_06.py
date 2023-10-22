'''Faça um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. OBS: Se a senha informada pelo usuário for inválida, a mensagem "ACESSO NEGADO" deve ser impressa e repetida a solicitação de uma nova senha até que ela seja válida. Caso contrário deve ser impressa a mensagem "ACESSO PERMITIDO" junto com um número que representa quantas vezes a senha foi informada.'''

senha_valida=1234
invasoes=0
senha= int(input("Digite sua senha!: "))
while senha!=senha_valida:
    senha=int(input("Dígite a senha valida!: "))
    invasoes=invasoes+1
print("Acesso permitido")
print(f"{invasoes} foram invalidas")