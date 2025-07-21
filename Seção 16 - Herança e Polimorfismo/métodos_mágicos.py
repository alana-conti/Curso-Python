"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

# dunder init -> __init__()
def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

Dunder > Double Underscore

# dunder repr -> Representação do objeto
## Esse método sobreescrito da classe Object, faz a representação do nosso objeto
def __repr__(self):
    return f'{self.titulo} escrito por {self.autor}'
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self): # Dunde string - tem preferência entre os métodos de representação
        return self.titulo
    
    def __len__(self): # Número de páginas, ou do título: len(self.titulo)
        return self.paginas

    def __del__(self): # Deleta o elemento e informa a ação realizada
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro): # Representação via método da adição -> realiza a concatenação dos elementos
        return f'{self} - {outro}'
    
    # dir(__builtins__) -> mostra os métodos disponíveis para implementação
    
    def __mul__(self, outro): # Responsável por alterar e tornar possível a realização da multiplicação
        if isinstance(outro, int): # Outro deve ser um número, por isso a verificação.
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)

print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 5)
