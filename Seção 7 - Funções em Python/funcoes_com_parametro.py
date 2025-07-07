"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função já sabemos que temos funções que :
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada, mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída;

# A função abaixo possui entrada e saída sempre igual

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

# Refatorando a função - recebe um parâmetro de entrada, sem ele NÃO funciona

def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado()) # TypeError

# Exemplo 2

def cantar_parabens():
    print('Parabêns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


# Refatorando a função

def cantar_parabens(aniversariante):
    print('Parabêns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')

cantar_parabens('Patricia')

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplos

def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2,5))
print(soma(10,20))

print(multiplica(4,5))
print(multiplica(2,8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS.: Se a gente informar um número errado de parâmetros ou argumentos, teremos TypeError

print(soma(2, 3, 4)) # TypeError - Passando argumentos a mais
print(soma(4)) # TypeError - Passando argumentos a menos

# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos Parâmetros importa

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(nome, sobrenome))
print(nome_completo(sobrenome, nome)) # Como eu inverti aqui, saí também invertido

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcía'))

# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

# O return finaliza a função, então CUIDADO COM O SEU POSICIONAMENTO

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))
"""

# Erro comum na utilização do return

def soma_impares(numeros):
    """
    Função que realiza a soma de números ímpares informados.
    :param numeros: Números que se desejam somar caso sejam ímpares.
    :return: Retorna a soma dos 'numeros' ímpares identificados.
    """
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

# O return finaliza a função, então CUIDADO COM O SEU POSICIONAMENTO

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))