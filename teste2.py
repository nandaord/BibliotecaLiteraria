# Dicionário para guardar as coisa
biblioteca = {}

# confg para colocar 
def cadastrar():
    
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    categoria = input("Digite a qual categoria o livro pertence: ")
    preco = float(input("Digite o preço do livro: "))
    #contador = len(biblioteca)
    #variavel pra contar
    
    #livro = []
    gambiarra = str(len(biblioteca))
    biblioteca[gambiarra] = [nome, autor, categoria, preco]
        #nome, autor, categoria, preço
    print("Livro cadastrado com sucesso!")
    print(biblioteca)
    print(biblioteca[contador])

# conf para aparecer tudo
def listarlivros():
    for nome, livro in biblioteca.items():
        print(f"Nome: {nome}, Autor: {livro['Autor']}, Categoria: {livro['Categoria']}, Preço: R${livro['Preço']:.2f}")


# conf livro não achado e add
def atualizar():
    nome = input("Nome do livro a ser atualizado: ")
    
    if nome in biblioteca:
        autor = input("Novo autor do livro: ")
        categoria = input("Nova categoria do livro: ")
        preco = float(input("Novo preço do livro: "))
        
        livro = {
            "Nome": nome,
            "Autor": autor,
            "Categoria": categoria,
            "Preço": preco
        }
        
        biblioteca[nome] = livro
        print("Livro atualizado com sucesso!")
    else:
        print("Livro não encontrado.")

#  excluir um livro
def excluir():
    nome = input("Nome do livro a ser excluído: ")
    
    if nome in biblioteca:
        del biblioteca[nome]
        print("Livro excluído com sucesso!")
    else:
        print("Livro não encontrado.")

# Menu interativo
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
    elif opcao == '2':
        listarlivros()
    elif opcao == '3':
        atualizar()
    elif opcao == '4':
        excluir()
    elif opcao == '5':
        break
    else:
        print("Tente novamente")