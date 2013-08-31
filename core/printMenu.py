# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        printMenu
# Purpose:     Imprimir um menu com suas opções
#
# Author:      Paulo Mateus
#
# Created:     30/08/2013
# Version:     beta 0.9.0
# Copyright:   (c) Paulo Mateus
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Importações
#-------------------------------------------------------------------------------
from __future__ import print_function

import sys
import os
sys.path.append(os.path.split(__file__)[0])

from library.colorirTerminal import *
CT = ColorirTerminal()

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Classe
#-------------------------------------------------------------------------------

class PrintMenu:

    if platform.system() == "Linux":
        colors = dict({
            'breadcrumb': 'azul3',
            'title':      'verde2',
            'returnItem': 'ciano',
            #'menus':      'branco',
            'items':      'branco',#'cinza'
            'selectOpt':  'ciano'
        })

    else:
        colors = dict({
            'breadcrumb': 'amarelo',
            'title':      'verde',
            'returnItem': 'ciano',
            #'menus':      'branco',
            'items':      'branco',#'cinza'
            'selectOpt':  'ciano'
        })

        show = dict({
            'breadcrumb': True 
        })

    @staticmethod
    def print(menu):
        """
        Desc: Menu a ser impresso
        
        menu = Menu: Menu a ser impresso
        """
        if PrintMenu.show['breadcrumb']:
            PrintMenu.breadcrumb(menu)
            print()

        PrintMenu.title(menu, menu.config['lengthBar'], menu.config['character'])
        print()

        PrintMenu.items(menu)
        print()

        PrintMenu.footer()
    # ----------------------------------------


    # ----------------------------------------
    #  Partes
    # ----------------------------------------
    @staticmethod
    def breadcrumb(menu):
        """
        Desc: Mostra o caminho percorrido até o menu atual

        menu = Menu:  
        """
        breadcrumb = menu.label
        menuFather = menu.father

        while menuFather != None:
            breadcrumb = menuFather.label + ' > ' + breadcrumb
            menuFather = menuFather.father 

        CT.imprimir(_("You are in:"), PrintMenu.colors['breadcrumb'], quebraLinha=False)
        print(" " + breadcrumb)


    @staticmethod
    def title(menu, lengthBar=30, character="*"):
        """
        Desc: Imprime o cabeçalho do menu

        menu = Menu:
        lengthBar = Int: Total de caracteres (largura) na perfumaria do menu
        character = Str: Perfumaria a ser utilizada.
                         O código pressupõe que len(character) = 1
        """
        # Cálculos
        sizeSideBarLeft = int((lengthBar - len(menu.label)-2)/2)

        sizeSideBarRight = sizeSideBarLeft 
        if (lengthBar - len(menu.label)-2)%2 == 1: # Se for ímpar, compensa do lado direito
            sizeSideBarRight += 1

        # Barra
        CT.imprimir(str(character * lengthBar), PrintMenu.colors['title'])

        # Título
        centerBar = character * sizeSideBarLeft + " " + menu.label + " " + character * sizeSideBarRight 
        CT.imprimir(str(centerBar), PrintMenu.colors['title'])

        # Barra
        CT.imprimir(str(character * lengthBar), PrintMenu.colors['title'])


    @staticmethod
    def items(menu, character="-"):
        """
        Desc: Imprime os itens do 'menu'

        menu = Menu:
        character = Str: Caractere separador
        """

        if menu.father != None:
            msg = 'Return to the previous menu'
        else:
            msg = 'Exit'

        CT.imprimir('0 ' +character+ ' ' + _(msg), PrintMenu.colors['returnItem'])

        counter = 1
        #for item in menu.getMenuItems() + menu.getLeafItems():
        for item in menu.items:
            CT.imprimir(str(counter) + ' '+character+' ' + item.label, PrintMenu.colors['items'])
            counter += 1


    @staticmethod
    def footer():
        """
        Desc: Imprime "Escolha uma opção"
        """

        CT.imprimir(_("Select a option: "), PrintMenu.colors['selectOpt'], quebraLinha=False)




