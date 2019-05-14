import integration_lib.parser_west as parser
import integration_lib.function as func

check_parse = parser.parser()

print(check_parse.args)

test_func = func.math_function(check_parse.args["args"]["function"])

print(test_func.run_func([2,1]))
