import sqlite3
from ajustes_preco.ajuste_preco import AjustePreco

class AjusteDao:
    def __init__(self, db_path):
        db_path = self.db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)
    
    # def listar_todos(self):
    #     conn = self.conectar()
    #     cursor = conn.cursor()
    #     cursor.execute('''SELECT
    #         ajustes_preco.cod_ajuste, 
    #         ajustes_preco.cod_rota,
    #         rotas.cod_iata_origem,
    #         rotas.cod_iata_destino,
    #         linhas_aereas.cod_linha_aerea,
    #         ajustes_preco.tipo_ajuste,
    #         ajustes_preco.
    #         INNER JOIN rotas WHERE ajustes_preco.cod_rota = rotas.cod_rota
    #         INNER JOIN linhas_aereas WHERE rotas.cod_linha_aerea = linhas_aereas.cod_linha_aerea
    #     ''')