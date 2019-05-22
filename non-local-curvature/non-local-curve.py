import scipy
import numpy
import sympy
import parser_west  as parser
import characteristic_function as chi
import nonLocalCurveEval as eval

def main():
    par = parser.parser(file_path="../config.yaml")
    char_func = chi.chi(par.args)

    print(eval.Eval(char_func))


if __name__ == "__main__":
    main()
