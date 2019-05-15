import ast
import scipy.integrate as inte
from sympy import *
import integration_lib.function as func


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
        I = inte.quad(self.eval_func, range[0], range[1], args=self.func.vars)
        print(I)


    def integrate_region(self):
        change_x = True
        counter = 0
        x = Symbol('x')
        y = Symbol('y')
        for i in self.func.domain:
            if "x" in i.original_str:
                counter += 1

        if counter == len(self.func.domain):
            change_x = False

        if not change_x:
            holder = integrate(self.func.original_str, y)
            print("Integration is " + str(holder))
            str_holder = str(holder)
            newIntegrals = []
            newIntegrals.append( str_holder.replace("y", "(" + self.region["max"].original_str + ")"))
            newIntegrals.append( str_holder.replace("y", "(" + self.region["min"].original_str + ")"))
            int_check = False
            for i in newIntegrals:
                if int_check:
                    tmp_list = list(i)
                    for k in range(0, len(tmp_list)):
                        if tmp_list[k] == '+':
                            tmp_list[k] = '-'
                        elif tmp_list[k] == '-':
                            tmp_list[k] = '+'
                    newIntegrals[newIntegrals.index(i)] = ''.join(tmp_list)
                else:
                    int_check = True
                    continue
            print(newIntegrals)
            newIntegral_str = ' - '.join(newIntegrals)
            print(newIntegral_str)
            new_args = {"args" : {"function" : newIntegral_str, "domain": [self.func.intersections[0], self.func.intersections[1]]}}
            new_func = func.math_function(new_args)
            new_integral = integral(new_func)
            new_integral.integrate_basic([self.func.intersections[0], self.func.intersections[1]])
        else:
            holder = integrate(self.func.original_str, x)
            print("Integration is " + str(holder))
            str_holder = str(holder)
            newIntegrals = []
            newIntegrals.append( str_holder.replace("x", "(" + self.region["max"].original_str + ")"))
            newIntegrals.append( str_holder.replace("x", "(" + self.region["min"].original_str + ")"))
            int_check = False
            for i in newIntegrals:
                if int_check:
                    tmp_list = list(i)
                    for k in range(0, len(tmp_list)):
                        if tmp_list[k] == '+':
                            tmp_list[k] = '-'
                        elif tmp_list[k] == '-':
                            tmp_list[k] = '+'
                    newIntegrals[newIntegrals.index(i)] = ''.join(tmp_list)
                else:
                    int_check = True
                    continue
            print(newIntegrals)
            newIntegral_str = ' - '.join(newIntegrals)
            print(newIntegral_str)
            new_args = {"args" : {"function" : newIntegral_str, "domain": [self.func.intersections[0], self.func.intersections[1]]}}
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
        print(first)
        print(second)
        print(f(2,1))
        if y_bool:
            if first[0] == tmp_func:
                print("1")
                holder = inte.dblquad(lambda x, y: eval(self.func.func) , float(second[0]), float(second[1]),
                lambda y: eval(first[0].replace(" ", "")), lambda y: float(first[1]))
            else:
                print("2")
                holder = inte.dblquad(lambda x, y: eval(self.func.func) , float(second[0]), float(second[1]),
                lambda y: float(first[0]), lambda y: eval(first[1].replace(" ", "")))
        if x_bool:
            if first[0] == tmp_func:
                print("3")
                holder = inte.dblquad(lambda y, x: eval(self.func.func) , float(second[0]), float(second[1]),
                lambda x: eval(first[0]), lambda x: float(first[1]))
            else:
                print("4")
                holder = inte.dblquad(lambda y, x: eval(self.func.func), float(second[0]), float(second[1]),
                lambda x: float(first[0]), lambda x: eval(first[1].replace(" ", "")))


        print(holder)



    def eval_func(self, *arg):
        return self.func.run_func([arg[0]])

    def eval_spec_func(self, func,*arg):
        return func.run_func([arg[0]])

    def region_def(self, funcs):

        i = float((self.func.intersections[0]+self.func.intersections[1])/2)
        dict = {"func": None}
        for j in funcs:
            if not dict["func"]:
                dict["func"] = j
            else:
                if dict["func"].run_func([i]) < j.run_func([i]):
                    dict["func"] = j
        for i in funcs:
            if dict["func"] == i:
                self.region.update({"max" : i})
            else:
                self.region.update({"min" : i})
