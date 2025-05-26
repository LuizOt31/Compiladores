from LAParser import LAParser
from LAVisitor import LAVisitor
from scope import Escopo, SymbolAlreadyDefinedException

class semantico(LAVisitor):
    def __init__(self):
        self.errors = []
        self.scope = Escopo()
        self.validTypes = ["inteiro", "literal", "real", "logico"]
        self.current_function = None

    def visitPrograma(self, ctx: LAParser.ProgramaContext):
        self.scope.criar_novo_escopo()
        super().visitPrograma(ctx)
        self.scope.sair_escopo()
        return "\n".join(self.errors) if self.errors else ""
    
    # def visitVariavel(self, ctx: LAParser.VariavelContext):
    #     tipo = ctx.tipo().getText()
    #     line = ctx.start.line
        
    #     # Verifica se o tipo existe
    #     if tipo not in self.validTypes and not self.scope.buscar_simbolo(tipo):
    #         self.errors.append(f"Linha {line}: tipo {tipo} nao declarado")
        
    #     # Verifica cada identificador
    #     for identifier in ctx.identificador():
    #         ident_text = identifier.getText()
    #         ident_line = identifier.start.line
            
    #         # Verifica se já foi declarado no escopo atual
    #         if any(symbol.name == ident_text for symbol in self.scope.escopo_atual()):
    #             self.errors.append(f"Linha {ident_line}: identificador {ident_text} ja declarado anteriormente")
    #         else:
    #             try:
    #                 self.scope.adicionar_simbolo(ident_text, tipo)
    #             except SymbolAlreadyDefinedException:
    #                 pass  # Já tratado acima

    def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
        if ctx.getChild(0).getText() == 'declare':
            tipo = ctx.variavel().tipo().getText()
            if tipo.startswith('^'):
                base_type = tipo[1:]
                if base_type not in self.validTypes and not self.scope.buscar_simbolo(base_type):
                    self.errors.append(f"Linha {ctx.start.line}: tipo {base_type} nao declarado")
            
            for identifier in ctx.variavel().identificador():
                key = identifier.getText()
                try:
                    self.scope.adicionar_simbolo(key, tipo)
                except SymbolAlreadyDefinedException:
                    self.errors.append(f"Linha {identifier.start.line}: identificador {key} ja declarado anteriormente")
        
        elif ctx.getChild(0).getText() == 'constante':
            tipo = ctx.tipo_basico().getText()
            nome = ctx.IDENT().getText()
            try:
                self.scope.adicionar_simbolo(nome, tipo, 'const')
            except SymbolAlreadyDefinedException:
                self.errors.append(f"Linha {ctx.start.line}: identificador {nome} ja declarado anteriormente")
        
        elif ctx.getChild(0).getText() == 'tipo':
            nome = ctx.IDENT().getText()
            tipo = ctx.tipo().getText()
            try:
                self.scope.adicionar_simbolo(nome, tipo, 'tipo')
                if tipo not in self.validTypes:
                    self.validTypes.append(tipo)
            except SymbolAlreadyDefinedException:
                self.errors.append(f"Linha {ctx.start.line}: identificador {nome} ja declarado anteriormente")
        
        return super().visitDeclaracao_local(ctx)

    def visitDeclaracao_global(self, ctx: LAParser.Declaracao_globalContext):
        is_func = ctx.getChild(0).getText() == 'funcao'
        nome = ctx.IDENT().getText()
        tipo = ctx.tipo_estendido().getText() if is_func else None
        
        if is_func and tipo.startswith('^'):
            base_type = tipo[1:]
            if base_type not in self.validTypes and not self.scope.buscar_simbolo(base_type):
                self.errors.append(f"Linha {ctx.start.line}: tipo {base_type} nao declarado")
        
        try:
            func_symbol = self.scope.adicionar_simbolo(nome, tipo, 'func' if is_func else 'proc')
            self.current_function = nome if is_func else None
        except SymbolAlreadyDefinedException:
            self.errors.append(f"Linha {ctx.start.line}: identificador {nome} ja declarado anteriormente")
            return super().visitDeclaracao_global(ctx)
        
        if ctx.parametros():
            for param in ctx.parametros().parametro():
                param_type = param.tipo_estendido().getText()
                for ident in param.identificador():
                    try:
                        param_symbol = self.scope.adicionar_simbolo(ident.getText(), param_type)
                        func_symbol.params.append((ident.getText(), param_type))
                    except SymbolAlreadyDefinedException:
                        self.errors.append(f"Linha {ident.start.line}: identificador {ident.getText()} ja declarado anteriormente")
        
        self.scope.criar_novo_escopo()
        result = super().visitDeclaracao_global(ctx)
        self.scope.sair_escopo()
        self.current_function = None
        return result
    
    def visitCmdRetorne(self, ctx: LAParser.CmdRetorneContext):
        if not self.current_function:
            self.errors.append(f"Linha {ctx.start.line}: comando retorne nao permitido nesse escopo")
        else:
            func_symbol = self.scope.buscar_simbolo(self.current_function)
            if func_symbol and func_symbol.type:
                expr_type = self.__getExpressaoType(ctx.expressao())
                if not self.__is_compatible(func_symbol.type, expr_type):
                    self.errors.append(f"Linha {ctx.start.line}: tipo de retorno incompativel")
        
        return super().visitCmdRetorne(ctx)

    def visitCmdChamada(self, ctx: LAParser.CmdChamadaContext):
        func_name = ctx.IDENT().getText()
        func_symbol = self.scope.buscar_simbolo(func_name)
        
        if not func_symbol or func_symbol.category not in ['func', 'proc']:
            self.errors.append(f"Linha {ctx.start.line}: identificador {func_name} nao declarado")
            return super().visitCmdChamada(ctx)
        
        expected_params = func_symbol.params
        actual_params = ctx.expressao()
        
        if len(expected_params) != len(actual_params):
            self.errors.append(f"Linha {ctx.start.line}: incompatibilidade de parametros na chamada de {func_name}")
        else:
            for i, (exp_param, act_expr) in enumerate(zip(expected_params, actual_params)):
                act_type = self.__getExpressaoType(act_expr)
                if not self.__is_compatible(exp_param[1], act_type):
                    self.errors.append(f"Linha {ctx.start.line}: tipo do parametro {i+1} incompativel")
        
        return super().visitCmdChamada(ctx)

    def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
        identificador = ctx.identificador().getText()
        tipo_identificador = self.__getIdentificadorType(ctx.identificador())
        tipo_expressao = self.__flatten_list(self.__getExpressaoType(ctx.expressao()))

        self.__checkAttributionType(identificador, tipo_identificador, tipo_expressao, ctx.start.line)
        return super().visitCmdAtribuicao(ctx)

    def visitCmdLeia(self, ctx: LAParser.CmdLeiaContext):
        for identifier in ctx.identificador():
            line = identifier.start.line
            self.__checkDeclaredIdentifier(identifier, line)

    def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
        for expressao in ctx.expressao():
            self.__getExpressaoType(expressao)
        super().visitCmdEscreva(ctx)

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
        return "logico"

    def __getExp_relacionalType(self, ctx: LAParser.Exp_relacionalContext):
        types = [self.__getExp_aritmeticaType(exp) for exp in ctx.exp_aritmetica()]
        if len(types) > 1:
            return "logico"
        return types[0] if types else None

    def __getExp_aritmeticaType(self, ctx: LAParser.Exp_aritmeticaContext):
        types = [self.__getTermoType(termo) for termo in ctx.termo()]
        return types[0] if types else None

    def __getTermoType(self, ctx: LAParser.TermoContext):
        types = self.__flatten_list([self.__getFatorType(fator) for fator in ctx.fator()])
        if len(ctx.op2()) > 0 and all(type in ["real", "inteiro"] for type in types):
            return "real"
        return types[0] if types else None

    def __getFatorType(self, ctx: LAParser.FatorContext):
        types = [self.__getParcelaType(parcela) for parcela in ctx.parcela()]
        return types[0] if types else None

    def __getParcelaType(self, ctx: LAParser.ParcelaContext):
        if ctx.parcela_unario():
            return self.__getParcela_unarioType(ctx.parcela_unario())
        if ctx.parcela_nao_unario():
            return self.__getParcela_nao_unarioType(ctx.parcela_nao_unario())
        return None

    def __getParcela_unarioType(self, ctx: LAParser.Parcela_unarioContext):
        if ctx.identificador():
            line = ctx.identificador().start.line
            self.__checkDeclaredIdentifier(ctx.identificador(), line)
            return self.__getIdentificadorType(ctx.identificador())
        if ctx.NUM_INT():
            return "inteiro"
        if ctx.NUM_REAL():
            return "real"
        if ctx.expressao():
            return self.__getExpressaoType(ctx.expressao()[0])
        return None

    def __getParcela_nao_unarioType(self, ctx: LAParser.Parcela_nao_unarioContext):
        if ctx.CADEIA():
            return "literal"
        return None

    def __getIdentificadorType(self, ctx: LAParser.IdentificadorContext):
        identificador = str(ctx.IDENT()[0])
        symbol = self.scope.buscar_simbolo(identificador)
        return symbol.type if symbol else None

    def __checkDeclaredIdentifier(self, identifier, line):
        text = identifier.getText()
        symbol = self.scope.buscar_simbolo(text)
        if not symbol:
            self.errors.append(f"Linha {line}: identificador {text} nao declarado")

    def __checkAttributionType(self, identifier, identifier_type, expression_types, line):
        if not identifier_type:
            return
        for type in expression_types:
            if not self.__is_compatible(identifier_type, type):
                self.errors.append(f"Linha {line}: atribuicao nao compativel para {identifier}")

    def __is_compatible(self, type_a, type_b):
        if type_a == type_b:
            return True
        if type_a in ["real", "inteiro"] and type_b in ["real", "inteiro"]:
            return True
        if type_a.startswith('^') and type_b.startswith('&'):
            pointed_type = type_a[1:]
            var_type = self.__get_base_type(type_b[1:])
            return pointed_type == var_type
        if type_a.startswith('^') and type_b.startswith('^'):
            return type_a == type_b
        return False

    def __get_base_type(self, type_name):
        symbol = self.scope.buscar_simbolo(type_name)
        return symbol.type if symbol else type_name

    def __flatten_list(self, nested_list):
        flattened = []
        for item in nested_list:
            if isinstance(item, list):
                flattened.extend(self.__flatten_list(item))
            elif item:
                flattened.append(item)
        return flattened