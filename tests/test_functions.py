import unittest
import sys
import integration_lib.parser_west as parser
import integration_lib.function as func
import integration_lib.integrate_func as integrate
import numpy as np


class TestFunctionsMethods(unittest.TestCase):
    def setUp(self):
        self.all_funcs = []
        for i in range(1,14):
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
            self.assertEqual(type(tmp), type((1,2)))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))


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
            self.assertEqual(type(tmp), type((1,2)))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))

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
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], -float(8296/13))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], -float(8296/13))


    def test_9(self):
        test_integrate = integrate.integral(self.all_funcs[8])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], 0)
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], 0)

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
            self.assertAlmostEqual(tmp[0], float(24057/5))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], float(24057/5))

    def test_13(self):
        test_integrate = integrate.integral(self.all_funcs[12])
        try:
            tmp = test_integrate.integrate_region()
            self.assertEqual(type(tmp), type(''))
        except:
            tmp = test_integrate.integrate_range()
            self.assertEqual(type(tmp), type((1,2)))
            self.assertAlmostEqual(tmp[0], float(20/3)*np.sin(8))


unittest.main()
