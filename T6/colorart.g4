grammar colorart;

program         : canvasDecl (colorDecl | shapeDecl)* EOF ;

canvasDecl      : 'canvas' INT 'x' INT ';' ;

colorDecl       : 'color' ID '=' HEXCOLOR ';' ;

shapeDecl       : circleDecl
                | rectangleDecl
                | lineDecl ;

circleDecl      : 'circle' INT INT 'radius' INT 'fill' ID ';' ;

rectangleDecl   : 'rectangle' INT INT 'width' INT 'height' INT 'fill' ID ';' ;

lineDecl        : 'line' INT INT 'to' INT INT 'stroke' ID ';' ;

// Tokens
ID              : [a-zA-Z_][a-zA-Z_0-9]* ;

HEXCOLOR        : '#' [0-9a-fA-F]{6} ;

INT             : [0-9]+ ;

WS              : [ \t\r\n]+ -> skip ;
