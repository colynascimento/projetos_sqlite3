import sqlite3
import os

conn = sqlite3.connect('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system("cls")

for row in resultados:
    print(row)
conn.close()