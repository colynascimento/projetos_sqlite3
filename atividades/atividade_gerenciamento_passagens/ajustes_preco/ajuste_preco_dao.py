import sqlite3
from ajustes_preco.ajuste_preco import AjustePreco

class AjusteDao:
    def __init__(self, db_path):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)
    
    def listar_todos(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''SELECT
            ajustes_preco.cod_ajuste, 
            ajustes_preco.cod_voo,
            rotas.preco_base AS preco_base,
            linhas_aereas.nome,
            ajustes_preco.tipo_ajuste,
            ajustes_preco.valor_porcentual,
            ajustes_preco.descricao,
            ajustes_preco.data_inicio,
            ajustes_preco.data_fim
            FROM ajustes_preco
            INNER JOIN voos ON ajustes_preco.cod_voo = voos.cod_voo
            INNER JOIN linhas_aereas ON voos.cod_linha_aerea = linhas_aereas.cod_linha_aerea
            INNER JOIN rotas ON voos.cod_rota = rotas.cod_rota
        ''')
        tabela_ajustes_preco = cursor.fetchall()
        conn.close()
        return tabela_ajustes_preco
    
    def cadastrar(self, novo_ajuste):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute(''' 
        INSERT INTO ajustes_preco (cod_voo, tipo_ajuste, valor_porcentual, descricao, data_inicio, data_fim)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (novo_ajuste.cod_voo, novo_ajuste.tipo_ajuste, novo_ajuste.valor_porcentual, novo_ajuste.descricao, novo_ajuste.data_inicio, novo_ajuste.data_fim))
        novo_ajuste.cod_rota = cursor.lastrowid # recupera id gerado pelo banco para o cod_ajuste
        conn.commit()
        conn.close()

    def editar(self, cod_ajuste, novo_tipo, novo_valor, nova_descricao, nova_data_inicio, nova_data_fim):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE ajustes_preco
            SET tipo_ajuste = ?,
                valor_porcentual = ?,
                descricao = ?,
                data_inicio = ?,
                data_fim = ?
            WHERE cod_ajuste = ?
        ''', (novo_tipo, novo_valor, nova_descricao, nova_data_inicio, nova_data_fim, cod_ajuste))
        conn.commit()
        conn.close()

    def deletar(self, cod_ajuste):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM ajustes_preco WHERE cod_ajuste = ?', (cod_ajuste,))
        conn.commit()
        conn.close()