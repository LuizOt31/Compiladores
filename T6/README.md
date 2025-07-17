# ColorArt - Linguagem de Desenho Geométrico

## Visão Geral

ColorArt é uma linguagem específica de domínio (DSL) para criação de desenhos vetoriais simples usando SVG. A linguagem permite definir cores, variáveis e desenhar formas geométricas básicas.

## Instalação e Dependências

### Pré-requisitos
- Python 3.7+
- ANTLR4 runtime para Python

```bash
pip install antlr4-python3-runtime
```

### Compilação da Gramática
```bash
java -jar antlr-4.13.0-complete.jar -visitor -Dlanguage=Python3 ColorArt.g4
```

## Execução

```bash
python3 colorart.py <arquivo_entrada>.ca <arquivo_saida>.svg
```

**Exemplo:**
```bash
python3 colorart.py casos-de-teste/entradas/teste1.ca saida.svg
```

## Testador Automático

Para executar todos os casos de teste automaticamente:

```bash
python3 testador.py
```

O testador irá:
- Executar todos os arquivos `.ca` da pasta `casos-de-teste/entradas/`
- Comparar as saídas com os arquivos esperados em `casos-de-teste/saidas-esperadas/`
- Gerar relatório de sucessos e falhas

## Testador de Erros

Para validar a detecção de erros do compilador:

```bash
python3 testador_erros.py
```

O testador de erros irá:
- Executar casos de teste que devem gerar erros
- Validar se os tipos corretos de erro são detectados
- Verificar erros léxicos, sintáticos e semânticos

### Casos de Teste de Erro

#### Erros Léxicos
- **`teste_erro_lexico.ca`** - Caracteres inválidos (ex: `@` em identificadores)

#### Erros Sintáticos  
- **`teste_erro_sintatico.ca`** - Sintaxe incorreta (chaves não fechadas, vírgulas ausentes)

#### Erros Semânticos
- **`teste_erro_semantico.ca`** - Cores não declaradas e declarações duplicadas
- **`teste_erro_variavel.ca`** - Variáveis duplicadas
- **`teste_erro_complexo.ca`** - Múltiplos erros semânticos (7 erros detectados)

### Resultados Esperados

```
============================================================
TESTADOR DE ERROS - COLORART
============================================================
Executando 5 teste(s) de erro

Teste teste_erro_lexico.ca: Erro léxico - caractere inválido
  Esperado: LEXICO -> PASSOU ✅
Teste teste_erro_sintatico.ca: Erro sintático - sintaxe incorreta
  Esperado: SINTATICO -> PASSOU ✅
Teste teste_erro_semantico.ca: Erro semântico - cores não declaradas
  Esperado: SEMANTICO -> PASSOU ✅
Teste teste_erro_variavel.ca: Erro semântico - variável duplicada
  Esperado: SEMANTICO -> PASSOU ✅
Teste teste_erro_complexo.ca: Erro semântico - múltiplos erros
  Esperado: SEMANTICO -> PASSOU ✅

============================================================
RESULTADO: 5/5 testes de erro passaram
✅ Todos os testes de erro passaram!
   O compilador está detectando corretamente os erros!
============================================================
```

## Sintaxe da Linguagem

### Declaração de Cores
```
cor { id=<nome>, valor="<valor_hex>" }
```

**Exemplo:**
```
cor { id=vermelho, valor="#FF0000" }
cor { id=azul, valor="#0000FF" }
```

### Declaração de Variáveis
```
variavel { id=<nome>, tipo=<tipo>, valor=<valor> }
```

**Tipos suportados:** `inteiro`, `cor`

**Exemplo:**
```
variavel { id=raio_padrao, tipo=inteiro, valor=50 }
variavel { id=cor_fundo, tipo=cor, valor=azul }
```

### Formas Geométricas

#### Círculo
```
circulo { centro=[x, y], raio=r [, cor=[cor_id]] [, borda=[cor_id]] }
```

#### Retângulo
```
retangulo { posicao=[x, y], largura=w, altura=h [, cor=[cor_id]] [, borda=[cor_id]] }
```

#### Linha
```
linha { inicio=[x1, y1], fim=[x2, y2] [, cor=[cor_id]] [, espessura=n] }
```

#### Polígono
```
poligono { pontos=[x1,y1, x2,y2, x3,y3, ...] [, cor=[cor_id]] [, borda=[cor_id]] }
```

## Exemplos

### Exemplo 1: Formas Básicas
```
// Definindo cores
cor { id=vermelho, valor="#FF0000" }
cor { id=azul, valor="#0000FF" }
cor { id=verde, valor="#00FF00" }

// Desenhando formas
circulo { centro=[100, 100], raio=50, cor=[vermelho] }
retangulo { posicao=[200, 50], largura=100, altura=80, cor=[azul], borda=[verde] }
linha { inicio=[50, 200], fim=[300, 250], cor=[verde], espessura=3 }
```

### Exemplo 2: Casa Simples
```
// Cores
cor { id=laranja, valor="#FFA500" }
cor { id=roxo, valor="#800080" }
cor { id=preto, valor="#000000" }

// Casa
retangulo { posicao=[100, 200], largura=200, altura=150, cor=[laranja], borda=[preto] }

// Telhado
poligono { pontos=[100,200, 200,100, 300,200], cor=[roxo], borda=[preto] }

// Porta
retangulo { posicao=[170, 280], largura=60, altura=70, cor=[preto] }
```

## Características da Linguagem

### Validações Semânticas
- Verificação de cores declaradas antes do uso
- Detecção de declarações duplicadas
- Validação de tipos de variáveis

### Saída SVG
- Gera código SVG padrão (800x600)
- Suporte completo a cores hexadecimais
- Elementos SVG compatíveis com navegadores

### Tratamento de Erros
- Erros léxicos, sintáticos e semânticos
- Mensagens de erro com linha e coluna
- Relatório detalhado de problemas

## Estrutura do Projeto

```
color-art/
├── ColorArt.g4                    # Gramática ANTLR4
├── colorart.py                    # Programa principal
├── testador.py                    # Testador automático (casos funcionais)
├── testador_erros.py              # Testador de erros (validação)
├── ColorArtSemantico.py           # Analisador semântico
├── GeradorSVG.py                  # Gerador de código SVG
├── TabelaDeSimbolos.py            # Tabela de símbolos
├── ColorArtSemanticoUtils.py      # Utilitários semânticos
├── casos-de-teste/
│   ├── entradas/                  # Arquivos de teste (.ca)
│   │   ├── teste1.ca             # Formas básicas
│   │   ├── teste2.ca             # Casa simples
│   │   ├── teste3.ca             # Paisagem complexa
│   │   ├── teste_erro_lexico.ca  # Erro léxico
│   │   ├── teste_erro_sintatico.ca # Erro sintático
│   │   ├── teste_erro_semantico.ca # Erro semântico
│   │   ├── teste_erro_variavel.ca  # Variável duplicada
│   │   └── teste_erro_complexo.ca  # Múltiplos erros
│   ├── saidas-esperadas/          # Saídas SVG de referência
│   └── saidas/                    # Saídas geradas pelos testes
├── antlr-4.13.0-complete.jar     # ANTLR4 JAR
└── README.md                      # Esta documentação
```

## Casos de Teste

### Testes Funcionais

#### Teste 1: Formas Básicas
- **Entrada:** `casos-de-teste/entradas/teste1.ca`
- **Descrição:** Círculo, retângulo e linha com cores básicas
- **Saída:** SVG com formas geométricas simples

#### Teste 2: Casa Simples
- **Entrada:** `casos-de-teste/entradas/teste2.ca`
- **Descrição:** Desenho de uma casa com polígono (telhado) e formas básicas
- **Saída:** SVG representando uma casa colorida

#### Teste 3: Paisagem Complexa
- **Entrada:** `casos-de-teste/entradas/teste3.ca`
- **Descrição:** Paisagem com sol, montanhas, casa e múltiplas cores
- **Saída:** SVG complexo demonstrando todas as funcionalidades

### Testes de Erro

#### Teste de Erro Léxico
- **Entrada:** `casos-de-teste/entradas/teste_erro_lexico.ca`
- **Descrição:** Caractere inválido `@` em identificador
- **Resultado:** Erro léxico detectado na linha 5

#### Teste de Erro Sintático
- **Entrada:** `casos-de-teste/entradas/teste_erro_sintatico.ca`
- **Descrição:** Chaves não fechadas e vírgulas ausentes
- **Resultado:** Erro sintático detectado

#### Teste de Erro Semântico
- **Entrada:** `casos-de-teste/entradas/teste_erro_semantico.ca`
- **Descrição:** Cores não declaradas e declaração duplicada
- **Resultado:** 3 erros semânticos detectados

#### Teste de Variável Duplicada
- **Entrada:** `casos-de-teste/entradas/teste_erro_variavel.ca`
- **Descrição:** Variável declarada duas vezes
- **Resultado:** 1 erro semântico detectado

#### Teste Complexo de Erros
- **Entrada:** `casos-de-teste/entradas/teste_erro_complexo.ca`
- **Descrição:** Múltiplos tipos de erros semânticos
- **Resultado:** 7 erros semânticos detectados

## Limitações Atuais

- Canvas fixo de 800x600 pixels
- Apenas formas geométricas básicas
- Sem suporte a animações
- Sem operações matemáticas complexas

## Extensões Futuras

- Suporte a gradientes
- Transformações (rotação, escala)
- Texto e fontes
- Animações SVG
- Canvas configurável
- Mais formas geométricas

## Exemplo de Saída SVG

A partir do código ColorArt:
```
cor { id=vermelho, valor="#FF0000" }
circulo { centro=[100, 100], raio=50, cor=[vermelho] }
```

Gera o SVG:
```svg
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<circle cx="100" cy="100" r="50" fill="#FF0000" stroke="black" stroke-width="2"/>
</svg>
```

## Como Contribuir

1. Adicione novos casos de teste em `casos-de-teste/entradas/`
2. Execute `python3 testador.py` para verificar se tudo funciona
3. Documente novas funcionalidades neste README

## Vídeo de Demonstração
**Assista à demonstração completa do ColorArt:**  
[Clique aqui para ver o vídeo no Google Drive](https://drive.google.com/file/d/1uCNakDi5qzgBcRFUS2lhZfBMEabRobXL/view?usp=sharing)  

*(Mostra todos os recursos da linguagem, exemplos de uso e execução dos testes)*


## Licença

Este projeto foi desenvolvido como trabalho acadêmico para a disciplina de Compiladores.
