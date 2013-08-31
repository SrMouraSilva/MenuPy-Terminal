# -*- encoding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        DetectarTeclado
# Purpose:     Controle de dados inseridos pelo usuário final
#
# Author:      Paulo Mateus
#
# Created:     05/03/2012
# Version:     beta 0.1
# Copyright:   (c) Mateus 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Importações
#-------------------------------------------------------------------------------
from __future__ import print_function


# Verificar OS
import platform


# Verificar versão do python
import sys
versaoPython = sys.version_info[0]


# Sistema operacional
sistOperacional = platform.system()


if sistOperacional == "Windows":
    import msvcrt
else:
    import termios


#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Classe
#-------------------------------------------------------------------------------
class DetectarTeclado:


    # ----------------------------------------
    #  Atributos
    # ----------------------------------------
    global sistOperacional
    global versaoPython


    # ----------------------------------------
    #  Métodos padrões
    # ----------------------------------------

    def __init__(self):
        """
        Desc: Método iniciador
        """
        pass


    def detectarTecla(self, mensagem="", modoDeteccao=True):
        """
        Desc: Retorna o valor digitado

        mensagem     = Str: Mensagem a ser exibida
        modoDeteccao = Bool: True, para captura de tecla automática
                             False, para o inverso

        return = Str: O que o usuário inseriu
        """

        # Detecção de tecla automática
        if modoDeteccao==True:
            if sistOperacional == "Windows":
                return self.detecWindows(mensagem)
            else:
                return self.detecUnix(mensagem)

        # Detecção de tecla manual
        else:
            if versaoPython == 3:
                return self.detecPy3(mensagem)
            else:
                return self.detecPy2(mensagem)

    # ----------------------------------------


    # ----------------------------------------
    #  Detecção manual
    # ----------------------------------------

    def detecPy2(self, mensagem=""):
        """
        Desc: Retorna o valor digitado

        mensagem = Str: Mensagem a ser exibida

        return = Str: O que o usuário inseriu
        """
        return raw_input(mensagem)


    def detecPy3(self, mensagem=""):
        """
        Desc: Retorna o valor digitado

        mensagem = Str: Mensagem a ser exibida

        return = Str: O que o usuário inseriu
        """
        return input(mensagem)


    # ----------------------------------------


    # ----------------------------------------
    #  Detecção automática
    # ----------------------------------------
    def detecWindows(self, mensagem="", exibirTecla=False):
        """
        Desc: Retorna o valor digitado

        mensagem    = Str: Mensagem a ser exibida
        exibirTecla = Bool: Exibir tecla inserida pelo usuário?

        return = Str: O que o usuário inseriu
        """
        if exibirTecla == False:
            return msvcrt.getch()
        else:
            return msvcrt.getche()


    def detecUnix(self, mensagem="", exibirTecla=False):
        """
        Desc: Retorna o valor digitado
        BASEADO EM: http://dis.4chan.org/read/prog/1236990226

        mensagem = Str: Mensagem a ser exibida

        return = Str: O que o usuário inseriu
        """

        oldflags = termios.tcgetattr(sys.stdin.fileno())
        newflags = list(oldflags)

        # Set non-canonical mode
        newflags[3] &= ~(termios.ICANON | termios.ECHO)
        try:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, newflags)
            chars = sys.stdin.read(1)
        finally:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, oldflags)

        # Mensagem
        print(mensagem, end="")
        if exibirTecla == True: print(chars)

        # Retorno
        return chars

#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Execução
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    pass