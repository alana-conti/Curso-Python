"""
Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.
"""

# MEU

def dobro(num1: int):
    print(f"O dobro de {num1} é {num1 * 2}")

dobro(2)
dobro(3)
dobro(4)

# PROFESSOR

def dobro(numero: int) -> int:
    return numero * 2

if __name__ == '__main__':
    valor: int = 4
    print(f"O dobro de {valor} é {dobro(valor)}")