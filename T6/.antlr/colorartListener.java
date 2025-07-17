// Generated from /home/lo/Documentos/Obsidian/UFSCar/7_semestre/Compiladores/Compiladores/T6/colorart.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link colorartParser}.
 */
public interface colorartListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link colorartParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(colorartParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link colorartParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(colorartParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link colorartParser#canvasDecl}.
	 * @param ctx the parse tree
	 */
	void enterCanvasDecl(colorartParser.CanvasDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link colorartParser#canvasDecl}.
	 * @param ctx the parse tree
	 */
	void exitCanvasDecl(colorartParser.CanvasDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link colorartParser#colorDecl}.
	 * @param ctx the parse tree
	 */
	void enterColorDecl(colorartParser.ColorDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link colorartParser#colorDecl}.
	 * @param ctx the parse tree
	 */
	void exitColorDecl(colorartParser.ColorDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link colorartParser#shapeDecl}.
	 * @param ctx the parse tree
	 */
	void enterShapeDecl(colorartParser.ShapeDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link colorartParser#shapeDecl}.
	 * @param ctx the parse tree
	 */
	void exitShapeDecl(colorartParser.ShapeDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link colorartParser#circleDecl}.
	 * @param ctx the parse tree
	 */
	void enterCircleDecl(colorartParser.CircleDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link colorartParser#circleDecl}.
	 * @param ctx the parse tree
	 */
	void exitCircleDecl(colorartParser.CircleDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link colorartParser#rectangleDecl}.
	 * @param ctx the parse tree
	 */
	void enterRectangleDecl(colorartParser.RectangleDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link colorartParser#rectangleDecl}.
	 * @param ctx the parse tree
	 */
	void exitRectangleDecl(colorartParser.RectangleDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link colorartParser#squareDecl}.
	 * @param ctx the parse tree
	 */
	void enterSquareDecl(colorartParser.SquareDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link colorartParser#squareDecl}.
	 * @param ctx the parse tree
	 */
	void exitSquareDecl(colorartParser.SquareDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link colorartParser#lineDecl}.
	 * @param ctx the parse tree
	 */
	void enterLineDecl(colorartParser.LineDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link colorartParser#lineDecl}.
	 * @param ctx the parse tree
	 */
	void exitLineDecl(colorartParser.LineDeclContext ctx);
}