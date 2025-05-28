# Erro para simbolo já definido dentro do escopo
class Except_Symbol(Exception):
    pass

class Simbolo:
    def __init__(self, nome, tipo, categoria, parametros=None):
        self.nome = nome
        self.tipo = tipo
        self.categoria = categoria  # 'variavel', 'funcao', 'procedimento', 'tipo', 'constante', 'parametro'
        self.parametros = parametros or []  # Para funções e procedimentos

class Escopo:
    def __init__(self):
        self.escopos = []
        self.tipos_definidos = {}  # Para armazenar tipos definidos pelo usuário

    def criar_novo_escopo(self):
        self.escopos.append([])

    def escopo_atual(self):
        if not self.escopos:
            self.criar_novo_escopo()
        return self.escopos[-1]

    def sair_escopo(self):
        if self.escopos:
            self.escopos.pop()

    def adicionar_simbolo(self, nome, tipo, categoria='variavel', parametros=None):
        escopo_corrente = self.escopo_atual()

        # Verifica se já existe no escopo atual
        for simbolo in escopo_corrente:
            if nome == simbolo.nome:
                raise Except_Symbol()
                        
        escopo_corrente.append(Simbolo(nome, tipo, categoria, parametros))

    def adicionar_tipo(self, nome, definicao):
        """Adiciona um tipo definido pelo usuário"""
        if nome in self.tipos_definidos:
            raise Except_Symbol()
        self.tipos_definidos[nome] = definicao

    def buscar_simbolo(self, nome):
        """Busca um símbolo em todos os escopos"""
        for escopo in reversed(self.escopos):
            for simbolo in escopo:
                if nome == simbolo.nome:
                    return simbolo
        return None

    def buscar_tipo_simbolo(self, nome):
        """Retorna apenas o tipo do símbolo"""
        simbolo = self.buscar_simbolo(nome)
        return simbolo.tipo if simbolo else None

    def buscar_tipo_definido(self, nome):
        """Busca um tipo definido pelo usuário"""
        return self.tipos_definidos.get(nome)

    def verificar_tipo_existe(self, tipo):
        """Verifica se um tipo existe (básico ou definido pelo usuário)"""
        tipos_basicos = ["inteiro", "literal", "real", "logico"]
        
        # Remove ^ se for ponteiro
        tipo_original = tipo
        if tipo.startswith('^'):
            tipo = tipo[1:]
        
        # Verifica se é um tipo básico
        if tipo in tipos_basicos:
            return True
            
        # Verifica se é um tipo definido pelo usuário
        if tipo in self.tipos_definidos:
            return True
            
        # Verifica se é um registro inline (contém "registro")
        if "registro" in tipo_original:
            return True
            
        return False

    def esta_em_funcao(self):
        """Verifica se estamos dentro de uma função (para comando retorne)"""
        for escopo in reversed(self.escopos):
            for simbolo in escopo:
                if simbolo.categoria == 'funcao':
                    return True
        return False

    def obter_tipo_campo_registro(self, tipo_registro, campo):
        """Obtém o tipo de um campo específico de um registro"""
        # Implementação simplificada - assumir que todos os campos são válidos
        # Em uma implementação completa, seria necessário analisar a estrutura do registro
        return "tipo_indefinido"
