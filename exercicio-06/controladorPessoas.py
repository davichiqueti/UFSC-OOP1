from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self) -> None:
        self.__clientes = list()
        self.__tecnicos = list()

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        for cliente_cadastrado in self.__clientes:
            if cliente_cadastrado.codigo == codigo:
                return
        novo_cliente = Cliente(nome=nome, codigo=codigo)
        self.__clientes.append(novo_cliente)
        return novo_cliente

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        for tecnico_cadastrado in self.__tecnicos:
            if tecnico_cadastrado.codigo == codigo:
                return
        novo_tecnico = Tecnico(nome=nome, codigo=codigo)
        self.__tecnicos.append(novo_tecnico)
        return novo_tecnico
