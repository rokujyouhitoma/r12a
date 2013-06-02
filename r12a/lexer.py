from rply import Token, LexerGenerator
from rply.token import SourcePosition

class Lexer(object):
    def __init__(self, source):
        self.source = source

    lg = LexerGenerator()
    lg.add("PLUS", r"\+")
    lg.add("MINUS", r"-")
    lg.add("NUMBER", r"\d+")
    lg.ignore(r"\s+")

    lexer = lg.build()

    def lex(self):
        return self.lexer.lex(self.source)
