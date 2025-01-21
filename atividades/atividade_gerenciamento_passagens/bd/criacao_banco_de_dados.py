import sqlite3

conn = sqlite3.connect('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')

cursor = conn.cursor()

cursor.execute('''       
    CREATE TABLE IF NOT EXISTS clientes(
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nascimento DATE NOT NULL,
                nacionalidade TEXT NOT NULL,
                documento TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL,
                deficiencia_legal_check TEXT CHECK(deficiencia_legal_check IN ('sim', 'não')) NOT NULL,
                deficiencia_legal TEXT
                );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS destinos(
                cod_iata CHAR(3) PRIMARY KEY,
                cod_icao CHAR(4) NOT NULL,
                nome_aeroporto TEXT NOT NULL,
                cidade TEXT NOT NULL,
                estado TEXT NOT NULL,
                pais TEXT NOT NULL,
                tipo_aeroporto TEXT CHECK(tipo_aeroporto IN ('internacional', 'doméstico', 'regional', 'carga'))     
                );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS linhas_aereas(
               cod_linha_aerea TEXT PRIMARY KEY,
               nome TEXT NOT NULL,
               pais_origem TEXT NOT NULL,
               contato_suporte TEXT NOT NULL,
               email TEXT NOT NULL
               );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rotas(
               cod_rota INTEGER PRIMARY KEY AUTOINCREMENT,
               cod_linha_aerea TEXT NOT NULL,
               cod_iata_origem CHAR(3) NOT NULL,
               cod_iata_destino CHAR(3) NOT NULL,
               preco_base REAL NOT NULL,
               FOREIGN KEY(cod_linha_aerea) REFERENCES linhas_aereas(cod_linha_aerea),
               FOREIGN KEY(cod_iata_origem) REFERENCES destinos(cod_iata),
               FOREIGN KEY(cod_iata_destino) REFERENCES destinos(cod_iata)
               );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS aeronaves(
                cod_aeronave INTEGER PRIMARY KEY,
                cod_linha_aerea INTEGER NOT NULL,
                modelo TEXT NOT NULL,
                capacidade_passageiros INTEGER NOT NULL,
                ano INT NOT NULL,
                FOREIGN KEY(cod_linha_aerea) REFERENCES linhas_aereas(cod_linha_aerea) 
                );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS voos(
               cod_voo INTEGER PRIMARY KEY,
               cod_rota INTEGER NOT NULL,
               cod_linha_aerea INTEGER NOT NULL,
               cod_aeronave INTEGER NOT NULL,
               cod_iata_origem CHAR(3) NOT NULL,
               cod_iata_destino CHAR(3) NOT NULL,
               data_hora_partida TEXT NOT NULL,
               data_hora_chegada TEXT NOT NULL,
               plataforma INT NOT NULL,
               FOREIGN KEY (cod_rota) REFERENCES rotas(cod_rota),
               FOREIGN KEY(cod_linha_aerea) REFERENCES linhas_aereas(cod_linha_aerea),
               FOREIGN KEY(cod_aeronave) REFERENCES aeronaves(cod_aeronave),
               FOREIGN KEY(cod_iata_origem) REFERENCES destinos(cod_iata),
               FOREIGN KEY(cod_iata_destino) REFERENCES destinos(cod_iata)
               );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS passagens(
               cod_passagem INTEGER PRIMARY KEY AUTOINCREMENT,
               cod_voo INTEGER NOT NULL,
               id_cliente INTEGER NOT NULL,
               tipo_assento TEXT CHECK(tipo_assento IN ('executivo', 'comfort', 'primeira classe')) NOT NULL,
               poltrona TEXT NOT NULL,
               status_passagem TEXT CHECK(status_passagem IN ('emitida', 'reservada', 'cancelada')),
               preco_final REAL NOT NULL,
               data_hora_compra TEXT NOT NULL,
               FOREIGN KEY(cod_voo) REFERENCES voos(cod_voo),
               FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
               );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ajustes_preco(
               cod_ajuste INTEGER PRIMARY KEY AUTOINCREMENT,
               cod_voo INTEGER NOT NULL,
               tipo_ajuste TEXT CHECK(tipo_ajuste IN ('desconto', 'aumento')),
               valor_porcentual REAL NOT NULL,
               descricao TEXT NOT NULL,
               data_inicio DATE NOT NULL,
               data_fim DATE NOT NULL,
               FOREIGN KEY(cod_voo) REFERENCES voo(cod_voo)
               );
''')

conn.commit()

conn.close()