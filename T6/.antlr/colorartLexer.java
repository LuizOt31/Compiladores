// Generated from /home/lo/Documentos/Obsidian/UFSCar/7_semestre/Compiladores/Compiladores/T6/colorart.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class colorartLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, CANVAS=5, COLOR=6, CIRCLE=7, RECTANGLE=8, 
		SQUARE=9, LINE=10, RADIUS=11, WIDTH=12, HEIGHT=13, FILL=14, STROKE=15, 
		TO=16, VAR=17, INT=18, WS=19, COMMENT=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "CANVAS", "COLOR", "CIRCLE", "RECTANGLE", 
			"SQUARE", "LINE", "RADIUS", "WIDTH", "HEIGHT", "FILL", "STROKE", "TO", 
			"VAR", "INT", "WS", "COMMENT"
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


	public colorartLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "colorart.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0014\u0097\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0005\u0010\u0081\b\u0010\n\u0010"+
		"\f\u0010\u0084\t\u0010\u0001\u0011\u0004\u0011\u0087\b\u0011\u000b\u0011"+
		"\f\u0011\u0088\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0005\u0013\u0091\b\u0013\n\u0013\f\u0013\u0094\t\u0013\u0001"+
		"\u0013\u0001\u0013\u0000\u0000\u0014\u0001\u0001\u0003\u0002\u0005\u0003"+
		"\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015"+
		"\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012"+
		"%\u0013\'\u0014\u0001\u0000\u0004\u0003\u0000AZ__az\u0004\u000009AZ__"+
		"az\u0003\u0000\t\n\r\r  \u0002\u0000\n\n\r\r\u0099\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000"+
		"#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001"+
		"\u0000\u0000\u0000\u0001)\u0001\u0000\u0000\u0000\u0003+\u0001\u0000\u0000"+
		"\u0000\u0005-\u0001\u0000\u0000\u0000\u0007/\u0001\u0000\u0000\u0000\t"+
		"1\u0001\u0000\u0000\u0000\u000b8\u0001\u0000\u0000\u0000\r>\u0001\u0000"+
		"\u0000\u0000\u000fE\u0001\u0000\u0000\u0000\u0011O\u0001\u0000\u0000\u0000"+
		"\u0013V\u0001\u0000\u0000\u0000\u0015[\u0001\u0000\u0000\u0000\u0017b"+
		"\u0001\u0000\u0000\u0000\u0019h\u0001\u0000\u0000\u0000\u001bo\u0001\u0000"+
		"\u0000\u0000\u001dt\u0001\u0000\u0000\u0000\u001f{\u0001\u0000\u0000\u0000"+
		"!~\u0001\u0000\u0000\u0000#\u0086\u0001\u0000\u0000\u0000%\u008a\u0001"+
		"\u0000\u0000\u0000\'\u008e\u0001\u0000\u0000\u0000)*\u0005-\u0000\u0000"+
		"*\u0002\u0001\u0000\u0000\u0000+,\u0005;\u0000\u0000,\u0004\u0001\u0000"+
		"\u0000\u0000-.\u0005=\u0000\u0000.\u0006\u0001\u0000\u0000\u0000/0\u0005"+
		",\u0000\u00000\b\u0001\u0000\u0000\u000012\u0005c\u0000\u000023\u0005"+
		"a\u0000\u000034\u0005n\u0000\u000045\u0005v\u0000\u000056\u0005a\u0000"+
		"\u000067\u0005s\u0000\u00007\n\u0001\u0000\u0000\u000089\u0005c\u0000"+
		"\u00009:\u0005o\u0000\u0000:;\u0005l\u0000\u0000;<\u0005o\u0000\u0000"+
		"<=\u0005r\u0000\u0000=\f\u0001\u0000\u0000\u0000>?\u0005c\u0000\u0000"+
		"?@\u0005i\u0000\u0000@A\u0005r\u0000\u0000AB\u0005c\u0000\u0000BC\u0005"+
		"l\u0000\u0000CD\u0005e\u0000\u0000D\u000e\u0001\u0000\u0000\u0000EF\u0005"+
		"r\u0000\u0000FG\u0005e\u0000\u0000GH\u0005c\u0000\u0000HI\u0005t\u0000"+
		"\u0000IJ\u0005a\u0000\u0000JK\u0005n\u0000\u0000KL\u0005g\u0000\u0000"+
		"LM\u0005l\u0000\u0000MN\u0005e\u0000\u0000N\u0010\u0001\u0000\u0000\u0000"+
		"OP\u0005s\u0000\u0000PQ\u0005q\u0000\u0000QR\u0005u\u0000\u0000RS\u0005"+
		"a\u0000\u0000ST\u0005r\u0000\u0000TU\u0005e\u0000\u0000U\u0012\u0001\u0000"+
		"\u0000\u0000VW\u0005l\u0000\u0000WX\u0005i\u0000\u0000XY\u0005n\u0000"+
		"\u0000YZ\u0005e\u0000\u0000Z\u0014\u0001\u0000\u0000\u0000[\\\u0005r\u0000"+
		"\u0000\\]\u0005a\u0000\u0000]^\u0005d\u0000\u0000^_\u0005i\u0000\u0000"+
		"_`\u0005u\u0000\u0000`a\u0005s\u0000\u0000a\u0016\u0001\u0000\u0000\u0000"+
		"bc\u0005w\u0000\u0000cd\u0005i\u0000\u0000de\u0005d\u0000\u0000ef\u0005"+
		"t\u0000\u0000fg\u0005h\u0000\u0000g\u0018\u0001\u0000\u0000\u0000hi\u0005"+
		"h\u0000\u0000ij\u0005e\u0000\u0000jk\u0005i\u0000\u0000kl\u0005g\u0000"+
		"\u0000lm\u0005h\u0000\u0000mn\u0005t\u0000\u0000n\u001a\u0001\u0000\u0000"+
		"\u0000op\u0005f\u0000\u0000pq\u0005i\u0000\u0000qr\u0005l\u0000\u0000"+
		"rs\u0005l\u0000\u0000s\u001c\u0001\u0000\u0000\u0000tu\u0005s\u0000\u0000"+
		"uv\u0005t\u0000\u0000vw\u0005r\u0000\u0000wx\u0005o\u0000\u0000xy\u0005"+
		"k\u0000\u0000yz\u0005e\u0000\u0000z\u001e\u0001\u0000\u0000\u0000{|\u0005"+
		"t\u0000\u0000|}\u0005o\u0000\u0000} \u0001\u0000\u0000\u0000~\u0082\u0007"+
		"\u0000\u0000\u0000\u007f\u0081\u0007\u0001\u0000\u0000\u0080\u007f\u0001"+
		"\u0000\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000\u0082\u0080\u0001"+
		"\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\"\u0001\u0000"+
		"\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0087\u000209\u0000"+
		"\u0086\u0085\u0001\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000"+
		"\u0088\u0086\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000"+
		"\u0089$\u0001\u0000\u0000\u0000\u008a\u008b\u0007\u0002\u0000\u0000\u008b"+
		"\u008c\u0001\u0000\u0000\u0000\u008c\u008d\u0006\u0012\u0000\u0000\u008d"+
		"&\u0001\u0000\u0000\u0000\u008e\u0092\u0005%\u0000\u0000\u008f\u0091\b"+
		"\u0003\u0000\u0000\u0090\u008f\u0001\u0000\u0000\u0000\u0091\u0094\u0001"+
		"\u0000\u0000\u0000\u0092\u0090\u0001\u0000\u0000\u0000\u0092\u0093\u0001"+
		"\u0000\u0000\u0000\u0093\u0095\u0001\u0000\u0000\u0000\u0094\u0092\u0001"+
		"\u0000\u0000\u0000\u0095\u0096\u0006\u0013\u0000\u0000\u0096(\u0001\u0000"+
		"\u0000\u0000\u0004\u0000\u0082\u0088\u0092\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}