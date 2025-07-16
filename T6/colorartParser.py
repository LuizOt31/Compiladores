# Generated from colorart.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,43,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,
        80,0,16,1,0,0,0,2,26,1,0,0,0,4,32,1,0,0,0,6,42,1,0,0,0,8,44,1,0,
        0,0,10,53,1,0,0,0,12,64,1,0,0,0,14,73,1,0,0,0,16,21,3,2,1,0,17,20,
        3,4,2,0,18,20,3,6,3,0,19,17,1,0,0,0,19,18,1,0,0,0,20,23,1,0,0,0,
        21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,
        0,0,1,25,1,1,0,0,0,26,27,5,3,0,0,27,28,5,19,0,0,28,29,5,16,0,0,29,
        30,5,19,0,0,30,31,5,1,0,0,31,3,1,0,0,0,32,33,5,4,0,0,33,34,5,17,
        0,0,34,35,5,2,0,0,35,36,5,18,0,0,36,37,5,1,0,0,37,5,1,0,0,0,38,43,
        3,8,4,0,39,43,3,10,5,0,40,43,3,14,7,0,41,43,3,12,6,0,42,38,1,0,0,
        0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,7,1,0,0,0,44,45,5,
        5,0,0,45,46,5,19,0,0,46,47,5,19,0,0,47,48,5,9,0,0,48,49,5,19,0,0,
        49,50,5,13,0,0,50,51,5,17,0,0,51,52,5,1,0,0,52,9,1,0,0,0,53,54,5,
        6,0,0,54,55,5,19,0,0,55,56,5,19,0,0,56,57,5,10,0,0,57,58,5,19,0,
        0,58,59,5,11,0,0,59,60,5,19,0,0,60,61,5,13,0,0,61,62,5,17,0,0,62,
        63,5,1,0,0,63,11,1,0,0,0,64,65,5,7,0,0,65,66,5,19,0,0,66,67,5,19,
        0,0,67,68,5,12,0,0,68,69,5,19,0,0,69,70,5,13,0,0,70,71,5,17,0,0,
        71,72,5,1,0,0,72,13,1,0,0,0,73,74,5,8,0,0,74,75,5,19,0,0,75,76,5,
        19,0,0,76,77,5,14,0,0,77,78,5,19,0,0,78,79,5,19,0,0,79,80,5,15,0,
        0,80,81,5,17,0,0,81,82,5,1,0,0,82,15,1,0,0,0,3,19,21,42
    ]

class colorartParser ( Parser ):

    grammarFileName = "colorart.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'canvas'", "'color'", "'circle'", 
                     "'rectangle'", "'square'", "'line'", "'radius'", "'width'", 
                     "'height'", "'size'", "'fill'", "'to'", "'stroke'", 
                     "'x'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "CANVAS", "COLOR", 
                      "CIRCLE", "RECTANGLE", "SQUARE", "LINE", "RADIUS", 
                      "WIDTH", "HEIGHT", "SIZE", "FILL", "TO", "STROKE", 
                      "X", "VAR", "HEXCOLOR", "INT", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_canvasDecl = 1
    RULE_colorDecl = 2
    RULE_shapeDecl = 3
    RULE_circleDecl = 4
    RULE_rectangleDecl = 5
    RULE_squareDecl = 6
    RULE_lineDecl = 7

    ruleNames =  [ "program", "canvasDecl", "colorDecl", "shapeDecl", "circleDecl", 
                   "rectangleDecl", "squareDecl", "lineDecl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    CANVAS=3
    COLOR=4
    CIRCLE=5
    RECTANGLE=6
    SQUARE=7
    LINE=8
    RADIUS=9
    WIDTH=10
    HEIGHT=11
    SIZE=12
    FILL=13
    TO=14
    STROKE=15
    X=16
    VAR=17
    HEXCOLOR=18
    INT=19
    WS=20
    COMMENT=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def canvasDecl(self):
            return self.getTypedRuleContext(colorartParser.CanvasDeclContext,0)


        def EOF(self):
            return self.getToken(colorartParser.EOF, 0)

        def colorDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(colorartParser.ColorDeclContext)
            else:
                return self.getTypedRuleContext(colorartParser.ColorDeclContext,i)


        def shapeDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(colorartParser.ShapeDeclContext)
            else:
                return self.getTypedRuleContext(colorartParser.ShapeDeclContext,i)


        def getRuleIndex(self):
            return colorartParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = colorartParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.canvasDecl()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 496) != 0):
                self.state = 19
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 17
                    self.colorDecl()
                    pass
                elif token in [5, 6, 7, 8]:
                    self.state = 18
                    self.shapeDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(colorartParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CanvasDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CANVAS(self):
            return self.getToken(colorartParser.CANVAS, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

        def X(self):
            return self.getToken(colorartParser.X, 0)

        def getRuleIndex(self):
            return colorartParser.RULE_canvasDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCanvasDecl" ):
                listener.enterCanvasDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCanvasDecl" ):
                listener.exitCanvasDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCanvasDecl" ):
                return visitor.visitCanvasDecl(self)
            else:
                return visitor.visitChildren(self)




    def canvasDecl(self):

        localctx = colorartParser.CanvasDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_canvasDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(colorartParser.CANVAS)
            self.state = 27
            self.match(colorartParser.INT)
            self.state = 28
            self.match(colorartParser.X)
            self.state = 29
            self.match(colorartParser.INT)
            self.state = 30
            self.match(colorartParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR(self):
            return self.getToken(colorartParser.COLOR, 0)

        def VAR(self):
            return self.getToken(colorartParser.VAR, 0)

        def HEXCOLOR(self):
            return self.getToken(colorartParser.HEXCOLOR, 0)

        def getRuleIndex(self):
            return colorartParser.RULE_colorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColorDecl" ):
                listener.enterColorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColorDecl" ):
                listener.exitColorDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColorDecl" ):
                return visitor.visitColorDecl(self)
            else:
                return visitor.visitChildren(self)




    def colorDecl(self):

        localctx = colorartParser.ColorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_colorDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(colorartParser.COLOR)
            self.state = 33
            self.match(colorartParser.VAR)
            self.state = 34
            self.match(colorartParser.T__1)
            self.state = 35
            self.match(colorartParser.HEXCOLOR)
            self.state = 36
            self.match(colorartParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def circleDecl(self):
            return self.getTypedRuleContext(colorartParser.CircleDeclContext,0)


        def rectangleDecl(self):
            return self.getTypedRuleContext(colorartParser.RectangleDeclContext,0)


        def lineDecl(self):
            return self.getTypedRuleContext(colorartParser.LineDeclContext,0)


        def squareDecl(self):
            return self.getTypedRuleContext(colorartParser.SquareDeclContext,0)


        def getRuleIndex(self):
            return colorartParser.RULE_shapeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShapeDecl" ):
                listener.enterShapeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShapeDecl" ):
                listener.exitShapeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShapeDecl" ):
                return visitor.visitShapeDecl(self)
            else:
                return visitor.visitChildren(self)




    def shapeDecl(self):

        localctx = colorartParser.ShapeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_shapeDecl)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.circleDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.rectangleDecl()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.lineDecl()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.squareDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CircleDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CIRCLE(self):
            return self.getToken(colorartParser.CIRCLE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

        def RADIUS(self):
            return self.getToken(colorartParser.RADIUS, 0)

        def FILL(self):
            return self.getToken(colorartParser.FILL, 0)

        def VAR(self):
            return self.getToken(colorartParser.VAR, 0)

        def getRuleIndex(self):
            return colorartParser.RULE_circleDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCircleDecl" ):
                listener.enterCircleDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCircleDecl" ):
                listener.exitCircleDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCircleDecl" ):
                return visitor.visitCircleDecl(self)
            else:
                return visitor.visitChildren(self)




    def circleDecl(self):

        localctx = colorartParser.CircleDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_circleDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(colorartParser.CIRCLE)
            self.state = 45
            self.match(colorartParser.INT)
            self.state = 46
            self.match(colorartParser.INT)
            self.state = 47
            self.match(colorartParser.RADIUS)
            self.state = 48
            self.match(colorartParser.INT)
            self.state = 49
            self.match(colorartParser.FILL)
            self.state = 50
            self.match(colorartParser.VAR)
            self.state = 51
            self.match(colorartParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RectangleDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECTANGLE(self):
            return self.getToken(colorartParser.RECTANGLE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

        def WIDTH(self):
            return self.getToken(colorartParser.WIDTH, 0)

        def HEIGHT(self):
            return self.getToken(colorartParser.HEIGHT, 0)

        def FILL(self):
            return self.getToken(colorartParser.FILL, 0)

        def VAR(self):
            return self.getToken(colorartParser.VAR, 0)

        def getRuleIndex(self):
            return colorartParser.RULE_rectangleDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRectangleDecl" ):
                listener.enterRectangleDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRectangleDecl" ):
                listener.exitRectangleDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRectangleDecl" ):
                return visitor.visitRectangleDecl(self)
            else:
                return visitor.visitChildren(self)




    def rectangleDecl(self):

        localctx = colorartParser.RectangleDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rectangleDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(colorartParser.RECTANGLE)
            self.state = 54
            self.match(colorartParser.INT)
            self.state = 55
            self.match(colorartParser.INT)
            self.state = 56
            self.match(colorartParser.WIDTH)
            self.state = 57
            self.match(colorartParser.INT)
            self.state = 58
            self.match(colorartParser.HEIGHT)
            self.state = 59
            self.match(colorartParser.INT)
            self.state = 60
            self.match(colorartParser.FILL)
            self.state = 61
            self.match(colorartParser.VAR)
            self.state = 62
            self.match(colorartParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SquareDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUARE(self):
            return self.getToken(colorartParser.SQUARE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

        def SIZE(self):
            return self.getToken(colorartParser.SIZE, 0)

        def FILL(self):
            return self.getToken(colorartParser.FILL, 0)

        def VAR(self):
            return self.getToken(colorartParser.VAR, 0)

        def getRuleIndex(self):
            return colorartParser.RULE_squareDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSquareDecl" ):
                listener.enterSquareDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSquareDecl" ):
                listener.exitSquareDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSquareDecl" ):
                return visitor.visitSquareDecl(self)
            else:
                return visitor.visitChildren(self)




    def squareDecl(self):

        localctx = colorartParser.SquareDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_squareDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(colorartParser.SQUARE)
            self.state = 65
            self.match(colorartParser.INT)
            self.state = 66
            self.match(colorartParser.INT)
            self.state = 67
            self.match(colorartParser.SIZE)
            self.state = 68
            self.match(colorartParser.INT)
            self.state = 69
            self.match(colorartParser.FILL)
            self.state = 70
            self.match(colorartParser.VAR)
            self.state = 71
            self.match(colorartParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE(self):
            return self.getToken(colorartParser.LINE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

        def TO(self):
            return self.getToken(colorartParser.TO, 0)

        def STROKE(self):
            return self.getToken(colorartParser.STROKE, 0)

        def VAR(self):
            return self.getToken(colorartParser.VAR, 0)

        def getRuleIndex(self):
            return colorartParser.RULE_lineDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineDecl" ):
                listener.enterLineDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineDecl" ):
                listener.exitLineDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineDecl" ):
                return visitor.visitLineDecl(self)
            else:
                return visitor.visitChildren(self)




    def lineDecl(self):

        localctx = colorartParser.LineDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lineDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(colorartParser.LINE)
            self.state = 74
            self.match(colorartParser.INT)
            self.state = 75
            self.match(colorartParser.INT)
            self.state = 76
            self.match(colorartParser.TO)
            self.state = 77
            self.match(colorartParser.INT)
            self.state = 78
            self.match(colorartParser.INT)
            self.state = 79
            self.match(colorartParser.STROKE)
            self.state = 80
            self.match(colorartParser.VAR)
            self.state = 81
            self.match(colorartParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





