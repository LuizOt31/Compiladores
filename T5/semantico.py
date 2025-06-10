from LAParser import LAParser
from LAVisitor import LAVisitor
from scope import Escopo, Except_Symbol
import re

class AnalisadorSemantico(LAVisitor):

    def __init__(self):
        self.errors = []
        self.errors_set = set()
        self.escopo = Escopo()
        self.c_code_main = []
        self.c_code_headers = [
            "#include <stdio.h>",
            "#include <stdlib.h>",
            "#include <string.h>"
        ]
        self.c_code_globals = []
        self.current_code_buffer = None
        self.indentation_level = 1

    def _get_indent(self):
        return "    " * self.indentation_level

    def _map_type_to_c(self, la_type):
        if la_type == "inteiro": return "int"
        if la_type == "real": return "float"
        if la_type == "logico": return "int"
        if la_type == "literal": return "char"
        if la_type.startswith('^'):
            base_type = self._map_type_to_c(la_type[1:])
            return f"{base_type}*"
        if self.escopo.buscar_tipo_definido(la_type) or la_type == "registro":
            return la_type
        return "void"

    def _get_format_specifier(self, la_type):
        if la_type == "inteiro": return "%d"
        if la_type == "real": return "%f"
        if la_type == "logico": return "%d"
        if la_type == "literal": return "%s"
        return ""

    def _c_expression(self, ctx):
        text = ctx.getText()
        if text.startswith('&'): return text
        text = re.sub(r'\bnao\b', '!', text)
        text = re.sub(r'\be\b', '&&', text)
        text = re.sub(r'\bou\b', '||', text)
        text = re.sub(r'(?<![<>!=])=(?![=])', '==', text)
        return text

    def visitPrograma(self, ctx: LAParser.ProgramaContext):
        self.escopo.criar_novo_escopo()
        if ctx.declaracoes():
            self.visit(ctx.declaracoes())
        
        self.current_code_buffer = self.c_code_main
        self.c_code_main.append("int main() {")
        if ctx.corpo():
            self.visit(ctx.corpo())
        self.c_code_main.append(f"{self._get_indent()}return 0;")
        self.c_code_main.append("}")
        
        if not self.errors:
            final_code = "\n".join(self.c_code_headers) + "\n\n"
            if self.c_code_globals:
                final_code += "\n".join(self.c_code_globals) + "\n\n"
            final_code += "\n".join(self.c_code_main)
            return final_code
        return self.imprimir_erros()

    def visitDeclaracao_global(self, ctx: LAParser.Declaracao_globalContext):
        nome_func = ctx.IDENT().getText()
        self.escopo.criar_novo_escopo()
        self.current_code_buffer = self.c_code_globals
        
        tipo_retorno_la = "void"
        if ctx.getText().startswith('funcao'):
            tipo_retorno_la = ctx.tipo_estendido().getText()
        
        tipo_retorno_c = self._map_type_to_c(tipo_retorno_la)
        assinatura = f"{tipo_retorno_c} {nome_func}("
        
        params_c = []
        if ctx.parametros():
            for param_ctx in ctx.parametros().parametro():
                tipo_param_la = param_ctx.tipo_estendido().getText()
                tipo_param_c = self._map_type_to_c(tipo_param_la)
                for ident_ctx in param_ctx.identificador():
                    nome_param = ident_ctx.getText()
                    self.escopo.adicionar_simbolo(nome_param, tipo_param_la)
                    
                    if tipo_param_la == "literal":
                        params_c.append(f"char* {nome_param}")
                    else:
                        params_c.append(f"{tipo_param_c} {nome_param}")

        assinatura += ", ".join(params_c) + ") {"
        self.c_code_globals.append(assinatura)
        
        self.indentation_level +=1
        for decl in ctx.declaracao_local():
            self.visit(decl)
        for cmd in ctx.cmd():
            self.visit(cmd)
        self.indentation_level -=1
            
        self.c_code_globals.append("}")
        self.escopo.sair_escopo()
        self.current_code_buffer = None

    # AQUI ESTÁ O NOVO MÉTODO para chamadas de procedimento
    def visitCmdChamada(self, ctx: LAParser.CmdChamadaContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        nome_func = ctx.IDENT().getText()
        
        args = []
        if ctx.expressao():
            for expr in ctx.expressao():
                args.append(self._c_expression(expr))
        
        arg_string = ", ".join(args)
        buffer.append(f"{self._get_indent()}{nome_func}({arg_string});")

    # Restante do código (sem alterações desde a última versão)
    def visitDeclaracao_local(self, ctx: LAParser.Declaracao_localContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        ident = self._get_indent()
        if ctx.variavel():
            variavel_ctx = ctx.variavel()
            tipo_ctx = variavel_ctx.tipo()
            if tipo_ctx.registro():
                for id_ctx in variavel_ctx.identificador():
                    nome_reg = id_ctx.getText()
                    campos_do_registro = {}
                    for campo_var_ctx in tipo_ctx.registro().variavel():
                        tipo_campo = campo_var_ctx.tipo().getText()
                        for campo_id_ctx in campo_var_ctx.identificador():
                            campos_do_registro[campo_id_ctx.getText()] = tipo_campo
                    try:
                        self.escopo.adicionar_simbolo(nome_reg, 'registro', 'variavel', campos=campos_do_registro)
                    except Except_Symbol:
                        self.adicionar_erro(f"Linha {id_ctx.start.line}: identificador {nome_reg} ja declarado anteriormente")
                    buffer.append(f"{ident}struct {{")
                    self.indentation_level += 1
                    for campo_var_ctx in tipo_ctx.registro().variavel():
                        self.visitVariavel(campo_var_ctx, buffer)
                    self.indentation_level -= 1
                    buffer.append(f"{ident}}} {nome_reg};")
            else:
                la_type = tipo_ctx.getText()
                c_type = self._map_type_to_c(la_type)
                for id_ctx in variavel_ctx.identificador():
                    nome_var = id_ctx.IDENT()[0].getText()
                    try:
                        self.escopo.adicionar_simbolo(nome_var, la_type, 'variavel')
                    except Except_Symbol:
                        self.adicionar_erro(f"Linha {id_ctx.start.line}: identificador {nome_var} ja declarado anteriormente")
                    dimensao_texto = id_ctx.dimensao().getText()
                    if la_type == "literal":
                        buffer.append(f"{ident}{c_type} {nome_var}[80];")
                    elif dimensao_texto:
                        buffer.append(f"{ident}{c_type} {nome_var}{dimensao_texto};")
                    else:
                        buffer.append(f"{ident}{c_type} {nome_var};")
        elif ctx.getText().startswith('constante'):
            nome_const = ctx.IDENT().getText()
            valor = ctx.valor_constante().getText()
            self.c_code_globals.insert(0, f"#define {nome_const} {valor}")
            try:
                self.escopo.adicionar_simbolo(nome_const, ctx.tipo_basico().getText(), 'constante')
            except Except_Symbol:
                self.adicionar_erro(f"Linha {ctx.start.line}: identificador {nome_const} ja declarado anteriormente")
        elif ctx.getText().startswith('tipo'):
            nome_tipo = ctx.IDENT().getText()
            try:
                self.escopo.adicionar_tipo(nome_tipo, ctx.tipo())
            except Except_Symbol:
                 self.adicionar_erro(f"Linha {ctx.start.line}: tipo {nome_tipo} ja declarado")
            self.c_code_globals.append(f"typedef struct {{")
            self.indentation_level += 1
            if ctx.tipo().registro():
                for var_ctx in ctx.tipo().registro().variavel():
                    self.visitVariavel(var_ctx, self.c_code_globals)
            self.indentation_level -= 1
            self.c_code_globals.append(f"}} {nome_tipo};")

    def visitVariavel(self, ctx: LAParser.VariavelContext, buffer_override=None):
        buffer = buffer_override if buffer_override is not None else self.current_code_buffer
        la_type = ctx.tipo().getText()
        c_type = self._map_type_to_c(la_type)
        for id_ctx in ctx.identificador():
            nome_var = id_ctx.getText()
            if la_type == "literal":
                buffer.append(f"{self._get_indent()}{c_type} {nome_var}[80];")
            else:
                buffer.append(f"{self._get_indent()}{c_type} {nome_var};")

    def visitCmdRetorne(self, ctx: LAParser.CmdRetorneContext):
        if self.current_code_buffer is not None:
            exp_text = self._c_expression(ctx.expressao())
            self.current_code_buffer.append(f"{self._get_indent()}return {exp_text};")

    def visitCorpo(self, ctx: LAParser.CorpoContext):
        for decl in ctx.declaracao_local():
            self.visit(decl)
        for cmd in ctx.cmd():
            self.visit(cmd)

    def visitCmdLeia(self, ctx: LAParser.CmdLeiaContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        for identificador in ctx.identificador():
            nome_var = identificador.getText()
            tipo_real = self.obter_tipo_identificador_completo(identificador)
            specifier = self._get_format_specifier(tipo_real)
            if tipo_real == "literal":
                 buffer.append(f'{self._get_indent()}scanf("{specifier}", {nome_var});')
            else:
                 buffer.append(f'{self._get_indent()}scanf("{specifier}", &{nome_var});')

    def visitCmdEscreva(self, ctx: LAParser.CmdEscrevaContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        format_str = []
        args_str = []
        for expressao in ctx.expressao():
            tipo = self.obter_tipo_expressao(expressao)
            format_str.append(self._get_format_specifier(tipo))
            args_str.append(expressao.getText())
        buffer.append(f'{self._get_indent()}printf("{"".join(format_str)}", { ", ".join(args_str) });')

    def visitCmdAtribuicao(self, ctx: LAParser.CmdAtribuicaoContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        lhs_identifier_text = ctx.identificador().getText()
        if ctx.PONTEIRO():
            lhs = "*" + lhs_identifier_text
        else:
            lhs = lhs_identifier_text
        rhs = self._c_expression(ctx.expressao())
        tipo_lhs = self.obter_tipo_identificador_completo(ctx.identificador())
        if tipo_lhs == "literal" and not ctx.PONTEIRO():
            buffer.append(f'{self._get_indent()}strcpy({lhs}, {rhs});')
        else:
            buffer.append(f'{self._get_indent()}{lhs} = {rhs};')
            
    def visitCmdSe(self, ctx: LAParser.CmdSeContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        cond = self._c_expression(ctx.expressao())
        buffer.append(f'{self._get_indent()}if ({cond}) {{')
        self.indentation_level += 1
        is_else_block = False
        for child in ctx.children:
            if isinstance(child, LAParser.CmdContext):
                if not is_else_block: self.visit(child)
            elif child.getText() == 'senao':
                is_else_block = True
                self.indentation_level -= 1
                buffer.append(f'{self._get_indent()}}} else {{')
                self.indentation_level += 1
        if is_else_block:
            is_else_block = False
            for child in ctx.children:
                if child.getText() == 'senao': is_else_block = True
                elif is_else_block and isinstance(child, LAParser.CmdContext): self.visit(child)
        self.indentation_level -= 1
        buffer.append(f'{self._get_indent()}}}')

    def visitCmdCaso(self, ctx: LAParser.CmdCasoContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        exp = self._c_expression(ctx.exp_aritmetica())
        buffer.append(f'{self._get_indent()}switch ({exp}) {{')
        self.indentation_level += 1
        if ctx.selecao(): self.visit(ctx.selecao())
        if ctx.getText().count('senao'):
            buffer.append(f'{self._get_indent()}default:')
            self.indentation_level += 1
            for cmd_ctx in ctx.cmd(): self.visit(cmd_ctx)
            buffer.append(f'{self._get_indent()}break;')
            self.indentation_level -= 1
        self.indentation_level -= 1
        buffer.append(f'{self._get_indent()}}}')

    def visitSelecao(self, ctx: LAParser.SelecaoContext):
        for item in ctx.item_selecao(): self.visit(item)

    def visitItem_selecao(self, ctx: LAParser.Item_selecaoContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        for num_intervalo in ctx.constantes().numero_intervalo():
            if len(num_intervalo.NUM_INT()) > 1:
                start, end = int(num_intervalo.NUM_INT(0).getText()), int(num_intervalo.NUM_INT(1).getText())
                for i in range(start, end + 1): buffer.append(f'{self._get_indent()}case {i}:')
            else:
                buffer.append(f'{self._get_indent()}case {num_intervalo.NUM_INT(0).getText()}:')
        self.indentation_level += 1
        for cmd in ctx.cmd(): self.visit(cmd)
        buffer.append(f'{self._get_indent()}break;')
        self.indentation_level -= 1

    def visitCmdPara(self, ctx: LAParser.CmdParaContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        var, start, end = ctx.IDENT().getText(), self._c_expression(ctx.exp_aritmetica(0)), self._c_expression(ctx.exp_aritmetica(1))
        buffer.append(f'{self._get_indent()}for ({var} = {start}; {var} <= {end}; {var}++) {{')
        self.indentation_level += 1
        for cmd in ctx.cmd(): self.visit(cmd)
        self.indentation_level -= 1
        buffer.append(f'{self._get_indent()}}}')

    def visitCmdEnquanto(self, ctx: LAParser.CmdEnquantoContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        cond = self._c_expression(ctx.expressao())
        buffer.append(f'{self._get_indent()}while ({cond}) {{')
        self.indentation_level += 1
        for cmd in ctx.cmd(): self.visit(cmd)
        self.indentation_level -= 1
        buffer.append(f'{self._get_indent()}}}')

    def visitCmdFaca(self, ctx: LAParser.CmdFacaContext):
        buffer = self.current_code_buffer if self.current_code_buffer is not None else self.c_code_main
        cond = self._c_expression(ctx.expressao())
        buffer.append(f'{self._get_indent()}do {{')
        self.indentation_level += 1
        for cmd in ctx.cmd(): self.visit(cmd)
        self.indentation_level -= 1
        buffer.append(f'{self._get_indent()}}} while ({cond});')

    def obter_tipo_expressao(self, ctx: LAParser.ExpressaoContext):
        tipo_result = self.obter_tipo_termo_logico(ctx.termo_logico(0))
        if len(ctx.termo_logico()) > 1: return "logico"
        return tipo_result

    def obter_tipo_termo_logico(self, ctx: LAParser.Termo_logicoContext):
        tipo_result = self.obter_tipo_fator_logico(ctx.fator_logico(0))
        if len(ctx.fator_logico()) > 1: return "logico"
        return tipo_result

    def obter_tipo_fator_logico(self, ctx: LAParser.Fator_logicoContext):
        if ctx.getText().startswith('nao'): return "logico"
        return self.obter_tipo_parcela_logica(ctx.parcela_logica())

    def obter_tipo_parcela_logica(self, ctx: LAParser.Parcela_logicaContext):
        if ctx.getText() in ['verdadeiro', 'falso']: return "logico"
        if ctx.exp_relacional(): return self.obter_tipo_exp_relacional(ctx.exp_relacional())
        return "tipo_indefinido"

    def obter_tipo_exp_relacional(self, ctx: LAParser.Exp_relacionalContext):
        tipo_result = self.obter_tipo_exp_aritmetica(ctx.exp_aritmetica(0))
        if ctx.op_relacional(): return "logico"
        return tipo_result

    def obter_tipo_exp_aritmetica(self, ctx: LAParser.Exp_aritmeticaContext):
        tipos = {self.obter_tipo_termo(t) for t in ctx.termo()}
        if "literal" in tipos: return "literal"
        if "real" in tipos: return "real"
        return "inteiro"

    def obter_tipo_termo(self, ctx: LAParser.TermoContext):
        tipos = {self.obter_tipo_fator(f) for f in ctx.fator()}
        if "literal" in tipos: return "literal"
        if "real" in tipos: return "real"
        return "inteiro"
        
    def obter_tipo_fator(self, ctx: LAParser.FatorContext):
        tipos = {self.obter_tipo_parcela(p) for p in ctx.parcela()}
        if "literal" in tipos: return "literal"
        if "real" in tipos: return "real"
        return "inteiro"

    def obter_tipo_parcela(self, ctx: LAParser.ParcelaContext):
        if ctx.parcela_nao_unario():
            if ctx.parcela_nao_unario().CADEIA(): return "literal"
            if ctx.parcela_nao_unario().identificador():
                tipo_base = self.obter_tipo_identificador_completo(ctx.parcela_nao_unario().identificador())
                return f"^{tipo_base}"
        if ctx.parcela_unario():
            p_unario = ctx.parcela_unario()
            if p_unario.identificador():
                return self.obter_tipo_identificador_completo(p_unario.identificador())
            if p_unario.IDENT():
                simbolo = self.escopo.buscar_simbolo(p_unario.IDENT().getText())
                return simbolo.tipo if simbolo else "tipo_indefinido"
            if p_unario.NUM_INT(): return "inteiro"
            if p_unario.NUM_REAL(): return "real"
            if p_unario.expressao(): return self.obter_tipo_expressao(p_unario.expressao(0))
        return "tipo_indefinido"

    def obter_tipo_identificador_completo(self, identificador_ctx):
        nome_base = identificador_ctx.IDENT(0).getText()
        simbolo = self.escopo.buscar_simbolo(nome_base)
        if not simbolo: return "tipo_indefinido"
        tipo_atual = simbolo.tipo
        if len(identificador_ctx.IDENT()) > 1:
            campos = simbolo.campos
            if not campos:
                tipo_def = self.escopo.buscar_tipo_definido(tipo_atual)
                if tipo_def and tipo_def.registro():
                    campos = {}
                    for var_ctx in tipo_def.registro().variavel():
                        for id_ctx in var_ctx.identificador():
                            campos[id_ctx.getText()] = var_ctx.tipo().getText()
            for i in range(1, len(identificador_ctx.IDENT())):
                nome_campo = identificador_ctx.IDENT(i).getText()
                if campos and nome_campo in campos:
                    tipo_atual = campos[nome_campo]
                else:
                    return "tipo_indefinido"
        return tipo_atual

    def adicionar_erro(self, erro):
        if erro not in self.errors_set:
            self.errors.append(erro)
            self.errors_set.add(erro)

    def imprimir_erros(self):
        return "\n".join(sorted(list(self.errors_set)))