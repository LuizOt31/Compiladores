from enum import Enum

class TabelaDeSimbolos:
    class TipoColorArt(Enum):
        INTEIRO = 1
        COR = 2
        VARIAVEL = 3
        INVALIDO = 4

    class EntradaTabelaDeSimbolos:
        def __init__(self, nome, tipo, valor = None):
            self.nome = nome
            self.tipo = tipo
            self.valor = valor

    def __init__(self):
        self.tabelaDeSimbolos = {}

    def adicionarTabelaSimbolos(self, nome: str, tipo: TipoColorArt, valor = None):
        etds = TabelaDeSimbolos.EntradaTabelaDeSimbolos(nome, tipo, valor)
        self.tabelaDeSimbolos[nome] = etds

    def adicionarEntradaTabelaSimbolos(self, entradaTabelaSimbolos: EntradaTabelaDeSimbolos):
        self.tabelaDeSimbolos[entradaTabelaSimbolos.nome] = entradaTabelaSimbolos

    def obterEntradaTabelaSimbolos(self, nome: str):
        return self.tabelaDeSimbolos.get(nome, None)

    def existe(self, nome: str):
        return nome in self.tabelaDeSimbolos

    def getTipo(self, nome: str):
        if self.existe(nome):
            return self.tabelaDeSimbolos[nome].tipo
        return None

    def getValor(self, nome: str):
        if self.existe(nome):
            return self.tabelaDeSimbolos[nome].valor
        return None 