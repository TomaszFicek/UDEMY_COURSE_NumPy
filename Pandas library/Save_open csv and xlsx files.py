import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def fetch_financial_data(company='AMZN'):

    # Function which download from stooq.pl website data about split quotation(notowan spolek on stock market
    import pandas_datareader.data as web  # import "data" method from "pandas_datareader" library
    return web.DataReader(name=company, data_source='stooq')  # function return data about AMZN company from stooq web..

df = fetch_financial_data('FB')

# print(df.info())
# print(df.describe())

df.to_csv('fb.csv')  # data export to csv file

df_nov = df[(df.index.month == 11) & (df.index.year == 2019)]

df_nov.to_excel('fb_nov.xlsx')

df_new = pd.read_excel('fb_nov.xlsx')
print(df_new, "\n")
