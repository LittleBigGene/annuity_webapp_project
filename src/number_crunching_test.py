import unittest
from number_crunching_modules import NumberCruncher

class NumberCruncher_test(unittest.TestCase):
    def setUpClass(self):
        self.cruncher = NumberCruncher(50,'m',1000)

    def actuarial_PV_test(self):
        self.assertAlmostEqual(0.98203195, self.cruncher.actuarial_PV())

        self.cruncher.update_age(60)

        self.assertAlmostEqual(0.978708033, self.cruncher.actuarial_PV())

if __name__ == '__main__':
    unittest.main()