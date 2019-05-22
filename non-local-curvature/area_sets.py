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

        if (point[0]**2 + point[1]**2) > self.radius:
            return True
        elif (point[0]**2 + point[1]**2) < self.radius:
            return True
        else:
            return False
