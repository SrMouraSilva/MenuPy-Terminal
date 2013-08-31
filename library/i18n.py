# -*- encoding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        i18n
# Purpose:     Internacionalização do código
#              Retirado de:
#              http://www.python.org.br/wiki/TraduzindoSeuPrograma
#              http://ndvo.wordpress.com/2009/05/26/usando-gettext-com-o-python/
#              http://www.doughellmann.com/PyMOTW/gettext/
#
# Author:      Paulo Mateus
#
# Created:     29/04/2012
# Copyright:   (c) Paulo Mateus
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

'''
#  Importa o gettext
import gettext
#  Cria uma instancia da tradução, com o nome do "domínio" (o seu programa e a pasta na qual estão os arquivos de tradução)
t = gettext.translation('menu', '')
#  Renomeia a função t.ugettext para "_" para facilitar no corpo do código
_ = t.ugettext
'''

#-------------------------------------------------------------------------------
# Importações
#-------------------------------------------------------------------------------
import locale

# lê variáveis de ambiente LC_ALL, LANG, ...
LC_ALL = locale.setlocale(locale.LC_ALL, '')

#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Procedimentos
#-------------------------------------------------------------------------------
# Tratamento de erros
class I18nError(Exception):
    pass

# Principal
def iniciar(arquivoTraducao, lingua=None, pasta="locale"):
    """
    Desc: Inicia a tradução a partir do 'arquivoTraducao' a partir da 'lingua' desejada

    nomeProg = Str: Nome do arquivo de tradução do programa
    lingua   = Str: Língua padrão. Caso arquivo não a tenha, os textos não serão
                    traduzidos
               None: Traduz para linguagem padrão do OS. Caso não possua tradução
                     para esta língua, os textos não serão traduzidos
    pasta    = Str: Pasta onde se encontram os arquivos de tradução (.mo)
    """

    # Importando pacote
    try:
        import gettext

        # Pegando língua padrão do sistema operacional
        if lingua == None:
            lingua = locale.getlocale()[0]

        # Instalando pacote de internacionalização
        lang = gettext.translation(arquivoTraducao, pasta, languages=[lingua], fallback=True)
        lang.install()

        # Procedimento da internacionalização
        global _
        _ = lang.gettext


    # Caso não pacote não existe
    except ImportError:

        # Define _() para programa não falhar
        import sys
        if sys.version_info[0] == 3:
            import builtins
        else:
            import __builtin__ as builtins

        builtins.__dict__[ "_" ] = lambda x: x

        # Gera erro
        '''raise I18nError("Você não possui o módulo 'gettext' instalado em seu sistema \
                         internacionalização não será usada.")'''
        return False
