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
        4,1,20,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,3,3,45,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,0,87,0,18,1,0,0,0,2,28,1,0,0,0,
        4,34,1,0,0,0,6,44,1,0,0,0,8,46,1,0,0,0,10,55,1,0,0,0,12,66,1,0,0,
        0,14,75,1,0,0,0,16,85,1,0,0,0,18,23,3,2,1,0,19,22,3,4,2,0,20,22,
        3,6,3,0,21,19,1,0,0,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,
        23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,
        0,0,28,29,5,5,0,0,29,30,5,18,0,0,30,31,5,1,0,0,31,32,5,18,0,0,32,
        33,5,2,0,0,33,3,1,0,0,0,34,35,5,6,0,0,35,36,5,17,0,0,36,37,5,3,0,
        0,37,38,3,16,8,0,38,39,5,2,0,0,39,5,1,0,0,0,40,45,3,8,4,0,41,45,
        3,10,5,0,42,45,3,14,7,0,43,45,3,12,6,0,44,40,1,0,0,0,44,41,1,0,0,
        0,44,42,1,0,0,0,44,43,1,0,0,0,45,7,1,0,0,0,46,47,5,7,0,0,47,48,5,
        18,0,0,48,49,5,18,0,0,49,50,5,11,0,0,50,51,5,18,0,0,51,52,5,14,0,
        0,52,53,5,17,0,0,53,54,5,2,0,0,54,9,1,0,0,0,55,56,5,8,0,0,56,57,
        5,18,0,0,57,58,5,18,0,0,58,59,5,12,0,0,59,60,5,18,0,0,60,61,5,13,
        0,0,61,62,5,18,0,0,62,63,5,14,0,0,63,64,5,17,0,0,64,65,5,2,0,0,65,
        11,1,0,0,0,66,67,5,9,0,0,67,68,5,18,0,0,68,69,5,18,0,0,69,70,5,12,
        0,0,70,71,5,18,0,0,71,72,5,14,0,0,72,73,5,17,0,0,73,74,5,2,0,0,74,
        13,1,0,0,0,75,76,5,10,0,0,76,77,5,18,0,0,77,78,5,18,0,0,78,79,5,
        16,0,0,79,80,5,18,0,0,80,81,5,18,0,0,81,82,5,15,0,0,82,83,5,17,0,
        0,83,84,5,2,0,0,84,15,1,0,0,0,85,86,5,18,0,0,86,87,5,4,0,0,87,88,
        5,18,0,0,88,89,5,4,0,0,89,90,5,18,0,0,90,17,1,0,0,0,3,21,23,44
    ]

class colorartParser ( Parser ):

    grammarFileName = "colorart.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "';'", "'='", "','", "'canvas'", 
                     "'color'", "'circle'", "'rectangle'", "'square'", "'line'", 
                     "'radius'", "'width'", "'height'", "'fill'", "'stroke'", 
                     "'to'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CANVAS", "COLOR", "CIRCLE", "RECTANGLE", 
                      "SQUARE", "LINE", "RADIUS", "WIDTH", "HEIGHT", "FILL", 
                      "STROKE", "TO", "VAR", "INT", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_canvasDecl = 1
    RULE_colorDecl = 2
    RULE_shapeDecl = 3
    RULE_circleDecl = 4
    RULE_rectangleDecl = 5
    RULE_squareDecl = 6
    RULE_lineDecl = 7
    RULE_rgbColor = 8

    ruleNames =  [ "program", "canvasDecl", "colorDecl", "shapeDecl", "circleDecl", 
                   "rectangleDecl", "squareDecl", "lineDecl", "rgbColor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    CANVAS=5
    COLOR=6
    CIRCLE=7
    RECTANGLE=8
    SQUARE=9
    LINE=10
    RADIUS=11
    WIDTH=12
    HEIGHT=13
    FILL=14
    STROKE=15
    TO=16
    VAR=17
    INT=18
    WS=19
    COMMENT=20

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




    def program(self):

        localctx = colorartParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.canvasDecl()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0):
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 19
                    self.colorDecl()
                    pass
                elif token in [7, 8, 9, 10]:
                    self.state = 20
                    self.shapeDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
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

        def getRuleIndex(self):
            return colorartParser.RULE_canvasDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCanvasDecl" ):
                listener.enterCanvasDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCanvasDecl" ):
                listener.exitCanvasDecl(self)




    def canvasDecl(self):

        localctx = colorartParser.CanvasDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_canvasDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(colorartParser.CANVAS)
            self.state = 29
            self.match(colorartParser.INT)
            self.state = 30
            self.match(colorartParser.T__0)
            self.state = 31
            self.match(colorartParser.INT)
            self.state = 32
            self.match(colorartParser.T__1)
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

        def rgbColor(self):
            return self.getTypedRuleContext(colorartParser.RgbColorContext,0)


        def getRuleIndex(self):
            return colorartParser.RULE_colorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColorDecl" ):
                listener.enterColorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColorDecl" ):
                listener.exitColorDecl(self)




    def colorDecl(self):

        localctx = colorartParser.ColorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_colorDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(colorartParser.COLOR)
            self.state = 35
            self.match(colorartParser.VAR)
            self.state = 36
            self.match(colorartParser.T__2)
            self.state = 37
            self.rgbColor()
            self.state = 38
            self.match(colorartParser.T__1)
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




    def shapeDecl(self):

        localctx = colorartParser.ShapeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_shapeDecl)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.circleDecl()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.rectangleDecl()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.lineDecl()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
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




    def circleDecl(self):

        localctx = colorartParser.CircleDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_circleDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(colorartParser.CIRCLE)
            self.state = 47
            self.match(colorartParser.INT)
            self.state = 48
            self.match(colorartParser.INT)
            self.state = 49
            self.match(colorartParser.RADIUS)
            self.state = 50
            self.match(colorartParser.INT)
            self.state = 51
            self.match(colorartParser.FILL)
            self.state = 52
            self.match(colorartParser.VAR)
            self.state = 53
            self.match(colorartParser.T__1)
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




    def rectangleDecl(self):

        localctx = colorartParser.RectangleDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rectangleDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(colorartParser.RECTANGLE)
            self.state = 56
            self.match(colorartParser.INT)
            self.state = 57
            self.match(colorartParser.INT)
            self.state = 58
            self.match(colorartParser.WIDTH)
            self.state = 59
            self.match(colorartParser.INT)
            self.state = 60
            self.match(colorartParser.HEIGHT)
            self.state = 61
            self.match(colorartParser.INT)
            self.state = 62
            self.match(colorartParser.FILL)
            self.state = 63
            self.match(colorartParser.VAR)
            self.state = 64
            self.match(colorartParser.T__1)
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

        def WIDTH(self):
            return self.getToken(colorartParser.WIDTH, 0)

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




    def squareDecl(self):

        localctx = colorartParser.SquareDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_squareDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(colorartParser.SQUARE)
            self.state = 67
            self.match(colorartParser.INT)
            self.state = 68
            self.match(colorartParser.INT)
            self.state = 69
            self.match(colorartParser.WIDTH)
            self.state = 70
            self.match(colorartParser.INT)
            self.state = 71
            self.match(colorartParser.FILL)
            self.state = 72
            self.match(colorartParser.VAR)
            self.state = 73
            self.match(colorartParser.T__1)
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




    def lineDecl(self):

        localctx = colorartParser.LineDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lineDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(colorartParser.LINE)
            self.state = 76
            self.match(colorartParser.INT)
            self.state = 77
            self.match(colorartParser.INT)
            self.state = 78
            self.match(colorartParser.TO)
            self.state = 79
            self.match(colorartParser.INT)
            self.state = 80
            self.match(colorartParser.INT)
            self.state = 81
            self.match(colorartParser.STROKE)
            self.state = 82
            self.match(colorartParser.VAR)
            self.state = 83
            self.match(colorartParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RgbColorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

        def getRuleIndex(self):
            return colorartParser.RULE_rgbColor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRgbColor" ):
                listener.enterRgbColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRgbColor" ):
                listener.exitRgbColor(self)




    def rgbColor(self):

        localctx = colorartParser.RgbColorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rgbColor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(colorartParser.INT)
            self.state = 86
            self.match(colorartParser.T__3)
            self.state = 87
            self.match(colorartParser.INT)
            self.state = 88
            self.match(colorartParser.T__3)
            self.state = 89
            self.match(colorartParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





