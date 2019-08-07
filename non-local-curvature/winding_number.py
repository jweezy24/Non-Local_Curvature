import numpy as np
import sympy
from shapely.geometry import LineString
from shapely.geometry import Point
from scipy.optimize import fsolve
import math
import time

class winder:

    def __init__(self, func_x, func_y, radius=0, origin=[0,0]):
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
        self.circle = self.origin.buffer(self.radius).boundary


    def test_nums(self,point):
        f_x = lambda t: eval(self.func_x)
        f_y = lambda t: eval(self.func_y)
        value = (f_x(point[0]), f_y(point[1]))
        return value 

    def calculate(self, start, point):
        vector = ((start[0] - point[0]), (start[1] - point[1]))
        line = [point, vector]

        atol_temp= .000001
        rtol_temp= .0001

        
        x_1 = vector[0]
        x_direction = vector[0]/vector[0]
        y_1 = vector[1]
        y_direction = vector[1]/vector[1]

        slope = (y_1/x_1)

        # angle = np.arctan(slope)

        #f = lambda x: slope*(x - point[0]) + point[1]
        
        l = LineString([(-x_direction*start[0]*2, -y_direction*start[1]*2),(point[0],point[1])])

        i = self.circle.intersection(l)
        l2 = None
        #print( f'Line:{l} intersection:{i}')
        if str(type(i)) == "<class 'shapely.geometry.multipoint.MultiPoint'>":
            # Are there an even number of intersections? save the line to test for later
            if len(list(i))%2 == 0:
                l2 = i
            else:
                for intsec_p in range(0, len(list(i))):
                    # Does the point already exist on the circle? Return True 
                    if np.isclose(list(i)[i].coords[0][0], point[0],rtol=rtol_tmp, atol=atol_temp) and np.isclose(list(i)[i].coords[0][1], point[1], rtol=rtol_tmp, atol=atol_temp):
                        #self.debug_point(point,False, f'Wrong True. Intersection:{i} Point:{point} Coords Close')
                        return True
            l2 = i
        elif str(type(i)) == "<class 'shapely.geometry.linestring.LineString'>":
            l2 = i
        elif str(type(i)) == "<class 'shapely.geometry.point.Point'>":
            #self.debug_point(point,False, f'Wrong True. Intersection:{i} Point:{point} Bad Point.')
            return True
        elif str(type(i)) == "<class 'shapely.geometry.collection.GeometryCollection'>":
            #self.debug_point(point,True, f'Wrong True. Intersection:{i} Point:{point} point missed by shapelys intersections.')
            return False
        else:
            #self.debug_point(point,True, f'False. Intersection:{i} Point:{point} type:{str(type(i))} Geometry object not accounted for')
            return False

        #l2 = LineString(i)
        #print( f'Line2:{l2} intersection:{i}')
        if l2 and l2.contains(Point(point)):
            #self.debug_point(point,False, f'Wrong True. Intersection:{i} Point:{point} Line:{l2}')
            return True
        else:
            #self.debug_point(point,True, f'False. Intersection:{i} Point:{point} Line:{l2}')
            return False

    def debug_point(self, point, expected_bool, log_message):
        if expected_bool:
            statement = point[0]**2 + point[1]**2 <= self.radius**2
        else:
            statement = point[0]**2 + point[1]**2 > self.radius**2

        if statement:
            print(log_message)





if __name__ == "__main__":

    wind = winder("2*np.cos(t)", "2*np.sin(t)", radius=2)
    print(wind.calculate((2,0), [1.821991980118068, -0.8198467884326306]))
