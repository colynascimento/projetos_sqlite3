from menus.menu_clientes import menu_clientes
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
            print("Opção de Linhas Aéreas ainda não implementada.")
            input("Pressione qualquer tecla para continuar.")
        elif area == '3':
            print("Opção de Voos ainda não implementada.")
            input("Pressione qualquer tecla para continuar.")
        elif area == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione qualquer tecla para continuar.")

menu_principal()

os.system('cls')
print('Obrigada por usar o sistema :)')