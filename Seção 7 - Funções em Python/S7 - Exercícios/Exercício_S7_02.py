"""
Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 2024”.
"""

# MEU

def calendario(data):
    data_fracionada = data.split('/')
    meses = {'01': "janeiro", '02': "fevereiro", '03': "março", '04': "abril",
            '05': "maio", '06': "junho", '07': "julho", '08': "agosto",
            '09': "setembro", '10': "outubro", '11': "novembro", '12': "dezembro"}
    return f"{data_fracionada[0]} de {meses[data_fracionada[1]]} de {data_fracionada[2]}."

print(calendario('01/01/2024'))
print(calendario('06/04/2000'))
print(calendario('06/07/2024'))
print(calendario('07/02/2003'))

# PROFESSOR

def data_por_extenso(data: str) -> None:
    d = data.split('/')

    dia: int = int(d[0])
    mes: int = int(d[1])
    ano: int = int(d[2])

    if mes == 1:
        mes_str = 'janeiro'
    elif mes == 2:
        mes_str = 'fevereiro'
    elif mes == 3:
        mes_str = 'março'
    elif mes == 4:
        mes_str = 'abril'
    elif mes == 5:
        mes_str = 'maio'
    elif mes == 6:
        mes_str = 'junho'
    elif mes == 7:
        mes_str = 'julho'
    elif mes == 8:
        mes_str = 'agosto'
    elif mes == 9:
        mes_str = 'setembro'
    elif mes == 10:
        mes_str = 'outubro'
    elif mes == 11:
        mes_str = 'novembro'
    elif mes == 12:
        mes_str = 'fevereiro'
    else:
        mes_str = 'desconhecido'

    print(f"{dia} de {mes_str} de {ano}.")

if __name__ == '__main__':
    data_por_extenso('01/01/2024')