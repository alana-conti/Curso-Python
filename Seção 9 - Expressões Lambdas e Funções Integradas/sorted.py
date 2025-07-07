"""
Sorted

OBS.: Apessar do nome não confunda com a função sort() que já estudamos em Listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome já diz, sorted() serve para ordenar.

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # Ordena do menor para o maior

print(numeros)

# sort() modifica a lista - sorted() gera uma nova ordenada

numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))

# OBS.: O sorted() sempre retorna uma lista com os elementos do iterável ordenados.

# Exemplo 2

numeros = [6, 1, 8, 2]
print(numeros)

print(tuple(sorted(numeros)))

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], 'cor': 'amarelo'},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], 'cor': 'preto', 'musica': 'rock'},
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

# Último exemplo

musicas = [
    {'título': "Thunderstruck", "tocou": 3},
    {'título': "Dead Skin Mask", "tocou": 2},
    {'título': "Black in Black", "tocou": 4},
    {'título': "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))
"""

# Último exemplo

musicas = [
    {'título': "Thunderstruck", "tocou": 3},
    {'título': "Dead Skin Mask", "tocou": 2},
    {'título': "Black in Black", "tocou": 4},
    {'título': "Too old to rock'in'roll, too ynoung to die", "tocou": 32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))
