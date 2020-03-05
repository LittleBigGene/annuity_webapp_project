import pandas as pd

class MortalityTableProvider():
    def get_table_from_SOA(self):
        print('not implemented yet')

    def get_table_from_csv(self):
        return pd.read_csv('./src/mortality.csv')

if __name__ == "__main__":
    mtp = MortalityTableProvider()

    print(mtp.get_table_from_csv())
    