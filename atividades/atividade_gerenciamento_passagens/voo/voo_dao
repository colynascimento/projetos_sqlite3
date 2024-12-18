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
        cursor.execute('SELECT * FROM voos')
        tabela_voos = cursor.fetchall()

        voos = []

        for linha in tabela_voos:
            voo = Voo(*linha)
            voos.append(voo)
        return voos
    
    def buscar_por_id(self, cod_voo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM voos WHERE cod_voo = ?', (cod_voo))
        resultado = cursor.fetchone()
        conn.close()
        return Voo(*resultado) if resultado else None