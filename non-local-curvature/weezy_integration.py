import os
import time
import numpy as np
import winding_number as checker
from numba import vectorize
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
    n = 1000
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

def func_2(func, x,y):
    return float(eval(func))

@generated_jit(nopython=True)
def func_eval_u(func,x,y):
    return lambda func,x,y: func_2

@vectorize(['float64(float64, float64)'], target='cuda')
def add_ufunc(x, y):
    return x + y

@njit(parallel = True)
def integrate2_u(func, range_x, range_y):
    n = 1000
    delta_x = float((range_x[1] - range_x[0])/n)
    delta_y = float((range_y[1] - range_y[0])/n)
    delta_a = float(delta_x*delta_y)

    start_x = float(range_x[0])
    start_y = float(range_y[0])

    total = 0.0
    for i in prange(n):
        for j in prange(n):
            total = float(func_eval_u(func, start_x + i*delta_x, start_y+ j*delta_y )) * delta_a + total

    return total



if __name__ == '__main__':
    time1 = time.time()
    print(integrate2('x**2 + y**2 - 2',(-2, 2), (-2,2)))
    time2 = time.time()
    print('{:s} function took {:.3f} ms'.format(integrate2.__name__, (time2-time1)*1000.0))
    time1 = time.time()
    print(integrate2_u('x**2 + y**2 - 2',(-2, 2), (-2,2)))
    time2 = time.time()
    print('{:s} function took {:.3f} ms'.format(integrate2.__name__, (time2-time1)*1000.0))