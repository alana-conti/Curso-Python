"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS.: O contrário não é verdadeiro. Ouseja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferença entre Funções e Generator Functions (Funções Geradoras)

----------------------------------------------------------------------------------------
| Funções                                    | Generator Functions                     |
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
| utilizan return                            | utilizam yield                          |
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
| retorna uma vez                            | podem utilizar yield múltiplas vezes    |
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
| quando executada, retorna um valor         | quando executada, retorna um generator  |
----------------------------------------------------------------------------------------

gen = conta_ate(5)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)

for num in gen:
    print(num)

gen = conta_ate(10)

print(next(gen)) # 1

print('Geek')

for num in gen: 
    print(num) # 2    
"""

# Exemplo de Generator Funtion (Função Geradora)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador # Fica aguardando um next()
        contador = contador + 1

# OBS.: Uma Generator Function não é um Generator. Ela gera um generator, ok?

gen = list(conta_ate(10))

print(gen)
