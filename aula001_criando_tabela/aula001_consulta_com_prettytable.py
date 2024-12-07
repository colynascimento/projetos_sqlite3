# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 06/12/2024
# Aula 001: SQLite3 - Consulta com Prettytable

import os
import sqlite3
from prettytable import PrettyTable 

conn = sqlite3.connect("../projetos_sqlite3/BD/meu_banco_de_dados.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system("cls")

# Cria a tabela PrettyTable e deine os nomes das colunas
tabela = PrettyTable()
# Obtém os nomes das colunas a partir do cursor.description
colunas = [descricao[0] for descricao in cursor.description]
# Define os nomes das colunas na tabela PrettyTable
tabela.field_names = colunas

# Adiciona as linhas à tabela
for row in resultados:
    tabela.add_row(row)

print(tabela)
conn.close()