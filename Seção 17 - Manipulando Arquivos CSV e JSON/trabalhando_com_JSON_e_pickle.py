"""
Trabalhando com JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube...) e terceiros (nós desenvolvedores).

import json

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])

# dumps -> formata a informação para ser compatível com o json (fazendo uso de aspas duplas "")

print(type(ret))

print(ret)
________________________________________________________________________________________

import json

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__) # Aspas simples

ret = json.dumps(felix.__dict__) # Aspas duplas

print(ret)
______________________________________________________________________________________

# Integrando o JSON com o Pickle

pip install jsonpickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

ret = jsonpickle.encode(felix)

print(ret)
______________________________________________________________________________________

# Refatorando o processo anterior / Escrevendo o arquivo json/pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
_____________________________________________________________________________________

# Refatorando o processo anterior para realizar a leitura do arquivo json/pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('Seção 17 - Manipulando Arquivos CSV e JSON/felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
"""

# Refatorando o processo anterior para realizar a leitura do arquivo json/pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('Seção 17 - Manipulando Arquivos CSV e JSON/felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
