"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e 
setters para os atributos e um método para imprimir os dados de uma pessoa
"""

from datetime import date

class Pessoa:
    def __init__(self, nome: str, datanscm: date, email: str) -> None:
        self.__nome: str = nome
        self.__datanscm: date = datanscm
        self.__email: str = email

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome + nome

    @property
    def datanscm(self) -> date:
        return self.__datanscm

    @nome.setter
    def datanscm(self, datanscm: date) -> None:
        self.__datanscm + datanscm

    @property
    def email(self) -> str:
        return self.__email

    @nome.setter
    def email(self, email: str) -> None:
        self.__email + email
    
    def imprimir(self) -> None:
        print('DADOS DO INDIVÍDUO:')
        print(f'Nome: {self.__nome}\nData de Nascimento: {self.__datanscm.strftime('%d/%m/%Y')}\nE-mail: {self.__email}')

if __name__ == '__main__':
    p: Pessoa = Pessoa('Felicity Jones', date(1987, 7, 22), 'angelina@gmail.com')
    
    p.imprimir()



