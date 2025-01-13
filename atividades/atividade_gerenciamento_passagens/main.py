from menus.menu_clientes import menu_clientes
from menus.menu_linhas_aereas import menu_linhas_aereas
from menus.menu_voos import menu_voos
import os

def menu_principal():
    while True:
        os.system('cls')

        print('Menu Principal')
        print('_' * 60)
        print('1 - Clientes')
        print('2 - Linhas Aéreas')
        print('3 - Vôos')
        print('0 - Sair')
        print('_' * 60)

        area = input('Qual área deseja acessar? ')

        if area == '1':
            menu_clientes()

        elif area == '2':
            menu_linhas_aereas()

        elif area == '3':
            menu_voos()
            
        elif area == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione qualquer tecla para continuar.")

menu_principal()

os.system('cls')
print('Obrigada por usar o sistema :)')