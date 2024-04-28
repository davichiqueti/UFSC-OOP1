

class Editora:
    def __init__(self, codigo: int, nome: str) -> None:
        self.__codigo = codigo
        self.__nome = nome

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @codigo.setter
    def codigo(self, value: int):
        if not (isinstance(value, int)):
            raise TypeError("Editora.codigo deve ser um inteiro")
        self.__codigo = value

    @nome.setter
    def nome(self, value: str):
        if not (isinstance(value, str)):
            raise TypeError("Editora.nome deve ser uma string")
        self.__nome = value
