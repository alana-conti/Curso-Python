"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o sofware precisa 
ter permissão:
    - Permissão de Leitura: Para ler o arquivo.
    - Permissão de Escrita: Para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)
# arquivo = open('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/arquivo.txt', 'x')

# Agora tendo o arquivo podemos utilizar tudo que já temos
print(arquivo.read())

arquivo.write(' Outro texto.')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())