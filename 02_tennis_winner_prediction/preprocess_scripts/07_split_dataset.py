import pandas as pd

df = pd.read_csv('encoded_extended_dataset.csv', sep = ';')

mid = df.shape[0] // 2

df1 = df.iloc[:mid]
df2 = df.iloc[mid:]

print(df.shape[0], df1.shape[0], df2.shape[0])

df1.to_csv('enc_ext_dataset1.csv', sep = ';')
df2.to_csv('enc_ext_dataset2.csv', sep = ';')
