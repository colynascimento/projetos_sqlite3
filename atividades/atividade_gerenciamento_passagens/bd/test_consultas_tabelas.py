import sqlite3
import os
from prettytable import PrettyTable

conn = sqlite3.connect('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM passagens")
resultados = cursor.fetchall()

os.system("cls")

tabela = PrettyTable()
colunas = [descricao[0] for descricao in cursor.description]
tabela.field_names = colunas

for row in resultados:
    tabela.add_row(row)

print(tabela)
conn.close()