import sqlite3
import os
import cliente.cliente_dao
import cliente.cliente
import linha_aerea
import voo
import sys
from prettytable import PrettyTable

os.system('cls')

print('Menu')
print('_' * 60)
print('1 - Clientes')
print('2 - Linhas Aéreas')
print('3 - Vôos')
print('_' * 60)

area = input('Qual área deseja acessar? ')

if area == '1':
    os.system('cls')

    print('Listar Clientes:')

    dao = cliente.cliente_dao.ClienteDao('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')
    clientes = dao.listar_todos()

    if not clientes:
        print('Nenhum cliente cadastrado.')
        print('_' * 60)
        input('Aperte uma tecla para voltar ao menu')

    else:
        tabela = PrettyTable()
        # field_names define os nomes que aparecerão no cabeçalho da tabela
        tabela.field_names = ['ID', 'Nome', 'Data Nascimento', 'Nacionalidade', 'Documento', 'Telefone', 'Email', 'Deficiencia Legal?']

        for cliente in clientes:
            tabela.add_row([cliente.id_cliente, cliente.nome, cliente.data_nascimento, cliente.nacionalidade, cliente.documento, cliente.telefone, cliente.email, cliente.deficiencia_legal])

        print(tabela)
        print('Opções')
        print('_' * 60)
        print('0 - Voltar ao Menu Principal')
        print('1 - Visualizar Histórico de Passagens')
        print('_' * 60)

        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            print('_' * 60)
            id_cliente = input('Insira o id do cliente: ')

            # if id_cliente == 


    
