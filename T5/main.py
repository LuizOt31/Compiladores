import sys
import os
from antlr4 import *
from LALexer import LALexer
from LAParser import LAParser
from antlr4.error.ErrorListener import ErrorListener
from semantico import AnalisadorSemantico


class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.syntax_errors = []
        self.lexical_errors = []
        self.parsing_completed = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol is not None:
            if offendingSymbol.text != '<EOF>':
                self.syntax_errors.append(f"Linha {line}: erro sintatico proximo a {offendingSymbol.text}")
            else:
                self.syntax_errors.append(f"Linha {line}: erro sintatico proximo a EOF")
        else:
            self.syntax_errors.append(f"Linha {line}: erro sintatico")

    def reportLexicalError(self, line, text, error_type=None):
        if error_type == "comentario_nao_fechado":
            self.lexical_errors.append(f"Linha {line}: comentario nao fechado")
        elif error_type == "cadeia_nao_fechada":
            self.lexical_errors.append(f"Linha {line}: cadeia literal nao fechada")
        else:
            self.lexical_errors.append(f"Linha {line}: {text} - simbolo nao identificado")

def main(input_file, output_file):
    try:
        input_stream = FileStream(input_file, encoding='utf-8')

        lexer = LALexer(input_stream)
        error_listener = CustomErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        token_stream = CommonTokenStream(lexer)
        token_stream.fill()

        for token in token_stream.tokens:
            if token.type == LALexer.ERRO:
                error_listener.reportLexicalError(token.line, token.text)
            elif token.type == LALexer.COMENTARIO_NAO_FECHADO:
                error_listener.reportLexicalError(token.line, token.text, "comentario_nao_fechado")
            elif token.type == LALexer.CADEIA_NAO_FECHADA:
                error_listener.reportLexicalError(token.line, token.text, "cadeia_nao_fechada")

        with open(output_file, 'w', encoding='utf-8') as f:
            if error_listener.lexical_errors:
                f.write(error_listener.lexical_errors[0] + "\n")
                f.write("Fim da compilacao\n")
                return

            token_stream.reset()
            parser = LAParser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)

            try:
                tree = parser.programa()
                error_listener.parsing_completed = True
            except Exception as e:
                if not error_listener.syntax_errors:
                
                    pass

            if error_listener.syntax_errors:
                f.write(error_listener.syntax_errors[0] + "\n")
                f.write("Fim da compilacao\n")
                return

            analyzer = AnalisadorSemantico()
            generated_code = analyzer.visit(tree)

            if analyzer.errors:
                for err in analyzer.errors:
                    f.write(err + "\n")
                f.write("Fim da compilacao\n")
            else:
                f.write(generated_code)


    except Exception as e:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Erro na compilação: {str(e)}\n")
            f.write("Fim da compilacao\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python3 main.py <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Erro: O arquivo de entrada '{input_file}' não existe.")
        sys.exit(1)

    main(input_file, output_file)