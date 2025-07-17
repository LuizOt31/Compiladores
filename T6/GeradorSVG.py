from ColorArtParser import ColorArtParser
from ColorArtVisitor import ColorArtVisitor
from TabelaDeSimbolos import TabelaDeSimbolos

class GeradorSVG(ColorArtVisitor):
    def __init__(self, width=800, height=600):
        self.tabela = TabelaDeSimbolos()
        self.svg_elements = []
        self.width = width
        self.height = height
    
    def visitPrograma(self, ctx: ColorArtParser.ProgramaContext):
        # Processar declarações primeiro
        for declaration in ctx.declaration():
            self.visitDeclaration(declaration)
        
        # Processar formas
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
        valor = ctx.CADEIA().getText().strip('"')
        self.tabela.adicionarTabelaSimbolos(nome, TabelaDeSimbolos.TipoColorArt.COR, valor)
    
    def visitVariable(self, ctx: ColorArtParser.VariableContext):
        nome = ctx.ID().getText()
        tipo_text = ctx.tipo().getText()
        
        if tipo_text == "inteiro":
            tipo = TabelaDeSimbolos.TipoColorArt.INTEIRO
            valor = int(ctx.value().getText()) if ctx.value().INT() else self._resolverValor(ctx.value().ID().getText())
        else:  # cor
            tipo = TabelaDeSimbolos.TipoColorArt.COR
            valor = self._resolverValor(ctx.value().ID().getText()) if ctx.value().ID() else ctx.value().INT().getText()
        
        self.tabela.adicionarTabelaSimbolos(nome, tipo, valor)
    
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
    
    def visitCircle(self, ctx: ColorArtParser.CircleContext):
        # Extrair coordenadas do centro
        coords = ctx.INT()
        cx = coords[0].getText()
        cy = coords[1].getText()
        raio = coords[2].getText()
        
        # Cor de preenchimento
        fill_color = "transparent"
        stroke_color = "black"
        
        ids = ctx.ID()
        if ids:
            if isinstance(ids, list):
                if len(ids) >= 1:  # cor de preenchimento
                    fill_color = self._resolverCor(ids[0].getText())
                if len(ids) >= 2:  # cor da borda
                    stroke_color = self._resolverCor(ids[1].getText())
            else:
                fill_color = self._resolverCor(ids.getText())
        
        svg_element = f'<circle cx="{cx}" cy="{cy}" r="{raio}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>'
        self.svg_elements.append(svg_element)
    
    def visitRectangle(self, ctx: ColorArtParser.RectangleContext):
        # Extrair coordenadas e dimensões
        coords = ctx.INT()
        x = coords[0].getText()
        y = coords[1].getText()
        width = coords[2].getText()
        height = coords[3].getText()
        
        # Cor de preenchimento
        fill_color = "transparent"
        stroke_color = "black"
        
        ids = ctx.ID()
        if ids:
            if isinstance(ids, list):
                if len(ids) >= 1:  # cor de preenchimento
                    fill_color = self._resolverCor(ids[0].getText())
                if len(ids) >= 2:  # cor da borda
                    stroke_color = self._resolverCor(ids[1].getText())
            else:
                fill_color = self._resolverCor(ids.getText())
        
        svg_element = f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>'
        self.svg_elements.append(svg_element)
    
    def visitLine(self, ctx: ColorArtParser.LineContext):
        # Extrair coordenadas
        coords = ctx.INT()
        x1 = coords[0].getText()
        y1 = coords[1].getText()
        x2 = coords[2].getText()
        y2 = coords[3].getText()
        
        # Cor da linha
        stroke_color = "black"
        stroke_width = "2"
        
        ids = ctx.ID()
        if ids:
            if isinstance(ids, list):
                if len(ids) >= 1:  # cor da linha
                    stroke_color = self._resolverCor(ids[0].getText())
            else:
                stroke_color = self._resolverCor(ids.getText())
        
        # Espessura (se especificada)
        if len(coords) >= 5:
            stroke_width = coords[4].getText()
        
        svg_element = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke_color}" stroke-width="{stroke_width}"/>'
        self.svg_elements.append(svg_element)
    
    def visitPolygon(self, ctx: ColorArtParser.PolygonContext):
        # Extrair pontos
        points = []
        points_ctx = ctx.points()
        
        for point_ctx in points_ctx.point():
            ints = point_ctx.INT()
            x = ints[0].getText()
            y = ints[1].getText()
            points.append(f"{x},{y}")
        
        points_str = " ".join(points)
        
        # Cor de preenchimento
        fill_color = "transparent"
        stroke_color = "black"
        
        ids = ctx.ID()
        if ids:
            if isinstance(ids, list):
                if len(ids) >= 1:  # cor de preenchimento
                    fill_color = self._resolverCor(ids[0].getText())
                if len(ids) >= 2:  # cor da borda
                    stroke_color = self._resolverCor(ids[1].getText())
            else:
                fill_color = self._resolverCor(ids.getText())
        
        svg_element = f'<polygon points="{points_str}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>'
        self.svg_elements.append(svg_element)
    
    def _resolverCor(self, nome):
        """Resolve uma cor pelo nome na tabela de símbolos"""
        if self.tabela.existe(nome):
            return self.tabela.getValor(nome)
        return "black"  # cor padrão
    
    def _resolverValor(self, nome):
        """Resolve um valor pelo nome na tabela de símbolos"""
        if self.tabela.existe(nome):
            return self.tabela.getValor(nome)
        return nome  # retorna o próprio nome se não encontrar
    
    def gerarSVG(self):
        """Gera o código SVG completo"""
        svg = [f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">']
        svg.extend(self.svg_elements)
        svg.append('</svg>')
        return svg 