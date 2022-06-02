import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
import utils.lapbylap as lapbylap
import utils.report as report
import utils.charts as charts

import seaborn as sns
sns.set()

def acceptable_int(value):
    v = int(value)
    if v <= 0:
        raise argparse.ArgumentTypeError('only positive integers are accepted')
    return v

def check_driver(found):
    if not found:
        raise Exception('Driver {driver} has not been found in season {year}'.format(
            driver = args.driver,
            year = str(args.year)
        ))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year', type = acceptable_int,
                        help = 'season year', default = 2000)
    parser.add_argument('-d', '--driver', type = str, help = 'name of driver',
                        default = 'MSC')
    parser.add_argument('-c', '--count', type = acceptable_int, default = 20,
                        help = 'count of drivers')
    parser.add_argument('-a', '--action', type = str, default = 'd_report',
                        help = 'possible actions: d_report')
    args = parser.parse_args()

    if args.action == 'd_report':
        positions = [str(x + 1) for x in range(args.count)] + ['ab']

        probs0, found0 = report.get_driver_probs(args.year, args.driver, args.count, type = 'r')
        probs1, found1 = lapbylap.get_probs(args.year, args.driver, args.count)
        probs2, found2 = report.get_driver_probs(args.year, args.driver, args.count, type = 'q')

        check_driver(found0 & found1 & found2)

        pos_results, _ = report.get_driver_series(args.year, args.driver, args.count, 'r')
        pos_qualfications, _ = report.get_driver_series(args.year, args.driver, args.count, 'q')
        pos_start_grids, _ = report.get_driver_series(args.year, args.driver, args.count, 's')

        charts.show_report_bars(
            categories = positions,
            values = [probs0, probs1, probs2, [pos_results, pos_qualfications, pos_start_grids]],
            driver = args.driver,
            seasson = args.year
        )
        plt.show()
