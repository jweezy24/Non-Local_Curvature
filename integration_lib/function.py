import parser
import sys

this_mod = sys.modules[__name__]

class math_function:

    def __init__(self, str):
        self.vars = []
        self.original_str = str
        for i in str:
            if ord(i) >= 97 and ord(i) <= 122:
                self.vars.append(i)
            else:
                continue
        self.func = parser.expr(str).compile()

    def run_func(self, args):
        if len(args) != len(self.vars):
            print("need more args")
            return False
        else:
            template = '{0} = {1}\n'
            strng = ''
            filename = ''
            for i in range(0, len(self.vars)):
                strng += template.format(self.vars[i], args[i])
            code = compile(strng, filename, 'exec')
            exec(code)
            return eval(self.func)
