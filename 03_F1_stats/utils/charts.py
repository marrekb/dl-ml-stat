import numpy as np
import matplotlib.pyplot as plt

def show_bar(categories, values, title = '', xlabel = '', ylabel = ''):
    plt.bar(categories, values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def set_ax(ax, title = '', xlabel = '', ylabel = ''):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

def show_report_bars(categories, values, driver: str, seasson: int):
    fig, ax = plt.subplots(2, 2, figsize = (20, 10))

    ax[0, 0].bar(categories, values[0])
    set_ax(ax[0, 0], 'results', 'positions', 'counts')

    ax[0, 1].bar(categories, values[1])
    set_ax(ax[0, 1], 'lab by lap', 'positions', 'percent [%]')

    ax[1, 0].bar(categories, values[2])
    set_ax(ax[1, 0], 'qualifications', 'positions', 'counts')

    ax[1, 1].set_yticks(range(0, len(categories), 1))
    ax[1, 1].set_yticklabels([categories[i] for i in range(0, len(categories), 1)])

    set_ax(ax[1, 1], 'time series', 'races', 'positions')


    races = np.arange(len(values[3][0]), dtype = np.int) + 1
    ax[1, 1].scatter(races, values[3][0], label = 'results')
    ax[1, 1].scatter(races, values[3][2], label = 'starting grids')
    ax[1, 1].scatter(races, values[3][1], label = 'qualifications')

    ax[1, 1].legend(loc = 'upper left')

    fig.suptitle('Report, season ' + str(seasson) + ', driver ' + driver)
