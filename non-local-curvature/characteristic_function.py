import scipy
import sympy
import numpy as np
from shapely.geometry import Point
import area_sets as area

class chi:

    def __init__(self, args):

        self.radius = args["curv"]["radius"]
        self.func_x = args["curv"]["func_x"]
        self.func_y = args["curv"]["func_y"]
        self.is_circle = args["curv"]["circle"]
        self.start = args["curv"]["start_point"]
        self.domain = self.create_domain()
        if self.is_circle:
            self.origin = args["curv"]["origin"]
        if self.is_circle:
            self.area_sets = area.A(self.radius, self.func_x, self.func_y, self.origin, self.domain)
        else:
            return

    def check(self, p1, p2):
        #print("Points given P1: " + str(p1) + "\t P2:" + str(p2))
        if self.is_circle:
            return self.area_sets.which_set_circle(p1, p2)

    def create_domain(self):
        x_eval = lambda t: eval(self.func_x)
        y_eval = lambda t: eval(self.func_y)
        points = []
        for angle in range(0,3608):
            points.append((x_eval((angle*np.pi)/180),y_eval((angle*np.pi)/180)))
        return points

