import csv
import pandas as pd

df = pd.read_csv("dwarf_stars.csv")
print(len(df))
df = df.dropna()
print(len(df))
print(df.dtypes)

df['Mass'] = df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df['Mass'] = df['Mass'] * 0.000954588
df['Radius'] = df['Radius'] * 0.102763

df.drop(['Unnamed: 0'], axis=1, inplace=True)

df.to_csv("sorted_dwarf_stars.csv")
