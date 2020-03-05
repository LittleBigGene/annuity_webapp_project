import numpy as np
import pandas as pd
import unittest
from discount_curve_module import DiscountCurveProvider
class test_DiscountCurveProvider(unittest.TestCase):

    def setUp(self):
        swap = pd.read_csv('./src/swaps.csv')
        self.dcp = DiscountCurveProvider(tenors = swap['Tenor'], parcurve = swap['Swap'])
        
    def test_bootstrap(self):
        answer = self.dcp.bootstrap()
        self.assertAlmostEqual(0.9842810, answer[0])
        self.assertAlmostEqual(0.9688091, answer[1])

if __name__ == '__main__':
    unittest.main()