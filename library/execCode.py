# -*- encoding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        ExecCode
# Purpose:     Abre programas
#
# Author:      Paulo Mateus
#
# Created:     11/05/2012
# Copyright:   (c) Paulo Mateus
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import subprocess

class ExecCodeC():
    """
    Baseado em:
    http://docs.python.org/library/subprocess.html#popen-objects
    """

    # ----------------------------------------
    #  Métodos padrões
    # ----------------------------------------

    def __init__(self, codigoTerminal):
        """
        Desc: Método iniciador

        codigoTerminal = Str: Código do terminal para abrir o programa
                         Se for um programa, use "nomePrograma"
                         Se for para executar um script, use
                         "compilador caminhoDoScript"
        """
        self.programa = subprocess.Popen(codigoTerminal)

    # ----------------------------------------

    # ----------------------------------------
    #  Métodos da classe
    # ----------------------------------------

    def retorno(self):
        """
        Desc: Retorna o retorno do main do programa C
        """
        return self.programa.poll()

    def fechar(self):
        """
        Desc: Fecha o programa caso o mesmo ainda esteja em execução
        """
        self.programa.terminate()
        #self.programa.kill()

#-------------------------------------------------------------------------------
# Execução
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    programaC = ExecCodeC("python E:\\Programação\\Python\\menu\\menu\\biblioteca\\colorirTerminal.py")
    input("Pressione ENTER para fechar")
    programaC.fechar()
