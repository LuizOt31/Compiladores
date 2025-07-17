# compiler.py
import sys
from antlr4 import *
from colorartLexer import colorartLexer
from colorartParser import colorartParser
from generateCode import CodeGenerator

def main(argv):
    if len(argv) < 3:
        print("Uso: python3 compiler.py <arquivo_entrada.cal> <arquivo_saida.py>")
        return

    input_stream = FileStream(argv[1], encoding="utf-8")
    output_py_path = argv[2]
    
    # Extrai o nome do arquivo de saída para o SVG
    # Ex: se a saída for 'output/result.py', o svg será 'output/result.svg'
    svg_filename = output_py_path.replace(".py", ".svg")

    # 1. Lexer
    lexer = colorartLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # 2. Parser
    parser = colorartParser(stream)
    tree = parser.program() # Começa a análise pela regra 'program'

    # 3. Code Generation
    # O nome do arquivo SVG que será salvo pelo script gerado
    generator = CodeGenerator(svg_filename) 
    walker = ParseTreeWalker()
    walker.walk(generator, tree)

    # Escreve o código Python gerado no arquivo de saída
    generated_code = generator.get_generated_code()
    with open(output_py_path, 'w', encoding='utf-8') as f:
        f.write(generated_code)
    
    print(f"Compilação concluída! Script Python gerado em '{output_py_path}'")
    print(f"Para gerar o SVG, execute: python3 {output_py_path}")


if __name__ == '__main__':
    main(sys.argv)