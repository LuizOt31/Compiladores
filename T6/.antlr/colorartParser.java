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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, VAR=16, HEXCOLOR=17, 
		INT=18, WS=19, COMMENT=20;
	public static final int
		RULE_program = 0, RULE_canvasDecl = 1, RULE_colorDecl = 2, RULE_shapeDecl = 3, 
		RULE_circleDecl = 4, RULE_rectangleDecl = 5, RULE_squareDecl = 6, RULE_lineDecl = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "canvasDecl", "colorDecl", "shapeDecl", "circleDecl", "rectangleDecl", 
			"squareDecl", "lineDecl"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'canvas'", "'x'", "';'", "'color'", "'='", "'circle'", "'radius'", 
			"'fill'", "'rectangle'", "'width'", "'height'", "'square'", "'line'", 
			"'to'", "'stroke'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "VAR", "HEXCOLOR", "INT", "WS", "COMMENT"
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
			setState(16);
			canvasDecl();
			setState(21);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8784L) != 0)) {
				{
				setState(19);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__3:
					{
					setState(17);
					colorDecl();
					}
					break;
				case T__5:
				case T__8:
				case T__12:
					{
					setState(18);
					shapeDecl();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(23);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(24);
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
			setState(26);
			match(T__0);
			setState(27);
			match(INT);
			setState(28);
			match(T__1);
			setState(29);
			match(INT);
			setState(30);
			match(T__2);
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
		public TerminalNode VAR() { return getToken(colorartParser.VAR, 0); }
		public TerminalNode HEXCOLOR() { return getToken(colorartParser.HEXCOLOR, 0); }
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
			setState(32);
			match(T__3);
			setState(33);
			match(VAR);
			setState(34);
			match(T__4);
			setState(35);
			match(HEXCOLOR);
			setState(36);
			match(T__2);
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
		public ShapeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shapeDecl; }
	}

	public final ShapeDeclContext shapeDecl() throws RecognitionException {
		ShapeDeclContext _localctx = new ShapeDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_shapeDecl);
		try {
			setState(41);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				circleDecl();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				rectangleDecl();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 3);
				{
				setState(40);
				lineDecl();
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
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
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
			setState(43);
			match(T__5);
			setState(44);
			match(INT);
			setState(45);
			match(INT);
			setState(46);
			match(T__6);
			setState(47);
			match(INT);
			setState(48);
			match(T__7);
			setState(49);
			match(VAR);
			setState(50);
			match(T__2);
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
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
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
			setState(52);
			match(T__8);
			setState(53);
			match(INT);
			setState(54);
			match(INT);
			setState(55);
			match(T__9);
			setState(56);
			match(INT);
			setState(57);
			match(T__10);
			setState(58);
			match(INT);
			setState(59);
			match(T__7);
			setState(60);
			match(VAR);
			setState(61);
			match(T__2);
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
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
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
			setState(63);
			match(T__11);
			setState(64);
			match(INT);
			setState(65);
			match(INT);
			setState(66);
			match(T__9);
			setState(67);
			match(INT);
			setState(68);
			match(T__7);
			setState(69);
			match(VAR);
			setState(70);
			match(T__2);
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
		public List<TerminalNode> INT() { return getTokens(colorartParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(colorartParser.INT, i);
		}
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
			setState(72);
			match(T__12);
			setState(73);
			match(INT);
			setState(74);
			match(INT);
			setState(75);
			match(T__13);
			setState(76);
			match(INT);
			setState(77);
			match(INT);
			setState(78);
			match(T__14);
			setState(79);
			match(VAR);
			setState(80);
			match(T__2);
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
		"\u0004\u0001\u0014S\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u0014\b\u0000\n\u0000\f\u0000"+
		"\u0017\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003*\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0000\u0000\b\u0000\u0002\u0004\u0006\b\n\f\u000e\u0000\u0000N\u0000"+
		"\u0010\u0001\u0000\u0000\u0000\u0002\u001a\u0001\u0000\u0000\u0000\u0004"+
		" \u0001\u0000\u0000\u0000\u0006)\u0001\u0000\u0000\u0000\b+\u0001\u0000"+
		"\u0000\u0000\n4\u0001\u0000\u0000\u0000\f?\u0001\u0000\u0000\u0000\u000e"+
		"H\u0001\u0000\u0000\u0000\u0010\u0015\u0003\u0002\u0001\u0000\u0011\u0014"+
		"\u0003\u0004\u0002\u0000\u0012\u0014\u0003\u0006\u0003\u0000\u0013\u0011"+
		"\u0001\u0000\u0000\u0000\u0013\u0012\u0001\u0000\u0000\u0000\u0014\u0017"+
		"\u0001\u0000\u0000\u0000\u0015\u0013\u0001\u0000\u0000\u0000\u0015\u0016"+
		"\u0001\u0000\u0000\u0000\u0016\u0018\u0001\u0000\u0000\u0000\u0017\u0015"+
		"\u0001\u0000\u0000\u0000\u0018\u0019\u0005\u0000\u0000\u0001\u0019\u0001"+
		"\u0001\u0000\u0000\u0000\u001a\u001b\u0005\u0001\u0000\u0000\u001b\u001c"+
		"\u0005\u0012\u0000\u0000\u001c\u001d\u0005\u0002\u0000\u0000\u001d\u001e"+
		"\u0005\u0012\u0000\u0000\u001e\u001f\u0005\u0003\u0000\u0000\u001f\u0003"+
		"\u0001\u0000\u0000\u0000 !\u0005\u0004\u0000\u0000!\"\u0005\u0010\u0000"+
		"\u0000\"#\u0005\u0005\u0000\u0000#$\u0005\u0011\u0000\u0000$%\u0005\u0003"+
		"\u0000\u0000%\u0005\u0001\u0000\u0000\u0000&*\u0003\b\u0004\u0000\'*\u0003"+
		"\n\u0005\u0000(*\u0003\u000e\u0007\u0000)&\u0001\u0000\u0000\u0000)\'"+
		"\u0001\u0000\u0000\u0000)(\u0001\u0000\u0000\u0000*\u0007\u0001\u0000"+
		"\u0000\u0000+,\u0005\u0006\u0000\u0000,-\u0005\u0012\u0000\u0000-.\u0005"+
		"\u0012\u0000\u0000./\u0005\u0007\u0000\u0000/0\u0005\u0012\u0000\u0000"+
		"01\u0005\b\u0000\u000012\u0005\u0010\u0000\u000023\u0005\u0003\u0000\u0000"+
		"3\t\u0001\u0000\u0000\u000045\u0005\t\u0000\u000056\u0005\u0012\u0000"+
		"\u000067\u0005\u0012\u0000\u000078\u0005\n\u0000\u000089\u0005\u0012\u0000"+
		"\u00009:\u0005\u000b\u0000\u0000:;\u0005\u0012\u0000\u0000;<\u0005\b\u0000"+
		"\u0000<=\u0005\u0010\u0000\u0000=>\u0005\u0003\u0000\u0000>\u000b\u0001"+
		"\u0000\u0000\u0000?@\u0005\f\u0000\u0000@A\u0005\u0012\u0000\u0000AB\u0005"+
		"\u0012\u0000\u0000BC\u0005\n\u0000\u0000CD\u0005\u0012\u0000\u0000DE\u0005"+
		"\b\u0000\u0000EF\u0005\u0010\u0000\u0000FG\u0005\u0003\u0000\u0000G\r"+
		"\u0001\u0000\u0000\u0000HI\u0005\r\u0000\u0000IJ\u0005\u0012\u0000\u0000"+
		"JK\u0005\u0012\u0000\u0000KL\u0005\u000e\u0000\u0000LM\u0005\u0012\u0000"+
		"\u0000MN\u0005\u0012\u0000\u0000NO\u0005\u000f\u0000\u0000OP\u0005\u0010"+
		"\u0000\u0000PQ\u0005\u0003\u0000\u0000Q\u000f\u0001\u0000\u0000\u0000"+
		"\u0003\u0013\u0015)";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}