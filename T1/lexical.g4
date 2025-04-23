lexer grammar lexical;

// Palavras-chave
ALGORITMO       : 'algoritmo'; 
FIM_ALGORITMO   : 'fim_algoritmo'; 
DECLARE         : 'declare'; 
LEIA            : 'leia'; 
ESCREVA         : 'escreva'; 
CONSTANTE       : 'constante'; 
VAR             : 'var'; 
TIPO            : 'tipo'; 
SE              : 'se'; 
ENTAO           : 'entao'; 
SENAO           : 'senao'; 
FIM_SE          : 'fim_se'; 
CASO            : 'caso'; 
SEJA            : 'seja'; 
FIM_CASO        : 'fim_caso'; 
PARA            : 'para'; 
ATE             : 'ate'; 
FIM_PARA        : 'fim_para'; 
ENQUANTO        : 'enquanto'; 
FACA            : 'faca'; 
FIM_ENQUANTO    : 'fim_enquanto'; 
REGISTRO        : 'registro'; 
FIM_REGISTRO    : 'fim_registro'; 
PROCEDIMENTO    : 'procedimento'; 
FIM_PROCEDIMENTO: 'fim_procedimento'; 
FUNCAO          : 'funcao'; 
FIM_FUNCAO      : 'fim_funcao'; 
RETORNE         : 'retorne';

// Tipos de variáveis
LITERAL         : 'literal'; 
INT             : 'inteiro'; 
REAL            : 'real'; 
LOGICO          : 'logico'; 
V               : 'verdadeiro'; 
F               : 'falso';

// Operadores
ATRIBUICAO      : '<-';
PONTOS          : '..';
OP_LOGICO       : 'e' | 'ou' | 'nao'; 
OP_REL          : '>=' | '<=' | '<>' | '>' | '<' | '='; 
OP_ART          : '+' | '-' | '*' | '/' | '%';

// Símbolos
TWO_POINTS      : ':'; 
ABRE_PARENTESES : '('; 
FECHA_PARENTESES: ')'; 
ABRE_VETOR      : '['; 
FECHA_VETOR     : ']'; 
VIRG            : ','; 
PONTEIRO        : '^'; 
ENDERECO        : '&'; 
PONTO           : '.';

// Identificadores e números
IDENT           : ('a'..'z' | 'A'..'Z') ('a'..'z' | 'A'..'Z' | '0'..'9' | '_')*;

fragment DIGITO : '0'..'9';
NUM_REAL : DIGITO+ '.' DIGITO+;    // sem sinal
NUM_INT  : DIGITO+;                // sem sinal

// Cadeia
CADEIA          : '"' (~["\r\n])*? '"' ;

// Comentário (fechado corretamente)
COMENTARIO      : '{' .*? '}' -> skip ;

// Espaços e quebras de linha
WS              : [ \t\r\n]+ -> skip ;
