from rply import Token, LexerGenerator
from rply.errors import LexingError
from rply.token import SourcePosition

class LexerError(Exception):
    pass

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
        stream = self.lexer.lex(self.source)
        return LexerWrapper(stream)

class LexerWrapper(object):
    def __init__(self, stream):
        self.stream = stream

    def next(self):
        try:
            token = self.stream.next()
            #if token:
            #    print token.name, token.value
            return token
        except StopIteration:
            return None
        except LexingError, e:
            raise LexerError()
