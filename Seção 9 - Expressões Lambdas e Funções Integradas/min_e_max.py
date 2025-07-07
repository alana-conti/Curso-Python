"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129] # Não importa se é lista, set, tupla ...
print(max(lista)) # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla)) # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto)) # 129

dicionario = {'a': 1,'b': 8,'c': 4,'d': 99,'e': 34,'f': 129}
print(max(dicionario)) # f
print(max(dicionario.values())) # 129

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.789))

print(max('Geek University'))

min() -> Retorna o menor valor em um iterável ou o menor valor de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129] # Não importa se é lista, set, tupla ...
print(min(lista)) # 1

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla)) # 1

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto)) # 1

dicionario = {'a': 1,'b': 8,'c': 4,'d': 99,'e': 34,'f': 129}
print(min(dicionario)) # a
print(min(dicionario.values())) # 1

# Faça um programa que receba dois valores do usuário e mostre o menor
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print(min('Geek University'))

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes)) # Tim

print(min(nomes)) # Arya

print(max(nomes, key=lambda nome: len(nome))) # Ollivander

print(min(nomes, key=lambda nome: len(nome))) # Tim

musicas = [
    {"título": "Thunderstruck", "tocou": 3},
    {"título": "Dead Skin Mask", "tocou": 2},
    {"título": "Black in Black", "tocou": 4},
    {"título": "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio: Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['título'])
print(min(musicas, key=lambda musica: musica['tocou'])['título'])

# Desafio: Como encontrar a música mais e menos tocada, sem usar max, min e lambda

max = 0
min = 999999
mais_tocada = None
menos_tocada = None

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
        mais_tocada = musica

    if musica['tocou'] < min:
        min = musica['tocou']
        menos_tocada = musica


print(f'A música mais tocada é: {mais_tocada["título"]}')

print(f'A música menos tocada é: {menos_tocada["título"]}')
"""

musicas = [
    {"título": "Thunderstruck", "tocou": 3},
    {"título": "Dead Skin Mask", "tocou": 2},
    {"título": "Black in Black", "tocou": 4},
    {"título": "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio: Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['título'])
print(min(musicas, key=lambda musica: musica['tocou'])['título'])

# Desafio: Como encontrar a música mais e menos tocada, sem usar max, min e lambda

max = 0
min = 999999
mais_tocada = None
menos_tocada = None

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
        mais_tocada = musica

    if musica['tocou'] < min:
        min = musica['tocou']
        menos_tocada = musica


print(f'A música mais tocada é: {mais_tocada["título"]}')

print(f'A música menos tocada é: {menos_tocada["título"]}')

