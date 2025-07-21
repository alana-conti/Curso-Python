"""
 3. Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.
"""

# Meu: 

from Exercício_S16_02 import Carro

if __name__ == '__main__':

    carro: Carro = Carro(marca='Fiat', modelo='Punto - 2016', portas=4)

    Carro.imprimir()

# Professor:

from Exercício_S16_02 import Carro


if __name__ == '__main__':
    carro: Carro = Carro(marca='Honda', modelo='Fit', portas=4)

    carro.imprimir()
