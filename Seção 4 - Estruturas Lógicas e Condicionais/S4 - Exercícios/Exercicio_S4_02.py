"""
Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido
"""

from math import sqrt

numero: int = int(input('Informe um número inteiro: '))

if numero >= 0:
    raiz = numero ** 0.5
    print(f'O número {numero} é positivo e sua raíz quadrada é {raiz}')
else:
    print(f'O valor {numero} é inválido')

if numero >= 0:
    print(f'O número {numero} é positivo e sua raíz quadrada é {sqrt(numero)}')
else:
    print(f'O valor {numero} é inválido')