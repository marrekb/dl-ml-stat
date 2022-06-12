import pandas as pd

df = pd.read_csv('dataset_without_outliers.csv', sep = ';')

print(df.columns)
df = df.drop(['tourney_id', 'draw_size', 'tourney_level',
              'tourney_date', 'p1_name', 'p1_ioc', 'p2_name', 'p2_ioc',
              'score', 'best_of', 'round',
              'w_ace', 'w_df', 'w_svpt', 'w_1stIn', 'w_1stWon', 'w_2ndWon', 'w_SvGms',
              'w_bpSaved', 'w_bpFaced', 'l_ace', 'l_df', 'l_svpt', 'l_1stIn',
              'l_1stWon', 'l_2ndWon', 'l_SvGms', 'l_bpSaved', 'l_bpFaced'], axis = 1)

d_s = {'Clay': 0, 'Hard': 1, 'Carpet': 2, 'Grass': 3}
df['surface'] = df['surface'].map(d_s)

df['p1_ht'] = df['p1_ht'].astype('int64')
df['p2_ht'] = df['p2_ht'].astype('int64')

df['p1_rank'] = df['p1_rank'].astype('int64')
df['p2_rank'] = df['p2_rank'].astype('int64')

df['p1_rank_points'] = df['p1_rank_points'].astype('int64')
df['p2_rank_points'] = df['p2_rank_points'].astype('int64')

df.fillna(0, inplace=True)

df.to_csv('encoded_extended_dataset.csv', sep = ';', index = False)
