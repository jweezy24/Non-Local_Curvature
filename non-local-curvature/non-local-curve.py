import scipy
import numpy
import sympy
import parser_west  as parser_yam
import characteristic_function as chi
import nonLocalCurveEval as eval
import argparse

''' 
First experiment:
    This Code was designed for testing the accuracy of the algorithms'''
def main(random=False):
    par = parser_yam.parser(file_path="../config.yaml")
    
    for i in range(1,100):
        n = 1000*i
        if not random:
            char_func = chi.chi(par.args,n)
        else:
            char_func = chi.chi(par.args,n,random)
        print(random)
        eval.Eval(char_func,random)
'''
Second Experiment:
    This experiment was designed for testing the relation of the start point to the curvature of an ellipse
'''
def main_2(random=False):
    par = parser_yam.parser(file_path="../config.yaml")
    n = 1000
    for i in range(0, 101):
        if not random:
            if i == 0:
                char_func = chi.chi(par.args,n)
            else:
                par.args["curv"]["func_x"] = par.args["curv"]["func_x"].replace("4*", f"(4- ({i}/50))*")
                char_func = chi.chi(par.args,n)
                par.args["curv"]["func_x"] = par.args["curv"]["func_x"].replace( f"(4- ({i}/50))*", "4*")
        else:
            char_func = chi.chi(par.args,n,random)
        eval.Eval(char_func,random, default=False, iter=f"({i}/100)")

'''
Third Experiment:
    This experiement tests semicircle  
'''
def main_3(random=False):
    par = parser_yam.parser(file_path="../config.yaml")
    n = 1000
    for i in range(1, 100):
        char_func = chi.chi(par.args,n*i)
        eval.Eval(char_func,random,default=False)


if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('--setting', help="Which type of test to run.")
    args = parser.parse_args()
    print(type(args.setting))
    if args.setting == '0':
        main()
    elif args.setting == '1':
        main_2()
    elif args.setting == '2':
        main_3()
    
