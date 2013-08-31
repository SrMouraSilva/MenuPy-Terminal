# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        menu
# Purpose:     Menu que contém itens e/ou menus
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

from core.item          import Item
from core.itemComponent import ItemComponent

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Classe
#-------------------------------------------------------------------------------

class Menu(ItemComponent):

    def __init__(self, father, label):
        """
        Desc: Menu que contém itens e/ou menus

        father = Str: Menu pai. 
                 None: Nenhum pai
        label  = Str: Título do menu
        """
        # Herança
        ItemComponent.__init__(self, father, label)


        self.items = []

        self.config = dict({
            "character": "*",
            "lengthBar": 30
        })

    def __repr__(self):
        """
        Desc: Retorna: Dados do objeto
        """
        retorno  = _("Menu: ") + self.label + "\n"
        retorno += _(" Description: \n\n")

        retorno += ItemComponent.__repr__(self)

        retorno += _(" Total items: ")+ str(self.totalItems) +"\n"
        retorno += _("  Menu items: ")+ str(self.totalMenuItems) +"\n"
        retorno += _("  Items items: ")+ str(self.totalLeafItems) +"\n"


        return retorno

    # ----------------------------------------


    # ----------------------------------------
    #  Métodos de incrementação
    # ----------------------------------------
    def _add(self, itemComponent):
        """
        Desc: Adiciona um itemComponent (item ou menu)
        """
        self.items.append(itemComponent)


    def addItem(self, label, function, *arg):
        """
        Desc: 

        label    = Str: Rótulo do item do menu
        function = Str: Nome da função
        arg      = Argumentos da funcao INCREMENTAR
        """
        item = Item(self, label, function, *arg)
        self._add(item)


    def addMenu(self, label):
        """
        Desc: Adiciona um menu neste menu

        father = Str: Menu pai. 
                 None: Nenhum pai
        label = Str: Título do menu
        """
        menu = Menu(self, label)
        menu.config['character'] = self.config['character']
        menu.config['lengthBar'] = self.config['lengthBar']
        self._add(menu)

    # ----------------------------------------


    # ----------------------------------------
    #  Informações do menu
    # ----------------------------------------
    # totalItems
    def _get_totalItems(self):
        """
        Desc: Retorna o total de itens do menu
        """
        return len(self.items)

    totalItems = property(fget=_get_totalItems)


    # totalMenuItems
    def _get_totalMenuItems(self):
        """
        Desc: Retorna o total de itens que são menus
        """

        totalItens = 0

        for item in self.items:
            if item.__class__.__name__.count("Menu") > 0:
                totalItens += 1

        return totalItens

    totalMenuItems = property(fget=_get_totalMenuItems)


    # totalLeafItems
    def _get_totalLeafItems(self):
        """
        Desc: Retorna o total de itens que chamam procedimentos
        """
        return self.totalItems - self.totalMenuItems

    totalLeafItems = property(fget=_get_totalLeafItems)

    # ----------------------------------------


    # ----------------------------------------
    #  Recuperação de dados
    # ----------------------------------------
    def getMenuItems(self):
        """
        Desc: Retorna List: Todos os menus filhos deste menu
        """
        menus = []

        for item in self.items:
            if item.__class__.__name__.count("Menu") > 0:
                menus.append(item)

        return menus

    def getLeafItems(self):
        """
        Desc: Retorna List: Todos os itens que chamam procedimentos deste menu
        """
        items = []

        for item in self.items:
            if item.__class__.__name__.count("Menu") == 0:
                items.append(item)

        return items


