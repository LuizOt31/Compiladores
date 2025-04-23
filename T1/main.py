from antlr4 import *
from lexical import lexical
import sys
import re
from antlr4.error.ErrorListener import ErrorListener

def main():
    '''
    Função principal do código. 
    Le os PATHs dos arquivos de entrada e saída, respectivamente, 
    e escreve no de saída os tokens da Linguagem Algoritmica no
    formato: <Palavra (ou token), Tipo do Token>
    '''
    if len(sys.argv) < 2:
        print("Erro, escreva: python3 main.py entrada.txt saida.txt\n")
        return
    
    # PATH dos arquivos
    entrada_path = FileStream(sys.argv[1], encoding="utf-8")
    saida_path = sys.argv[2]

    lexer = lexical(entrada_path)
    token = lexer.nextToken() # primeiro token do código

    # try:

    with open(saida_path, mode='w') as saida:

        # loop até acabar o arquivo de entrada (EOF é o caracter final)
        while token.type != Token.EOF:
            tipo = lexical.symbolicNames[token.type] # pega o tipo do token do arquivo .g4
            print(f" '<{token.text}', {tipo}>", file=saida)
            token = lexer.nextToken()

    # except Exception as e:
    #     error_msg = str(e)
    #     print(error_msg)



if __name__ == '__main__':
    main()