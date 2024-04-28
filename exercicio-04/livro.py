from autor import Autor
from editora import Editora
from capitulo import Capitulo
from typing import Set, Union


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
        if not (isinstance(codigo, int)):
            raise TypeError('Livro.codigo recebe "codigo: int"')
        if not (isinstance(titulo, str)):
            raise TypeError('Livro.titulo recebe "titulo: str"')
        if not (isinstance(ano, int)):
            raise TypeError('Livro.ano recebe "ano: int"')
        if not (isinstance(editora, Editora)):
            raise TypeError('Livro.editora recebe "editora: Editora"')
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = set()
        self.__capitulos = set()
        # Adicionando objetos nas listas (verificações de tipo nos métodos)
        self.incluir_autor(autor)
        self.incluir_capitulo(numero_capitulo, titulo_capitulo)

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if not (isinstance(codigo, int)):
            raise TypeError('Livro.codigo deve ser um inteiro')
        self.__codigo = codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if not (isinstance(titulo, str)):
            raise TypeError('Livro.titulo deve ser uma string')
        self.__titulo = titulo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        if not (isinstance(ano, int)):
            raise TypeError('Livro.ano deve ser um inteiro')
        self.__ano = ano

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora: str):
        if not (isinstance(editora, Editora)):
            raise TypeError('Livro.editora deve ser um objeto do tipo Editora')
        self.__editora = editora

    @property
    def autores(self) -> Set[Autor]:
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if not (isinstance(autor, Autor)):
            print('Livro.incluir_autor recebe "autor: Autor"')
            return
        if autor in self.__autores:
            print('Livro.incluir_autor já possui o autor a ser incluído')
            return
        self.__autores.add(autor)

    def excluir_autor(self, autor: Autor):
        # Desvios condições. Verificações de tipagem e regra de negócio
        if not (isinstance(autor, Autor)):
            print('Livro.excluir_autor recebe "autor: Autor"')
            return
        if autor not in self.__autores:
            print('Livro.autores não possui o autor a ser removido')
            return
        # Execução padrão
        self.__autores.discard(autor)

    @property
    def capitulos(self) -> Set[Capitulo]:
        return self.__capitulos

    def incluir_capitulo(self, numero: int, titulo: str):
        # Desvios condições. Verificações de tipagem e regra de negócio
        if not (isinstance(numero, int) and (isinstance(titulo, str))):
            print(
                'Livros.incluir_capitulo recebe "numero: int" E "titulo: str"'
            )
            return
        if self.find_capitulo_by_titulo(titulo) in self.capitulos:
            print('Livros.capitulos já possui um capitulo com este titulo')
            return
        # Execução padrão
        novo_capitulo = Capitulo(numero, titulo)
        self.__capitulos.add(novo_capitulo)

    def excluir_capitulo(self, titulo: str):
        if not (isinstance(titulo, str)):
            print('Livros.excluir_capitulo recebe "titulo: str"')
            return
        capitulo_to_remove = self.find_capitulo_by_titulo(titulo)
        if not capitulo_to_remove:
            print('Livros.capitulos não possui um capitulo com este titulo')
            return
        self.__capitulos.discard(capitulo_to_remove)

    def find_capitulo_by_titulo(self, titulo: str) -> Union[Capitulo, None]:
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
        return None
