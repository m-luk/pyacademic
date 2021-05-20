import pandas as pd
import numpy as np
from math import *
from os import system
from art import *

# data preparation
df = pd.read_csv('it.csv')
its = df.columns.to_list()
its.remove('min')
its.remove('max')


def get_toler(dim, it):
    ''' 
    Returns International Tolerance value for given dimension(dim) and class(it) 
    '''
    # check if it in data
    if it not in its:
        print("#### IT not supported ####\n")
        return False

    # check if dimension correct
    try:
        dim = float(dim)
    except ValueError as err:
        print('#### Dimension inserted is not a number ####\n')
        return False

    if dim <= 0 or dim > 3150:
        print("#### Dimension not supported ####\n")
        return False

    # get toler value
    toler = df[it][(df['min'] < dim) & (df['max'] >= dim)]

    return round(toler.to_list()[0], 5)


if __name__ == "__main__":
    _ = system('cls')

    print('toler.py 2021 v0.1\nInsert \'q\' followed by <ENTER> to exit, or CTRL+C\n')

    print(text2art("TOLER.PY"))

    # program loop
    while(1):
        # get dimension from user
        dim = input('\nInsert dimension: ').strip()

        if dim == 'q':
            break

        # get IT from user
        it = input('Insert IT: ').strip()

        if it == 'q':
            break

        toler = get_toler(dim, it)

        if toler:
            print('\n Tolerance for dim={} int IT{} is: {} [mm]'.format(
                dim,
                it,
                toler
            ))
        else:
            print('\nUnable to calculate, enter values again\n')
