import numpy as np
import pandas as pd


print('Numpy:', np.__version__)
print('Pandas:', pd.__version__)

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def fetch_financial_data(company='AMZN'):

    # Function which download from stooq.pl website data about split quotation(notowan spolek on stock market
    import pandas_datareader.data as web  # import "data" method from "pandas_datareader" library
    return web.DataReader(name=company, data_source='stooq')  # function return data about AMZN company from stooq web..

"""
df = fetch_financial_data()  # aligning data from above function to "df" fariable - becomes a "DataFrame" object
print(df, "\n")

df.head(10)
print(df.head(10), "\n")  # "head" method allows show only 10 (in this situation) rows

print(df.tail(10), "\n")  # "tail" method allows show last 10 (in this situation) rows

df.columns = [col.lower() for col in df.columns]  # "col.lower()" method change every name of columns to low letter

print(df.head(5), "\n")

df = df.head(10)
print(df, '\n')

print(df[['open', 'close']], '\n')  # cutting all rows from columns "open" and "close" (we get DataFrame object)

print(df.iloc[2:5, [3]], '\n')  # cutting by "iloc" method (cutting by index number of rows and columns) - in this...
# situation cut rows from 2 to 4 and third column

print(df.sort_values(by=['low'], ascending=False), '\n')  # sorting by columns(values) "low" descending(malejąco)
"""
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

df = fetch_financial_data("UBER")  # download data about UBER company by use "fetch_financial_data("UBER")" function

print(df.info())
print(df.describe().T)

df['Average'] = (df.Open + df.Close)/2.0  # adding new column "Average" to DataFrame object
print(df, "\n")

df = df.sort_index()  # sorting by index (from oldest to youngest date)
print(df.head(), "\n")

df['Close_shift'] = df.Close.shift(1)  # adding new column "Close_shift" / "shift()" method is uses to move down data..
# .. In this case data from column Close are moved one place down
print(df.head(), "\n")

df['Daily_change'] = df.Close / df.Close_shift - 1

print(df.head(), "\n")

print(df.Daily_change.min(), "\n")  # displaying the biggest drop of shares of stock(spadek akcji gieldowych)

print(df.Daily_change.max(), "\n")  # displaying the biggest increase of shares of stock(zwrost akcji gieldowych)

print(df[(df.index >= '2019-05-10') & (df.index <= '2019-06-10')])  # filtration object by index - used AND (&) condit..

print(df[df.index.month == 5])  # filtration object by index by "month" method - displaying all records from may
