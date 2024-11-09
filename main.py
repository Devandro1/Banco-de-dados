from livro import Livro
from autor import Autor
from generos import Genero
from pedido import Pedido

def main():
    while True:
        print("\nMenu Principal:")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Autores")
        print("3. Gerenciar Gêneros")
        print("4. Gerenciar Pedidos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\nGerenciar Livros:")
            print("1. Listar Livros")
            print("2. Adicionar Livro")
            print("3. Atualizar Livro")
            print("4. Remover Livro")
            print("5. Voltar ao Menu Principal")
            opcao_livro = input("Escolha uma opção: ")
            
            if opcao_livro == '1':
                livros = Livro.listar()
                for livro in livros:
                    print(livro)
            elif opcao_livro == '2':
                titulo = input("Título: ")
                id_autor = int(input("ID do Autor: "))
                id_genero = int(input("ID do Gênero: "))
                novo_livro = Livro(titulo=titulo, id_autor=id_autor, id_genero=id_genero)
                novo_livro.inserir()
                print("Livro adicionado com sucesso!")
            elif opcao_livro == '3':
                id = int(input("ID do Livro: "))
                titulo = input("Novo Título: ")
                id_autor = int(input("Novo ID do Autor: "))
                id_genero = int(input("Novo ID do Gênero: "))
                livro_atualizado = Livro(id=id, titulo=titulo, id_autor=id_autor, id_genero=id_genero)
                livro_atualizado.atualizar()
                print("Livro atualizado com sucesso!")
            elif opcao_livro == '4':
                id = int(input("ID do Livro: "))
                livro_remover = Livro(id=id)
                livro_remover.remover()
                print("Livro removido com sucesso!")
            elif opcao_livro == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '2':
            print("\nGerenciar Autores:")
            print("1. Listar Autores")
            print("2. Adicionar Autor")
            print("3. Atualizar Autor")
            print("4. Remover Autor")
            print("5. Voltar ao Menu Principal")
            opcao_autor = input("Escolha uma opção: ")
            
            if opcao_autor == '1':
                autores = Autor.listar()
                for autor in autores:
                    print(autor)
            elif opcao_autor == '2':
                nome = input("Nome do Autor: ")
                novo_autor = Autor(nome=nome)
                novo_autor.inserir()
                print("Autor adicionado com sucesso!")
            elif opcao_autor == '3':
                id = int(input("ID do Autor: "))
                nome = input("Novo Nome: ")
                autor_atualizado = Autor(id=id, nome=nome)
                autor_atualizado.atualizar()
                print("Autor atualizado com sucesso!")
            elif opcao_autor == '4':
                id = int(input("ID do Autor: "))
                autor_remover = Autor(id=id)
                autor_remover.remover()
                print("Autor removido com sucesso!")
            elif opcao_autor == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '3':
            print("\nGerenciar Gêneros:")
            print("1. Listar Gêneros")
            print("2. Adicionar Gênero")
            print("3. Atualizar Gênero")
            print("4. Remover Gênero")
            print("5. Voltar ao Menu Principal")
            opcao_genero = input("Escolha uma opção: ")
            
            if opcao_genero == '1':
                generos = Genero.listar()
                for genero in generos:
                    print(genero)
            elif opcao_genero == '2':
                nome = input("Nome do Gênero: ")
                novo_genero = Genero(nome=nome)
                novo_genero.inserir()
                print("Gênero adicionado com sucesso!")
            elif opcao_genero == '3':
                id = int(input("ID do Gênero: "))
                nome = input("Novo Nome: ")
                genero_atualizado = Genero(id=id, nome=nome)
                genero_atualizado.atualizar()
                print("Gênero atualizado com sucesso!")
            elif opcao_genero == '4':
                id = int(input("ID do Gênero: "))
                genero_remover = Genero(id=id)
                genero_remover.remover()
                print("Gênero removido com sucesso!")
            elif opcao_genero == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '4':
            print("\nGerenciar Pedidos:")
            print("1. Listar Pedidos")
            print("2. Adicionar Pedido")
            print("3. Atualizar Pedido")
            print("4. Remover Pedido")
            print("5. Voltar ao Menu Principal")
            opcao_pedido = input("Escolha uma opção: ")
            
            if opcao_pedido == '1':
                pedidos = Pedido.listar()
                for pedido in pedidos:
                    print(pedido)
            elif opcao_pedido == '2':
                id_livro = int(input("ID do Livro: "))
                quantidade = int(input("Quantidade: "))
                novo_pedido = Pedido(id_livro=id_livro, quantidade=quantidade)
                novo_pedido.inserir()
                print("Pedido adicionado com sucesso!")
            elif opcao_pedido == '3':
                id = int(input("ID do Pedido: "))
                id_livro = int(input("Novo ID do Livro: "))
                quantidade = int(input("Nova Quantidade: "))
                pedido_atualizado = Pedido(id=id, id_livro=id_livro, quantidade=quantidade)
                pedido_atualizado.atualizar()
                print("Pedido atualizado com sucesso!")
            elif opcao_pedido == '4':
                id = int(input("ID do Pedido: "))
                pedido_remover = Pedido(id=id)
                pedido_remover.remover()
                print("Pedido removido com sucesso!")
            elif opcao_pedido == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
