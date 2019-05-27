import scipy
import numpy as np
import sympy

class A:

    def __init__(self, radius, func):
        #True
        self.is_closed = True
        self.A_e = []
        self.A_i = []
        #default orientation
        self.is_clockwise = True
        #orientation is outward by default
        self.orientation = True

        #grabs the domian defined by the user
        self.radius = radius
        self.func = func

    #if the domain is a circle
    def which_set_circle(self, point):
        #print("Point checked: " + str(point))
        if (point[0]**2 + (point[1]-2)**2) > self.radius**2:
            return True
        elif (point[0]**2 + (point[1]-2)**2) < self.radius**2:
            return False
        else:
            return False
