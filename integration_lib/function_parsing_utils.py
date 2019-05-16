import parser
import sys
from numpy import sqrt, sin, cos, pi

def variable_parser(args):
    checker = False
    vars = []
    if type(args) != type(''):
        args = args["args"]["function"]

    for i in args:
        if ord(i) >= 97 and ord(i) <= 122:
            checker = False
            if i == 'x' or i == 'y':
                checker = True

            if checker:
                if i not in vars:
                    vars.append(i)
        else:
            continue

    return vars

def range_parse(range):
    tmp_holder = range.split(",")
    x_domains = []
    y_domains = []
    for i in tmp_holder:
        print(tmp_holder)
        tmp2 = i.split('<=')
        if tmp2[1] == 'x':
            tmp2.remove('x')
            x_domains = tmp2

        if tmp2[1] == 'y':
            tmp2.remove('y')
            y_domains = tmp2

    return [x_domains, y_domains]

if __name__ == '__main__':
    print(range_parse("0 <= y <= 3, y**float(1/3) <= x <= 2"))
