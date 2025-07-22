"""
Manipulando data e hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

2025-07-21 23:17:41.331420

2025-07-21 23:22:41.331420

import datetime

print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

## Métodos presentes na CLASSE datetime

# Retorna a data e hora corrente
print(datetime.datetime.now())

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
# datetime.datetime(2025, 7, 21, 23, 19, 21, 905926)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minuto, 0 segund, 0 microsegundo
inicio = inicio.replace(year=2023, hour=20, minute=0, second=0, microsecond=0)

print(inicio)
_____________________________________________________________________________________________________

import datetime

evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))

print(type('31/12/2018'))

print(evento)

# Recebendo dados do usuário e convertendo para data

nascimento = input('Informe sua data de nascimento (dd/mm/yyy): ')

print(nascimento)

print(type(nascimento))

nascimento = nascimento.split('/')

print(nascimento)

print(type(nascimento))

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
_____________________________________________________________________________________________________

import datetime

evento = datetime.datetime.now()

# Acessa individual dos elementos de data e hora

print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo

print(dir(evento)) # O que mais podemos fazer??
"""

import datetime

evento = datetime.datetime.now()

# Acessa individual dos elementos de data e hora

print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo

print(dir(evento)) # O que mais podemos fazer??
