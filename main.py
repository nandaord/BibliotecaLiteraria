#manipulacao de dados

biblioteca = {}
bibliotecaExemplo = {
    "titulo" : ["harry potter", "metamorfose"],
    "autor" : ["jk", "franz kafka"],
    "categoria" : [1, 2],
    "valor" : [105, 200]

}

categorias = ["Terror", "Aventura", "Sci-fi"]

def cadastrar():
    with open("antonio.txt","a", encoding="utf-8") as arquivo:
        nome = input("Digite o nome do livro: ").title()
        autor = input("Digite o nome do autor do livro: ").title()
        categoria = input("Digite a qual categoria o livro pertence: ").title()
        preco = float(input("Digite o preço do livro: "))
        
        arquivo.write(nome + " " + autor + " "+ categoria + " "+ str(preco) +"\n")
        #contador = len(biblioteca)
        #variavel pra contar
    
    #livro = []


    livroJaExiste = False

    for y in biblioteca:
        get = biblioteca.get(y)
        if get[0] == nome and get[1] == autor: 
            livroJaExiste = True
    
    if livroJaExiste == True:
        print("\nJá existe")
    
    else:
        
        biblioteca[len(biblioteca) + 1] = [nome, autor, categoria, preco]
        #nome, autor, categoria, preço
        print("Livro cadastrado com sucesso!")
        print(biblioteca)
    
    arquivo.close()



def deletar():
    # TODO: considerar se só tem um livro pra deletar e criar uma bibklioteca vazianesse caso
    global biblioteca #ter certeza de que variavel biblioteca é o mesmo da global
    if biblioteca == {}:
        print("A biblioteca está vazia!")
    else:
        listar()
        tituloParaDeletar = input("Digite o ID do livro que deseja deletar: ")
        if biblioteca["titulo"].count(tituloParaDeletar) > 1:
            #quero mostrar lista apenas do titulo, com autor,categoria e valor
            print("Escreva o nome do autor para confirmar o livro certo: ")
            for x in biblioteca:
                if biblioteca["titulo"][x]:
                    print(biblioteca[x])
            autorParaDeletar = input()


                    #get index to delete
            contador = -1
            for x in range(len(biblioteca["titulo"])):
                contador += 1
                if biblioteca["titulo"][x] == tituloParaDeletar and biblioteca["autor"][x] == autorParaDeletar:
                    indexParaDeletar = contador
                    break
            del biblioteca["titulo"][indexParaDeletar]
            del biblioteca["autor"][indexParaDeletar]
            del biblioteca["categoria"][indexParaDeletar]
            del biblioteca["valor"][indexParaDeletar]
        else:

            biblioteca = {}

def listar():
    global biblioteca
    if biblioteca == {}:
        print("A biblioteca está vazia!")
    for i in range(len(biblioteca['titulo'])):
        print(f"""{i}. '{biblioteca['titulo'][i]}' por {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; R$: {biblioteca["valor"][i]}.""")



def atualizar():
    posicao=int(input(f"Digite o número do livro que deseja modificar de acordo com a listagem: {listar()}"))
    item=input("Digite de qual categoria deseja modificar a informação:")
    novo=input("Qual será o novo valor?")


    if item == "titulo":
        biblioteca["titulo"][posicao] = novo

    elif item =="autor":
        biblioteca["autor"][posicao] = novo

    elif item =="categoria":
        biblioteca["categoria"][posicao] = novo

    elif item =="valor":
        biblioteca["valor"][posicao] = float(novo)
        

while True:
    print("\n Gerenciamento de Biblioteca Pessoal \n")
    print("1. Cadastrar Livro")
    print("\n2. Listar Livros")
    print("\n3. Atualizar Livro")
    print("\n4. Excluir Livro")
    print("\n5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '2':
        listar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '3':
        atualizar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '4':
        deletar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '5':
        break
    else:
        print("Tente novamente")
