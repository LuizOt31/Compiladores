
from LAParser import LAParser
from LAVisitor import LAVisitor
from scope import Scope, SymbolAlreadyDefinedException
from utils import flatten_list, is_coercible


class Alguma(LAVisitor):
    """
    Classe responsável por visitar e analisar a estrutura de um programa na linguagem 'Alguma'.
    """

    def __init__(self):
        self.errors = []
        self.scope = Scope()
        self.validTypes = ["inteiro", "literal", "real", "logico"]

    def visitPrograma(self, ctx: LAParser.ProgramaContext) -> str:
        super().visitPrograma(ctx)
        return self.__printErrors()

    def visitCorpo(self, ctx: LAParser.CorpoContext):
        self.scope.newScope()
        return super().visitCorpo(ctx)

    def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
        return super().visitDeclaracao_local(ctx)

    def visitVariavel(self, ctx: LAParser.VariavelContext):
        type = ctx.tipo().getText()
        line = ctx.start.line

        self.__checkType(type, line)

        for identifier in ctx.identificador():
            key = identifier.getText()
            line = identifier.start.line

            try:
                self.scope.add(key, type)

            except SymbolAlreadyDefinedException:
                self.errors.append(
                    f"Linha {line}: identificador {key} ja declarado anteriormente"
                )

    def visitCmdLeia(self, ctx: LAParser.CmdLeiaContext):
        for identifier in ctx.identificador():
            line = identifier.start.line
            self.__checkDeclaredIdentifier(identifier, line)

    def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
        for expressao in ctx.expressao():
            self.__getExpressaoType(expressao)

        super().visitCmdEscreva(ctx)

    def visitCmdEnquanto(self, ctx: LAParser.CmdEnquantoContext):
        self.__getExpressaoType(ctx.expressao())
        super().visitCmdEnquanto(ctx)

    def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
        identificador = ctx.identificador().getText()
        tipo_identificador = self.__getIdentificadorType(
            ctx.identificador()
        )  # Tipo do identificador alvo
        tipo_expressao = flatten_list(
            self.__getExpressaoType(ctx.expressao())
        )  # Tipo da expressão

        self.__checkAttributionType(
            identificador, tipo_identificador, tipo_expressao, ctx.start.line
        )
        return super().visitCmdAtribuicao(ctx)

    def __getExpressaoType(self, ctx: LAParser.ExpressaoContext):
        types = []

        for termo_logico in ctx.termo_logico():
            for fator_logico in termo_logico.fator_logico():
                types.append(self.__getFator_logicoType(fator_logico))

        return types

    def __getFator_logicoType(self, ctx: LAParser.Fator_logicoContext):
        return self.__getParcela_logicaType(ctx.parcela_logica())

    def __getParcela_logicaType(self, ctx: LAParser.Parcela_logicaContext):
        if ctx.exp_relacional():
            return self.__getExp_relacionalType(ctx.exp_relacional())

    def __getExp_relacionalType(self, ctx: LAParser.Exp_relacionalContext):
        types = [self.__getExp_aritmeticaType(exp) for exp in ctx.exp_aritmetica()]

        # If there are more than one expression, then it is a logical expression,
        # which always has the type "logico"
        if len(types) > 1:
            return "logico"

        return types

    def __getExp_aritmeticaType(self, ctx: LAParser.Exp_aritmeticaContext):
        types = [self.__getTermoType(termo) for termo in ctx.termo()]
        return types

    def __getTermoType(self, ctx: LAParser.TermoContext):
        types = flatten_list([self.__getFatorType(fator) for fator in ctx.fator()])

        # Coerce integers to real numbers on multiplication and division
        if len(ctx.op2()) > 0 and all(type in ["real", "inteiro"] for type in types):
            return "real"

        return types

    def __getFatorType(self, ctx: LAParser.FatorContext):
        types = [self.__getParcelaType(parcela) for parcela in ctx.parcela()]
        return types

    def __getParcelaType(self, ctx: LAParser.ParcelaContext):
        if ctx.parcela_unario():
            return self.__getParcela_unarioType(ctx.parcela_unario())

        if ctx.parcela_nao_unario():
            return self.__getParcela_nao_unarioType(ctx.parcela_nao_unario())

    def __getParcela_unarioType(self, ctx: LAParser.Parcela_unarioContext):
        identifier = ctx.identificador()

        if identifier:
            line = identifier.start.line
            self.__checkDeclaredIdentifier(identifier, line)
            return self.__getIdentificadorType(identifier)

        if ctx.NUM_INT():
            return "inteiro"

        if ctx.NUM_REAL():
            return "real"

        if ctx.expressao():
            return self.__getExpressaoType(ctx.expressao()[0])

    def __getParcela_nao_unarioType(
        self, ctx: LAParser.Parcela_nao_unarioContext
    ):
        if ctx.CADEIA():
            return ["literal"]

    def __getIdentificadorType(self, ctx: LAParser.IdentificadorContext):
        identificador = str(ctx.IDENT()[0])

        symbol = self.scope.find(identificador)

        if symbol:
            return symbol.type

    def __checkType(self, type: str, line) -> bool:
        if type not in self.validTypes:
            self.errors.append(f"Linha {line}: tipo {type} nao declarado")
            return False

        return True

    def __printErrors(self) -> str:
        return "\n".join(self.errors)

    def __checkDeclaredIdentifier(self, identifier, line):
        text = identifier.getText()
        symbol = self.scope.find(text)

        if not symbol:
            self.errors.append(f"Linha {line}: identificador {text} nao declarado")

    def __checkAttributionType(
        self, identifier, identifier_type, expression_types, line
    ):
        if not all(is_coercible(identifier_type, type) for type in expression_types):
            self.errors.append(
                f"Linha {line}: atribuicao nao compativel para {identifier}"
            )











































# from LAVisitor import LAVisitor
# from LAParser import LAParser
# from antlr4 import *
# from collections import defaultdict

# class Symbol:
#     def __init__(self, name, type_, category):
#         self.name = name
#         self.type = type_
#         self.category = category  # var, const, func, proc, tipo

# class SemanticAnalyzer(LAVisitor):
#     def __init__(self):
#         self.errors = []
#         self.scopes = [dict()]  # pilha de escopos
#         self.type_definitions = set(["literal", "inteiro", "real", "logico"])
#         self.current_function = None

#     def current_scope(self):
#         return self.scopes[-1]

#     def enter_scope(self):
#         self.scopes.append(dict())

#     def exit_scope(self):
#         self.scopes.pop()

#     def declare(self, symbol: Symbol, line):
#         scope = self.current_scope()
#         if symbol.name in scope:
#             self.errors.append(f"Linha {line}: identificador {symbol.name} ja declarado anteriormente")
#         else:
#             scope[symbol.name] = symbol

#     def resolve(self, name):
#         for scope in reversed(self.scopes):
#             if name in scope:
#                 return scope[name]
#         return None

#     def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
#         if ctx.getChild(0).getText() == "declare":
#             tipo = ctx.variavel().tipo().getText()
#             if tipo not in self.type_definitions:
#                 self.errors.append(f"Linha {ctx.start.line}: tipo {tipo} nao declarado")
#             for identificador in ctx.variavel().identificador():
#                 for ident_token in identificador.IDENT():
#                     nome = ident_token.getText()
#                     self.declare(Symbol(nome, tipo, "var"), ident_token.symbol.line)
#         elif ctx.getChild(0).getText() == "constante":
#             tipo = ctx.tipo_basico().getText()
#             nome = ctx.IDENT().getText()
#             self.declare(Symbol(nome, tipo, "const"), ctx.start.line)
#         elif ctx.getChild(0).getText() == "tipo":
#             nome = ctx.IDENT().getText()
#             self.type_definitions.add(nome)
#             self.declare(Symbol(nome, "tipo", "tipo"), ctx.start.line)
#         return self.visitChildren(ctx)

#     def visitDeclaracao_global(self, ctx: LAParser.Declaracao_globalContext):
#         is_func = ctx.getChild(0).getText() == "funcao"
#         nome = ctx.IDENT().getText()
#         tipo = ctx.tipo_estendido().getText() if is_func else "procedimento"
#         categoria = "func" if is_func else "proc"

#         self.declare(Symbol(nome, tipo, categoria), ctx.start.line)
#         self.enter_scope()

#         if ctx.parametros():
#             self.visit(ctx.parametros())

#         if ctx.declaracao_local():
#             for decl in ctx.declaracao_local():
#                 self.visit(decl)

#         if ctx.cmd():
#             for c in ctx.cmd():
#                 self.visit(c)

#         self.exit_scope()
#         return None

#     def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
#         ident = ctx.identificador().IDENT(0).getText()
#         linha = ctx.start.line
#         simbolo = self.resolve(ident)

#         if not simbolo:
#             self.errors.append(f"Linha {linha}: identificador {ident} nao declarado")
#             return None

#         tipo_destino = simbolo.type
#         tipo_expressao = self.visit(ctx.expressao())
#         if not self.is_compatible(tipo_destino, tipo_expressao):
#             self.errors.append(f"Linha {linha}: atribuicao nao compativel para {ident}")
#         return None

#     def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
#         for expressao in ctx.expressao():
#             self.visit(expressao)
#         return None

#     def visitIdentificador(self, ctx: LAParser.IdentificadorContext):
#         nome = ctx.IDENT(0).getText()
#         simbolo = self.resolve(nome)
#         if simbolo:
#             return simbolo.type
#         else:
#             self.errors.append(f"Linha {ctx.IDENT(0).symbol.line}: identificador {nome} nao declarado")
#             return "tipo_indefinido"

#     def visitExpressao(self, ctx: LAParser.ExpressaoContext):
#         tipos = [self.visit(term) for term in ctx.termo_logico()]
#         if any(t == "tipo_indefinido" for t in tipos):
#             return "tipo_indefinido"
#         if len(set(tipos)) == 1:
#             return tipos[0]
#         return "tipo_indefinido"

#     def visitTermo_logico(self, ctx: LAParser.Termo_logicoContext):
#         return self.visitChildren(ctx)

#     def visitFator_logico(self, ctx: LAParser.Fator_logicoContext):
#         return self.visitChildren(ctx)

#     def visitParcela_logica(self, ctx: LAParser.Parcela_logicaContext):
#         if ctx.getText() in ["verdadeiro", "falso"]:
#             return "logico"
#         return self.visit(ctx.exp_relacional())

#     def visitExp_relacional(self, ctx: LAParser.Exp_relacionalContext):
#         tipos = [self.visit(e) for e in ctx.exp_aritmetica()]
#         if len(set(tipos)) == 1 and tipos[0] in ["inteiro", "real", "literal"]:
#             return "logico"
#         return "tipo_indefinido"

#     def visitExp_aritmetica(self, ctx: LAParser.Exp_aritmeticaContext):
#         tipos = [self.visit(term) for term in ctx.termo()]
#         if all(t in ["inteiro", "real"] for t in tipos):
#             return "real" if "real" in tipos else "inteiro"
#         return "tipo_indefinido"

#     def visitTermo(self, ctx: LAParser.TermoContext):
#         tipos = [self.visit(fator) for fator in ctx.fator()]
#         if all(t in ["inteiro", "real"] for t in tipos):
#             return "real" if "real" in tipos else "inteiro"
#         return "tipo_indefinido"

#     def visitFator(self, ctx: LAParser.FatorContext):
#         tipos = [self.visit(parcela) for parcela in ctx.parcela()]
#         if all(t in ["inteiro", "real"] for t in tipos):
#             return "real" if "real" in tipos else "inteiro"
#         return "tipo_indefinido"

#     def visitParcela(self, ctx: LAParser.ParcelaContext):
#         if ctx.parcela_unario():
#             return self.visit(ctx.parcela_unario())
#         elif ctx.parcela_nao_unario():
#             return self.visit(ctx.parcela_nao_unario())
#         return "tipo_indefinido"


#     def visitParcela_unario(self, ctx: LAParser.Parcela_unarioContext):
#         if ctx.NUM_INT():
#             print("INT literal:", ctx.NUM_INT().getText())
#             return "inteiro"
#         if ctx.NUM_REAL():
#             print("REAL literal:", ctx.NUM_REAL().getText())
#             return "real"
#         if ctx.identificador():
#             print("IDENT usado:", ctx.identificador().getText())
#             return self.visitIdentificador(ctx.identificador())
#         return "tipo_indefinido"


#     def visitParcela_nao_unario(self, ctx: LAParser.Parcela_nao_unarioContext):
#         if ctx.CADEIA():
#             return "literal"
#         return self.visitChildren(ctx)

#     def is_compatible(self, tipo_destino, tipo_origem):
#         if tipo_destino == tipo_origem:
#             return True
#         if tipo_destino in ["real", "inteiro"] and tipo_origem in ["real", "inteiro"]:
#             return True
#         if tipo_destino.startswith("^") and tipo_origem.startswith("&"):
#             return True
#         return False
