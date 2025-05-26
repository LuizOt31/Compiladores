class SymbolAlreadyDefinedException(Exception):
    "Símbolo já definido no escopo"
    pass

class Symbol:
    def __init__(self, name, type_, category=None):
        self.name = name
        self.type = type_
        self.category = category  # 'var', 'const', 'func', 'proc', 'tipo'
        self.params = []  # Para funções/procedimentos

class Escopo:
    def __init__(self):
        self.escopos = []
        self.current_function = None  # Para verificar retorno

    def criar_novo_escopo(self):
        self.escopos.append([])

    def escopo_atual(self):
        return self.escopos[-1] if self.escopos else None

    def sair_escopo(self):
        if self.escopos:
            self.escopos.pop()

    def adicionar_simbolo(self, nome, tipo, category='var'):
        escopo_corrente = self.escopo_atual()
        if not escopo_corrente:
            self.criar_novo_escopo()
            escopo_corrente = self.escopo_atual()

        for symbol in escopo_corrente:
            if nome == symbol.name:
                raise SymbolAlreadyDefinedException()
                        
        new_symbol = Symbol(nome, tipo, category)
        escopo_corrente.append(new_symbol)
        return new_symbol

    def buscar_simbolo(self, nome):
        for escopo in reversed(self.escopos):
            for symbol in escopo:
                if nome == symbol.name:
                    return symbol
        return None

    def buscar_tipo(self, nome):
        symbol = self.buscar_simbolo(nome)
        return symbol.type if symbol else None