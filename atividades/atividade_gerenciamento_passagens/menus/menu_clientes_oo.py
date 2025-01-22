import os
from prettytable import PrettyTable

class MenuClientes:
    def __init__(self, dao):
        self.dao = dao
    
    def exibir_menu(self):
        os.system('cls')

        print('Menu de Clientes')
        print('_' * 60)

        clientes = self.dao.listar_todos()
        self.exibir_clientes(clientes)

        print('Opções')
        print('_' * 60)
        print('0 - Voltar ao Menu Principal')
        print('1 - Visualizar Histórico de Passagens')
        print('_' * 60)

        menu = input('Digite a opção desejada: ')
        if menu == '0':
            return
        elif menu == '1':
            self.visualizar_historico_passagens()
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione qualquer tecla para continuar.")

    def exibir_clientes(self, clientes):
        if not clientes:
            print('Nenhum cliente cadastrado.')

        else:
            tabela = PrettyTable(['ID', 'Nome', 'Data Nascimento', 'Nacionalidade', 'Documento', 'Telefone', 'Email', 'Deficiencia Legal?'])
            for cliente in clientes:
                tabela.add_row([cliente.id_cliente, cliente.nome, cliente.data_nascimento, cliente.nacionalidade, cliente.documento, cliente.telefone, cliente.email, cliente.deficiencia_legal])
            print(tabela)

    def visualizar_historico_passagens(self):
        print('_' * 60)
        id_cliente = input('Insira o id do cliente: ')
        cliente = self.dao.buscar_por_id(id_cliente)

        if cliente is None:
            print('Cliente não encontrado.')

        else:
            os.system('cls')
            print(f'Histórico de passagens de {cliente.nome}:')
            historico = self.dao.buscar_historico_passagens(id_cliente)

            if not historico:
                print('Nenhuma passagem comprada.')
            else:
                tabela = PrettyTable(['Codigo Passagem', 'Origem', 'Destino', 'Data/Hora Partida', 'Data/Hora Chegada', 'Preco', 'Linha Aérea'])

                for passagem in historico:
                    tabela.add_row(passagem)
                print(tabela)

        input("Pressione qualquer tecla para voltar ao menu de clientes.")