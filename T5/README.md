# T5 - Gerador de Código para Linguagem LA

Este é o quinto trabalho da disciplina de Compiladores, que consiste na implementação de um **gerador de código** completo para a linguagem LA (Linguagem Algorítmica). O compilador produz código C executável equivalente ao programa LA de entrada.

## Descrição do Projeto

O T5 implementa um compilador completo que realiza:
- **Análise Léxica**: Tokenização do código fonte LA
- **Análise Sintática**: Construção da árvore sintática 
- **Análise Semântica**: Verificação de tipos, escopos e erros semânticos
- **Geração de Código**: Produção de código C compilável e executável

### Exemplo de Funcionamento

**Entrada (Linguagem LA):**
```
algoritmo
  declare
    x: inteiro
  leia(x)
  escreva(x)
fim_algoritmo
```

**Saída (Código C gerado):**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int x;
    scanf("%d", &x);
    printf("%d", x);
    return 0;
}
```

## Requisitos do Sistema

- **Java JDK 11 ou superior** (para executar o ANTLR4)
- **Python 3.6 ou superior**
- **GCC** (para compilar o código C gerado)
- **ANTLR4** (JAR incluído no projeto)
- **Biblioteca Python:** `antlr4-python3-runtime==4.13.0`

## Estrutura do Projeto

### Arquivos Principais

- `LA.g4`: Gramática da linguagem LA em formato ANTLR4
- `main.py`: Programa principal que executa o compilador completo
- `semantico.py`: Implementação do analisador semântico e gerador de código
- `scope.py`: Sistema de escopos e tabela de símbolos
- `test.py`: Script para execução automatizada dos testes
- `antlr-4.13.2-complete.jar`: Biblioteca ANTLR4 para geração do parser

### Diretórios

- `casos-de-teste/`: Casos de teste do compilador
  - `entrada/`: Programas LA para teste (20 casos)
  - `saida_esperada/`: Saídas esperadas da execução
  - `entrada-execucao/`: Entradas para os programas compilados
  - `exemplos-codigo-C/`: Exemplos de código C de referência
- `saida_gerada/`: Código C gerado pelos testes (criado automaticamente)

### Arquivos Gerados (ANTLR4)

Após compilação da gramática, são gerados:
- `LALexer.py`: Analisador léxico
- `LAParser.py`: Analisador sintático  
- `LAVisitor.py`: Interface visitor para análise semântica
- `LAListener.py`: Interface listener
- Arquivos auxiliares (`.tokens`, `.interp`)

## Instalação e Configuração

### 1. Verificar Requisitos

Verifique se possui Java 11+ instalado:
```bash
java --version
```

Verifique se possui Python 3.6+ instalado:
```bash
python3 --version
```

Verifique se possui GCC instalado:
```bash
gcc --version
```

### 2. Instalar Dependências Python

```bash
pip install -r requirements.txt
```

Ou instalar manualmente:
```bash
pip install antlr4-python3-runtime==4.13.0
```

### 3. Gerar Arquivos do ANTLR4

Execute o comando para gerar os arquivos Python a partir da gramática:
```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener LA.g4
```

## Execução

### Compilação de Arquivo Individual

Para compilar um programa LA e gerar código C:

```bash
python3 main.py <arquivo_entrada> <arquivo_saida>
```

**Exemplo:**
```bash
python3 main.py casos-de-teste/entrada/1.declaracao_leitura_impressao_inteiro.alg saida.c
```

### Execução dos Testes Automatizados

Para executar todos os 20 casos de teste:

```bash
python3 test.py
```

O script realiza:
1. Compilação do código LA para C
2. Compilação do código C com GCC
3. Execução do programa compilado
4. Comparação da saída com o resultado esperado

## Características da Linguagem LA

A linguagem LA (Linguagem Algorítmica) suporta:

### Tipos de Dados
- `inteiro`: Números inteiros
- `real`: Números reais (ponto flutuante)
- `literal`: Strings/cadeias de caracteres
- `logico`: Valores booleanos (verdadeiro/falso)
- `registro`: Estruturas de dados
- Ponteiros (prefixo `^`)

### Estruturas de Controle
- `se...entao...senao...fim_se`: Condicionais
- `caso...seja...senao...fim_caso`: Switch/case
- `para...ate...faca...fim_para`: Loop for
- `enquanto...faca...fim_enquanto`: Loop while
- `faca...ate`: Loop do-while

### Declarações
- `declare`: Declaração de variáveis
- `constante`: Declaração de constantes
- `tipo`: Declaração de tipos customizados
- `procedimento`: Declaração de procedimentos
- `funcao`: Declaração de funções

### Operações
- Aritméticas: `+`, `-`, `*`, `/`, `%`
- Relacionais: `=`, `<>`, `>=`, `<=`, `>`, `<`
- Lógicas: `e`, `ou`, `nao`
- Atribuição: `<-`

## Casos de Teste

O projeto inclui 20 casos de teste que cobrem:

1. **Declaração e I/O básico**: Inteiros, reais, literais
2. **Expressões**: Aritméticas e lógicas
3. **Estruturas condicionais**: Se-então-senão
4. **Estruturas de repetição**: Para, enquanto, faça-até
5. **Estruturas de dados**: Registros, vetores, ponteiros
6. **Subprogramas**: Procedimentos e funções
7. **Constantes e tipos**: Declarações customizadas

**Taxa de sucesso atual: 100% (20/20 testes passando)**

## Funcionamento do Compilador

### Análise Léxica e Sintática
- Utiliza ANTLR4 para tokenização e parsing
- Gramática LL(*) para linguagem LA
- Tratamento de erros léxicos e sintáticos

### Análise Semântica
- Verificação de tipos e compatibilidade
- Sistema de escopos aninhados
- Validação de declarações e uso de identificadores
- Verificação de parâmetros de funções/procedimentos

### Geração de Código
- Mapeamento direto LA → C
- Tradução de tipos: `inteiro`→`int`, `real`→`float`, `literal`→`char*`
- Tradução de operadores: `e`→`&&`, `ou`→`||`, `nao`→`!`
- Geração de estruturas de controle equivalentes
- Tratamento de registros como structs C

## Saída do Compilador

O comportamento do compilador depende da entrada:

- **Com erros**: Saída contém descrição dos erros encontrados
  ```
  Linha 10: identificador x ja declarado anteriormente
  Fim da compilacao
  ```

- **Sem erros**: Saída contém o código C gerado
  ```c
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  
  int main() {
      // código gerado
      return 0;
  }
  ```

## Arquivos de Configuração

- `requirements.txt`: Dependências Python
- `.gitignore`: Arquivos ignorados pelo Git
- `README.md`: Esta documentação

## Tratamento de Erros

O compilador detecta e reporta:
- **Erros léxicos**: Símbolos não reconhecidos, comentários/strings não fechados
- **Erros sintáticos**: Estruturas malformadas
- **Erros semânticos**: Tipos incompatíveis, identificadores não declarados, etc.

## Execução em Linha de Comando

O compilador segue o padrão exigido:
```bash
python3 main.py <arquivo_entrada> <arquivo_saida>
```

- **Argumento 1**: Caminho completo do arquivo de entrada (.alg)
- **Argumento 2**: Caminho completo do arquivo de saída (.c)
- **Saída**: Sempre salva em arquivo (nunca imprime no terminal)

## Compilação e Execução do Código Gerado

Após gerar o código C, é possível compilar e executar:

```bash
# Gerar código C
python3 main.py programa.alg programa.c

# Compilar com GCC
gcc programa.c -o programa

# Executar
./programa
```

## Desenvolvimento

Este projeto foi desenvolvido como parte da disciplina de Compiladores e implementa todos os estágios de um compilador moderno, desde a análise léxica até a geração de código executável.

---

**Autor**: [Nome do desenvolvedor]  
**Disciplina**: Construção de Compiladores  
**Instituição**: [Nome da instituição]  
**Ano**: 2025
