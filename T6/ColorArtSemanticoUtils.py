class ColorArtSemanticoUtils:
    errosSemanticos = []

    @staticmethod
    def adicionarErroSemantico(token, mensagem):
        linha = token.line
        coluna = token.column
        erro = f"Erro semântico na linha {linha}, coluna {coluna}: {mensagem}"
        ColorArtSemanticoUtils.errosSemanticos.append(erro)

    @staticmethod
    def limparErros():
        ColorArtSemanticoUtils.errosSemanticos = [] 