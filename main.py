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
        print("Arquivo txt nao foi encontrado!")
        print("Criaremos um arquivo para voce.")
        arquivo = open("antonio.txt", "w")
        arquivo.close()

    print(biblioteca)
    return biblioteca


categorias = ["Terror", "Aventura", "Sci-fi","Romance","Infantil","Drama","Gêneros Literário","Young Adult", "Outros"]

def cadastrar():
    
    with open("antonio.txt", "a", encoding="utf-8") as arquivo:
        while True:
            titulo = input("Digite o nome do livro: ")
            if titulo.strip()=="": #titulo.strip() tira os espaços vazio da extremidade
                print("Por favor, digite algo!")
            else:
                break 
        autor = input("Digite o nome do autor do livro: ")
        while True:
            titulo = input("Digite o nome do livro: ")
            if titulo.strip()=="": 
                print("Por favor, digite algo!")
            else:
                break 
    
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
        print("A biblioteca está vazia!")
    else:
        listar()
        try:
            idParaDeletar = int(input("Digite o ID do livro que deseja deletar: "))
            del biblioteca["titulo"][idParaDeletar]
            del biblioteca["autor"][idParaDeletar]
            del biblioteca["categoria"][idParaDeletar]
            del biblioteca["valor"][idParaDeletar]
            doDicionarioParaFile() # quero reescrever o file INTEIRO, baseado na nova biblioteca
        except IndexError:
            print("Não existe livro com esse valor.\nAção cancelada.")
        except ValueError:
            print("Escreva um número")


                
def doDicionarioParaFile():
    with open("antonio.txt", ("w"), encoding="utf-8") as arquivo:
        for i in range(len(biblioteca["titulo"])):
            arquivo.write(biblioteca["titulo"][i] + "\n") # I want each of these to be in one line
            arquivo.write(biblioteca["autor"][i] + "\n")
            arquivo.write(str(biblioteca["categoria"][i]) + "\n")
            arquivo.write(str(biblioteca["valor"][i]) + "\n")
        arquivo.close()

def listar():
    print(" 1-Listar Tudo\n2-Listar filtrado por categoria especifica\n3-Listar Gastos Totais\n4- Listar gastos filtrado por categoria\n5-Listar filtrado por categoria")

    try:
        choice = int(input())

        if choice == 1:
            listarSimples()
        elif choice == 2:
            choiceCategoria = int(input(f"{list(enumerate(categorias))}\nQual categoria? "))
            for i in range(len(biblioteca['titulo'])):
                if biblioteca['categoria'][i] == choiceCategoria:
                    print(f"""{i}. '{biblioteca['titulo'][i]}' por {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; R$: {biblioteca["valor"][i]}.""")
        elif choice == 3:
            custoTotal = 0
            for i in range(len(biblioteca['titulo'])):
                custoTotal += biblioteca["valor"][i]
            print(f"{custoTotal} R$")
        elif choice == 4:
            custoTotal = 0
            choiceCategoria = int(input(f"{list(enumerate(categorias))}\nQual categoria? "))
            
            for i in range(len(biblioteca['titulo'])):
                if biblioteca['categoria'][i] == choiceCategoria:
                    custoTotal += biblioteca["valor"][i]
            print(f"{custoTotal} R$")


        elif choice == 5:
            print("\n")
            for x in range(0, 9):
                print(f"\nLivros de {categorias[x]}: \n")
                for i in range(len(biblioteca['titulo'])):
                    if biblioteca['categoria'][i] == x:
                        print(f"""{i}. '{biblioteca['titulo'][i]}' por {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; R$: {biblioteca["valor"][i]}.""")
        else:
            print("Digite um número válido!\n Ação cancelada.")
    except ValueError:
        print("Digite um número!\n Ação cancelada.")


        # agr pra printar


def listarSimples():
    for i in range(len(biblioteca['titulo'])):
                print(f"""{i}. '{biblioteca['titulo'][i]}' por {biblioteca['autor'][i]}\n{categorias[biblioteca['categoria'][i]]} ; R$: {biblioteca["valor"][i]}.""")


def atualizar():
        print("\n")
        posicao=int(input(f"Digite o número do livro que deseja modificar de acordo com a listagem:"))
        print("1- titulo\n2- autor\n3-genero\n4-custo\n")
        item=int(input("Digite o id de qual categoria voce quer editar: "))
        novo=input("Qual será o novo valor?")


        if item == 1:
            biblioteca["titulo"][posicao] = novo
            print("entrou nesse primeiro if")

        elif item ==2:
            biblioteca["autor"][posicao] = novo

        elif item ==3:
            biblioteca["categoria"][posicao] = int(novo)

        elif item ==4:
            biblioteca["valor"][posicao] = float(novo)
        print(biblioteca)
        doDicionarioParaFile()
        
    
        

biblioteca = inicializar()


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
        listarSimples()
        atualizar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '4':
        listarSimples()
        deletar()
        input("\nAção concluída com sucesso. \nAperte Enter para continuar.")
    elif opcao == '5':
        doDicionarioParaFile()
        break
    else:
        print("Tente novamente")


biblioteca = inicializar()

listar()
