import sqlite3
from ajustes_preco.ajuste_preco import AjustePreco

class AjusteDao:
    def __init__(self, db_path):
        db_path = self.db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)
    
    def listar_todos(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''SELECT
            ajustes_preco.cod_ajuste, 
            ajustes_preco.cod_voo,
            linhas_aereas.nome_linha_aerea,
            ajustes_preco.tipo_ajuste,
            ajustes_preco.valor_porcentual,
            ajustes_preco.descricao,
            ajustes_preco.data_inicio,
            ajustes_preco.data_fim,
            INNER JOIN voos WHERE ajustes_preco.cod_voos = voos.cod_voo
            INNER JOIN linhas_aereas WHERE voos.cod_linha_aerea = linhas_aereas.cod_linha_aerea
        ''')