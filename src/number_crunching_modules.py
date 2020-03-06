import numpy as np

class NumberCruncher():

    def __init__(self, age, sex, payment, mortality, discount):
        self.age = max(min(age,120),0)
        self.sex = sex
        self.payment = max(payment,0)
        self.mortality = np.asarray(mortality)
        self.discount = np.asarray(discount)
        self.max_age = 120

    def update_age(self, age):
        self.age = max(min(age,120),0)
    
    def update_sex(self, sex):
        self.sex = sex

    def update_payment(self, payment):
        self.payment = max(payment,0)

    def actuarial_PV(self):
        qx_fromage = self.mortality[self.age:]
        tpx = np.cumprod(1 - qx_fromage)[:self.max_age]
        dfs = np.asarray(self.discount[:len(qx_fromage)])
        return self.payment * (tpx @ dfs)

    def life_expectancy(self):
        qx_fromage = self.mortality[self.age:]
        tpx = np.cumprod(1 - qx_fromage)
        surv_to_ages = np.arange(self.age, self.age + len(tpx))
        return qx_fromage[0] * surv_to_ages[0] \
        + (tpx[:-1] * qx_fromage[1:]) @ surv_to_ages[1:] \
        + tpx[-1] * 1 * (surv_to_ages[-1] + 1)