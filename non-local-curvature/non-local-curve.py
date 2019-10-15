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
        n = 360*i
        if not random:
            char_func = chi.chi(par.args,n)
        else:
            char_func = chi.chi(par.args,n,random)
        print(random)
        eval.Eval(char_func,random)


if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('--random', help="Using random points or not.")
    args = parser.parse_args()
    if args.random:
        main(random=True)
    else:
        main()
    
