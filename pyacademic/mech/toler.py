"""
IT tolerance calculating script with CLI
"""

import argparse
import sys
from os import system

import pandas as pd
from art import *

from . import DATA_DIR

# path to tolerance table
IT_PATH = DATA_DIR / "it.csv"

# data preparation
df = pd.read_csv(IT_PATH)
its = df.columns.to_list()
its.remove("min")
its.remove("max")


def get_tolerance(dim: float, it: int) -> float:
    """ get IT tolerance value for given dimension in given class

    Args:
        dim (float): tolerated dimension value in mm
        it (int): tolerance class

    Returns:
        float: tolerance value
    """
    # check if it in data
    if str(it) not in its:
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
    toler = df[str(it)][(df["min"] < dim) & (df["max"] >= dim)]

    return round(toler.to_list()[0], 5)


def get_tolerance_str(dim: float, it: int) -> float:
    """ run get_tolerance and print the output with info """
    tolerance = get_tolerance(dim, it)
    print(
        f"Tolerance for dim={dim} [mm] in IT{it} is: {tolerance} [mm]")
    return tolerance


def run_ui():
    """ run interface """
    # clear console
    print("toler.py 2021 v0.1\nInsert \'q\' followed by <ENTER> to exit, or CTRL+C\n")
    print(text2art("TOLER.PY"))

    # program loop
    while True:
        # get dimension from user
        user_dim = input("\nInsert dimension: ").strip()

        if user_dim == 'q':
            break

        # get IT from user
        user_it = input("Insert IT: ").strip()

        if user_it == 'q':
            break

        if not get_tolerance(user_dim, user_it):
            print("\nUnable to calculate, enter values again\n")


parser = argparse.ArgumentParser(
    description="Tolerance value calculator, run without commands for iUI")
parser.add_argument("dimension", type=float, action="store",
                    help="Tolerated dimension value (in mm)")
parser.add_argument("IT_class", action="store", type=int,
                    help="Tolerance class according to IT")
# TODO: add unit handling
# parser.add_argument("--unit", action="store", type=str,
#                     help="unit in which tolerance value will be returned")


def main():
    """ handler function """
    if len(sys.argv) == 1:
        run_ui()
    else:
        args = parser.parse_args()

        get_tolerance_str(args.dimension, args.IT_class)


if __name__ == "__main__":
    main()
