import sys
import os
from antlr4 import *
from LALexer import LALexer
from LAParser import LAParser
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.syntax_errors = []
        self.lexical_errors = []
        self.parsing_completed = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Trata erro sintático
        if offendingSymbol is not None:
            if offendingSymbol.text != '<EOF>':
                self.syntax_errors.append(f"Linha {line}: erro sintatico proximo a {offendingSymbol.text}")
            else:
                # Tratamento específico para tokens EOF
                self.syntax_errors.append(f"Linha {line}: erro sintatico proximo a EOF")
        else:
            # Se o símbolo não estiver disponível, usa uma mensagem genérica
            self.syntax_errors.append(f"Linha {line}: erro sintatico")

    def reportLexicalError(self, line, text, error_type=None):
        # Trata erro léxico com base no tipo
        if error_type == "comentario_nao_fechado":
            self.lexical_errors.append(f"Linha {line}: comentario nao fechado")
        elif error_type == "cadeia_nao_fechada":
            self.lexical_errors.append(f"Linha {line}: cadeia literal nao fechada")
        else:
            # Erro léxico padrão (símbolo não identificado)
            self.lexical_errors.append(f"Linha {line}: {text} - simbolo nao identificado")

def main(input_file, output_file):
    try:
        # Lê o arquivo de entrada
        input_stream = FileStream(input_file, encoding='utf-8')
        
        # Cria o lexer
        lexer = LALexer(input_stream)
        
        # Configura o erro customizado para o lexer
        error_listener = CustomErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)
        
        # Verifica erros léxicos através do token ERRO
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()
        
        # Verifica se há tokens de erro léxico 
        for token in token_stream.tokens:
            if token.type == LALexer.ERRO:
                error_listener.reportLexicalError(token.line, token.text)
            elif token.type == LALexer.COMENTARIO_NAO_FECHADO:
                error_listener.reportLexicalError(token.line, token.text, "comentario_nao_fechado")
            elif token.type == LALexer.CADEIA_NAO_FECHADA:
                error_listener.reportLexicalError(token.line, token.text, "cadeia_nao_fechada")
        
        # Se não houver erros léxicos, segue para análise sintática
        if not error_listener.lexical_errors:
            token_stream.reset()  # Resetar o stream para iniciar a análise sintática
            
            # Cria o parser
            parser = LAParser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            
            # Executa a análise sintática
            try:
                parser.programa()  # Inicia a análise a partir da regra inicial
                error_listener.parsing_completed = True
            except Exception as e:
                # Em caso de erro de parsing não capturado pelo ErrorListener
                if not error_listener.syntax_errors:
                    error_listener.syntax_errors.append(f"Erro de parsing: {str(e)}")
        
        # Gera o arquivo de saída
        with open(output_file, 'w', encoding='utf-8') as f:
            # Se houver erros léxicos, eles têm prioridade sobre os sintáticos
            if error_listener.lexical_errors:
                f.write(error_listener.lexical_errors[0] + "\n")
            elif error_listener.syntax_errors:
                f.write(error_listener.syntax_errors[0] + "\n")
            elif error_listener.parsing_completed:
                f.write("Fim da compilacao\n")
            else:
                f.write("Erro desconhecido durante a compilação\n")
            
            # No final do arquivo, sempre adiciona a mensagem de fim de compilação
            if not (error_listener.parsing_completed and not (error_listener.lexical_errors or error_listener.syntax_errors)):
                f.write("Fim da compilacao\n")

    except Exception as e:
        # Em caso de erro não tratado
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Erro na compilação: {str(e)}\n")
            f.write("Fim da compilacao\n")

if __name__ == '__main__':
    # Verifica se o número correto de argumentos foi fornecido
    if len(sys.argv) != 3:
        print("Uso: python3 main.py <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Verifica se o arquivo de entrada existe
    if not os.path.isfile(input_file):
        print(f"Erro: O arquivo de entrada '{input_file}' não existe.")
        sys.exit(1)
    
    main(input_file, output_file) 