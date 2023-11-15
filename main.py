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
    global biblioteca #ter certeza de que variavel biblioteca é o mesmo da global
    
    titulo = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    
    print(f"Essas sao as categorias disponiveis: {list(enumerate(categorias))}")
    
    categoria = int(input("Digite a qual categoria o livro pertence: "))
    preco = float(input("Digite o preço do livro: "))
    if biblioteca == {}:
        biblioteca = {
            "titulo" : [titulo],
            "autor" : [autor],
            "categoria" : [categoria],
            "valor" : [preco]
        }
    else:

        biblioteca["titulo"].append(titulo)
        biblioteca["autor"].append(autor)
        biblioteca["categoria"].append(categoria)
        biblioteca["valor"].append(preco)


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

cadastrar()
cadastrar()
deletar()
listar()

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
