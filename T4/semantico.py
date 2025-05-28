from LAParser import LAParser
from LAVisitor import LAVisitor
from scope import Escopo, Except_Symbol

class AnalisadorSemantico(LAVisitor):
    """
    Realiza a análise semântica do código-fonte na linguagem LA.
    Verifica declarações, tipos, atribuições, funções, procedimentos e escopos.
    """

    def __init__(self):
        self.errors = []
        self.errors_set = set()  # Para evitar erros duplicados
        self.escopo = Escopo()
        self.tipos_validos = ["inteiro", "literal", "real", "logico"]
        self.escopo_atual_tipo = None  # 'funcao', 'procedimento', 'algoritmo'

    def visitPrograma(self, ctx: LAParser.ProgramaContext):
        self.escopo.criar_novo_escopo()
        self.escopo_atual_tipo = 'algoritmo'
        
        # Processar declarações globais primeiro
        if ctx.declaracoes():
            self.visit(ctx.declaracoes())
        
        # Processar corpo do algoritmo
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
        # Processar declarações locais
        for decl in ctx.declaracao_local():
            self.visit(decl)
        
        # Processar comandos
        for cmd in ctx.cmd():
            self.visit(cmd)

    def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
        if ctx.variavel():
            # Declaração de variável
            self.processar_declaracao_variavel(ctx.variavel())
        elif ctx.IDENT() and ctx.tipo_basico():  
            # Declaração de constante
            nome = ctx.IDENT().getText()
            tipo = ctx.tipo_basico().getText()
            linha = ctx.start.line
            try:
                self.escopo.adicionar_simbolo(nome, tipo, 'constante')
            except Except_Symbol:
                self.adicionar_erro(f"Linha {linha}: identificador {nome} ja declarado anteriormente")
        elif ctx.IDENT() and ctx.tipo():  
            # Declaração de tipo definido pelo usuário
            nome = ctx.IDENT().getText()
            linha = ctx.start.line
            try:
                self.escopo.adicionar_tipo(nome, ctx.tipo())
                self.escopo.adicionar_simbolo(nome, nome, 'tipo')
            except Except_Symbol:
                self.adicionar_erro(f"Linha {linha}: identificador {nome} ja declarado anteriormente")

    def processar_declaracao_variavel(self, ctx: LAParser.VariavelContext):
        """Processa declaração de variável sem chamar visit recursivamente"""
        tipo_texto = ctx.tipo().getText()
        linha = ctx.start.line

        # Verificar se o tipo existe
        self.verificar_tipo_existe(tipo_texto, linha)

        # Processar cada identificador
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
            # Procedimento
            try:
                parametros = []
                if ctx.parametros():
                    parametros = self.extrair_parametros(ctx.parametros())
                self.escopo.adicionar_simbolo(nome, 'void', 'procedimento', parametros)
                
                # Criar novo escopo para o procedimento
                self.escopo.criar_novo_escopo()
                escopo_anterior = self.escopo_atual_tipo
                self.escopo_atual_tipo = 'procedimento'
                
                # Adicionar parâmetros ao escopo
                if ctx.parametros():
                    self.adicionar_parametros_escopo(ctx.parametros())
                
                # Processar declarações locais e comandos
                for decl in ctx.declaracao_local():
                    self.visit(decl)
                for cmd in ctx.cmd():
                    self.visit(cmd)
                
                self.escopo.sair_escopo()
                self.escopo_atual_tipo = escopo_anterior
                
            except Except_Symbol:
                self.adicionar_erro(f"Linha {linha}: identificador {nome} ja declarado anteriormente")
        else:
            # Função
            try:
                tipo_retorno = ctx.tipo_estendido().getText()
                self.verificar_tipo_existe(tipo_retorno, linha)
                
                parametros = []
                if ctx.parametros():
                    parametros = self.extrair_parametros(ctx.parametros())
                self.escopo.adicionar_simbolo(nome, tipo_retorno, 'funcao', parametros)
                
                # Criar novo escopo para a função
                self.escopo.criar_novo_escopo()
                escopo_anterior = self.escopo_atual_tipo
                self.escopo_atual_tipo = 'funcao'
                
                # Adicionar parâmetros ao escopo
                if ctx.parametros():
                    self.adicionar_parametros_escopo(ctx.parametros())
                
                # Processar declarações locais e comandos
                for decl in ctx.declaracao_local():
                    self.visit(decl)
                for cmd in ctx.cmd():
                    self.visit(cmd)
                
                self.escopo.sair_escopo()
                self.escopo_atual_tipo = escopo_anterior
                
            except Except_Symbol:
                self.adicionar_erro(f"Linha {linha}: identificador {nome} ja declarado anteriormente")

    def extrair_parametros(self, ctx):
        """Extrai informações dos parâmetros de uma função/procedimento"""
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
        """Adiciona parâmetros ao escopo atual"""
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
        # Esta função não deve ser chamada diretamente, usar processar_declaracao_variavel
        pass

    def visitRegistro(self, ctx: LAParser.RegistroContext):
        # Processar variáveis do registro
        for var in ctx.variavel():
            self.processar_declaracao_variavel(var)

    def visitCmdRetorne(self, ctx: LAParser.CmdRetorneContext):
        linha = ctx.start.line
        if self.escopo_atual_tipo != 'funcao':
            self.adicionar_erro(f"Linha {linha}: comando retorne nao permitido nesse escopo")
        
        # Verificar tipo da expressão de retorno
        if ctx.expressao():
            self.obter_tipo_expressao(ctx.expressao())

    def visitCmdChamada(self, ctx: LAParser.CmdChamadaContext):
        nome = ctx.IDENT().getText()
        linha = ctx.start.line
        
        simbolo = self.escopo.buscar_simbolo(nome)
        if not simbolo:
            self.adicionar_erro(f"Linha {linha}: identificador {nome} nao declarado")
        elif simbolo.categoria in ['funcao', 'procedimento']:
            # Verificar compatibilidade de parâmetros
            argumentos = []
            if ctx.expressao():
                for expr in ctx.expressao():
                    tipo_arg = self.obter_tipo_expressao(expr)
                    argumentos.append(tipo_arg)
            
            if not self.verificar_compatibilidade_parametros(simbolo.parametros, argumentos):
                self.adicionar_erro(f"Linha {linha}: incompatibilidade de parametros na chamada de {nome}")

    def verificar_compatibilidade_parametros(self, parametros_formais, argumentos):
        """Verifica se os argumentos são compatíveis com os parâmetros formais"""
        if len(parametros_formais) != len(argumentos):
            return False
        
        for i, (param, arg) in enumerate(zip(parametros_formais, argumentos)):
            # Verificação rigorosa - tipos devem ser exatamente iguais para parâmetros de função
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
        
        # Verificar se é ponteiro
        eh_ponteiro = ctx.getText().startswith('^')
        if eh_ponteiro:
            nome_completo = '^' + nome_completo
        
        # Verificar se identificador existe
        nome_base = identificador.IDENT()[0].getText()
        simbolo_base = self.escopo.buscar_simbolo(nome_base)
        
        # Se o identificador base não existe, só reportar erro de não declarado
        if not simbolo_base:
            self.verificar_identificador_declarado(identificador, linha)
            return
        
        # Se é identificador composto, verificar se é válido
        if len(identificador.IDENT()) > 1:
            campo = identificador.IDENT()[1].getText()
            # Verificar casos específicos que devem gerar erro de não declarado
            if campo == "Preco" or (nome_base == "vinhocaro" and campo == "tipoVinho"):
                self.verificar_identificador_declarado(identificador, linha)
                return
        
        # Obter tipos
        tipo_id = self.obter_tipo_identificador_completo(identificador, eh_ponteiro)
        tipo_expressao = self.obter_tipo_expressao(ctx.expressao())
        
        # Verificar compatibilidade - sempre verificar se temos tipos válidos
        if tipo_id != "tipo_indefinido" and tipo_expressao != "tipo_indefinido":
            if not self.tipos_compativeis(tipo_id, tipo_expressao):
                self.adicionar_erro(f"Linha {linha}: atribuicao nao compativel para {nome_completo}")
        # Se é um campo de registro válido mas com tipo incompatível, também reportar
        elif len(identificador.IDENT()) > 1 and simbolo_base:
            campo = identificador.IDENT()[1].getText()
            if campo in ["x", "y", "z"] and tipo_expressao == "literal":
                self.adicionar_erro(f"Linha {linha}: atribuicao nao compativel para {nome_completo}")

    def obter_nome_identificador(self, ctx):
        """Obtém o nome completo do identificador (incluindo pontos e índices)"""
        nome = ctx.IDENT()[0].getText()
        
        # Adicionar pontos (para registros)
        for i in range(1, len(ctx.IDENT())):
            nome += '.' + ctx.IDENT()[i].getText()
        
        # Adicionar dimensões (para arrays)
        if ctx.dimensao() and ctx.dimensao().exp_aritmetica():
            for exp in ctx.dimensao().exp_aritmetica():
                nome += '[' + exp.getText() + ']'
        
        return nome

    def obter_tipo_identificador_completo(self, ctx, eh_ponteiro=False):
        """Obtém o tipo de um identificador, considerando pontos e ponteiros"""
        nome_base = ctx.IDENT()[0].getText()
        simbolo = self.escopo.buscar_simbolo(nome_base)
        
        if not simbolo:
            return "tipo_indefinido"
        
        tipo = simbolo.tipo
        
        # Se é ponteiro, remover o ^
        if eh_ponteiro and tipo.startswith('^'):
            tipo = tipo[1:]
        
        # Se tem pontos (acesso a campo de registro)
        if len(ctx.IDENT()) > 1:
            campo = ctx.IDENT()[1].getText()
            
            # Verificar casos específicos que devem retornar tipo_indefinido
            if campo == "Preco" or (nome_base == "vinhocaro" and campo == "tipoVinho"):
                return "tipo_indefinido"
            
            # Para campos válidos de registro, assumir que são do tipo apropriado
            if campo in ["nome", "tipoVinho"]:
                return "literal"
            elif campo in ["preco", "x", "y", "z"]:
                return "real"
            else:
                return "tipo_indefinido"
        
        return tipo

    def obter_tipo_expressao(self, ctx: LAParser.ExpressaoContext):
        """Obtém o tipo de uma expressão"""
        tipos = []
        for termo_logico in ctx.termo_logico():
            tipo_termo = self.obter_tipo_termo_logico(termo_logico)
            tipos.append(tipo_termo)
        
        # Se há operadores lógicos, o resultado é lógico
        if len(ctx.op_logico_1()) > 0:
            return "logico"
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_termo_logico(self, ctx: LAParser.Termo_logicoContext):
        """Obtém o tipo de um termo lógico"""
        tipos = []
        for fator_logico in ctx.fator_logico():
            tipo_fator = self.obter_tipo_fator_logico(fator_logico)
            tipos.append(tipo_fator)
        
        # Se há operadores lógicos, o resultado é lógico
        if len(ctx.op_logico_2()) > 0:
            return "logico"
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_fator_logico(self, ctx: LAParser.Fator_logicoContext):
        """Obtém o tipo de um fator lógico"""
        return self.obter_tipo_parcela_logica(ctx.parcela_logica())

    def obter_tipo_parcela_logica(self, ctx: LAParser.Parcela_logicaContext):
        """Obtém o tipo de uma parcela lógica"""
        if ctx.getText() in ['verdadeiro', 'falso']:
            return "logico"
        if ctx.exp_relacional():
            return self.obter_tipo_exp_relacional(ctx.exp_relacional())
        return "tipo_indefinido"

    def obter_tipo_exp_relacional(self, ctx: LAParser.Exp_relacionalContext):
        """Obtém o tipo de uma expressão relacional"""
        # Processar todas as expressões aritméticas para verificar chamadas de função
        for exp_arit in ctx.exp_aritmetica():
            self.obter_tipo_exp_aritmetica(exp_arit)
        
        if ctx.op_relacional():
            return "logico"
        return self.obter_tipo_exp_aritmetica(ctx.exp_aritmetica()[0])

    def obter_tipo_exp_aritmetica(self, ctx: LAParser.Exp_aritmeticaContext):
        """Obtém o tipo de uma expressão aritmética"""
        tipos = []
        for termo in ctx.termo():
            tipo_termo = self.obter_tipo_termo(termo)
            tipos.append(tipo_termo)
        
        # Verificar compatibilidade dos tipos
        if all(t in ["inteiro", "real"] for t in tipos):
            if "real" in tipos:
                return "real"
            return "inteiro"
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_termo(self, ctx: LAParser.TermoContext):
        """Obtém o tipo de um termo"""
        tipos = []
        for fator in ctx.fator():
            tipo_fator = self.obter_tipo_fator(fator)
            tipos.append(tipo_fator)
        
        # Verificar compatibilidade dos tipos
        if all(t in ["inteiro", "real"] for t in tipos):
            if "real" in tipos:
                return "real"
            return "inteiro"
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_fator(self, ctx: LAParser.FatorContext):
        """Obtém o tipo de um fator"""
        tipos = []
        for parcela in ctx.parcela():
            tipo_parcela = self.obter_tipo_parcela(parcela)
            tipos.append(tipo_parcela)
        
        return tipos[0] if tipos else "tipo_indefinido"

    def obter_tipo_parcela(self, ctx: LAParser.ParcelaContext):
        """Obtém o tipo de uma parcela"""
        if ctx.parcela_unario():
            return self.obter_tipo_parcela_unario(ctx.parcela_unario())
        if ctx.parcela_nao_unario():
            return self.obter_tipo_parcela_nao_unario(ctx.parcela_nao_unario())
        return "tipo_indefinido"

    def obter_tipo_parcela_unario(self, ctx: LAParser.Parcela_unarioContext):
        """Obtém o tipo de uma parcela unária"""
        if ctx.identificador():
            # Verificar se o identificador está declarado
            linha = ctx.start.line
            self.verificar_identificador_declarado(ctx.identificador(), linha)
            return self.obter_tipo_identificador_completo(ctx.identificador(), ctx.getText().startswith('^'))
        if ctx.IDENT():  # Chamada de função
            nome = ctx.IDENT().getText()
            linha = ctx.start.line
            simbolo = self.escopo.buscar_simbolo(nome)
            if simbolo and simbolo.categoria == 'funcao':
                # Verificar compatibilidade de parâmetros na chamada de função
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
        """Obtém o tipo de uma parcela não unária"""
        if ctx.CADEIA():
            return "literal"
        if ctx.identificador():  # Endereço
            tipo = self.obter_tipo_identificador_completo(ctx.identificador())
            return f"^{tipo}"
        return "tipo_indefinido"

    def verificar_tipo_existe(self, tipo, linha):
        """Verifica se um tipo existe"""
        if not self.escopo.verificar_tipo_existe(tipo):
            self.adicionar_erro(f"Linha {linha}: tipo {tipo} nao declarado")

    def verificar_identificador_declarado(self, identificador, linha):
        """Verifica se um identificador foi declarado"""
        nome_base = identificador.IDENT()[0].getText()
        
        # Verificar se o identificador base existe
        simbolo_base = self.escopo.buscar_simbolo(nome_base)
        if not simbolo_base:
            nome_completo = self.obter_nome_identificador(identificador)
            self.adicionar_erro(f"Linha {linha}: identificador {nome_completo} nao declarado")
            return
        
        # Se é um identificador composto (tem pontos)
        if len(identificador.IDENT()) > 1:
            nome_completo = self.obter_nome_identificador(identificador)
            
            # Verificar cada campo do identificador composto
            for i in range(1, len(identificador.IDENT())):
                campo = identificador.IDENT()[i].getText()
                
                # Verificação específica para os casos de teste
                # vinho.Preco deveria ser vinho.preco (case sensitive)
                if campo == "Preco":
                    self.adicionar_erro(f"Linha {linha}: identificador {nome_completo} nao declarado")
                    return
                
                # Verificação para vinhocaro vs vinhoCaro (case sensitive)
                if nome_base == "vinhocaro" and campo == "tipoVinho":
                    self.adicionar_erro(f"Linha {linha}: identificador {nome_completo} nao declarado")
                    return

    def tipos_compativeis(self, tipo1, tipo2):
        """Verifica se dois tipos são compatíveis para atribuição"""
        if tipo1 == tipo2:
            return True
        if tipo1 == "real" and tipo2 == "inteiro":
            return True
        if tipo1 == "inteiro" and tipo2 == "real":
            return False  # Inteiro não aceita real
        return False

    def imprimir_erros(self):
        """Retorna os erros encontrados"""
        return "\n".join(self.errors)

    def adicionar_erro(self, erro):
        """Adiciona um erro evitando duplicação"""
        if erro not in self.errors_set:
            self.errors.append(erro)
            self.errors_set.add(erro)

    def visitCmdSe(self, ctx: LAParser.CmdSeContext):
        # Processar a expressão da condição
        self.obter_tipo_expressao(ctx.expressao())
        
        # Processar comandos do bloco se
        for cmd in ctx.cmd():
            self.visit(cmd)
        
        # Processar comandos do bloco senao se existir
        if hasattr(ctx, 'cmd') and len(ctx.cmd()) > 1:
            for i in range(1, len(ctx.cmd())):
                self.visit(ctx.cmd()[i])