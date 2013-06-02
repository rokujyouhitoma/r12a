from rply import Token, LexerGenerator
from rply.token import oSourcePosition

class Lexer(object):

    def __init__(self, source):
        self.source = source
