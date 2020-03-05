import unittest
import pandas as pd
from number_crunching_modules import NumberCruncher
from discount_curve_module import DiscountCurveProvider
class NumberCruncher_test(unittest.TestCase):
    def setUpClass(self):
        mort = pd.read_csv('./src/mortality.csv')
        swap = pd.read_csv('./src/swaps.csv')
        dcp = DiscountCurveProvider(tenors = swap['Tenor'], parcurve = swap['Swap'])
        self.cruncher = NumberCruncher(50,'m',1000, mort, dcp.bootstrap())

    def test_actuarial_PV(self):
        self.assertAlmostEqual(0.98203195, self.cruncher.actuarial_PV())

        self.cruncher.update_age(60)
        self.assertAlmostEqual(0.978708033, self.cruncher.actuarial_PV())

if __name__ == '__main__':
    unittest.main()