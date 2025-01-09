import sqlite3
from rotas.rota import Rota

class RotaDao:
    def __init__(self, db_path):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)
    
    def visualizar(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM rotas')
        rotas = cursor.fetchall()

        tabela_rotas = []

        for linha in rotas:
            rota = Rota(*linha)
            tabela_rotas.append(rota)
        return tabela_rotas
    
    def filtrar_por_linha_aerea(self, cod_linha_aerea):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM rotas WHERE cod_linha_aerea = ?', (cod_linha_aerea,))
        rotas_filtradas = cursor.fetchall()

        tabela_filtrada = []

        for linha in rotas_filtradas:
            rota = Rota(*linha)
            tabela_filtrada.append(rota)
        return tabela_filtrada
    
    def cadastrar(self, nova_rota):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO rotas (cod_rota, cod_linha_aerea, cod_iata_origem, cod_iata_destino, preco_base)
            VALUES (?, ?, ?, ?, ?)               
        ''', (nova_rota.cod_rota, nova_rota.cod_linha_aerea, nova_rota.cod_iata_origem, nova_rota.cod_iata_destino, nova_rota.preco_base))
        conn.comit()
        conn.close()

    def deletar(self, cod_rota):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM rotas WHERE cod_rota = ?', (cod_rota,))
        conn.commit()
        conn.close()
