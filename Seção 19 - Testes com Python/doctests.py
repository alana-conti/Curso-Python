"""
Doctests -> Testes dentro da documentação

Doctests são testes que colocamos na docstring das funções/métodos Python.

def soma(a, b):
    # soma os números a e b

    #>>> soma(1, 2)
    #3

    #>>> soma(4, 6)
    #10
    #
    return a + b

# OBS.: No pycharm ele vai executar como teste.

# Para rodar um test do doctest (no terminar):
   # python -m doctest -v doctests.py

print(soma(3, 4)) # 7

# Saída

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

# Outro Exemplo, Aplicando o TDD

def duplicar(valores):
    #duplica os valores em uma lista
    
    #>>> duplicar([1, 2, 3, 4])
    #[2, 4, 6, 8]

    #>>> duplicar([])
    #[]

    #>>> duplicar(['a', 'b', 'c'])
    #['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    #Traceback (most recent call last):
    #   ...
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    #
    return [2 * elemento for elemento in valores]

# Erro inesperado...

OBS: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.

def fala_oi():
    #Fala oi

    #>>> fala_oi()
    #'oi' (precisa estar com aspas simples)
    #
    return "oi"

# Um último caso estranho...
# O Sublime Text -> mostra o problema que pode haver no teste abaixo por conta dos espaços extras que fazem falhar em alguns cenários

#def verdade():
    #Retorna verdade

    #>>> verdade()
    #True
    #
    return True

"""

# Um último caso estranho...
# O Sublime Text -> mostra o problema que pode haver no teste abaixo por conta dos espaços extras que fazem falhar em alguns cenários

def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
