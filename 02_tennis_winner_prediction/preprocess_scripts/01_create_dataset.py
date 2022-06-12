import pandas as pd
import os
import numpy as np

data_files = os.listdir('raw_data/')

data_frames = []

for file in data_files:
    data_frames.append(pd.read_csv('raw_data/' + file, sep = ','))

df = pd.concat(data_frames)

df = df.sort_values(by = ['tourney_date', 'match_num'])
df = df.reset_index()

print(df['surface'].value_counts()) #Clay, Hard, Carpet, Grass
print(df['surface'].isna().sum())
df['surface'] = df['surface'].fillna('Clay')

df.to_csv('raw_full_dataset.csv', sep = ';', index = False)
