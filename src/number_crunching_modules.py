class NumberCruncher():

    def __init__(self, age, sex, payment):
        self.age = age
        self.sex = sex
        self.payment = payment

    def update_age(self, age):
        self.age = age
    
    def update_sex(self, sex):
        self.sex = sex

    def update_payment(self, payment):
        self.payment = payment

    def actuarial_PV(self, mortality_rates, discount_rates):
        for x in range (0, len(mortality_rates)):
            tpx_array = np.array(tpx(mortality_rates[:x]))
        return np.inner(tpx_array, discount_rates)

    def life_expectancy(self, mortality_rates):
        for x in range (0, len(mortality_rates)):
            life_array = np.array(tpx(mortality_rates[:x]) * (x + 1))
        return sum(life_array)

    def tpx(self, mortality_rates)
        import numpy as np
        return np.prod((1 - np.array(morality_rates)))


if __name__ == "__main__":
    age = 50
    sex = 'm'
    payment = 1000
    crunch = NumberCruncher(age, sex, payment)

    print('results')