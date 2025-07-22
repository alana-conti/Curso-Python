"""
Checagem de Tipos com MyPy

-> https://mypy-lang.org
# MyPy -> nasceu para ser uma nova linguagem de programação, com o tempo foi reescrito para ser um 
checador de tipos da linguagem Python oficial.
-> Ele trabalha em conjunto com o Type Hinting

PARA UTILIZAR:
- no terminal:
    mypy nome_do_arquivo.py

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

print(cabecalho('geek university', alinhamento=True))
"""

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

print(cabecalho('geek university', alinhamento=True))

cabecalho(texto='4', alinhamento=True)
