import pyodbc   # type: ignore

def conectar():
    # Substitua as informações da sua conexão
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=seu_servidor;'
        'DATABASE=sua_base_de_dados;'
        'UID=seu_usuario;'
        'PWD=sua_senha'
    )
    return conn
