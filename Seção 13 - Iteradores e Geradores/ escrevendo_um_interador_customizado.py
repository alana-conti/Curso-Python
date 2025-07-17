"""
 Escrevendo um Interador Customizado

 - __init__ : função especial chamada de construtor -> responsável por criar um objeto.
 - self.menor = menor | self.maior = maior -> dentro de um objeto são métodos.

Para criar um iterador basta que você tenha declarado as classes __init__ e __next__
"""

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    def __iter__(self):
        return self
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

con = Contador(1, 6)

print(con.menor)
print(con.maior)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

for n in Contador(1, 61):
    print(n)

for n in range(1, 61):
    print(n)
