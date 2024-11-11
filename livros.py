from db_connection import conectar

class Livro:
    def __init__(self, id_livro=None, titulo_livro='', id_autor=None, id_genero=None):
        self.id = id_livro
        self.titulo = titulo_livro
        self.id_autor = id_autor
        self.id_genero = id_genero

    def inserir(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO livros (id_livro, titulo_livro, id_autor, id_genero) VALUES (?, ?, ?, ?)",
            (self.id, self.titulo, self.id_autor, self.id_genero)
        )
        conn.commit()
        conn.close()

    def atualizar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE livros SET titulo_livro = ?, id_autor = ?, id_genero = ? WHERE id_livro = ?",
            (self.titulo, self.id_autor, self.id_genero, self.id)
        )
        conn.commit()
        conn.close()

    def remover(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE id_livro = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT livros.id_livro, livros.titulo_livro, generos.nome_genero, autores.nome_autor FROM livros INNER JOIN generos ON livros.id_genero = generos.id_genero INNER JOIN autores ON livros.id_autor = autores.id_autor ")
        livros = cursor.fetchall()
        conn.close()
        return livros
