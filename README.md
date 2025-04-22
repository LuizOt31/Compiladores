# Analisador Léxico para Linguagem Jander

Este projeto implementa um analisador léxico para linguagem Jander utilizando ANTLR4 ([ANother Tool for Language Recognition](https://www.antlr.org/)). O analisador é capaz de reconhecer tokens como identificadores, palavras-chave, operadores e constantes em um arquivo de texto contendo código da linguagem.

## Alunos
- Arthur Braga da Fonseca - RA: 811461


## Estrutura do Projeto

- `lexical.g4`: Arquivo de gramática ANTLR4 que define as regras léxicas da linguagem
- `lexical.py`: Arquivo gerado pelo ANTLR4 contendo o analisador léxico
- `main.py`: Script principal para execução do analisador
- `entrada.txt`: Arquivo de exemplo contendo código na linguagem alvo
- `saida.txt`: Arquivo de saída gerado pelo analisador

## Bibliotecas Utilizadas

- **ANTLR4**: Framework para construção de analisadores lexicais e sintáticos
- **Python 3**: Linguagem de programação utilizada para implementação
- **antlr4-python3-runtime**: Biblioteca Python que permite a execução de analisadores gerados pelo ANTLR4

## Regras Léxicas

O analisador reconhece:

- Palavras-chave: `algoritmo`, `fim_algoritmo`, `declare`, `leia`, `escreva`, etc.
- Tipos de dados: `literal`, `inteiro`, `real`, `logico`
- Operadores: lógicos, aritméticos e relacionais
- Identificadores: sequências de letras e números começando com letra
- Números: inteiros e reais
- Comentários: texto entre chaves `{}`
- Texto: strings entre aspas duplas

## Como Executar

1. Certifique-se de ter o Python 3 instalado
2. Instale o pacote antlr4-python3-runtime:
   ```
   pip install antlr4-python3-runtime
   ```
3. Execute o programa passando o arquivo de entrada e o arquivo de saída:
   ```
   python main.py entrada.txt saida.txt
   ```

## Exemplo de Uso

Arquivo de entrada (`entrada.txt`):

```
{ leitura de nome e idade com escrita de mensagem usando estes dados }

algoritmo
	declare
		nome: literal
	declare
		idade: inteiro

	{ leitura de nome e idade do teclado }
	leia(nome)
	leia(idade)

	{ saída da mensagem na tela }
	escreva(nome, " tem ", idade, " anos.")
fim_algoritmo
```

Arquivo de saída (`saida.txt`):

```
 '<algoritmo', ALGORITMO>
 '<declare', DECLARE>
 '<nome', IDENT>
 '<:', TWO_POINTS>
 '<literal', LITERAL>
 ...
```

## Geração de Analisador

Para regenerar o analisador a partir da gramática:

1. Tenha o ANTLR4 instalado (disponível no arquivo `antlr-4.13.2-complete.jar`)
2. Execute:
   ```
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 lexical.g4
   ```
