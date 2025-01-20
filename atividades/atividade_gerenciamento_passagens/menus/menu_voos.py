from prettytable import PrettyTable
from voos.voo_dao import Voo, VooDAO
from linhas_aereas.linha_aerea_dao import LinhaAereaDAO
from rotas.rota_dao import RotaDao
from ajustes_preco.ajuste_preco_dao import AjusteDao, AjustePreco
import os

def menu_voos():

    # caminho do bd
    voo_dao = VooDAO('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')
    linha_aerea_dao = LinhaAereaDAO('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')
    rota_dao = RotaDao('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')
    ajustes_preco_dao = AjusteDao('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')

    while True:
        os.system('cls')
        print('Menu de Vôos')

        voos = voo_dao.listar_todos()

        if not voo_dao:
            print('Nenhum vôo cadastrado.')

        else:
            tabela = PrettyTable(['Código Vôo', 'Código Linha Aérea', 'Linha Aérea', 'Cidade Origem', 'Cidade Destino', 'Partida', 'Chegada'])

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
            cadastrar(voo_dao, linha_aerea_dao, rota_dao)
        elif opcao == '3':
            modificar(voo_dao)
        elif opcao == '4':
            deletar(voo_dao)
        elif opcao == '5':
            exibir_ajustes_preco(voo_dao, ajustes_preco_dao)
        else:
            print('Opção inválida. Tente novamente.')
            input('Pressione Enter para continuar.')

def exibir_detalhes(voo_dao):
    
    while True:

        print('_' * 60)
        voo_detalhado = int(input('Insira o código do vôo que deseja consultar: ')) # inserir validação aqui

        voo_detalhado = voo_dao.buscar_por_cod(voo_detalhado)

        if not voo_detalhado:
            print('Código inválido.')
            print('Pressione Enter para retornar.')

        else:
            detalhes = voo_dao.consultar(voo_detalhado.cod_voo)

            tabela_detalhada = PrettyTable(['Código Vôo', 'Linha Aérea', 'IATA Origem', 'IATA Destino', 'Partida', 'Chegada', 'Valor', 'Plataforma'])

            for detalhe in detalhes:
                tabela_detalhada.add_row(detalhe)

        print(tabela_detalhada)
        input('Pressione Enter para voltar ao menu.')
        
        menu_voos()

def cadastrar(voo_dao, linha_aerea_dao, rota_dao):
    while True:
        print('_' * 60)

        cod_linha_aerea = input('Insira o código da linha aérea: ').upper()
        nome_linha_aerea = linha_aerea_dao.nomear_por_cod(cod_linha_aerea)

        if linha_aerea_dao.buscar_por_cod(cod_linha_aerea) is None:
            print('Linha Aérea não encontrada.')
            continue
        else:
            os.system('cls')

            print(f'Voos de {nome_linha_aerea}:')

            detalhes = voo_dao.consultar_por_linha_aerea(cod_linha_aerea)

            tabela_detalhada = PrettyTable(['Código Vôo', 'Linha Aérea', 'IATA Origem', 'IATA Destino', 'Partida', 'Chegada', 'Valor', 'Plataforma'])
            
            for detalhe in detalhes:
                tabela_detalhada.add_row(detalhe)

            print(tabela_detalhada)

            print(f'Cadastrar novo vôo de {nome_linha_aerea}:')
            print('_' * 60)
            cod_rota = int(input('Insira o código de uma rota já existente na companhia: '))
            cod_aeronave = int(input('Insira o código de uma aeronave da companhia: '))
            data_hora_partida = input('Insira a data e hora de partida no formato (AAAA-MM-DD HH:MM): ')
            data_hora_chegada = input('Insira a data e hora de chegada no formato (AAAA-MM-DD HH:MM): ')
            plataforma = int(input('Insira a plataforma de embarque(apenas números): '))
            
            rota = rota_dao.buscar_por_cod(cod_rota)
            if rota is None:
                print('Código de rota não encontrado. Tente novamente.')
                continue

            cod_iata_origem = rota.cod_iata_origem
            cod_iata_destino = rota.cod_iata_destino

            novo_voo = Voo(None, cod_rota, cod_aeronave, cod_linha_aerea, cod_iata_origem, cod_iata_destino, data_hora_partida, data_hora_chegada, plataforma)
            voo_dao.cadastrar(novo_voo)

            print('Voo adicionado com sucesso!')
            input('Pressione Enter para voltar...')
            menu_voos()

def modificar(voo_dao):
    
    while True:
        print('_' * 60)
        print('Editar:')
        print()

        cod_voo = int(input('Insira o código do voo que deseja modificar: ')) # criar validação aqui
        
        voo = voo_dao.buscar_por_cod(cod_voo)

        if voo is None:
            print('Código de vôo não encontrado. Tente novamente.')
            continue

        print('Qual informação deseja editar?')
        print('_' * 60)
        print('0 - Voltar ao Menu de Vôos')
        print('1 - Código da Aeronave') # aeronave, plataforma, valor atual, passagens disponíveis
        print('2 - Data/hora partida')
        print('3 - Data/hora chegada')
        print('4 - Plataforma')
        print('')
        print('Algumas informações não podem ser editadas.')
        print('Se não encontrou a opção desejada, volte ao menor anterior e exclua o vôo e crie um novo.')

        print('_' * 60)

        escolha = input('Digite o campo escolhido: ')
        novo_valor = input('Insira o novo valor atualizado: ')

        if escolha == '0':
            return
        elif escolha == '1':
            escolha = 'cod_aeronave'
            novo_valor = int(novo_valor)
        elif escolha == '2':
            escolha = 'data_hora_partida'
        elif escolha == '3':
            escolha = 'data_hora_chegada'
        elif escolha == '4':
            escolha = 'plataforma'
            novo_valor = int(novo_valor)
        else:
            print('Opção inválida. Tente novamente.')
            input('Pressione Enter para continuar.')
            continue


        voo_dao.editar(cod_voo, escolha, novo_valor)
        print('Valor base da rota modificado com sucesso!')
        input('Pressione Enter para voltar...')
        menu_voos()

def deletar(voo_dao):
    while True:
            print('_' * 60)
            print('Excluir rota')
            print()

            cod_voo = int(input('Insira o código do voo que deseja excluir: ')) # criar validação aqui

            voo_dao.deletar(cod_voo)
            print(f'Rota {cod_voo} deletado com sucesso!')
            input('Pressione Enter para voltar...')
            menu_voos()

def exibir_ajustes_preco(ajustes_preco_dao):
     while True:
        print('_' * 60)
        print('Ajustes nos Preços das Passagens')
        print()

        ajustes = ajustes_preco_dao.listar_todos()

        if not ajustes_preco_dao:
            print('Nenhum ajuste de preço ativo no momento.')

        else:
            tabela = PrettyTable(['Código Ajuste', 'Código Vôo', 'Preço Base', 'Linha Aérea', 'Tipo de Ajuste', 'Valor Porcentual', 'Descricao', 'Data Início', 'Data Fim'])

            for ajuste in ajustes:
                tabela.add_row(ajuste)
                
            print(tabela)

            print()
            print('Opções')
            print('_' * 60)
            print('0 - Voltar ao Menu de Vôos')
            print('1 - Adicionar Novo Ajuste')
            print('2 - Editar Ajuste Existente')
            print('3 - Desativar Ajuste')
            print('_' * 60)

            escolha = input('Digite a opção desejada: ')

            if escolha == '0':
                pass
            elif escolha == '1':
                cadastrar_ajuste_preco(ajustes_preco_dao)
            elif escolha == '2':
                editar_ajuste_preco(ajustes_preco_dao)
            elif escolha == '3':
                desativar_ajustes_preco(ajustes_preco_dao)
            else:
                print('Opção inválida. Tente novamente.')
                input('Pressione Enter para continuar.')
                continue

            menu_voos()

def cadastrar_ajuste_preco(ajustes_preco_dao):
    while True:
        print('_' * 60)
        print('Cadastrar Novo Ajuste de Preço')
        print()

        cod_voo = input('Insira o código do vôo: ') # criar validação aqui
        tipo_ajuste = input('Insira o tipo de ajuste (aumento/desconto): ')
        valor_porcentual = float(input('Insira o valor em porcentagem de alteração do preco: '))
        descricao = input('Insira uma breve descrição do ajuste: ')
        data_inicio = input('Insira a data de ínicio do ajuste: ')
        data_fim = input('Insira a data de término do ajuste: ')
        
        novo_ajuste = AjustePreco(None, cod_voo, tipo_ajuste, valor_porcentual, descricao, data_inicio, data_fim)
        ajustes_preco_dao.cadastrar(novo_ajuste)
        print('Ajuste de preço ativado com sucesso!')
        input('Pressione Enter para voltar...')
        menu_voos()

def editar_ajuste_preco(ajustes_preco_dao):
    while True:
        print('_' * 60)
        print('Modificar Ajuste de Preço:')
        print()

        cod_ajuste = int(input('Insira o código do vôo que deseja modificar: ')) # criar validação aqui

        novo_tipo = input('Insira o tipo de ajuste (aumento/desconto): ')
        novo_valor = float(input('Insira o novo valor em porcentagem da alteração do preco: '))
        nova_descricao = input('Insira a descrição do ajuste: ')
        nova_data_inicio = input('Insira a data de ínicio do ajuste: ')
        nova_data_fim = input('Insira a data de término do ajuste: ')


        ajustes_preco_dao.editar(cod_ajuste, novo_tipo, novo_valor, nova_descricao, nova_data_inicio, nova_data_fim)
        print('Ajuste de preço atualizado com sucesso!')
        input('Pressione Enter para voltar...')
        menu_voos()

def desativar_ajustes_preco(ajustes_preco_dao):
    while True:
        print('_' * 60)
        print('Desativar Ajuste de Preço:')
        print()

        cod_ajuste = int(input('Insira o código da rota que deseja excluir: ')) # criar validação aqui
        
        ajustes_preco_dao.deletar(cod_ajuste)
        print(f'Rota {cod_ajuste} deletada com sucesso!')
        input('Pressione Enter para voltar...')
        menu_voos()
