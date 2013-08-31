# -*- encoding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        Classe ColorirTerminal:
# Purpose:
#
# Author:      Internet
#              http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
#              http://www.burgaud.com/bring-colors-to-the-windows-console-with-python/
#
# Contribuition Paulo Mateus  (mateus.moura@hotmail.com)
#               Alan Jeferson (alan_toc@hotmail.com)
#
# Created:     05/05/2012
# Copyright:   (c)
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Importações
#-------------------------------------------------------------------------------
from __future__ import print_function

import platform
import sys

if platform.system() == "Windows":
    from ctypes import windll, Structure, c_short, c_ushort, byref

#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Classe
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Classe
#-------------------------------------------------------------------------------
class ColorirTerminal:
    """
    Pego em:
    http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    http://www.vivaolinux.com.br/artigo/Formatando-o-bash-com-cores-e-efeitos
    """

    '''
        LINUX
    \x1b[0m  reset; clears all colors and styles (to white on black)
    \x1b[1m  bold on (see below)
    \x1b[3m  italics on
    \x1b[4m  underline on
    \x1b[7m  inverse on; reverses foreground & background colors
    \x1b[9m  strikethrough on
    \x1b[22m bold off (see below)
    \x1b[23m italics off
    \x1b[24m underline off
    \x1b[27m inverse off
    \x1b[29m strikethrough off
    \x1b[30m set foreground color to black
    \x1b[31m set foreground color to red
    \x1b[32m set foreground color to green
    \x1b[33m set foreground color to yellow
    \x1b[34m set foreground color to blue
    \x1b[35m set foreground color to magenta (purple)
    \x1b[36m set foreground color to cyan
    \x1b[37m set foreground color to white
    \x1b[39m set foreground color to default (white)
    \x1b[40m set background color to black
    \x1b[41m set background color to red
    \x1b[42m set background color to green
    \x1b[43m set background color to yellow
    \x1b[44m set background color to blue
    \x1b[45m set background color to magenta (purple)
    \x1b[46m set background color to cyan
    \x1b[47m set background color to white
    \x1b[49m set background color to default (black)


    HEADER  = '\033[95m'
    OKBLUE  = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL    = '\033[91m'
    ENDC    = '\033[0m'
    ALERT   = '\033[31m'

        WINDOWS
    BACKGROUND_BLACK     = 0x0000
    BACKGROUND_BLUE      = 0x0010
    BACKGROUND_GREEN     = 0x0020
    BACKGROUND_CYAN      = 0x0030
    BACKGROUND_RED       = 0x0040
    BACKGROUND_MAGENTA   = 0x0050
    BACKGROUND_YELLOW    = 0x0060
    BACKGROUND_GREY      = 0x0070
    '''

    # Sistema operacional
    OS = platform.system()


    # ----------------------------------------
    #  Métodos padrões
    # ----------------------------------------

    def __init__(self, corLetra='cinza'):
        """
        Desc: Método iniciador
        Altera a cor da letra do texto no terminal
        """

        self.coresPadroes = {
            'Linux': {
                'preto':    '\033[30m',
                'laranja':  '\033[91m',
                'vermelho': '\033[31m',
                'verde1':   '\033[92m',
                'verde2':   '\033[32m',
                'amarelo1': '\033[93m',
                'amarelo2': '\033[33m',
                'azul':     '\033[96m',
                'azul2':    '\033[94m',
                'azul3':    '\033[34m',
                'magenta':  '\033[35m',
                'ciano':    '\033[36m',
                'cinza':    '\033[90m',
                'cinza2':   '\033[97m',
                'cinza3':   '\033[37m',
                'branco':   '\033[39m',
                'rosa':     '\033[95m',
                'terminar': '\033[0m'
            },
            'Windows': {
                'preto':    0x0000,
                'azul':     0x0001,
                'verde':    0x0002,
                'ciano':    0x0003,
                'vermelho': 0x0004,
                'magenta':  0x0005,
                'amarelo':  0x0006,
                'branco':   0x0007,
                'cinza':    0x0008,
                'terminar': ''
            }

        }


        # Cor padrão
        #self.corLetra = corLetra.lower()


    def __repr__(self):
        """
        Desc: Retorna: Informações da classe
        """

        retorno  = "Utilize esta classe para alterar a cor do texto no "
        retorno += "terminal/prompt de comando\n\n"

        if self.OS != "Windows" and self.OS != "Linux":
            retorno += "Desculpe mas seu sistema operacional (" + self.OS + ")"
            retorno += " é incompatível com esta versão da classe\n\n"

            retorno += "Sistemas operacionais compatíveis:\n"
            retorno += " - Windows\n"
            retorno += " - Linux\n"
            return retorno

        retorno += "Cores disponíveis\n"

        coresOrdenadas = self.listaCores()
        for cor in coresOrdenadas:
                if cor == "terminar": continue
                retorno += " - " + self.imprimir(cor, cor, True) + "\n"

        if self.OS == "Windows":
            retorno += "\n* Para visualizar lista de cores COLORIDA, execute: \n"
            retorno += "ColorirTerminal.listaCores(True)"

        return retorno


    # ----------------------------------------


    # ----------------------------------------
    #  Métodos de impressão
    # ----------------------------------------
    def imprimir(self, texto, corLetra=None, retornar=False, quebraLinha=True):
        """
        Desc: Imprime o 'texto' na 'corLetra' ou retorna-o caso 'retornar'=True
        PARA SISTEMAS UNIX

        texto:   = Str: Texto a ser formatado. Caso a cor não exista, não colore
        corLerta = Str: Nome da cor da letra
                   None: Não colore
        retornar = Bool: True, para retornar o texto formatado (EXCUSIVO PARA
                         SISTEMAS UNIX)
                         False, para imprimir o texto
        quebraLinha = Bool: Você quer que quebre a linha após a impressão do texto?

        """
        # Não imprimir cores
        if corLetra == None or not corLetra in self.coresPadroes[self.OS]:
            if quebraLinha == False: fim = ""
            else: fim = "\n"

            print(texto, end=fim)
            return


        # Alterar cor da letra
        if corLetra == None:
            corLetra = self.corLetra
        else:
            corLetra.lower()

        # Para Linux
        if self.OS == "Linux":

            # Formatando o texto
            texto = self.coresPadroes[self.OS][corLetra] + texto + self.coresPadroes[self.OS]['terminar']

            # Retornar ou imprimir
            if retornar != True:
                if quebraLinha == False: fim = ""
                else: fim = "\n"

                print(texto, end=fim)

            else:
                return texto


        # Para Windows
        elif self.OS == "Windows":

            # Retornar ou imprimir
            if retornar == True:
                return texto

            # Pegando as cores atuais
            default_colors = self._get_text_attr()
            default_bg = default_colors & 0x0070

            # Imprimindo o texto
            self._set_text_attr( self.coresPadroes[self.OS][corLetra] | default_bg |
                                 0x0008)

            #  Quebra de linha
            #'''
            if quebraLinha == False: fim = ""
            else: fim = "\n"

            print(texto, end=fim)
            #'''
            #print(texto)

            self._set_text_attr(default_colors)


    def listaCores(self, imprimir=False):
        """
        Desc: Retorna ou imprime a lista as cores disponíves para seu sistema
        operacional

        imprimir = Bool: Você quer imprimir em vez de retornar?
        """

        coresOrdenadas = sorted(self.coresPadroes[self.OS])

        # Retornar
        if imprimir == False:
            return coresOrdenadas

        # Imprimir
        else:
            for cor in coresOrdenadas:
                if cor == "terminar": continue
                #print(" - " + self.imprimir(cor, cor, False))
                self.imprimir(" - " + cor, cor, False)

    # ----------------------------------------


    # ----------------------------------------
    #  Para impressão no Windows
    # ----------------------------------------



    def _get_text_attr(self):
      """Returns the character attributes (colors) of the console screen
      buffer."""
      csbi = _CONSOLE_SCREEN_BUFFER_INFO()
      _GetConsoleScreenBufferInfo(_stdout_handle, byref(csbi))
      return csbi.wAttributes

    def _set_text_attr(self, color):
      """Sets the character attributes (colors) of the console screen
      buffer. Color is a combination of foreground and background color,
      foreground and background intensity."""
      _SetConsoleTextAttribute(_stdout_handle, color)

    """
    http://www.burgaud.com/bring-colors-to-the-windows-console-with-python/
    Colors text in console mode application (win32).
    Uses ctypes and Win32 methods _SetConsoleTextAttribute and
    _GetConsoleScreenBufferInfo.

    $Id: color_console.py 534 2009-05-10 04:00:59Z andre $
    """

if platform.system() == "Windows":
    _SHORT = c_short
    _WORD = c_ushort

    _STD_INPUT_HANDLE  = -10
    _STD_OUTPUT_HANDLE = -11
    _STD_ERROR_HANDLE  = -12


    _stdout_handle = windll.kernel32.GetStdHandle(_STD_OUTPUT_HANDLE)
    _SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
    _GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo

    class _COORD(Structure):
      """struct in wincon.h."""
      _fields_ = [
        ("X", _SHORT),
        ("Y", _SHORT)]

    class _SMALL_RECT(Structure):
      """struct in wincon.h."""
      _fields_ = [
        ("Left", _SHORT),
        ("Top", _SHORT),
        ("Right", _SHORT),
        ("Bottom", _SHORT)]

    class _CONSOLE_SCREEN_BUFFER_INFO(Structure):
      """struct in wincon.h."""
      _fields_ = [
        ("dwSize", _COORD),
        ("dwCursorPosition", _COORD),
        ("wAttributes", _WORD),
        ("srWindow", _SMALL_RECT),
        ("dwMaximumWindowSize", _COORD)]

#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
# Execução
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    CT = ColorirTerminal()
    print(CT)

    CT.imprimir("\nEste é um exemplo de um texto com a cor azul\n", "azul")

    print("Executado: ColorirTerminal.listaCores(True)")
    print("Cores disponíveis para seu sistema operacional: ")
    print()
    CT.listaCores(True)
    input()
