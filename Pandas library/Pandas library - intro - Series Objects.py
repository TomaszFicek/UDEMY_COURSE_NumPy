import pandas as pd
import numpy as np

"""
################ SERIES OBJECT #######################
s = pd.Series(data=[2, 4, 6, 7])
print(s, "\n")

s = pd.Series(data=[2, 4, 6, 7], index=['a', 'b', 'c', 'd'], name='sample')  # declaration of "Series" object from ..
# .. Pandas (pd) library. In this object we can declare for example list od number, we can cal index each element and..
# give a name of this "Series" object
print(s, "\n")

print("^^^^^^^^^^^^^^^")

s = pd.Series(data=[2, np.nan, 6, 7], index=['a', 'b', 'c', 'd'], name='sample')  # "np.nan" is used to filling missing.
# ... data
print(s, "\n")

print("^^^^^^^^^^^^^^^")


s = pd.Series(data=np.arange(10, 20), index=pd.date_range(start='20200701', periods=10), name="data_as_index")
#  in above example indexes are 10 days from 01-07-2020 - "pd.date_range"
print(s, "\n")

print(s.index, "\n")

print(s.values, "\n")
"""

####### WORK WITH SERIES OBJECT ##################

price = pd.Series({"Apple": 200, "CD Projekt": 60, "Amazon": 1900})
print(price, "\n")

print(price["Apple"], "\n")
print(price[1], "\n")

print(price.count(), "\n")  # "count" method give a amount of elements object

print(price.value_counts(), "\n")  # this method is uses to count how many is the same elements in Series object

print(price.describe(), "\n")  # "describe" function give all statistic parameters (mean, max, min, std, var, etc.)

print(price.nlargest(2), "\n")  # "nlargest/nsmallest" method give largest/smallest element from object - as argument..
# .. of this method we give a amount of largest/smallest value od Series object

print(price.rank(), "\n")

print(price.sort_values(), "\n")

print(price.sort_index(), "\n")

price_pln = price.apply(lambda x: x * 3.8)  # "apply" method allows customize created Series object

print(price_pln, "\n")
