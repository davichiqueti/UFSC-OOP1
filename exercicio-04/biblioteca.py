from livro import Livro
from typing import Set


class Biblioteca:
    def __init__(self):
        self.__livros = set()

    @property
    def livros(self) -> Set[Livro]:
        return self.__livros

    def incluir_livro(self, livro: Livro):
        if not (isinstance(livro, Livro)):
            print('Biblioteca.incluir_livro recebe "livro: Livro"')
            return
        self.__livros.add(livro)

    def excluir_livro(self, livro: Livro):
        if not (isinstance(livro, Livro)):
            print('Biblioteca.excluir_livro recebe "livro: Livro"')
            return
        self.__livros.discard(livro)
