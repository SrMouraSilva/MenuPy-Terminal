# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        item component
# Purpose:     Abstraction of item component
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

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Classe
#-------------------------------------------------------------------------------
class ItemComponent():

    def __init__(self, father, label):
        """
        Desc: Abstração de um item component

        father = Str: Menu pai
                 None: Nenhum pai
        label = Str: Título do ItemComponent
        """

        self.father = father
        self.label = label


    def __repr__(self):
        """
        Desc: Retorna: Dados do objeto
        """
        if self.father == None:
            return ''

        retorno  = _(" Menu Father: ")+ self.father.label +"\n"
        retorno += "\n"

        return retorno
