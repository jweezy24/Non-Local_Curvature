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

    def __init__(self, func, random):

        self.char_func = func
        epsilon = 100
        for i in range(1,10):
            time1 = time.time()
            epsilon = 10000
            self.val = self.eval(epsilon)
            time2 = time.time()
            self.actual = -5.24411510858423962093
            print('Evaluation of Integral took {:.3f} minutes'.format( (time2-time1)/60))
            error = abs(abs(self.actual - self.val)/self.actual)
            print('Error evaluate to, {:.2f}'.format(error*100))
            if random:
                with open('./results_random.txt', 'a') as f:
                    f.write(f'Error percent: {error}\tEpsilon:1/{epsilon}\tDomain Size: {self.char_func.domain_size} \tIntegration Evaluation: {self.val}\t Time: {((time2-time1)/60)}\n')
                if error*100 < 1:
                    with open('./random_domains.txt', 'a') as f:
                        f.write(f'Domain: {str(self.char_func.domain)}')
                        f.write(f' Error for this domain: {error}\t Domain Size: {self.char_func.domain_size}\t Epsilon: {epsilon}')
            else:
                with open('./results_without_random.txt', 'a') as f:
                    f.write(f'Error percent: {error}\tEpsilon:1/{epsilon}\tDomain Size: {self.char_func.domain_size} \tIntegration Evaluation: {self.val}\t Time: {((time2-time1)/60)}\n')


        #self.weezy_integration = lambda func, range: jack_integral.integrate(func, range)

    def eval_char_func(self, p1, p2):
        val = self.char_func.check(p1,p2)
        if val:
            return 1
        else:
            return -1

    def eval(self,epsilon):
        total = 0.0
        #for i in range(10, 1, -1):
        #I_1 = scipy.integrate.dblquad(lambda x,y: self.holder(x,y), -np.inf, self.char_func.start[1]-float(1/epsilon), -np.inf, self.char_func.start[0]-float(1/epsilon))[0]
        #I_2 = scipy.integrate.dblquad(lambda x,y: self.holder(x,y), self.char_func.start[1]+float(1/epsilon), np.inf , self.char_func.start[0]+float(1/epsilon), np.inf)[0]
        
        #I_1 = scipy.integrate.dblquad(lambda x,y: self.holder(x,y), self.char_func.start[1]-epsilon, self.char_func.start[1]-float(1/epsilon),  self.char_func.start[0]-epsilon, self.char_func.start[0]-float(1/epsilon))[0]
        #I_2 = scipy.integrate.dblquad(lambda x,y: self.holder(x,y), self.char_func.start[1]+float(1/epsilon), self.char_func.start[1]+epsilon,  self.char_func.start[0]+float(1/epsilon), self.char_func.start[0]+epsilon)[0]

        I_1 = scipy.integrate.dblquad(lambda r,theta: self.holder(r,theta), 0, (3*np.pi/2)-float(1/epsilon), lambda x: -np.inf, lambda y: -2-float(1/epsilon))[0]
        I_2 = scipy.integrate.dblquad(lambda r,theta: self.holder(r,theta), (3*np.pi/2)+float(1/epsilon), 2*np.pi, lambda x: -2+float(1/epsilon), lambda y: np.inf)[0]
        
        print("Integral1 evals to: " + str(I_1))
        print("Integral2 evals to: " + str(I_2))
        print("Integral evals to: " + str(I_1 + I_2))
        return I_1+I_2

    def holder(self, x, y):
        #print("point is " + str((r, theta)))
        #vector_x = self.char_func.start[0]-x
        #vector_y = self.char_func.start[1]-y
        vector_x = self.char_func.start[0]-(x*cos(y))
        vector_y = self.char_func.start[1]-(x*sin(y))

        x_1 = (x*cos(y))
        y_1 = (x*sin(y))

        norm = math.sqrt(vector_x**2 + vector_y**2)
        #working code
        return float(1/2)*(float(self.eval_char_func(self.char_func.start,(x_1, y_1))/norm**(1+float(1/2))))
        #return float(1/2)*(self.eval_char_func((0,0),(r, theta))/r**(1+float(1/2)))
