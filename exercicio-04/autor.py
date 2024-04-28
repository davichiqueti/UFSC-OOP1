

class Autor:
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
    def codigo(self, codigo: int):
        if not (isinstance(codigo, int)):
            raise TypeError('Autor.codigo deve ser um inteiro')
        self.__codigo = codigo

    @nome.setter
    def nome(self, nome: str):
        if not (isinstance(nome, str)):
            raise TypeError('Autor.nome deve ser uma string')
        self.__nome = nome
