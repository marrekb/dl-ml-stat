import numpy as np
import pandas as pd
import os

# test comment
def get_driver_probs(year: int, driver: str, count_of_drivers: int, type: str):
    res = np.zeros(count_of_drivers + 1, dtype = np.int)
    path = 'data/season/' + str(year) + '/' + type + '.csv'

    if not os.path.exists(path):
        raise Exception('%s path is not exist' % path)

    data = pd.read_csv(path, sep = ';')

    if driver in data.columns:
        column = data[driver]

        for race in range(data.shape[0]):
            pos = str(column[race])
            if pos.isnumeric():
                pos = int(pos) - 1
                if pos >= count_of_drivers:
                    pos = count_of_drivers - 1
                res[pos] += 1
            else:
                res[count_of_drivers] += 1
        return res, True
    return None, False

def get_driver_series(year: int, driver: str, count_of_drivers: int, type: str):
    path = 'data/season/' + str(year) + '/' + type + '.csv'

    if not os.path.exists(path):
        raise Exception('%s path is not exist' % path)

    data = pd.read_csv(path, sep = ';')

    if driver in data.columns:
        column = data[driver]
        res = np.zeros(data.shape[0], dtype = np.int)

        for race in range(data.shape[0]):
            pos = str(column[race])
            if pos.isnumeric():
                pos = int(pos) - 1
                if pos >= count_of_drivers:
                    pos = count_of_drivers - 1
                res[race] = pos
            else:
                res[race] = count_of_drivers
        return res, True
    return None, False
