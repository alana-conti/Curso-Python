"""
Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles
"""

valor1: int = int(input('Informe o primeiro valor inteiro: '))
valor2: int = int(input('Informe o segundo valor inteiro: '))
valor3: int = int(input('Informe o terceiro valor inteiro: '))

soma: int = (valor1 + valor2 + valor3)

print(f'A soma dos valores {valor1} com {valor2} e {valor3} é {soma}.')