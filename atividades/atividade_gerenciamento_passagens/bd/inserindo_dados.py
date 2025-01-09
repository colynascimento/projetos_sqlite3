import sqlite3
import os

conn = sqlite3.connect('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')

cursor = conn.cursor()

cursor.execute('''
    INSERT INTO clientes (nome, data_nascimento, nacionalidade, documento, telefone, email, deficiencia_legal_check, deficiencia_legal) 
    VALUES
        ('João Franco', '1990-01-15', 'Brasileiro', '12345678901', '11987654321', 'joao.silva@email.com', 'não', NULL),
        ('Maria Oliveira', '1985-07-22', 'Brasileira', '98765432100', '21999887766', 'maria.oliveira@email.com', 'sim', 'deficiência visual'),
        ('Carlos Santos', '1995-03-10', 'Brasileiro', '45678912302', '31987654321', 'carlos.santos@email.com', 'não', NULL);
''')

cursor.execute('''
    INSERT INTO destinos (cod_iata, cod_icao, nome_aeroporto, cidade, estado, pais, tipo_aeroporto) 
    VALUES
        ('GRU', 'SBGR', 'Aeroporto Internacional de Guarulhos', 'São Paulo', 'SP', 'Brasil', 'internacional'),
        ('SDU', 'SBRJ', 'Aeroporto Santos Dumont', 'Rio de Janeiro', 'RJ', 'Brasil', 'doméstico'),
        ('MIA', 'KMIA', 'Miami International Airport', 'Miami', 'FL', 'EUA', 'internacional');
''')

cursor.execute('''
    INSERT INTO linhas_aereas (cod_linha_aerea, nome, pais_origem, contato_suporte, email) 
    VALUES
        ('LT4', 'LATAM Airlines', 'Brasil', '+551199887766', 'suporte@latam.com'),
        ('AA1', 'American Airlines', 'EUA', '+18005551234', 'support@aa.com'),
        ('GL7', 'Gol Linhas Aéreas', 'Brasil', '+551134567890', 'contato@gol.com.br');
''')

cursor.execute('''
    INSERT INTO aeronaves (cod_aeronave, cod_linha_aerea, modelo, capacidade_passageiros, ano) 
    VALUES
        (1, 'GL7', 'Boeing 737', 189, 2005),
        (2, 'LT4', 'Airbus A320', 180, 2010),
        (3, 'AA1', 'Embraer E195', 132, 2008);
''')

cursor.execute('''
    INSERT INTO voos (cod_voo, cod_linha_aerea, cod_aeronave, cod_iata_origem, cod_iata_destino, data_hora_partida, data_hora_chegada, plataforma) 
    VALUES
        (1, 'LT4', 1, 'GRU', 'MIA', '2024-12-10 08:00', '2024-12-10 16:00', 5),
        (2, 'AA1', 2, 'SDU', 'GRU', '2024-12-11 15:30', '2024-12-11 17:00', 2),
        (3, 'GL7', 3, 'MIA', 'GRU', '2024-12-12 10:00', '2024-12-12 18:00', 7);
''')

cursor.execute('''
    INSERT INTO passagens (cod_voo, id_cliente, tipo_assento, poltrona, status_passagem, preco_final, data_hora_compra) 
    VALUES
        (1, 1, 'executivo', '1A', 'emitida', 1500.00, '2024-12-01 09:30'),
        (2, 2, 'comfort', '10B', 'reservada', 500.00, '2024-12-02 14:45'),
        (3, 3, 'primeira classe', '2C', 'emitida', 2500.00, '2024-12-03 11:20');
''')

cursor.execute('''
    INSERT INTO rotas (cod_linha_aerea, cod_iata_origem, cod_iata_destino, preco_base) 
    VALUES
        ('LT4', 'GRU', 'MIA', 1200.00),
        ('AA1', 'SDU', 'GRU', 400.00),
        ('GL7', 'MIA', 'GRU', 1300.00);
''')

cursor.execute('''
    INSERT INTO ajustes_preco (cod_rota, tipo_ajuste, valor_porcentual, descricao, data_inicio, data_fim) 
    VALUES
        (1, 'desconto', 10.00, 'Promoção de Natal', '2024-12-01', '2024-12-25'),
        (2, 'aumento', 15.00, 'Alta temporada', '2024-12-15', '2025-01-15'),
        (3, 'desconto', 5.00, 'Fidelidade', '2024-12-05', '2024-12-10');
''')

conn.commit()

conn.close()