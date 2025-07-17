# T6 - Analisador Léxico para Linguagem ColorArt

Este é o sexto trabalho da disciplina de Compiladores, que consiste na implementação de um **analisador léxico** para a linguagem ColorArt - uma linguagem de domínio específico para criação de desenhos e gráficos vetoriais.

## Descrição do Projeto

O T6 implementa um analisador léxico que realiza:
- **Tokenização**: Reconhecimento dos tokens da linguagem ColorArt
- **Validação Léxica**: Detecção de símbolos não reconhecidos
- **Tratamento de Erros**: Relatório detalhado de erros léxicos encontrados

### Exemplo de Funcionamento

**Entrada (Linguagem ColorArt):**
```colorart
canvas 800x600;

color red = #FF0000;
color blue = #0000FF;

circle 100 100 radius 50 fill red;
rectangle 200 150 width 100 height 80 fill blue;
line 50 50 to 300 300 stroke red;
```

**Saída (Análise bem-sucedida):**
```
Analise lexica concluida sem erros.
```

**Saída (Com erro léxico):**
```
Linha 5:10 erro lexico: simbolo '@' nao reconhecido.
```

## Requisitos do Sistema

- **Java JDK 11 ou superior** (para executar o ANTLR4)
- **Python 3.6 ou superior**
- **ANTLR4** (JAR incluído no projeto)
- **Biblioteca Python:** `antlr4-python3-runtime`

## Estrutura do Projeto

### Arquivos Principais

- `colorart.g4`: Gramática da linguagem ColorArt em formato ANTLR4
- `main.py`: Programa principal que executa o analisador léxico
- `exemplo.py`: Exemplo de geração de SVG usando svgwrite
- `antlr-4.13.2-complete.jar`: Biblioteca ANTLR4 para geração do lexer

### Diretórios

- `casos-de-teste/`: Casos de teste do analisador
  - `lexico/entrada/`: Programas ColorArt para teste (5 casos)
  - `lexico/saida/`: Saídas esperadas dos testes léxicos
  - `sintatico/`: Casos de teste sintáticos (futuros)
- `.antlr/`: Arquivos temporários do ANTLR4
- `__pycache__/`: Cache do Python

### Arquivos Gerados (ANTLR4)

Após compilação da gramática, são gerados:
- `colorartLexer.py`: Analisador léxico principal
- `colorartParser.py`: Analisador sintático (para uso futuro)
- `colorartListener.py`: Interface listener
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

### 2. Instalar Dependências Python

```bash
pip install antlr4-python3-runtime
```

Para o exemplo SVG (opcional):
```bash
pip install svgwrite
```

### 3. Gerar Arquivos do ANTLR4

Execute o comando para gerar os arquivos Python a partir da gramática:
```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener colorart.g4
```

## Execução

### Análise de Arquivo Individual

Para analisar um programa ColorArt:

```bash
python3 main.py <arquivo_entrada> <arquivo_saida>
```

**Exemplo:**
```bash
python3 main.py casos-de-teste/lexico/entrada/1-teste-colorart.txt saida.txt
```

### Execução do Exemplo SVG

Para gerar um exemplo de SVG:
```bash
python3 exemplo.py
```

Isso criará o arquivo `output.svg` com formas geométricas.

## Características da Linguagem ColorArt

A linguagem ColorArt é uma DSL (Domain Specific Language) para criação de desenhos vetoriais que suporta:

### Declaração de Canvas
```colorart
canvas 800x600;  // Define área de desenho de 800x600 pixels
```

### Definição de Cores
```colorart
color red = #FF0000;     // Cor vermelha
color blue = #0000FF;    // Cor azul
color green = #00FF00;   // Cor verde
```

### Formas Geométricas

**Círculos:**
```colorart
circle 100 100 radius 50 fill red;  // Círculo em (100,100) com raio 50
```

**Retângulos:**
```colorart
rectangle 200 150 width 100 height 80 fill blue;  // Retângulo 100x80
```

**Linhas:**
```colorart
line 50 50 to 300 300 stroke red;  // Linha de (50,50) até (300,300)
```

### Tokens Reconhecidos

- **Palavras-chave**: `canvas`, `color`, `circle`, `rectangle`, `line`, `radius`, `width`, `height`, `fill`, `stroke`, `to`
- **Operadores**: `=`, `x` (para dimensões)
- **Identificadores**: Nomes de variáveis `[a-zA-Z_][a-zA-Z_0-9]*`
- **Cores Hexadecimais**: `#[0-9a-fA-F]{6}`
- **Números Inteiros**: `[0-9]+`
- **Comentários**: `% comentário até o final da linha`
- **Delimitadores**: `;`

## Casos de Teste

O projeto inclui 5 casos de teste léxicos que cobrem:

1. **Teste 1**: Programa básico válido (canvas + cor + círculo)
2. **Teste 2**: Programa com erros léxicos (vírgula inválida, símbolo #)
3. **Teste 3**: Teste com identificadores e estruturas válidas
4. **Teste 4**: Teste de tokens específicos
5. **Teste 5**: Programa mais complexo com múltiplas formas

## Funcionamento do Analisador Léxico

### Tokenização
- Utiliza ANTLR4 para reconhecimento de padrões
- Gramática regular para tokens da linguagem
- Tratamento de espaços em branco e comentários

### Tratamento de Erros
- Detecção de símbolos não reconhecidos
- Relatório de erro com linha e coluna
- Parada na primeira ocorrência de erro

### Saída do Analisador

O comportamento do analisador depende da entrada:

- **Sem erros léxicos**:
  ```
  Analise lexica concluida sem erros.
  ```

- **Com erros léxicos**:
  ```
  Linha 5:10 erro lexico: simbolo '@' nao reconhecido.
  ```

## Execução em Linha de Comando

O analisador segue o padrão exigido:
```bash
python3 main.py <arquivo_entrada> <arquivo_saida>
```

- **Argumento 1**: Caminho completo do arquivo de entrada (.txt)
- **Argumento 2**: Caminho completo do arquivo de saída (.txt)
- **Saída**: Sempre salva em arquivo (nunca imprime no terminal)

## Geração de SVG (Exemplo)

O arquivo `exemplo.py` demonstra como os desenhos ColorArt podem ser convertidos para formato SVG:

```python
import svgwrite

dwg = svgwrite.Drawing('output.svg', size=('800px', '600px'))
dwg.add(dwg.circle(center=(100, 100), r=50, fill='red'))
dwg.add(dwg.rect(insert=(200, 150), size=(100, 80), fill='blue'))
dwg.add(dwg.line(start=(50, 50), end=(300, 300), stroke='green'))
dwg.save()
```

## Extensões Futuras

O projeto pode ser estendido com:
- Análise sintática completa
- Análise semântica (verificação de cores declaradas)
- Gerador de código SVG automático
- Suporte a mais formas geométricas (polígonos, elipses)
- Transformações (rotação, escala, translação)

## Arquivos de Configuração

- `.gitignore`: Arquivos ignorados pelo Git (gerados pelo ANTLR4, cache Python)
- `README.md`: Esta documentação

## Estrutura da Gramática

A gramática `colorart.g4` define:
- **Programa**: Declaração de canvas seguida de declarações de cor e forma
- **Declarações**: Canvas, cores e formas geométricas
- **Tokens**: Identificadores, números, cores hexadecimais
- **Comentários**: Linhas iniciadas com `%`
