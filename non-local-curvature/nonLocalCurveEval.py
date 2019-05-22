import ast
import scipy.integrate as inte
import scipy
from sympy import *
import integration_lib.function as func
from numpy import sqrt, sin, cos, pi
import numpy as np
import sys
import math

class Eval:

    def __init__(self, func):

        self.char_func = func
        self.eval()

    def eval_char_func(self, p1, p2):
        if not self.char_func.check(p1,p2):
            return 1
        else:
            return -1

    def eval(self):
        p = (2,0)
        I = inte.dblquad(lambda x,y: (self.eval_char_func(p,(x,y))/sqrt((p[0] - x)**2 + (p[1]- y)**2)),
        -np.inf, np.inf, -np.inf, np.inf)
        print(I)
