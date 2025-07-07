"""
Any e All

all() -> retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiros? False

print(all([1, 2, 3, 4])) # Todos os números são verdadeiros? True

print(all([])) # Todos os números são verdadeiros? True

print(all((1, 2, 3, 4))) # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cristiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

# OBS.: Um iterável vazio convertido em booloean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

any() -> Retorna True ou False, se qualquer valor do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

# Exemplos

print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, (), []])) # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cristiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])) # True

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
"""

print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, (), []])) # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cristiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])) # True

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))