"""
IT tolerance calculating script with CLI
"""

import os
import shutil
from math import *
from os import system
from pathlib import Path

import numpy as np
import pandas as pd
import tabulate as tab
from art import *

# path to tolerance table
IT_PATH = Path(os.path.realpath(__file__)).parent / "it.csv"

# data preparation
df = pd.read_csv(IT_PATH)
its = df.columns.to_list()
its.remove("min")
its.remove("max")


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
    toler = df[it][(df["min"] < dim) & (df["max"] >= dim)]

    return round(toler.to_list()[0], 5)


def main():
    # clear console
    _ = system("cls")

    print("toler.py 2021 v0.1\nInsert \'q\' followed by <ENTER> to exit, or CTRL+C\n")
    print(text2art("TOLER.PY"))

    # program loop
    while True:
        # get dimension from user
        dim = input("\nInsert dimension: ").strip()

        if dim == 'q':
            break

        # get IT from user
        it = input("Insert IT: ").strip()

        if it == 'q':
            break

        toler = get_toler(dim, it)

        if toler:
            print("\n Tolerance for dim={} int IT{} is: {} [mm]".format(
                dim,
                it,
                toler
            ))
        else:
            print("\nUnable to calculate, enter values again\n")


if __name__ == "__main__":
    main()