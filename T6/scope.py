# scope.py

class Symbol:
    def __init__(self, name, type, value=None):
        self.name = name
        self.type = type
        self.value = value

class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = {}

    def add_symbol(self, symbol):
        """Adiciona um símbolo ao escopo atual."""
        if self.symbols.get(symbol.name):
            return False  # Símbolo já existe neste escopo
        self.symbols[symbol.name] = symbol
        return True

    def find_symbol(self, name):
        """Encontra um símbolo neste escopo ou em escopos pais."""
        symbol = self.symbols.get(name)
        if symbol:
            return symbol
        if self.parent:
            return self.parent.find_symbol(name)
        return None