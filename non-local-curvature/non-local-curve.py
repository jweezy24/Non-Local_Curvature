import scipy
import numpy
import sympy
import parser_west  as parser_yam
import characteristic_function as chi
import nonLocalCurveEval as eval
import argparse

def main(random=False):
    par = parser_yam.parser(file_path="../config.yaml")
    for i in range(1,100):
        n = 100*i
        if not random:
            char_func = chi.chi(par.args,n)
        else:
            char_func = chi.chi(par.args,n,random)
        print(random)
        eval.Eval(char_func,random)

def main_2(random=False):
    par = parser_yam.parser(file_path="../config.yaml")
    n = 100
    for i in range(0, 101):
        if not random:
            if i == 0:
                char_func = chi.chi(par.args,n)
            else:
                par.args["curv"]["func_x"] = par.args["curv"]["func_x"].replace("/2", f"/(2 - ({i}/100))")
                char_func = chi.chi(par.args,n)
                par.args["curv"]["func_x"] = par.args["curv"]["func_x"].replace(f"/(2 - ({i}/100))", f"/2")
        else:
            char_func = chi.chi(par.args,n,random)
        eval.Eval(char_func,random, default=False, iter=f"({i}/100)")


if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('--random', help="Using random points or not.")
    parser.add_argument('--setting', help="Which type of test to run.")
    args = parser.parse_args()
    print(args.setting)
    if args.random and args.setting == 0:
        main(random=True)
    elif not args.random and args.setting == 0:
        main()
    elif args.random and not args.setting == 1:
        main_2(random=True)
    elif not args.random and not args.setting == 1:
        main_2()
    
