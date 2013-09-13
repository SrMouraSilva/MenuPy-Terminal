# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        menu
# Purpose:     Classe criadora de menus
#
# Author:      Paulo Mateus
#
# Created:     05/07/2011
# Version:     beta 0.7.0
# Copyright:   (c) Paulo Mateus
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Importações
#-------------------------------------------------------------------------------
from __future__ import print_function


# Perfumaria
import os # Limpar tela

# Verificar OS
import platform
import sys

sys.path.append(os.path.split(__file__)[0])

# Core
from core.itemComponent import ItemComponent
from core.item          import Item
from core.menu          import Menu
from core.printMenu     import PrintMenu
from core.menuXml       import MenuXml

# Procedimentos padrões
from library.procedimentos import *

# Detectar teclas
from library.detectarTeclado import DetectarTeclado

# Internacionalização
from library.i18n import iniciar as i18n_iniciar
i18n_iniciar('menu')

# Terminal colorido
from library.colorirTerminal import *
CT = ColorirTerminal()

#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Métodos para futuras classes
#-------------------------------------------------------------------------------
# Tratamento de erros
class MenuPyError(Exception):
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



def limparTela(sistOperacional):
    """
    Desc: Limpa a tela do prompt

    sistOperacional = Atribute: os.environ['OS']
    """

    if sistOperacional == "Windows":
        os.system("cls")
    else:
        os.system("clear")


#-------------------------------------------------------------------------------
# Inicializando sistema
#-------------------------------------------------------------------------------
_detec = DetectarTeclado()

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Classe
#-------------------------------------------------------------------------------

class MenuPy:


    # ----------------------------------------
    #  Métodos padrões
    # ----------------------------------------

    def __init__(self, title=_("Title")):
        """
        Desc: Método iniciador

        title = Str: Rótulo do título
        """

        self.root = Menu(None, title)

        # Encapsulamento
        self.xml = MenuXml(self)

        # Herança
        MenuXml.__init__(self, self)


        # Configurações do menu:
        self.config = dict({
            "version": "beta 0.9.0",

            "cleanTerminal": True
        })
        if platform.system() != "Windows" and platform.system() != "Linux":
            self.config["detectKey"] = "manual"
        else:
            self.config["detectKey"] = "automatic"


    # ----------------------------------------
    def run(self):
        """
        Desc: Executa o menu
        """

        menu = self.root

        while menu != None:

            if self.config["cleanTerminal"] == True:
                limparTela(platform.system())

            PrintMenu.print(menu)

            selectedOption = self._capturarTecla(menu.totalItems)

            # Retornar ao menu anterior
            if selectedOption == 0:
                menu = menu.father
                continue

            selectedOption -= 1 # List's begins with id 0

            # Executar função de item
            if menu.items[selectedOption].__class__.__name__ == "Item":
                menu.items[selectedOption].run()
                continue

            # Exibir dados do menu
            menu = menu.items[selectedOption]


    # ----------------------------------------


    # ----------------------------------------
    #  Métodos de captura de tecla
    # ----------------------------------------

    def _capturarTecla(self, numFinal, numInicial=-1):
        """
        Desc: Captura a tecla que o usuário final tecla para ativar a opção do menu

        numFinal   = Int: Número final de elementos da lista.
                          O máximo que a classe suporta é "9"
        numInicial = Int: Número inicial de contagem

        return = Int: Elemento selecionado dentro das opções possíveis
        """


        #  Método de captura depende do sistema operacional a ser utilizado
        if self.config["detectKey"] == "automatico":

            print() # Printar a frase anterior, que end=""
            opcaoSelecionada = False

            # Verificar se a tecla pressionada é uma opção
            #    not (Tecla selecionada é um número)  (concatenado com) not (Selecionado uma das opções)
            while (opcaoSelecionada <= ord(str(numInicial)) or opcaoSelecionada > ord(str(numFinal)) \
                   or opcaoSelecionada==False):
                #  Convertendo para formato utilizado pelo sistema
                opcaoSelecionada = str(_detec.detectarTecla(modoDeteccao=True))
                #  Compatibilidade entre os sistemas operacionais
                if platform.system() == "Windows" and sys.version_info[0] == 3:
                    opcaoSelecionada = opcaoSelecionada[2]
                opcaoSelecionada = ord(opcaoSelecionada)

            # Conversão para string
            opcaoSelecionada = chr(opcaoSelecionada)

        else:
            while True:

                # Pegar tecla:
                opcaoSelecionada = _detec.detectarTecla(modoDeteccao=False)


                # Verificar se a opção foi válida
                if opcaoSelecionada.isdigit():

                    # Verificar se a string é uma opção
                    if int(opcaoSelecionada) > numInicial \
                       and int(opcaoSelecionada) <= numFinal:
                        break
                    else: print(_("Select a valid option: "), end="")

                else: print(_("Select a valid option: "), end="")


        # Conversão para inteiro
        opcaoSelecionada = int(opcaoSelecionada)

        return opcaoSelecionada

    # ----------------------------------------


    # ----------------------------------------
    #  Métodos de percorrimento
    # ----------------------------------------
    def getItemComponent(self, path):
        """
        Desc: Retorna o itemComponent requisitado cuja posição fora dada em 'path'

        path  = List: Caminho do menu
                []: Raiz

        return ItemComponent: Elemento requisitado 
        """
        component = self.root

        while path:
            try:
                component = component.items[path[0]]
            except IndexError:
                raise MenuPyError(_("The given path is invalid!"))
            path = path[1:] 

        return component

    # ----------------------------------------


    # ----------------------------------------
    #  Métodos de incrementação de itemElement's
    # ----------------------------------------
    def addSubMenu(self, path, label):
        """
        Desc: Adiciona um submenu a um menu.
              Submenu herda as self.config do pai

        path  = List: Caminho do submenu
                []: Raiz
        label = Str: Rótulo do item do menu
        """
        menu = self.getItemComponent(path)

        if menu.__class__.__name__  != "Menu":
            raise MenuPyError(_("You can not add submenus on an item! \nThe given path points to the Item "+ menu.label +" and not to a Menu."))

        menu.addMenu(label)


    def addItem(self, path, label, function, *arg):
        """
        Desc: Adicionar item a um menu

        path  = List: Caminho do submenu
                []: Raiz

        label    = Str: Rótulo do item do menu
        function = Str: Nome da função
        arg      = Argumentos da funcao INCREMENTAR
        """

        menu = self.getItemComponent(path)

        if menu.__class__.__name__  != "Menu":
            raise MenuPyError(_("You can not add items on an Item! \nThe given path points to the Item "+ menu.label +" and not to a Menu."))

        menu.addItem(label, function, *arg)


#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Execução
#-------------------------------------------------------------------------------
#if __name__ == '__main__':
if 1==1:

    def imprimir(imprimir="Eu que fiz essa funcao! xD"):

        print(imprimir)

        print()
        if sys.version_info[0] == 3:
            input(_("\nPress Enter to complete this procedure"))
        else:
            raw_input(_("\nPress Enter to complete this procedure"))
        print()


    # ----------------------------------------
    #  Exemplo de menu
    # ----------------------------------------

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

    #menu.run()
    #'''


    # Para salvar/carregar em um XML
    #  Salvar
    #menu.xml.save()
    #  Carregar
    #menu = Menu()
    #menu.load("menuExemplo.xml")



    '''
    import pydoc
    teste = pydoc.Doc()
    teste.document(Menu)
    #pydoc.Doc.document(Menu)
    '''
