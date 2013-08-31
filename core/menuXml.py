# -*- encoding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        MenuXML
# Purpose:     Adiciona as opções de salvamento e carregamento no Menu
#
# Author:      Paulo Mateus
#
# Created:     23/04/2012
# Copyright:   (c) Mateus 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Importações
#-------------------------------------------------------------------------------

import os
import sys

# Procedimentos padrões
sys.path.append(os.path.split(__file__)[0])
from library.procedimentos import *

# Salvar e carregar
from xml.etree.ElementTree import Element, ElementTree

#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
# Classe
#-------------------------------------------------------------------------------

class MenuXml:

    # ----------------------------------------
    #  Métodos padrões
    # ----------------------------------------

    def __init__(self, menuPyInstance):
        """
        Desc: Método iniciador

        menuPyInstance = MenuPy: Instância da classe MenuPy
        """
        self.menuPy = menuPyInstance

    # ----------------------------------------

    # ----------------------------------------
    #  Armazenamento: Salvar
    # ----------------------------------------

    def save(self, path='menuPy.xml'):
        """
        Desc: Gera e salva o xml no 'path'

        path = str: Endereço do arquivo xml
        """
        # Gerando XML
        arquivo = self._salvar_ClasseMenu()

        # Salvando
        ElementTree(arquivo).write(endereco)



    def _salvar_ClasseMenu(self):
        """
        Desc: Responsável por criar as tags de <classe_menu>

        return = xml.etree.ElementTree.Element: Elemento a ser salvo
        """

        # Níveis:
        # classe_menu
        classe_menu = Element("classe_menu")

        # classe_menu - config
        config = Element("config")

        config = self._salvar_inserirFilhos_prop(
            self.menuPy.config, config
        )


        # classe_menu - cores
        cores = Element("cores", attrib={"libAtual":self.cores['libAtual']})

        cores = self._salvar_inserirFilhos_prop(
            self.cores[self.cores['libAtual']],
            cores
        )


        #  classe_menu - menu
        menu = Element("menu", {"id":str(self.menu[0]), "nome":self.nome})


        # classe_menu: Salvar filhos
        classe_menu.append(config)
        classe_menu.append(cores)

        #  Pegar os filhos e inseri-los no menu
        menu = self._salvar_inserirFilhos(menu)
        #  Inserindo menu em class_menu
        classe_menu.append(menu)


        return classe_menu

    def _salvar_inserirFilhos_prop(self, dicionario, Elemento):
        """
        Desc: Responsável por inserir as propriedades do menu, inserindo os
              itens do 'dicionario' no 'Elemento'.

        dicionario = Dict: Dados que serão inseridos em 'Elemento'
        Elemento   = xml.etree.ElementTree.Element(): Nó em que os itens serão inseridos

        return = Elemento com os dados adicionados
        """
        for chave, valor in dicionario.items():
            # Demarcando strings
            if tipoVariavel(valor) == "str":
                valor = "'" + valor + "'"


            Elemento.append(
                Element("conf",
                        {"key":str(chave),
                         "type":tipoVariavel(valor)},
                         text=str(valor)
                )
            )

        return Elemento

    def _salvar_inserirFilhos(self, menu):
        """
        Desc: Responsável por inserir os filhos de self

        menu = xml.etree.ElementTree.Element(): Menu em que os itens serão inseridos
        """

        for item in self.itens:

            if self.eMenu(item):
                menu.append(item._salvar_ClasseMenu())

            elif tipoVariavel(item) == "list":

                menuFilho = Element("item", {"text":item[1], "parametros":item[3]})

                # Adicionando funcao
                if tipoVariavel(item[2]) == "Quitter":
                    menuFilho.attrib["funcao"] = "retornar"
                elif tipoVariavel(item[2]) == "str":
                    menuFilho.attrib["funcao"] = item[2]
                else:
                    menuFilho.attrib["funcao"] = item[2].__name__

                menu.append(menuFilho)

        return menu

    # ----------------------------------------


    # ----------------------------------------
    #  Armazenamento: Carregar
    # ----------------------------------------

    def load(self, path):
        """
        Desc: Carrega o menu salvo em xml no 'endereco'

        path = str: Endereço do arquivo xml

        retorno = Boolean: True caso o carregamento tenha sido um sucesso
        """

        xml = ElementTree(file=path)
        classe_menu = xml.getroot()

        self._carregar_ClasseMenu(classe_menu)

        return True


    def _carregar_ClasseMenu(self, Elemento):
        """
        Desc: Responsável por montar menu

        Elemento = ElementTree().xml.getroot(): Raiz de ElementTree
        """

        # Pegando a lista de elementos
        TAGclasse_menu = list(Elemento)

        # Carregando menu
        for elemento in TAGclasse_menu:

            # Configurações
            if elemento.tag == "config":
                self._carregar_prop(self.config, elemento)
            # Cores
            elif elemento.tag == "cores":
                # Biblioteca sendo utilizada
                self.cores['libAtual'] = elemento.attrib['libAtual']
                # Cores modificadas pelo usuário
                self._carregar_prop(self.cores[self.cores['libAtual']], elemento)

            # Itens
            elif elemento.tag == "menu":
                atributos = elemento.attrib
                self.nome = atributos["nome"]
                self._carregar_filhosMenu(elemento)


    def _carregar_prop(self, dicionario, Elemento):
        """
        Desc: Responsável por carregar as propriedades do menu, atualizando o
              itens do 'dicionario' no 'Elemento'.

        dicionario = Dict: Dados que serão atualizados a partir do 'Elemento'
        element    = xml.etree.ElementTree.Element(): Nó contendo os dados que
                         serão inseridos no 'dicionario'

        return = Elemento com os dados adicionados
        """

        # Pegando a lista de elementos
        TAG = list(Elemento)


        # Atualizando artibutos de configuração
        for elemento in TAG:

            # Pegando os atributos da tag
            atributos = elemento.attrib

            # Formatação da variável
            atributos["text"] = eval(atributos["type"]+"("+atributos["text"]+")")

            # Inserindo no 'dicionario'
            dicionario[atributos["key"]] = atributos["text"]



    def _carregar_filhosMenu(self, Elemento):
        """
        Desc: Carrega os filhos do menu

        Elemento = xml.etree.ElementTree.Element(): Tag menu
        """
        # Pegando a lista de elementos
        TAGmenu = list(Elemento)

        # Atualizando artibutos de configuração
        for elemento in TAGmenu:

            # Item
            if elemento.tag == "item":
                atributos = elemento.attrib
                self.adicionarItem([], atributos['text'], atributos['funcao'], atributos['parametros'])

            # Menu
            elif elemento.tag == "classe_menu":
                self.adicionarSubMenu([], "")
                self.itens[-1]._carregar_ClasseMenu(elemento)
