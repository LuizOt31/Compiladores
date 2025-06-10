class Except_Symbol(Exception):
    pass

class Simbolo:
    def __init__(self, nome, tipo, categoria, parametros=None, campos=None):
        self.nome = nome
        self.tipo = tipo
        self.categoria = categoria
        self.parametros = parametros or []
        self.campos = campos or {}


class Escopo:
    def __init__(self):
        self.escopos = []
        self.tipos_definidos = {}

    def criar_novo_escopo(self):
        self.escopos.append([])

    def escopo_atual(self):
        if not self.escopos:
            self.criar_novo_escopo()
        return self.escopos[-1]

    def sair_escopo(self):
        if self.escopos:
            self.escopos.pop()

    def adicionar_simbolo(self, nome, tipo, categoria='variavel', parametros=None, campos=None):
        escopo_corrente = self.escopo_atual()

        for simbolo in escopo_corrente:
            if nome == simbolo.nome:
                raise Except_Symbol()
                        
        escopo_corrente.append(Simbolo(nome, tipo, categoria, parametros, campos))

    def adicionar_tipo(self, nome, definicao):
        if nome in self.tipos_definidos:
            raise Except_Symbol()
        self.tipos_definidos[nome] = definicao

    def buscar_simbolo(self, nome):
        for escopo in reversed(self.escopos):
            for simbolo in escopo:
                if nome == simbolo.nome:
                    return simbolo
        return None

    def buscar_tipo_simbolo(self, nome):
        simbolo = self.buscar_simbolo(nome)
        return simbolo.tipo if simbolo else None

    def buscar_tipo_definido(self, nome):
        return self.tipos_definidos.get(nome)

    def verificar_tipo_existe(self, tipo):
        tipos_basicos = ["inteiro", "literal", "real", "logico"]
        
        tipo_original = tipo
        if tipo.startswith('^'):
            tipo = tipo[1:]
        
        if tipo in tipos_basicos:
            return True
            
        if tipo in self.tipos_definidos:
            return True
            
        if "registro" in tipo_original:
            return True
            
        return False

    def esta_em_funcao(self):
        for escopo in reversed(self.escopos):
            for simbolo in escopo:
                if simbolo.categoria == 'funcao':
                    return True
        return False

    def obter_tipo_campo_registro(self, tipo_registro, campo):
        return "tipo_indefinido"
