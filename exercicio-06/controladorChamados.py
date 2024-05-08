from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self) -> None:
        self.__chamados = list()
        self.__tipos_chamados = list()

    @property
    def chamados(self) -> list:
        return self.__chamados

    @property
    def tipos_chamados(self) -> list:
        return self.__tipos_chamados

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        count = 0
        for chamado_cadastrado in self.chamados:
            if chamado_cadastrado.tipo == tipo:
                count += 1
        return count

    def inclui_chamado(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado
    ) -> Chamado:
        if (
            isinstance(data, Date)
            and isinstance(cliente, Cliente)
            and isinstance(tecnico, Tecnico)
            and isinstance(titulo, str)
            and isinstance(descricao, str)
            and isinstance(prioridade, int)
            and isinstance(tipo, TipoChamado)
        ):
            for chamado_cadastrado in self.chamados:
                if (
                    chamado_cadastrado.data == data
                    and chamado_cadastrado.cliente == cliente
                    and chamado_cadastrado.tecnico == tecnico
                    and chamado_cadastrado.tipo == tipo
                ):
                    return
            novo_chamado = Chamado(
                data,
                cliente,
                tecnico,
                titulo,
                descricao,
                prioridade,
                tipo
            )
            self.__chamados.append(novo_chamado)
            return novo_chamado

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        for tipo_chamado_cadastrado in self.tipos_chamados:
            if tipo_chamado_cadastrado.codigo == codigo:
                return
        novo_tipo_chamado = TipoChamado(codigo, descricao, nome)
        self.__tipos_chamados.append(novo_tipo_chamado)
        return novo_tipo_chamado
