"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

#OBS: O módulo Pickle não é seguro contra dados maliciosos e deste forma
não é recomendado trabalhar com arquivos pickle vindos de outras pessoas
que você não conheça ou de fontes desconhecidas.

# Fazendo a escrita em arquivos pickle
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')

felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arquivo: # 'wb' -> write, binary -> escrevendo um arquivo binarizado
    pickle.dump((felix, pluto), arquivo)

# Fazer a leitura de dados em arquivos pickle

with open('animais.pickle', 'rb') as arquivo: # 'rb' -> read, binary -> lendo um arquivo binarizado
    gato, cachorro = pickle.load(arquivo) # O load é o carregamento do arquivo, que consiste na sua descompactação
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')

# De arquivos binarizados nós carregamos os objetos em si, não apenas as informações
"""
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')

# Fazer a leitura de dados em arquivos pickle

with open('Seção 17 - Manipulando Arquivos CSV e JSON/animais.pickle', 'rb') as arquivo: # 'rb' -> read, binary -> lendo um arquivo binarizado
    gato, cachorro = pickle.load(arquivo) # O load é o carregamento do arquivo, que consiste na sua descompactação
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')

# De arquivos binarizados nós carregamos os objetos em si, não apenas as informações
