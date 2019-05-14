import parser
import sys

this_mod = sys.modules[__name__]

class math_function:

    def __init__(self, args):
        if type(args) == type({}):
            self.vars = []
            self.original_str = args["args"]["function"]
            for i in args["args"]["function"]:
                if ord(i) >= 97 and ord(i) <= 122 and 'sqrt' not in args['args']['function']:
                    self.vars.append(i)
                else:
                    continue
            self.func = parser.expr(args["args"]["function"]).compile()
            self.domain = self.generate_functions_from_domain(args["args"]["domain"])
            self.intersections = self.find_domain_intersections()
        elif type(args) == type(''):
            self.vars = []
            self.original_str = args
            checker = True
            for i in args:
                checker = True
                if ord(i) >= 97 and ord(i) <= 122:
                    if 'float' in args:
                        for j in 'float':
                            if i == j:
                                checker = False
                    if checker:
                        self.vars.append(i)
                else:
                    continue
            self.func = parser.expr(args).compile()
            self.domain = 0

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

    def generate_functions_from_domain(self, domainStr):
        tmp_d = domainStr.split(',')
        functions = []
        for i in tmp_d:
            if '=' in i:
                holder = i.split('=')
                functions.append(math_function(holder[1].strip()))
        for i in functions:
            print(i.run_func([1]))

        return functions

    def find_domain_intersections(self):
        negative = False
        intersections = []
        for i in self.domain:
            if '**float' in i.original_str:
                negative = True
                break
        if not negative:
            for i in range(-10001, 10000):
                avg = 0
                for j in self.domain:
                    avg += j.run_func([i])

                for k in self.domain:
                    if avg/3 == j.run_func([i]):
                        intersections.append(i)
        else:
            for i in range(0, 10000):
                avg = 0
                for j in self.domain:
                    avg += float(j.run_func([i]))

                for k in self.domain:
                    if float(avg/len(self.domain)) == float(j.run_func([i])):
                        intersections.append(i)
                        break
        return intersections
