"""
Sistema de Arquivos - Navegação

AULA PRÉVIA:
- Computadores/celulares/tablets -> armazenam conteúdos em arquivos, dentro de diretórios;
    - Os arquivos armazenados podem ser textos, planilhas, imagens vídeos etc.;
    - Estrutura do arquivo: filename.extension (para as pessoas a extension faz a diferença - já para o computador o que varia são os 
    metadados - tamanho, data, tipo, acessos e modificações, resolução etc.);
    - Os arquivos são organizados em diretórios (pastas) - eles se organizam de forma hierarquica (árvore hierarquica);
        - Diretório Raiz (Root Directory) -> é o diretório base/principal;
        - SISTEMA WINDOWS: C:\ (diretório raiz)
        - SISTEMAS POSIX (sistemas operacionais modernos - macOS/Linux): / (diretório raiz) -> cd (para abrir), ls (lista os elementos), 
        tree (forma a árvore de arquivos dentro do diretório), ctrl + c (para a ação)
        - Path -> o caminho do diretório onde ele está armazenado até o arquivo -> no Linux acessa com pwd | cat + path = acessa o conteúdo do arquivo;
        - Path no Windows -> C:\Users\Kenneth\my_next_course.py
        - Path Absoluto -> pega do princípio ao arquivo;
        - Path Relativo -> /home/workspaces/backups/../ -> significa = lista pra mim todo o conteúdo de backups;
        - .. -> move o diretório acima na hierarquia;
        - . -> significa diretório local;
        - cd .. -> volta um diretório no Linux;
        - cp -> copia no Linux;
        - mv -> move no Linux;
-----------------------------------------------------------------------------------------------     

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operation System -> Sistema Operacional;
pwd no Linux -> revela o diretório corrente;

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd()) # Exemplo: /media/sf_Documents/vm/Projects

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd()) # Exemplo: /media/sf_Documents/vm

os.chdir('..')

print(os.getcwd()) # Exemplo: /media/sf_Documents

os.chdir('..')

print(os.getcwd()) # Exemplo: /media

os.chdir('..')

print(os.getcwd()) # Exemplo: /

os.chdir('..')

print(os.getcwd()) # Exemplo: /

# Podemos checar se um diretório é relativo ou absoluto

print(os.path.isabs('/home/geek/')) # True - se for False ele não é absoluto, logo é relativo

# OBS.: Para usuários Windows
# Se você infelizmente estiver utilizando um computador com Widows, 
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users\\geek'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name()) # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional -> Windows não vai
print(os.uname())

# Fazer o import
import sys

print(sys.platform())

# 'home/geek/workspace/sistema'
# mkdir -> no Linux cria o diretório

print(os.getcwd()) # Exemplo: /media/sf_Documents/vm/Project/guppe

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd()) # Exemplo: /media/sf_Documents/vm/Project/guppe/geek/university

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o 
# diretório que será juntado ao atual.

# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir('/etc')) # Não tem no Windows

print(len(os.listdir('/etc')))

print(os.listdir('C:\\')) # Windows

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir() 

arquivos = list(os.scandir('/etc'))

print(arquivos)

print(dir(arquivos[0]))
#_____________________________________________
scanner = os.scandir()

arquivos = list(scanner)

print(arquivos[0].inode()) # Numeração do arquivo na árvore de diretórios
print(arquivos[0].is_dir()) # É um diretório? False
print(arquivos[0].is_file()) # É um arquivo? True
print(arquivos[0].is_symlink()) # É um link simbólico? False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Camiho até o arquivo
print(arquivos[0].stat()) # Estatísticas do arquivo

# OBS.: Quando utilizamos a função sacandir() nós precisamos fechá-la, assim quando abrimos um arquivo

scanner.close()
"""

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir() 

arquivos = list(os.scandir('/etc'))

print(arquivos)

print(dir(arquivos[0]))
#_____________________________________________
scanner = os.scandir()

arquivos = list(scanner)

print(arquivos[0].inode()) # Numeração do arquivo na árvore de diretórios
print(arquivos[0].is_dir()) # É um diretório? False
print(arquivos[0].is_file()) # É um arquivo? True
print(arquivos[0].is_symlink()) # É um link simbólico? False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Camiho até o arquivo
print(arquivos[0].stat()) # Estatísticas do arquivo

# OBS.: Quando utilizamos a função sacandir() nós precisamos fechá-la, assim quando abrimos um arquivo

scanner.close()
