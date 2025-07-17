grammar colorart;

program         : canvasDecl (colorDecl | shapeDecl)* EOF ;

canvasDecl      : CANVAS INT '-' INT ';' ;
colorDecl       : COLOR VAR '=' rgbColor ';' ;
shapeDecl       : circleDecl | rectangleDecl | lineDecl | squareDecl ;

circleDecl      : CIRCLE INT INT RADIUS INT FILL VAR ';' ;
rectangleDecl   : RECTANGLE INT INT WIDTH INT HEIGHT INT FILL VAR ';' ;
squareDecl      : SQUARE INT INT WIDTH INT FILL VAR ';' ;
lineDecl        : LINE INT INT TO INT INT STROKE VAR ';' ;

rgbColor        : INT ',' INT ',' INT ;

// Tokens
CANVAS  : 'canvas' ;
COLOR   : 'color' ;
CIRCLE  : 'circle' ;
RECTANGLE : 'rectangle' ;
SQUARE  : 'square' ;
LINE    : 'line' ;
RADIUS  : 'radius' ;
WIDTH   : 'width' ;
HEIGHT  : 'height' ;
FILL    : 'fill' ;
STROKE  : 'stroke' ;
TO      : 'to' ;

VAR             : ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;
INT             : ('0'..'9')+ ;
WS              : ( ' ' | '\t' | '\r' | '\n' ) -> skip ;
COMMENT         : '%' ~[\r\n]* -> skip ;
