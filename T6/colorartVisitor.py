# Generated from colorart.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .colorartParser import colorartParser
else:
    from colorartParser import colorartParser

# This class defines a complete generic visitor for a parse tree produced by colorartParser.

class colorartVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by colorartParser#program.
    def visitProgram(self, ctx:colorartParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by colorartParser#canvasDecl.
    def visitCanvasDecl(self, ctx:colorartParser.CanvasDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by colorartParser#colorDecl.
    def visitColorDecl(self, ctx:colorartParser.ColorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by colorartParser#shapeDecl.
    def visitShapeDecl(self, ctx:colorartParser.ShapeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by colorartParser#circleDecl.
    def visitCircleDecl(self, ctx:colorartParser.CircleDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by colorartParser#rectangleDecl.
    def visitRectangleDecl(self, ctx:colorartParser.RectangleDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by colorartParser#squareDecl.
    def visitSquareDecl(self, ctx:colorartParser.SquareDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by colorartParser#lineDecl.
    def visitLineDecl(self, ctx:colorartParser.LineDeclContext):
        return self.visitChildren(ctx)



del colorartParser