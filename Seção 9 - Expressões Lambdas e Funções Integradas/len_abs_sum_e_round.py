"""
Len, Abs, Sum e Round

# Len

len() -> retorna o tamanho (ou seja, o número de itens) de um iterável.

# Exemplo

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len
print('Geek University'.__len__())

# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplos Abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

print(abs('geek')) -> NÃO FUNCIONA COM STRING

# Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial.

# OBS.: O valor inicial default = 0


# Exemplos Sum

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.145, 5.678]))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}.values()))

print(sum('Geek University', 'x')) # Não funciona com strings

# Round

round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for
informada retorna o inteiro mais o próximo da entrada

# Exemplos Round

print(round(10.2))

print(round(10.5)) # Até aqui arredonda pra baixo

print(round(10.6))

print(round(1.21212121, 2))

print(round(1.2199999, 2))
"""

# Exemplos Round

print(round(10.2))

print(round(10.5)) # Até aqui arredonda pra baixo

print(round(10.6))

print(round(1.21212121, 2))

print(round(1.2199999, 2))

