import scipy
import numpy as np
import sympy
import winding_number

class A:

    def __init__(self, radius, func_x, func_y):
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
        self.func_x = func_x
        self.func_y = func_y
        self.calc = winding_number.winder(self.func_x,self.func_y, self.radius)

    #if the domain is a circle
    def which_set_circle(self, point):
        #print("Point checked: " + str(point))
        #calc = winding_number.winder(self.func, self.radius)
        if self.calc.calculate(point) != 0:
            return True
        else:
            return False
