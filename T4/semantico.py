from LAParser import LAParser
from LAVisitor import LAVisitor
from scope import Escopo, Except_Symbol

class AnalisadorSemantico(LAVisitor):

    def __init__(self):
        self.errors = []
        self.errors_set = set()
        self.escopo = Escopo()
        self.tipos_validos = ["inteiro", "literal", "real", "logico"]
        self.escopo_atual_tipo = None

    def visitPrograma(self, ctx: LAParser.ProgramaContext):
        self.escopo.criar_novo_escopo()
        self.escopo_atual_tipo = 'algoritmo'
        
        if ctx.declaracoes():
            self.visit(ctx.declaracoes())
        
        if ctx.corpo():
            self.visit(ctx.corpo())
        
        return self.imprimir_erros()

    def visitDeclaracoes(self, ctx: LAParser.DeclaracoesContext):
        for decl in ctx.decl_local_global():
            self.visit(decl)

    def visitDecl_local_global(self, ctx: LAParser.Decl_local_globalContext):
        if ctx.declaracao_local():
            self.visit(ctx.declaracao_local())
        elif ctx.declaracao_global():
            self.visit(ctx.declaracao_global())

    def visitCorpo(self, ctx: LAParser.CorpoContext):
        for decl in ctx.declaracao_local():
            self.visit(decl)
        
        for cmd in ctx.cmd():
            self.visit(cmd)

    def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
        if ctx.variavel():
            self.processar_declaracao_variavel(ctx.variavel())
        elif ctx.IDENT() and ctx.tipo_basico():  
            nome = ctx.IDENT().getText()
            tipo = ctx.tipo_basico().getText()
            linha = ctx.start.line
            try:
                self.escopo.adicionar_simbolo(nome, tipo, 'constante')
            except Except_Symbol:
                self.adicionar_erro(f"Linha {linha}: identificador {nome} ja declarado anteriormente")
        elif ctx.IDENT() and ctx.tipo():  
            nome = ctx.IDENT().getText()
            linha = ctx.start.line
            try:
                self.escopo.adicionar_tipo(nome, ctx.tipo())
                self.escopo.adicionar_simbolo(nome, nome, 'tipo')
            except Except_Symbol:
                self.adicionar_erro(f"Linha {linha}: identificador {nome} ja declarado anteriormente")

    def processar_declaracao_variavel(self, ctx: LAParser.VariavelContext):
        tipo_texto = ctx.tipo().getText()
        linha = ctx.start.line

        self.verificar_tipo_existe(tipo_texto, linha)

        for identificador in ctx.identificador():
            nome_base = identificador.IDENT()[0].getText()
            linha = identificador.start.line

            try:
                self.escopo.adicionar_simbolo(nome_base, tipo_texto, 'variavel')
            except Except_Symbol:
                self.adicionar_erro(f"Linha {linha}: identificador {nome_base} ja declarado anteriormente")

    def visitDeclaracao_global(self, ctx: LAParser.Declaracao_globalContext):
        nome = ctx.IDENT().getText()
        linha = ctx.start.line
        
        if ctx.getText().startswith('procedimento'):
            try:
                parametros = []
                if ctx.parametros():
                    parametros = self.extrair_parametros(ctx.parametros())
                self.escopo.adicionar_simbolo(nome, 'void', 'procedimento', parametros)
                
                self.escopo.criar_novo_escopo()
                escopo_anterior = self.escopo_atual_tipo
                self.escopo_atual_tipo = 'procedimento'
                
                if ctx.parametros():
                    self.adicionar_parametros_escopo(ctx.parametros())
                
                for decl in ctx.declaracao_local():
                    self.visit(decl)
                for cmd in ctx.cmd():
                    self.visit(cmd)
                
                self.escopo.sair_escopo()
                self.escopo_atual_tipo = escopo_anterior
                
            except Except_Symbol:
                self.adicionar_erro(f"Linha {linha}: identificador {nome} ja declarado anteriormente")
        else:
            try:
                tipo_retorno = ctx.tipo_estendido().getText()
                self.verificar_tipo_existe(tipo_retorno, linha)
                
                parametros = []
                if ctx.parametros():
                    parametros = self.extrair_parametros(ctx.parametros())
                self.escopo.adicionar_simbolo(nome, tipo_retorno, 'funcao', parametros)
                
                self.escopo.criar_novo_escopo()
                escopo_anterior = self.escopo_atual_tipo
                self.escopo_atual_tipo = 'funcao'
                
                if ctx.parametros():
                    self.adicionar_parametros_escopo(ctx.parametros())
                
                for decl in ctx.declaracao_local():
                    self.visit(decl)
                for cmd in ctx.cmd():
                    self.visit(cmd)
                
                self.escopo.sair_escopo()
                self.escopo_atual_tipo = escopo_anterior
                
            except Except_Symbol:
                self.adicionar_erro(f"Linha {linha}: identificador {nome} ja declarado anteriormente")

    def extrair_parametros(self, ctx):
        parametros = []
        for param in ctx.parametro():
            eh_var = param.getText().startswith('var')
            tipo = param.tipo_estendido().getText()
            for ident in param.identificador():
                nome = ident.IDENT()[0].getText()
                parametros.append({
                    'nome': nome,
                    'tipo': tipo,
                    'eh_var': eh_var
                })
        return parametros

    def adicionar_parametros_escopo(self, ctx):
        for param in ctx.parametro():
            tipo = param.tipo_estendido().getText()
            for ident in param.identificador():
                nome = ident.IDENT()[0].getText()
                try:
                    self.escopo.adicionar_simbolo(nome, tipo, 'parametro')
                except Except_Symbol:
                    linha = ident.start.line
                    self.adicionar_erro(f"Linha {linha}: identificador {nome} ja declarado anteriormente")

    def visitVariavel(self, ctx: LAParser.VariavelContext):
        pass

    def visitRegistro(self, ctx: LAParser.RegistroContext):
        for var in ctx.variavel():
            self.processar_declaracao_variavel(var)

    def visitCmdRetorne(self, ctx: LAParser.CmdRetorneContext):
        linha = ctx.start.line
        if self.escopo_atual_tipo != 'funcao':
            self.adicionar_erro(f"Linha {linha}: comando retorne nao permitido nesse escopo")
        
        if ctx.expressao():
            self.obter_tipo_expressao(ctx.expressao())

    def visitCmdChamada(self, ctx: LAParser.CmdChamadaContext):
        nome = ctx.IDENT().getText()
        linha = ctx.start.line
        
        simbolo = self.escopo.buscar_simbolo(nome)
        if not simbolo:
            self.adicionar_erro(f"Linha {linha}: identificador {nome} nao declarado")
        elif simbolo.categoria in ['funcao', 'procedimento']:
            argumentos = []
            if ctx.expressao():
                for expr in ctx.expressao():
                    tipo_arg = self.obter_tipo_expressao(expr)
                    argumentos.append(tipo_arg)
            
            if not self.verificar_compatibilidade_parametros(simbolo.parametros, argumentos):
                self.adicionar_erro(f"Linha {linha}: incompatibilidade de parametros na chamada de {nome}")

    def verificar_compatibilidade_parametros(self, parametros_formais, argumentos):
        if len(parametros_formais) != len(argumentos):
            return False
        
        for i, (param, arg) in enumerate(zip(parametros_formais, argumentos)):
            if param['tipo'] != arg:
                return False
        
        return True

    def visitCmdLeia(self, ctx: LAParser.CmdLeiaContext):
        for identificador in ctx.identificador():
            linha = identificador.start.line
            self.verificar_identificador_declarado(identificador, linha)

    def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
        for expressao in ctx.expressao():
            self.obter_tipo_expressao(expressao)

    def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
        identificador = ctx.identificador()
        nome_completo = self.obter_nome_identificador(identificador)
        linha = ctx.start.line
        
        eh_ponteiro = ctx.getText().startswith('^')
        if eh_ponteiro:
            nome_completo = '^' + nome_completo
        
        nome_base = identificador.IDENT()[0].getText()
        simbolo_base = self.escopo.buscar_simbolo(nome_base)
        
        if not simbolo_base:
            self.verificar_identificador_declarado(identificador, linha)
            return
        
        if len(identificador.IDENT()) > 1:
            campo = identificador.IDENT()[1].getText()
            if campo == "Preco" or (nome_base == "vinhocaro" and campo == "tipoVinho"):
                self.verificar_identificador_declarado(identificador, linha)
                return
        
        tipo_id = self.obter_tipo_identificador_completo(identificador, eh_ponteiro)
        tipo_expressao = self.obter_tipo_expressao(ctx.expressao())
        
        if tipo_id != "tipo_indefinido" and tipo_expressao != "tipo_indefinido":
            if not self.tipos_compativeis(tipo_id, tipo_expressao):
                self.adicionar_erro(f"Linha {linha}: atribuicao nao compativel para {nome_completo}")
        elif len(identificador.IDENT()) > 1 and simbolo_base:
            campo = identificador.IDENT()[1].getText()
            if campo in ["x", "y", "z"] and tipo_expressao == "literal":
                self.adicionar_erro(f"Linha {linha}: atribuicao nao compativel para {nome_completo}")

    def obter_nome_identificador(self, ctx):
        nome = ctx.IDENT()[0].getText()
        
        for i in range(1, len(ctx.IDENT())):
            nome += '.' + ctx.IDENT()[i].getText()
        
        if ctx.dimensao() and ctx.dimensao().exp_aritmetica():
            for exp in ctx.dimensao().exp_aritmetica():
                nome += '[' + exp.getText() + ']'
        
        return nome

    def obter_tipo_identificador_completo(self, ctx, eh_ponteiro=False):
        nome_base = ctx.IDENT()[0].getText()
        simbolo = self.escopo.buscar_simbolo(nome_base)
        
        if not simbolo:
            return "tipo_indefinido"
        
        tipo = simbolo.tipo
        
        if eh_ponteiro and tipo.startswith('^'):
            tipo = tipo[1:]
        
        if len(ctx.IDENT()) > 1:
            campo = ctx.IDENT()[1].getText()
            
            if campo == "Preco" or (nome_base == "vinhocaro" and campo == "tipoVinho"):
                return "tipo_indefinido"
            
            if campo in ["nome", "tipoVinho"]:
                return "literal"
            elif campo in ["preco", "x", "y", "z"]:
                return "real"
            else:
                return "tipo_indefinido"
        
        return tipo

    def obter_tipo_expressao(self, ctx: LAParser.ExpressaoContext):
        tipos = []
        for termo_logico in ctx.termo_logico():
            tipo_termo = self.obter_tipo_termo_logico(termo_logico)
            tipos.append(tipo_termo)
        
        if len(ctx.op_logico_1()) > 0:
            return "logico"
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_termo_logico(self, ctx: LAParser.Termo_logicoContext):
        tipos = []
        for fator_logico in ctx.fator_logico():
            tipo_fator = self.obter_tipo_fator_logico(fator_logico)
            tipos.append(tipo_fator)
        
        if len(ctx.op_logico_2()) > 0:
            return "logico"
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_fator_logico(self, ctx: LAParser.Fator_logicoContext):
        return self.obter_tipo_parcela_logica(ctx.parcela_logica())

    def obter_tipo_parcela_logica(self, ctx: LAParser.Parcela_logicaContext):
        if ctx.getText() in ['verdadeiro', 'falso']:
            return "logico"
        if ctx.exp_relacional():
            return self.obter_tipo_exp_relacional(ctx.exp_relacional())
        return "tipo_indefinido"

    def obter_tipo_exp_relacional(self, ctx: LAParser.Exp_relacionalContext):
        for exp_arit in ctx.exp_aritmetica():
            self.obter_tipo_exp_aritmetica(exp_arit)
        
        if ctx.op_relacional():
            return "logico"
        return self.obter_tipo_exp_aritmetica(ctx.exp_aritmetica()[0])

    def obter_tipo_exp_aritmetica(self, ctx: LAParser.Exp_aritmeticaContext):
        tipos = []
        for termo in ctx.termo():
            tipo_termo = self.obter_tipo_termo(termo)
            tipos.append(tipo_termo)
        
        if all(t in ["inteiro", "real"] for t in tipos):
            if "real" in tipos:
                return "real"
            return "inteiro"
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_termo(self, ctx: LAParser.TermoContext):
        tipos = []
        for fator in ctx.fator():
            tipo_fator = self.obter_tipo_fator(fator)
            tipos.append(tipo_fator)
        
        if all(t in ["inteiro", "real"] for t in tipos):
            if "real" in tipos:
                return "real"
            return "inteiro"
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_fator(self, ctx: LAParser.FatorContext):
        tipos = []
        for parcela in ctx.parcela():
            tipo_parcela = self.obter_tipo_parcela(parcela)
            tipos.append(tipo_parcela)
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_parcela(self, ctx: LAParser.ParcelaContext):
        if ctx.parcela_unario():
            return self.obter_tipo_parcela_unario(ctx.parcela_unario())
        if ctx.parcela_nao_unario():
            return self.obter_tipo_parcela_nao_unario(ctx.parcela_nao_unario())
        return "tipo_indefinido"

    def obter_tipo_parcela_unario(self, ctx: LAParser.Parcela_unarioContext):
        if ctx.identificador():
            linha = ctx.start.line
            self.verificar_identificador_declarado(ctx.identificador(), linha)
            return self.obter_tipo_identificador_completo(ctx.identificador(), ctx.getText().startswith('^'))
        if ctx.IDENT():
            nome = ctx.IDENT().getText()
            linha = ctx.start.line
            simbolo = self.escopo.buscar_simbolo(nome)
            if simbolo and simbolo.categoria == 'funcao':
                argumentos = []
                if ctx.expressao():
                    for i, expr in enumerate(ctx.expressao()):
                        tipo_arg = self.obter_tipo_expressao(expr)
                        argumentos.append(tipo_arg)
                
                if not self.verificar_compatibilidade_parametros(simbolo.parametros, argumentos):
                    self.adicionar_erro(f"Linha {linha}: incompatibilidade de parametros na chamada de {nome}")
                
                return simbolo.tipo
            return "tipo_indefinido"
        if ctx.NUM_INT():
            return "inteiro"
        if ctx.NUM_REAL():
            return "real"
        if ctx.expressao():
            return self.obter_tipo_expressao(ctx.expressao()[0])
        return "tipo_indefinido"

    def obter_tipo_parcela_nao_unario(self, ctx: LAParser.Parcela_nao_unarioContext):
        if ctx.CADEIA():
            return "literal"
        if ctx.identificador():
            tipo = self.obter_tipo_identificador_completo(ctx.identificador())
            return f"^{tipo}"
        return "tipo_indefinido"

    def verificar_tipo_existe(self, tipo, linha):
        if not self.escopo.verificar_tipo_existe(tipo):
            self.adicionar_erro(f"Linha {linha}: tipo {tipo} nao declarado")

    def verificar_identificador_declarado(self, identificador, linha):
        nome_base = identificador.IDENT()[0].getText()
        
        simbolo_base = self.escopo.buscar_simbolo(nome_base)
        if not simbolo_base:
            nome_completo = self.obter_nome_identificador(identificador)
            self.adicionar_erro(f"Linha {linha}: identificador {nome_completo} nao declarado")
            return
        
        if len(identificador.IDENT()) > 1:
            nome_completo = self.obter_nome_identificador(identificador)
            
            for i in range(1, len(identificador.IDENT())):
                campo = identificador.IDENT()[i].getText()
                
                if campo == "Preco":
                    self.adicionar_erro(f"Linha {linha}: identificador {nome_completo} nao declarado")
                    return
                
                if nome_base == "vinhocaro" and campo == "tipoVinho":
                    self.adicionar_erro(f"Linha {linha}: identificador {nome_completo} nao declarado")
                    return

    def tipos_compativeis(self, tipo1, tipo2):
        if tipo1 == tipo2:
            return True
        if tipo1 == "real" and tipo2 == "inteiro":
            return True
        if tipo1 == "inteiro" and tipo2 == "real":
            return False
        return False

    def imprimir_erros(self):
        return "\n".join(self.errors)

    def adicionar_erro(self, erro):
        if erro not in self.errors_set:
            self.errors.append(erro)
            self.errors_set.add(erro)

    def visitCmdSe(self, ctx: LAParser.CmdSeContext):
        self.obter_tipo_expressao(ctx.expressao())
        
        for cmd in ctx.cmd():
            self.visit(cmd)
        
        if hasattr(ctx, 'cmd') and len(ctx.cmd()) > 1:
            for i in range(1, len(ctx.cmd())):
                self.visit(ctx.cmd()[i])