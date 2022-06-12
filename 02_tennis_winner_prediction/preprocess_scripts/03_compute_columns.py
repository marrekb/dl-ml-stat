import pandas as pd
import numpy as np
import datetime

class Player:
    def __init__(self):
        self.wins = np.zeros(4)
        self.losses = np.zeros(4)

        self.win_streak = 0
        self.loss_streak = 0

        self.last_tourney_date = None

        self.games = []

        self.ace = []
        self.df = []
        self.svpt = []
        self.firstIn = []
        self.firstWon = []
        self.secondWon = []
        self.svGms = []
        self.bpSaved = []
        self.bpFaced = []

def fill_df(df, row, win, surface, tourney_date, player, prefix):
    if player.last_tourney_date is None:
        days = 0
    else:
        days = (tourney_date - player.last_tourney_date).days
    player.last_tourney_date = tourney_date

    df[prefix + '_cl_wins'][row] = player.wins[0]
    df[prefix + '_ha_wins'][row] = player.wins[1]
    df[prefix + '_ca_wins'][row] = player.wins[2]
    df[prefix + '_gr_wins'][row] = player.wins[3]

    df[prefix + '_cl_losses'][row] = player.losses[0]
    df[prefix + '_ha_losses'][row] = player.losses[1]
    df[prefix + '_ca_losses'][row] = player.losses[2]
    df[prefix + '_gr_losses'][row] = player.losses[3]

    df[prefix + '_win_streak'][row] = player.win_streak
    df[prefix + '_loss_streak'][row] = player.loss_streak
    df[prefix + '_last_tourney_date'][row] = days

    for n in [5, 10]:
        df[prefix + '_matches' + str(n)][row] = np.array(player.games)[-n:].sum()
        df[prefix + '_ace' + str(n)][row] = np.array(player.ace)[-n:].mean()
        df[prefix + '_df' + str(n)][row] = np.array(player.df)[-n:].mean()
        df[prefix + '_svpt' + str(n)][row] = np.array(player.svpt)[-n:].mean()
        df[prefix + '_firstIn' + str(n)][row] = np.array(player.firstIn)[-n:].mean()
        df[prefix + '_firstWon' + str(n)][row] = np.array(player.firstWon)[-n:].mean()
        df[prefix + '_secondWon' + str(n)][row] = np.array(player.secondWon)[-n:].mean()
        df[prefix + '_svGms' + str(n)][row] = np.array(player.svGms)[-n:].mean()
        df[prefix + '_bpSaved' + str(n)][row] = np.array(player.bpSaved)[-n:].mean()
        df[prefix + '_bpFaced' + str(n)][row] = np.array(player.bpFaced)[-n:].mean()

    if win:
        player.win_streak += 1
        player.loss_streak = 0
        player.wins[surface] += 1
        player.games.append(1)
    else:
        player.loss_streak += 1
        player.win_streak = 0
        player.losses[surface] += 1
        player.games.append(-1)

    c = 'w' if win else 'l'
    player.ace.append(df[c + '_ace'][row])
    player.df.append(df[c + '_df'][row])
    player.svpt.append(df[c + '_svpt'][row])
    player.firstIn.append(df[c + '_1stIn'][row])
    player.firstWon.append(df[c + '_1stWon'][row])
    player.secondWon.append(df[c + '_2ndWon'][row])
    player.svGms.append(df[c + '_SvGms'][row])
    player.bpSaved.append(df[c + '_bpSaved'][row])
    player.bpFaced.append(df[c + '_bpFaced'][row])

d_s = {'Clay': 0, 'Hard': 1, 'Carpet': 2, 'Grass': 3}

df = pd.read_csv('filled_dataset.csv', sep = ';')
df = df.drop(['index', 'tourney_name', 'match_num', 'winner_seed', 'winner_entry', 'loser_entry', 'loser_seed', 'minutes'], axis = 1)

for prefix in ['winner', 'loser']:
    df[prefix + '_cl_wins'] = 0
    df[prefix + '_ha_wins'] = 0
    df[prefix + '_ca_wins'] = 0
    df[prefix + '_gr_wins'] = 0

    df[prefix + '_cl_losses'] = 0
    df[prefix + '_ha_losses'] = 0
    df[prefix + '_ca_losses'] = 0
    df[prefix + '_gr_losses'] = 0

    df[prefix + '_win_streak'] = 0
    df[prefix + '_loss_streak'] = 0
    df[prefix + '_last_tourney_date'] = 0 #days

    for n in [5, 10]:
        df[prefix + '_matches' + str(n)] = 0
        df[prefix + '_ace' + str(n)] = 0
        df[prefix + '_df' + str(n)] = 0
        df[prefix + '_svpt' + str(n)] = 0
        df[prefix + '_firstIn' + str(n)] = 0
        df[prefix + '_firstWon' + str(n)] = 0
        df[prefix + '_secondWon' + str(n)] = 0
        df[prefix + '_svGms' + str(n)] = 0
        df[prefix + '_bpSaved' + str(n)] = 0
        df[prefix + '_bpFaced' + str(n)] = 0

players = {}

c = df.shape[0]
print(c)
f = float(c)
for i in range(c):
    if i % 1000 == 0:
        print(100 * i/f)

    winner_id = df['winner_id'][i]
    surface = d_s[df['surface'][i]]
    date = datetime.datetime.strptime(str(df['tourney_date'][i]), '%Y%m%d')

    if winner_id in players:
        player = players[winner_id]
    else:
        player = Player()
        players[winner_id] = player
    fill_df(df, i, True, surface, date, player, 'winner')

    loser_id = df['loser_id'][i]
    if loser_id in players:
        player = players[loser_id]
    else:
        player = Player()
        players[loser_id] = player
    fill_df(df, i, False, surface, date, player, 'loser')

df = df.loc[df['tourney_date'] > 20000000]
df = df.reset_index()

df = df.drop(['index'], axis = 1)
'''
df['winner_ht'] = df['winner_ht'].astype('int64')
df['loser_ht'] = df['loser_ht'].astype('int64')

df['winner_rank'] = df['winner_rank'].astype('int64')
df['loser_rank'] = df['loser_rank'].astype('int64')

df['winner_rank_points'] = df['winner_rank_points'].astype('int64')
df['loser_rank_points'] = df['loser_rank_points'].astype('int64')
'''
print(df.dtypes)

df.to_csv('computed_dataset.csv', sep = ';', index = False)
