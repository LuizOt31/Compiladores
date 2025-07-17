from ColorArtParser import ColorArtParser
from ColorArtVisitor import ColorArtVisitor
from ColorArtSemanticoUtils import ColorArtSemanticoUtils
from TabelaDeSimbolos import TabelaDeSimbolos

class ColorArtSemantico(ColorArtVisitor):
    def __init__(self):
        self.tabelaDeSimbolos = TabelaDeSimbolos()
    
    def visitPrograma(self, ctx: ColorArtParser.ProgramaContext):
        # Visitar todas as declarações primeiro
        for declaration in ctx.declaration():
            self.visitDeclaration(declaration)
        
        # Depois visitar todas as formas
        for shape in ctx.shape():
            self.visitShape(shape)
    
    def visitDeclaration(self, ctx: ColorArtParser.DeclarationContext):
        color = ctx.color()
        variable = ctx.variable()
        
        if color is not None:
            self.visitColor(color)
        elif variable is not None:
            self.visitVariable(variable)
    
    def visitColor(self, ctx: ColorArtParser.ColorContext):
        nome = ctx.ID().getText()
        
        if self.tabelaDeSimbolos.existe(nome):
            ColorArtSemanticoUtils.adicionarErroSemantico(ctx.start, f"Cor '{nome}' já declarada")
        else:
            valor = ctx.CADEIA().getText().strip('"')
            self.tabelaDeSimbolos.adicionarTabelaSimbolos(nome, TabelaDeSimbolos.TipoColorArt.COR, valor)
    
    def visitVariable(self, ctx: ColorArtParser.VariableContext):
        nome = ctx.ID().getText()
        
        if self.tabelaDeSimbolos.existe(nome):
            ColorArtSemanticoUtils.adicionarErroSemantico(ctx.start, f"Variável '{nome}' já declarada")
        else:
            tipo_text = ctx.tipo().getText()
            if tipo_text == "inteiro":
                tipo = TabelaDeSimbolos.TipoColorArt.INTEIRO
                valor = int(ctx.value().getText()) if ctx.value().INT() else ctx.value().ID().getText()
            else:  # cor
                tipo = TabelaDeSimbolos.TipoColorArt.COR
                valor = ctx.value().ID().getText() if ctx.value().ID() else ctx.value().INT().getText()
            
            self.tabelaDeSimbolos.adicionarTabelaSimbolos(nome, tipo, valor)
    
    def visitShape(self, ctx: ColorArtParser.ShapeContext):
        circle = ctx.circle()
        rectangle = ctx.rectangle()
        line = ctx.line()
        polygon = ctx.polygon()
        
        if circle is not None:
            self.visitCircle(circle)
        elif rectangle is not None:
            self.visitRectangle(rectangle)
        elif line is not None:
            self.visitLine(line)
        elif polygon is not None:
            self.visitPolygon(polygon)
    
    def _verificarCor(self, ctx, corId):
        """Método auxiliar para verificar se uma cor foi declarada"""
        if corId and not self.tabelaDeSimbolos.existe(corId):
            ColorArtSemanticoUtils.adicionarErroSemantico(ctx.start, f"Cor '{corId}' não declarada")
    
    def visitCircle(self, ctx: ColorArtParser.CircleContext):
        # Verificar se a cor foi declarada (se especificada)
        ids = ctx.ID()
        if ids:
            if isinstance(ids, list):
                for id_token in ids:
                    self._verificarCor(ctx, id_token.getText())
            else:
                self._verificarCor(ctx, ids.getText())
    
    def visitRectangle(self, ctx: ColorArtParser.RectangleContext):
        # Verificar se a cor foi declarada (se especificada)
        ids = ctx.ID()
        if ids:
            if isinstance(ids, list):
                for id_token in ids:
                    self._verificarCor(ctx, id_token.getText())
            else:
                self._verificarCor(ctx, ids.getText())
    
    def visitLine(self, ctx: ColorArtParser.LineContext):
        # Verificar se a cor foi declarada (se especificada)
        ids = ctx.ID()
        if ids:
            if isinstance(ids, list):
                for id_token in ids:
                    self._verificarCor(ctx, id_token.getText())
            else:
                self._verificarCor(ctx, ids.getText())
    
    def visitPolygon(self, ctx: ColorArtParser.PolygonContext):
        # Verificar se a cor foi declarada (se especificada)
        ids = ctx.ID()
        if ids:
            if isinstance(ids, list):
                for id_token in ids:
                    self._verificarCor(ctx, id_token.getText())
            else:
                self._verificarCor(ctx, ids.getText()) 