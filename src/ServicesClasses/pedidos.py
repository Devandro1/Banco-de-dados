from db_connection import conectar

class Pedido:
    def __init__(self, id_pedido=None, id_livro=None, quantidade=0,data_pedido=None):
        self.id = id_pedido
        self.id_livro = id_livro
        self.quantidade = quantidade
        self.data_pedido = data_pedido

    def inserir(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pedidos (id_pedido, id_livro, quantidade,data_pedido) VALUES (?, ?, ?,?)",
            (self.id,self.id_livro, self.quantidade, self.data_pedido)
        )
        conn.commit()
        conn.close()

    def atualizar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE pedidos SET id_livro = ?, quantidade = ?, data_pedido = ? WHERE id_pedido = ?",
            (self.id_livro, self.quantidade, self.data_pedido, self.id)
        )
        conn.commit()
        conn.close()

    def remover(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pedidos WHERE id_pedido = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT pedidos.id_pedido, livros.titulo_livro, pedidos.quantidade , pedidos.data_pedido FROM pedidos JOIN livros ON pedidos.id_livro = livros.id_livro")
        pedidos = cursor.fetchall()
        conn.close()
        return pedidos
