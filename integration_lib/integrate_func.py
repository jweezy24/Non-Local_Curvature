import ast
import scipy.integrate as inte
from sympy import *


class integral:

    def __init__(self, function):

        self.func = function

    def integrate(self):
        print(self.func.func)
        x = Symbol('x')
        y= Symbol('y')
        print(integrate(self.func.original_str, x, ))
        I = inte.quad(self.eval_func, 0, 1, args=self.func.vars)
        print(I)

    def eval_func(self, *arg):
        return self.func.run_func([arg[0],arg[0]])
