"""
Escrevendo em arquivos

# OBS.: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS.: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe apenas uma string como parâmetro, caso contrário teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write (escrita)

# Forma Pythônica

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muita fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Está é a última linha.\n')

# Forma tradicional de escrita em arquivo -> não Pythônica

arquivo = open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.\n')

arquivo.closed()

with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)
"""
with open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
