from prettytable import PrettyTable
from cliente.cliente_dao import ClienteDao
import os

def menu_clientes():
    # caminho do bd
    dao = ClienteDao('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')
    
    while True:
        os.system('cls')

        print('Menu de Clientes')
        print('_' * 60)

        clientes = dao.listar_todos()

        if not clientes:
            print('Nenhum cliente cadastrado.')

        else:
            tabela = PrettyTable()
            tabela.field_names = ['ID', 'Nome', 'Data Nascimento', 'Nacionalidade', 'Documento', 'Telefone', 'Email', 'Deficiencia Legal?']
    
            for cliente in clientes:
                tabela.add_row([cliente.id_cliente, cliente.nome, cliente.data_nascimento, cliente.nacionalidade, cliente.documento, cliente.telefone, cliente.email, cliente.deficiencia_legal])
    
            print(tabela)
            
        print('Opções')
        print('_' * 60)
        print('0 - Voltar ao Menu Principal')
        print('1 - Visualizar Histórico de Passagens')
        print('_' * 60)

        menu = input('Digite a opção desejada: ')

        if menu == '0':
            return
        elif menu == '1':
            visualizar_historico_passagens(dao)
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione qualquer tecla para continuar.")

def visualizar_historico_passagens(dao):
    print('_' * 60)
    id_cliente = input('Insira o id do cliente: ')
    cliente = dao.buscar_por_id(id_cliente)

    if cliente is None:
        print('Cliente não encontrado.')

    else:
        os.system('cls')
        print(f'Histórico de passagens de {cliente.nome}:')
        historico = dao.buscar_historico_passagens(id_cliente)

        if not historico:
            print('Nenhuma passagem comprada.')
        else:
            tabela = PrettyTable()
            tabela.field_names = ['Codigo Passagem', 'Origem', 'Destino', 'Data/Hora Partida', 'Data/Hora Chegada', 'Preco', 'Linha Aérea']
            
            for passagem in historico:
                tabela.add_row(passagem)
            print(tabela)

    input("Pressione qualquer tecla para voltar ao menu de clientes.")