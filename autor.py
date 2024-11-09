from db_connection import conectar

class Autor:
    def __init__(self, id=None, nome=''):
        self.id = id
        self.nome = nome

    def inserir(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO autores (nome) VALUES (?)", (self.nome,))
        conn.commit()
        conn.close()

    def atualizar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE autores SET nome = ? WHERE id = ?", (self.nome, self.id))
        conn.commit()
        conn.close()

    def remover(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM autores WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM autores")
        autores = cursor.fetchall()
        conn.close()
        return autores
