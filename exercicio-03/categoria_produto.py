

class CategoriaProduto:
    def __init__(self, titulo: str) -> None:
        if (isinstance(titulo, str)):
            self.__titulo = titulo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if (isinstance(titulo, str)):
            self.__titulo = titulo
