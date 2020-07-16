import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

url = 'appstore_games.csv'
df_raw = pd.read_csv(url)

print(df_raw.head(), "\n")

print(df_raw.columns)

df = df_raw.copy()

print(df.info(), "\n")

df = df.drop(columns=['URL', 'Subtitle', 'Icon URL', 'In-app Purchases', 'Description'])  # DROP method is uses to..
# .. delete columns from DataFrame object

print(df, "\n")

df = df.set_index('ID')  # set index as column "ID"
print(df.head(), "\n")

df.columns = [col.lower().replace(' ', '_') for col in df.columns]  # change in all columns capital letter to low ...
# ... ane replace space (' ') sign to '_' sign

print(df.head(), "\n")

print(df.primary_genre.value_counts(), "\n")  # VALUE_COUNTS method allow check how many is each element in column (in this..
# ... casse in column "primary_genre"_

print(df.primary_genre.value_counts().nlargest(5), "\n")  # NLARGEST(5) method allows show top 5 element in searched column

print(df.age_rating.value_counts(), "\n")

# df.age_rating.value_counts().plot()  # PLOT method is uses to generate plot/curve
# plt.show()  # PLT.SHOW is uses to displaying earlier generated plot/curve

# df.age_rating.value_counts().plot(kind='bar')  # KIND='BAR' attribute is uses to generate a bar graph (wykres slupkowy)
# plt.show()

# df.age_rating.value_counts().plot(kind='pie')  # KIND='BAR' attribute is uses to generate a pie chart (wykres kolowy)
# plt.show()

df['lan_numb'] = df.languages.str.split(', ').str.len()  # creating new column "lan_numb" which contains number of ...
# ...languages in each row (each application from Google App store)
print(df.head(), "\n")

print(df.lan_numb.value_counts(), "\n")

print(df.info(), "\n")
print(df.isnull().sum(), "\n")  # creating mask with false if exist data and true when there isn't data
df = df.dropna()  # DROPNA methof delete rows where lost some data
print(df.isnull().sum(), "\n")
print(df.info())



