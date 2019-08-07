import ast
import scipy.integrate as inte
import scipy
from sympy import *
from numpy import sqrt, sin, cos, pi
import numpy as np
import sys
import math
import time

class Eval:

    def __init__(self, func):

        self.char_func = func
        self.eval()

    def eval_char_func(self, p1, p2):
        val = self.char_func.check(p1,p2)
        if val == None:
            return 0
        elif val:
            return 1
        else:
            return -1

    def eval(self):
        total = 0.0
        #for i in range(10, 1, -1):
        I = inte.dblquad(lambda r,theta:
        self.holder(r,theta),
        0, 2*pi, float(1/100000), np.inf)
        print("Integral evals to: " + str(I))
        print(total)

    def holder(self, r, theta):
        #print("point is " + str((r, theta)))
        vector_x = self.char_func.start[0]-r*np.cos(theta) 
        vector_y = self.char_func.start[1]-r*np.sin(theta)
        norm = math.sqrt(vector_x**2 + vector_y**2)
        #working code
        return float(1/2)*(self.eval_char_func(self.char_func.start,(r*np.cos(theta), r*np.sin(theta)))/norm**(1+float(1/2)))
        #return float(1/2)*(self.eval_char_func((0,0),(r, theta))/r**(1+float(1/2)))
