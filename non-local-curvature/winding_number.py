import math
import time
import random
import sympy as sp
import numpy as np
import instersection_algorithms as inter
from shapely.geometry import LineString
from shapely.geometry import Point
from scipy.optimize import fsolve
from numba import jit, njit, prange, generated_jit


class winder:

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

    def winding_calculate(self, start, point):
        winding_number = 0
        intersections = 0

        for p in self.domain:
            holder = winding_number
            #intersections = inter.ray_casting_alg(tuple(p), point, holder, tuple(self.bounds))
            #intersections = inter.bounding_box_algorithm(tuple(p), point, holder, tuple(self.bounds))
            winding_number = inter.winding_num(point, tuple(p), holder, tuple(self.bounds))

        #intersections = math.floor(intersections/len(self.bounds))

        #return self.ray_casting_alg_check(intersections)
        #return self.bounding_box_algorithm_check(intersections)
        return self.winding_number_check(winding_number, point)


    def intersection_calculate(self, start, point):
        vector = ((start[0] - point[0]), (start[1] - point[1]))
        line = [point, vector]

        atol_temp= 10**-11
        rtol_temp= 10**-11

        atol_temp_point= 10**-11
        rtol_temp_point= 10**-11
        
        x_direction = vector[0]/vector[0]
        y_direction = vector[1]/vector[1]

        l = LineString([(start[0], start[1]),(point[0],point[1])])

        i = self.circle.intersection(l)
        l2 = None
        start_count = 0
        #print( f'Line:{l} intersection:{i}')
        if str(type(i)) == "<class 'shapely.geometry.multipoint.MultiPoint'>":
            # Are there an even number of intersections? save the line to test for later
            intersections = len(list(i))
            list_of_points = list(i)
            for intsec_p in range(0, len(list_of_points)):
                    # Does the point already exist on the circle? Return True 
                    if (np.isclose(list_of_points[intsec_p].coords[0][0], start[0],rtol=rtol_temp, atol=atol_temp) and np.isclose(list_of_points[intsec_p].coords[0][1], start[1], rtol=rtol_temp, atol=atol_temp)):
                        if start_count > 0:
                            intersections -= 2
                        start_count += 1
                    elif np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp, atol=atol_temp) and np.isclose(list_of_points[intsec_p].coords[0][1], point[1], rtol=rtol_temp, atol=atol_temp):
                        self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} point is not apart of the circle.')
                        return True
                    elif (intsec_p < len(list_of_points)-1 
                    and np.isclose(abs(list_of_points[intsec_p].coords[0][0]-list_of_points[intsec_p+1].coords[0][0]), 0,rtol=rtol_temp_point, atol=atol_temp_point) 
                    and np.isclose(abs(list_of_points[intsec_p].coords[0][1]-list_of_points[intsec_p+1].coords[0][1]), 0, rtol=rtol_temp_point, atol=atol_temp_point)):
                        intersections -= 1

            if start_count > 1 and len(list_of_points) == 2 and intersections == 0:
                self.debug_point(point,True, f' Intersection:{i} number of intersections:{intersections} Point:{point} multiple intersections with start but in domain.')
                return False
            elif (point[1] > start[1] and 
            not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
            and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
            and intersections%2 == 0
            and intersections != 0):
                self.debug_point(point,True, f' Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections above line')
                return False
            elif (point[1] < start[1] and 
            not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
            and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
            and intersections%2 == 0):
                self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections below line')
                return True
            elif (point[1] > start[1] and 
            not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
            and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
            and intersections%2 == 1):
                self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections above line but in domain.')
                return True
            elif (point[1] < start[1] and 
            not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
            and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
            and intersections%2 == 1):
                self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections below line')
                return False
            else:
                return None

        elif str(type(i)) == "<class 'shapely.geometry.linestring.LineString'>":
            self.debug_point(point,True, f'False. Intersection:{i} Point:{point} Line is wrong')
            return False
        elif str(type(i)) == "<class 'shapely.geometry.point.Point'>":
            intersections = 1

            if np.isclose(i.coords[0][0], start[0],rtol=rtol_temp, atol=atol_temp) and np.isclose(i.coords[0][1], start[1], rtol=rtol_temp, atol=atol_temp):
                intersections -= 1
                return None

            if point[1] > start[1] and intersections%2 == 0:
                self.debug_point(point,False, f' Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections above line')
                return True
            elif point[1] < start[1] and intersections%2 == 0:
                self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections below line')
                return False
            elif point[1] > start[1] and intersections%2 == 1:
                self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections above line')
                return False
            elif point[1] <  start[1] and intersections%2 == 1:
                self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections below line')
                return True

        elif str(type(i)) == "<class 'shapely.geometry.collection.GeometryCollection'>":
            #self.debug_point(point,True, f'False. Intersection:{i} Point:{point} point missed by shapelys intersections.')
            if point[1] > start[1]:
                return True
            elif point[1] <= start[1]:
                return False
        else:
            self.debug_point(point,True, f'False. Intersection:{i} Point:{point} type:{str(type(i))} Geometry object not accounted for')
            return None

    def winding_number_check(self, winding_number,point):
        winding_number = (1/(2*np.pi))*winding_number
        #WINDING NUMBER CASES
        if winding_number >= .999:
            #self.debug_point(point,False, f'Winding Number Value:{winding_number} Point:{point} Greater than one but outside circle')
            return True
        else:
            #self.debug_point(point,True, f'Winding Number Value:{winding_number} Point:{point} Less than one but inside cirlce')
            return False

    def ray_casting_alg_check(self, intersections):
         #RAY CASTING CASES
        if intersections%2 == 1:
            return True
        else:
            return False
    def bounding_box_algorithm_check(self, intersections):
        if intersections != 0:
            return True
        else:
            return False

    def debug_point(self, point, expected_bool, log_message):
        if expected_bool:
            statement = point[0]**2 + point[1]**2 <= self.radius**2
        else:
            statement = point[0]**2 + point[1]**2 > self.radius**2

        if statement:
            # if random.random() > .9:
            #     with open('./outside_points.txt', 'a') as f_1:
            #         f_1.write(f' {str(point).replace("(", "").replace(")", "")} \n')
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
