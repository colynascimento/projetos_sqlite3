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

nome_cliente = input('Digite o nome do cliente: ')
nova_idade = int(input('Digite a nova idade: '))

# Atualiza a idade com base no nome fornecido pelo usuário
cursor.execute('UPDATE clientes SET idade = ? WHERE nome = ?', 
               (nova_idade, nome_cliente))

# Salva as alterações no banco de dados
conn.commit()
print('Dados atualizados com sucesso!')
conn.close()