# T2 - Analisador Sintático para Linguagem LA

Este é o segundo trabalho da disciplina de Compiladores, que consiste na implementação de um analisador sintático para a linguagem LA (Linguagem Algorítmica).

## Requisitos

- Java JDK 8 ou superior
- Python 3.6 ou superior
- ANTLR4 (o JAR está incluído no projeto)
- Biblioteca antlr4-python3-runtime

## Estrutura do Projeto

- `LA.g4`: Gramática da linguagem LA em formato ANTLR4
- `main.py`: Programa principal que executa o analisador sintático
- `antlr-4.13.2-complete.jar`: Biblioteca ANTLR4 para geração do parser
- `test.py`: Script para executar testes automatizados
- `casos-de-teste/`: Diretório com casos de teste
  - `entrada/`: Arquivos de entrada para testes
  - `saida_esperada/`: Saídas esperadas para cada teste

## Compilação

Para compilar o projeto, siga os passos abaixo:

1. Entre na pasta T2:

   ```
   cd T2
   ```

2. Certifique-se de ter o Java 11 ou superior instalado para executar o ANTLR4:

   ```
   java --version
   ```

   Obs: O ANTLR tool requer Java 11+, enquanto o runtime Java requer Java 8+.

3. Certifique-se de ter o Python 3 instalado

   ```
   python3 --version
   ```

4. Instale o pacote antlr4-python3-runtime:

   ```
   pip install antlr4-python3-runtime
   ```

5. Gere o analisador léxico e sintático:

   ```
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 LA.g4
   ```

   Este comando irá gerar os arquivos Python necessários para o analisador léxico e sintático, incluindo LALexer.py e LAParser.py, entre outros.

## Execução

Para executar o analisador sintático:

```bash
python3 main.py <arquivo_entrada> <arquivo_saida>
```

Onde:

- `<arquivo_entrada>`: Caminho para o arquivo com o código-fonte em linguagem LA
- `<arquivo_saida>`: Caminho para o arquivo onde será gravada a saída do analisador

## Testes Automatizados

O projeto inclui um sistema de testes automatizados que verifica se o analisador está produzindo as saídas corretas para os casos de teste fornecidos.

Para executar os testes:

```bash
python3 test.py
```

Por padrão, o script de teste usará:

- Arquivos de entrada: `casos-de-teste/entrada/*.txt`
- Saídas esperadas: `casos-de-teste/saida_esperada/*.txt`
- Diretório para saídas geradas: `saida_gerada/`

Você também pode especificar diretórios personalizados:

```bash
python3 test.py <dir_entrada> <dir_saida_esperada> <dir_saida_gerada>
```

O script executa o analisador sintático em cada arquivo de entrada e compara a saída gerada com a saída esperada, fornecendo estatísticas e detalhes sobre os testes que passaram ou falharam.

## Funcionalidades

O analisador sintático identifica:

- Erros léxicos (tokens não reconhecidos, comentários e cadeias não fechados)
- Erros sintáticos (estrutura do programa inadequada)

## Exemplos de Saída

Em caso de sucesso:

```
Fim da compilacao
```

Em caso de erro léxico:

```
Linha X: Y - simbolo nao identificado
Fim da compilacao
```

Em caso de erro sintático:

```
Linha X: erro sintatico proximo a Y
Fim da compilacao
```

