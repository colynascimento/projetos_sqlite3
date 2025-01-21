import sqlite3
import os

conn = sqlite3.connect('../projetos_sqlite3/BD/bd_sistema_gerenciamento_passagens.db')

cursor = conn.cursor()

cursor.execute('''
    INSERT INTO clientes (nome, data_nascimento, nacionalidade, documento, telefone, email, deficiencia_legal_check, deficiencia_legal) 
    VALUES
        ('João Franco', '1990-01-15', 'Brasileiro', '12345678901', '11987654321', 'joao.silva@email.com', 'não', NULL),
        ('Maria Oliveira', '1985-07-22', 'Brasileira', '98765432100', '21999887766', 'maria.oliveira@email.com', 'sim', 'deficiência visual'),
        ('Carlos Santos', '1995-03-10', 'Brasileiro', '45678912302', '31987654321', 'carlos.santos@email.com', 'não', NULL),
        ('Ana Beatriz Lima', '1992-04-18', 'Brasileira', '12309845671', '21999876543', 'ana.lima@email.com', 'não', NULL),
        ('Pedro Henrique Costa', '1988-11-25', 'Brasileiro', '32165498700', '31987654300', 'pedro.costa@email.com', 'sim', 'deficiência auditiva'),
        ('Julia Carvalho Mendes', '1997-08-10', 'Brasileira', '78965412308', '11998877665', 'julia.mendes@email.com', 'não', NULL),
        ('Lucas Almeida Rocha', '2000-06-15', 'Brasileiro', '45678932112', '31976543210', 'lucas.rocha@email.com', 'não', NULL),
        ('Sophia Martins', '1994-09-05', 'Brasileira', '65412398777', '21965432198', 'sophia.martins@email.com', 'sim', 'mobilidade reduzida'),
        ('Rafael Alves Souza', '1985-01-30', 'Brasileiro', '98732165444', '11954321678', 'rafael.souza@email.com', 'não', NULL),
        ('Isabela Ferreira', '2001-12-12', 'Brasileira', '34561278903', '11977788899', 'isabela.ferreira@email.com', 'não', NULL),
        ('Diego Pereira Santos', '1993-03-23', 'Brasileiro', '21354687900', '31965498765', 'diego.santos@email.com', 'sim', 'deficiência visual parcial'),
        ('Mariana Gonçalves', '1990-07-19', 'Brasileira', '12378945666', '21988877654', 'mariana.goncalves@email.com', 'não', NULL),
        ('Bruno Silva Oliveira', '1995-10-31', 'Brasileiro', '65498732111', '21943219876', 'bruno.oliveira@email.com', 'não', NULL);
''')

cursor.execute('''
    INSERT INTO destinos (cod_iata, cod_icao, nome_aeroporto, cidade, estado, pais, tipo_aeroporto) 
    VALUES
        ('GRU', 'SBGR', 'Aeroporto Internacional de Guarulhos', 'São Paulo', 'SP', 'Brasil', 'internacional'),
        ('SDU', 'SBRJ', 'Aeroporto Santos Dumont', 'Rio de Janeiro', 'RJ', 'Brasil', 'doméstico'),
        ('MIA', 'KMIA', 'Miami International Airport', 'Miami', 'FL', 'EUA', 'internacional'),
        ('LAX', 'KLAX', 'Los Angeles International Airport', 'Los Angeles', 'CA', 'EUA', 'internacional'),
        ('JFK', 'KJFK', 'John F. Kennedy International Airport', 'New York', 'NY', 'EUA', 'internacional'),
        ('SCL', 'SCEL', 'Comodoro Arturo Merino Benítez International Airport', 'Santiago', 'RM', 'Chile', 'internacional'),
        ('BRC', 'SAVC', 'Aeroporto Internacional de San Carlos de Bariloche', 'San Carlos de Bariloche', 'RN', 'Argentina', 'internacional'),
        ('LIS', 'LPPT', 'Aeroporto Humberto Delgado', 'Lisboa', 'Lisboa', 'Portugal', 'internacional'),
        ('CDG', 'LFPG', 'Aeroporto Charles de Gaulle', 'Paris', 'Île-de-France', 'França', 'internacional'),
        ('FCO', 'LIRF', 'Aeroporto Leonardo da Vinci', 'Roma', 'Lazio', 'Itália', 'internacional');
''')

cursor.execute('''
    INSERT INTO linhas_aereas (cod_linha_aerea, nome, pais_origem, contato_suporte, email) 
    VALUES
        ('LT4', 'LATAM Airlines', 'Brasil', '+551199887766', 'suporte@latam.com'),
        ('AA1', 'American Airlines', 'EUA', '+18005551234', 'support@aa.com'),
        ('GL7', 'Gol Linhas Aéreas', 'Brasil', '+551134567890', 'contato@gol.com.br'),
        ('UA9', 'United Airlines', 'EUA', '+18005556677', 'help@united.com'),
        ('AF3', 'Air France', 'França', '+330157303495', 'contact@airfrance.com'),
        ('DL2', 'Delta Airlines', 'EUA', '+18005432982', 'customer.service@delta.com'),
        ('AZ8', 'Alitalia', 'Itália', '+390650204904', 'assistenza@alitalia.com'),
        ('QR5', 'Qatar Airways', 'Qatar', '+97440230123', 'support@qatarairways.com.qa'),
        ('LH6', 'Lufthansa', 'Alemanha', '+496970058741', 'service@lufthansa.com'),
        ('EK1', 'Emirates', 'Emirados Árabes Unidos', '+97142345888', 'contactus@emirates.com');
''')

cursor.execute('''
    INSERT INTO rotas (cod_linha_aerea, cod_iata_origem, cod_iata_destino, preco_base) 
    VALUES
        ('LT4', 'GRU', 'MIA', 1200.00),
        ('AA1', 'SDU', 'GRU', 400.00),
        ('GL7', 'MIA', 'GRU', 1300.00),
        ('UA9', 'JFK', 'LAX', 350.00),
        ('AF3', 'CDG', 'FCO', 220.00),
        ('DL2', 'LAX', 'JFK', 180.00),
        ('AZ8', 'FCO', 'CDG', 250.00),
        ('QR5', 'LIS', 'SCL', 700.00),
        ('LH6', 'LHR', 'FRA', 300.00),
        ('EK1', 'DXB', 'JFK', 1300.00);
''')

cursor.execute('''
    INSERT INTO aeronaves (cod_aeronave, cod_linha_aerea, modelo, capacidade_passageiros, ano) 
    VALUES
        (1, 'GL7', 'Boeing 737', 189, 2005),
        (2, 'LT4', 'Airbus A320', 180, 2010),
        (3, 'AA1', 'Embraer E195', 132, 2008);
''')

cursor.execute('''
    INSERT INTO voos (cod_voo, cod_rota, cod_linha_aerea, cod_aeronave, cod_iata_origem, cod_iata_destino, data_hora_partida, data_hora_chegada, plataforma) 
    VALUES
        (1, 1, 'LT4', 1, 'GRU', 'MIA', '2024-12-10 08:00', '2024-12-10 16:00', 5),
        (2, 2, 'AA1', 2, 'SDU', 'GRU', '2024-12-11 15:30', '2024-12-11 17:00', 2),
        (3, 3, 'GL7', 3, 'MIA', 'GRU', '2024-12-12 10:00', '2024-12-12 18:00', 7);
''')

cursor.execute('''
    INSERT INTO passagens (cod_voo, id_cliente, tipo_assento, poltrona, status_passagem, preco_final, data_hora_compra) 
    VALUES
        (1, 1, 'executivo', '1A', 'emitida', 1500.00, '2024-12-01 09:30'),
        (2, 2, 'comfort', '10B', 'reservada', 500.00, '2024-12-02 14:45'),
        (3, 3, 'primeira classe', '2C', 'emitida', 2500.00, '2024-12-03 11:20'),
        (4, 4, 'executivo', '1B', 'emitida', 1200.00, '2024-12-04 10:00'),
        (5, 5, 'comfort', '12A', 'reservada', 800.00, '2024-12-05 15:45');
''')

cursor.execute('''
    INSERT INTO ajustes_preco (cod_voo, tipo_ajuste, valor_porcentual, descricao, data_inicio, data_fim) 
    VALUES
        (1, 'desconto', -10.00, 'Promoção de Natal', '2024-12-01', '2024-12-25'),
        (2, 'aumento', 15.00, 'Alta temporada', '2024-12-15', '2025-01-20'),
        (3, 'desconto', -5.00, 'Fidelidade', '2025-01-18', '2025-01-31');
''')

conn.commit()

conn.close()