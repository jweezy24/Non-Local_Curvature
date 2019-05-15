import parser
import sys
import integration_lib.function_parsing_utils as utils

this_mod = sys.modules[__name__]

class math_function:

    def __init__(self, args):
        if type(args) == type({}):
            self.vars = utils.variable_parser(args)
            self.original_str = args["args"]["function"]
            checker = True
            self.func = parser.expr(args["args"]["function"]).compile()
            if 'None' != args["args"]["domain"]:
                self.domain = self.generate_functions_from_domain(args["args"]["domain"])
                if self.domain:
                    self.intersections = self.find_domain_intersections()
            elif 'None' != args["args"]["range"]:
                self.domain_range = utils.range_parse(args["args"]["range"])
                self.domain = None
            else:
                self.domain = args["args"]["domain"]

        elif type(args) == type(''):
            self.vars = utils.variable_parser(args)
            self.original_str = args
            checker = True
            self.func = parser.expr(args).compile()
            self.domain = 0

    def run_func(self, args):
        if len(args) != len(self.vars):
            print("len(args): " + str(len(args)))
            print("len(self.vars): " + str(len(self.vars)))
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
        print("DOMAIN STR: " + str(domainStr))
        if type(domainStr) == type(''):
            tmp_d = domainStr.split(',')
            functions = []
            for i in tmp_d:
                if '=' in i:
                    holder = i.split('=')
                    functions.append(math_function(holder[1].strip()))

            return functions
        else:
            return None

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
                    if float(avg/len(self.domain)) == float(j.run_func([i])):
                        if i not in intersections:
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
