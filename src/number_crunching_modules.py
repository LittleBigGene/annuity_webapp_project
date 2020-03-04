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

    def actuarial_PV(self):
        return 1000

    def life_expectancy(self):
        return 80


if __name__ == "__main__":
    age = 50
    sex = 'm'
    payment = 1000
    crunch = NumberCruncher(age, sex, payment)

    print('results')