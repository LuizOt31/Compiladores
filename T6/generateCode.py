# CodeGenerator.py
from colorartListener import colorartListener
from colorartParser import colorartParser

class CodeGenerator(colorartListener):
    def __init__(self, output_filename):
        self.output_filename = output_filename
        self.code = []
        self.colors = {} # Tabela de símbolos para armazenar as cores declaradas

    # Chamado ao entrar na regra principal do programa
    def enterProgram(self, ctx:colorartParser.ProgramContext):
        self.code.append("import svgwrite")
        self.code.append(f"dwg = svgwrite.Drawing('{self.output_filename}', profile='tiny')")

    # Chamado ao sair da regra principal
    def exitProgram(self, ctx:colorartParser.ProgramContext):
        self.code.append("dwg.save()")

    # Processa a declaração do canvas
    def exitCanvasDecl(self, ctx:colorartParser.CanvasDeclContext):
        width = ctx.INT(0).getText()
        height = ctx.INT(1).getText()
        # Modifica a linha de inicialização do drawing com o tamanho correto
        self.code[1] = f"dwg = svgwrite.Drawing('{self.output_filename}', size=('{width}px', '{height}px'), profile='tiny')"

    # Armazena uma cor declarada
    def exitColorDecl(self, ctx:colorartParser.ColorDeclContext):
        name = ctx.VAR().getText()
        r = ctx.rgbColor().INT(0).getText()
        g = ctx.rgbColor().INT(1).getText()
        b = ctx.rgbColor().INT(2).getText()
        self.colors[name] = f"'rgb({r},{g},{b})'"

    # Gera o código para um círculo
    def exitCircleDecl(self, ctx:colorartParser.CircleDeclContext):
        cx = ctx.INT(0).getText()
        cy = ctx.INT(1).getText()
        r = ctx.INT(2).getText()
        color_var = ctx.VAR().getText()
        fill_color = self.colors.get(color_var, "'black'") # Usa preto se a cor não for encontrada
        self.code.append(f"dwg.add(dwg.circle(center=({cx}, {cy}), r={r}, fill={fill_color}))")

    # Gera o código para um retângulo
    def exitRectangleDecl(self, ctx:colorartParser.RectangleDeclContext):
        x = ctx.INT(0).getText()
        y = ctx.INT(1).getText()
        width = ctx.INT(2).getText()
        height = ctx.INT(3).getText()
        color_var = ctx.VAR().getText()
        fill_color = self.colors.get(color_var, "'black'")
        self.code.append(f"dwg.add(dwg.rect(insert=({x}, {y}), size=('{width}px', '{height}px'), fill={fill_color}))")
    
    # Gera o código para um quadrado
    def exitSquareDecl(self, ctx:colorartParser.SquareDeclContext):
        x = ctx.INT(0).getText()
        y = ctx.INT(1).getText()
        width = ctx.INT(2).getText()
        color_var = ctx.VAR().getText()
        fill_color = self.colors.get(color_var, "'black'")
        self.code.append(f"dwg.add(dwg.rect(insert=({x}, {y}), size=('{width}px', '{width}px'), fill={fill_color}))")

    # Gera o código para uma linha
    def exitLineDecl(self, ctx:colorartParser.LineDeclContext):
        x1 = ctx.INT(0).getText()
        y1 = ctx.INT(1).getText()
        x2 = ctx.INT(2).getText()
        y2 = ctx.INT(3).getText()
        color_var = ctx.VAR().getText()
        stroke_color = self.colors.get(color_var, "'black'")
        self.code.append(f"dwg.add(dwg.line(start=({x1}, {y1}), end=({x2}, {y2}), stroke={stroke_color}))")

    # Retorna o código final gerado
    def get_generated_code(self):
        return "\n".join(self.code)