# -*- coding: utf-8 -*-

# Importações
#-------------------------------------------------------------------------------
from __future__ import print_function

import sys

from core.itemComponent import ItemComponent
from core.item          import Item
from core.menu          import Menu
from core.printMenu     import PrintMenu
from menu               import MenuPy



# Internacionalização
from biblioteca.i18n import iniciar as i18n_iniciar
i18n_iniciar('menu')

#-------------------------------------------------------------------------------

def echo(msg):
   print(echo)

#-------------------------------------------------------------------------------
# Test
#-------------------------------------------------------------------------------
'''
menu = Menu(None, 'Menu nível 1')
menu.addMenu('Menu nível 2')
menu.addItem('Item 1', echo)

print('-----------------------------------')
print(menu)
print('-----------------------------------')

PrintMenu.print(menu)

print('-----------------------------------')

PrintMenu.print(menu.getMenuItems()[0])

'''
    
if 1 == 1:
    def imprimir(imprimir="Eu que fiz essa funcao! xD"):

        print(imprimir)

        print()
        if sys.version_info[0] == 3:
            input(_("\nPress Enter to complete this procedure"))
        else:
            raw_input(_("\nPress Enter to complete this procedure"))
        print()


    menu = MenuPy(_("Main Menu"))
    menu.config["detectKey"] = "manual"
    #menu.config["limparTela"] = False
    #menu.root.config["character"] = "_"

    #'''
    # Menu
    menu.addSubMenu([], "Geometria plana")
    menu.addSubMenu([], "Geometria espacial")
    menu.addSubMenu([], "Geometria analítica")
    menu.addSubMenu([], "Sobre")

    menu.root.items[0].config["character"] = "_"
    menu.root.items[1].config["character"] = "^"
    menu.root.items[3].config["character"] = "x"


    # Geomeria plana
    menu.addItem([0], "Lei dos Senos", imprimir, 'Testando impressão da opção 1')
    menu.addItem([0], "Teorema de pitagoras", imprimir, 'Testando impressão da opção 2')
    menu.addSubMenu([0], "SubMenu")

    #  Geometria plana -> SubMenu
    menu.addItem([0, 2], "Item 1", imprimir)
    menu.addItem([0, 2], "Item 2", imprimir)
    menu.addItem([0, 2], "Item 3", imprimir)


    # Geometria espacial
    menu.addItem([1], "Lambda", imprimir)
    menu.addItem([1], "Teorema de pitagoras", imprimir)


    # Sobre
    menu.addItem([3], "Autor", imprimir, 'Paulo Mateus Moura da Silva')
    menu.addItem([3], "Data do início do desenvolvimento", imprimir, '05/07/2011')
    menu.addItem([3], "Versão", imprimir, 'Versão '+ menu.config["version"])

    menu.run()
