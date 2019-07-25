import numpy as np
import sympy
from shapely.geometry import LineString
from shapely.geometry import Point
from scipy.optimize import fsolve
import math
import time

class winder:

    def __init__(self, func_x, func_y, radius=0):
        self.func_x = func_x
        self.func_y = func_y
        self.line_holder = None
        self.first_line = None
        self.first_line_mag = 0
        self.turns = 0
        self.range = []
        self.radius = radius
        origin = Point(0, 0)
        self.circle = origin.buffer(self.radius).boundary


    def test_nums(self,point):
        f_x = lambda t: eval(self.func_x)
        f_y = lambda t: eval(self.func_y)
        value = f_x(point[0]) + f_y(point[1])
        return value

    def calculate(self, start, point):
        vector = ((start[0] - point[0]), (start[1] - point[1]))
        line = [point, vector]
        
        x_1 = vector[0]
        y_1 = vector[1]

        slope = (y_1/x_1)
        

        f = lambda x: slope*(x - point[0]) + point[1]
        #f1_y = lambda x: 

        l = LineString([(self.radius,f(self.radius)),(-self.radius,f(-self.radius)) ])

        i = self.circle.intersection(l)
        l2 = None
        if str(type(i)) == "<class 'shapely.geometry.multipoint.MultiPoint'>":
            l2 = LineString(i)
        elif str(type(i)) == "<class 'shapely.geometry.collection.GeometryCollection'>":
            print(point)
            print(i)
            return False
        elif str(type(i)) == "<class 'shapely.geometry.linestring.LineString'>":
            l2 = i
        else:
            return False

        l2 = LineString(i)

        if l2.contains(Point(point)):
            point_count = 0
            for p in i:
                point_count+=1
            if point_count > 0 and point_count%2 == 0:
                return True
            else:
                return False
        else:
            return False





if __name__ == "__main__":

    wind = winder("2*np.cos(t)", "2*np.sin(t)", radius=2)
    print(wind.calculate((2,0),(0,7)))
