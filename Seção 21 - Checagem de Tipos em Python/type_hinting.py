"""
Type Hinting

# Indicação formal de indicar estáticamente o tipo de um dado em uma linguagem onde a Tipagem é Dinâmica

# Python 3.5 - PEP 484

def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'

print(cumprimentar('Geek'))
"""

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

print(cabecalho('geek university', alinhamento='geek'))
