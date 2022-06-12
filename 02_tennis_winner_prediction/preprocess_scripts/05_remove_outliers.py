import pandas as pd

df = pd.read_csv('extended_dataset.csv', sep = ';')

print('last_tourney_date', df.loc[df['p1_last_tourney_date'] > 1000].shape[0], df.loc[df['p2_last_tourney_date'] > 1000].shape[0])

print('svpt5', df.loc[df['p1_svpt5'] > 200].shape[0], df.loc[df['p2_svpt5'] > 200].shape[0])

print('svpt10', df.loc[df['p1_svpt10'] > 150].shape[0], df.loc[df['p2_svpt10'] > 150].shape[0])

print('firstIn5', df.loc[df['p1_firstIn5'] > 150].shape[0], df.loc[df['p2_firstIn5'] > 150].shape[0])

print('firstIn10', df.loc[df['p1_firstIn10'] > 100].shape[0], df.loc[df['p2_firstIn10'] > 100].shape[0])

df = df.loc[df['p1_last_tourney_date'] < 1000]
df = df.loc[df['p2_last_tourney_date'] < 1000]

print(df.shape[0])

df.to_csv('dataset_without_outliers.csv', sep = ';', index = False)
