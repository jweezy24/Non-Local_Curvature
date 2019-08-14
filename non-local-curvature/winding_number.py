import numpy as np
import sympy
from shapely.geometry import LineString
from shapely.geometry import Point
from scipy.optimize import fsolve
import math
import time

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

        atol_temp_point= 10**-4
        rtol_temp_point= 10**-4
        
        x_direction = vector[0]/vector[0]
        y_direction = vector[1]/vector[1]

        # slope = (y_1/x_1)

        # angle = np.arctan(slope)

        #f = lambda x: slope*(x - point[0]) + point[1]
        
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
                    if np.isclose(list_of_points[intsec_p].coords[0][0], start[0],rtol=rtol_temp, atol=atol_temp) and np.isclose(list_of_points[intsec_p].coords[0][1], start[1], rtol=rtol_temp, atol=atol_temp):
                        intersections -= 1
                        start_count += 1
                    elif np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point) and np.isclose(list_of_points[intsec_p].coords[0][1], point[1], rtol=rtol_temp_point, atol=atol_temp_point):
                        intersections -= 1
                    elif (intsec_p < len(list_of_points)-1 
                    and np.isclose(abs(list_of_points[intsec_p].coords[0][0]-list_of_points[intsec_p+1].coords[0][0]), 0,rtol=rtol_temp_point, atol=atol_temp_point) 
                    and np.isclose(abs(list_of_points[intsec_p].coords[0][1]-list_of_points[intsec_p+1].coords[0][1]), 0, rtol=rtol_temp_point, atol=atol_temp_point)):
                        intersections -= 1

            if start_count > 1 and len(list_of_points) == 2 and intersections == 0:
                return False
            elif (point[1] > start[1] and 
            not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
            and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
            and intersections%2 == 0
            and intersections != 0):
                #self.debug_point(point,False, f' Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections above line')
                return True
            elif (point[1] < start[1] and 
            not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
            and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
            and intersections%2 == 0):
                #self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections below line')
                return False
            elif (point[1] > start[1] and 
            not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
            and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
            and intersections%2 == 1):
                #self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections above line')
                return False
            elif (point[1] < start[1] and 
            not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
            and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
            and intersections%2 == 1):
                #self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections below line')
                return True
            else:
                return None

        elif str(type(i)) == "<class 'shapely.geometry.linestring.LineString'>":
            #self.debug_point(point,True, f'False. Intersection:{i} Point:{point} Line is wrong')
            return False
        elif str(type(i)) == "<class 'shapely.geometry.point.Point'>":
            intersections = 1

            if np.isclose(i.coords[0][0], start[0],rtol=rtol_temp, atol=atol_temp) and np.isclose(i.coords[0][1], start[1], rtol=rtol_temp, atol=atol_temp):
                intersections -= 1
                return None

            if point[1] > start[1] and intersections%2 == 0:
                #self.debug_point(point,False, f' Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections above line')
                return True
            elif point[1] < start[1] and intersections%2 == 0:
                #self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections below line')
                return False
            elif point[1] > start[1] and intersections%2 == 1:
                #self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections above line')
                return False
            elif point[1] <  start[1] and intersections%2 == 1:
                #self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections below line')
                return True
    
        elif str(type(i)) == "<class 'shapely.geometry.collection.GeometryCollection'>":
            ##self.debug_point(point,True, f'False. Intersection:{i} Point:{point} point missed by shapelys intersections.')
            if point[1] > start[1]:
                return True
            elif point[1] <= start[1]:
                return False
        else:
            #self.debug_point(point,True, f'False. Intersection:{i} Point:{point} type:{str(type(i))} Geometry object not accounted for')
            return None

    def debug_point(self, point, expected_bool, log_message):
        if expected_bool:
            statement = point[0]**2 + point[1]**2 <= self.radius**2
        else:
            statement = point[0]**2 + point[1]**2 > self.radius**2

        if statement:
            print(log_message)





if __name__ == "__main__":

    wind = winder("2*np.cos(t)", "2*np.sin(t)", radius=2)
    print(wind.calculate((0,-2), [2.1,0]))
