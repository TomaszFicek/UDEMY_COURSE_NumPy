""" To export/import to excel file should install 2 libraries: OPENPYXL and XLRD """

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

"""

def fetch_financial_data(company='AMZN'):

    # Function which download from stooq.pl website data about split quotation(notowan spolek on stock market
    import pandas_datareader.data as web  # import "data" method from "pandas_datareader" library
    return web.DataReader(name=company, data_source='stooq')  # function return data about AMZN company from stooq web..

df = fetch_financial_data('FB')

# print(df.info())
# print(df.describe())

df.to_csv('fb.csv')  # data export to csv file

df_nov = df[(df.index.month == 11) & (df.index.year == 2019)]

df_nov.to_excel('fb_nov.xlsx')  # data export to excel

df_new = pd.read_excel('fb_nov.xlsx', index_col=0)  # read xlsx data from excel - "index_col" attribute set which column
# .. will be a index column - in this situation first column from excel sheet will be a index in red DataFrame object
print(df_new, "\n")
"""

df = pd.read_csv('london_bike.csv')
print(df.head())
print(df.describe().T)

