from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
import sys
from colorartLexer import colorartLexer

class CustomErrorListener(ErrorListener):
    def __init__(self, output_file):
        super().__init__()
        self.output = output_file
        self.error_found = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if self.error_found:
            return
        self.error_found = True
        
        # CORREÇÃO: Usamos a exceção 'e' para obter o texto do erro
        input_stream = e.input
        start_index = e.startIndex
        texto_invalido = input_stream.getText(start_index, start_index)
        
        mensagem_erro = f"Linha {line}:{column} erro lexico: simbolo '{texto_invalido}' nao reconhecido.\n"
        
        self.output.seek(0)
        self.output.truncate()
        self.output.write(mensagem_erro)


def main():
    '''
    Principal função do programa.
    Funciona como um validador léxico. Lê um arquivo de entrada e verifica se há
    erros léxicos.
    - Se encontrar um erro, escreve a mensagem de erro no arquivo de saída e para.
    - Se não houver erros, escreve uma mensagem de sucesso no arquivo de saída.
    '''
    if len(sys.argv) < 3:
        print("Uso: python3 seu_script.py <arquivo_entrada> <arquivo_saida>")
        return

    input_path = FileStream(sys.argv[1], encoding="utf-8")
    output_path = sys.argv[2]

    with open(output_path, 'w', encoding='utf-8') as saida:
        lexer = colorartLexer(input_path)
        lexer.removeErrorListeners()

        error_listener = CustomErrorListener(saida)
        lexer.addErrorListener(error_listener)

        while not error_listener.error_found:
            token = lexer.nextToken()
            if token.type == Token.EOF:
                break # Fim do arquivo, saia do loop

        if not error_listener.error_found:
            saida.write("Analise lexica concluida sem erros.\n")


if __name__ == '__main__':
    main()