from livros import Livro
from autores import Autor
from generos import Genero
from pedidos import Pedido
from relatorios import Relatorio
from db_connection import conectar

def splash_screen():
    """Exibe a tela de boas-vindas (Splash Screen) com o nome da aplicação e os componentes do grupo."""
    print("#" * 40)
    print("#" * 7 + " SISTEMA DE VENDAS " + "#" * 7)
    print("#" * 40)
    print("# TOTAL DE REGISTROS EXISTENTES #")

    # Executa consultas para contar o número de registros em cada tabela
    connection = conectar()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(1) FROM autores")
    fornecedores_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(1) FROM livros")
    clientes_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(1) FROM generos")
    produtos_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(1) FROM pedidos")
    pedidos_count = cursor.fetchone()[0]


    print(f"1 - AUTORES: {fornecedores_count}")
    print(f"2 - LIVROS: {clientes_count}")
    print(f"3 - GENEROS: {produtos_count}")
    print(f"4 - PEDIDOS: {pedidos_count}")

    print("\n# CRIADO POR: Eduardo Rodrigues #")
    print("# Emanuel #")
    print("# Devandro #")
    print("\n# DISCIPLINA: BANCO DE DADOS #")
    print("# 2024/2 #")
    print("# PROFESSOR: HOWARD ROATTI #")
    print("#" * 40)

def main():
    splash_screen()

    while True:
        
        print("\nMenu Principal:")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Autores")
        print("3. Gerenciar Gêneros")
        print("4. Gerenciar Pedidos")
        print("5. Exibir Relatórios")
        print("6. Sair")
        
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
                for id_livro, titulo_livro, nome_genero, nome_autor in livros:
                 print(f"ID: {id_livro}, Nome: {titulo_livro}, Gênero: {nome_genero}, Autor: {nome_autor}")
            elif opcao_livro == '2':
                id_livro = int(input("Id do Livro: "))
                titulo = input("Título: ")
                id_autor = int(input("ID do Autor: "))
                id_genero = int(input("ID do Gênero: "))
                novo_livro = Livro(id_livro=id_livro, titulo_livro=titulo, id_autor=id_autor, id_genero=id_genero)
                novo_livro.inserir()
                print("Livro adicionado com sucesso!")
            elif opcao_livro == '3':
                id = int(input("ID do Livro: "))
                titulo = input("Novo Título: ")
                id_autor = int(input("Novo ID do Autor: "))
                id_genero = int(input("Novo ID do Gênero: "))
                livro_atualizado = Livro(id_livro=id, titulo_livro=titulo, id_autor=id_autor, id_genero=id_genero)
                livro_atualizado.atualizar()
                print("Livro atualizado com sucesso!")
            elif opcao_livro == '4':
                id = int(input("ID do Livro: "))
                livro_remover = Livro(id_livro=id)
                livro_remover.remover()
                print("Livro removido com sucesso!")
            elif opcao_livro == '5':
                continue
            else:
                print("Opção inválida.")
        
        elif opcao == '2':
            # Gerenciamento de Autores
            print("\nGerenciar Autores:")
            print("\nGerenciar Autores:")
            print("1. Listar Autores")
            print("2. Adicionar Autor")
            print("3. Atualizar Autor")
            print("4. Remover Autor")
            print("5. Voltar ao Menu Principal")
            opcao_autor = input("Escolha uma opção: ")
            
            if opcao_autor == '1':
                 autores = Autor.listar()
                 for id_autor, nome_autor in autores:
                  print(f"ID: {id_autor}, Nome: {nome_autor}")
            elif opcao_autor == '2':
                id = int(input("ID do Autor: "))
                nome = input("Nome do Autor: ")
                novo_autor = Autor(id_autor=id,nome_autor=nome)
                novo_autor.inserir()
                print("Autor adicionado com sucesso!")
            elif opcao_autor == '3':
                id = int(input("ID do Autor: "))
                nome = input("Novo Nome: ")
                autor_atualizado = Autor(id_autor=id, nome_autor=nome)
                autor_atualizado.atualizar()
                print("Autor atualizado com sucesso!")
            elif opcao_autor == '4':
                id = int(input("ID do Autor: "))
                autor_remover = Autor(id_autor=id)
                autor_remover.remover()
                print("Autor removido com sucesso!")
            elif opcao_autor == '5':
                continue
            else:
                print("Opção inválida.")
        
        elif opcao == '3':
            # Gerenciamento de Gêneros
            print("\nGerenciar Gêneros:")
            print("1. Listar Gêneros")
            print("2. Adicionar Gênero")
            print("3. Atualizar Gênero")
            print("4. Remover Gênero")
            print("5. Voltar ao Menu Principal")
            opcao_genero = input("Escolha uma opção: ")
            
            if opcao_genero == '1':
                 generos = Genero.listar()
                 for id_genero, nome_genero in generos:
                  print(f"ID: {id_genero}, Nome: {nome_genero}")
            elif opcao_genero == '2':
                id_genero = int(input("ID do Gênero: "))
                nome = input("Nome do Gênero: ")
                novo_genero = Genero(id_genero=id_genero, nomegenero=nome)
                novo_genero.inserir()
                print("Gênero adicionado com sucesso!")
            elif opcao_genero == '3':
                id = int(input("ID do Gênero: "))
                nome = input("Novo Nome: ")
                genero_atualizado = Genero(id_genero=id, nomegenero=nome)
                genero_atualizado.atualizar()
                print("Gênero atualizado com sucesso!")
            elif opcao_genero == '4':
                id = int(input("ID do Gênero: "))
                genero_remover = Genero(id_genero=id)
                genero_remover.remover()
                print("Gênero removido com sucesso!")
            elif opcao_genero == '5':
                continue
            else:
                print("Opção inválida.")
        
        elif opcao == '4':
            # Gerenciamento de Pedidos
            print("\nGerenciar Pedidos:")
            print("1. Listar Pedidos")
            print("2. Adicionar Pedido")
            print("3. Atualizar Pedido")
            print("4. Remover Pedido")
            print("5. Voltar ao Menu Principal")
            opcao_pedido = input("Escolha uma opção: ")
            
            if opcao_pedido == '1':
                pedidos = Pedido.listar()
                for id_pedido,id_livro,quantidade,data_pedido in pedidos:
                    print(f"IdPedido: {id_pedido} Livro: {id_livro} Quantidade: {quantidade} DataPedido: {data_pedido}")
            elif opcao_pedido == '2':
                id_pedido = int(input("ID do Pedido: "))
                id_livro = int(input("ID do Livro: "))
                quantidade = int(input("Quantidade: "))
                data_pedido = input("Data do Pedido: ")
                novo_pedido = Pedido(id_pedido=id_pedido,id_livro=id_livro, quantidade=quantidade,data_pedido=data_pedido)
                novo_pedido.inserir()
                print("Pedido adicionado com sucesso!")
            elif opcao_pedido == '3':
                id_pedido = int(input("ID do Pedido: "))
                id_livro = int(input("Novo ID do Livro: "))
                quantidade = int(input("Nova Quantidade: "))
                data_pedido = input("Nova data do pedido: ")
                pedido_atualizado = Pedido(id_pedido=id_pedido, id_livro=id_livro, quantidade=quantidade, data_pedido=data_pedido)
                pedido_atualizado.atualizar()
                print("Pedido atualizado com sucesso!")
            elif opcao_pedido == '4':
                id_pedido = int(input("ID do Pedido: "))
                pedido_remover = Pedido(id_pedido=id_pedido)
                pedido_remover.remover()
                print("Pedido removido com sucesso!")
            elif opcao_pedido == '5':
                continue
            else:
                print("Opção inválida.")
        
        elif opcao == '5':
            print("\nExibir Relatórios:")
            print("1. Relatório de Pedidos por Gênero")
            print("2. Relatório de Pedidos por Autor")
            print("3. Relatório Detalhado de todos os  Pedidos")
            print("4. Voltar ao Menu Principal")
            opcao_relatorio = input("Escolha uma opção: ")
            
            if opcao_relatorio == '1':
                resultados = Relatorio.relatorio_pedidos_por_genero()
                for nome_genero,quantidade, in resultados:
                    print(f"Nome Genero: {nome_genero} Quantidade: {quantidade}")
            elif opcao_relatorio == '2':
                resultados = Relatorio.relatorio_todos_autores_com_pedidos()
                for nome_autor,quantidade, in resultados:
                    print(f"NomeAutor: {nome_autor} Quantidade: {quantidade}")
            elif opcao_relatorio == '3':
                Relatorio.relatorio_pedidos_detalhados()
            elif opcao_relatorio == '4':
                continue
            else:
                print("Opção inválida.")
        
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
