"""
Trabalhando com módulos Built-In (módulos integrados, que já vem instalados no Python)

|Python|Módulos Built-In|
-------------------------

# Utilizando alias (apelidos) para módulos ou funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

# Importando todo o módulo

import random

print(random.random())

# Utilizando alias (apelidos) para módulos ou funções

from random import randint as rdi

print(rdi(5, 89))

# Utilizando alias (apelidos) para módulos ou funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

# Nós costumamos utilizar tuple para colocar múltiplos imports de um mesmo módulo 

from random import (
    random, 
    randint, 
    shuffle, 
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))

https://docs.python.org/3/py-modindex.html 
"""
# Nós costumamos utilizar tuple para colocar múltiplos imports de um mesmo módulo 

from random import (
    random, 
    randint, 
    shuffle, 
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))