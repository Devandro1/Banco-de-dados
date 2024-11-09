from db_connection import conectar

class Relatorio:

    @staticmethod
    def relatorio_pedidos_por_genero():
        """Relatório sumarizando o valor total dos pedidos agrupados por gênero."""
        connection = Relatorio.conectar()
        cursor = connection.cursor()
        
        cursor.execute("""
        SELECT g.nome AS genero, SUM(p.quantidade) AS total_quantidade
        FROM pedidos p
        JOIN livros l ON p.id_livro = l.id
        JOIN generos g ON l.id_genero = g.id
        GROUP BY g.nome
        """)
        
        resultados = cursor.fetchall()
        print("\nRelatório de Vendas por Gênero:")
        for genero, total_quantidade in resultados:
            print(f"Gênero: {genero}, Total de Pedidos: {total_quantidade}")
        
        connection.close()

    @staticmethod
    def relatorio_pedidos_detalhados():
        """Relatório detalhado com junção de tabelas, mostrando informações de pedidos, livros, autores e gêneros."""
        connection = Relatorio.conectar()
        cursor = connection.cursor()
        
        cursor.execute("""
        SELECT p.id, l.titulo, a.nome AS autor, g.nome AS genero, p.quantidade
        FROM pedidos p
        JOIN livros l ON p.id_livro = l.id
        JOIN autores a ON l.id_autor = a.id
        JOIN generos g ON l.id_genero = g.id
        """)
        
        resultados = cursor.fetchall()
        print("\nRelatório Detalhado de Pedidos:")
        for id_pedido, titulo, autor, genero, quantidade in resultados:
            print(f"Pedido ID: {id_pedido}, Livro: {titulo}, Autor: {autor}, Gênero: {genero}, Quantidade: {quantidade}")
        
        connection.close()
