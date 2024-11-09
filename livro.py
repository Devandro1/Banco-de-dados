from db_connection import conectar

class Livro:
    def __init__(self, id=None, titulo='', id_autor=None, id_genero=None):
        self.id = id
        self.titulo = titulo
        self.id_autor = id_autor
        self.id_genero = id_genero

    def inserir(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO livros (titulo, id_autor, id_genero) VALUES (?, ?, ?)",
            (self.titulo, self.id_autor, self.id_genero)
        )
        conn.commit()
        conn.close()

    def atualizar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE livros SET titulo = ?, id_autor = ?, id_genero = ? WHERE id = ?",
            (self.titulo, self.id_autor, self.id_genero, self.id)
        )
        conn.commit()
        conn.close()

    def remover(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        conn.close()
        return livros
