import numpy as np
import pandas as pd
import os

def get_probs(year: int, driver: str, count_of_drivers: int):
    res = np.zeros(count_of_drivers + 1, dtype = np.int)
    path = 'data/lap_by_lap/' + str(year) + '/'

    if not os.path.exists(path):
        raise Exception('%s path is not exist' % path)

    races =  os.listdir(path)

    for race in races:
        data = pd.read_csv(path + race, sep = ';')

        if driver in data.columns:
            column = data[driver]

            for lap in range(data.shape[0]):
                pos = str(column[lap])
                if pos.isnumeric():
                    pos = int(pos) - 1
                    if pos >= count_of_drivers:
                        pos = count_of_drivers - 1
                    res[pos] += 1
                else:
                    res[count_of_drivers] += 1

    sum = res.sum()
    if sum == 0:
        return None, False
    return (100.0 * res) / sum, True
