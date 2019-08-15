import math
import time
import sympy as sp
import numpy
import minpy.numpy as np
import mxnet
from mxnet.gluon import nn
from minpy.context import cpu, gpu
from shapely.geometry import LineString
from shapely.geometry import Point
from scipy.optimize import fsolve
from numba import vectorize
from numba import jit, njit, prange, generated_jit


@njit(parallel = True)
def sumation(p,domain):
    total = 0
    for pos in range(0,len(domain)):
        if pos < len(domain)-1:
            point_1 = domain[pos]
            point_2 = domain[pos+1]
            vector_diff_1 = (point_1[0] - p[0], point_1[1]- p[1])
            vector_diff_2 = (point_2[0] - p[0], point_2[1]- p[1])
            dot_prod = vector_diff_1[0]*vector_diff_2[0] + vector_diff_1[1]*vector_diff_2[1]
            vector_length_1 = math.sqrt(vector_diff_1[0]**2 + vector_diff_1[1]**2)
            vector_length_2 = math.sqrt(vector_diff_2[0]**2 + vector_diff_2[1]**2)
            denom = vector_length_1*vector_length_2
            value = float(dot_prod/denom)
            calculation = numpy.arccos(value)
            total += calculation
    return total

class winder:

    def __init__(self, func_x, func_y, radius=0, origin=[0,0], points=[]):
        self.func_x = func_x
        self.func_y = func_y
        self.line_holder = None
        self.first_line = None
        self.first_line_mag = 0
        self.turns = 0
        self.range = []
        self.radius = radius
        self.origin = Point(origin[0], origin[1])
        self.origin_list = origin
        self.domain = points
        self.circle = LineString(points)


    def test_nums(self,point):
        f_x = lambda t: eval(self.func_x)
        f_y = lambda t: eval(self.func_y)
        value = (f_x(point[0]), f_y(point[1]))
        return value

    def calculate(self, start, point):
        vector = ((start[0] - point[0]), (start[1] - point[1]))
        line = [point, vector]

        atol_temp= 10**-11
        rtol_temp= 10**-11

        atol_temp_point= 10**-11
        rtol_temp_point= 10**-11
        
        x_direction = vector[0]/vector[0]
        y_direction = vector[1]/vector[1]

        winding_number = self.angle_summation_method(point, False)
        if  winding_number >= 1:
            self.debug_point(point,False, f'Winding_number:{winding_number} Point:{point} point is not apart of the circle.')
            return True
        else:
            self.debug_point(point,True, f'Winding_number:{winding_number} Point:{point} point is apart of the circle.')
            return False


    def debug_point(self, point, expected_bool, log_message):
        if expected_bool:
            statement = point[0]**2 + point[1]**2 <= self.radius**2
        else:
            statement = point[0]**2 + point[1]**2 > self.radius**2

        if statement:
            print(log_message)


    def angle_summation_method(self, p, if_gpu):
        constant = 1/(2*np.pi)
        total = 0.0
        if if_gpu:
            with gpu(0):
                total = sumation(p,tuple(self.domain))
        else:
            for pos in range(0,len(self.domain)):
                    if pos < len(self.domain)-1:
                        point_1 = self.domain[pos]
                        point_2 = self.domain[pos+1]
                        vector_diff_1 = (point_1[0] - p[0], point_1[1]- p[1])
                        vector_diff_2 = (point_2[0] - p[0], point_2[1]- p[1])
                        dot_prod = vector_diff_1[0]*vector_diff_2[0] + vector_diff_1[1]*vector_diff_2[1]
                        vector_length_1 = math.sqrt(vector_diff_1[0]**2 + vector_diff_1[1]**2)
                        vector_length_2 = math.sqrt(vector_diff_2[0]**2 + vector_diff_2[1]**2)
                        denom = vector_length_1*vector_length_2
                        value = dot_prod/denom
                        calculation = numpy.arccos(value)
                        total += calculation
        return constant*total




def create_domain(func_x, func_y):
        x_eval = lambda t: eval(func_x)
        y_eval = lambda t: eval(func_y)
        points = []
        for angle in range(0,361):
            points.append((x_eval((angle*np.pi)/180),y_eval((angle*np.pi)/180)))
        return points


if __name__ == "__main__":

    domain = create_domain("2*np.cos(t)", "2*np.sin(t)")

    wind = winder("2*np.cos(t)", "2*np.sin(t)", radius=2, points=domain)
    print(wind.angle_summation_method((-1,0),True))
