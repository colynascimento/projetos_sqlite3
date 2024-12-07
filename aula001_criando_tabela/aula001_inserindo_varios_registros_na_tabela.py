# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 06/12/2024
# Aula 001: SQLite3 - Inserindo vários registros na tabela

import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("../projetos_sqlite3/BD/meu_banco_de_dados.db")

cursor = conn.cursor()

dados_varios_clientes = [
    ("Maria Souza", 25),
    ("Carlos Pereira", 35),
    ("Pedro José", 28),
    ("Ana Costa", 28),
    ("Luís Gomes", 30),
    ("Fernanda Lima", 22),
    ("Roberto Silva", 40),
    ("Juliana Almeida", 33),
    ("Lucas Martins", 27),
    ("Sofia Ferreira", 31)
]

cursor.executemany(
    "INSERT INTO clientes (nome, idade) VALUES (?, ?)", dados_varios_clientes
)

conn.commit()

conn.close()