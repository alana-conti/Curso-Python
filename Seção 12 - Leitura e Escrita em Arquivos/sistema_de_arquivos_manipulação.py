"""
Sistema de Arquivos - Manipulação

import os

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('text.txt')) # False
print(os.path.exists('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/text.txt')) # True

# Diretório

# Paths - relativos
print(os.path.exists('geek')) # False

# Paths - absolutos
print(os.path.exists('/workspaces')) # True
print(os.path.exists('/workspaces/Curso-Python')) # True

# Criando arquivos

# Forma 1
open('arquivo-test.txt', 'w').close()

# Forma 2
open('arquivo-test2.txt', 'a').close()

# Forma 3
with open('arquivo-test3.txt', 'w') as arquivo:
    pass
    
# Criando arquivos da forma mais adequada

os.mknod('arquivo-teste4,txt')

os.mknod('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/university.txt')

# OBS.: Se você estiver utilizando no MacOS, pove haver um erro de PermissionError

# OBS.: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

# Criando diretórios - únicos (um a um)

# Path Relativo
os.mkdir('templates')

# Path Absoluto
os.mkdir('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/templates')

# OBS.: A função mkdir() cria um diretório se esse não existir. Caso exista, teremos FileExistsError

os.mkdir('/etc/template')

# OBS.: Se não tivermos permissão para criar o diretório teremos um PermissionError

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates/geek/university')

# OBS.: Se já existir, teremos um FileExistsError

os.makedirs('templates2/novo2/outro2', exist_ok=True) # Se existir ignore

# Renomear arquivos e diretórios

# Diretórios
os.rename('templates2', 'geek2')

# OBS.: Se o diretório não existir teremos um FileNotFoundError

# OBS.: Se o diretório que queremos renomear não estiver vazio teremos um OSError

# Arquivos
os.rename('/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/teste.txt', '/workspaces/Curso-Python/Seção 12 - Leitura e Escrita em Arquivos/geek.txt')

# Como deletar arquivos
# ATENÇÃO! Tome cuidado com os comando de deleção. Ao deletarmos um arquivo ou diretório, eles 
# não vão para a lixeira. Eles somem.

os.remove('geek.txt')

# OBS.: Se você estiver no Windows w o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS.: Caso o arquivo não exista teremos o FileNotFoundError

# OBS.: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Como deletar diretórios vazios

os.rmdir('templates')

# OBS.: Se o diretório tiver qualquer conteúdo teremos um OSError

# OBS.: Caso o diretório não exista teremos o FileNotFoundError

---touch: comando do sistema posix (Linux/MacOS) que serve para criar arquivos

# Removendo uma árvore de arquivos
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios

os.removedirs('geek2/mais')

# OBS.: Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!


# Para mandar algo para a lixeira precisamos instalar uma biblioteca (pip install send2trash - talvez precise instalar primeiro: sudo apt-get install lsb-core)

# Importando a biblioteca send2trash (envia arquivos e diretórios para a lixeira)

from send2trash import send2trash

os.remove('cesta1.txt') # Não vai para a lixeira. É deletado imediatamente.

send2trash('cesta2.txt') # Vai pra lixeira. Pode ser restaurado.

# OBS.: Se o arquivo não existir teremos OSError.

send2trash('teste')

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}.')
    with open(os.path.join(tmp, 'arquivo_temporario.txt', 'w')) as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando 
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos 
# os arquivos temporários 'vivos' dentro dos blocos with.

# OBS.: possivelmente, o código acima não irá funcionar se você estiver utilizando 
# o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos temporários.

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS.: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b''

# Sem o bloco With

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()