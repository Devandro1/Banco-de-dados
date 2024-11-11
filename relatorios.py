from db_connection import conectar

class Relatorio:

    @staticmethod
    def relatorio_pedidos_por_genero():
        """Relatório sumarizando o valor total dos pedidos agrupados por gênero."""
        connection = conectar()
        cursor = connection.cursor()
        
        cursor.execute("""
        SELECT g.nome_genero AS genero, SUM(p.quantidade) AS total_quantidade
        FROM PEDIDOS p
        JOIN LIVROS l ON p.id_livro = l.id_livro
        JOIN GENEROS g ON l.id_genero = g.id_genero
        GROUP BY g.nome_genero
        """)
        
        resultados = cursor.fetchall()
        print("\nRelatório de Vendas por Gênero:")
        for genero, total_quantidade in resultados:
            print(f"Gênero: {genero}, Total de Pedidos: {total_quantidade}")
        
        connection.close()

    @staticmethod
    def relatorio_pedidos_detalhados():
        """Relatório detalhado com junção de tabelas, mostrando informações de pedidos, livros, autores e gêneros."""
        connection = conectar()
        cursor = connection.cursor()
        
        cursor.execute("""
        SELECT p.id_pedido, l.titulo_livro, a.nome_autor AS autor, g.nome_genero AS genero, p.quantidade
        FROM PEDIDOS p
        JOIN LIVROS l ON p.id_livro = l.id_livro
        JOIN AUTORES a ON l.id_autor = a.id_autor
        JOIN GENEROS g ON l.id_genero = g.id_genero
        """)
        
        resultados = cursor.fetchall()
        print("\nRelatório Detalhado de Pedidos:")
        for id_pedido, titulo, autor, genero, quantidade in resultados:
            print(f"Pedido ID: {id_pedido}, Livro: {titulo}, Autor: {autor}, Gênero: {genero}, Quantidade: {quantidade}")
        
        connection.close()

    @staticmethod
    def relatorio_pedidos_por_autor():
        """Relatório sumarizando o valor total dos pedidos agrupados por Autor."""
        connection = conectar()
        cursor = connection.cursor()
        
        cursor.execute("""
        SELECT autores.nome_autor, SUM(pedidos.quantidade) AS total_quantidade
        FROM PEDIDOS 
        INNER JOIN livros ON pedidos.id_livro = livros.id_livro
        INNER JOIN autores ON livros.id_autor = autores.id_autor
        GROUP BY autores.nome_autor
        """)
        
        resultados = cursor.fetchall()
        print("\nRelatório de Vendas por Autor:")
        for nome_autor, total_quantidade in resultados:
            print(f"Nome Autor: {nome_autor} Quantidade : {total_quantidade}")
        
        connection.close()
