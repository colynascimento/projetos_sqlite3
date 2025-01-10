from prettytable import PrettyTable
from linhas_aereas.linha_aerea_dao import LinhaAereaDAO
from aeronaves.aeronave_dao import AeronaveDao
from aeronaves.aeronave import Aeronave
from rotas.rota_dao import RotaDao, Rota
import os

def menu_linhas_aereas():

    # caminho do bd
    linha_aerea_dao = LinhaAereaDAO('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')
    aeronave_dao = AeronaveDao('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')
    rotas_dao = RotaDao('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')

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
            visualizar_rotas(rotas_dao)
        else:
            print('Opção inválida. Tente novamente.')
            input('Pressione Enter para continuar.')


def cadastrar_aeronaves(linha_aerea_dao, aeronave_dao):

    while True:
        print('_' * 60)

        cod_linha_aerea = input('Insira o código da linha aérea: ').upper()
        nome_linha_aerea = linha_aerea_dao.nomear_por_cod(cod_linha_aerea)

        if linha_aerea_dao.buscar_por_cod(cod_linha_aerea) is None:
            print('Linha Aérea não encontrada.')
            continue
        else:
            os.system('cls')

            print(f'Aeronaves de {nome_linha_aerea}:')

            filtro_linha_aerea = aeronave_dao.filtrar_por_linha_aerea(cod_linha_aerea)
            tabela_filtrada = PrettyTable()
            tabela_filtrada.field_names = ['Código Aeronave', 'Modelo', 'Capacidade de Passageiros', 'Ano']
    
            for aeronave in filtro_linha_aerea:
                tabela_filtrada.add_row([aeronave.cod_aeronave, aeronave.modelo, aeronave.capacidade_passageiros, aeronave.ano])
    
            print(tabela_filtrada)

            print('Cadastrar nova aeronave:')
            print('_' * 60)
            cod_aeronave = int(input('Insira o código da aeronave(apenas números): ')) # criar validação aqui
            modelo = input('Insira o modelo: ')
            capacidade_passageiros = int(input('Insira a capacidade máxima de passageiros: '))
            ano = int(input('Insira o ano de fabricação: '))
            
            nova_aeronave = Aeronave(cod_aeronave, cod_linha_aerea, modelo, capacidade_passageiros, ano)
            aeronave_dao.cadastrar(nova_aeronave)

            print('Aeronave adicionada com sucesso!')
            input('Pressione Enter para voltar...')
            menu_linhas_aereas()

def visualizar_rotas(rotas_dao):

    while True:
        os.system('cls')
        print('Visualizar Rotas Operadas:')

        rotas = rotas_dao.visualizar()

        if not rotas:
            print('Nenhuma rota cadastrada.')

        else:
            tabela = PrettyTable()
            tabela.field_names = ['Código Rota', 'Código Linha Aérea', 'Linha Aérea','Cidade Origem', 'IATA Origem', 'Cidade Destino', 'IATA Destino', 'Preco Base']

            for rota in rotas:
                tabela.add_row(rota)
            print(tabela)

        print('Opções')
        print('_' * 60)
        print('0 - Voltar de Linhas Aéreas')
        print('1 - Cadastrar Novas Rotas')
        print('2 - Modificar Preço Base de Rota')
        print('3 - Excluir Rota')
        print('_' * 60)

        opcao = input('Insira a opção escolhida: ')

        if opcao == '0':
            return
        elif opcao == '1':
            cadastrar_rotas(rotas_dao)
        elif opcao == '2':
            modificar_preco_rota(rotas_dao)
        elif opcao == '3':
            deletar_rota(rotas_dao)
        else:
            print('Opção inválida. Tente novamente.')
            input('Pressione Enter para continuar.')
        
def cadastrar_rotas(rotas_dao):

    while True:
        print('_' * 60)
        print('Cadastrar nova rota')
        print()

        cod_linha_aerea = input('Insira o código da linha aérea: ') # criar validação aqui
        cod_iata_origem = input('Insira o código IATA do aeroporto de origem: ')
        cod_iata_destino = input('Insira o código IATA do aeroporto de destino: ')
        preco_base = float(input('Insira o preço base (Utilize o ponto como separador decimal): '))
        
        nova_rota = Rota(None, cod_linha_aerea, cod_iata_origem, cod_iata_destino, preco_base)
        rotas_dao.cadastrar(nova_rota)
        print('Rota adicionada com sucesso!')
        input('Pressione Enter para voltar...')
        menu_linhas_aereas()

def modificar_preco_rota(rotas_dao):

    while True:
        print('_' * 60)
        print('Modificar preço base da rota')
        print()

        cod_rota = int(input('Insira o código da rota que deseja modificar: ')) # criar validação aqui
        novo_preco_base = float(input('Insira o novo preço base (Utilize o ponto como separador decimal): '))
        
        rotas_dao.editar_preco_base(cod_rota, novo_preco_base)
        print('Valor base da rota modificado com sucesso!')
        input('Pressione Enter para voltar...')
        menu_linhas_aereas()

def deletar_rota(rotas_dao):

    while True:
        print('_' * 60)
        print('Excluir rota')
        print()

        cod_rota = int(input('Insira o código da rota que deseja excluir: ')) # criar validação aqui
        
        rotas_dao.deletar(cod_rota)
        print(f'Rota {cod_rota} deletada com sucesso!')
        input('Pressione Enter para voltar...')
        menu_linhas_aereas()