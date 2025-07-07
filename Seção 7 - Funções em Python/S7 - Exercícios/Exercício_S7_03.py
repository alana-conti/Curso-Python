"""
 Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""

# MEU

def maior_valor(*args):
    return f"O maior valor da lista é {max(args)}."

numero = (3, 5, 6, 4, 8, 23, 54, 23, 42, 24, 61)

print(maior_valor(*numero))

# PROFESSOR

def maior(inteiros: list[int]):
    return max(inteiros)

if __name__ == '__main__':
    lista: list[int] = [2, 5, 1, 0, 89, 23]
    print(f'O maior valor na lista {lista} é {maior(lista)}')
