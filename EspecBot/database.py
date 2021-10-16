import os
import pandas as pd
import sqlite3

os.system('cls')

#ler = input('coloque o dado aki: ')

local = 'EspecBot/database/'
nome = 'dados_espc.xlsx'
pl = local + nome


dado = pd.read_excel(pl)

data = 'EspecBot/database/DataBase.db'

conn = sqlite3.connect(data)

#dado.to_sql(name='Dados', con=conn) #Cria o Banco de dados

dado_read = pd.read_sql('SELECT * FROM Dados', con=conn)

list = """
        SELECT "CODE", "FRACE", "DADOS"
        FROM Dados;
        """

dado_read = pd.read_sql(list, con=conn, index_col='CODE')
print(dado_read)
