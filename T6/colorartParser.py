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
        4,1,20,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,42,8,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,78,
        0,16,1,0,0,0,2,26,1,0,0,0,4,32,1,0,0,0,6,41,1,0,0,0,8,43,1,0,0,0,
        10,52,1,0,0,0,12,63,1,0,0,0,14,72,1,0,0,0,16,21,3,2,1,0,17,20,3,
        4,2,0,18,20,3,6,3,0,19,17,1,0,0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,
        19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,
        1,25,1,1,0,0,0,26,27,5,1,0,0,27,28,5,18,0,0,28,29,5,2,0,0,29,30,
        5,18,0,0,30,31,5,3,0,0,31,3,1,0,0,0,32,33,5,4,0,0,33,34,5,16,0,0,
        34,35,5,5,0,0,35,36,5,17,0,0,36,37,5,3,0,0,37,5,1,0,0,0,38,42,3,
        8,4,0,39,42,3,10,5,0,40,42,3,14,7,0,41,38,1,0,0,0,41,39,1,0,0,0,
        41,40,1,0,0,0,42,7,1,0,0,0,43,44,5,6,0,0,44,45,5,18,0,0,45,46,5,
        18,0,0,46,47,5,7,0,0,47,48,5,18,0,0,48,49,5,8,0,0,49,50,5,16,0,0,
        50,51,5,3,0,0,51,9,1,0,0,0,52,53,5,9,0,0,53,54,5,18,0,0,54,55,5,
        18,0,0,55,56,5,10,0,0,56,57,5,18,0,0,57,58,5,11,0,0,58,59,5,18,0,
        0,59,60,5,8,0,0,60,61,5,16,0,0,61,62,5,3,0,0,62,11,1,0,0,0,63,64,
        5,12,0,0,64,65,5,18,0,0,65,66,5,18,0,0,66,67,5,10,0,0,67,68,5,18,
        0,0,68,69,5,8,0,0,69,70,5,16,0,0,70,71,5,3,0,0,71,13,1,0,0,0,72,
        73,5,13,0,0,73,74,5,18,0,0,74,75,5,18,0,0,75,76,5,14,0,0,76,77,5,
        18,0,0,77,78,5,18,0,0,78,79,5,15,0,0,79,80,5,16,0,0,80,81,5,3,0,
        0,81,15,1,0,0,0,3,19,21,41
    ]

class colorartParser ( Parser ):

    grammarFileName = "colorart.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'canvas'", "'x'", "';'", "'color'", "'='", 
                     "'circle'", "'radius'", "'fill'", "'rectangle'", "'width'", 
                     "'height'", "'square'", "'line'", "'to'", "'stroke'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VAR", "HEXCOLOR", "INT", "WS", "COMMENT" ]

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
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    VAR=16
    HEXCOLOR=17
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
            self.state = 16
            self.canvasDecl()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8784) != 0):
                self.state = 19
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 17
                    self.colorDecl()
                    pass
                elif token in [6, 9, 13]:
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
            self.state = 26
            self.match(colorartParser.T__0)
            self.state = 27
            self.match(colorartParser.INT)
            self.state = 28
            self.match(colorartParser.T__1)
            self.state = 29
            self.match(colorartParser.INT)
            self.state = 30
            self.match(colorartParser.T__2)
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




    def colorDecl(self):

        localctx = colorartParser.ColorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_colorDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(colorartParser.T__3)
            self.state = 33
            self.match(colorartParser.VAR)
            self.state = 34
            self.match(colorartParser.T__4)
            self.state = 35
            self.match(colorartParser.HEXCOLOR)
            self.state = 36
            self.match(colorartParser.T__2)
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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.circleDecl()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.rectangleDecl()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.lineDecl()
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

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

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
            self.state = 43
            self.match(colorartParser.T__5)
            self.state = 44
            self.match(colorartParser.INT)
            self.state = 45
            self.match(colorartParser.INT)
            self.state = 46
            self.match(colorartParser.T__6)
            self.state = 47
            self.match(colorartParser.INT)
            self.state = 48
            self.match(colorartParser.T__7)
            self.state = 49
            self.match(colorartParser.VAR)
            self.state = 50
            self.match(colorartParser.T__2)
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

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

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
            self.state = 52
            self.match(colorartParser.T__8)
            self.state = 53
            self.match(colorartParser.INT)
            self.state = 54
            self.match(colorartParser.INT)
            self.state = 55
            self.match(colorartParser.T__9)
            self.state = 56
            self.match(colorartParser.INT)
            self.state = 57
            self.match(colorartParser.T__10)
            self.state = 58
            self.match(colorartParser.INT)
            self.state = 59
            self.match(colorartParser.T__7)
            self.state = 60
            self.match(colorartParser.VAR)
            self.state = 61
            self.match(colorartParser.T__2)
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

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

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
            self.state = 63
            self.match(colorartParser.T__11)
            self.state = 64
            self.match(colorartParser.INT)
            self.state = 65
            self.match(colorartParser.INT)
            self.state = 66
            self.match(colorartParser.T__9)
            self.state = 67
            self.match(colorartParser.INT)
            self.state = 68
            self.match(colorartParser.T__7)
            self.state = 69
            self.match(colorartParser.VAR)
            self.state = 70
            self.match(colorartParser.T__2)
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

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(colorartParser.INT)
            else:
                return self.getToken(colorartParser.INT, i)

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
            self.state = 72
            self.match(colorartParser.T__12)
            self.state = 73
            self.match(colorartParser.INT)
            self.state = 74
            self.match(colorartParser.INT)
            self.state = 75
            self.match(colorartParser.T__13)
            self.state = 76
            self.match(colorartParser.INT)
            self.state = 77
            self.match(colorartParser.INT)
            self.state = 78
            self.match(colorartParser.T__14)
            self.state = 79
            self.match(colorartParser.VAR)
            self.state = 80
            self.match(colorartParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





