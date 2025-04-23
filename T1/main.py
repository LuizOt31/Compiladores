from antlr4 import *
from lexical import lexical
from antlr4.error.ErrorListener import ErrorListener
import sys
import re

class CustomErrorListener(ErrorListener):
    '''
    Classe para tratar erros lexicos
    Herda ErrorListener, para que em cada token que 
    não for identificado, a classe será chamada para tratar.
    '''
    def __init__(self, output):
        super().__init__()
        self.output = output
        self.error_found = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        '''
        Funcao que realmente trata os erros de:
            * comentários não fechados na mesma linha
            * cadeias não fechadas
            * simbolos não identificados
        '''
        self.error_found = True

        # Comentário não fechado
        if '{' in msg and ('EOF' in msg or '\\n' in msg or '\\r' in msg):
            print(f"Linha {line}: comentario nao fechado", file=self.output)

        # Cadeia literal não fechada
        elif '"' in msg and ('EOF' in msg or '\\n' in msg or '\\r' in msg):
            print(f"Linha {line}: cadeia literal nao fechada", file=self.output)

        # Símbolo não identificado
        else:
            simbolo = re.search(r"'(.*?)'", msg)
            texto = simbolo.group(1) if simbolo else offendingSymbol.text
            print(f"Linha {line}: {texto} - simbolo nao identificado", file=self.output)

def main():
    '''
    Principal função do programa.
    Le dois argumentos, os PATHs de arquivo de entrada e saída, respectivamente, e
    imprime na saída os tokens com seus tipos no
    estilo: <token, tipo token>
    '''

    if len(sys.argv) < 3:
        print("Uso: python script.py <arquivo_entrada> <arquivo_saida>")
        return

    # paths arquivo entrada e saída
    entrada_path = FileStream(sys.argv[1], encoding="utf-8")
    saida_path = sys.argv[2]

    # abrindo arquivo de saída para escrever nele
    with open(saida_path, mode='w') as saida:

        lexer = lexical(entrada_path)

        lexer.removeErrorListeners()

        listener = CustomErrorListener(saida)
        lexer.addErrorListener(listener)

        while True:
            token = lexer.nextToken()

            # Se atingir o final do arquio (EOF), para o loop
            if token.type == Token.EOF or listener.error_found:
                break

            # Só processa tokens do canal principal
            if token.channel == Token.DEFAULT_CHANNEL:
                tipo = lexer.symbolicNames[token.type]
                if tipo in ['IDENT', 'CADEIA', 'NUM_INT', 'NUM_REAL']:
                    print(f"<'{token.text}',{tipo}>", file=saida)
                else:
                    print(f"<'{token.text}','{token.text}'>", file=saida)

if __name__ == '__main__':
    main()
