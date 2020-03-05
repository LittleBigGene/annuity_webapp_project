import numpy as np
from mortality_table_module import MortalityTableProvider
from discount_curve_module import DiscountCurveProvider
from swap_rate_module import SwapRateProvider
class NumberCruncher():

    def __init__(self, age, sex, payment, mortality, discount):
        self.age = age
        self.sex = sex
        self.payment = payment
        self.mortality = mortality
        self.discount = discount

    def update_age(self, age):
        self.age = age
    
    def update_sex(self, sex):
        self.sex = sex

    def update_payment(self, payment):
        self.payment = payment


    def actuarial_PV(self):
        for x in range (0, len(self.mortality)):
            tpx = np.prod((1 - np.array(self.mortality)))
            tpx_array = np.array(tpx[:x] )
        return np.inner(tpx_array, self.discount)

    def life_expectancy(self):
        for x in range (0, len(self.mortality)):
            tpx = np.prod((1 - np.array(self.mortality)))
            life_array = np.array(tpx[:x] * (x + 1))
        return sum(life_array)

if __name__ == "__main__":
    age = 50
    sex = 'm'
    payment = 1000

    mtp = MortalityTableProvider()
    mortality = mtp.get_table_from_csv()

    srp = SwapRateProvider()
    swap = srp.get_swap_from_csv()

    dcp = DiscountCurveProvider(tenors = swap['Tenor'], parcurve = swap['Swap'])

    crunch = NumberCruncher(age, sex, payment, mortality, dcp.bootstrap())

    print(crunch.actuarial_PV())