from antlr4 import *
from colorartLexer import colorartLexer
from antlr4.error.ErrorListener import ErrorListener
import sys
import re

class CustomErrorListener(ErrorListener):
    def __init__(self, output):
        super().__init__()
        self.output = output
        self.error_found = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.error_found = True
        simbolo = re.search(r"'(.*?)'", msg)
        texto = simbolo.group(1) if simbolo else offendingSymbol.text
        print(f"Linha {line}: {texto} - simbolo nao identificado", file=self.output)

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 script.py <arquivo_entrada> <arquivo_saida>")
        return

    entrada_path = FileStream(sys.argv[1], encoding="utf-8")
    saida_path = sys.argv[2]

    with open(saida_path, mode='w') as saida:
        lexer = colorartLexer(entrada_path)
        lexer.removeErrorListeners()
        listener = CustomErrorListener(saida)
        lexer.addErrorListener(listener)

        while True:
            token = lexer.nextToken()

            if token.type == Token.EOF or listener.error_found:
                break

            if token.channel == Token.DEFAULT_CHANNEL:
                # Verifica se o tipo do token está dentro dos limites de symbolicNames
                if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] is not None:
                    tipo = lexer.symbolicNames[token.type]
                    if tipo in ['VAR', 'HEXCOLOR', 'INT']:
                        print(f"<'{token.text}',{tipo}>", file=saida)
                    else:
                        print(f"<'{token.text}','{token.text}'>", file=saida)
                else:
                    # Token não reconhecido - isso não deveria acontecer se o error listener estiver funcionando
                    print(f"<'{token.text}',UNKNOWN>", file=saida)

if __name__ == '__main__':
    main()