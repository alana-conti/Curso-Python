"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função, onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError


def exponencial(numero, potencia=2): # Informando após o = o parâmetro se torna opcional
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3,2))

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3,5)) # Eleva a potência informada pelo usuário

# OBS.:
# Se o usuário passar apenas um argumento, este será atribuído ao parâmetro número, e será calculado o quadrado desse número;
# Se o usuário passar dois argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao parâmetro potência. Então
# será calculada esta potência.

# OBS.: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(num=2, potencia):
    return num ** potencia

print(teste(6))

# CERTO!

def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) # TypeError
print(soma()) # TypeError

def soma(num1=5, num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma())

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor :
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor!'
    return f'Olá {nome}!'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True)) # Só passar True não daria certo
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Por que utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de códigos;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções etc;
def diz_oi():
    print('Oi ')

variavel = diz_oi

variavel()

# Exemplos

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS.: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof = 'Geek' # Variável local
    return f'Olá {prof}'

print(diz_oi())

print(prof) # NameError

# ATENÇÃO com variáveis globais (se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())

# Ajustado:

total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

print(dentro()) -> é desconhecida fora da função fora
"""
