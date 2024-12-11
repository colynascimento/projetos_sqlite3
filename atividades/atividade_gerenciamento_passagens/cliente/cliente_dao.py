import sqlite3
from cliente import Cliente

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