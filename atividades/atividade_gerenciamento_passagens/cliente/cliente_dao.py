import sqlite3
from cliente.cliente import Cliente

class ClienteDao:
    def __init__(self, db_path):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)
    
    def listar_todos(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        tabela_clientes = cursor.fetchall()

        clientes = []

        for linha in tabela_clientes:
            cliente = Cliente(*linha) # Desempacotar a linha e criar um objeto Cliente
            clientes.append(cliente)
        return clientes

    def buscar_por_id(self, id_cliente):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id_cliente = ?', (id_cliente,))
        resultado = cursor.fetchone()
        conn.close()
        return Cliente(*resultado) if resultado else None
    
    def buscar_historico_passagens(self, id_cliente):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                passagens.cod_passagem,
                origem.cidade AS cidade_origem, 
                destino.cidade AS cidade_destino,
                voos.data_hora_partida, 
                voos.data_hora_chegada, 
                passagens.preco_final, 
                linhas_aereas.nome
            FROM passagens 
            INNER JOIN voos ON passagens.cod_voo = voos.cod_voo
            INNER JOIN destinos origem ON voos.cod_iata_origem = origem.cod_iata
            INNER JOIN destinos destino ON voos.cod_iata_destino = destino.cod_iata
            INNER JOIN linhas_aereas ON voos.cod_linha_aerea = linhas_aereas.cod_linha_aerea 
            WHERE passagens.id_cliente = ?
        ''', (id_cliente,))
        
        historico = cursor.fetchall()
        conn.close()
        return historico