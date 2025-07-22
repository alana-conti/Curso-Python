"""
Tipos de dados mais precisos

-> int, str, float, List, Set, Dict, etc

# def dobro(valor: int) -> int:
#     return valor * 2
# 
# print(dobro(8))
# print(dobro(42))

-> Literal type
-> Union
-> Final
-> Typed dictionaries
-> Protocols

# Literal type -> o programa deve atender Leteralmente aquelas opções

from typing import Literal

def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


# def calcula_v1(operacao: str, num1: int, num2: int) -> None:
#     if operacao == '+':
#         print(f'{num1} + {num2} = {num1 + num2}')
#     elif operacao == '-':
#         print(f'{num1} - {num2} = {num1 - num2}')
#     else:
#         raise ValueError(f'Operação inválida {operacao!r}') # !r -> coloca aquele valor informado no retorno do erro entre aspas simples

def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')

calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
calcula_v2('*', 3, 5)

# Union -> retorno de mais de uma tipagem possível

from typing import Union

def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado

# Final -> usado para criar constantes

from typing import Final

NOME: Final = 'Geek'

print(NOME)

NOME = 'University'

print(NOME)

# final -> um decorador para classes ou métodos que não permite estendê-los e/ou sobreescrevê-los, respectivamente

from typing import final

@final
class Pessoa:
    pass


class Estudante():
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando...')

# Typed Dictionaries -> dicionário tipado, onde se criam os atributos que serão as chaves do dicionário já com as suas tipagens

from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int

geek = CursoPython(versao='3.8.5', atualizacao=2020)

print(geek)

outro = CursoPython(algo='vai', coisa=True)

print(outro)

# Protocols -> o protocolo é como uma regra (PEP 544)

from typing import Protocol


class Curso(Protocol): # Todo objeto que seguir esse protocolo, terá o atributo titulo. ATENÇÃO! Protocolos não podem ser inicializados (__init__)
    titulo: str

def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Oi'

v1 = Venda()
# c1 = Curso()

# estudar(c1)
estudar(v1)
"""

# Protocol -> o protocolo é como uma regra (PEP 544)

from typing import Protocol


class Curso(Protocol): # Todo objeto que seguir esse protocolo, terá o atributo titulo. ATENÇÃO! Protocolos não podem ser inicializados (__init__)
    titulo: str

def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Oi'

v1 = Venda()
# c1 = Curso()

# estudar(c1)
estudar(v1)
