import sqlite3
from voo import Voo

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
            voos.cod_iata_origem,
            origem.cidade AS cidade_origem,
            voos.cod_iata_destino,
            destino.cidade AS cidade_destino,
            voos.data_hora_partida,
            voos.data_hora_chegada
        FROM voos
        INNER JOIN linhas_aereas ON voos.cod_linha_aerea = linhas_aereas.cod_linha_aerea
        INNER JOIN destinos origem ON rotas.cod_iata_origem = origem.cod_iata
        INNER JOIN destinos destino ON rotas.cod_iata_destino = destino.cod_iata
        ''')
        tabela_voos = cursor.fetchall()
        conn.close()
        return tabela_voos
    
    def buscar_por_id(self, cod_voo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM voos WHERE cod_voo = ?', (cod_voo))
        resultado = cursor.fetchone()
        conn.close()
        return Voo(*resultado) if resultado else None