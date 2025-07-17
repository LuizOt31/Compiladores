grammar ColorArt;

programa: (declaration | shape)+ EOF;

declaration: color | variable;
shape: circle | rectangle | line | polygon;

color: 'cor' '{' 'id' '=' ID ',' 'valor' '=' CADEIA '}';
variable: 'variavel' '{' 'id' '=' ID ',' 'tipo' '=' tipo ',' 'valor' '=' value '}';

circle: 'circulo' '{' 'centro' '=' '[' INT ',' INT ']' ',' 'raio' '=' INT (',' 'cor' '=' '[' ID ']')? (',' 'borda' '=' '[' ID ']')? '}';
rectangle: 'retangulo' '{' 'posicao' '=' '[' INT ',' INT ']' ',' 'largura' '=' INT ',' 'altura' '=' INT (',' 'cor' '=' '[' ID ']')? (',' 'borda' '=' '[' ID ']')? '}';
line: 'linha' '{' 'inicio' '=' '[' INT ',' INT ']' ',' 'fim' '=' '[' INT ',' INT ']' (',' 'cor' '=' '[' ID ']')? (',' 'espessura' '=' INT)? '}';
polygon: 'poligono' '{' 'pontos' '=' '[' points ']' (',' 'cor' '=' '[' ID ']')? (',' 'borda' '=' '[' ID ']')? '}';

points: point (',' point)*;
point: INT ',' INT;
tipo: 'inteiro' | 'cor';
value: INT | ID;

CADEIA: '"' (~('"'|'\\'|'\n'|'\r') )* '"';
ID: ([a-zA-Z])([a-zA-Z]|'0'..'9'|'_')*;
INT: ('0'..'9')+;

WS: [ \t\r\n] -> skip;
COMMENT: '//' ~[\r\n]* -> skip; 