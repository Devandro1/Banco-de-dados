from db_connection import conectar

class Pedido:
    def __init__(self, id=None, id_livro=None, quantidade=0):
        self.id = id
        self.id_livro = id_livro
        self.quantidade = quantidade

    def inserir(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pedidos (id_livro, quantidade) VALUES (?, ?)",
            (self.id_livro, self.quantidade)
        )
        conn.commit()
        conn.close()

    def atualizar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE pedidos SET id_livro = ?, quantidade = ? WHERE id = ?",
            (self.id_livro, self.quantidade, self.id)
        )
        conn.commit()
        conn.close()

    def remover(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pedidos WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos")
        pedidos = cursor.fetchall()
        conn.close()
        return pedidos
