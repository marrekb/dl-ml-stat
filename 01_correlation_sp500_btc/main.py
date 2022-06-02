import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import datetime
sns.set()

# retrieving data from csv files
sp500 = pd.read_csv('data/sp500.csv', sep = ';', index_col = 'Date')
btc = pd.read_csv('data/btc.csv', sep = ';', index_col = 'Date')

# combining columns of close prices
sp500['sp500'] = sp500['Close']
btc['btc'] = btc['Close']
data = pd.concat([sp500['sp500'], btc['btc']], axis = 1)

data = data.dropna()
data['date'] = pd.to_datetime(data.index.values, format='%m/%d/%Y')

# adding new columns in order to get reasonable charts
data['sp500n'] = (data['sp500'] - data['sp500'].min()) / (data['sp500'].max() - data['sp500'].min())
data['btcn'] = (data['btc'] - data['btc'].min()) / (data['btc'].max() - data['btc'].min())

days = [365, 180, 90, 60, 15]
df_result = pd.DataFrame(columns = ['days', 'Pearsons r', 'p-value'])

for day in days:
    new_data = data.loc[data['date'] >= (datetime.datetime.now() - datetime.timedelta(days = day))]
    r, p = stats.pearsonr(new_data['sp500'], new_data['btc'])
    df_result = df_result.append({'days': day, 'Pearsons r': r, 'p-value': p}, ignore_index = True)


    plt.subplots(figsize=(10, 10))
    plt.title('Correlation of BTC and S&P500 in last ' + str(day) + ' days')
    plt.plot(new_data['date'], new_data['sp500n'], label = 'S&P 500')
    plt.plot(new_data['date'], new_data['btcn'], label = 'BTC')
    plt.legend()

    plt.savefig('results/corr_days_' + str(day) + '.png')

df_result['days'] = df_result['days'].astype(int)
df_result.to_csv('results/data.csv')
