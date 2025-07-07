"""
Faça um programa que receba dois números inteiros e mostre qual deles é o maior
"""
numero: int = int(input('Informe um número inteiro: '))
numero1: int = int(input('Informe outro número inteiro: '))

if numero > numero1:
    print(f'Entre {numero} e {numero1}, o maior valor é {numero}')
elif numero == numero1:
    print(f'Os números {numero} e {numero1} são iguais')
else:
    print(f'Entre {numero} e {numero1}, o maior valor é {numero1}')