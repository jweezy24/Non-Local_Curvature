import unittest
import sys
import integration_lib.parser_west as parser
import integration_lib.function as func
import integration_lib.integrate_func as integrate
import numpy as np


class TestFunctionsMethods(unittest.TestCase):
    def setUp(self):
        self.all_funcs = []
        for i in range(1,13):
            tmp = parser.parser(file_path="./working_functs/"+str(i)+".yaml")
            self.all_funcs.append(func.math_function(tmp.args))


    def test_1(self):
        test_integrate = integrate.integral(self.all_funcs[0])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))


    def test_2(self):
        test_integrate = integrate.integral(self.all_funcs[1])
        try:
            tmp = test_integrate.integrate_region()
        except:
            print(test_integrate.integrate_range())


    def test_3(self):
        test_integrate = integrate.integral(self.all_funcs[2])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))


    def test_4(self):
        test_integrate = integrate.integral(self.all_funcs[3])
        try:
            tmp = test_integrate.integrate_region()
        except:
            print(test_integrate.integrate_range())

    def test_5(self):
        test_integrate = integrate.integral(self.all_funcs[4])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))


    def test_6(self):
        test_integrate = integrate.integral(self.all_funcs[5])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))


    def test_7(self):
        test_integrate = integrate.integral(self.all_funcs[6])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], 11136)
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], 11136)

    def test_8(self):
        test_integrate = integrate.integral(self.all_funcs[7])
        try:
            tmp = test_integrate.integrate_region()
            print(type(tmp))
            self.assertEqual(type(tmp), type((1,2)))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))


    def test_9(self):
        test_integrate = integrate.integral(self.all_funcs[8])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))

    def test_10(self):
        test_integrate = integrate.integral(self.all_funcs[9])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))

    def test_11(self):
        test_integrate = integrate.integral(self.all_funcs[10])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], np.pi)
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], np.pi)

    def test_12(self):
        test_integrate = integrate.integral(self.all_funcs[11])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], 4811.4)
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], 4811.4)


unittest.main()
