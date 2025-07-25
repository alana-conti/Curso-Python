"""
Trabalhando com deltas de data e hora (diferença entre início e fim)

data_inicial = dd/mm/yyyy 12:55:34.9939329
data_final  =  dd/mm/yyyy 13:34.23.0948484

delta = data_final - data_inicial
___________________________________________________________________________________________________________________________________

import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2026, 3, 3, 0)

# calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas...') # // -> retorna a divisão inteira
___________________________________________________________________________________________________________________________________

# Adicionando dias -> exemplo do boleto

import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3) # Utiliza a classe

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
"""
# Adicionando dias -> exemplo do boleto

import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3) # Utiliza a classe

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
