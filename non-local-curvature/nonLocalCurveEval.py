import ast
import scipy.integrate as inte
import scipy
from sympy import *
from numpy import sqrt, sin, cos, pi
import numpy as np
import sys
import math
import time
#import matplotlib.pyplot as plt

class Eval:

    def __init__(self, func, random, default=0, iter=None):

        self.inside_points = []
        self.outside_points = []
        self.point_count = 0

        #algorithm testing for a new algorithm on a circle
        if default == 0:
            self.char_func = func
            epsilon = 100
            for i in range(5,10):
                time1 = time.time()
                epsilon = 10**(i)
                self.val = self.eval(epsilon)
                time2 = time.time()
                self.actual = -5.24411510858423962093
                print('Evaluation of Integral took {:.3f} minutes'.format( (time2-time1)/60))
                error = abs(abs(self.actual - self.val)/self.actual)
                print('Error evaluate to, {:.2f}'.format(error*100))
                with open(f'./results_{self.char_func.alg}.txt', 'a') as f:
                    f.write(f'Error percent: {error}\tEpsilon:1/{float(epsilon)}\tDomain Size: {2*self.char_func.domain_size} \tIntegration Evaluation: {self.val}\t Time: {((time2-time1)/60)}\n')

        elif default == 1:
            self.char_func = func
            for i in range(2, 5):
                epsilon = 10**i
                time1 = time.time()
                self.val = self.eval(epsilon)
                time2 = time.time()
                with open(f'./results_{self.char_func.alg}_ellipse.txt', 'a') as f:
                            f.write(f'Integration Evaluation: {self.val}\t Time: {((time2-time1)/60)}\t EquationX: {self.char_func.func_x}\t EquationY: {self.char_func.func_y}\t iter: {iter}  \n')
        
        elif default == 2:
            self.char_func = func
            for i in range(0,100):
                time1 = time.time()
                epsilon = 10**(6) * (100-i)
                self.val = self.eval(epsilon)
                time2 = time.time()
                self.actual = -5.24411510858423962093
                print('Evaluation of Integral took {:.3f} minutes'.format( (time2-time1)/60))
                error = abs(abs(self.actual - self.val)/self.actual)
                print('Error evaluate to, {:.2f}'.format(error*100))
                with open(f'./results_{self.char_func.alg}.txt', 'a') as f:
                    f.write(f'Error percent: {error}\tEpsilon:1/{float(epsilon)}\tDomain Size: {2*self.char_func.domain_size} \tIntegration Evaluation: {self.val}\t Time: {((time2-time1)/60)}\n')

        #self.weezy_integration = lambda func, range: jack_integral.integrate(func, range)

    def eval_char_func(self, p1, p2):
        val = self.char_func.check(p1,p2)
        #self.point_count += 1
        # if self.point_count >= 10000:
        #     xs = []
        #     ys = []
        #     print(self.char_func.domain)
        #     for point in self.char_func.domain_full:
        #         xs.append(point[0])
        #         ys.append(point[1])
                
        #     plt.plot(xs,ys)
        #     plt.show() 
        #     self.point_count = 0
        #     plt.cfg()
        if val:
            #plt.plot(p2[0],p2[1], 'bo')
            return 1
        else:
            #plt.plot(p2[0],p2[1], 'rx')
            return -1

    def eval(self,epsilon):
        total = 0.0
        #for i in range(10, 1, -1):
        #I_1 = scipy.integrate.dblquad(lambda x,y: self.holder(x,y), -np.inf, self.char_func.start[1]-float(1/epsilon), -np.inf, self.char_func.start[0]-float(1/epsilon))[0]
        #I_2 = scipy.integrate.dblquad(lambda x,y: self.holder(x,y), self.char_func.start[1]+float(1/epsilon), np.inf , self.char_func.start[0]+float(1/epsilon), np.inf)[0]
        
        #I_1 = scipy.integrate.dblquad(lambda x,y: self.holder(x,y), self.char_func.start[1]-epsilon, self.char_func.start[1]-float(1/epsilon),  self.char_func.start[0]-epsilon, self.char_func.start[0]-float(1/epsilon))[0]
        #I_2 = scipy.integrate.dblquad(lambda x,y: self.holder(x,y), self.char_func.start[1]+float(1/epsilon), self.char_func.start[1]+epsilon,  self.char_func.start[0]+float(1/epsilon), self.char_func.start[0]+epsilon)[0]

        I = scipy.integrate.dblquad(lambda r,theta: self.holder(r,theta), 0, 2*np.pi, float(1/epsilon), np.inf)[0]
        print("Integral evals to: " + str(I))
        return I

    def holder(self, r, theta):
        #print("point is " + str((r, theta)))
        #vector_x = self.char_func.start[0]-x
        #vector_y = self.char_func.start[1]-y
        #    vector_x = self.char_func.start[0]-(x*cos(y))
        #vector_y = self.char_func.start[1]-(x*sin(y))

        x_2 = self.char_func.start[0]+(r*cos(theta))
        y_2 = self.char_func.start[1]+(r*sin(theta))

            
        #x_1 = (x*cos(y))
        #y_1 = (x*sin(y))

        #norm = math.sqrt(vector_x**2 + vector_y**2)
        #working code
        return float(1/2)*(float(self.eval_char_func(self.char_func.start,(x_2, y_2))/r**(1+float(1/2))))
        #return float(1/2)*(self.eval_char_func((0,0),(r, theta))/r**(1+float(1/2)))
