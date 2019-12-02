import os
import time
import numpy as np
import intersection_calculations as checker
from numba import jit, njit, prange, generated_jit

os.environ['CUDA_VISIBLE_DEVICES'] = "0"

def integrate(x_func, range2):
    n = 1000000
    delta_x = float((range2[1] - range2[0])/n)
    print(delta_x)
    x_func_eval = lambda t: float(eval(x_func))
    total = 0.0


    if range2[0] == range2[1]:
        return 0


    start_num = float(range2[0])

    for i in range(0,n+1):
        total += float(x_func_eval(start_num+(i*delta_x))) * delta_x
        pass
    return total

def integrate2(func, range_x, range_y):
    n = 10000
    delta_x = float((range_x[1] - range_x[0])/n)
    delta_y = float((range_y[1] - range_y[0])/n)
    delta_a = float(delta_x*delta_y)
    func_eval = lambda x, y: float(eval(func))

    start_x = range_x[0]
    start_y = range_y[0]

    total = 0.0
    for i in range(0,n+1):
        for j in range(0, n+1):
            total += float(func_eval(start_x + i*delta_x, start_y+ j*delta_y )) * delta_a

    return total
@njit
def add_ufunc(x, y):
    return x + y

@jit(parallel = True)
def sumation(start_x, delta_x, func_2, start_y, delta_y, delta_a, total,n):
    for i in prange(n):
        for j in prange(n):
            total = func_2(add_ufunc(start_x, i*delta_x), add_ufunc(start_y, j*delta_y) ) * delta_a + total
    return total

def integrate2_u(func, range_x, range_y):
    n = 10000
    delta_x = float((range_x[1] - range_x[0])/n)
    delta_y = float((range_y[1] - range_y[0])/n)
    delta_a = float(delta_x*delta_y)


    start_x = float(range_x[0])
    start_y = float(range_y[0])

    total = 0.0
    
    total = sumation(start_x, delta_x, func, start_y, delta_y, delta_a, total,n)

    return total



if __name__ == '__main__':
    time1 = time.time()
    print(integrate2('x**2 + y**2 - 2',(-2, 2), (-2,2)))
    time2 = time.time()
    print('{:s} function took {:.3f} ms'.format(integrate2.__name__, (time2-time1)*1000.0))
    time1 = time.time()
    print(integrate2_u(lambda x,y: eval('x**2 + y**2 - 2'),(-2, 2), (-2,2)))
    time2 = time.time()
    print('{:s} function took {:.3f} ms'.format(integrate2.__name__, (time2-time1)*1000.0))