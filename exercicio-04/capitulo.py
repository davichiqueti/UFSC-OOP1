

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
    def numero(self, numero: int):
        if not (isinstance(numero, int)):
            raise TypeError('Capitulo.numero deve ser um inteiro')
        self.__numero = numero

    @titulo.setter
    def titulo(self, titulo: str):
        if not (isinstance(titulo, str)):
            raise TypeError('Capitulo.titulo deve ser uma string')
        self.__titulo = titulo
