"""
Utility script aimed to help with managing photo collection
"""

import glob
import shutil
import os
import argparse
import sys
from pathlib import Path


# path constants
CWD = Path(os.getcwd())
LR_EXPORT = CWD / "LR_export"


def pprint(line):
    """ Pretty print line """
    print("\n" + "-"*80)
    print(line)
    print("-"*80)


def extract_lr_export():
    """ Extract all .jpgs from LR_export to CWD """

    file_list = glob.glob(str(LR_EXPORT) + "/*.jpg")

    pprint("Moving files from LR_export")

    for file in file_list:
        shutil.copy(file, CWD)

    pprint("Finished moving files from LR_export")


def remove_nefs():
    """ Remove all NEF files in CWD """

    nef_list = glob.glob(str(CWD) + "/*.NEF")

    # security check
    if not input("Confirm by writing 'yes': ") == "yes":
        return

    pprint("Removing all .NEFs")

    for nef in nef_list:
        os.remove(nef)

    pprint("Finished removing .NEFs")


def configure_parser():
    """ Configures argument parser """

    parser = argparse.ArgumentParser(
        description="Python tool aimed for managing photo collection")

    parser.add_argument("--extract-export", action="store_true",
                        help="Extract all .jpgs from LR_export catalog to CWD")

    parser.add_argument("--remove-nef", action="store_true",
                        help="Remove all .NEF files in the CWD (USE WITH CAUTION!)")

    return parser


# argument handling if run directly
if __name__ == "__main__":

    parser = configure_parser()

    if len(sys.argv) > 1:
        args = parser.parse_args()
    else:
        parser.print_help()
        exit(0)

    if args.extract_export:
        extract_lr_export()

    if args.remove_nef:
        remove_nefs()
