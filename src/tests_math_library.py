import math_librabry
import unittest


class TestAddition(unittest.TestCase):

    def test_add_two(self):
        self.assertEqual(math_librabry.addition(1, 2), 4,)

    def test_add_more(self):
        self.assertEqual(math_librabry.addition(1, 4, 8, 10, 2 ,-3), 22)

    def test_add_two_float(self):
        self.assertEqual(math_librabry.addition(1.3, 1.4), 2.7)

class TestSubtraction(unittest.TestCase):

    def test_sub_two(self):
        self.assertEqual(math_librabry.subtraction(4, 3), 1)

    def test_sub_more(self):
        self.assertEqual(math_librabry.subtraction(15, 4, 2, 1, -3), 11)

    def test_sub_two_float(self):
        self.assertEqual(math_librabry.subtraction(4.8, 3.2), 1.6)

class TestDivision(unittest.TestCase):

    def test_div_two(self):
        self.assertEqual(math_librabry.division(10, 2), 5)
        self.assertEqual(math_librabry.division(-10, 2), -5)

    def test_div_more(self):
        self.assertEqual(math_librabry.division(16, 2, 4), 2)

    def test_div_two_float(self):
        self.assertEqual(math_librabry.division(5, 3), 1.667)

class TestMultiplication(unittest.TestCase):

    def test_mul_two(self):
        self.assertEqual(math_librabry.multiplication(2, 8), 16)
        self.assertEqual(math_librabry.multiplication(-30, 2), -60)

    def test_mul_more(self):
        self.assertEqual(math_librabry.multiplication(3, 4, 4), 48)
        self.assertEqual(math_librabry.multiplication(3, 4, -4), -48)

    def test_mul_two_float(self):
        self.assertEqual(math_librabry.multiplication(4.3, 2.6), 11.18)


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(math_librabry.factorial(4), 24)

    def test_incorrect_factorial(self):
        self.assertEqual(math_librabry.factorial(-3), None)
        self.assertEqual(math_librabry.factorial(3.3), None)

class TestSqrt(unittest.TestCase):

    def test_2sqrt(self):
        self.assertEqual(math_librabry.sqrt(4, 2), 2)
        self.assertEqual(math_librabry.sqrt(-2), None)

    def test_bigger_sqrt(self):
        self.assertEqual(math_librabry.sqrt(16, 4), 2)
        self.assertEqual(math_librabry.sqrt(8, 3), 2)
        self.assertEqual(math_librabry.sqrt(-8, 3), None)

    def test_float_sqrt(self):
        self.assertAlmostEqual(math_librabry.sqrt(8.8, 2), 2.96647, delta=0.00001)


class TestExponent(unittest.TestCase):

    def test_2exponent(self):
        self.assertEqual(math_librabry.exponent(4, 2), 16)
        self.assertEqual(math_librabry.exponent(4, 0), 1)
        self.assertEqual(math_librabry.exponent(0, 2), 0)

    def test_bigger_exponent(self):
        self.assertEqual(math_librabry.exponent(2, 4), 16)
        self.assertEqual(math_librabry.exponent(2, 5), 32)

    def test_float_exponent(self):
        self.assertAlmostEqual(math_librabry.exponent(2.356, 2), 5.55073, delta=0.00001)
        self.assertAlmostEqual(math_librabry.exponent(2.356, 4), 30.81067, delta=0.00001)


class TestAbs(unittest.TestCase):

    def test_abs(self):
        self.assertEqual(math_librabry.abs(8), 8)
        self.assertEqual(math_librabry.abs(-8), 8)
        self.assertEqual(math_librabry.abs(0), 0)



class TestLogartihm(unittest.TestCase):

    def test_logarithm(self):
        self.assertAlmostEqual(math_librabry.logarithm(4, 3), 1.26185, delta=0.00001)
        self.assertAlmostEqual(math_librabry.logarithm(1, 10), 0, delta=0.00001)
        self.assertAlmostEqual(math_librabry.logarithm(10, 5), 1.43067, delta=0.00001)

    def test_wrong_logarithm(self):
        self.assertEqual(math_librabry.logarithm(3, 0), None)
        self.assertEqual(math_librabry.logarithm(10, 1), None)
        self.assertEqual(math_librabry.logarithm(-10, 1), None)
        self.assertEqual(math_librabry.logarithm(-1, 10), None)



class TestSine(unittest.TestCase):

    def test_sine(self):
        self.assertAlmostEqual(math_librabry.sine(5), 0.0871557, delta=0.00001)
        self.assertAlmostEqual(math_librabry.sine(100), 0.9848077, delta=0.00001)
        self.assertAlmostEqual(math_librabry.sine(-5), 0.0871557, delta=0.00001)
        self.assertAlmostEqual(math_librabry.sine(0), 0, delta=0.00001)


class TestCosine(unittest.TestCase):

    def test_cosine(self):
        self.assertAlmostEqual(math_librabry.cosine(5), 0.9961946, delta=0.00001)
        self.assertAlmostEqual(math_librabry.cosine(100), -0.173648, delta=0.00001)
        self.assertAlmostEqual(math_librabry.cosine(-5), 0.9961946, delta=0.00001)
        self.assertAlmostEqual(math_librabry.cosine(0), 1, delta=0.00001)

class TestTangent(unittest.TestCase):

    def test_tangent(self):
        self.assertAlmostEqual(math_librabry.tangent(5),0.0874886, delta=0.00001)
        self.assertAlmostEqual(math_librabry.tangent(100),-5.6712818, delta=0.00001)
        self.assertAlmostEqual(math_librabry.tangent(-5),-0.0874886, delta=0.00001)
        self.assertAlmostEqual(math_librabry.tangent(0), 0, delta=0.00001)





