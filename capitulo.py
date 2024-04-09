

class Capitulo:
    def __init__(self, numero: int, titulo: str) -> None:
        self.__numero = numero
        self.__titulo = titulo

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def titulo(self) -> str:
        return self.__titulo

    @numero.setter
    def numero(self, value: int):
        if not (isinstance(value, int)):
            raise TypeError("Capitulo.numero deve ser um inteiro")
        self.__numero = value

    @titulo.setter
    def titulo(self, value: str):
        if not (isinstance(value, str)):
            raise TypeError("Capitulo.titulo deve ser uma string")
        self.__titulo = value
