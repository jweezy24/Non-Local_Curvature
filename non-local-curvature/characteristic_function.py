import scipy.constants
import math
import numpy as np
import intersection_calculations
import random
#For testing domain generation
#import matplotlib.pyplot as plt

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
        self.start = args["curv"]["start_point"]
        self.origin= args["curv"]["origin"]
        self.alg = args["curv"]["alg"]
        self.equ = args["curv"]["equation"]
        self.isHem = args["curv"]["is_hemisphere"]
        self.domain_size = n
        self.domain, self.domain_full = self.create_domain(n,random)
        #self.domain = [[(0,0), (0,1), (1,0), (0,0)]]
        self.area_sets = intersection_calculations.insideness(self.func_x, self.func_y, radius=self.radius, origin=self.origin, 
        points= self.domain, bounds=self.bounds)

    def check(self, p1, p2):
        #print("Points given P1: " + str(p1) + "\t P2:" + str(p2))
        return self.area_sets.point_insideness(p1, p2, self.alg)

    def create_domain(self, n,random_check):
        x_eval = lambda t: eval(self.func_x)
        y_eval = lambda t: eval(self.func_y)

        domain = []
        # domain.add((x_eval(0),y_eval(0),0))
        # domain.add((x_eval(np.pi),y_eval(np.pi), np.pi))
        # domain.add((x_eval(np.pi/2),y_eval(np.pi/2), np.pi/2))
        # domain.add((x_eval((3*np.pi)/2),y_eval((3*np.pi)/2), (3*np.pi/2)))
        domain2 = []

        if random_check:
            for angle in range(1,n+1):
                p_1 = ((angle*2*np.pi*random.random())/n) + (2*np.pi/n)
                p_1_ref = p_1
                if p_1_ref > 2*np.pi:
                    p_1_ref = p_1/(2*np.pi)
                point_holder = (x_eval(p_1),y_eval(p_1),p_1_ref)
                self.min_max(point_holder)
                domain.append(point_holder)
        else:
            if self.isHem:
                for angle in range(0,n+1):
                    if angle != 0 and angle != n:
                        p_1 = ((angle*np.pi)/(n+1))
                    elif angle == n:
                        p_1 = np.pi
                    else:
                        p_1 = 0
                        p_1_ref = 0
                    point_holder = (x_eval(p_1),y_eval(p_1),p_1)
                    self.min_max(point_holder)
                    domain.append(point_holder)
                #print(domain)
            
                
            else:
                for angle in range(0,n+1):
                    if angle != 0 and angle != n:
                        p_1 = ((angle*2*np.pi)/n)
                    elif angle == n:
                        p_1 = 2*np.pi
                    else:
                        p_1 = 0
                        p_1_ref = 0
                
                    point_holder = (x_eval(p_1),y_eval(p_1),p_1)
                    self.min_max(point_holder)
                    domain.append(point_holder)
                
    
        domain_sorted = domain
        #print(domain_sorted)
        
        #****uniform spacing rectangular gird****
        
        if self.isHem:
            line1, line2 = self.grow_set(self.start, domain[0], domain[-1])
            front_start = domain[0][0]
            back_start = domain[-1][0]
            for i in range(1,n, int(n/6)):
                front = (float(front_start+i),eval(line1.replace('x',str(front_start+i))),float(front_start+i))
                self.min_max(front)
                domain_sorted.insert(0, front)
            
            for i in range(1, n, int(n/6)):
                back = (float((back_start-i)),eval(line2.replace('x',str((back_start-i)))),float((back_start-i)))
                self.min_max(back)
                domain_sorted.append(back)
            

            # front = (float(domain[0][0]+n+2),eval(line1.replace('x',str(domain[0][0]+n+2))),float(domain[0][0]+n+2))
            # self.min_max(front)
            # domain_sorted.insert(0, front)
            
            # back = (float(-(n+2)),eval(line2.replace('x',str(-(n+2)))),float(-(n+2)))
            # self.min_max(back)
            # domain_sorted.append(back)

        #Code to demonstrate domain creation
        # xs = []
        # ys = []
        # for point in domain_sorted:
        #     xs.append(point[0])
        #     ys.append(point[1])
            
        # plt.plot(xs,ys)
        # plt.show()

        count = 0
        points = []
        for point in domain_sorted:
            last_point = (point[0],point[1])
            points.append((point[0],point[1]))
            count+=1
            if count >= 997:
                domain2.append(points)
                points = []
                count = 0
                points.append(last_point)

        if len(points) > 0:
            domain2.append(points)
        
        if not self.isHem:
            domain2[-1].append((domain_sorted[0][0], domain_sorted[0][1]))
        
        # #Code to demonstrate domain creation
        # xs = []
        # ys = []
        # for point in domain_sorted:
        #     xs.append(point[0])
        #     ys.append(point[1])
            
        # plt.plot(xs,ys)
        # plt.show() 

        return domain2,domain_sorted

    def grow_set(self, start_point, end1, end2):
        slope_l1 = (end1[1]-start_point[1])/(end1[0]-start_point[0])
        slope_l2 = (end2[1]-start_point[1])/(end2[0]-start_point[0])
        #Change this to be open ended
        line_eq1 = f"{slope_l1}*x + 2"
        line_eq2 = f"{slope_l2}*x + 2"
        return (line_eq1, line_eq2)

    def min_max(self,gen_point):
        if type(self.bounds[0]) == type('t') or self.bounds[0] < gen_point[0]:
            x_min = gen_point[0]
            self.bounds[0] = gen_point[0]
        if type(self.bounds[1]) == type('t') or self.bounds[1] < gen_point[1]:
            y_min = gen_point[1]
            self.bounds[1] = gen_point[1]
        if type(self.bounds[2]) == type('t') or self.bounds[2] > gen_point[0]:
            x_max = gen_point[0]
            self.bounds[2] = gen_point[0]
        if type(self.bounds[3]) == type('t') or self.bounds[3] > gen_point[1]:
            y_max = gen_point[1]
            self.bounds[3] = gen_point[1]

