"""
Escrevendo em arquivos CSV

reader() (leitor) - de forma lógica usando o primeiro teremos também a utilização do segundo -> writer() (escritor)

## writerow() -> Escreve uma linha

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista.

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

# 'w' -> para escrever a primeira vez, toda vez que é executado apaga as informações previamente existentes.
# 'a' -> acrescenta informações sem remover as anteriores. O que faz com que o cabeçalho seja reescrito caso 
não se remova a linha correspondente.

# DictWriter

# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.

from csv import DictWriter

with open('filmes3.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
"""
# DictWriter

# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.

from csv import DictWriter

with open('filmes3.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme =  input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
