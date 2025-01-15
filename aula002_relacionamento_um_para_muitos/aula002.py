import sqlite3
from prettytable import PrettyTable
from pathlib import Path
import os

os.system('cls')

# Caminho relativo
db_path = Path('BD') / 'bd_rel_1_n'
conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()

# Criação da tabela 'Clientes' (tabela principal)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone TEXT,
    cidade TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    data TEXT NOT NULL,
    valor_total REAL NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente)
)
''')

def cliente_existe(id_cliente):
    # Retornar True se o cliente existir, False caso contrário
    cursor.execute(
        'SELECT 1 FROM Clientes WHERE id_cliente = ?', (id_cliente,))
    return cursor.fetchone() is not None

def inserir_cliente():
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o e-mail do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    cidade = input('Digite a cidade do cliente: ')
    cursor.execute(''' 
    INSERT INTO Clientes (nome, email, telefone, cidade)
    VALUES (?, ?, ?, ?)
    ''', (nome, email, telefone, cidade))
    conn.commit()
    print('Cliente inserido com sucesso!')

def  inserir_pedido():
    cursor.execute(''' 
    SELECT * FROM clientes
    ''')
    resultados = cursor.fetchall()

    if not resultados: # Validação para pedidos sem clientes
        print('-' * 70)
        print('Nenhum cliente encontrado. Cadastre um cliente primeiro.')
        print('-' * 70)
        return
    
    tabela = PrettyTable['id_cliente', 'Nome', 'Email', 'Telefone', 'Cidade']
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)

    try:
        # Garantir que o ID seja um número inteiro
        id_cliente = int(input('Digite o ID do cliente: '))

        # Verificar se o cliente existe antes de prosseguir
        if not cliente_existe(id_cliente):
            print('-' * 70)
            print(f'Erro: Cliente com ID {id_cliente} não encontrado!')
            print('Por favor, cadastre o cliente primeiro.')
            print('-' * 70)
            return
        
        produto = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade: '))
        data = input('Digite a data do pedido (AAAA-MM-DD): ')
        valor_total = float(input('Digite o valor total: '))

        cursor.execute('''
        INSERT INTO Pedidos (id_cliente, produto, quantidade, data, valor_total)
        VALUES (?, ?, ?, ?, ?)
        ''', (id_cliente, produto, quantidade, data, valor_total))
        conn.commit()
        print('Pedido inserido com sucesso!')
    except ValueError:
        print('-' * 70)
        print('Erro: ID do cliente deve ser um número inteiro.')
        print('-' * 70)

def consultar_pedidos():
    cursor.execute(''' 
    SELECT
        Clientes.nome, Clientes.email, Clientes.cidade,
        Pedidos.produto, Pedidos.quantidade, Pedidos.valor_total
    FROM
        Clientes
    JOIN
        Pedidos ON Clientes.id_cliente = Pedidos.id_cliente
    ''')
    resultados = cursor.fetchall()

    tabela = PrettyTable(
        ['Nome', 'Email', 'Cidade', 'Produto', 'Quantidade', 'Valor total'])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)

def alterar_pedido():
    try:
        id_pedido = int(input('Digite o ID do pedido que deseja operar: '))

        cursor.execute(
            'SELECT * FROM Pedidos WHERE id_pedido = ?', (id_pedido,))
        pedido = cursor.fetchone()

        if not pedido:
            print('-' * 70)
            print(f'Erro: Pedido com ID {id_pedido} não encontrado!')
            print('-' * 70)
            return
        
        print('-' * 70)
        print('Dados atuais do pedido:')
        print(f'Produto: {pedido[2]}')
        print(f'Quantidade: {pedido[3]}')
        print(f'Data: {pedido[4]}')
        print(f'Valor_total: {pedido[5]}')
        print('-' * 70)

        produto = input(
            'Digite o novo nome do produto (ou pressione Enter para manter o atual): ' or pedido[2]
        )
        quantidade = input(
            'Digite a nova quantidade (ou pressione Enter para manter a atual): ' or pedido [3]
        )
        data = input(
            'Digite a nova data (AAAA-MM-DD) (ou pressione Enter para manter a atual):' or pedido[4]
        )
        valor_total = input(
            'Digite o novo valor total (ou pressione Enter para manter o atual): ' or pedido[5]
        )

        cursor.execute(''' 
        UPDATE Pedidos
        SET produto = ?, quantidade = ?, data = ?, valor_total = ?
        WHERE id_pedido = ?
        ''', (produto, int(quantidade), data, float(valor_total), id_pedido))
        conn.commit()
        print('Pedido atualizado com sucesso!')
    except ValueError:
        print('-' * 70)
        print('Erro: Entrada inválida')
        print('-' * 70)

    while True:
        print('\n Menu:')
        print('1. Inserir Cliente')
        print('2. Inserir Pedido')
        print('3. Consultar Pedidos')
        print('4. Alterar Pedido')
        print('5. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            inserir_cliente()
        elif opcao == '2':
            inserir_pedido()
        elif opcao == '3':
            consultar_pedidos()
        elif opcao == '4':
            alterar_pedido()
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('-' * 70)
            print('Opção inválida. Tente novamente.')
            print('-' * 70)

conn.close()