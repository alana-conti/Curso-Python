"""
PEP8 - Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigod Python de forma Pythônica

[1] - Utilize Camel Case para nomes de classes (nome simples com inicial maóuscula sem espaços - CalculadoraCientifica);
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo separados por _ para funções ou variáveis;
def soma():
    pass


def soma_dois()
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação! (NÃO use o tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classes com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports devem ser sempre feitos em linhas separadas;
Import errado
    import sys, os

import certo
    import sys
    import os

Não há problemas em utilizar:

from types import StringTyoe, ListType

Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)
- Imports devem ser colocados no topo do arquivo logo depois de quaisquer comentários ou docstrings e antes de constantes ou variáveis globais;

[6] Espaços em expressões e instruções

- Não faça:

funcao{ algo[ 1 ], { outro: 2 } }

- Faça:

funcao{algo[ 1 ], { outro: 2}}

- Não Faça:

algo (1)

- Faça:

algo(1)

- Não Faça:

dict ['chave'] = list [indice]

- Faça:

dict['chave'] = list[indice]

- Não Faça:

x              = 1
y              = 3
variavel_longa = 5

- Faça:

x = 1
y = 3
variavel_longa = 5

[7] Termine sempre uma instrução com uma nova linha
"""

import this
