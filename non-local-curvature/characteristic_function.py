import scipy
import numpy
import sympy
import area_sets as area

class chi:

    def __init__(self, args):

        self.radius = args["curv"]["radius"]
        self.func_x = args["curv"]["func_x"]
        self.func_y = args["curv"]["func_y"]
        self.is_circle = args["curv"]["circle"]
        self.area_sets = area.A(self.radius, self.func_x, self.func_y)

    def check(self, p1, p2):
        #print("Points given P1: " + str(p1) + "\t P2:" + str(p2))
        if self.is_circle:
            return self.area_sets.which_set_circle(p2)
