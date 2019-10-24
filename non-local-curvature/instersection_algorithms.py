import math
import time
import numpy as np
import sys
from numba import jit, njit, prange, generated_jit


@njit(parallel=True)
def calculate_intersections(domain, p):
    intersections = 0
    for pos in range(0,len(domain)):
        if pos < len(domain)-1:
            point_1 = domain[pos]
            point_2 = domain[pos+1]
            u = (point_1[0] - point_2[0], point_1[1]- point_2[1])
            negative_u = (point_2[0] - point_1[0], point_2[1]- point_1[1])
            v_1 = (point_1[0] - p[0], point_1[1]- p[1])
            v_2 = (point_2[0] - p[0], point_2[1]- p[1])
            v_dot = v_1[0]*v_2[0] + v_1[1]*v_2[1]
            u_dot_1 = negative_u[0] * v_1[0] + negative_u[1] * v_1[1]
            u_dot_2 = u[0] * v_2[0] + u[1] * v_2[1]
            if v_dot > 0 and u_dot_1 > 0 and -1*u_dot_2 > 0:
                intersections += 1
    return intersections

_eps = 0.00001
_huge = sys.float_info.max
_tiny = sys.float_info.min
 
@njit(parallel=True)
def ray_casting_alg(domain, p, prior_intersections, min_max):
    global _eps
    global _huge
    global _tiny

    intersect = prior_intersections
    x_max = min_max[0]
    y_max = min_max[1]
    x_min = min_max[2]
    y_min = min_max[3]

    if p[0] < x_min or p[1] < y_min:
        return 0
            
    if p[0] > x_max or p[1] > y_max:
        return 0

    for pos in range(0, len(domain)):
        if pos < len(domain)-1:
            p_1 = domain[pos]
            p_2 = domain[pos+1]
            if p_1[1] > p_2[1]:
                p_1 = p_2
                p_2 = p_1
            if p[1] == p_1[1] or p[1] == p_2[1]:
                p = (p[0], p[1] + _eps)

        
            if (p[1] > p_1[1] or p[1] <  p_2[1]) or (p[0] > max(p_1[0], p_2[0])):
                pass                
        
            if p[0] < min(p_1[0], p_2[0]):
                intersect += 1
            else:
                if abs(p_1[0] - p_2[0]) > _tiny:
                    m_red = (p_2[1] - p_1[1]) / (float(p_2[0] - p_1[0]))
                else:
                    m_red = _huge
                if abs(p_1[0] - p[0]) > _tiny:
                    m_blue = (p[1] - p_1[1]) / (float(p[0] - p_1[0]))
                else:
                    m_blue = _huge
                if m_blue >= m_red:
                    intersect += 1
    return intersect



@njit(parallel=True)
def bounding_box_algorithm(domain, p, prior_intersections, min_max):
    intersections = prior_intersections
    left_int = False
    right_int = False
    last_intersection = 0
    x_max = min_max[0]
    y_max = min_max[1]
    x_min = min_max[2]
    y_min = min_max[3]
    y_tolerence = .00000001

    if p[0] < x_min or p[1] < y_min:
        return 0
            
    if p[0] > x_max or p[1] > y_max:
        return 0

    for pos in range(0,len(domain)):
        if pos < len(domain)-1:
            point_1 = domain[pos]
            point_2 = domain[pos+1]
            
            if point_1[1] > point_2[1]:
                w_y = point_1[1]
                w = point_1
                v_y = point_2[1]
                v = point_2
            else:
                w_y = point_2[1]
                w = point_2
                v_y = point_1[1]
                v = point_1
        
            w_v = (w[0]-v[0], w[1]- v[1])
            p_v = (p[0]-v[0], p[1]-v[1])
            dot_prod = w_v[0] * p_v[0] + w_v[1]*p_v[1]

            #print(p)
            #print(dot_prod)
            #print(intersections)

            if v[1] <= p[1] and p[1] < w[1] and dot_prod > 0:
                intersections += 1

            elif w[1] <= p[1] and p[1] < v[1] and dot_prod <= 0:
                intersections -=1

    return intersections

@njit(parallel = True)
def winding_num(p,domain,total, min_max):

    x_max = min_max[0]
    y_max = min_max[1]
    x_min = min_max[2]
    y_min = min_max[3]

    if p[0] < x_min or p[1] < y_min:
        return 0
            
    if p[0] > x_max or p[1] > y_max:
        return 0

    for pos in range(0,len(domain)):
        if pos < len(domain)-1:
            point_1 = domain[pos]
            point_2 = domain[pos+1]
            vector_diff_1 = (point_1[0] - p[0], point_1[1]- p[1])
            vector_diff_2 = ( point_2[0] - p[0], point_2[1]- p[1])
            dot_prod = vector_diff_1[0]*vector_diff_2[0] + vector_diff_1[1]*vector_diff_2[1]
            calculation = np.arccos(dot_prod/(np.sqrt(vector_diff_1[0]**2 + vector_diff_1[1]**2) * np.sqrt(vector_diff_2[0]**2 + vector_diff_2[1]**2)))
            total += calculation
    return total

    

def create_domain(func_x, func_y):
        x_eval = lambda t: eval(func_x)
        y_eval = lambda t: eval(func_y)
        points = []
        for angle in range(0,361):
            points.append((x_eval((angle*np.pi)/180),y_eval((angle*np.pi)/180)))
        return points

if __name__ == "__main__":

    domain = create_domain("2*np.cos(t)", "2*np.sin(t)")

    print(bounding_box_algorithm(domain, (-6,1)))
        

        
