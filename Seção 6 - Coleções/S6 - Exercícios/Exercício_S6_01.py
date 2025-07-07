"""
Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida
mostre na tela os valores lidos.
"""

# MEU

valor = 0
valores = []

while valor < 6:
    print('Informe um valor inteiro: ')
    valor_informado = int(input())
    valor = valor + 1
    valores.append(valor_informado)

print(valores)

# PROFESSOR

lista: list[int] = []

while len(lista) < 6:
    valor: int = int(input(f'Informe o valor {len(lista) + 1}/6: '))
    lista.append(valor)

for valor in lista:
    print(valor)