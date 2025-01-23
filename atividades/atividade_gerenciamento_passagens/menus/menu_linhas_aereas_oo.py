import os
from prettytable import PrettyTable

class MenuLinhasAereas:
    def __init__(self, linha_aerea_dao, aeronave_dao, aeronave, rota_dao):
        self.linha_aerea_dao = linha_aerea_dao
        self.aeronave_dao = aeronave_dao
        self.aeronave = aeronave
        self.rota_dao = rota_dao

    def exibir_menu(self):

        while True:
            os.system('cls')
            print('Menu de Linhas Aéreas')

            linhas_aereas = self.linha_aerea_dao.listar_todas()
            self.exibir_linhas_aereas(linhas_aereas)

            print('Opções')
            print('_' * 60)
            print('0 - Voltar ao Menu Principal')
            print('1 - Cadastrar Novas Aeronaves')
            print('2 - Visualizar Rotas Operadas')
            print('_' * 60)

            menu = input('Digite a opção desejada: ')

            if menu == '0':
                break
            elif menu == '1':
                self.cadastrar_aeronaves()
            elif menu == '2':
                self.rotas()
            else:
                print('Opção inválida. Tente novamente.')
                input('Pressione Enter para continuar.')

    def exibir_linhas_aereas(self, linhas_aereas):
        if not linhas_aereas:
            print('Nenhuma linha aérea cadastrada.')
        else:
            tabela = PrettyTable(['Código Linha Aérea', 'Nome', 'País de Origem', 'Contato Suporte', 'E-mail'])
            for linha_aerea in linhas_aereas:
                tabela.add_row([linha_aerea.cod_linha_aerea, linha_aerea.nome, linha_aerea.pais_origem, linha_aerea.contato_suporte, linha_aerea.email])
            print(tabela)

    def exibir_aeronaves_por_linha_aerea(self, cod_linha_aerea):
        if not self.linha_aerea_dao.buscar_por_cod(cod_linha_aerea):
            print('Linha Aérea não encontrada.')
            input("Pressione qualquer tecla para tentar novamente.")
            return False
        
        nome_linha_aerea = self.linha_aerea_dao.nomear_por_cod(cod_linha_aerea)
        filtro_linha_aerea = self.aeronave_dao.filtrar_por_linha_aerea(cod_linha_aerea)
        print(f'Aeronaves de {nome_linha_aerea}:')

        if not filtro_linha_aerea:
            print('Nenhuma aeronave encontrada para esta linha aérea.')
        else:
            tabela_filtrada = PrettyTable(['Código Aeronave', 'Modelo', 'Capacidade de Passageiros', 'Ano'])
            for aeronave in filtro_linha_aerea:
                tabela_filtrada.add_row([aeronave.cod_aeronave, aeronave.modelo, aeronave.capacidade_passageiros, aeronave.ano])
            print(tabela_filtrada)
        return True
    
    def cadastrar_aeronaves(self):

        while True:
            print('_' * 60)

            cod_linha_aerea = input('Insira o código da linha aérea: ').upper()
            sucesso = self.exibir_aeronaves_por_linha_aerea(cod_linha_aerea)

            if not sucesso:
                continue

            print('Cadastrar nova aeronave:')
            print('_' * 60)

            cod_aeronave = int(input('Insira o código da aeronave(apenas números): ')) # criar validação aqui
            modelo = input('Insira o modelo: ')
            capacidade_passageiros = int(input('Insira a capacidade máxima de passageiros: '))
            ano = int(input('Insira o ano de fabricação: '))

            nova_aeronave = self.aeronave(cod_aeronave, cod_linha_aerea, modelo, capacidade_passageiros, ano)
            self.aeronave_dao.cadastrar(nova_aeronave)
            print('Aeronave adicionada com sucesso!')
            input('Pressione Enter para voltar...')


    def rotas(self):
        pass