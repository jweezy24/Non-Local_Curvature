import scipy
import numpy
import sympy
import area_sets as area

class chi:

    def __init__(self, args):

        self.radius = args["curv"]["radius"]
        self.func = args["curv"]["func"]
        self.is_circle = args["curv"]["circle"]
        self.area_sets = area.A(self.radius, self.func)

    def check(self, p1, p2):
        if self.is_circle:
            return self.area_sets.which_set_circle(p2)
