"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o args?

O parâmetro args utilizado em uma função, coloca os valores extras informados como
entradas em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

# Entendendo o args

def soma_todos_numeros(*args):
    print(args)

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(2, 3)
soma_todos_numeros(2, 3, 4)
soma_todos_numeros(3, 4, 5, 6)

# Efetuando a soma -> Primeira forma

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

# Efetuando a soma -> Segunda forma

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

# print(soma_todos_numeros('a')) -> Não funciona por conta da soma

print(soma_todos_numeros(23.4, 12.5))

# Pode-se acrescentar mais parâmetros além do *args

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3, 4))
print(soma_todos_numeros('Angelina', 'Jolie', 3, 4, 5, 6))

print(soma_todos_numeros('Angelina', 'Jolie', 23.4, 12.5))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza de quem você é...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))


def soma_todos_numeros(*args):
    print(args)
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# print(soma_todos_numeros(numeros)) TypeError

# Desempacotador (*)

print(soma_todos_numeros(*numeros))

# OBS.: O asterisco serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar esses dados.
"""

def soma_todos_numeros(*args):
    print(args)
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# print(soma_todos_numeros(numeros)) TypeError

# Desempacotador (*)

print(soma_todos_numeros(*numeros))

# OBS.: O asterisco serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar esses dados.
