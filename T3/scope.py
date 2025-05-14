# Erro para simbolo já definido dentro do escopo
class Except_Symbol(Exception):
    pass

class Variavel:
    def __init__(self, type, value, name):
        self.type = type
        self.value = value
        self.name = name


class Escopo:
    def __init__(self):
        self.escopos = []

    def criar_novo_escopo(self):
        self.escopos.append([])

    def escopo_atual(self):
        return self.escopos[-1]

    def sair_escopo(self):
        self.escopos.pop()

    def adicionar_simbolo(self, nome, tipo):
        escopo_corrente = self.escopo_atual()

        for var in escopo_corrente:
            if nome == var.name:
                raise Except_Symbol()
                        
        escopo_corrente.append(Variavel(tipo, None, nome))

    def buscar_simbolo(self, nome):
        for escopo in self.escopos:
            for var in escopo:
                if nome == var.name:
                    return var.type
        return None
