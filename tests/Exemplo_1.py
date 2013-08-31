# -*- encoding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bolsista
#
# Created:     05/03/2012
# Copyright:   (c) Bolsista 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from menu import Menu


def testes(mensagem, adicional=""):
    print(mensagem, adicional)


# Criando menu
menu = Menu("Menu Principal")

# Menu
menu.adicionarSubMenu([], "Submenu 1")
menu.adicionarItem([], "Sair", quit)

# Submenu 1
menu.adicionarItem([0], "Opção 1", testes, "Opção 1 foi selecionada")
menu.adicionarItem([0], "Opção 2", testes, "Opção 2 foi selecionada", "Interessante, não?")
menu.adicionarItem([0], "Retornar ao menu anterior", "retornar")

menu.executar()