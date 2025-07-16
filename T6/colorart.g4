// colorart.g4 

grammar colorart;

program         : canvasDecl (colorDecl | shapeDecl)* EOF ;

// As regras do parser agora usam os nomes dos tokens em maiúsculo
canvasDecl      : CANVAS INT X INT ';' ;
colorDecl       : COLOR VAR '=' HEXCOLOR ';' ;

shapeDecl       : circleDecl
                | rectangleDecl
                | lineDecl
                | squareDecl
                ;

circleDecl      : CIRCLE INT INT RADIUS INT FILL VAR ';' ;
rectangleDecl   : RECTANGLE INT INT WIDTH INT HEIGHT INT FILL VAR ';' ;
squareDecl      : SQUARE INT INT SIZE INT FILL VAR ';' ;
lineDecl        : LINE INT INT TO INT INT STROKE VAR ';' ;


// --- LEXER (Tokens) ---

CANVAS          : 'canvas';
COLOR           : 'color';
CIRCLE          : 'circle';
RECTANGLE       : 'rectangle';
SQUARE          : 'square';
LINE            : 'line';
RADIUS          : 'radius';
WIDTH           : 'width';
HEIGHT          : 'height';
SIZE            : 'size';
FILL            : 'fill';
TO              : 'to';
STROKE          : 'stroke';
X               : 'x';

VAR             : [a-zA-Z_][a-zA-Z_0-9]* ; // VAR agora só pega o que não for palavra-chave
HEXCOLOR        : '#' [0-9a-fA-F]{6} ;
INT             : [0-9]+ ;
WS              : [ \t\r\n]+ -> skip ;
COMMENT         : '%' ~[\r\n]* -> skip ;