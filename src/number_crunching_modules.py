import numpy as np
class NumberCruncher():

    def __init__(self, age, sex, payment, mortality):
        self.age = age
        self.sex = sex
        self.payment = payment
        self.mortality = mortality

    def update_age(self, age):
        self.age = age
    
    def update_sex(self, sex):
        self.sex = sex

    def update_payment(self, payment):
        self.payment = payment

    def actuarial_PV(self, discount_rates):
        for x in range (0, len(self.mortality)):
            tpx = np.prod((1 - np.array(self.mortality)))
            tpx_array = np.array(tpx[:x] )
        return np.inner(tpx_array, discount_rates)

    def life_expectancy(self):
        for x in range (0, len(self.mortality)):
            tpx = np.prod((1 - np.array(self.mortality)))
            life_array = np.array(tpx[:x] * (x + 1))
        return sum(life_array)

if __name__ == "__main__":
    age = 50
    sex = 'm'
    payment = 1000
    crunch = NumberCruncher(age, sex, payment)

    print('results')