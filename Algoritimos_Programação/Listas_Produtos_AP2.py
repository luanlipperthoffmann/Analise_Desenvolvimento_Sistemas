produtos=[]
opcao_menu=0
posicao=0
produto_posicao=0
produto_removido=0
verificador=0

print("\033[1;32m \n================================================") # Aqui o código \033[1;32m para dar cor ao menu, sendo 1 o tema bold e 32 a cor do texto para verde
print("\033[93m   SEJA BEM-VINDO AO GERENCIADOR DE PRODUTOS!\n")
print(" \033[34m MENU: ")
print(" \033[33m 1. \033[1;32m Adicionar Produto")
print(" \033[33m 2. \033[1;32m Adicionar Produto em um Posição Específica")
print(" \033[33m 3. \033[1;32m Remover Produto")
print(" \033[33m 4. \033[1;32m Listar Produtos")
print(" \033[33m 9. \033[1;32m Sair")
print("================================================")

while opcao_menu !=9:
    opcao_menu=int(input("\033[96m\nEscolha a opção desejada no menu: \033[0m"))
    if opcao_menu==1:
        verificador=(str(input("Informe o nome do produto a ser adicionado a sua lista: ")))
        if verificador not in produtos:
            produtos.insert(0,verificador)
            print(f"Produto \033[1;32m'{produtos[0]}'\033[m adicionado com sucesso!") #Aqui 0 print vai mostrar sempre o produto na  posicao 0
        else:
                print(f"O produto \033[1;32m'{verificador}'\033[m já existe na sua lista!")
    elif opcao_menu==2:
        produto_posicao=str(input("Qual o produto deseja adicionar? "))
        if produto_posicao not in produtos:
            posicao= int(input(f"Em qual posição deseja adicionar o produto: \033[1;32m'{produto_posicao}'\033[m? (0 à {len(produtos)}): ")) #Aqui a função len(produtos) irá printar na tela o final total de psiçoes ocupadas na lista
            tamanho_lista=len(produtos)
            if posicao>=0 and posicao <= tamanho_lista:
                produtos.insert(posicao, produto_posicao)
                print(f"Produto \033[1;32m'{produto_posicao}'\033[m adicionado com sucesso!")
            else:
                print("\033[1;31m\nPOSIÇÃO INVÁLIDA. \nA operação não pode ser concluida; \nTente Novamente!")
        else:
            print(f"O produto \033[1;32m'{produto_posicao}'\033[m já existe na sua lista!")
    elif opcao_menu==3:
        produto_removido=str(input("Qual produto deseja remover? "))
        produtos.remove(produto_removido)
        print(f"Produto \033[1;32m'{produto_removido}'\033[m removido com sucesso!") 
    elif opcao_menu==4:
        print(f"Os Itens adicionados na  lista são:\n")
        print("\n".join(produtos))
    elif opcao_menu==9:
        print("\033[1;32mObrigado por usar o Gerenciador de Produto; \nAté mais!")
    else: 
        print("\033[1;31m \nComando inválido! \nInforme o número do menu desejado.")