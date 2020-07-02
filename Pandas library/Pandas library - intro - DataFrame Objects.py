import pandas as pd
import numpy as np
np.set_printoptions(precision=4, suppress=True)

"""
df = pd.DataFrame(data=[12, 13, 14], index=['first', 'second', 'third'], columns=['col_1'])
print(df, "\n")

df1 = pd.DataFrame({'WIG20': ['PKN ORLEN', 'PKO BP'],
                    'mWIG40': ['Amica', 'Playway']})
print(df1, "\n")

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

df = pd.DataFrame(data=[[12, 13, 14], [14, 15, 16]], index=['first', 'second'], columns=['col_1', 'col_2', 'col_3'])
print(df, "\n")

print(df.index, '\n')
print(df.columns, '\n')
print(df.values, '\n')
print(df.info, '\n')
print(df.describe(), '\n')
print(df.describe().T, '\n')
"""
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

df = pd.DataFrame(data=[[10, 12, 13], [23, 12, 10]], index=["first", 'second'], columns=['col_1', 'col_2', 'col_3'])
print(df, "\n")

print(df['col_1'], "\n")  # cutting first column from df object - cutted column is "Series" type
print(df[['col_1']], "\n")  # cutting first column from df object - cutted column is "DataFrame" type

df.columns = ['a', 'b', 'c']  # changing name of columns
print(df, "\n")

print(df.b, '\n')  # fastest way to cutting columns - "df."name_of_column"

df['a+c'] = df.a + df.c  # adding new column which will be sum of column a and column c
print(df, "\n")

print(df.loc['second', 'a+c'], "\n")  # "loc" method is uses to cutting variable from DataFrame by give name of index..
# .. and name of column

print(df.iloc[1, 0], "\n")  # "iloc" method is uses to cutting variable from DataFrame by give number of index..
# .. and number of column
