class NumberCruncher():
    
    def __init__(self, age, sex, payment_amt):
        self.age = age
        self.sex = sex
        self.payment_amt = payment_amt 

    def actuarial_PV(self):
        return 1000

    def life_expectancy(self):
        return 80


if __name__ == "__main__":
    age = 33
    sex = 'female'
    payment_amt = [1,1,1,1,1,1,1]
    crunch = NumberCruncher(age, sex, payment_amt)

    print('results')