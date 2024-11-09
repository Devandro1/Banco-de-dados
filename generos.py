from db_connection import conectar

class Genero:
    def __init__(self, id=None, nome=''):
        self.id = id
        self.nome = nome

    def inserir(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO generos (nome) VALUES (?)", (self.nome,))
        conn.commit()
        conn.close()

    def atualizar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE generos SET nome = ? WHERE id = ?", (self.nome, self.id))
        conn.commit()
        conn.close()

    def remover(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM generos WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM generos")
        generos = cursor.fetchall()
        conn.close()
        return generos
