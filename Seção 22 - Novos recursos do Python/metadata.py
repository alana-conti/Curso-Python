"""
Metadata
"""
from importlib import metadata

print(metadata.version('pip')) # Vê a versão de qualquer pacote instalado

metadados_pip = metadata.metadata('pip') # Quais os metadados disponíveis em um pacote

print((metadados_pip))

print(list(metadados_pip))

print(metadados_pip['Project-URL'])

print(len(metadata.files('pip'))) # Pode verificar a quantia de arquivos em um pacote

print(metadata.requires('django')) # Quais outros pacotes o pacote em questão requer | é uma forma de lidar com conflito de bibliotecas
