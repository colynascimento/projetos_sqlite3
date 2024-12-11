import sqlite3
from linha_aerea import LinhaAerea

class LinhaAereaDAO:
    def __init__(self, db_path):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)
    
    def listar_todas(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM linhas_aereas')
        tabela_linhas_aereas = cursor.fetchall()

        linhas_aereas = []

        for linha in tabela_linhas_aereas:
            linha_aerea = LinhaAerea(*linha)
            linhas_aereas.append(linha_aerea)
        return linhas_aereas
    
    def buscar_por_id(self, cod_linha_aerea):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM linhas_aereas WHERE cod_linha_aerea = ?', (cod_linha_aerea))
        resultado = cursor.fetchone()
        conn.close()
        return LinhaAerea(*resultado) if resultado else None