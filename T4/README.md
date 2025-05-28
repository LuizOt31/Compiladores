# T4 - Analisador Semântico para Linguagem LA

Este é o quarto trabalho da disciplina de Compiladores, que consiste na implementação de um analisador semântico completo para a linguagem LA (Linguagem Algorítmica).

## Requisitos

- Java JDK 11 ou superior (para executar o ANTLR4)
- Python 3.6 ou superior
- ANTLR4 (o JAR está incluído no projeto)
- Biblioteca antlr4-python3-runtime

## Estrutura do Projeto

### Arquivos Principais

- `LA.g4`: Gramática da linguagem LA em formato ANTLR4
- `main.py`: Programa principal que executa o analisador semântico
- `semantico.py`: Implementação completa do analisador semântico
- `scope.py`: Sistema de escopos e tabela de símbolos
- `test.py`: Script para executar testes automatizados
- `antlr-4.13.2-complete.jar`: Biblioteca ANTLR4 para geração do parser

### Diretórios

- `casos-de-teste/`: Diretório com casos de teste
  - `entrada/`: Arquivos de entrada para testes (9 casos de teste)
  - `saida/`: Saídas esperadas para cada teste
- `saida_gerada/`: Diretório onde são geradas as saídas dos testes
- `.venv/`: Ambiente virtual Python (se criado)

### Arquivos de Configuração

- `.gitignore`: Ignora arquivos gerados automaticamente
- `README.md`: Este arquivo

## Instalação e Configuração

1. **Clone ou acesse o diretório T4:**

   ```bash
   cd T4
   ```

2. **Verifique se tem Java 11+ instalado:**

   ```bash
   java --version
   ```

3. **Verifique se tem Python 3 instalado:**

   ```bash
   python3 --version
   ```

4. **Instale as dependências:**
   ```bash
   pip install antlr4-python3-runtime
   ```

## Compilação

Para gerar os arquivos necessários do ANTLR4:

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener LA.g4
```

Este comando gera os seguintes arquivos:

- `LALexer.py`: Analisador léxico
- `LAParser.py`: Analisador sintático
- `LAVisitor.py`: Interface visitor para análise semântica
- `LAListener.py`: Interface listener
- Arquivos auxiliares (`.tokens`, `.interp`)

## Execução

### Execução Individual

Para analisar um arquivo específico:

```bash
python3 main.py <arquivo_entrada> <arquivo_saida>
```

**Exemplo:**

```bash
python3 main.py casos-de-teste/entrada/1.algoritmo_7-2_apostila_LA.txt saida.txt
```

### Execução dos Testes Automatizados

Para executar todos os casos de teste:

```bash
python3 test.py
```

Ou especificando diretórios customizados:

```bash
python3 test.py <dir_entrada> <dir_saida_esperada> <dir_saida_gerada>
```

## Casos de Teste

O projeto inclui 9 casos de teste que cobrem:

1. **Teste 1**: Atribuição incompatível com ponteiros
2. **Teste 2**: Atribuição incompatível em campos de registro
3. **Teste 3**: Identificadores case-sensitive e campos de registro
4. **Teste 4**: Incompatibilidade de parâmetros em funções
5. **Teste 5**: Arrays e identificadores não declarados
6. **Teste 6**: Comando retorne em escopo inadequado
7. **Teste 7**: Comando retorne em procedimento
8. **Teste 8**: Identificadores já declarados
9. **Teste 9**: Identificadores duplicados

**Taxa de sucesso atual: 100% (9/9 testes passando)**

## Exemplos de Saída

### Sucesso (sem erros):

```
Fim da compilacao
```

### Com erros semânticos:

```
Linha 10: identificador tVinho ja declarado anteriormente
Linha 16: identificador vinho.Preco nao declarado
Linha 28: identificador vinhocaro.tipoVinho nao declarado
Fim da compilacao
```
