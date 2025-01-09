import sqlite3
from linha_aereas import Aeronave

class AeronaveDao:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def conectar(self):
        return sqlite3.connect(self.db_path)
    
    def listar_todas(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM aeronaves')
        tabela_aeronaves = cursor.fetchall()
        
        aeronaves = []
        
        for linha in tabela_aeronaves:
            aeronave = Aeronave(*linha)
            aeronaves.append(aeronave)
        return aeronaves
    
    def filtrar_por_linha_aerea(self, cod_linha_aerea):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM aeronaves WHERE cod_linha_aerea = ?', (cod_linha_aerea,))
        tabela_filtrada = cursor.fetchall()
        conn.close()
        return tabela_filtrada
    
    def buscar_por_id(self, cod_aeronave):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM aeronaves WHERE cod_aeronave = ?', (cod_aeronave,))
        resultado = cursor.fetchone()
        conn.close()
        return Aeronave(*resultado) if resultado else None
    
