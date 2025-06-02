grammar colorart;

program         : canvasDecl (colorDecl | shapeDecl)* EOF ;

// Define o tamanho da tela do canva
canvasDecl      : 'canvas' INT 'x' INT ';' ;

// Definir cor
colorDecl       : 'color' ID '=' HEXCOLOR ';' ;

// Definir a forma geometrica
shapeDecl       : circleDecl
                | rectangleDecl
                | lineDecl ;

// Definir um circulo
circleDecl      : 'circle' INT INT 'radius' INT 'fill' ID ';' ;

// Definir um retangulo
rectangleDecl   : 'rectangle' INT INT 'width' INT 'height' INT 'fill' ID ';' ;

// Definir um linha
lineDecl        : 'line' INT INT 'to' INT INT 'stroke' ID ';' ;

// Tokens
ID              : [a-zA-Z_][a-zA-Z_0-9]* ;

// formato para definir uma cor
HEXCOLOR        : '#' [0-9a-fA-F]{6} ;

INT             : [0-9]+ ;

WS              : [ \t\r\n]+ -> skip ;
