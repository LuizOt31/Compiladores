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









































# from LAParser import LAParser
# from LAVisitor import LAVisitor
# from scope import Escopo, SymbolAlreadyDefinedException

# class semantico(LAVisitor):
#     """
#     Responsável por fazer a análise semântica da LA
#     """

#     def __init__(self):
#         self.errors = []
#         self.scope = Escopo()
#         self.validTypes = ["inteiro", "literal", "real", "logico"]

#     def visitPrograma(self, ctx: LAParser.ProgramaContext):
#         super().visitPrograma(ctx)
#         return self.__printErrors()

#     def visitCorpo(self, ctx: LAParser.CorpoContext):
#         self.scope.criar_novo_escopo()
#         return super().visitCorpo(ctx)

#     def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
#         return super().visitDeclaracao_local(ctx)

#     def visitVariavel(self, ctx: LAParser.VariavelContext):
#         type = ctx.tipo().getText()
#         line = ctx.start.line

#         self.__checkType(type, line)

#         for identifier in ctx.identificador():
#             key = identifier.getText()
#             line = identifier.start.line

#             try:
#                 self.scope.adicionar_simbolo(key, type)

#             except SymbolAlreadyDefinedException:
#                 self.errors.append(
#                     f"Linha {line}: identificador {key} ja declarado anteriormente"
#                 )

#     def visitCmdLeia(self, ctx: LAParser.CmdLeiaContext):
#         for identifier in ctx.identificador():
#             line = identifier.start.line
#             self.__checkDeclaredIdentifier(identifier, line)

#     def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
#         for expressao in ctx.expressao():
#             self.__getExpressaoType(expressao)

#         super().visitCmdEscreva(ctx)

#     def visitCmdEnquanto(self, ctx: LAParser.CmdEnquantoContext):
#         self.__getExpressaoType(ctx.expressao())
#         super().visitCmdEnquanto(ctx)

#     def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
#         identificador = ctx.identificador().getText()
#         tipo_identificador = self.__getIdentificadorType(
#             ctx.identificador()
#         )  # Tipo do identificador alvo
#         tipo_expressao = self.__flatten_list(
#             self.__getExpressaoType(ctx.expressao())
#         )  # Tipo da expressão

#         self.__checkAttributionType(
#             identificador, tipo_identificador, tipo_expressao, ctx.start.line
#         )
#         return super().visitCmdAtribuicao(ctx)

#     def __getExpressaoType(self, ctx: LAParser.ExpressaoContext):
#         types = []

#         for termo_logico in ctx.termo_logico():
#             for fator_logico in termo_logico.fator_logico():
#                 types.append(self.__getFator_logicoType(fator_logico))

#         return types

#     def __getFator_logicoType(self, ctx: LAParser.Fator_logicoContext):
#         return self.__getParcela_logicaType(ctx.parcela_logica())

#     def __getParcela_logicaType(self, ctx: LAParser.Parcela_logicaContext):
#         if ctx.exp_relacional():
#             return self.__getExp_relacionalType(ctx.exp_relacional())

#     def __getExp_relacionalType(self, ctx: LAParser.Exp_relacionalContext):
#         types = [self.__getExp_aritmeticaType(exp) for exp in ctx.exp_aritmetica()]

#         # If there are more than one expression, then it is a logical expression,
#         # which always has the type "logico"
#         if len(types) > 1:
#             return "logico"

#         return types

#     def __getExp_aritmeticaType(self, ctx: LAParser.Exp_aritmeticaContext):
#         types = [self.__getTermoType(termo) for termo in ctx.termo()]
#         return types

#     def __getTermoType(self, ctx: LAParser.TermoContext):
#         types = self.__flatten_list([self.__getFatorType(fator) for fator in ctx.fator()])

#         # Coerce integers to real numbers on multiplication and division
#         if len(ctx.op2()) > 0 and all(type in ["real", "inteiro"] for type in types):
#             return "real"

#         return types

#     def __getFatorType(self, ctx: LAParser.FatorContext):
#         types = [self.__getParcelaType(parcela) for parcela in ctx.parcela()]
#         return types

#     def __getParcelaType(self, ctx: LAParser.ParcelaContext):
#         if ctx.parcela_unario():
#             return self.__getParcela_unarioType(ctx.parcela_unario())

#         if ctx.parcela_nao_unario():
#             return self.__getParcela_nao_unarioType(ctx.parcela_nao_unario())

#     def __getParcela_unarioType(self, ctx: LAParser.Parcela_unarioContext):
#         identifier = ctx.identificador()

#         if identifier:
#             line = identifier.start.line
#             self.__checkDeclaredIdentifier(identifier, line)
#             return self.__getIdentificadorType(identifier)

#         if ctx.NUM_INT():
#             return "inteiro"

#         if ctx.NUM_REAL():
#             return "real"

#         if ctx.expressao():
#             return self.__getExpressaoType(ctx.expressao()[0])

#     def __getParcela_nao_unarioType(
#         self, ctx: LAParser.Parcela_nao_unarioContext
#     ):
#         if ctx.CADEIA():
#             return ["literal"]

#     def __getIdentificadorType(self, ctx: LAParser.IdentificadorContext):
#         identificador = str(ctx.IDENT()[0])

#         return self.scope.buscar_simbolo(identificador)

#     def __checkType(self, type: str, line) -> bool:
#         if type not in self.validTypes:
#             self.errors.append(f"Linha {line}: tipo {type} nao declarado")
#             return False

#         return True

#     def __printErrors(self) -> str:
#         return "\n".join(self.errors)

#     def __checkDeclaredIdentifier(self, identifier, line):
#         text = identifier.getText()
#         symbol = self.scope.buscar_simbolo(text)

#         if not symbol:
#             self.errors.append(f"Linha {line}: identificador {text} nao declarado")

#     def __checkAttributionType(
#         self, identifier, identifier_type, expression_types, line
#     ):
#         if not all(self.__is_coercible(identifier_type, type) for type in expression_types):
#             self.errors.append(
#                 f"Linha {line}: atribuicao nao compativel para {identifier}"
#             )

#     def __is_coercible(self, type_a, type_b):
#         if type_a == "real" and type_b == "inteiro":
#             return True

#         return type_a == type_b

#     def __flatten_list(self, nested_list):
#         flattened = []

#         for item in nested_list:
#             if isinstance(item, list):
#                 flattened.extend(self.__flatten_list(item))
#             else:
#                 flattened.append(item)

#         return flattened
