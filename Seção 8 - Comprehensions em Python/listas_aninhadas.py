"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação, possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (matrizes);

Em Python nós temos as Listas

numeros = [1, 'b', 3.234, True, 5]

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0])
print(listas[0][1]) # 2
print(listas[2][1]) # 8

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehensions

[[print(valor) for valor in lista] for lista in listas]

# Outros Exemplos

# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

#                    colunas               linhas
print([['*' for i in range(1, 4)] for j in range(1, 4)])
"""

# Outros Exemplos

# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

#                    colunas               linhas
print([['*' for i in range(1, 4)] for j in range(1, 4)])