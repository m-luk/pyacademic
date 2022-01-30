import argparse
import os
import sys
from pathlib import Path

import pandas as pd
from pandas import DataFrame

SCRIPT_PATH = Path(os.path.realpath(__file__))
SCRIPT_DIR = SCRIPT_PATH.parent


def load_threads():
    """ loads threads database to global scope """
    global threads_df
    threads_df = pd.read_csv(SCRIPT_DIR / "mthreads.csv", index_col=0,)


def match_thread_min_diam(diam: float, give_n: int = 1) -> DataFrame:
    """ calulates thread for given minimum core diameter"""
    return threads_df[threads_df.d3 >= diam].head(give_n)


parser = argparse.ArgumentParser(
    description="MTREAD\nmatches threads to requested minimal core diameter")

parser.add_argument("core", type=float,
                    help="Minimal diameter of threads core")
parser.add_argument("--matches", action="store", default=5, type=int,
                    help="how many matching threads to show, in d3 ascending order (default 5)")


def main():
    load_threads()
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        print(match_thread_min_diam(args.core, args.matches))


if __name__ == "__main__":
    main()