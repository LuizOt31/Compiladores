# Analisador Léxico para LA (Linguagem Algorítmica)

Este projeto implementa um analisador léxico para a Linguagem Algorítmica (LA) desenvolvida pelo prof. Jander, no âmbito do DC/UFSCar. O analisador utiliza ANTLR4 ([ANother Tool for Language Recognition](https://www.antlr.org/)) para identificar tokens como identificadores, palavras-chave, operadores e constantes em um arquivo de texto contendo código da linguagem.

## Membros do Grupo

- Arthur Braga da Fonseca - RA: 811461
- Luiz Otávio Teixeira Mello - RA: 811967
- Leonardo Triiltz Siqueira- RA: 811904

## Estrutura do Projeto

- `lexical.g4`: Arquivo de gramática ANTLR4 que define as regras léxicas da linguagem
- `lexical.py`: Arquivo gerado pelo ANTLR4 contendo o analisador léxico
- `main.py`: Script principal para execução do analisador
- `entrada.txt`: Arquivo de exemplo contendo código na linguagem LA
- `saida.txt`: Arquivo de saída gerado pelo analisador

## Tratamento de Erros

O analisador léxico identifica e reporta os seguintes erros:

- Símbolos não identificados
- Comentários não fechados na mesma linha
- Cadeias de caracteres não fechadas na mesma linha

Quando um erro léxico é encontrado, o programa interrompe a execução e reporta o erro, indicando o símbolo e a linha onde o erro ocorre.

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação utilizada para implementação

## Bibliotecas Utilizadas

- **ANTLR4**: Framework para construção de analisadores lexicais e sintáticos
- **antlr4-python3-runtime**: Biblioteca Python que permite a execução de analisadores gerados pelo ANTLR4

## Regras Léxicas

O analisador reconhece:

- Palavras-chave: `algoritmo`, `fim_algoritmo`, `declare`, `leia`, `escreva`, etc.
- Tipos de dados: `literal`, `inteiro`, `real`, `logico`
- Operadores: lógicos, aritméticos e relacionais
- Identificadores: sequências de letras e números começando com letra
- Números: inteiros e reais
- Comentários: texto entre chaves `{}`
- Cadeias de caracteres: texto entre aspas duplas

## Pré-requisitos e Ordem de Execução

1. Certifique-se de ter o Java instalado para executar o ANTLR4

   ```
   java --version
   ```

2. Certifique-se de ter o Python 3 instalado

   ```
   python3 --version
   ```

3. Instale o pacote antlr4-python3-runtime:

   ```
   pip install antlr4-python3-runtime
   ```

4. Gere o analisador léxico:

   ```
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 lexical.g4
   ```

   Este comando irá gerar os arquivos Python necessários para o analisador léxico.

5. Agora você pode executar o programa principal:
   ```
   python3 main.py <arquivo_de_entrada> <arquivo_de_saida>
   ```
   Obs: Os símbolos `<` e `>` são apenas ilustrativos, não devem ser incluídos no comando. Por exemplo:
   ```
   python3 main.py entrada.txt saida.txt
   ```

## Como Executar

Para executar o analisador léxico, após seguir os pré-requisitos acima, use o comando:

```
python3 main.py <arquivo_de_entrada> <arquivo_de_saida>
```

## Geração de Analisador

Para regenerar o analisador a partir da gramática:

1. Tenha o ANTLR4 instalado (disponível no arquivo `antlr-4.13.2-complete.jar`)
2. Execute:
   ```
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 lexical.g4
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
<'algoritmo','algoritmo'>
<'declare','declare'>
<'nome',IDENT>
<':',':'>
<'literal','literal'>
<'declare','declare'>
<'idade',IDENT>
<':',':'>
<'inteiro','inteiro'>
<'leia','leia'>
<'(','('>
<'nome',IDENT>
<')',')'>
<'leia','leia'>
<'(','('>
<'idade',IDENT>
<')',')'>
<'escreva','escreva'>
<'(','('>
<'nome',IDENT>
<',',','>
<'" tem "',CADEIA>
<',',','>
<'idade',IDENT>
<',',','>
<'" anos."',CADEIA>
<')',')'>
<'fim_algoritmo','fim_algoritmo'>
```

## Exemplo de Erro Léxico

Entrada com erro:

```
algoritmo
	declare
		nome~ literal
	declare
		idade: inteiro

	leia(nome)
	leia(idade)

	escreva(nome, " tem ", idade, " anos.")
fim_algoritmo
```

Saída produzida:

```
<'algoritmo','algoritmo'>
<'declare','declare'>
<'nome',IDENT>
Linha 3: ~ - simbolo nao identificado
```

## Testes Automatizados

O projeto inclui um conjunto de casos de teste automatizados para verificar o funcionamento correto do analisador léxico. Os testes estão localizados no diretório `testes/`.

### Estrutura dos Testes

- `testes/entrada/`: Contém os arquivos de entrada para teste
- `testes/saida_esperada/`: Contém os arquivos com as saídas esperadas
- `test.py`: Script Python que executa os testes automaticamente

### Como Executar os Testes

1. Certifique-se de que o analisador léxico foi gerado (passo 4 da seção Pré-requisitos)
2. Execute o script de testes:
   ```
   python3 test.py
   ```

O script irá:

1. Processar cada arquivo de entrada na pasta `testes/entrada/`
2. Comparar a saída gerada com o arquivo esperado em `testes/saida_esperada/`
3. Reportar quais testes passaram e quais falharam
4. Mostrar um resumo final com o número total de testes e quantos foram bem-sucedidos
