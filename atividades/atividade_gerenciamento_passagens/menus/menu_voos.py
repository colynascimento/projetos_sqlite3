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
        voos = voo_dao.listar_todos()

        print('_' * 60)
        cod_voo = int(input('Insira o código do vôo que deseja consultar: ')) # inserir validação aqui

        cod_voo = voo_dao.buscar_por_id(cod_voo)

        if not cod_voo:
            print('Nenhum vôo cadastrado.')

        else:
            detalhes = voo_dao.consultar(cod_voo)

            tabela_detalhada = PrettyTable()
            tabela_detalhada.field_names = ['Código Vôo', 'Linha Aérea', 'IATA Origem', 'IATA Destino', 'Partida', 'Chegada', 'Valor', 'Plataforma']

            for detalhe in detalhes:
                tabela_detalhada.add_row(detalhe)

        print(tabela_detalhada)
        input('Pressione Enter para voltar ao menu.')
        
        