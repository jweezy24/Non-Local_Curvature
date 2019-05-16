import unittest
import sys
import integration_lib.parser_west as parser
import integration_lib.function as func
import integration_lib.integrate_func as integrate


class TestFunctionsMethods(unittest.TestCase):
    def setUp(self):
        self.all_funcs = []
        for i in range(1,10):
            tmp = parser.parser(file_path="./working_functs/"+str(i)+".yaml")
            self.all_funcs.append(func.math_function(tmp.args))


    def test_1(self):
        test_integrate = integrate.integral(self.all_funcs[0])
        try:
            print(test_integrate.integrate_region())
        except:
            print(test_integrate.integrate_range())

    def test_2(self):
        test_integrate = integrate.integral(self.all_funcs[1])
        try:
            print(test_integrate.integrate_region())
        except:
            print(test_integrate.integrate_range())


    def test_3(self):
        test_integrate = integrate.integral(self.all_funcs[2])
        try:
            print(test_integrate.integrate_region())
        except:
            print(test_integrate.integrate_range())

    def test_4(self):
        test_integrate = integrate.integral(self.all_funcs[3])
        try:
            print(test_integrate.integrate_region())
        except:
            print(test_integrate.integrate_range())

    def test_5(self):
        test_integrate = integrate.integral(self.all_funcs[4])
        try:
            print(test_integrate.integrate_region())
        except:
            print(test_integrate.integrate_range())

    def test_6(self):
        test_integrate = integrate.integral(self.all_funcs[5])
        try:
            print(test_integrate.integrate_region())
        except:
            print(test_integrate.integrate_range())

    def test_7(self):
        test_integrate = integrate.integral(self.all_funcs[6])
        try:
            print(test_integrate.integrate_region())
        except:
            print(test_integrate.integrate_range())

unittest.main()
