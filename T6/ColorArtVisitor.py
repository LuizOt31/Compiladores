# Generated from ColorArt.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ColorArtParser import ColorArtParser
else:
    from ColorArtParser import ColorArtParser

# This class defines a complete generic visitor for a parse tree produced by ColorArtParser.

class ColorArtVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ColorArtParser#programa.
    def visitPrograma(self, ctx:ColorArtParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#declaration.
    def visitDeclaration(self, ctx:ColorArtParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#shape.
    def visitShape(self, ctx:ColorArtParser.ShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#color.
    def visitColor(self, ctx:ColorArtParser.ColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#variable.
    def visitVariable(self, ctx:ColorArtParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#circle.
    def visitCircle(self, ctx:ColorArtParser.CircleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#rectangle.
    def visitRectangle(self, ctx:ColorArtParser.RectangleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#line.
    def visitLine(self, ctx:ColorArtParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#polygon.
    def visitPolygon(self, ctx:ColorArtParser.PolygonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#points.
    def visitPoints(self, ctx:ColorArtParser.PointsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#point.
    def visitPoint(self, ctx:ColorArtParser.PointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#tipo.
    def visitTipo(self, ctx:ColorArtParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColorArtParser#value.
    def visitValue(self, ctx:ColorArtParser.ValueContext):
        return self.visitChildren(ctx)



del ColorArtParser