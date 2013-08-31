# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        item
# Purpose:     Itens do Menu
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

from core.itemComponent import ItemComponent


#-------------------------------------------------------------------------------
# Métodos para futuras classes
#-------------------------------------------------------------------------------
# Tratamento de erros
class ItemError(Exception):
    pass

    '''
    def __init__(self, mensagem=None):
        """
        Desc: Erros do Menu

        mensagem = Str: Mensagem de erro
        """
        Exception.__init__(self)
        if mensagem != None:
            self.message = mensagem
        else:
            self.message = "Ocorreu um erro inesperado!"
    '''



#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Classe
#-------------------------------------------------------------------------------

class Item(ItemComponent):

    def __init__(self, father, label, function, *arg):
        """
        Desc: Item referente a um Menu

        father   = Menu: Menu pai
        label    = Str: Rótulo do item do menu
        function = : Referência à função a ser executada
        arg      = Mixed: Argumentos da funcao INCREMENTAR
        """

        if father == None:
            raise ItemError(_("Item needs a father!"))

        ItemComponent.__init__(self, father, label) # Herança

        self.function = function
        self.arg      = arg

    def run(self):
        """
        Desc: Executa sua self.function
        """
        if self.function.__class__.__name__ == "str":
            eval(self.function)(*eval(self.arg))

        else:
            self.function(*self.arg)

