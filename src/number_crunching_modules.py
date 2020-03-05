import numpy as np
from mortality_table_module import MortalityTableProvider
from discount_curve_module import DiscountCurveProvider
from swap_rate_module import SwapRateProvider
class NumberCruncher():

    def __init__(self, age, sex, payment, mortality, discount):
        self.age = age
        self.sex = sex
        self.payment = payment
        self.mortality = np.asarray(mortality)

    def update_age(self, age):
        self.age = age
    
    def update_sex(self, sex):
        self.sex = sex

    def update_payment(self, payment):
        self.payment = payment

    def actuarial_PV(self, discount_rates):
        qx_fromage = self.mortality[self.age:]
        tpx = np.cumprod(1 - qx_fromage)
        dfs = np.asarray(discount_rates[:len(qx_fromage)])
        return 1000 * (tpx @ dfs)

    def life_expectancy(self):
        qx_fromage = self.mortality[self.age:]
        tpx = np.cumprod(1 - qx_fromage)
        surv_to_ages = np.arange(self.age, self.age + len(tpx))
        return qx_fromage[0] * surv_to_ages[0] \
        + (tpx[:-1] * qx_fromage[1:]) @ surv_to_ages[1:] \
        + tpx[-1] * 1 * (surv_to_ages[-1] + 1)


    
