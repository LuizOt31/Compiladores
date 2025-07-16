# semantico.py

from antlr4.error.ErrorListener import ErrorListener
from colorartListener import colorartListener
from colorartParser import colorartParser
from scope import Scope, Symbol

class SemanticError(Exception):
    """Classe para erros semânticos personalizados."""
    def __init__(self, message, line, column):
        super().__init__(f"Erro Semântico na linha {line}:{column}: {message}")

class AnalisadorSemantico(colorartListener):
    def __init__(self):
        self.scope = Scope()
        self.canvas_dimensions = None

    # ANÁLISE DO CANVAS
    def enterCanvasDecl(self, ctx:colorartParser.CanvasDeclContext):
        width = int(ctx.INT(0).getText())
        height = int(ctx.INT(1).getText())
        self.canvas_dimensions = (width, height)
        print("Análise Semântica: Dimensões do canvas definidas para", self.canvas_dimensions)

    # ANÁLISE DE DECLARAÇÃO DE COR
    def enterColorDecl(self, ctx:colorartParser.ColorDeclContext):
        color_name = ctx.VAR().getText()
        color_value = ctx.HEX().getText()
        line = ctx.start.line
        column = ctx.start.column

        symbol = Symbol(name=color_name, type='cor', value=color_value)
        
        if not self.scope.add_symbol(symbol):
            raise SemanticError(f"A cor '{color_name}' já foi declarada.", line, column)
        
        print(f"Análise Semântica: OK - Cor '{color_name}' declarada com valor {color_value}.")

    # FUNÇÃO AUXILIAR PARA VERIFICAR CORES E LIMITES
    def _check_shape(self, ctx, shape_name, points):
        line = ctx.start.line
        column = ctx.start.column

        # 1. Verifica se o canvas foi declarado
        if not self.canvas_dimensions:
            raise SemanticError("Nenhum canvas foi declarado. Use 'canvas LxA;' no início.", line, column)

        # 2. Verifica se a cor foi declarada
        color_name = ctx.VAR().getText()
        if not self.scope.find_symbol(color_name):
            raise SemanticError(f"A cor '{color_name}' não foi declarada.", line, column)
        
        # 3. Verifica os limites do canvas
        canvas_width, canvas_height = self.canvas_dimensions
        for point_name, x, y in points:
            if not (0 <= x <= canvas_width and 0 <= y <= canvas_height):
                raise SemanticError(
                    f"O {shape_name} está (parcialmente ou totalmente) fora dos limites do canvas. "
                    f"Ponto problemático '{point_name}' em ({x}, {y}).",
                    line, column
                )
        
        print(f"Análise Semântica: OK - {shape_name} com cor '{color_name}'.")

    # ANÁLISE DAS FORMAS GEOMÉTRICAS
    def enterCircleDecl(self, ctx:colorartParser.CircleDeclContext):
        cx = int(ctx.INT(0).getText())
        cy = int(ctx.INT(1).getText())
        radius = int(ctx.INT(2).getText())

        points_to_check = [
            ('centro', cx, cy),
            ('topo', cx, cy - radius),
            ('base', cx, cy + radius),
            ('esquerda', cx - radius, cy),
            ('direita', cx + radius, cy)
        ]
        self._check_shape(ctx, 'círculo', points_to_check)

    def enterRectangleDecl(self, ctx:colorartParser.RectangleDeclContext):
        x1 = int(ctx.INT(0).getText())
        y1 = int(ctx.INT(1).getText())
        x2 = int(ctx.INT(2).getText())
        y2 = int(ctx.INT(3).getText())

        points_to_check = [
            ('ponto inicial', x1, y1),
            ('ponto final', x2, y2)
        ]
        self._check_shape(ctx, 'retângulo', points_to_check)

    def enterLineDecl(self, ctx:colorartParser.LineDeclContext):
        x1 = int(ctx.INT(0).getText())
        y1 = int(ctx.INT(1).getText())
        x2 = int(ctx.INT(2).getText())
        y2 = int(ctx.INT(3).getText())

        points_to_check = [
            ('ponto inicial', x1, y1),
            ('ponto final', x2, y2)
        ]
        self._check_shape(ctx, 'linha', points_to_check)

    def enterSquareDecl(self, ctx:colorartParser.SquareDeclContext):
        cx = int(ctx.INT(0).getText())
        cy = int(ctx.INT(1).getText())
        size = int(ctx.INT(2).getText())
        half_size = size / 2

        # Para o quadrado, verificamos os 4 cantos
        points_to_check = [
            ('canto superior esquerdo', cx - half_size, cy - half_size),
            ('canto superior direito', cx + half_size, cy - half_size),
            ('canto inferior esquerdo', cx - half_size, cy + half_size),
            ('canto inferior direito', cx + half_size, cy + half_size)
        ]
        self._check_shape(ctx, 'quadrado', points_to_check)