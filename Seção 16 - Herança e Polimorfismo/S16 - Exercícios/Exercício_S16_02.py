"""
 2. Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e 
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do 
veículo de forma a apresentar também a quantidade de portas do carro.
"""

# Meu:
from Exercício_S16_01 import Veiculo

class Carro(Veiculo):

    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo)
        self.__portas: int = portas
    
    @property
    def portas(self) -> int:
        return self.__portas
    
    @portas.setter
    def portas(self, portas: int) -> None:
        self.__portas = portas
    
    def imprimir(self) -> None:
        return f'| MARCA: {self.marca} | MODELO: {self.modelo} | PORTAS: {self.portas} |'


# Professor:
from Exercício_S16_01 import Veiculo

class Carro(Veiculo):

    def __init__(self, portas: int, marca: str, modelo: str) -> None:
        super().__init__(marca, modelo)
        self.__portas: int = portas

    @property
    def portas(self) -> int:
        return self.__portas

    @portas.setter
    def portas(self, portas: int) -> None:
        self.__portas = portas

    def imprimir(self) -> None:
        super().imprimir()
        print(f'Portas: {self.portas}')
