import pandas as pd
import numpy as np

def switch_values(df, idx2, column1, column2):
    data1 = df[column1][idx2].copy()
    data2 = df[column2][idx2].copy()

    df[column1][idx2] = data2
    df[column2][idx2] = data1

df = pd.read_csv('computed_dataset.csv', sep = ';')

print(df.shape[0])

#df = df.drop(['index'], axis = 1)

df.columns = df.columns.str.replace('winner', 'p1')
df.columns = df.columns.str.replace('loser', 'p2')

print(df.columns)

c = df.shape[0]
print('count', c)

df['win'] = 0

np.random.seed(42)
idx = np.random.permutation(c)

mid = c // 2

idx2 = idx[mid:]

df['win'][idx2] = 1

for column in df.columns:
    if column.find('p1') > -1:
        switch_values(df, idx2, column, column.replace('p1', 'p2'))

print(df['win'].value_counts())

df.to_csv('extended_dataset.csv', sep = ';', index = False)
