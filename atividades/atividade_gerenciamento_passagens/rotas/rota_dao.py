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
        cursor.execute('''SELECT 
                rotas.cod_rota,
                rotas.cod_linha_aerea,
                linhas_aereas.nome,
                origem.cidade AS cidade_origem,
                rotas.cod_iata_origem,
                destino.cidade AS cidade_destino,
                rotas.cod_iata_destino,
                rotas.preco_base
            FROM rotas
            INNER JOIN linhas_aereas ON rotas.cod_linha_aerea = linhas_aereas.cod_linha_aerea
            INNER JOIN destinos origem ON rotas.cod_iata_origem = origem.cod_iata
            INNER JOIN destinos destino ON rotas.cod_iata_destino = destino.cod_iata           
        ''')
        tabela_rotas = cursor.fetchall()
        conn.close()
        return tabela_rotas
    
    def buscar_por_cod(self, cod_rota):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM rotas WHERE cod_rota = ?', (cod_rota,))
        resultado = cursor.fetchone()
        conn.close()
        return Rota(*resultado) if resultado else None
    
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
            INSERT INTO rotas (cod_linha_aerea, cod_iata_origem, cod_iata_destino, preco_base)
            VALUES (?, ?, ?, ?)               
        ''', (nova_rota.cod_linha_aerea, nova_rota.cod_iata_origem, nova_rota.cod_iata_destino, nova_rota.preco_base))
        nova_rota.cod_rota = cursor.lastrowid # recupera id gerado pelo banco para o cod_rota
        conn.commit()
        conn.close()

    def deletar(self, cod_rota):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM rotas WHERE cod_rota = ?', (cod_rota,))
        conn.commit()
        conn.close()

    def editar_preco_base(self, cod_rota, novo_preco):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE rotas
            SET preco_base = ?
            WHERE cod_rota = ?
        ''', (novo_preco, cod_rota))
        conn.commit()
        conn.close()

    def aplicar_desconto(self, cod_rota, ajuste_preco):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO ajuste_preco (cod_rota, tipo_ajuste, valor_porcentual, descricao, data_inicio, data_fim)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (cod_rota, 'desconto', ajuste_preco.valor_porcentual, ajuste_preco.descricao, ajuste_preco.data_inicio, ajuste_preco.data_fim))
        conn.commit()
        conn.close()

    def aplicar_aumento(self, cod_rota, ajuste_preco):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO ajuste_preco (cod_rota, tipo_ajuste, valor_porcentual, descricao, data_inicio, data_fim)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (cod_rota, 'aumento', ajuste_preco.valor_porcentual, ajuste_preco.descricao, ajuste_preco.data_inicio, ajuste_preco.data_fim))
        conn.commit()
        conn.close()