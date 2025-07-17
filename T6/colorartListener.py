# Generated from colorart.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .colorartParser import colorartParser
else:
    from colorartParser import colorartParser

# This class defines a complete listener for a parse tree produced by colorartParser.
class colorartListener(ParseTreeListener):

    # Enter a parse tree produced by colorartParser#program.
    def enterProgram(self, ctx:colorartParser.ProgramContext):
        pass

    # Exit a parse tree produced by colorartParser#program.
    def exitProgram(self, ctx:colorartParser.ProgramContext):
        pass


    # Enter a parse tree produced by colorartParser#canvasDecl.
    def enterCanvasDecl(self, ctx:colorartParser.CanvasDeclContext):
        pass

    # Exit a parse tree produced by colorartParser#canvasDecl.
    def exitCanvasDecl(self, ctx:colorartParser.CanvasDeclContext):
        pass


    # Enter a parse tree produced by colorartParser#colorDecl.
    def enterColorDecl(self, ctx:colorartParser.ColorDeclContext):
        pass

    # Exit a parse tree produced by colorartParser#colorDecl.
    def exitColorDecl(self, ctx:colorartParser.ColorDeclContext):
        pass


    # Enter a parse tree produced by colorartParser#shapeDecl.
    def enterShapeDecl(self, ctx:colorartParser.ShapeDeclContext):
        pass

    # Exit a parse tree produced by colorartParser#shapeDecl.
    def exitShapeDecl(self, ctx:colorartParser.ShapeDeclContext):
        pass


    # Enter a parse tree produced by colorartParser#circleDecl.
    def enterCircleDecl(self, ctx:colorartParser.CircleDeclContext):
        pass

    # Exit a parse tree produced by colorartParser#circleDecl.
    def exitCircleDecl(self, ctx:colorartParser.CircleDeclContext):
        pass


    # Enter a parse tree produced by colorartParser#rectangleDecl.
    def enterRectangleDecl(self, ctx:colorartParser.RectangleDeclContext):
        pass

    # Exit a parse tree produced by colorartParser#rectangleDecl.
    def exitRectangleDecl(self, ctx:colorartParser.RectangleDeclContext):
        pass


    # Enter a parse tree produced by colorartParser#squareDecl.
    def enterSquareDecl(self, ctx:colorartParser.SquareDeclContext):
        pass

    # Exit a parse tree produced by colorartParser#squareDecl.
    def exitSquareDecl(self, ctx:colorartParser.SquareDeclContext):
        pass


    # Enter a parse tree produced by colorartParser#lineDecl.
    def enterLineDecl(self, ctx:colorartParser.LineDeclContext):
        pass

    # Exit a parse tree produced by colorartParser#lineDecl.
    def exitLineDecl(self, ctx:colorartParser.LineDeclContext):
        pass


    # Enter a parse tree produced by colorartParser#rgbColor.
    def enterRgbColor(self, ctx:colorartParser.RgbColorContext):
        pass

    # Exit a parse tree produced by colorartParser#rgbColor.
    def exitRgbColor(self, ctx:colorartParser.RgbColorContext):
        pass



del colorartParser