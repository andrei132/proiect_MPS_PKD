import math
import unittest
import numpy as np
from src.functions import min_leafs
from src.functions import max_leafs
from src.functions import arithmetic_average
from src.functions import geometric_average
# from src.functions import weighted_average
from src.functions import calculate_median
# from src.functions import power_limit
# from src.functions import log_limit
from src.functions import sin_limit


class MyTestCase(unittest.TestCase):
    def test_minleafs(self):
        a = 10
        b = 20
        c = 30
        result = min_leafs(a, b, c)
        self.assertEqual(result, a)

    def test_maxleafs(self):
        a = 10
        b = 20
        c = 30
        result = max_leafs(a, b, c)
        self.assertEqual(result, c)

    def test_arithmetic_average(self):
        a = 10
        b = -20
        c = 40
        d = 0
        result = arithmetic_average(a, b, c, d)
        self.assertEqual(result, (a + b + c + d) / 4)

    def test_geometric_average1(self):
        a = 10
        b = 20
        result = geometric_average(a, b)
        self.assertEqual(result, math.sqrt(a * b))

    def test_geometric_average2(self):
        a = 10
        b = 20
        c = 30
        result = '%.10f' % geometric_average(a, b, c)
        self.assertEqual(result, '%.10f' % math.exp(math.log(a * b * c) / 3))

    # def test_weighted_average(self):
    #     a = 10
    #     b = 20
    #     c = 30
    #     a1 = 1
    #     a2 = 2
    #     a3 = 3
    #     result = '%.2f' % weighted_average((a, b, c), (a1, a2, a3))
    #     self.assertEqual(result, '%.2f' % 23.33)

    def test_calculate_median1(self):
        a = 10
        b = 20
        c = 40
        d = 12
        e = 35
        result = calculate_median((a, b, c, d, e))
        self.assertEqual(result, 20)

    def test_calculate_median2(self):
        a = 10
        b = 20
        c = 40
        d = 12
        result = calculate_median((a, b, c, d))
        self.assertEqual(result, (20 + 12) / 2)

    # def test_power_limit1(self):
    #     a = 13
    #     b = 10
    #     c = 13
    #     d = 12
    #     e = 2
    #     result = power_limit((a, b, c, d), e)
    #     self.assertEqual(result, 1)

    # def test_power_limit2(self):
    #     a = 0.1
    #     b = 0.2
    #     c = 0.3
    #     d = 0.4
    #     e = 2
    #     result = '%.2f' % power_limit((a, b, c, d), e)
    #     self.assertEqual(result, '%.2f' % 0.16)

    # def test_log_limit1(self):
    #     a = np.array([1, 2, 3, 4, 5])
    #     result = log_limit(a)
    #     self.assertEqual(result, 1)

    # def test_log_limit2(self):
    #     a = np.array([0])
    #     result = log_limit(a)
    #     self.assertEqual(result, 0)

    def test_sin_limit1(self):
        a = np.array([[0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]])
        result = sin_limit(a)
        self.assertEqual(result, 0)

    def test_sin_limit2(self):
        a = np.array([-np.pi, -np.pi/2, -np.pi/4])
        result = sin_limit(a)
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()
