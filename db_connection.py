import pyodbc   

def conectar():
    # Substitua as informações da sua conexão
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=EDUARDO\\BIBLIOTECA;'
        'DATABASE=Biblioteca;'
        'UID=sa;'
        'PWD=senhabanco;'
        'TrustServerCertificate=yes;'
    )
    return conn
