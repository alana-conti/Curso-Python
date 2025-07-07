"""
Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos
valores pares ele possui
"""

# MEU

valor = 0
valores = []
par = 0

while valor < 10:
    print('Informe um valor inteiro: ')
    valor_informado = int(input())
    valor = valor + 1
    valores.append(valor_informado)
    if valor_informado % 2 == 0:
        par = par + 1

print(f'Foram informados os valores: {valores}')

print(f'Dos valores informados {par} são pares')

# PROFESSOR

lista: list[int] = []
contador_pares: int = 0

while len(lista) < 10:
    valor: int = int(input(f'Informe o valor {len(lista) + 1}/10: '))
    lista.append(valor)

    if valor % 2 == 0:
        contador_pares = contador_pares + 1

if contador_pares > 0:
    print(f'A lista {lista} possui {contador_pares} pares.')
else:
    print(f'A lista {lista} não possui valores pares.')