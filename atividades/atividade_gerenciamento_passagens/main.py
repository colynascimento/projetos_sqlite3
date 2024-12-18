import sqlite3
import os
import cliente
import linha_aerea
import voo
import sys
import cliente

os.system('cls')

print('Menu')
print('_' * 60)
print('1 - Clientes')
print('2 - Linhas Aéreas')
print('3 - Vôos')
print('_' * 60)

area = input('Qual área deseja acessar? ')

if area == '1':
    os.system('cls')
    cliente.cliente_dao.ClienteDao

