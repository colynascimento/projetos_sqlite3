# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 06/12/2024
# Aula 001: SQLite3 - Inserindo dados na tabela

import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("C:\coly_git\projetos_sqlite3\BD\meu_banco_de_dados.bd")

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

# definição de uma tupla com os dados
dados_cliente = ("João Silva", 30)

# Placeholders (?, ?): Os pontos de interrogação são usados como
# "espaços reservados". Eles serão substituídos pelos valores da 
# tupla dados_cliente (ou seja, "João Silva" e 30).
# Por quê: Usar placeholders é uma prática recomendada,
# pois previne ataques de injeção de SQL.
cursor.execute("INSERT INTO clientes (nome, idade) VALUES (?, ?)", dados_cliente)

conn.commit() # Salva a transação no banco de dados
conn.close() # fecha conexão