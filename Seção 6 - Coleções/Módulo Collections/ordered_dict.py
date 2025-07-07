"""
Módulo Collections - Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedtDict

# Em um dicionário a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.

# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""
from collections import OrderedDict

# Entendendo a diferença entre Dict e OrderedDict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True -> já que a ordem dos elementos não importa para o dicionário
print(dict1)
print(dict2)

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False -> já que a ordem dos elementos importa para o ordered dicionário
print(odict1)
print(odict2)