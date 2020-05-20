import intersection_algorithms as bb
import matplotlib.pyplot as plt
import characteristic_function as chi
import parser_west  as parser_yam
import os,sys
import random


class context_stuff:
    def __init__(self):
        self.par = parser_yam.parser(file_path="../config.yaml")
        self.char_func = chi.chi(self.par.args,30)
        self.point_count = 0
        self.x_points = []
        self.y_points = []
        self.domain_to_test = []
        #self.char_func.bounds = [0,0,1,1]
        #self.char_func.domain = [[(0,0), (0,1), (1,0), (0,0)]]
        #self.char_func.domain_full = [(0,0), (0,1), (1,0), (0,0)]

    def create_domain(self):
        end = (self.char_func.bounds[0]-2,self.char_func.bounds[1]-2)
        start = (self.char_func.bounds[2],self.char_func.bounds[3])
        for i in range(0, 200):
            y = ((start[1])/200) * i + (end[1]/200)*(200-i)
            for j in range(0, 30):
                x = ((start[0])/30)  * j + (end[0]/30)*(30-j)
                val = self.char_func.check((0,0),(x,y))
                #print(f"({x},{y})")
                if val:
                    plt.plot(x,y, 'bo')
                else:
                    plt.plot(x,y, 'rx')
                        
        print(self.char_func.domain_full)
        xs = []
        ys = []
        for point in self.char_func.domain_full:
            xs.append(point[0])
            ys.append(point[1])
            
        plt.plot(xs,ys)
        self.point_count = 0



def main():
    obj = context_stuff()
    obj.create_domain()
    plt.show() 


main()

