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
    #TODO: CRIAR POSSIBILIDADE da biblioteca estar vazia, pois não terá nem chaves

    #temos que considerar tbm se 'e o primeiro cadastro, se for, temos que criar as chaves da biblioteca
    titulo = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    #dar um display nas categorias
    print(f"Essas sao as categorias disponiveis: {list(enumerate(categorias))}")
    #dar um display nas categorias. tem q usar loop for in range
    categoria = int(input("Digite a qual categoria o livro pertence: "))
    preco = float(input("Digite o preço do livro: "))

    bibliotecaExemplo["titulo"].append(titulo)
    bibliotecaExemplo["autor"].append(autor)
    bibliotecaExemplo["categoria"].append(categoria)
    bibliotecaExemplo["valor"].append(preco)

cadastrar()
print(bibliotecaExemplo)


def deletar():
    # TODO: considerar se só tem um livro pra deletar e criar uma bibklioteca vazianesse caso
    tituloParaDeletar = input("Digite o nome do livro que deseja deletar: ")
    if bibliotecaExemplo["titulo"].count(tituloParaDeletar) > 1:
        #quero mostrar lista apenas do titulo, com autor,categoria e valor
        print("Escreva o nome do autor para confirmar o livro certo: ")
        for x in bibliotecaExemplo:
            if bibliotecaExemplo["titulo"][x]:
                print(bibliotecaExemplo[x])
        autorParaDeletar = input()


                #get index to delete
        contador = -1
        for x in len(bibliotecaExemplo["titulo"]):
            contador += 1
            if bibliotecaExemplo["titulo"][x] == tituloParaDeletar and bibliotecaExemplo["autor"][x] == autorParaDeletar:
                indexParaDeletar = contador
                break
        del bibliotecaExemplo["titulo"][indexParaDeletar]
        del bibliotecaExemplo["autor"][indexParaDeletar]
        del bibliotecaExemplo["categoria"][indexParaDeletar]
        del bibliotecaExemplo["valor"][indexParaDeletar]
    else:

        indexParaDeletar = bibliotecaExemplo.index(tituloParaDeletar)
        del bibliotecaExemplo["titulo"][indexParaDeletar]
        del bibliotecaExemplo["autor"][indexParaDeletar]
        del bibliotecaExemplo["categoria"][indexParaDeletar]
        del bibliotecaExemplo["valor"][indexParaDeletar]

def listar():
    for i in range(len(bibliotecaExemplo["titulo"])):
        print(f"""{i}. '{bibliotecaExemplo["titulo"][i]}' por {bibliotecaExemplo['autor'][i]}\n{categorias[bibliotecaExemplo['categoria'][i]]} ; R$: {bibliotecaExemplo["valor"][i]}.""")


listar()

#def atualizar():