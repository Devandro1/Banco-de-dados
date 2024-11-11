from db_connection import conectar

class Genero:
    def __init__(self, id_genero=None, nomegenero=''):
        self.id = id_genero
        self.nome = nomegenero

    def inserir(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO generos (id_genero, nome_genero) VALUES (?, ?)", (self.id, self.nome))
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_genero, nome_genero FROM generos")
        generos = cursor.fetchall()
        conn.close()
        return generos

    def atualizar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE generos SET nome_genero = ? WHERE id_genero = ?", (self.nome, self.id))
        conn.commit()
        conn.close()

    def remover(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM generos WHERE id_genero = ?", (self.id,))
        conn.commit()
        conn.close()
