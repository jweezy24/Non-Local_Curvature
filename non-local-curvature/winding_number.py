from scipy.optimize import fsolve
import numpy as np
import sympy
import math

class winder:

    def __init__(self, func_x, func_y, radius=0):
        self.func_x = func_x
        self.func_y = func_y
        self.line_holder = None
        self.first_line = None
        self.first_line_mag = 0
        self.turns = 0
        self.range = []

        self.make_range(radius)


    def test_nums(self,point):
        f = lambda x,y: eval(self.func)
        val = f(point[0],point[1])
        return val
    def calculate(self, point):
        angle1 = 0
        start = True
        flip = False
        negative = False
        for x,y in self.range:
            func_point = (x, y)
            vector = ((x - point[0]), (y - point[1]))
            line = [point, vector]
            #magnitude of the vector
            r = np.sqrt((func_point[0] - point[0])**2  + (func_point[1] - point[1])**2)
            if not self.line_compare(line):
                flip = True
            elif start:
                start = False
                self.first_line = line
                self.first_line_mag = r
                continue
            elif self.first_line and line:
                angles = self.angle_between(self.first_line, line)
                self.first_line = line
                if not math.isnan(angles):
                    #print(angles * (180.0/np.pi))
                    angle1 += angles * (180.0/np.pi)
                print(angle1)
            if angle1 >= 360:
                self.turns = 1
        return self.turns


    def line_compare(self, line):
        if not self.line_holder:
            self.line_holder = line
            return True
        elif line[0] != self.line_holder[0] or line[1] != self.line_holder[1]:
            self.line_holder = line
            return True
        else:
            return False

    def angle_between(self, line1, line2):
        dot_prod = line1[1][0]*line2[1][0] + line1[1][1]*line2[1][1]
        denom = math.sqrt(line1[1][0]**2 + line1[1][1]**2) * math.sqrt(line2[1][0]**2 + line2[1][1]**2)
        return np.arccos(dot_prod/denom)


    def make_range(self,radius):
        r = radius
        func_x_eval = lambda y: eval(self.func_x)
        func_y_eval = lambda x: eval(self.func_y)
        for i in range(0, 1):
            point_pos = (func_x_eval(r*np.cos((i*np.pi)/180)), func_y_eval(r*np.sin((i*np.pi)/180)))
            point_neg_x = (-func_x_eval(r*np.cos((i*np.pi)/180)), func_y_eval(r*np.sin((i*np.pi)/180)))
            point_neg = (-func_x_eval(r*np.cos((i*np.pi)/180)), -func_y_eval(r*np.sin((i*np.pi)/180)))
            point_neg_y = (func_x_eval(r*np.cos((i*np.pi)/180)), -func_y_eval(r*np.sin((i*np.pi)/180)))
            self.range.append(point_pos)
            self.range.append(point_neg)
            self.range.append(point_neg_x)
            self.range.append(point_neg_y)




if __name__ == "__main__":

    wind = winder("(4 -(y)**2 )**(1/2)", "(4 - (x)**2)**(1/2)", radius=2)
    print(wind.calculate((.2, 0)))
