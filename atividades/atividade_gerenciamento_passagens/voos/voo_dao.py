import sqlite3
from voos.voo import Voo

class VooDAO:
    def __init__(self, db_path):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)
    
    def listar_todos(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''SELECT
            voos.cod_voo,
            voos.cod_linha_aerea,
            linhas_aereas.nome,
            origem.cidade AS cidade_origem,
            destino.cidade AS cidade_destino,
            voos.data_hora_partida,
            voos.data_hora_chegada
        FROM voos
        INNER JOIN rotas ON voos.cod_rota = rotas.cod_rota
        INNER JOIN linhas_aereas ON voos.cod_linha_aerea = linhas_aereas.cod_linha_aerea
        INNER JOIN destinos origem ON voos.cod_iata_origem = origem.cod_iata
        INNER JOIN destinos destino ON voos.cod_iata_destino = destino.cod_iata
        ''')
        tabela_voos = cursor.fetchall()
        conn.close()
        return tabela_voos
    
    def buscar_por_id(self, cod_voo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM voos WHERE cod_voo = ?', (cod_voo,))
        resultado = cursor.fetchone()
        conn.close()
        return Voo(*resultado) if resultado else None
    
    def consultar(self, cod_voo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT
                voos.cod_aeronave,
                linhas_aereas.nome AS nome_linha_aerea,
                voos.cod_iata_origem,
                voos.cod_iata_destino,
                voos.data_hora_partida,
                voos.data_hora_chegada,
                (rotas.preco_base * (1 - COALESCE(ajustes_preco.valor_porcentual, 0) / 100)) AS preco_atual,
                voos.plataforma
            FROM voos
            INNER JOIN linhas_aereas ON voos.cod_linha_aerea = linhas_aereas.cod_linha_aerea
            INNER JOIN rotas ON voos.cod_rota = rotas.cod_rota
            LEFT JOIN ajustes_preco ON voos.cod_voo = ajustes_preco.cod_voo
                AND (ajustes_preco.data_inicio IS NULL OR CURRENT_DATE >= ajustes_preco.data_inicio)
                AND (ajustes_preco.data_fim IS NULL OR CURRENT_DATE <= ajustes_preco.data_fim)
            WHERE voos.cod_voo = ?
        ''',    (cod_voo,)) # COALESCE substitui o valor do desconto por 0 caso ele seja nulo, garantindo a integridade do valor mesmo sem ajuste de preço
        consulta = cursor.fetchall()
        conn.close()
        return consulta
        
        # modificar na criação do bd na tabela ajuste_preco para cod_rota tornar-se cod_voo