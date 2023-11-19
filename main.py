#manipulacao de dados


def inicializar():
    biblioteca = {
    "titulo" : [],
    "autor" : [],
    "categoria": [],
    "valor": []
    }

    with open("antonio.txt", "r", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip() # se nao usar strip, printa \n
            print(f" essa eh linha: {linha}")
            if linha == "":
                break #sair do loop caso linha esteja em branco, significa que nao ha mais livros. Um failsafe.
            else:
                biblioteca["titulo"].append(linha)         
                linha = next(arquivo).strip()
                biblioteca["autor"].append(linha)
                linha = next(arquivo).strip()
                biblioteca["categoria"].append(int(linha))
                linha = next(arquivo).strip()
                biblioteca["valor"].append(float(linha))
        arquivo.close()

    print(biblioteca)
    return biblioteca


categorias = ["Terror", "Aventura", "Sci-fi"]

def cadastrar():
    global biblioteca #ter certeza de que variavel biblioteca é o mesmo da global
    
    with open("antonio.txt", "a", encoding="utf-8") as arquivo:
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
            biblioteca["categoria"].append(int(categoria))
            biblioteca["valor"].append(float(preco))
        
    #arquivo.write(titulo + " " + autor + " " + str(categoria) + " " + str(preco) + "\n")
        arquivo.write("\n")
        arquivo.write(titulo + "\n") # I want each of these to be in one line
        arquivo.write(autor + "\n")
        arquivo.write(str(categoria) + "\n")
        arquivo.write(str(preco) + "\n")
        arquivo.close()


def deletar():
    listar()
    # TODO: considerar se só tem um livro pra deletar e criar uma bibklioteca vazianesse caso
    global biblioteca #ter certeza de que variavel biblioteca é o mesmo da global
    if biblioteca == {}:
        print("A biblioteca está vazia!")
    else:
        listar()
        idParaDeletar = input("Digite o ID do livro que deseja deletar: ")
        del biblioteca["titulo"][idParaDeletar]
        del biblioteca["autor"][idParaDeletar]
        del biblioteca["categoria"][idParaDeletar]
        del biblioteca["valor"][idParaDeletar]
        doDicionarioParaFile() # quero reescrever o file INTEIRO, baseado na nova biblioteca


                
def doDicionarioParaFile():
    global biblioteca #ter certeza de que variavel biblioteca é o mesmo da global
    with open("antonio.txt", ("w"), encoding="utf-8") as arquivo:
        for i in range(len(biblioteca["titulo"])):
            arquivo.write(biblioteca["titulo"][i] + "\n") # I want each of these to be in one line
            arquivo.write(biblioteca["autor"][i] + "\n")
            arquivo.write(str(biblioteca["categoria"][i]) + "\n")
            arquivo.write(str(biblioteca["valor"][i]) + "\n")
        arquivo.close()

def listar():
    print(biblioteca)
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
    
        

"""while True:
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
        print("Tente novamente")"""

"""inicializar()
cadastrar()
deletar()"""


biblioteca = inicializar()
doDicionarioParaFile()
