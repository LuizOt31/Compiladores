from LAVisitor import LAVisitor
from LAParser import LAParser
from antlr4 import *
from collections import defaultdict

class Symbol:
    def __init__(self, name, type_, category):
        self.name = name
        self.type = type_
        self.category = category  # var, const, func, proc, tipo

class SemanticAnalyzer(LAVisitor):
    def __init__(self):
        self.errors = []
        self.scopes = [dict()]  # pilha de escopos
        self.type_definitions = set(["literal", "inteiro", "real", "logico"])
        self.current_function = None

    def current_scope(self):
        return self.scopes[-1]

    def enter_scope(self):
        self.scopes.append(dict())

    def exit_scope(self):
        self.scopes.pop()

    def declare(self, symbol: Symbol, line):
        scope = self.current_scope()
        if symbol.name in scope:
            self.errors.append(f"Linha {line}: identificador {symbol.name} ja declarado anteriormente")
        else:
            scope[symbol.name] = symbol

    def resolve(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
        if ctx.getChild(0).getText() == "declare":
            tipo = ctx.variavel().tipo().getText()
            if tipo not in self.type_definitions:
                self.errors.append(f"Linha {ctx.start.line}: tipo {tipo} nao declarado")
            for identificador in ctx.variavel().identificador():
                for ident_token in identificador.IDENT():
                    nome = ident_token.getText()
                    self.declare(Symbol(nome, tipo, "var"), ident_token.symbol.line)
        elif ctx.getChild(0).getText() == "constante":
            tipo = ctx.tipo_basico().getText()
            nome = ctx.IDENT().getText()
            self.declare(Symbol(nome, tipo, "const"), ctx.start.line)
        elif ctx.getChild(0).getText() == "tipo":
            nome = ctx.IDENT().getText()
            self.type_definitions.add(nome)
            self.declare(Symbol(nome, "tipo", "tipo"), ctx.start.line)
        return self.visitChildren(ctx)

    def visitDeclaracao_global(self, ctx: LAParser.Declaracao_globalContext):
        is_func = ctx.getChild(0).getText() == "funcao"
        nome = ctx.IDENT().getText()
        tipo = ctx.tipo_estendido().getText() if is_func else "procedimento"
        categoria = "func" if is_func else "proc"

        self.declare(Symbol(nome, tipo, categoria), ctx.start.line)
        self.enter_scope()

        if ctx.parametros():
            self.visit(ctx.parametros())

        if ctx.declaracao_local():
            for decl in ctx.declaracao_local():
                self.visit(decl)

        if ctx.cmd():
            for c in ctx.cmd():
                self.visit(c)

        self.exit_scope()
        return None

    def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
        ident = ctx.identificador().IDENT(0).getText()
        linha = ctx.start.line
        simbolo = self.resolve(ident)

        if not simbolo:
            self.errors.append(f"Linha {linha}: identificador {ident} nao declarado")
            return None

        tipo_destino = simbolo.type
        tipo_expressao = self.visit(ctx.expressao())

        if not self.is_compatible(tipo_destino, tipo_expressao):
            self.errors.append(f"Linha {linha}: atribuicao nao compativel para {ident}")
        return None

    def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
        for expressao in ctx.expressao():
            self.visit(expressao)
        return None

    def visitIdentificador(self, ctx: LAParser.IdentificadorContext):
        nome = ctx.IDENT(0).getText()
        simbolo = self.resolve(nome)
        if simbolo:
            return simbolo.type
        else:
            self.errors.append(f"Linha {ctx.IDENT(0).symbol.line}: identificador {nome} nao declarado")
            return "tipo_indefinido"

    def visitExpressao(self, ctx: LAParser.ExpressaoContext):
        tipos = [self.visit(term) for term in ctx.termo_logico()]
        if any(t == "tipo_indefinido" for t in tipos):
            return "tipo_indefinido"
        if len(set(tipos)) == 1:
            return tipos[0]
        return "tipo_indefinido"

    def visitTermo_logico(self, ctx: LAParser.Termo_logicoContext):
        return self.visitChildren(ctx)

    def visitFator_logico(self, ctx: LAParser.Fator_logicoContext):
        return self.visitChildren(ctx)

    def visitParcela_logica(self, ctx: LAParser.Parcela_logicaContext):
        if ctx.getText() in ["verdadeiro", "falso"]:
            return "logico"
        return self.visit(ctx.exp_relacional())

    def visitExp_relacional(self, ctx: LAParser.Exp_relacionalContext):
        tipos = [self.visit(e) for e in ctx.exp_aritmetica()]
        if len(set(tipos)) == 1 and tipos[0] in ["inteiro", "real", "literal"]:
            return "logico"
        return "tipo_indefinido"

    def visitExp_aritmetica(self, ctx: LAParser.Exp_aritmeticaContext):
        tipos = [self.visit(term) for term in ctx.termo()]
        if all(t in ["inteiro", "real"] for t in tipos):
            return "real" if "real" in tipos else "inteiro"
        return "tipo_indefinido"

    def visitTermo(self, ctx: LAParser.TermoContext):
        return self.visitChildren(ctx)

    def visitFator(self, ctx: LAParser.FatorContext):
        return self.visitChildren(ctx)

    def visitParcela(self, ctx: LAParser.ParcelaContext):
        return self.visitChildren(ctx)

    def visitParcela_unario(self, ctx: LAParser.Parcela_unarioContext):
        if ctx.NUM_INT():
            return "inteiro"
        if ctx.NUM_REAL():
            return "real"
        if ctx.identificador():
            return self.visitIdentificador(ctx.identificador())
        return self.visitChildren(ctx)

    def visitParcela_nao_unario(self, ctx: LAParser.Parcela_nao_unarioContext):
        if ctx.CADEIA():
            return "literal"
        return self.visitChildren(ctx)

    def is_compatible(self, tipo_destino, tipo_origem):
        if tipo_destino == tipo_origem:
            return True
        if tipo_destino in ["real", "inteiro"] and tipo_origem in ["real", "inteiro"]:
            return True
        if tipo_destino.startswith("^") and tipo_origem.startswith("&"):
            return True
        return False
