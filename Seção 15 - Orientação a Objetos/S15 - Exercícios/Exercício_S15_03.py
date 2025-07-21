"""
3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de 
forma que:
a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também 
permitir que seja informado um número de canal para efetuar a troca.
"""

# MEU

class Televisao:

    def __init__(self, status: str, volume: int, canal: int) -> None:
        self.__status: str = status
        self.__volume: int = volume
        self.__canal: int = canal

    def ligar(self) -> None:
        self.__status = 'Ligada'
    
    def desligar(self) -> None:
        self.__status = 'Desligada'
    
    def aumentar_volume(self) -> None:
        self.__volume += 1
    
    def diminuir_volume(self) -> None:
        self.__volume -= 1

    def aumentar_canal(self) -> None:
        self.__canal += 1
    
    def diminuir_canal(self) -> None:
        self.__canal -= 1

    @property
    def canal(self) -> int:
        return self.__canal 

    @canal.setter
    def canal(self, canal: int) -> None:
        self.__canal = canal
    
    def dados_tv(self) -> None:
        print(f"Status: {self.__status}")
        print(f"Canal: {self.__canal}")
        print(f"Volume: {self.__volume}")


class ControleRemoto:
    
    def __init__(self, televisao: Televisao):
        self.__televisao: Televisao = televisao
    
    def ligar(self):
        self.__televisao.ligar()
    
    def desligar(self):
        self.__televisao.desligar()

    def aumentar_volume(self):
        self.__televisao.aumentar_volume()
    
    def diminuir_volume(self):
        self.__televisao.diminuir_volume()

    def aumentar_canal(self):
        self.__televisao.aumentar_canal()
    
    def diminuir_canal(self):
        self.__televisao.diminuir_canal()

    def escolher_canal(self, canal: int):
        self.__televisao.canal = canal

if __name__ == '__main__':
    tv_sala = Televisao('Desligada', 10, 10)
    controle_remoto = ControleRemoto(tv_sala)

    Televisao.dados_tv(tv_sala)
    print('__________________')

    controle_remoto.ligar()

    Televisao.dados_tv(tv_sala)
    print('__________________')

    controle_remoto.escolher_canal(15)

    Televisao.dados_tv(tv_sala)
    print('__________________')
    
    controle_remoto.aumentar_volume()

    Televisao.dados_tv(tv_sala)
    print('__________________')

    controle_remoto.aumentar_canal()

    Televisao.dados_tv(tv_sala)
    print('__________________')

    controle_remoto.diminuir_volume()

    Televisao.dados_tv(tv_sala)
    print('__________________')

    controle_remoto.diminuir_canal()

    Televisao.dados_tv(tv_sala)
    print('__________________')

    controle_remoto.desligar()

    Televisao.dados_tv(tv_sala)
    print('__________________')

# Professor

class Televisao:
    def __init__(self):
        self.__status: bool = False
        self.__volume: int = 0
        self.__canal: int = 0

    @property
    def status(self) -> bool:
        return self.__status
    
    @status.setter
    def status(self, status: bool) -> None:
        return self.__status == status

    @property
    def volume(self) -> int:
        return self.__volume
    
    @volume.setter
    def volume(self, volume: int) -> None:
        return self.__volume == volume

    @property
    def canal(self) -> int:
        return self.__canal
    
    @canal.setter
    def canal(self, canal: int) -> None:
        return self.__canal == canal
    
    def ligar_desligar(self) -> None:
        self.status = not self.status

        if self.status:
            print(f"Status da TV: Ligada")
        else:
            print(f"Status da TV: Desligada")

    def aumentar_volume(self) -> None:
        self.volume = self.volume + 1
        print(f"Volume da TV +: {self.volume}")

    def diminuir_volume(self) -> None:
        self.volume = self.volume - 1
        print(f"Volume da TV -: {self.volume}")

    def aumentar_canal(self) -> None:
        self.canal = self.canal + 1
        print(f"Canal da TV +: {self.canal}")

    def diminuir_canal(self) -> None:
        self.canal = self.canal - 1
        print(f"Canal da TV -: {self.canal}")

    def mudar_canal(self, canal: int) -> None:
        self.canal = canal
        print(f"Canal da TV ++: {self.canal}")

class ControleRemoto:

    def __init__(self, televisao: Televisao) -> None:
        self.__televisao: Televisao = televisao

    @property
    def televisao(self):
        return self.__televisao

    def ligar_desligar(self):
        self.televisao.ligar_desligar()

    def aumentar_volume(self) -> None:
        self.televisao.aumentar_volume()

    def diminuir_volume(self) -> None:
        self.televisao.diminuir_volume()

    def aumentar_canal(self) -> None:
        self.televisao.aumentar_canal()

    def diminuir_canal(self) -> None:
        self.televisao.diminuir_canal()

    def mudar_canal(self, canal: int) -> None:
        self.televisao.mudar_canal(canal)

if __name__ == '__main__':
    tv: Televisao = Televisao()

    tv.ligar_desligar()

    tv.aumentar_canal()
    tv.aumentar_canal()
    tv.aumentar_canal()

    tv.mudar_canal(42)

    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()

    tv.diminuir_canal()
    tv.diminuir_volume()

    tv.ligar_desligar()

    cr: ControleRemoto = ControleRemoto(tv)

    cr.ligar_desligar()

    cr.aumentar_canal()
    cr.aumentar_canal()
    cr.aumentar_canal()

    cr.mudar_canal(42)

    cr.aumentar_volume()
    cr.aumentar_volume()
    cr.aumentar_volume()

    cr.diminuir_canal()
    cr.diminuir_volume()

    cr.ligar_desligar()
