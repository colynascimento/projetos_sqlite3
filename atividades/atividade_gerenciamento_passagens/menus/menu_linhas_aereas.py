from prettytable import PrettyTable
from linhas_aereas.linha_aerea_dao import LinhaAereaDAO
from aeronaves.aeronave_dao import AeronaveDao
from aeronaves.aeronave import Aeronave
import os

def menu_linhas_aereas():

    # caminho do bd
    linha_aerea_dao = LinhaAereaDAO('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')
    aeronave_dao = AeronaveDao('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')

    while True:
        os.system('cls')
        print('Menu de Linhas Aéreas')

        linhas_aereas = linha_aerea_dao.listar_todas()

        if not linhas_aereas:
            print('Nenhuma linha aérea cadastrada.')

        else:
            tabela = PrettyTable()
            tabela.field_names = ['Código Linha Aérea', 'Nome', 'País de Origem', 'Contato Suporte', 'E-mail']

            for linha_aerea in linhas_aereas:
                tabela.add_row([linha_aerea.cod_linha_aerea, linha_aerea.nome, linha_aerea.pais_origem, linha_aerea.contato_suporte, linha_aerea.email])
                
            print(tabela)

        print('Opções')
        print('_' * 60)
        print('0 - Voltar ao Menu Principal')
        print('1 - Cadastrar Novas Aeronaves')
        print('2 - Visualizar Rotas Operadas')
        print('_' * 60)

        opcao = input('Digite a opção desejada: ')

        if opcao == '0':
            return
        elif opcao == '1':
            cadastrar_aeronaves(linha_aerea_dao, aeronave_dao)
        elif opcao == '2':
            visualizar_rotas()
        else:
            print('Opção inválida. Tente novamente.')
            input('Pressione qualquer tecla para continuar.')


def cadastrar_aeronaves(linha_aerea_dao, aeronave_dao):

    while True:
        print('_' * 60)
        cod_linha_aerea = input('Insira o código da linha aérea: ').upper()
        nome_linha_aerea = linha_aerea_dao.nomear_por_cod(cod_linha_aerea)

        print(f"Tipo de cod_linha_aerea: {type(cod_linha_aerea)}")
        print(f"Valor de cod_linha_aerea: {cod_linha_aerea}")

        if linha_aerea_dao.buscar_por_cod(cod_linha_aerea) is None:
            print('Linha Aérea não encontrada.')
            continue
        else:
            os.system('cls')

            print(f'Aeronaves de {nome_linha_aerea}:')
            aeronave_dao.filtrar_por_linha_aerea(cod_linha_aerea)
            print('_' * 60)
            print('Cadastrar nova aeronave:')
            cod_aeronave = int(input('Insira o código da aeronave(apenas números): ')) # criar validação aqui
            modelo = input('Insira o modelo: ')
            capacidade_passageiros = int(input('Insira a capacidade máxima de passageiros: '))
            ano = int(input('Insira o ano de fabricação: '))
            
            nova_aeronave = Aeronave(cod_aeronave, cod_linha_aerea, modelo, capacidade_passageiros, ano)
            aeronave_dao.cadastrar(nova_aeronave)

            print('Aeronave adicionada com sucesso!')
            input('Pressione Enter para voltar...')

def visualizar_rotas():
    pass