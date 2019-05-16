import ast
import scipy.integrate as inte
from sympy import *
import integration_lib.function as func
from numpy import sqrt, sin, cos, pi


class integral:

    def __init__(self, function):

        self.func = function
        check = False
        #checks to see which are functions and which are static ranges
        if function.domain:
            for i in function.domain:
                if type(i) == type(self.func):
                    check = True
                else:
                    check = False
            if check:
                self.region = {}
                self.region_def(self.func.domain)

    def integrate_basic(self, range):
        #print(range)
        if 'x' in self.func.original_str:
            #print(self.func.original_str)
            I = inte.quad(lambda x: eval(self.func.func), range[0], range[1])
        elif 'y' in self.func.original_str:
            #print(self.func.original_str)
            I = inte.quad(lambda y: eval(self.func.func), range[0], range[1])
        print(I)


    def integrate_region(self):
        change_x = True
        counter = 0
        x = Symbol('x')
        y = Symbol('y')
        for i in self.func.domain:
            if "x" in i.original_str:
                change_x = False


        if not change_x:
            holder = integrate(self.func.original_str, y)
            if 'gamma' in str(holder):
                return "integral not solvable with given domain"
            #print("Y integration: " + str(holder))
            str_holder = str(holder)
            newIntegrals = []
            newIntegrals.append( str_holder.replace("y", "(" + self.region["max"].original_str + ")"))
            newIntegrals.append( str_holder.replace("y", "(" + self.region["min"].original_str + ")"))
            int_check = False
            newIntegrals[1] = "(" + newIntegrals[1] + ")"
            #print(newIntegrals)
            newIntegral_str = ' - '.join(newIntegrals)
            #print(newIntegral_str)
            new_args = {"args" : {"function" : newIntegral_str, "functions": [self.func.intersections[0], self.func.intersections[1]]}}
            new_func = func.math_function(new_args)
            new_integral = integral(new_func)
            new_integral.integrate_basic([self.func.intersections[0], self.func.intersections[1]])
        else:
            holder = integrate(self.func.original_str, x)
            #print("Integration is " + str(holder))
            str_holder = str(holder)
            newIntegrals = []
            newIntegrals.append( str_holder.replace("x", "(" + self.region["max"].original_str + ")"))
            newIntegrals.append( str_holder.replace("x", "(" + self.region["min"].original_str + ")"))
            int_check = False
            newIntegrals[1] = "(" + newIntegrals[1] + ")"
            #print(newIntegrals)
            newIntegral_str = ' - '.join(newIntegrals)
            #print("New Integral: " + newIntegral_str)
            new_args = {"args" : {"function" : newIntegral_str, "functions": [self.func.intersections[0], self.func.intersections[1]]}}
            new_func = func.math_function(new_args)
            new_integral = integral(new_func)
            new_integral.integrate_basic([self.func.intersections[0], self.func.intersections[1]])

    def integrate_range(self):
        first = []
        second = []
        for i in self.func.domain_range:
            if 'y' in str(i):
                first = i
            elif 'x' in str(i):
                first = i
            else:
                second = i

        x_bool = False
        y_bool = False
        for i in first:
            if 'x' in i or 'y' in i:
                if 'x' in i: x_bool = True
                if 'y' in i: y_bool = True
                tmp_func = i
        f = (lambda x, y: eval(self.func.original_str))
        if y_bool:
            if first[0] == tmp_func:
                #print("1")
                holder = inte.dblquad(lambda x, y: eval(self.func.func) , float(second[0]), float(second[1]),
                lambda y: eval(first[0].replace(" ", "")), lambda y: float(first[1]))
            else:
                #print("2")
                holder = inte.dblquad(lambda x, y: eval(self.func.func) , float(second[0]), float(second[1]),
                lambda y: float(first[0]), lambda y: eval(first[1].replace(" ", "")))
        if x_bool:
            if first[0] == tmp_func:
                #print("3")
                holder = inte.dblquad(lambda y, x: eval(self.func.func) , float(second[0]), float(second[1]),
                lambda x: eval(first[0]), lambda x: float(first[1]))
            else:
                #print("4")
                holder = inte.dblquad(lambda y, x: eval(self.func.func), float(second[0]), float(second[1]),
                lambda x: float(first[0]), lambda x: eval(first[1].replace(" ", "")))


        #print(holder)



    def eval_func(self, *arg):
        return self.func.run_func([arg[0]])



    def region_def(self, funcs):

        i = float((self.func.intersections[0]+self.func.intersections[1])/2)
        print("bigger_function_check at: " + str(i))
        dict = {"func": None}
        for j in funcs:
            if not dict["func"]:
                dict["func"] = j
            else:
                print("Intersections at: " + str(self.func.intersections)) 
                try:
                    tmp_holder = dict["func"].run_func([i])
                    if tmp_holder:
                        if dict["func"].run_func([i]) < j.run_func([i]):
                            dict["func"] = j
                    else:
                        comp = int(dict["func"].original_str)
                        var = j.run_func([i])
                        if type(comp) != type(var):
                            if comp < var.real:
                                dict["func"] = j
                        else:
                            if comp < var:
                                dict["func"] = j

                except Exception as e:
                    print(e)

        for i in funcs:
            if dict["func"] == i:
                self.region.update({"max" : i})
            else:
                self.region.update({"min" : i})
