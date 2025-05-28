# T3 - Analisador Semântico para Linguagem LA

Este é o terceiro trabalho da disciplina de Compiladores, que consiste na implementação de um analisador semântico para a linguagem LA (Linguagem Algorítmica).

## Requisitos

- Java JDK 8 ou superior
- Python 3.6 ou superior
- ANTLR4 (o JAR está incluído no projeto)
- Biblioteca antlr4-python3-runtime

## Estrutura do Projeto

- `LA.g4`: Gramática da linguagem LA em formato ANTLR4
- `main.py`: Programa principal que executa o analisador semântico
- `scope.py`: Suporte a escopos ou tabela de símbolos
- `semantico.py`: Implementação do analisador semântico
- `test.py`: Script para executar testes automatizados
- `antlr-4.13.2-complete.jar`: Biblioteca ANTLR4 para geração do parser
- `casos-de-teste/`: Diretório com casos de teste
  - `entrada/`: Arquivos de entrada para testes
  - `saida_esperada/`: Saídas esperadas para cada teste

## Compilação

Para compilar o projeto, siga os passos abaixo:

1. Entre na pasta T3:

   ```
   cd T3
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
   **OBS:** Caso esteja rodando em um WSL, crie e ative um ambiente virtual:
      ```
      python3 -m venv .venv
      source .venv/bin/activate
      ```

4. Instale o pacote antlr4-python3-runtime:

   ```
   pip install antlr4-python3-runtime
   ```

5. Gere o analisador léxico, sintático e estrututuras para o semântico:

   ```
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor LA.g4
   ```

   Este comando irá gerar os arquivos Python necessários para o analisador léxico e sintático, incluindo LALexer.py e LAParser.py, e também irá gerar os arquivo LAVisitor.py e LAListener.py para o analisador semântico.

## Execução

Para executar o analisador semântico:

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

O script executa o analisador semântico em cada arquivo de entrada e compara a saída gerada com a saída esperada, fornecendo estatísticas e detalhes sobre os testes que passaram ou falharam.

## Funcionalidades

O analisador semântico implementa as seguintes verificações:

 - Identificador já declarado no mesmo escopo

 - Uso de tipo não declarado

 - Uso de identificador não declarado

 - Atribuição incompatível com o tipo declarado

 - Pilha de escopos para controle de visibilidade

 - Tipagem básica de expressões (inteiro, real, literal, logico)

 - Compatibilidade entre ponteiros e tipos básicos

## Exemplos de Saída

Em caso de sucesso:

```
Fim da compilacao
```

Em caso de erro semântico:

```
Linha X: <Mensagem de erro>
Fim da compilacao
```
Exemplo:
   ```
 Linha 7: tipo inteir nao declarado
Linha 11: identificador idades nao declarado
Fim da compilacao
   ```