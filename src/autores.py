from db_connection import conectar

class Autor:
    def __init__(self, id_autor=None, nome_autor=''):
        self.id = id_autor
        self.nome = nome_autor

    def inserir(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO autores (id_autor , nome_autor) VALUES (?,?)", (self.id,self.nome))
        conn.commit()
        conn.close()

    def atualizar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE autores SET nome_autor = ? WHERE id_autor = ?", (self.nome, self.id))
        conn.commit()
        conn.close()

    def remover(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM autores WHERE id_autor = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_autor, nome_autor FROM autores")
        autores = cursor.fetchall()
        conn.close()
        return autores
