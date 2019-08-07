import scipy
import numpy as np
import sympy
import winding_number

class A:

    def __init__(self, radius, func_x, func_y, origin=[0,0]):
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
        self.calc = winding_number.winder(self.func_x,self.func_y, self.radius, origin)

    #if the domain is a circle
    def which_set_circle(self, point, point2):
        #print("Point checked: " + str(point))
        #calc = winding_number.winder(self.func, self.radius)
        return self.calc.calculate(point, point2)

        # if (point[0]**2 + (point[1])**2) > self.radius**2:
        #     return True
        # elif (point[0]**2 + (point[1])**2) < self.radius**2:
        #     return False
        # else:
        #     return False
