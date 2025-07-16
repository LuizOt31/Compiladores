import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from colorartLexer import colorartLexer
from colorartParser import colorartParser
from colorartListener import colorartListener

from semantico import AnalisadorSemantico, SemanticError

class CustomErrorListener(ErrorListener):
    """
    Listener customizado para capturar erros sintáticos e reportá-los.
    """
    def __init__(self, output_file_path):
        super().__init__()
        self.output_file_path = output_file_path

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Extrai o texto do token ofensivo
        token_text = offendingSymbol.text if offendingSymbol else 'desconhecido'
        
        # Cria a mensagem de erro
        error_message = f"Erro Sintático na Linha {line}:{column}: Próximo de '{token_text}'\n"
        
        # Escreve o erro no arquivo de saída e interrompe a execução
        with open(self.output_file_path, 'w', encoding='utf-8') as f:
            f.write(error_message)
        
        # Lança uma exceção para parar a compilação
        raise Exception(error_message)


def main():
    """
    Função principal que orquestra as fases do compilador:
    1. Análise Léxica e Sintática
    2. Análise Semântica
    """
    if len(sys.argv) < 3:
        print("Uso: python3 main.py <arquivo_entrada> <arquivo_saida>")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        # --- Fase 1: Análise Léxica e Sintática ---
        input_stream = FileStream(input_path, encoding='utf-8')
        lexer = colorartLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = colorartParser(token_stream)

        # Remove os listeners padrão e adiciona o nosso
        parser.removeErrorListeners()
        error_listener = CustomErrorListener(output_path)
        parser.addErrorListener(error_listener)
        
        # Inicia a análise sintática a partir da regra 'program'
        tree = parser.program()

        # Se a análise sintática passou (nenhuma exceção foi lançada), prosseguimos.

        # --- Fase 2: Análise Semântica ---
        # O AnalisadorSemantico é um Listener, então usamos o ParseTreeWalker
        walker = ParseTreeWalker()
        semantic_analyzer = AnalisadorSemantico() # Nossa classe do arquivo semantico.py
        walker.walk(semantic_analyzer, tree)

        # Se chegamos aqui sem levantar uma SemanticError, a análise foi um sucesso.
        with open(output_path, 'w', encoding='utf-8') as saida:
            saida.write("Analise semantica concluida sem erros.\n")
        print("Análise Semântica concluída com sucesso!")

    except SemanticError as se:
        # Captura e escreve o erro semântico que nós criamos
        with open(output_path, 'w', encoding='utf-8') as saida:
            saida.write(str(se) + "\n")
        print(se) # Mostra o erro no console
        sys.exit(1)
        
    except Exception as e:
        # Captura outros erros (sintáticos do nosso listener ou de arquivo)
        # A mensagem de erro já foi escrita no arquivo pelo listener,
        # então aqui só precisamos imprimir no console e sair.
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()