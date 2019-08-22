import scipy
import numpy
import sympy
import parser_west  as parser
import characteristic_function as chi
import nonLocalCurveEval as eval

def main():
    par = parser.parser(file_path="../config.yaml")
    n = 100
    for i in range(1,10):
        n = n*i
        char_func = chi.chi(par.args,n)
        eval.Eval(char_func)


if __name__ == "__main__":
    main()
