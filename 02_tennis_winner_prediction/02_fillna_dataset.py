import pandas as pd

def fill_row(row, first_column, second_column, default_value):
    if pd.isna(row[first_column]):
        if pd.isna(row[second_column]):
            row[first_column] = default_value
            row[second_column] = default_value
        else:
            row[first_column] = row[second_column]
    else:
        if pd.isna(row[second_column]):
            row[second_column] = row[first_column]
    return row

def replace_hand(row):
    if row['winner_hand'] == 'A':
        if row['loser_hand'] == 'A':
            row['winner_hand'] = 'R'
            row['loser_hand'] = 'R'
        else:
            row['winner_hand'] = row['loser_hand']
    else:
        if row['loser_hand'] == 'A':
            row['loser_hand'] = row['winner_hand']
    return row

if __name__ == '__main__':
    columns = ['surface', 'tourney_date', 'winner_id', 'winner_name', 'winner_hand',
               'winner_ht', 'winner_age', 'loser_id', 'loser_name', 'loser_hand',
               'loser_ht', 'loser_age', 'round', 'winner_rank', 'winner_rank_points',
               'loser_rank', 'loser_rank_points']
    df = pd.read_csv('raw_full_dataset.csv', sep = ';')

    df = df[columns]

    print('hand A')
    df = df.apply(lambda x: replace_hand(x), axis = 1)
    print('hand')
    df = df.apply(lambda x: fill_row(x, 'winner_hand', 'loser_hand', 'R'), axis = 1)
    print('ht')
    df = df.apply(lambda x: fill_row(x, 'winner_ht', 'loser_ht', 0.0), axis = 1)
    print('age')
    df = df.apply(lambda x: fill_row(x, 'winner_age', 'loser_age', 0.0), axis = 1)
    print('rank')
    df = df.apply(lambda x: fill_row(x, 'winner_rank', 'loser_rank', 0.0), axis = 1)
    print('points')
    df = df.apply(lambda x: fill_row(x, 'winner_rank_points', 'loser_rank_points', 0.0), axis = 1)

    '''

    df = df.loc[df['tourney_date'] > 20000000]
    df = df.reset_index()
    '''

    print('cut by date')
    print(df.isna().sum())
    print(df['winner_hand'].value_counts())
    print(df['loser_hand'].value_counts())

    df.to_csv('filled_dataset.csv', sep = ';', index = False)
