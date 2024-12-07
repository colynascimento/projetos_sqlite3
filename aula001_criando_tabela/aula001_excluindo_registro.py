# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 06/12/2024
# Aula 001: SQLite3 - Excluindo um registro

import os
import sqlite3

conn = sqlite3.connect("C:\coly_git\projetos_sqlite3\BD\meu_banco_de_dados.bd")

cursor = conn.cursor()

os.system('cls')

nome_cliente = input('Digite o nome do cliente para excluir: ')

# Executa a exclusão com base no nome fornecido pelo usuário
cursor.execute('DELETE FROM clientes where NOME = ?', (nome_cliente))
conn.commit()

print('Cliente deletado com sucesso!')

# Fecha a conexão
conn.close()