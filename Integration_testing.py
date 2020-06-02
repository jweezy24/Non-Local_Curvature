import sys
import os
from scipy import integrate
import math


def root_x(x):
    return 1/pow(x,(1/2))


def test():

    for i in range(1,100):
        epsilon = 1/pow(10,i)
        result = str(integrate.quad(root_x, epsilon, 1))
        with open("integral_test_results.txt","a") as f:
            f.write(f"{result}\n")
        print(result)


def main():
    test()

main()