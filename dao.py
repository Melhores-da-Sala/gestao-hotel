import mysql.connector

def connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',          # Garanta que o usuário é 'root'
        password='1234', # Coloque AQUI a senha que você usa para entrar no MySQL Workbench
        database='hotelaria',
        port=3306             # Porta padrão do MySQL
    )