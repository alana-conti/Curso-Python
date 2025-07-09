"""
Instalando e utilizando módulos externos

Utilizamos o gerenciador de pacotes Python chamado PIP - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> é utilizado para permitir impressão de textos coloridos no terminal.

Instalando um módulo:

pip install nome-do-modulo

# Instalando o pacote colorama

pip install colorama

# Utilizando o pacote instalado

from colorama import init
init()

from colorama import Fore, Back, Style

print(Fore.LIGHTBLUE_EX + 'Geek University')

print(Style.DIM + 'Geek University')

print(Back.GREEN + 'Geek University')

print(Style.RESET_ALL + 'Geek University')
"""

import pydf

pdf = pydf.generate_pdf("<h1>Geek University</h1><br><br><strong>Programa&ccedil;&atilde;o em Python: Essencial</strong>")

with open('Seção 11 - Trabalhando com Módulos e Pacotes Python/test_doc.pdf', 'wb') as f:
    f.write(pdf)
