import sqlite3
from aeronaves.aeronave import Aeronave

class AeronaveDao:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def conectar(self):
        return sqlite3.connect(self.db_path)
    
    def listar_todas(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM aeronaves')
        aeronaves = cursor.fetchall()
        
        tabela_aeronaves = []
        
        for linha in aeronaves:
            aeronave = Aeronave(*linha)
            tabela_aeronaves.append(aeronave)
        return tabela_aeronaves
    
    def filtrar_por_linha_aerea(self, cod_linha_aerea):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM aeronaves WHERE cod_linha_aerea = ?', (cod_linha_aerea,))
        resultado = cursor.fetchall() # retorna uma tupla
        tabela_filtrada = [Aeronave(*linha) for linha in resultado] # cria uma lista de objetos
        conn.close()
        return tabela_filtrada
    
    def buscar_por_id(self, cod_aeronave):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM aeronaves WHERE cod_aeronave = ?', (cod_aeronave,))
        resultado = cursor.fetchone()
        conn.close()
        return Aeronave(*resultado) if resultado else None
    
    def cadastrar(self, nova_aeronave):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO aeronaves (cod_aeronave, cod_linha_aerea, modelo, capacidade_passageiros, ano)
            VALUES (?, ?, ?, ?, ?)
        ''', (nova_aeronave.cod_aeronave, nova_aeronave.cod_linha_aerea, nova_aeronave.modelo, nova_aeronave.capacidade_passageiros, nova_aeronave.ano))
        conn.commit()
        conn.close()

    def deletar(self, cod_aeronave):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM aeronaves WHERE cod_aeronave = ?', (cod_aeronave,))
        conn.commit()
        conn.close()

    def editar(self, cod_aeronave, aeronave_atualizada):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE aeronaves 
            SET cod_aeronave = ?, modelo = ?, capacidade_passageiros = ?, ano = ?)
            WHERE cod_aeronave = ?
        ''', (aeronave_atualizada.cod_aeronave, aeronave_atualizada.modelo, aeronave_atualizada.capacidade_passageiros, aeronave_atualizada.ano, cod_aeronave))
        conn.commit()
        conn.close()