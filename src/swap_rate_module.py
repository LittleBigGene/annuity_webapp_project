import pandas as pd

class SwapRateProvider():

    def get_swap_rates(self):
        print('not implemented yet')

    def get_swap_from_csv(self):
        return pd.read_csv('./src/swaps.csv')


if __name__ == "__main__":
    srp = SwapRateProvider()

    print(srp.get_swap_from_csv())