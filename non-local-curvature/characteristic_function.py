import scipy.constants
import math
import numpy as np
import area_sets as area
import random

class chi:

    def __init__(self, args,n,random=False):

        x_min = 't'
        y_min = 't'
        x_max = 't'
        y_max = 't'
        self.bounds = [x_min,y_min,x_max,y_max]

        self.radius = args["curv"]["radius"]
        self.func_x = args["curv"]["func_x"]
        self.func_y = args["curv"]["func_y"]
        self.is_circle = args["curv"]["circle"]
        self.start = args["curv"]["start_point"]
        self.domain_size = n
        self.domain = self.create_domain(n,random)

        if self.is_circle:
            self.origin = args["curv"]["origin"]
        if self.is_circle:
            self.area_sets = area.A(self.radius, self.func_x, self.func_y, self.origin, self.domain, self.bounds)
        else:
            return

    def check(self, p1, p2):
        #print("Points given P1: " + str(p1) + "\t P2:" + str(p2))
        if self.is_circle:
            return self.area_sets.which_set_circle(p1, p2)

    def create_domain(self, n,random_check):
        x_eval = lambda t: eval(self.func_x)
        y_eval = lambda t: eval(self.func_y)

        domain = set()
        domain.add((x_eval(0),y_eval(0)))
        domain.add((x_eval(np.pi),y_eval(np.pi)))
        domain.add((x_eval(np.pi/2),y_eval(np.pi/2)))
        domain.add((x_eval((3*np.pi)/2),y_eval((3*np.pi)/2)))
        domain2 = []

        if random_check:
            for angle in range(1,n+1):
                p_1 = (angle*2*np.pi*random.random()/n) + (angle/n)
                point_holder = (x_eval(p_1),y_eval(p_1),p_1)
                self.min_max(point_holder)
                domain.add(point_holder)
        else:
            for angle in range(1,n+1):
                p_1 = (angle*2*np.pi/n) + (angle/n)
                point_holder = (x_eval(p_1),y_eval(p_1),p_1)
                self.min_max(point_holder)
                domain.add(point_holder)
    
    
        domain_sorted = sorted(domain, key=lambda tup: tup[1])

        count = 0
        points = []
        for point in domain_sorted:
            points.append((point[0],point[1]))
            count+=1
            if count >= 998:
                domain2.append(points)
                points = []
                count = 0
        return domain2

    def min_max(self,gen_point):
        if type(self.bounds[0]) == type('t') or self.bounds[0] < gen_point[0]:
            x_min = gen_point[0]
            self.bounds[0] = gen_point[0]
        elif type(self.bounds[1]) == type('t') or self.bounds[1] < gen_point[1]:
            y_min = gen_point[1]
            self.bounds[1] = gen_point[1]
        elif type(self.bounds[2]) == type('t') or self.bounds[2] > gen_point[0]:
            x_max = gen_point[0]
            self.bounds[2] = gen_point[0]
        elif type(self.bounds[3]) == type('t') or self.bounds[3] > gen_point[1]:
            y_max = gen_point[1]
            self.bounds[3] = gen_point[1]

