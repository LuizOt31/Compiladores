from antlr4 import *
from lexical import lexical
import sys

def main():
    if len(sys.argv) < 3:
        return

    entrada_path = FileStream(sys.argv[1], encoding="utf-8")
    saida_path = sys.argv[2]

    lexer = lexical(entrada_path)
    token = lexer.nextToken()

    with open(saida_path, mode='w') as saida:
        while token.type != Token.EOF:
            tipo = lexer.symbolicNames[token.type]

            if tipo == 'ERRO':
                linha = token.line
                caractere = token.text
                saida.write(f"Linha {linha}: {caractere} - simbolo nao identificado\n")
                break  # <-- Parar imediatamente após erro
            elif tipo in ['IDENT', 'CADEIA', 'NUM_INT', 'NUM_REAL']:
                saida.write(f"<'{token.text}',{tipo}>\n")
            else:
                saida.write(f"<'{token.text}','{token.text}'>\n")

            token = lexer.nextToken()

if __name__ == '__main__':
    main()
