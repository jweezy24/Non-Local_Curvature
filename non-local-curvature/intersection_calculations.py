import math
import time
import random
import sympy as sp
import numpy as np
import intersection_algorithms as inter
from shapely.geometry import LineString
from shapely.geometry import Point
from scipy.optimize import fsolve
from numba import jit, njit, prange, generated_jit


class insideness:

    def __init__(self, func_x, func_y, radius=0, origin=[0,0], points=[],bounds=[]):
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
        self.bounds = bounds
        #self.circle = LineString(points)

    def test_nums(self,point):
        f_x = lambda t: eval(self.func_x)
        f_y = lambda t: eval(self.func_y)
        value = (f_x(point[0]), f_y(point[1]))
        return value

    def point_insideness(self, start, point, alg):
        winding_number = 0
        intersections = 0

        if alg == "bounding_box":
            for p in self.domain:
                if type(intersections) == type(None):
                    holder = 0
                else:
                    holder = intersections
                intersections = inter.bounding_box_algorithm(tuple(p), point, holder, tuple(self.bounds))
            
            return self.bounding_box_algorithm_check(intersections,point)

        elif alg == "winding_number":
            for p in self.domain:
                holder = winding_number
                winding_number = inter.winding_num(point, tuple(p), holder, tuple(self.bounds))

            return self.winding_number_check(winding_number, point)

        elif alg == "crossing_number":
            cn = 0
            for p in self.domain:
                cn = inter.crossing_number(tuple(p), point, cn)
            
            if cn%2 == 1:
                return True
            else:
                return False


    def winding_number_check(self, winding_number,point):
        winding_number = (1/(2*np.pi))*winding_number
        #WINDING NUMBER CASES
        if float(winding_number) >= .99999999:
            #self.debug_point(point,False, f'Winding Number Value:{winding_number} Point:{point} Greater than one but outside circle')
            return True
        else:
            #self.debug_point(point,True, f'Winding Number Value:{winding_number} Point:{point} Less than one but inside cirlce')
            return False

    def ray_casting_alg_check(self, intersections,point):
         #RAY CASTING CASES
        if intersections%2 == 1:
            #self.debug_point(point,False, f'Intersections:{intersections} Point:{point} Should be outside')
            return True
        else:
            #self.debug_point(point,True, f'Intersections:{intersections} Point:{point} Should be inside')
            return False


    def bounding_box_algorithm_check(self, intersections, point):
        if type(intersections) != type(None) and intersections == 0:
            #self.debug_point(point,False, f'Intersections:{intersections} Point:{point} Should be outside')
            return True
        else:
            #self.debug_point(point,True, f'Intersections:{intersections} Point:{point} Should be inside')
            return False


    def debug_point(self, point, expected_bool, log_message):
        if expected_bool:
            statement = point[0]**2 + point[1]**2 <= self.radius**2
        else:
            statement = point[0]**2 + point[1]**2 > self.radius**2

        if statement:
            print(log_message)




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
