
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: ('%.2f' % x))  # set displaying two number after comma



def fetch_financial_data(company='AMZN'):

    # Function which download from stooq.pl website data about split quotation(notowan spolek on stock market
    import pandas_datareader.data as web  # import "data" method from "pandas_datareader" library
    return web.DataReader(name=company, data_source='stooq')  # function return data about AMZN company from stooq web..



apple = fetch_financial_data('AAPL')
amazon = fetch_financial_data('AMZN')
google = fetch_financial_data('GOOGL')
uber = fetch_financial_data('UBER')

apple.columns = ['apple_' + col.lower() for col in apple.columns]
amazon.columns = ['amazon_' + col.lower() for col in amazon.columns]
google.columns = ['google_' + col.lower() for col in google.columns]
uber.columns = ['uber_' + col.lower() for col in uber.columns]


####################### CONCAT method ###########################

"""
df = pd.concat(objs=[apple, amazon, google, uber], axis=1)
print(df.head(), "\n")  # "concat" method is uses to join DataFrame objects

print(df.describe().T, '\n')

closes = [col for col in df.columns if col.endswith('close')]
print(closes, '\n')
"""

#########################3 APPEND method #########################

print(uber.head(), "\n")

uber_6 = uber[uber.index.month == 6]
uber_7 = uber[uber.index.month == 7]


uber_6_7 = uber_6.append(uber_7)

print(uber_6_7)
