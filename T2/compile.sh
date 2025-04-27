#!/bin/bash

# Gera os arquivos do ANTLR a partir da gramática
echo "Gerando parser e lexer da linguagem LA..."
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 LA.g4

echo "Verificando se a biblioteca antlr4-python3-runtime está instalada..."
pip install antlr4-python3-runtime

echo "Compilação concluída!"
echo "Para executar o analisador use: python main.py <arquivo_entrada> <arquivo_saida>" 