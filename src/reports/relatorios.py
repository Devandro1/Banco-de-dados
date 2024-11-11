from db_connection import conectar

class Relatorio:

    @staticmethod

    def relatorio_pedidos_por_genero():
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
     connection.close()
     return resultados

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
    def relatorio_todos_autores_com_pedidos():
        connection = conectar()
        cursor = connection.cursor()
        
        # Usando LEFT JOIN para garantir que todos os autores sejam incluídos, mesmo que não tenham pedidos
        cursor.execute("""
            SELECT autores.nome_autor, 
                   ISNULL(SUM(pedidos.quantidade), 0) AS total_quantidade
            FROM autores
            LEFT JOIN livros ON autores.id_autor = livros.id_autor
            LEFT JOIN pedidos ON livros.id_livro = pedidos.id_livro
            GROUP BY autores.nome_autor
        """)
        
        resultados = cursor.fetchall()
        connection.close()
        return resultados
