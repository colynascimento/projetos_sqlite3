from prettytable import PrettyTable
from voos.voo_dao import Voo, VooDAO
import os

def menu_voos():

    # caminho do bd
    voo_dao = VooDAO('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')

    while True:
        os.system('cls')
        print('Menu de Vôos')

        voos = voo_dao.listar_todos()

        if not voo_dao:
            print('Nenhum vôo cadastrado.')

        else:
            tabela = PrettyTable()
            tabela.field_names = ['Código Vôo', 'Código Linha Aérea', 'Linha Aérea', 'Cidade Origem', 'Cidade Destino', 'Partida', 'Chegada']

            for voo in voos:
                tabela.add_row(voo)
                
            print(tabela)

        print('Opções')
        print('_' * 60)
        print('0 - Voltar ao Menu Principal')
        print('1 - Consulta detalhada') # aeronave, plataforma, valor atual, passagens disponíveis
        print('2 - Cadastrar Novo Vôo')
        print('3 - Editar Vôo Existente')
        print('4 - Excluir Vôo')
        print('5 - Ajustes no Preço (Promoções/Aumentos)')
        print('_' * 60)

        opcao = input('Digite a opção desejada: ')

        if opcao == '0':
            return
        elif opcao == '1':
            exibir_detalhes(voo_dao)
        elif opcao == '2':
            # visualizar_rotas(rotas_dao)
            pass
        else:
            print('Opção inválida. Tente novamente.')
            input('Pressione Enter para continuar.')

def exibir_detalhes(voo_dao):
    
    while True:
        print('_' * 60)
        cod_voo = input('Insira o código do vôo que deseja consultar: ') # inserir validação aqui
        
        
        