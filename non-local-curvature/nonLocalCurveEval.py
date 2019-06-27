import ast
import scipy.integrate as inte
import scipy
from sympy import *
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
        total = 0.0
        for i in range(10, 1, -1):
            p = (4*cos(float((i *pi)/180)), 4*sin(float((i *pi)/180)))
            I = inte.dblquad(lambda r,theta:
            (float(1/2)*(self.eval_char_func((0,0),(r*math.cos(theta), r*math.sin(theta)))/r**(1+float(1/2)))),
            0, 2*pi, float(i/100000), np.inf)
            print("Integral evals to: " + str(I) + "\tThe angle is: " + str(i))
            # if I[0] > 100000 or I[0] == np.inf or I[0] == -np.inf:
            #     continue
            # else:
            #     total += float(I[0])
        print(total)
