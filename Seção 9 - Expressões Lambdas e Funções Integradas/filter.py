"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS.: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))

print(f'Novamente: {list(res)}')

# OBS.: Assim como na função mao(), após serem utilizados os dados de filter() eles são excluídos da memória.

# Remoção de dados faltantes

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

# Por lambda

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)
                    OU
res = filter(lambda pais: pais != '', paises)

print(list(res))

# Na comparação booleana o 0 é considerado False

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável. - retorna cada um dos dados

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função. - retorna True ou False - e com base nisso filtra

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

print(usuarios)

# Filtrar os usuários que estão inativos no twitter

# Forma 1

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativos)

# Forma 2

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

# Combinas filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo "Sua instrutora é" + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
"""

# Combinas filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo "Sua instrutora é" + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)