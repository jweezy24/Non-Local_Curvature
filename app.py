import integration_lib.parser_west as parser
import integration_lib.function as func
import integration_lib.integrate_func as integrate

check_parse = parser.parser()

print(check_parse.args)

test_func = func.math_function(check_parse.args)

print(test_func.run_func([2,1]))

print(test_func.intersections)

test_integrate = integrate.integral(test_func)

print(test_integrate.integrate_region())
