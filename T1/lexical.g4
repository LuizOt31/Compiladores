lexer grammar lexical;

TEXTO : '"' (~[\r\n])*? '"';
//COMENTARIO_NAO_FECHADO : '{' ~('}' | '\n')* '\n';

WS : [ \t\r\n]+ -> skip;
COMENTARIO: '{' (~[\r\n])*? '}' -> skip;

// terminais literais
ALGORITMO : 'algoritmo';
FIM_ALGORITMO: 'fim_algoritmo';
DECLARE: 'declare';
LEIA: 'leia';
ESCREVA: 'escreva';
CONSTANTE: 'constante';
VAR: 'var';
TIPO: 'tipo';
SE: 'se';
ENTAO: 'entao';
SENAO: 'senao';
FIM_SE: 'fim_se';
CASO: 'caso';
SEJA: 'seja';
FIM_CASO: 'fim_caso';
PARA: 'para';
ATE: 'ate';
FIM_PARA: 'fim_para';
ENQUANTO: 'enquanto';
FACA: 'faca';
FIM_ENQUANTO: 'fim_enquanto';
REGISTRO: 'registro';
FIM_REGISTRO: 'fim_registro';
PROCEDIMENTO: 'procedimento';
FIM_PROCEDIMENTO: 'fim_procedimento';
FUNCAO: 'funcao';
FIM_FUNCAO: 'fim_funcao';
RETORNE: 'retorne';



// tipo variável
LITERAL: 'literal';
INT: 'inteiro';
REAL: 'real';
LOGICO: 'logico';
// booleano
V: 'verdadeiro';
F: 'falso';

// Operadores lógicos
OP_LOGICO: 'e' | 'ou' | 'nao';
OP_REL: '>' | '>=' | '<' | '<=' | '<>' | '=';
OP_ART: '+' | '-' | '*' | '/' | '%';

TWO_POINTS: ':';
ABRE_PARENTESES: '(';
FECHA_PARENTESES: ')';
ABRE_VETOR: '['; // vetor é chamado de dimensão em LA
FECHA_VETOR: ']';

IDENT: ('a'..'z' | 'A'..'Z')('a'..'z' | 'A'..'Z' | '0'..'9')*;

VIRG: ',';  

fragment
DIGITO: '0'..'9';

NUM_INT: ('+'|'-')? DIGITO+;
NUM_REAL: ('+'|'-')? DIGITO+ '.' DIGITO+;
