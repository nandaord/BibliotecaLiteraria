#manipulacao de dados
def inicializar():
    

    biblioteca = {
    "titulo" : [],
    "autor" : [],
    "categoria": [],
    "valor": []
    }
    
    try:
        with open("antonio.txt", "r", encoding = "utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip() # se nao usar strip, printa \n
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
    except FileNotFoundError:
        print(prompts[escolhaLingua][9])
        arquivo = open("antonio.txt", "w")
        arquivo.close()

    return biblioteca




def cadastrar():
    
    with open("antonio.txt", "a", encoding="utf-8") as arquivo:
        titulo = input(promptsCadastrar[escolhaLingua][0]) 
        autor = input(promptsCadastrar[escolhaLingua][1])
    
        print(list(enumerate(categorias)))
    
        categoria = int(input(promptsCadastrar[escolhaLingua][2]))
        preco = float(input(promptsCadastrar[escolhaLingua][3]))

        if biblioteca == {}:
            biblioteca = {
                "titulo" : [titulo],
                "autor" : [autor],
                "categoria" : [categoria],
                "valor" : [preco]
            }
            biblioteca["titulo"].append(titulo)
            biblioteca["autor"].append(autor)
            biblioteca["categoria"].append(int(categoria))
            biblioteca["valor"].append(float(preco))
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
        arquivo.write(str(preco) + "\n") # talvez tirar \n
        arquivo.close()


def deletar():
    if biblioteca == {}:
        print(promptsDeletar[escolhaLingua][0])  
    else:
        listar()
        try:
            idParaDeletar = int(input(promptsDeletar[escolhaLingua][1]))  
            del biblioteca["titulo"][idParaDeletar]
            del biblioteca["autor"][idParaDeletar]
            del biblioteca["categoria"][idParaDeletar]
            del biblioteca["valor"][idParaDeletar]
            doDicionarioParaFile()  
        except IndexError:
            print(promptsDeletar[escolhaLingua][2])  
        except ValueError:
            print(promptsDeletar[escolhaLingua][3])  


                
def doDicionarioParaFile():
    with open("antonio.txt", ("w"), encoding="utf-8") as arquivo:
        for i in range(len(biblioteca["titulo"])):
            arquivo.write(biblioteca["titulo"][i] + "\n") # I want each of these to be in one line
            arquivo.write(biblioteca["autor"][i] + "\n")
            arquivo.write(str(biblioteca["categoria"][i]) + "\n")
            arquivo.write(str(biblioteca["valor"][i]) + "\n")
        arquivo.close()

def listar():
    print(promptsListar[escolhaLingua][0])  
    
    try:
        choice = int(input())

        if choice == 1:
            listarBasico()
        elif choice == 2:
            print(promptsListar[escolhaLingua][1])  
            for indice, categoria in enumerate(categorias):
                print(f"{indice}. {categoria}")
            choiceCategoria = int(input(promptsListar[escolhaLingua][2]))  
            for i in range(len(biblioteca['titulo'])):
                if biblioteca['categoria'][i] == choiceCategoria:
                    print(f"""{i}. '{biblioteca['titulo'][i]}' by {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; {promptsListar[escolhaLingua][3]}\n""".format(biblioteca["valor"][i]))
        elif choice == 3:
            custoTotal = 0
            for i in range(len(biblioteca['titulo'])):
                custoTotal += biblioteca["custo"][i]
            print(promptsListar[escolhaLingua][3].format(custoTotal))  
        elif choice == 4:
            custoTotal = 0
            choiceCategoria = int(input(promptsListar[escolhaLingua][5]))  
            
            for i in range(len(biblioteca['titulo'])):
                if biblioteca['categoria'][i] == choiceCategoria:
                    custoTotal += biblioteca["valor"][i]
            print(promptsListar[escolhaLingua][4].format(custoTotal))  

        elif choice == 5:
            print("\n")
            for x in range(0, 9):
                print(f"\nBooks of {categorias[x]}: \n")
                for i in range(len(biblioteca['titulo'])):
                    if biblioteca['categoria'][i] == x:
                        print(f"""{i}. '{biblioteca['titulo'][i]}' by {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; {promptsListar[escolhaLingua][3]}\n""")
        else:
            print(promptsListar[escolhaLingua][6])  
    except ValueError:
        print(promptsListar[escolhaLingua][7])  
    except IndexError:
        print(promptsListar[escolhaLingua][8])  


def listarBasico():
    for i in range(len(biblioteca['titulo'])):
                print(f"""{i}. '{biblioteca['titulo'][i]}' by {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; {promptsListar[escolhaLingua][3]}\n""".format(biblioteca["valor"][i]))
                #preciso do format para printar o custo correto
    print("\n")

def atualizar():
    print("\n")
    posicao = int(input(promptsAtualizar[escolhaLingua][1]))  
    print(promptsAtualizar[escolhaLingua][0])  
    item = int(input(promptsAtualizar[escolhaLingua][2]))  
    novo = input(promptsAtualizar[escolhaLingua][3])  

    if item == 1:
        biblioteca["titulo"][posicao] = novo
        print(promptsAtualizar[escolhaLingua][4])  
    elif item == 2:
        biblioteca["autor"][posicao] = novo
    elif item == 3:
        biblioteca["categoria"][posicao] = int(novo)
    elif item == 4:
        biblioteca["valor"][posicao] = float(novo)

    print(biblioteca)
    doDicionarioParaFile()
        
    
categorias = ["Terror", "Aventura", "Sci-fi","Romance","Infantil","Drama","Misterio","Young Adult", "Outros"]

escolha = int(input("Select Language by typing its ID number:\n0-Português\n1-English\n"))
#languagesAvailable = ["pt", "en"]
escolhaLingua = "en"
if escolha == 0:
    escolhaLingua = "pt"
elif escolha == 1:
    escolhaLingua = "en"
else:
    print("Choice was not understood. Defaulting to English.")



#AQUI VAMOS TER AS PROMPTS
prompts = {
    "pt": [
        "\n Gerenciamento de Biblioteca Pessoal \n",
        "1. Cadastrar Livro",
        "\n2. Listar Livros",
        "\n3. Atualizar Livro",
        "\n4. Excluir Livro",
        "\n5. SAIR",
        "Escolha uma opção: ",
        "\nAção concluída com sucesso. \nAperte Enter para continuar.",
        "Tente novamente.",
        "Arquivo txt nao foi encontrado!\nCriaremos um arquivo para voce.",
    ],
    "en": [
        "\n Personal Library Management \n",
        "1. Register Book",
        "\n2. List Books",
        "\n3. Edit Book info",
        "\n4. Delete Book",
        "\n5. QUIT",
        "Choose an option: ",
        "\nAction concluded successfully. \nHit Enter to continue.",
        "Try Again.",
        "txt file not found!\nA file has been created for you."
    ]
}

promptsCadastrar =  {
    "pt": [ "Digite o título do livro: ",
        "Digite o nome do autor do livro: ",  
        "Digite a qual categoria o livro pertence: ", 
        "Digite o preço do livro: "
    ],
    "en": [ "Book name: ",
           "Author Name: ", 
           "Choose the book's category by number: ", 
           "Book price:"

    ]
}

promptsDeletar = {
    "pt": [
        "A biblioteca está vazia!",
        "Digite o ID do livro que deseja deletar: ",
        "Não existe livro com esse valor.\nAção cancelada.",
        "Escreva um número"
    ],
    "en": [
        "The library is empty!",
        "Enter the ID of the book you want to delete: ",
        "No book with that ID exists.\nAction canceled.",
        "Write a number"
    ]
}

promptsListar = {
    "pt": [
        "1-Listar Tudo\n2-Listar filtrado por categoria especifica\n3-Listar Gastos Totais\n4- Listar gastos filtrado por categoria\n5-Listar filtrado por categoria",
        "Essas são as categorias disponíveis:",
        "\nQual categoria? ",
        "{} R$",
        "{} R$",
        f"{list(enumerate(categorias))}\nQual categoria? ",
        "Digite um número válido!\n Ação cancelada.",
        "Digite um número!\n Ação cancelada.",
        "Ha um index errado no arquivo .txt, no genero literario."
    ],
    "en": [
        "1-List Everything\n2-List filtered by specific category\n3-List Total Expenses\n4-List expenses filtered by category\n5-List filtered by category",
        "These are the available categories:",
        "\nWhich category? ",
        "{} $",
        "{} $",
        f"{list(enumerate(categorias))}\nWhich category? ",
        "Enter a valid number!\n Action canceled.",
        "Enter a number!\n Action canceled.",
        "There is an incorrect index in the .txt file, in the literary genre."
    ]
}

promptsAtualizar = {
    "pt": [
        "1- titulo\n2- autor\n3-genero\n4-custo\n",
        "Digite o número do livro que deseja modificar de acordo com a listagem:",
        "Digite o id de qual categoria você quer editar: ",
        "Qual será o novo valor?",
        "entrou nesse primeiro if"
    ],
    "en": [
        "1- title\n2- author\n3-genre\n4-cost\n",
        "Enter the number of the book you want to modify according to the listing:",
        "Enter the id of which category you want to edit: ",
        "What will be the new value?",
        "Entered this first if"
    ]
}






biblioteca = inicializar()


while True:
    print(prompts[escolhaLingua][0])
    print(prompts[escolhaLingua][1])
    print(prompts[escolhaLingua][2])
    print(prompts[escolhaLingua][3])
    print(prompts[escolhaLingua][4])
    print(prompts[escolhaLingua][5])
    
    opcao = input(prompts[escolhaLingua][6])
    
    if opcao == '1':
        cadastrar()
        input(prompts[escolhaLingua][7])
    elif opcao == '2':
        listar()
        input(prompts[escolhaLingua][7])
    elif opcao == '3':
        listarBasico()
        atualizar()
        input(prompts[escolhaLingua][7])
    elif opcao == '4':
        listarBasico()
        deletar()
        input(prompts[escolhaLingua][7])
    elif opcao == '5':
        doDicionarioParaFile()
        break
    else:
        print(prompts[escolhaLingua][8])
