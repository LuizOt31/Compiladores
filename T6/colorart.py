# Gerador de Arte Vetorial ColorArt
# Projeto de Compiladores - Sistema de Desenho Geométrico
# Autor: Implementação baseada na estrutura do trabalho ABNT

import sys
import traceback
from antlr4 import *
from ColorArtLexer import ColorArtLexer
from ColorArtParser import ColorArtParser
from ColorArtSemantico import ColorArtSemantico
from ColorArtSemanticoUtils import ColorArtSemanticoUtils
from GeradorSVG import GeradorSVG
from antlr4.error.ErrorListener import ErrorListener

def saidaArquivo(nomeArquivo, saida):
    """Escreve a saída em um arquivo"""
    with open(nomeArquivo, 'w', encoding='utf-8') as arquivo:
        for linha in saida:
            arquivo.write(f'{linha}\n')

class ColorArtParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Erro sintático na linha {line}, coluna {column}: {msg}"
        raise SyntaxError(error_message)

class ColorArtLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        char_position = offendingSymbol.start if offendingSymbol else column
        char_value = offendingSymbol.text if offendingSymbol else "desconhecido"
        
        if char_value.strip() == '':
            error_message = f"Erro léxico na linha {line}, coluna {column}: Campo vazio detectado."
        else:
            error_message = f"Erro léxico na linha {line}, coluna {column}: {msg}. Caractere '{char_value}' na posição {char_position}."
        
        raise ValueError(error_message)

def main(argv):
    if len(argv) != 3:
        print("Uso: python colorart.py <arquivo_entrada>.ca <arquivo_saida>.svg")
        print("Exemplo: python colorart.py desenho.ca saida.svg")
        return
    
    arquivoEntrada = argv[1]
    arquivoSaida = argv[2]
    
    # Lista para armazenar a saída
    saida = []
    
    try:
        # Lendo o arquivo de entrada
        arquivo = FileStream(arquivoEntrada, encoding="utf-8")
        
        # Criando o analisador léxico
        lexer = ColorArtLexer(arquivo)
        lexer.addErrorListener(ColorArtLexerErrorListener())
        
        # Criando o fluxo de tokens
        stream = CommonTokenStream(lexer)
        
        # Criando o analisador sintático
        parser = ColorArtParser(stream)
        parser.addErrorListener(ColorArtParserErrorListener())
        
        # Executando o analisador sintático
        arvore = parser.programa()
        
        # Executando o analisador semântico
        listener = ColorArtSemantico()
        listener.visitPrograma(arvore)
        
        # Se existirem erros, eles são mostrados na saída
        for error in ColorArtSemanticoUtils.errosSemanticos:
            saida.append(error)
        
        # Se não houverem erros, o código SVG é gerado
        if len(ColorArtSemanticoUtils.errosSemanticos) == 0:
            print("Nenhum erro semântico encontrado. Gerando código SVG...")
            gerador = GeradorSVG()
            gerador.visitPrograma(arvore)
            svg_lines = gerador.gerarSVG()
            for linha in svg_lines:
                saida.append(linha)
            print(f"Arquivo SVG gerado com sucesso: {arquivoSaida}")
        else:
            print(f"Encontrados {len(ColorArtSemanticoUtils.errosSemanticos)} erros semânticos.")
        
        # Limpar erros para próxima execução
        ColorArtSemanticoUtils.limparErros()
        
    except Exception as e:
        print(f"Erro durante a compilação: {str(e)}")
        saida.append(str(e))
        saida.append(traceback.format_exc())
    
    # Escrever saída no arquivo
    saidaArquivo(arquivoSaida, saida)

if __name__ == "__main__":
    main(sys.argv) 