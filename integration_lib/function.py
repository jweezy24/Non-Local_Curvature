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
            self.func = parser.expr(args["args"]["function"]).compile()
            if 'None' != args["args"]["functions"]:
                self.domain = self.generate_functions_from_domain(args["args"]["functions"])
                self.domain_range = None
                if self.domain:
                    self.intersections = self.find_domain_intersections()
            elif 'None' != args["args"]["range"]:
                self.domain_range = utils.range_parse(args["args"]["range"])
                self.domain = None
            else:
                self.domain = args["args"]["functions"]

        elif type(args) == type(''):
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
            template = '''from math import *\n{0} = {1}\n'''
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
        try:
            x = sympy.Symbol('x')
            y = sympy.Symbol('y')
            tmp_test = sympy.solve(self.domain[0].original_str + ' - ' + self.domain[1].original_str, x,y)
            print("FINISHED: " + str(tmp_test))
            if 'x' in str(tmp_test):
                inte_1 = scipy.optimize.fsolve(self.f, [float(tmp_test[0][1]), 0.0]).item(0)
                inte_2 = scipy.optimize.fsolve(self.f, [float(tmp_test[1][1]), 0.0]).item(0)
                intersections.append(inte_1)
                intersections.append(inte_2)
            else:
                inte_1 = scipy.optimize.fsolve(self.f, [float(tmp_test[0][0]), 0.0]).item(0)
                inte_2 = scipy.optimize.fsolve(self.f, [float(tmp_test[1][0]), 0.0]).item(0)
                intersections.append(inte_1)
                intersections.append(inte_2)
        except Exception as e:
            print(e)



        min = 'West'
        max = 'Jack'
        #print(intersections)
        for i in intersections:
            if min == 'West':
                min = i
            elif min < i:
                min = i
            if max == 'Jack':
                max = i
            elif max > i:
                max = i
        intersections = [min,max]
        return intersections

    def f(self, xy):
        x,y = xy
        z = np.array([eval('y-(' + self.domain[0].original_str + ')'), eval('y-(' + self.domain[1].original_str + ')')])
        return z
