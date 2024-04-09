from autor import Autor
from editora import Editora
from capitulo import Capitulo


class Livro:
    def __init__(
        self,
        codigo: int,
        titulo: str,
        ano: int,
        editora: Editora,
        autor: Autor,
        numero_capitulo: int,
        titulo_capitulo: str
    ):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        capitulo = Capitulo(numero_capitulo, titulo_capitulo)
        self.__capitulos = [capitulo]

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def ano(self) -> int:
        return self.__ano

    @property
    def editora(self) -> Editora:
        return self.__editora

    @property
    def autores(self) -> list[Autor]:
        return self.__autores

    @property
    def capitulos(self) -> list[Capitulo]:
        return self.__capitulos

    @codigo.setter
    def codigo(self, value:int):
        if not (isinstance(value, int)):
            raise TypeError("Livro.codigo deve ser um inteiro")
        self.__codigo = value

    @titulo.setter
    def titulo(self, value: str):
        if not (isinstance(value, str)):
            raise TypeError("Livro.titulo deve ser uma string")
        self.__titulo = value

    @ano.setter
    def ano(self, value:int):
        if not (isinstance(value, int)):
            raise TypeError("Livro.ano deve ser um inteiro")
        self.__ano = value

    @editora.setter
    def editora(self, value: str):
        if not (isinstance(value, Editora)):
            raise TypeError("Livro.editora deve ser objeto da classe Autor")
        self.__editora = value

    def incluir_autor(self, autor: Autor):
        if not (isinstance(autor, int)):
            raise TypeError("Livro.autores só pode incluir objetos da classe Autor")
        self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if not (isinstance(autor, int)):
            raise TypeError("Livro.autores só pode excluir objetos da classe Autor")
        self.__autores.remove(autor)

    def incluir_capitulo(self):
        pass

    def __find_capitulo_by_titulo(self, titulo: str) -> Capitulo:
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
