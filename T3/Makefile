ANTLR_JAR=antlr-4.13.2-complete.jar
GRAMMAR=LA.g4

gen:
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor $(GRAMMAR)
	@echo "Generating Python files from ANTLR grammar..."




clean:
	rm -f LA*.py LA*.tokens *.interp
	rm -rf .antlr __pycache__
	find . -name "*.pyc" -delete


test: clean gen
	bash -c "source .venv/bin/activate && python3 -B test.py"
