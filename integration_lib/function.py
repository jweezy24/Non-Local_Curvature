import parser

class math_function:
    def __init__(self, str):

        self.func = parser.expr(str).compile()
