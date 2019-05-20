import parser
import sys
import integration_lib.function_parsing_utils as utils
import numpy as np
import scipy
from numpy import sqrt, sin, cos, pi
import sympy

this_mod = sys.modules[__name__]

class math_function:

    def __init__(self, args):
        if type(args) == type({}):
            self.vars = utils.variable_parser(args)
            self.original_str = args["args"]["function"]
            checker = True
            self.double_var = False
            self.func = parser.expr(args["args"]["function"]).compile()
            if 'None' != args["args"]["functions"] and 'R**2' != args["args"]["functions"]:
                self.domain = self.generate_functions_from_domain(args["args"]["functions"])
                self.domain_range = None
                if self.domain:
                    self.intersections = self.find_domain_intersections()
            elif 'R**2' == args["args"]["functions"]:
                self.domain = [-np.inf, np.inf]
            elif 'None' != args["args"]["range"]:
                self.domain_range = utils.range_parse(args["args"]["range"])
                self.domain = None
            else:
                self.domain = args["args"]["functions"]

        elif type(args) == type(''):
            self.double_var = False
            self.vars = utils.variable_parser(args)
            self.original_str = args
            checker = True
            self.func = parser.expr(args).compile()
            self.domain = 0

    def run_func(self, args):
        if len(args) != len(self.vars):
            #print("len(args): " + str(len(args)))
            #print("len(self.vars): " + str(len(self.vars)))
            return False
        else:
            template = '''{0} = {1}\n'''
            strng = ''
            filename = ''
            for i in range(0, len(self.vars)):
                strng += template.format(self.vars[i], args[i])
            code = compile(strng, filename, 'exec')
            exec(code)
            return eval(self.func)

    def generate_functions_from_domain(self, domainStr):
        #print("DOMAIN STR: " + str(domainStr))
        if type(domainStr) == type(''):
            tmp_d = domainStr.split(',')
            tmp_d2 = domainStr.split(',')
            functions = []
            x = sympy.Symbol('x')
            y = sympy.Symbol('y')
            if 'y=' and 'x=' in domainStr:
                print([tmp_d2[0].replace('=', '-'), tmp_d2[1].replace('=', '-')])
                tmp_test = sympy.solve([tmp_d2[0].replace('=', '-'), tmp_d2[1].replace('=', '-')], x,y)
                print("GENERATE: " + str(tmp_test))
                self.double_var = True
            for i in tmp_d:
                if '=' in i and not self.double_var:
                    holder = i.split('=')
                    functions.append(math_function(holder[1].strip()))
                elif self.double_var:
                    self.intersections = [sympy.solve([tmp_d2[0].replace('=', '-'), tmp_d2[1].replace('=', '-')], x,y)[0][1], 0]
                    holder = i.split('=')
                    functions.append(math_function(holder[1].strip()))

            return functions
        else:
            return None

    def find_domain_intersections(self):
        negative = False
        intersections = []
        if self.double_var:
            return self.intersections
        try:
            x = sympy.Symbol('x')
            y = sympy.Symbol('y')
            print(self.domain)
            tmp_test = sympy.solve(self.domain[0].original_str + ' - ' + self.domain[1].original_str, x,y)
            print("FINISHED: " + str(tmp_test))
            if 'x' in str(tmp_test):
                if type(tmp_test[0][1]) != type(0) or type(tmp_test[1][1]) != type(0.0):
                    if 'I' in str(tmp_test[0][1]):
                        intersections.append(float(complex(tmp_test[0][1]).real))
                        intersections.append(float(complex(tmp_test[1][1]).real))
                    else:
                        if len(tmp_test) == 1:
                            #intersections.append(eval(str(sympy.sympify(tmp_test[0][1]))))
                            if len(self.domain) > 1:
                                if type(self.domain[1].run_func([float(eval('-'+str(sympy.sympify(tmp_test[0][1]))))])) != type(0.0):
                                    intersections.append(eval(str(sympy.sympify(tmp_test[0][1]))))
                                    intersections.append(0.0)
                                else:
                                    intersections.append(eval(str(sympy.sympify(tmp_test[0][1]))))
                                    intersections.append(eval('-'+str(sympy.sympify(tmp_test[0][1]))))
                            else:
                                if type(self.domain[0].run_func([float(eval('-'+str(sympy.sympify(tmp_test[0][1]))))])) != type(0.0):
                                    intersections.append(eval(str(sympy.sympify(tmp_test[0][1]))))
                                    intersections.append(0.0)
                                else:
                                    intersections.append(eval(str(sympy.sympify(tmp_test[0][1]))))
                                    intersections.append(eval('-'+str(sympy.sympify(tmp_test[0][1]))))
                        else:
                            intersections.append(eval(str(sympy.sympify(tmp_test[0][1]))))
                            intersections.append(eval(str(sympy.sympify(tmp_test[1][1]))))

                else:
                    intersections.append(float(tmp_test[0][1]))
                    intersections.append(float(tmp_test[1][1]))
            else:
                if type(tmp_test[0][0]) != type(0) or type(tmp_test[1][0]) != type(0.0):
                    if 'I' in str(tmp_test[0][0]):
                        intersections.append(float(complex(tmp_test[0][0]).real))
                        intersections.append(float(complex(tmp_test[1][0]).real))
                    else:
                        if len(tmp_test) == 1:
                            if len(self.domain) > 1:
                                if type(self.domain[1].run_func([float(eval('-'+str(sympy.sympify(tmp_test[0][0]))))])) != type(0.0):
                                    intersections.append(eval(str(sympy.sympify(tmp_test[0][0]))))
                                    intersections.append(0.0)
                                else:
                                    intersections.append(eval(str(sympy.sympify(tmp_test[0][0]))))
                                    intersections.append(eval('-'+str(sympy.sympify(tmp_test[0][0]))))
                            else:
                                if type(self.domain[0].run_func([float(eval('-'+str(sympy.sympify(tmp_test[0][0]))))])) != type(0.0):
                                    intersections.append(eval(str(sympy.sympify(tmp_test[0][0]))))
                                    intersections.append(0.0)
                                else:
                                    intersections.append(eval(str(sympy.sympify(tmp_test[0][0]))))
                                    intersections.append(eval('-'+str(sympy.sympify(tmp_test[0][0]))))
                        else:
                            intersections.append(eval(str(sympy.sympify(tmp_test[0][0]))))
                            intersections.append(eval(str(sympy.sympify(tmp_test[1][0]))))

                else:
                    intersections.append(float(tmp_test[0][0]))
                    intersections.append(float(tmp_test[1][0]))
        except Exception as e:
            print("Line {0} exception: {1}".format(sys.exc_info()[-1].tb_lineno, str(e)))


        return intersections


    def find_intersections(self):
        pass

    def f(self, xy):
        x,y = xy
        z = np.array([eval('y-(' + self.domain[0].original_str + ')'), eval('y-(' + self.domain[1].original_str + ')')])
        return z
