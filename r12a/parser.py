from rply import ParserGenerator, Token, ParsingError
from rply.token import BaseBox


class BoxInt(BaseBox):
    def __init__(self, value):
        self.value = value

    def getint(self):
        return self.value

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer

    def parse(self):
        return self.parser.parse(self.lexer.lex())

    pg = ParserGenerator(["NUMBER", "PLUS", "MINUS"],
                         precedence=[("left", ['PLUS', 'MINUS'])],
                         cache_id="r12a")

    @pg.production("main : expr")
    def main(p):
        return p[0]

    @pg.production("expr : expr PLUS expr")
    @pg.production("expr : expr MINUS expr")
    def expr_op(p):
        lhs = p[0].getint()
        rhs = p[2].getint()
        if p[1].gettokentype() == "PLUS":
            return BoxInt(lhs + rhs)
        elif p[1].gettokentype() == "MINUS":
            return BoxInt(lhs - rhs)
        else:
            raise AssertionError("This is impossible, abort the time machine!")

    @pg.production("expr : NUMBER")
    def expr_num(p):
        return BoxInt(int(p[0].getstr()))

    parser = pg.build()
