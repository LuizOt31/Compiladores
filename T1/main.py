from antlr4 import *
from lexical import lexical
import sys
import re


def main():
    if len(sys.argv) < 2:
        print("Erro, escreva: python3 main.py entrada.txt saida.txt\n")
        return
    
    entrada_path = FileStream(sys.argv[1], encoding="utf-8")
    saida_path = sys.argv[2]

    lexer = lexical(entrada_path)
    token = lexer.nextToken()

    with open(saida_path, mode='w') as saida:

        while token.type != Token.EOF:
            tipo = lexical.symbolicNames[token.type]
            print(f" '<{token.text}', {tipo}>", file=saida)
            token = lexer.nextToken()

if __name__ == '__main__':
    main()