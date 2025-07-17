"""
Modos de Arquivos

r -> Abre para leitura - padrão
w -> Abre para escrita - sobreescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o contúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. (Temos o controle do cursor)

# OBS.: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo 
# será adicionada SEMPRE ao final do arquivo. Com o modo 'a', não controlamos o cursor.

https://docs.python.org/3/library/functions.html#open

# Exemplo x:


with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo.\n')

try:
    with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já existe.')

# Exemplo 'a'

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

# Exemplo r+ (complicado e pouco usual neste formato)

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/outro.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('Novo topo.\n')
    arquivo.write('Nova linha.\n')
    arquivo.write('Outra mais uma linha.\n')

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionada.\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(32)
    arquivo.write('Outra mais uma linha.\n')         
"""

