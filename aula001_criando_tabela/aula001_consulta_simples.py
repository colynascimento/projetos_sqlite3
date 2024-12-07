# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 06/12/2024
# Aula 001: SQLite3 - Executando consulta simples

import os
import sqlite3

caminho_banco = os.path.join("..", "projetos_sqlite3", "BD", "meu_banco_de_dados.db")

# print(f"Caminho do banco: {os.path.abspath(caminho_banco)}")

conn = sqlite3.connect(caminho_banco)

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system("cls")
for row in resultados:
    print(row)
conn.close()