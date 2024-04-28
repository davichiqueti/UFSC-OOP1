

class Cliente:
    def __init__(self, nome: str, fone: int):
        if (isinstance(nome, str)):
            self.__nome = nome
        if (isinstance(fone, int)):
            self.__fone = fone

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if (isinstance(nome, str)):
            self.__nome = nome

    @property
    def fone(self) -> int:
        return self.__fone

    @fone.setter
    def fone(self, fone: int):
        if (isinstance(fone, int)):
            self.__fone = fone
