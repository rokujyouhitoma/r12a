from rply import Token, LexerGenerator
from rply.token import SourcePosition


class Keyword(object):
    def __init__(self, normal_token, inline_token, state):
        self.normal_token = normal_token
        self.inline_token = inline_token
        self.state = state

class Lexer(object):

    EXPR_END = 1

    keywords = {
    }

    def __init__(self, source, initial_lineno):
        self.source = source
        self.lineno = initial_lineno
        self.current_value = []
        self.idx = 0
        self.columno = 1

    def emit(self, token):
        value = "".join(self.current_value)
        self.clear()
        return Token(token, value, self.current_pos())

    def clear(self):
        del self.current_value[:]

    def current_pos(self):
        return SourcePosition(self.idx, self.lineno, self.columno)

    def tokenize(self):
        while True:
            yield self.emit("PLUS")
            #yield self.emit("MINUS")
