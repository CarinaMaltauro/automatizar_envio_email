import pandas as pd

import mysql.connector 
from mysql.connector import Error

from senha_mysql import senha

# Função para criar a conexão
def create_connection():
    try:
        # Conectar ao MySQL
        connection = mysql.connector.connect(
            host="localhost",   # ou IP do servidor MySQL
            user="root",        # seu usuário MySQL
            password=senha,   # sua senha MySQL
            database="banco_teste"  # nome do banco de dados
        )
        
        #if connection.is_connected():
            #print("Conexão bem-sucedida ao banco de dados MySQL!")

        return connection
        
    except Error as e:
        #print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Função para fechar a conexão
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        #print("Conexão fechada.")

# Criar a conexão
connection = create_connection()

# Executar consulta 
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT nome, email FROM users WHERE regiao = 'Sul';")  # Exemplo: mostra o banco de dados atual
    # Pegando todas as linhas de uma vez 
    dados = cursor.fetchall()
    #print("Você está conectado ao banco de dados:", dados)

# Criar DataFrame do pandas com os dados
df = pd.DataFrame(dados, columns=["nome","email"])


# Fechar a conexão
close_connection(connection)