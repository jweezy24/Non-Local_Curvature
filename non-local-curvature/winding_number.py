from scipy.optimize import fsolve
import numpy as np
import sympy
import math

class winder:

    def __init__(self, func, radius=0):
        self.func = func
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
        for x,y in self.range:
            func_point = (x, y)
            line = [point, func_point]
            if self.test_nums(func_point) != 4:
                continue
            #magnitude of the vector
            r = np.sqrt((func_point[0] - point[0])**2  + (func_point[1] - point[1])**2)
            if not self.line_compare(line):
                print("HERE")
                flip = True
            elif start:
                start = False
                self.first_line = line
                self.first_line_mag = r
                continue
            elif self.first_line and line:
                angles = self.angle_between(self.first_line, line)
                if not math.isnan(angles):
                    print(angles)
                    angle1 += angles
        print(float(angle1/(1)))
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
        return np.arctan(((line2[1][0]-line1[1][0])/2)/((line2[0][1]-line1[1][1])/2))

    def make_range(self,r):
        func_holder = self.func
        for i in range(0, 361):
            point = ((r)*np.cos((i*np.pi)/180), (r)*np.sin((i*np.pi)/180))
            self.range.append(point)




if __name__ == "__main__":

    wind = winder("x**2 + y**2", radius=2)
    print(wind.calculate((0,6)))
