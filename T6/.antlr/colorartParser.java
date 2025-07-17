// Generated from /home/lo/Documentos/Obsidian/UFSCar/7_semestre/Compiladores/Compiladores/T6/colorart.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class colorartParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, CANVAS=5, COLOR=6, CIRCLE=7, RECTANGLE=8, 
		SQUARE=9, LINE=10, RADIUS=11, WIDTH=12, HEIGHT=13, FILL=14, STROKE=15, 
		TO=16, VAR=17, INT=18, WS=19, COMMENT=20;
	public static final int
		RULE_program = 0, RULE_canvasDecl = 1, RULE_colorDecl = 2, RULE_shapeDecl = 3, 
		RULE_circleDecl = 4, RULE_rectangleDecl = 5, RULE_squareDecl = 6, RULE_lineDecl = 7, 
		RULE_rgbColor = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "canvasDecl", "colorDecl", "shapeDecl", "circleDecl", "rectangleDecl", 
			"squareDecl", "lineDecl", "rgbColor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'-'", "';'", "'='", "','", "'canvas'", "'color'", "'circle'", 
			"'rectangle'", "'square'", "'line'", "'radius'", "'width'", "'height'", 
			"'fill'", "'stroke'", "'to'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "CANVAS", "COLOR", "CIRCLE", "RECTANGLE", 
			"SQUARE", "LINE", "RADIUS", "WIDTH", "HEIGHT", "FILL", "STROKE", "TO", 
			"VAR", "INT", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "colorart.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public colorartParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public CanvasDeclContext canvasDecl() {
			return getRuleContext(CanvasDeclContext.class,0);
		}
		public TerminalNode EOF() { return getToken(colorartParser.EOF, 0); }
		public List<ColorDeclContext> colorDecl() {
			return getRuleContexts(ColorDeclContext.class);
		}
		public ColorDeclContext colorDecl(int i) {
			return getRuleContext(ColorDeclContext.class,i);
		}
		public List<ShapeDeclContext> shapeDecl() {
			return getRuleContexts(ShapeDeclContext.class);
		}
		public ShapeDeclContext shapeDecl(int i) {
			return getRuleContext(ShapeDeclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			canvasDecl();
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1984L) != 0)) {
				{
				setState(21);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case COLOR:
					{
					setState(19);
					colorDecl();
					}
					break;
				case CIRCLE:
				case RECTANGLE:
				case SQUARE:
				case LINE:
					{
					setState(20);
					shapeDecl();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(26);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CanvasDeclContext extends ParserRuleContext {
		public TerminalNode CANVAS() { return getToken(colorartParser.CANVAS, 0); }
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
		public CanvasDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_canvasDecl; }
	}

	public final CanvasDeclContext canvasDecl() throws RecognitionException {
		CanvasDeclContext _localctx = new CanvasDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_canvasDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(CANVAS);
			setState(29);
			match(INT);
			setState(30);
			match(T__0);
			setState(31);
			match(INT);
			setState(32);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ColorDeclContext extends ParserRuleContext {
		public TerminalNode COLOR() { return getToken(colorartParser.COLOR, 0); }
		public TerminalNode VAR() { return getToken(colorartParser.VAR, 0); }
		public RgbColorContext rgbColor() {
			return getRuleContext(RgbColorContext.class,0);
		}
		public ColorDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_colorDecl; }
	}

	public final ColorDeclContext colorDecl() throws RecognitionException {
		ColorDeclContext _localctx = new ColorDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_colorDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(COLOR);
			setState(35);
			match(VAR);
			setState(36);
			match(T__2);
			setState(37);
			rgbColor();
			setState(38);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShapeDeclContext extends ParserRuleContext {
		public CircleDeclContext circleDecl() {
			return getRuleContext(CircleDeclContext.class,0);
		}
		public RectangleDeclContext rectangleDecl() {
			return getRuleContext(RectangleDeclContext.class,0);
		}
		public LineDeclContext lineDecl() {
			return getRuleContext(LineDeclContext.class,0);
		}
		public SquareDeclContext squareDecl() {
			return getRuleContext(SquareDeclContext.class,0);
		}
		public ShapeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shapeDecl; }
	}

	public final ShapeDeclContext shapeDecl() throws RecognitionException {
		ShapeDeclContext _localctx = new ShapeDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_shapeDecl);
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CIRCLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				circleDecl();
				}
				break;
			case RECTANGLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				rectangleDecl();
				}
				break;
			case LINE:
				enterOuterAlt(_localctx, 3);
				{
				setState(42);
				lineDecl();
				}
				break;
			case SQUARE:
				enterOuterAlt(_localctx, 4);
				{
				setState(43);
				squareDecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CircleDeclContext extends ParserRuleContext {
		public TerminalNode CIRCLE() { return getToken(colorartParser.CIRCLE, 0); }
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
		public TerminalNode RADIUS() { return getToken(colorartParser.RADIUS, 0); }
		public TerminalNode FILL() { return getToken(colorartParser.FILL, 0); }
		public TerminalNode VAR() { return getToken(colorartParser.VAR, 0); }
		public CircleDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_circleDecl; }
	}

	public final CircleDeclContext circleDecl() throws RecognitionException {
		CircleDeclContext _localctx = new CircleDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_circleDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(CIRCLE);
			setState(47);
			match(INT);
			setState(48);
			match(INT);
			setState(49);
			match(RADIUS);
			setState(50);
			match(INT);
			setState(51);
			match(FILL);
			setState(52);
			match(VAR);
			setState(53);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RectangleDeclContext extends ParserRuleContext {
		public TerminalNode RECTANGLE() { return getToken(colorartParser.RECTANGLE, 0); }
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
		public TerminalNode WIDTH() { return getToken(colorartParser.WIDTH, 0); }
		public TerminalNode HEIGHT() { return getToken(colorartParser.HEIGHT, 0); }
		public TerminalNode FILL() { return getToken(colorartParser.FILL, 0); }
		public TerminalNode VAR() { return getToken(colorartParser.VAR, 0); }
		public RectangleDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rectangleDecl; }
	}

	public final RectangleDeclContext rectangleDecl() throws RecognitionException {
		RectangleDeclContext _localctx = new RectangleDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_rectangleDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(RECTANGLE);
			setState(56);
			match(INT);
			setState(57);
			match(INT);
			setState(58);
			match(WIDTH);
			setState(59);
			match(INT);
			setState(60);
			match(HEIGHT);
			setState(61);
			match(INT);
			setState(62);
			match(FILL);
			setState(63);
			match(VAR);
			setState(64);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SquareDeclContext extends ParserRuleContext {
		public TerminalNode SQUARE() { return getToken(colorartParser.SQUARE, 0); }
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
		public TerminalNode WIDTH() { return getToken(colorartParser.WIDTH, 0); }
		public TerminalNode FILL() { return getToken(colorartParser.FILL, 0); }
		public TerminalNode VAR() { return getToken(colorartParser.VAR, 0); }
		public SquareDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_squareDecl; }
	}

	public final SquareDeclContext squareDecl() throws RecognitionException {
		SquareDeclContext _localctx = new SquareDeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_squareDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(SQUARE);
			setState(67);
			match(INT);
			setState(68);
			match(INT);
			setState(69);
			match(WIDTH);
			setState(70);
			match(INT);
			setState(71);
			match(FILL);
			setState(72);
			match(VAR);
			setState(73);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineDeclContext extends ParserRuleContext {
		public TerminalNode LINE() { return getToken(colorartParser.LINE, 0); }
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
		public TerminalNode TO() { return getToken(colorartParser.TO, 0); }
		public TerminalNode STROKE() { return getToken(colorartParser.STROKE, 0); }
		public TerminalNode VAR() { return getToken(colorartParser.VAR, 0); }
		public LineDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineDecl; }
	}

	public final LineDeclContext lineDecl() throws RecognitionException {
		LineDeclContext _localctx = new LineDeclContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_lineDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(LINE);
			setState(76);
			match(INT);
			setState(77);
			match(INT);
			setState(78);
			match(TO);
			setState(79);
			match(INT);
			setState(80);
			match(INT);
			setState(81);
			match(STROKE);
			setState(82);
			match(VAR);
			setState(83);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RgbColorContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
		public RgbColorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rgbColor; }
	}

	public final RgbColorContext rgbColor() throws RecognitionException {
		RgbColorContext _localctx = new RgbColorContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_rgbColor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(INT);
			setState(86);
			match(T__3);
			setState(87);
			match(INT);
			setState(88);
			match(T__3);
			setState(89);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0014\\\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u0016\b\u0000"+
		"\n\u0000\f\u0000\u0019\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0003\u0003-\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0000\u0000\t\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0000\u0000"+
		"W\u0000\u0012\u0001\u0000\u0000\u0000\u0002\u001c\u0001\u0000\u0000\u0000"+
		"\u0004\"\u0001\u0000\u0000\u0000\u0006,\u0001\u0000\u0000\u0000\b.\u0001"+
		"\u0000\u0000\u0000\n7\u0001\u0000\u0000\u0000\fB\u0001\u0000\u0000\u0000"+
		"\u000eK\u0001\u0000\u0000\u0000\u0010U\u0001\u0000\u0000\u0000\u0012\u0017"+
		"\u0003\u0002\u0001\u0000\u0013\u0016\u0003\u0004\u0002\u0000\u0014\u0016"+
		"\u0003\u0006\u0003\u0000\u0015\u0013\u0001\u0000\u0000\u0000\u0015\u0014"+
		"\u0001\u0000\u0000\u0000\u0016\u0019\u0001\u0000\u0000\u0000\u0017\u0015"+
		"\u0001\u0000\u0000\u0000\u0017\u0018\u0001\u0000\u0000\u0000\u0018\u001a"+
		"\u0001\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u001a\u001b"+
		"\u0005\u0000\u0000\u0001\u001b\u0001\u0001\u0000\u0000\u0000\u001c\u001d"+
		"\u0005\u0005\u0000\u0000\u001d\u001e\u0005\u0012\u0000\u0000\u001e\u001f"+
		"\u0005\u0001\u0000\u0000\u001f \u0005\u0012\u0000\u0000 !\u0005\u0002"+
		"\u0000\u0000!\u0003\u0001\u0000\u0000\u0000\"#\u0005\u0006\u0000\u0000"+
		"#$\u0005\u0011\u0000\u0000$%\u0005\u0003\u0000\u0000%&\u0003\u0010\b\u0000"+
		"&\'\u0005\u0002\u0000\u0000\'\u0005\u0001\u0000\u0000\u0000(-\u0003\b"+
		"\u0004\u0000)-\u0003\n\u0005\u0000*-\u0003\u000e\u0007\u0000+-\u0003\f"+
		"\u0006\u0000,(\u0001\u0000\u0000\u0000,)\u0001\u0000\u0000\u0000,*\u0001"+
		"\u0000\u0000\u0000,+\u0001\u0000\u0000\u0000-\u0007\u0001\u0000\u0000"+
		"\u0000./\u0005\u0007\u0000\u0000/0\u0005\u0012\u0000\u000001\u0005\u0012"+
		"\u0000\u000012\u0005\u000b\u0000\u000023\u0005\u0012\u0000\u000034\u0005"+
		"\u000e\u0000\u000045\u0005\u0011\u0000\u000056\u0005\u0002\u0000\u0000"+
		"6\t\u0001\u0000\u0000\u000078\u0005\b\u0000\u000089\u0005\u0012\u0000"+
		"\u00009:\u0005\u0012\u0000\u0000:;\u0005\f\u0000\u0000;<\u0005\u0012\u0000"+
		"\u0000<=\u0005\r\u0000\u0000=>\u0005\u0012\u0000\u0000>?\u0005\u000e\u0000"+
		"\u0000?@\u0005\u0011\u0000\u0000@A\u0005\u0002\u0000\u0000A\u000b\u0001"+
		"\u0000\u0000\u0000BC\u0005\t\u0000\u0000CD\u0005\u0012\u0000\u0000DE\u0005"+
		"\u0012\u0000\u0000EF\u0005\f\u0000\u0000FG\u0005\u0012\u0000\u0000GH\u0005"+
		"\u000e\u0000\u0000HI\u0005\u0011\u0000\u0000IJ\u0005\u0002\u0000\u0000"+
		"J\r\u0001\u0000\u0000\u0000KL\u0005\n\u0000\u0000LM\u0005\u0012\u0000"+
		"\u0000MN\u0005\u0012\u0000\u0000NO\u0005\u0010\u0000\u0000OP\u0005\u0012"+
		"\u0000\u0000PQ\u0005\u0012\u0000\u0000QR\u0005\u000f\u0000\u0000RS\u0005"+
		"\u0011\u0000\u0000ST\u0005\u0002\u0000\u0000T\u000f\u0001\u0000\u0000"+
		"\u0000UV\u0005\u0012\u0000\u0000VW\u0005\u0004\u0000\u0000WX\u0005\u0012"+
		"\u0000\u0000XY\u0005\u0004\u0000\u0000YZ\u0005\u0012\u0000\u0000Z\u0011"+
		"\u0001\u0000\u0000\u0000\u0003\u0015\u0017,";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}