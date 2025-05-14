from LAParser import LAParser
from LAVisitor import LAVisitor
from scope import Escopo, Except_Symbol

class AnalisadorSemantico(LAVisitor):
    """
    Realiza a análise semântica do código-fonte na linguagem LA.
    Verifica declarações, tipos e atribuições incorretas.
    """

    def __init__(self):
        self.errors = []
        self.escopo = Escopo()
        self.tipos_validos = ["inteiro", "literal", "real", "logico"]

    def visitPrograma(self, ctx: LAParser.ProgramaContext):
        super().visitPrograma(ctx)
        return self.imprimir_erros()

    def visitCorpo(self, ctx: LAParser.CorpoContext):
        self.escopo.criar_novo_escopo()
        return super().visitCorpo(ctx)

    def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
        return super().visitDeclaracao_local(ctx)

    def visitVariavel(self, ctx: LAParser.VariavelContext):
        tipo = ctx.tipo().getText()
        linha = ctx.start.line

        self.verificar_tipo(tipo, linha)

        for identificador in ctx.identificador():
            nome_id = identificador.getText()
            linha = identificador.start.line

            try:
                self.escopo.adicionar_simbolo(nome_id, tipo)
            except Except_Symbol:
                self.errors.append(
                    f"Linha {linha}: identificador {nome_id} ja declarado anteriormente"
                )

    def visitCmdLeia(self, ctx: LAParser.CmdLeiaContext):
        for identificador in ctx.identificador():
            linha = identificador.start.line
            self.verificar_identificador_declarado(identificador, linha)

    def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
        for expressao in ctx.expressao():
            self.obter_tipo_expressao(expressao)
        super().visitCmdEscreva(ctx)

    def visitCmdEnquanto(self, ctx: LAParser.CmdEnquantoContext):
        self.obter_tipo_expressao(ctx.expressao())
        super().visitCmdEnquanto(ctx)

    def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
        nome_id = ctx.identificador().getText()
        tipo_id = self.obter_tipo_identificador(ctx.identificador())
        tipo_expressao = self.achatado(self.obter_tipo_expressao(ctx.expressao()))

        self.verificar_atribuicao(nome_id, tipo_id, tipo_expressao, ctx.start.line)
        return super().visitCmdAtribuicao(ctx)

    def obter_tipo_expressao(self, ctx: LAParser.ExpressaoContext):
        tipos = []
        for termo_logico in ctx.termo_logico():
            for fator_logico in termo_logico.fator_logico():
                tipos.append(self.obter_tipo_fator_logico(fator_logico))
        return tipos

    def obter_tipo_fator_logico(self, ctx: LAParser.Fator_logicoContext):
        return self.obter_tipo_parcela_logica(ctx.parcela_logica())

    def obter_tipo_parcela_logica(self, ctx: LAParser.Parcela_logicaContext):
        if ctx.exp_relacional():
            return self.obter_tipo_expressao_relacional(ctx.exp_relacional())

    def obter_tipo_expressao_relacional(self, ctx: LAParser.Exp_relacionalContext):
        tipos = [self.obter_tipo_expressao_aritmetica(exp) for exp in ctx.exp_aritmetica()]
        if len(tipos) > 1:
            return "logico"
        return tipos

    def obter_tipo_expressao_aritmetica(self, ctx: LAParser.Exp_aritmeticaContext):
        return [self.obter_tipo_termo(termo) for termo in ctx.termo()]

    def obter_tipo_termo(self, ctx: LAParser.TermoContext):
        tipos = self.achatado([self.obter_tipo_fator(fator) for fator in ctx.fator()])
        if len(ctx.op2()) > 0 and all(t in ["real", "inteiro"] for t in tipos):
            return "real"
        return tipos

    def obter_tipo_fator(self, ctx: LAParser.FatorContext):
        return [self.obter_tipo_parcela(parcela) for parcela in ctx.parcela()]

    def obter_tipo_parcela(self, ctx: LAParser.ParcelaContext):
        if ctx.parcela_unario():
            return self.obter_tipo_parcela_unaria(ctx.parcela_unario())
        if ctx.parcela_nao_unario():
            return self.obter_tipo_parcela_nao_unaria(ctx.parcela_nao_unario())

    def obter_tipo_parcela_unaria(self, ctx: LAParser.Parcela_unarioContext):
        identificador = ctx.identificador()
        if identificador:
            linha = identificador.start.line
            self.verificar_identificador_declarado(identificador, linha)
            return self.obter_tipo_identificador(identificador)

        if ctx.NUM_INT():
            return "inteiro"
        if ctx.NUM_REAL():
            return "real"
        if ctx.expressao():
            return self.obter_tipo_expressao(ctx.expressao()[0])

    def obter_tipo_parcela_nao_unaria(self, ctx: LAParser.Parcela_nao_unarioContext):
        if ctx.CADEIA():
            return ["literal"]

    def obter_tipo_identificador(self, ctx: LAParser.IdentificadorContext):
        nome = str(ctx.IDENT()[0])
        return self.escopo.buscar_simbolo(nome)

    def verificar_tipo(self, tipo: str, linha):
        if tipo not in self.tipos_validos:
            self.errors.append(f"Linha {linha}: tipo {tipo} nao declarado")

    def verificar_identificador_declarado(self, identificador, linha):
        nome = identificador.getText()
        if not self.escopo.buscar_simbolo(nome):
            self.errors.append(f"Linha {linha}: identificador {nome} nao declarado")

    def verificar_atribuicao(self, nome, tipo_id, tipos_expr, linha):
        if not all(self.aux(tipo_id, tipo) for tipo in tipos_expr):
            self.errors.append(f"Linha {linha}: atribuicao nao compativel para {nome}")

    def aux(self, tipo_a, tipo_b):
        if tipo_a == "real" and tipo_b == "inteiro":
            return True
        return tipo_a == tipo_b

    def achatado(self, lista_aninhada):
        resultado = []
        for item in lista_aninhada:
            if isinstance(item, list):
                resultado.extend(self.achatado(item))
            else:
                resultado.append(item)
        return resultado

    def imprimir_erros(self):
        return "\n".join(self.errors)